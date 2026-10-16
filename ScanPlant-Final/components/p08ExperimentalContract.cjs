// Test-only contract. No images, model bytes, source identities or network access.
const MODEL_SHA256 = '82c7bab4de164c70cd97e6651397ab19078437852ea8f2246d99ebdd2dafbf3c';
const LABELS_SHA256 = '0299f64143a228cc0268ee8f92917ccb71f0e9971b3396dc5bb7cb12785a3c47';
const INPUT_LENGTH = 224 * 224 * 3;
const PARITY_TOLERANCE = 0.0001;
const STABILITY_TOLERANCE = 0.000001;

function assert(condition, message) {
  if (!condition) throw new Error(`P08 experimental: ${message}`);
}

function validateFile(ref) {
  assert(ref && /^[a-z0-9][a-z0-9.-]*$/.test(ref.file), 'nome de arquivo inseguro');
  assert(/^[a-f0-9]{64}$/.test(ref.sha256) && /^[a-f0-9]{32}$/.test(ref.md5), 'digest ausente');
  assert(Number.isSafeInteger(ref.bytes) && ref.bytes > 0, 'tamanho inválido');
}

function validateManifest(manifest, labels) {
  assert(manifest.schema_version === 1 && manifest.kind === 'p08_private_android_float32_proof', 'manifesto inválido');
  assert(manifest.model.sha256 === MODEL_SHA256 && manifest.labels.sha256 === LABELS_SHA256, 'bytes não autorizados');
  validateFile(manifest.model); validateFile(manifest.labels);
  assert(labels.length === 12, 'esperados 12 rótulos');
  labels.forEach((label, index) => {
    assert(label.index === index && label.class_id === `species_${String(index + 1).padStart(2, '0')}`
      && typeof label.scientific_name === 'string' && label.scientific_name.length > 0, 'ordem dos rótulos divergente');
  });
  assert(manifest.preprocessing === 'pipeline_pillow_bilinear_rgb224_float32_0_255_embedded_rescaling', 'pré-processamento divergente');
  assert(manifest.parity_tolerance === PARITY_TOLERANCE && manifest.stability_tolerance === STABILITY_TOLERANCE, 'tolerâncias divergentes');
  assert(manifest.warmup_runs === 2 && manifest.timed_runs === 20, 'protocolo de latência divergente');
  assert(manifest.cases.length === 24, 'esperados os 24 casos aceitos');
  const files = new Set();
  manifest.cases.forEach((entry) => {
    validateFile(entry.input);
    assert(entry.input.bytes === INPUT_LENGTH * 4 && !files.has(entry.input.file), 'tensor duplicado ou tamanho divergente');
    files.add(entry.input.file);
    compareOutput(entry.probabilities, entry.probabilities);
  });
}

function decodeFloat32LE(bytes) {
  assert(bytes.byteLength === INPUT_LENGTH * 4, 'tamanho do RGB Float32 divergente');
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  const result = new Float32Array(INPUT_LENGTH);
  for (let i = 0; i < result.length; i += 1) {
    const value = view.getFloat32(i * 4, true);
    assert(Number.isFinite(value) && value >= 0 && value <= 255 && Number.isInteger(value), 'RGB fora de 0..255');
    result[i] = value;
  }
  return result;
}

function checkTensorContract(model) {
  assert(model.inputs.length === 1 && model.outputs.length === 1, 'quantidade de tensores divergente');
  assert(model.inputs[0].dataType === 'float32' && model.inputs[0].shape.join(',') === '1,224,224,3', 'entrada nativa divergente');
  assert(model.outputs[0].dataType === 'float32' && model.outputs[0].shape.join(',') === '1,12', 'saída nativa divergente');
}

function compareOutput(output, expected, tolerance = PARITY_TOLERANCE) {
  assert(output && expected && output.length === 12 && expected.length === 12, 'comprimento da saída divergente');
  let maxError = 0; let sum = 0;
  output.forEach((value, index) => {
    assert(Number.isFinite(value) && value >= 0 && value <= 1 && Number.isFinite(expected[index]), 'probabilidade inválida');
    sum += value; maxError = Math.max(maxError, Math.abs(value - expected[index]));
  });
  assert(Math.abs(sum - 1) <= 0.0001, 'soma de probabilidades divergente');
  return { passed: maxError <= tolerance, maxAbsoluteError: maxError, tolerance };
}

function latencySummary(samples) {
  assert(samples.length === 20 && samples.every(x => Number.isFinite(x) && x >= 0), 'amostras de latência inválidas');
  const sorted = [...samples].sort((a, b) => a - b);
  return { count: samples.length, minMs: sorted[0], medianMs: (sorted[9] + sorted[10]) / 2,
    p95Ms: sorted[18], maxMs: sorted[19], meanMs: samples.reduce((a, b) => a + b, 0) / samples.length };
}

module.exports = { MODEL_SHA256, LABELS_SHA256, INPUT_LENGTH, PARITY_TOLERANCE, STABILITY_TOLERANCE,
  validateFile, validateManifest, decodeFloat32LE, checkTensorContract, compareOutput, latencySummary };
