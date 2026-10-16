const { test } = require('node:test');
const assert = require('node:assert/strict');
const c = require('../components/p08ExperimentalContract.cjs');

const probabilities = () => [1, ...Array(11).fill(0)];
function fixture() {
  const ref = (file, bytes = 1) => ({ file, bytes, sha256: 'a'.repeat(64), md5: 'b'.repeat(32) });
  return {
    labels: Array.from({ length: 12 }, (_, index) => ({ index, class_id: `species_${String(index + 1).padStart(2, '0')}`, scientific_name: `Genus species${index}` })),
    manifest: { schema_version: 1, kind: 'p08_private_android_float32_proof',
      model: { ...ref('model.tflite'), sha256: c.MODEL_SHA256 },
      labels: { ...ref('labels.json'), sha256: c.LABELS_SHA256 },
      preprocessing: 'pipeline_pillow_bilinear_rgb224_float32_0_255_embedded_rescaling',
      parity_tolerance: 0.0001, stability_tolerance: 0.000001, warmup_runs: 2, timed_runs: 20,
      cases: Array.from({ length: 24 }, (_, index) => ({ index, input: ref(`case-${index}.f32`, c.INPUT_LENGTH * 4), probabilities: probabilities() })) },
  };
}

test('only the pinned model and twelve ordered labels are accepted', () => {
  const f = fixture(); c.validateManifest(f.manifest, f.labels);
  f.labels.reverse(); assert.throws(() => c.validateManifest(f.manifest, f.labels));
  f.labels.reverse(); f.manifest.model.sha256 = 'c'.repeat(64);
  assert.throws(() => c.validateManifest(f.manifest, f.labels));
});
test('uint8, 1001 classes and mismatched tensor shapes fail closed', () => {
  const model = { inputs: [{ shape: [1,224,224,3], dataType: 'float32' }], outputs: [{ shape: [1,12], dataType: 'float32' }] };
  c.checkTensorContract(model);
  model.inputs[0].dataType = 'uint8'; assert.throws(() => c.checkTensorContract(model));
  model.inputs[0].dataType = 'float32'; model.outputs[0].shape = [1,1001];
  assert.throws(() => c.checkTensorContract(model));
});
test('preprocessing and tolerances cannot silently change', () => {
  const f = fixture(); f.manifest.preprocessing = 'nearest_uint8';
  assert.throws(() => c.validateManifest(f.manifest, f.labels));
  const g = fixture(); g.manifest.parity_tolerance = 0.02;
  assert.throws(() => c.validateManifest(g.manifest, g.labels));
});
test('private filenames reject absolute paths and traversal', () => {
  for (const file of ['/tmp/model', '../model', 'file://model', 'case/0.f32']) {
    assert.throws(() => c.validateFile({ file, sha256: 'a'.repeat(64), md5: 'b'.repeat(32), bytes: 1 }));
  }
});
test('all 24 tensors required, without duplicate fixture references', () => {
  const f = fixture(); f.manifest.cases.pop(); assert.throws(() => c.validateManifest(f.manifest, f.labels));
  const g = fixture(); g.manifest.cases[1].input.file = g.manifest.cases[0].input.file;
  assert.throws(() => c.validateManifest(g.manifest, g.labels));
});
test('little endian values stay raw 0..255 without scaling or channel exchange', () => {
  const bytes = new Uint8Array(c.INPUT_LENGTH * 4); const view = new DataView(bytes.buffer);
  [0,127,255].forEach((x,i) => view.setFloat32(i*4,x,true));
  assert.deepEqual(Array.from(c.decodeFloat32LE(bytes).subarray(0,3)), [0,127,255]);
  view.setFloat32(0,-1,true); assert.throws(() => c.decodeFloat32LE(bytes));
  view.setFloat32(0,NaN,true); assert.throws(() => c.decodeFloat32LE(bytes));
  assert.throws(() => c.decodeFloat32LE(bytes.subarray(4)));
});
test('runtime parity and stability failures remain failures', () => {
  const expected = probabilities(); const actual = [...expected]; actual[0] -= 0.001; actual[1] += 0.001;
  assert.equal(c.compareOutput(actual, expected).passed, false);
  assert.equal(c.compareOutput(expected, expected, c.STABILITY_TOLERANCE).passed, true);
  assert.throws(() => c.compareOutput([NaN, ...Array(11).fill(0)], expected));
  assert.throws(() => c.compareOutput(Array(12).fill(0), expected));
});
test('latency statistics use twenty timed runs, with no invented performance budget', () => {
  const stats = c.latencySummary(Array.from({ length: 20 }, (_, i) => i + 1));
  assert.deepEqual(stats, { count: 20, minMs: 1, medianMs: 10.5, p95Ms: 19, maxMs: 20, meanMs: 10.5 });
  assert.throws(() => c.latencySummary([1,2]));
});
