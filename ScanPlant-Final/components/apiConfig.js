// ======================================================================
// CONFIGURAÇÃO DA API - SCANPLANT - MULTI-IP AUTOMÁTICO
// ======================================================================
// Sistema inteligente que tenta múltiplos IPs automaticamente

// localhost é priorizado para Development Build conectado por USB/ADB.
const KNOWN_IPS = [
  'localhost',
  '192.168.0.130',   // Casa
  '10.211.60.56',    // Escola/Trabalho
  '192.168.1.100',   // Outra rede (exemplo)
  '10.0.0.100',      // Outra rede (exemplo)
];

const PORT = 5041;
const API_PATH = '/api';

let workingBaseUrl = null;
let discoveryPromise = null;

// Função para testar se um IP está acessível
async function testConnection(ip) {
  const baseUrl = ip === 'localhost' 
    ? `http://localhost:${PORT}${API_PATH}`
    : `http://${ip}:${PORT}${API_PATH}`;
  
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000); // 2 segundos timeout
    
    const response = await fetch(`${baseUrl}/health`, {
      method: 'GET',
      signal: controller.signal,
    });
    
    clearTimeout(timeoutId);
    
    if (response.ok) {
      return baseUrl;
    }
  } catch (error) {
    // Falhas são esperadas durante a descoberta e não devem gerar logs com dados de rede.
  }
  
  return null;
}

// Função para descobrir o IP que funciona
async function discoverWorkingIP() {
  if (workingBaseUrl) {
    return workingBaseUrl;
  }

  if (!discoveryPromise) {
    discoveryPromise = (async () => {
      for (const ip of KNOWN_IPS) {
        const baseUrl = await testConnection(ip);
        if (baseUrl) {
          workingBaseUrl = baseUrl;
          return baseUrl;
        }
      }

      throw new Error('API indisponível');
    })();
  }

  try {
    return await discoveryPromise;
  } finally {
    discoveryPromise = null;
  }
}

export const API_CONFIG = {
  // Esta função retorna o BASE_URL dinâmico
  getBaseUrl: async () => {
    return await discoverWorkingIP();
  },
  
  TIMEOUT: 10000,
  
  // Adicionar novo IP à lista
  addKnownIP: (ip) => {
    if (!KNOWN_IPS.includes(ip)) {
      KNOWN_IPS.push(ip);
    }
  },
  
  // Forçar re-descoberta (útil se mudar de rede)
  resetConnection: () => {
    workingBaseUrl = null;
    discoveryPromise = null;
  }
};

// ======================================================================
// COMO DESCOBRIR SEU IP LOCAL:
// ======================================================================
// 
// WINDOWS:
//   1. Abra o PowerShell no diretório do backend
//   2. Execute: .\get-ip.ps1
//   3. O script mostrará seu IP e copiará a URL completa
//
// MANUAL (Windows):
//   1. Abra PowerShell ou CMD
//   2. Execute: ipconfig
//   3. Procure por "Endereço IPv4" na seção Wi-Fi ou Ethernet
//   4. Use esse IP no formato: http://SEU_IP:5041/api
//
// MANUAL (Mac/Linux):
//   1. Abra o Terminal
//   2. Execute: ifconfig | grep "inet "
//   3. Procure pelo IP que não seja 127.0.0.1
//   4. Use esse IP no formato: http://SEU_IP:5041/api
//
// ======================================================================
// IMPORTANTE:
// ======================================================================
// - Certifique-se de que seu celular e PC estão na MESMA REDE Wi-Fi
// - Desative firewalls que possam bloquear a porta 5041
// - A API deve estar rodando antes de testar o app
// ======================================================================
