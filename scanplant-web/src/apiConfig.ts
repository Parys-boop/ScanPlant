// URL Configuration
// In a web environment, we usually point to the relative path or a specific environment variable
// Since we are porting the specific logic, we keep the discovery logic but adapt it for web CORS.

export const API_CONFIG = {
  // Try to use the window hostname if available, assuming backend serves frontend or is on same network
  BASE_URL: `http://${window.location.hostname}:5041/api`,
  TIMEOUT: 10000,
};