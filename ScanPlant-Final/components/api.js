import AsyncStorage from '@react-native-async-storage/async-storage';
import { Platform } from 'react-native';
import { API_CONFIG } from './apiConfig';

// URL da API - será descoberta dinamicamente
let API_URL = API_CONFIG.BASE_URL; // Fallback inicial
let isDiscoveringAPI = false;

// Descobrir API no primeiro uso
const getApiUrl = async () => {
  if (!isDiscoveringAPI && API_CONFIG.getBaseUrl) {
    isDiscoveringAPI = true;
    try {
      API_URL = await API_CONFIG.getBaseUrl();
      console.log(`🌐 API descoberta: ${API_URL} (Platform: ${Platform.OS})`);
    } catch (error) {
      console.warn('⚠️ Erro ao descobrir API, usando fallback:', API_URL);
    }
    isDiscoveringAPI = false;
  }
  return API_URL;
};

console.log(`⏱️ Timeout configurado: ${API_CONFIG.TIMEOUT}ms`);


// Token storage
const TOKEN_KEY = '@scanplant_token';

// Salvar token
export const saveToken = async (token) => {
  try {
    await AsyncStorage.setItem(TOKEN_KEY, token);
  } catch (error) {
    console.error('Erro ao salvar token:', error);
  }
};

// Obter token
export const getToken = async () => {
  try {
    return await AsyncStorage.getItem(TOKEN_KEY);
  } catch (error) {
    console.error('Erro ao obter token:', error);
    return null;
  }
};

// Remover token
export const removeToken = async () => {
  try {
    await AsyncStorage.removeItem(TOKEN_KEY);
  } catch (error) {
    console.error('Erro ao remover token:', error);
  }
};

// Fazer requisição autenticada
const apiRequest = async (endpoint, options = {}) => {
  // Descobre a API URL dinamicamente
  const currentApiUrl = await getApiUrl();
  const token = await getToken();
  
  const headers = {
    'Content-Type': 'application/json',
    ...options.headers,
  };

  if (token) {
    headers['Authorization'] = `Bearer ${token}`;
  }

  try {
    const fullUrl = `${currentApiUrl}${endpoint}`;
    console.log(`📡 Fazendo requisição para: ${fullUrl}`);
    console.log(`📦 Método: ${options.method || 'GET'}`);
    if (options.body) {
      console.log(`📤 Body:`, options.body);
    }
    
    const response = await fetch(fullUrl, {
      ...options,
      headers,
    });

    console.log(`✅ Resposta recebida - Status: ${response.status}`);
    
    let data;
    const contentType = response.headers.get('content-type');
    
    if (contentType && contentType.includes('application/json')) {
      data = await response.json();
    } else {
      const text = await response.text();
      console.warn('⚠️ Resposta não é JSON:', text.substring(0, 200));
      data = { message: text };
    }

    if (!response.ok) {
      console.error(`❌ Erro na resposta (Status ${response.status}):`, data);
      const errorMessage = data.message || data.error || data.title || `Erro ${response.status}`;
      return { data: null, error: { message: errorMessage, status: response.status, details: data } };
    }

    return { data, error: null };
  } catch (error) {
    console.error('❌ API Error:', error);
    console.error('❌ Detalhes do erro:', error.message);
    console.error('❌ Stack:', error.stack);
    
    let errorMessage = error.message;
    if (error.message.includes('Network request failed')) {
      errorMessage = 'Erro de conexão. Verifique se a API está rodando.';
    } else if (error.message.includes('timeout')) {
      errorMessage = 'A requisição demorou muito. Tente novamente.';
    }
    
    return { data: null, error: { message: errorMessage } };
  }
};

// ==================== AUTENTICAÇÃO ====================

