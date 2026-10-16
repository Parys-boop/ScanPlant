import React, { useEffect, useState } from 'react';
import { SafeAreaView, ScrollView, Text } from 'react-native';
import * as FileSystem from 'expo-file-system';
import { loadTensorflowModel } from 'react-native-fast-tflite';
import contract from './p08ExperimentalContract.cjs';

// Activation requires an explicit flag and a private bundle already installed by USB.
// No experimental assets are required, bundled, fetched or used by the normal flow.
const bundleId = process.env.EXPO_PUBLIC_P08_EXPERIMENT_ID;
const clock = () => global.performance.now();

function timeout(promise) {
  let timer;
  return Promise.race([promise, new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error('Timeout na inferência experimental.')), 30000);
  })]).finally(() => clearTimeout(timer));
}

export default function P08ExperimentalProofScreen() {
  const [message, setMessage] = useState('Preparando teste técnico privado…');
  useEffect(() => {
    let cancelled = false;
    async function run() {
      if (!/^[a-f0-9]{64}$/.test(bundleId || '')) throw new Error('ID privado do ensaio ausente ou inválido.');
      const root = `${FileSystem.documentDirectory}p08-experiment/${bundleId}/`;
      async function checkedFile(ref) {
        contract.validateFile(ref);
        const uri = root + ref.file;
        const info = await FileSystem.getInfoAsync(uri, { md5: true });
        if (!info.exists || info.size !== ref.bytes || info.md5 !== ref.md5) throw new Error('Arquivo privado ausente ou alterado.');
        return uri;
      }
      const manifest = JSON.parse(await FileSystem.readAsStringAsync(root + 'manifest.json'));
      const labels = JSON.parse(await FileSystem.readAsStringAsync(await checkedFile(manifest.labels)));
      contract.validateManifest(manifest, labels);
      const start = clock();
      const model = await timeout(loadTensorflowModel({ url: await checkedFile(manifest.model) }, 'default'));
      const loadMs = clock() - start;
      contract.checkTensorContract(model);
      let firstInput; let firstOutput;
      const cases = [];
      for (const [index, entry] of manifest.cases.entries()) {
        if (cancelled) return;
        const base64 = await FileSystem.readAsStringAsync(await checkedFile(entry.input), { encoding: FileSystem.EncodingType.Base64 });
        const binary = global.atob(base64);
        const bytes = Uint8Array.from(binary, c => c.charCodeAt(0));
        const input = contract.decodeFloat32LE(bytes); // Already resized; do not scale a second time.
        if (index === 0) {
          firstInput = input;
          for (let n = 0; n < manifest.warmup_runs; n += 1) await timeout(model.run([input]));
        }
        const inferStart = clock();
        const output = Array.from((await timeout(model.run([input])))[0]);
        const inferenceMs = clock() - inferStart;
        if (index === 0) firstOutput = output;
        cases.push({ index, output, inferenceMs, parity: contract.compareOutput(output, entry.probabilities) });
        if (!cancelled) setMessage(`Teste técnico: ${index + 1}/24 tensores. Não avalia qualidade botânica.`);
      }
      const samples = []; const repeats = [];
      for (let n = 0; n < manifest.timed_runs; n += 1) {
        if (cancelled) return;
        const startRun = clock();
        const output = Array.from((await timeout(model.run([firstInput])))[0]);
        samples.push(clock() - startRun);
        repeats.push(contract.compareOutput(output, firstOutput, contract.STABILITY_TOLERANCE));
      }
      const result = { schema_version: 1, kind: 'p08_private_android_result', bundleId,
        modelSha256: contract.MODEL_SHA256, labelsSha256: contract.LABELS_SHA256,
        delegate: model.delegate, loadMs, cases, repeats, latency: contract.latencySummary(samples),
        latencyScope: 'JS monotonic clock around awaited native inference; excludes preprocessing and file IO',
        passed: cases.every(x => x.parity.passed) && repeats.every(x => x.passed),
        physicalNetworkStateVerifiedByApp: false, botanicalPerformanceClaim: false };
      const file = `result-${Date.now()}.json`;
      await FileSystem.writeAsStringAsync(root + file, JSON.stringify(result));
      console.log(`P08_EXPERIMENT_RESULT ${JSON.stringify({ file, bundleId, passed: result.passed })}`);
      if (!cancelled) setMessage(`Teste técnico ${result.passed ? 'passou' : 'divergiu'}. Mediana: ${result.latency.medianMs.toFixed(1)} ms. Não aprova reconhecimento ou uso em produto.`);
    }
    run().catch(error => {
      console.log(`P08_EXPERIMENT_ERROR ${JSON.stringify({ bundleId, epochMs: Date.now(), message: String(error.message || error) })}`);
      if (!cancelled) setMessage(`Teste não concluído: ${error.message || error}`);
    });
    return () => { cancelled = true; };
  }, []);
  return (
    <SafeAreaView style={{ flex: 1, padding: 24 }}>
      <ScrollView>
        <Text style={{ fontSize: 22 }}>P08 · TESTE EXPERIMENTAL PRIVADO</Text>
        <Text>{message}</Text>
        <Text>12 rótulos provisórios. Modelo anterior e fluxo normal preservados. Nenhuma conclusão de precisão botânica.</Text>
      </ScrollView>
    </SafeAreaView>
  );
}
