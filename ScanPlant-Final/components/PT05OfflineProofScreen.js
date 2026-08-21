import React, { useEffect, useState } from 'react';
import { ActivityIndicator, SafeAreaView, ScrollView, StyleSheet, Text, View } from 'react-native';
import { Asset } from 'expo-asset';
import * as FileSystem from 'expo-file-system';
import { decode } from 'jpeg-js';
import { loadTensorflowModel } from 'react-native-fast-tflite';

import manifest from '../assets/offline-proof/manifest.json';

const IMAGE_SIZE = 224;
const INPUT_BYTES = IMAGE_SIZE * IMAGE_SIZE * 3;
const OPERATION_TIMEOUT_MS = 8000;
const WATCHDOG_TIMEOUT_MS = 18000;

function stage(name, details = {}) {
  console.log(`PT05_STAGE ${JSON.stringify({ stage: name, ...details })}`);
}

function withTimeout(name, promise, timeoutMs = OPERATION_TIMEOUT_MS) {
  let timer;
  const timeout = new Promise((_, reject) => {
    timer = setTimeout(() => reject(new Error(`Timeout em ${name}.`)), timeoutMs);
  });
  return Promise.race([promise, timeout]).finally(() => clearTimeout(timer));
}

function base64ToBytes(base64) {
  const binary = global.atob(base64);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) bytes[index] = binary.charCodeAt(index);
  return bytes;
}

function resizeRgbaToRgb(rgba, sourceWidth, sourceHeight) {
  const rgb = new Uint8Array(INPUT_BYTES);
  for (let y = 0; y < IMAGE_SIZE; y += 1) {
    const sourceY = Math.min(sourceHeight - 1, Math.floor((y * sourceHeight) / IMAGE_SIZE));
    for (let x = 0; x < IMAGE_SIZE; x += 1) {
      const sourceX = Math.min(sourceWidth - 1, Math.floor((x * sourceWidth) / IMAGE_SIZE));
      const sourceOffset = (sourceY * sourceWidth + sourceX) * 4;
      const targetOffset = (y * IMAGE_SIZE + x) * 3;
      rgb[targetOffset] = rgba[sourceOffset];
      rgb[targetOffset + 1] = rgba[sourceOffset + 1];
      rgb[targetOffset + 2] = rgba[sourceOffset + 2];
    }
  }
  return rgb;
}

function formatScore(value) {
  return `${(value * 100).toFixed(2)}%`;
}

function topPredictions(output, labels) {
  return Array.from(output)
    .map((score, index) => ({ index, score, label: labels[index] || `classe-${index}` }))
    .sort((left, right) => right.score - left.score)
    .slice(0, 5);
}

async function bundledJpegToRgb() {
  stage('image-start');
  const imageAsset = Asset.fromModule(require('../assets/offline-proof/daisy.jpg'));
  await withTimeout('image-download', imageAsset.downloadAsync());
  const base64 = await withTimeout('image-read', FileSystem.readAsStringAsync(imageAsset.localUri, {
    encoding: FileSystem.EncodingType.Base64,
  }));
  stage('image-loaded');
  stage('decode-start');
  const decoded = decode(base64ToBytes(base64), { useTArray: true, formatAsRGBA: true });
  stage('decode-finished', { width: decoded.width, height: decoded.height });
  return {
    source: { width: decoded.width, height: decoded.height },
    rgb: resizeRgbaToRgb(decoded.data, decoded.width, decoded.height),
  };
}

