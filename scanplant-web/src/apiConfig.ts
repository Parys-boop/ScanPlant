// URL Configuration
// In a web environment, we usually point to the relative path or a specific environment variable
// Since we are porting the specific logic, we keep the discovery logic but adapt it for web CORS.

const getApiBaseUrl = () => {
  // Se estiver em produção (Vercel), use a URL permanente do Railway
  if (import.meta.env.PROD) {
    // API hospedada no Railway (permanente)
    return import.meta.env.VITE_API_URL || 'https://scanplant-production.up.railway.app/api';
  }
  
  // Em desenvolvimento, use localhost
  return 'http://localhost:5041/api';
};

export const API_CONFIG = {
  BASE_URL: getApiBaseUrl(),
  TIMEOUT: 10000,
};