export const auth = {
  // Registrar
  signUp: async (email, password, name = '') => {
    console.log('🔵 signUp chamado com:', { email, password: '***', name });
    
    const { data, error } = await apiRequest('/auth/register', {
      method: 'POST',
      body: JSON.stringify({ email, password, name }),
    });

    console.log('🔵 Resposta signUp:', { data, error });

    if (data?.token) {
      await saveToken(data.token);
    }

    return { data, error };
  },

  // Login
  signIn: async (email, password) => {
    const { data, error } = await apiRequest('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ email, password }),
    });

    if (data?.token) {
      await saveToken(data.token);
    }

    return { data, error };
  },

  // Logout
  signOut: async () => {
    await removeToken();
    return { error: null };
  },

  // Obter usuário atual
  getCurrentUser: async () => {
    const token = await getToken();
    if (!token) {
      return { data: null, error: { message: 'Não autenticado' } };
    }

    const { data, error } = await apiRequest('/auth/me', {
      method: 'GET',
    });

    return { data: { user: data }, error };
  },

  // Atualizar perfil
  updateProfile: async (profileData) => {
    // Converter snake_case para PascalCase
    const pascalData = {
      Name: profileData.name,
      Phone: profileData.phone,
      Bio: profileData.bio,
      AvatarUrl: profileData.avatar_url,
      ExperienceLevel: profileData.experience_level,
      PlantPreference: profileData.plant_preference,
      City: profileData.city,
    };

    const response = await apiRequest('/auth/profile', {
      method: 'PUT',
      body: JSON.stringify(pascalData),
    });

    // Converter resposta de volta para snake_case
    if (response.data) {
      const user = response.data;
      response.data = [{
        id: user.id,
        email: user.email,
        name: user.name,
        phone: user.phone,
        bio: user.bio,
        avatar_url: user.avatarUrl,
        experience_level: user.experienceLevel,
        plant_preference: user.plantPreference,
        city: user.city,
        created_at: user.createdAt,
        updated_at: user.updatedAt
      }];
    }

    return response;
  },

  // Listar usuários
  getUsers: async () => {
    console.log('🔵 getUsers chamado');
    const result = await apiRequest('/auth/users', {
      method: 'GET',
    });
    console.log('🔵 getUsers resultado:', result);
    return result;
  },

  // Buscar usuário por ID
  getUserById: async (userId) => {
    console.log('🔵 getUserById chamado com ID:', userId);
    const result = await apiRequest(`/auth/users/${userId}`, {
      method: 'GET',
    });
    console.log('🔵 getUserById resultado:', result);
    return result;
  },
};

// ==================== PLANTAS ====================

