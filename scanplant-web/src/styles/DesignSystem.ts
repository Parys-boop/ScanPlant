// Design System Profissional - ScanPlant Web

// Paleta de Cores Profissional
export const Colors = {
  // Cores Primárias (Verde Claro Moderno)
  primary: {
    50: '#f0fdf4',
    100: '#dcfce7',
    200: '#bbf7d0',
    300: '#86efac',
    400: '#4ade80',
    500: '#22c55e', // Verde claro principal
    600: '#16a34a',
    700: '#15803d',
    800: '#166534',
    900: '#14532d',
  },
  
  // Cores Neutras (Escala de Cinza)
  neutral: {
    50: '#fafafa',
    100: '#f5f5f5',
    200: '#e5e5e5',
    300: '#d4d4d4',
    400: '#a3a3a3',
    500: '#737373',
    600: '#525252',
    700: '#404040',
    800: '#262626',
    900: '#171717',
  },
  
  // Cores de Sistema
  success: '#10b981',
  warning: '#f59e0b',
  error: '#ef4444',
  info: '#3b82f6',
  
  // Cores de Fundo
  background: {
    primary: '#ffffff',
    secondary: '#f8fafc',
    tertiary: '#f1f5f9',
    dark: '#1f2937',
  },
  
  // Cores de Texto
  text: {
    primary: '#1f2937',
    secondary: '#6b7280',
    tertiary: '#9ca3af',
    inverse: '#ffffff',
    muted: '#a1a1aa',
  },
  
  // Cores de Borda
  border: {
    light: '#e5e7eb',
    medium: '#d1d5db',
    dark: '#9ca3af',
  },
};

// Tipografia Profissional
export const Typography = {
  // Tamanhos de Fonte (em pixels)
  fontSize: {
    xs: '12px',
    sm: '14px',
    base: '16px',
    lg: '18px',
    xl: '20px',
    '2xl': '24px',
    '3xl': '30px',
    '4xl': '36px',
    '5xl': '48px',
  },
  
  // Pesos de Fonte
  fontWeight: {
    normal: '400',
    medium: '500',
    semibold: '600',
    bold: '700',
  },
  
  // Altura da Linha
  lineHeight: {
    tight: '1.25',
    normal: '1.5',
    relaxed: '1.75',
  },
};

// Espaçamento Consistente (em pixels)
export const Spacing = {
  xs: '4px',
  sm: '8px',
  md: '16px',
  lg: '24px',
  xl: '32px',
  '2xl': '48px',
  '3xl': '64px',
  '4xl': '80px',
  '5xl': '96px',
};

// Bordas e Raios (em pixels)
export const BorderRadius = {
  none: '0',
  sm: '4px',
  md: '8px',
  lg: '12px',
  xl: '16px',
  '2xl': '24px',
  full: '9999px',
};

// Sombras
export const Shadows = {
  sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
  md: '0 2px 4px 0 rgba(0, 0, 0, 0.1)',
  lg: '0 4px 8px 0 rgba(0, 0, 0, 0.15)',
  xl: '0 8px 16px 0 rgba(0, 0, 0, 0.2)',
};

// Breakpoints e medidas responsivas
export const Breakpoints = {
  mobileMax: '640px',
  tabletMin: '641px',
  tabletMax: '1024px',
  desktopMin: '1025px',
};

export const Layout = {
  contentMax: '1200px',
  contentMaxNarrow: '760px',
  contentMaxChat: '980px',
};

// Ícones Profissionais (símbolos minimalistas)
export const Icons = {
  // Navegação
  back: '‹',
  forward: '›',
  up: '⌃',
  down: '⌄',
  close: '✕',
  
  // Ações
  add: '+',
  remove: '−',
  edit: '✎',
  delete: '⌫',
  save: '✓',
  cancel: '✕',
  rotate: '↻',
  
  // Interface
  menu: '≡',
  search: '⌕',
  filter: '⚙',
  settings: '⚙',
  
  // Conteúdo
  image: '▢',
  camera: '⌘',
  gallery: '▦',
  location: '⌖',
  calendar: '▣',
  collection: '⊞',
  users: '⋙',
  community: '▦',
  
  // Plantas
  plant: '❋',
  leaf: '❋',
  flower: '✿',
  tree: '♦',
  identify: '❋',
  
  // Estados
  success: '✓',
  warning: '!',
  error: '✕',
  info: 'i',
  loading: '○',
};

export default {
  Colors,
  Typography,
  Spacing,
  BorderRadius,
  Shadows,
  Breakpoints,
  Layout,
  Icons,
};
