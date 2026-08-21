const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const { decode } = require('jpeg-js');

const projectRoot = path.resolve(__dirname, '..');
const assetDirectory = path.join(projectRoot, 'assets', 'offline-proof');
const manifest = JSON.parse(fs.readFileSync(path.join(assetDirectory, 'manifest.json'), 'utf8'));

function fail(message) {
  throw new Error(`PT-05 asset validation failed: ${message}`);
}

function hash(fileName) {
  return crypto.createHash('sha256').update(fs.readFileSync(path.join(assetDirectory, fileName))).digest('hex');
}

function tableField(bytes, table, fieldIndex) {
  const vtable = table - bytes.readInt32LE(table);
  const vtableLength = bytes.readUInt16LE(vtable);
  const entry = vtable + 4 + (fieldIndex * 2);
  if (entry + 2 > vtable + vtableLength) return 0;
  return bytes.readUInt16LE(entry);
}

function indirect(bytes, offset) {
  return offset + bytes.readUInt32LE(offset);
}

function tableVector(bytes, table, fieldIndex) {
  const field = tableField(bytes, table, fieldIndex);
  if (!field) return [];
  const vector = table + field + bytes.readUInt32LE(table + field);
  const length = bytes.readUInt32LE(vector);
  const first = vector + 4;
  return Array.from({ length }, (_, index) => indirect(bytes, first + (index * 4)));
}

function scalarVector(bytes, table, fieldIndex, readElement) {
  const field = tableField(bytes, table, fieldIndex);
  if (!field) return [];
  const vector = table + field + bytes.readUInt32LE(table + field);
  const length = bytes.readUInt32LE(vector);
  const first = vector + 4;
  return Array.from({ length }, (_, index) => readElement(first + (index * 4)));
}

function tensorDetails(bytes, tensor) {
  const typeField = tableField(bytes, tensor, 1);
  const type = typeField ? bytes.readUInt8(tensor + typeField) : 0;
  return { type, shape: scalarVector(bytes, tensor, 0, (offset) => bytes.readInt32LE(offset)) };
}

function inspectTflite(modelPath) {
  const bytes = fs.readFileSync(modelPath);
  if (bytes.subarray(4, 8).toString('ascii') !== 'TFL3') fail('o arquivo não possui a assinatura TFL3.');
  const model = indirect(bytes, 0);
  // Model fields: version=0, operator_codes=1, subgraphs=2.
  const subgraphs = tableVector(bytes, model, 2);
  if (subgraphs.length !== 1) fail(`esperado um subgrafo, encontrado ${subgraphs.length}.`);
  const subgraph = subgraphs[0];
  const tensors = tableVector(bytes, subgraph, 0);
  const inputs = scalarVector(bytes, subgraph, 1, (offset) => bytes.readInt32LE(offset));
  const outputs = scalarVector(bytes, subgraph, 2, (offset) => bytes.readInt32LE(offset));
  if (inputs.length !== 1 || outputs.length !== 1) fail('o modelo precisa ter exatamente uma entrada e uma saída.');
  return { input: tensorDetails(bytes, tensors[inputs[0]]), output: tensorDetails(bytes, tensors[outputs[0]]) };
}

function assertEqual(actual, expected, description) {
  if (JSON.stringify(actual) !== JSON.stringify(expected)) fail(`${description}: esperado ${JSON.stringify(expected)}, obtido ${JSON.stringify(actual)}.`);
}

for (const item of [manifest.model, manifest.labels, manifest.image]) {
  if (hash(item.file) !== item.sha256) fail(`SHA-256 divergente para ${item.file}.`);
}

const details = inspectTflite(path.join(assetDirectory, manifest.model.file));
if (details.input.type !== 3 || details.output.type !== 3) fail('entrada e saída precisam ser uint8 (TensorType 3).');
assertEqual(details.input.shape, manifest.input.shape, 'shape da entrada');
assertEqual(details.output.shape, manifest.output.shape, 'shape da saída');
if (manifest.input.colorOrder !== 'RGB' || manifest.input.bytes !== 224 * 224 * 3) fail('contrato RGB/bytes de entrada inválido.');

const labels = fs.readFileSync(path.join(assetDirectory, manifest.labels.file), 'utf8').trim().split(/\r?\n/);
if (labels.length !== manifest.labels.count || labels.length !== details.output.shape[1]) fail('quantidade de labels não confere com a saída.');
if (!labels.includes(manifest.expectedTop1)) fail('o label esperado não consta no arquivo de labels.');

const jpeg = decode(fs.readFileSync(path.join(assetDirectory, manifest.image.file)), { useTArray: true, formatAsRGBA: true });
if (!jpeg.width || !jpeg.height || jpeg.data.length !== jpeg.width * jpeg.height * 4) fail('JPEG determinístico inválido.');

const proofModule = fs.readFileSync(path.join(projectRoot, 'components', 'PT05OfflineProofScreen.js'), 'utf8');
if (/\b(fetch|XMLHttpRequest|axios|https?:\/\/|apiConfig|AsyncStorage|Location|Notifications)\b/i.test(proofModule)) fail('o módulo da prova contém dependência remota, persistente ou de localização.');

console.log(JSON.stringify({
  status: 'PASS',
  model: { sha256: manifest.model.sha256, input: details.input, output: details.output },
  labels: labels.length,
  jpeg: { width: jpeg.width, height: jpeg.height },
  rgbBytes: manifest.input.bytes,
}));
