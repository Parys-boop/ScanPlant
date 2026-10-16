import PT05OfflineProofScreen from './components/PT05OfflineProofScreen';

// A variável é definida apenas no perfil EAS phase0-offline. A decisão ocorre
// antes de carregar o fluxo principal, que continua intocado em AppMain.js.
const isPT05OfflineProof = process.env.EXPO_PUBLIC_PT05_OFFLINE_PROOF === '1';
const isP08ExperimentalProof = process.env.EXPO_PUBLIC_P08_EXPERIMENTAL_PROOF === '1';
if (isPT05OfflineProof && isP08ExperimentalProof) {
  throw new Error('Selecione somente um modo de prova offline.');
}

const App = isP08ExperimentalProof
  ? require('./components/P08ExperimentalProofScreen').default
  : isPT05OfflineProof ? PT05OfflineProofScreen : require('./AppMain').default;

export default App;