export const database = {
  // Inserir planta
  insert: async (table, data) => {
    if (table !== 'plants') {
      return { data: null, error: { message: 'Tabela não suportada' } };
    }

    // Converter snake_case para PascalCase para a API C#
    const plantData = {
      ScientificName: data.scientific_name,
      CommonName: data.common_name,
      Family: data.family,
      Genus: data.genus,
      WikiDescription: data.wiki_description,
      CareInstructions: data.care_instructions,
      ImageData: data.image_data,
      Latitude: data.latitude,
      Longitude: data.longitude,
      City: data.city,
      LocationName: data.location_name,
      WateringFrequencyDays: data.watering_frequency_days,
      WateringFrequencyText: data.watering_frequency_text,
      ReminderEnabled: data.reminder_enabled || false,
      Notes: data.notes,
    };

    const response = await apiRequest('/plants', {
      method: 'POST',
      body: JSON.stringify(plantData),
    });

    // Converter a resposta de volta para snake_case
    if (response.data) {
      const plant = response.data;
      response.data = [{
        id: plant.id,
        scientific_name: plant.scientificName,
        common_name: plant.commonName,
        family: plant.family,
        genus: plant.genus,
        wiki_description: plant.wikiDescription,
        care_instructions: plant.careInstructions,
        image_data: plant.imageData,
        latitude: plant.latitude,
        longitude: plant.longitude,
        city: plant.city,
        location_name: plant.locationName,
        watering_frequency_days: plant.wateringFrequencyDays,
        watering_frequency_text: plant.wateringFrequencyText,
        reminder_enabled: plant.reminderEnabled,
        notes: plant.notes,
        user_id: plant.userId,
        created_at: plant.createdAt,
      }];
    }

    return response;
  },

  // Buscar plantas
  select: async (table, columns = '*', filters = {}) => {
    if (table === 'plants') {
      const userId = filters.user_id || filters.eq?.user_id;
      let endpoint = '/plants';

      if (userId === 'current') {
        endpoint = '/plants/my';
      } else if (userId) {
        endpoint = `/plants/user/${userId}`;
      }

      const response = await apiRequest(endpoint, {
        method: 'GET',
      });

      // Converter PascalCase para snake_case
      if (response.data && Array.isArray(response.data)) {
        response.data = response.data.map(plant => ({
          id: plant.id,
          scientific_name: plant.scientificName,
          common_name: plant.commonName,
          family: plant.family,
          genus: plant.genus,
          wiki_description: plant.wikiDescription,
          care_instructions: plant.careInstructions,
          image_data: plant.imageData,
          latitude: plant.latitude,
          longitude: plant.longitude,
          city: plant.city,
          location_name: plant.locationName,
          watering_frequency_days: plant.wateringFrequencyDays,
          watering_frequency_text: plant.wateringFrequencyText,
          reminder_enabled: plant.reminderEnabled,
          notes: plant.notes,
          user_id: plant.userId,
          created_at: plant.createdAt,
        }));
      }

      return response;
    } else if (table === 'profiles') {
      // Para perfis de usuário
      const userId = filters.id || filters.eq?.id;
      if (userId) {
        const response = await apiRequest(`/auth/users/${userId}`, {
          method: 'GET',
        });
        
        // Converter PascalCase para snake_case
        if (response.data) {
          const user = response.data;
          response.data = {
            id: user.id,
            email: user.email,
            name: user.name,
            phone: user.phone,
            bio: user.bio,
            avatar_url: user.avatarUrl,
            experience_level: user.experienceLevel,
            plant_preference: user.plantPreference,
            city: user.city,
            created_at: user.createdAt,
            updated_at: user.updatedAt
          };
        }
        
        return response;
      } else {
        return await apiRequest('/auth/users', {
          method: 'GET',
        });
      }
    }
    
    return { data: null, error: { message: 'Tabela não suportada' } };
  },

  // Atualizar planta
  update: async (table, data, filters) => {
    if (table !== 'plants') {
      return { data: null, error: { message: 'Tabela não suportada' } };
    }

    const plantId = filters.id || filters.eq?.id;
    if (!plantId) {
      return { data: null, error: { message: 'ID da planta não fornecido' } };
    }

    return await apiRequest(`/plants/${plantId}`, {
      method: 'PUT',
      body: JSON.stringify(data),
    });
  },

  // Deletar planta
  delete: async (table, filters) => {
    if (table !== 'plants') {
      return { data: null, error: { message: 'Tabela não suportada' } };
    }

    const plantId = filters.id || filters.eq?.id;
    if (!plantId) {
      return { data: null, error: { message: 'ID da planta não fornecido' } };
    }

    return await apiRequest(`/plants/${plantId}`, {
      method: 'DELETE',
    });
  },
};

// ==================== CHATS ====================

export const chats = {
  // Criar ou obter chat
  createOrGet: async (otherUserId) => {
    return await apiRequest('/chats', {
      method: 'POST',
      body: JSON.stringify({ otherUserId }),
    });
  },

  // Listar chats
  list: async () => {
    return await apiRequest('/chats', {
      method: 'GET',
    });
  },

  // Obter chat por ID
  get: async (chatId) => {
    return await apiRequest(`/chats/${chatId}`, {
      method: 'GET',
    });
  },

  // Marcar como lido
  markAsRead: async (chatId) => {
    return await apiRequest(`/chats/${chatId}/read`, {
      method: 'PUT',
    });
  },
};

