import PT05OfflineProofScreen from './components/PT05OfflineProofScreen';

// A variável é definida apenas no perfil EAS phase0-offline. A decisão ocorre
// antes de carregar o fluxo principal, que continua intocado em AppMain.js.
const isPT05OfflineProof = process.env.EXPO_PUBLIC_PT05_OFFLINE_PROOF === '1';

const App = isPT05OfflineProof
  ? PT05OfflineProofScreen
  : require('./AppMain').default;

export default App;