export default function PT05OfflineProofScreen() {
  const [state, setState] = useState({ phase: 'Preparando prova CPU offline…', result: null, error: null });

  useEffect(() => {
    let cancelled = false;
    let completed = false;
    const startedAt = Date.now();

    const finish = (result, nextState) => {
      if (completed) return;
      completed = true;
      console.log(`PT05_RESULT ${JSON.stringify(result)}`);
      if (!cancelled) setState(nextState);
    };

    const watchdog = setTimeout(() => {
      finish(
        { origin: 'bundled', status: 'error', error: 'Watchdog global PT-05 expirou.', durationMs: Date.now() - startedAt },
        { phase: 'Falha na prova offline.', result: null, error: 'Watchdog global PT-05 expirou.' },
      );
    }, WATCHDOG_TIMEOUT_MS);

    async function runProof() {
      try {
        stage('screen-mounted');
        stage('labels-start');
        const labelsAsset = Asset.fromModule(require('../assets/offline-proof/labels.txt'));
        await withTimeout('labels-download', labelsAsset.downloadAsync());
        const labelsText = await withTimeout('labels-read', FileSystem.readAsStringAsync(labelsAsset.localUri));
        const labels = labelsText.replace(/^\uFEFF/, '').split(/\r?\n/).map((label) => label.trim()).filter(Boolean);
        const expectedOutputLength = manifest.output.shape[1];
        if (labels.length !== manifest.labels.count || labels.length !== expectedOutputLength) throw new Error(`Labels inválidos: ${labels.length}/${expectedOutputLength}.`);
        stage('labels-loaded', { count: labels.length });

        if (!cancelled) setState({ phase: 'Decodificando JPEG e preparando RGB 224×224…', result: null, error: null });
        const image = await withTimeout('image-pipeline', bundledJpegToRgb());
        if (image.rgb.byteLength !== INPUT_BYTES) throw new Error('Buffer RGB com tamanho inválido.');

        if (!cancelled) setState({ phase: 'Carregando modelo TFLite empacotado (CPU)…', result: null, error: null });
        stage('model-start');
        const model = await withTimeout('model-load', loadTensorflowModel(require('../assets/offline-proof/mobilenet_v1_1.0_224_quant.tflite')));
        const outputTensor = model.outputs[0];
        if (!outputTensor || outputTensor.dataType !== 'uint8' || outputTensor.shape.join(',') !== manifest.output.shape.join(',')) throw new Error('Tensor de saída não confere com o manifesto.');
        stage('model-loaded', { outputLength: outputTensor.shape[1] });
        if (!cancelled) setState({ phase: 'Executando inferência local…', result: null, error: null });
        stage('inference-start');
        const outputs = await withTimeout('inference', model.run([image.rgb]));
        if (!outputs[0] || outputs[0].length !== labels.length || outputs[0].length !== expectedOutputLength) throw new Error('Tamanho real da saída não confere com labels.');
        stage('inference-finished', { outputLength: outputs[0].length });
        const top5 = topPredictions(outputs[0], labels);
        const top1 = top5[0];
        const elapsedMs = Date.now() - startedAt;

        const result = {
          modelSha256: manifest.model.sha256,
          origin: 'bundled',
          input: { type: 'uint8', shape: manifest.input.shape, bytes: image.rgb.byteLength, source: image.source },
          top1: { label: top1.label, score: Number(top1.score.toFixed(6)) },
          top5: top5.map((item) => ({ label: item.label, score: Number(item.score.toFixed(6)) })),
          durationMs: elapsedMs,
          expectedTop1: manifest.expectedTop1,
          passed: top1.label === manifest.expectedTop1 && elapsedMs <= 10000,
        };
        finish(result, { phase: result.passed ? 'Prova aprovada.' : 'Prova concluída com divergência.', result, error: null });
      } catch (error) {
        const safeError = error instanceof Error ? error.message : 'Erro desconhecido.';
        finish({ origin: 'bundled', status: 'error', error: safeError, durationMs: Date.now() - startedAt }, { phase: 'Falha na prova offline.', result: null, error: safeError });
      }
    }

    runProof();
    return () => { cancelled = true; clearTimeout(watchdog); };
  }, []);

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.eyebrow}>PT-05 · DIAGNÓSTICO ISOLADO</Text>
        <Text style={styles.title}>Reconhecimento TFLite offline</Text>
        <Text style={styles.body}>{state.phase}</Text>
        {!state.result && !state.error && <ActivityIndicator size="large" color="#2f855a" />}
        {state.error && <Text style={styles.error}>{state.error}</Text>}
        {state.result && (
          <View style={[styles.result, state.result.passed ? styles.pass : styles.fail]}>
            <Text style={styles.resultTitle}>{state.result.passed ? 'PASSOU' : 'DIVERGIU'}</Text>
            <Text style={styles.resultLine}>Top-1: {state.result.top1.label} ({formatScore(state.result.top1.score)})</Text>
            <Text style={styles.resultLine}>Esperado: {state.result.expectedTop1}</Text>
            <Text style={styles.resultLine}>CPU: {state.result.durationMs} ms · RGB: {state.result.input.bytes} bytes</Text>
            <Text style={styles.top5}>Top-5{state.result.top5.map((item, index) => `\n${index + 1}. ${item.label} — ${formatScore(item.score)}`).join('')}</Text>
          </View>
        )}
        <Text style={styles.note}>Modelo e imagem vêm do pacote do aplicativo. Esta tela não usa API, localização, login ou persistência.</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#f4fbf6' },
  container: { flexGrow: 1, justifyContent: 'center', padding: 24, gap: 16 },
  eyebrow: { color: '#2f855a', fontSize: 12, fontWeight: '700', letterSpacing: 1 },
  title: { color: '#153723', fontSize: 28, fontWeight: '800' },
  body: { color: '#31533e', fontSize: 16, lineHeight: 23 },
  result: { borderRadius: 12, borderWidth: 1, padding: 16, gap: 8 },
  pass: { backgroundColor: '#ecfdf3', borderColor: '#68d391' },
  fail: { backgroundColor: '#fff7ed', borderColor: '#fb923c' },
  resultTitle: { color: '#153723', fontSize: 20, fontWeight: '800' },
  resultLine: { color: '#1f3b2b', fontSize: 15 },
  top5: { color: '#31533e', fontSize: 14, lineHeight: 20, marginTop: 4 },
  error: { color: '#9b2c2c', fontSize: 16, lineHeight: 23 },
  note: { color: '#52705d', fontSize: 13, lineHeight: 19, marginTop: 16 },
});