// ==================== MENSAGENS ====================

export const messages = {
  // Enviar mensagem
  send: async (chatId, content) => {
    return await apiRequest('/messages', {
      method: 'POST',
      body: JSON.stringify({ chatId, content }),
    });
  },

  // Listar mensagens do chat
  list: async (chatId) => {
    return await apiRequest(`/messages/chat/${chatId}`, {
      method: 'GET',
    });
  },

  // Marcar mensagem como lida
  markAsRead: async (messageId) => {
    return await apiRequest(`/messages/${messageId}/read`, {
      method: 'PUT',
    });
  },

  // Contador de não lidas
  unreadCount: async () => {
    return await apiRequest('/messages/unread/count', {
      method: 'GET',
    });
  },
};

// Exportação compatível com Supabase
export const supabase = {
  auth,
  from: (table) => ({
    insert: (data) => database.insert(table, data),
    select: (columns = '*') => ({
      eq: (field, value) => ({
        order: (orderField, options) => ({
          then: async (resolve, reject) => {
            try {
              const result = await database.select(table, columns, { [field]: value });
              resolve(result);
            } catch (error) {
              reject(error);
            }
          }
        }),
        single: async () => {
          const result = await database.select(table, columns, { [field]: value });
          // Se já é um objeto único (profiles), retornar como está
          // Se é array, pegar o primeiro elemento
          const singleData = Array.isArray(result.data) ? result.data?.[0] : result.data;
          return { ...result, data: singleData || null };
        },
        // Para compatibilidade, retornar direto também
        then: async (resolve, reject) => {
          try {
            const result = await database.select(table, columns, { [field]: value });
            resolve(result);
          } catch (error) {
            reject(error);
          }
        }
      }),
      single: async () => {
        const result = await database.select(table, columns);
        // Se já é um objeto único (profiles), retornar como está
        // Se é array, pegar o primeiro elemento
        const singleData = Array.isArray(result.data) ? result.data?.[0] : result.data;
        return { ...result, data: singleData || null };
      },
      limit: (count) => ({
        then: async (resolve, reject) => {
          try {
            // Para chats, buscar os chats do usuário
            if (table === 'chats') {
              const result = await apiRequest('/chats', { method: 'GET' });
              resolve(result);
            } else {
              const result = await database.select(table, columns);
              resolve(result);
            }
          } catch (error) {
            reject(error);
          }
        }
      }),
      neq: (field, value) => ({
        then: async (resolve, reject) => {
          try {
            // Usado para listar usuários exceto o atual
            if (table === 'profiles') {
              const result = await apiRequest('/auth/users', { method: 'GET' });
              resolve(result);
            } else {
              const result = await database.select(table, columns);
              resolve(result);
            }
          } catch (error) {
            reject(error);
          }
        }
      }),
      order: (field, options) => ({
        then: async (resolve, reject) => {
          try {
            const result = await database.select(table, columns);
            resolve(result);
          } catch (error) {
            reject(error);
          }
        }
      }),
    }),
    update: (data) => ({
      eq: (field, value) => database.update(table, data, { [field]: value }),
    }),
    upsert: (data, options) => ({
      select: async () => {
        // Para profiles, usar endpoint de atualização de perfil
        if (table === 'profiles') {
          return await auth.updateProfile(data);
        }
        return { data: null, error: { message: 'Upsert não suportado para esta tabela' } };
      },
    }),
    delete: () => ({
      eq: (field, value) => database.delete(table, { [field]: value }),
    }),
  }),
};

// ==================== STORAGE (Mock) ====================
// As imagens são salvas como Base64 no banco, não precisa storage separado
export const storage = {
  upload: async (bucket, path, file) => {
    console.log('Storage upload não implementado - usando Base64 no banco');
    return { data: { path }, error: null };
  },
  getPublicUrl: (bucket, path) => {
    console.log('Storage getPublicUrl não implementado - usando Base64 do banco');
    return { publicURL: path, error: null };
  },
};
