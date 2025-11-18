import React, { useState, useEffect, useCallback, useRef } from 'react';
import {
  View,
  Text,
  FlatList,
  Image,
  StyleSheet,
  TouchableOpacity,
  Alert,
  RefreshControl,
  SafeAreaView,
  StatusBar,
  ActivityIndicator,
  TextInput,
} from 'react-native';
import { database, auth, supabase } from './api'; // API C# com JWT automático
import { Feather } from '@expo/vector-icons'; // Importando ícones
import { LinearGradient } from 'expo-linear-gradient';

// Simulação do seu DesignSystem para o exemplo funcionar
const Colors = {
    primary: { 50: '#F0FDF4', 100: '#DCFCE7', 400: '#4ADE80', 500: '#22C55E', 600: '#16A34A'},
    background: { primary: '#FFFFFF', secondary: '#F8FAFC' },
    text: { primary: '#1E293B', secondary: '#475569', tertiary: '#94A3B8', inverse: '#FFFFFF' },
    neutral: { 300: '#CBD5E1', 400: '#94A3B8' },
    success: '#22C55E'
};
const Spacing = { xs: 4, sm: 8, md: 12, lg: 16, xl: 24, '2xl': 32 };
const BorderRadius = { lg: 12, xl: 16, full: 9999 };
const Shadows = {
    md: {
        shadowColor: "#000",
        shadowOffset: { width: 0, height: 2, },
        shadowOpacity: 0.1,
        shadowRadius: 8,
        elevation: 5,
    }
};
const Typography = {
    styles: {
        h2: { fontSize: 24, fontWeight: 'bold' },
        h3: { fontSize: 20, fontWeight: 'bold' },
        body: { fontSize: 16 },
        bodyMedium: { fontSize: 16, fontWeight: '600' },
        caption: { fontSize: 12, color: Colors.text.tertiary },
        small: { fontSize: 14, color: Colors.text.tertiary },
    }
};
// Fim da simulação do DesignSystem

const PLACEHOLDER_IMAGE = require('../assets/placeholder.png');

const resolveImageSource = (imageData) => {
  if (typeof imageData === 'string' && imageData.length > 0) {
    const trimmed = imageData.trim();
    if (trimmed.startsWith('data:') || trimmed.startsWith('http://') || trimmed.startsWith('https://')) {
      return { uri: trimmed };
    }
    const compact = trimmed.replace(/\s/g, '');
    if (compact.length > 0 && /^[A-Za-z0-9+/=]+$/.test(compact)) {
      return { uri: `data:image/jpeg;base64,${compact}` };
    }
  }
  return PLACEHOLDER_IMAGE;
};

const PlantGallery = ({ navigation, route }) => {
  const initialMode = route.params?.initialMode || 'personal';
  const [plants, setPlants] = useState([]);
  const [filteredPlants, setFilteredPlants] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const searchInputRef = useRef(null);
  const searchTextRef = useRef('');
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);
  const [searched, setSearched] = useState(false);
  const [viewMode, setViewMode] = useState(initialMode); // 'personal' ou 'community'
  // Quando initialMode é 'community', não deve haver toggle para voltar para 'personal'
  const [userInfo, setUserInfo] = useState(null);
  const [showFilters, setShowFilters] = useState(false);
  const [filters, setFilters] = useState({
    family: null,
    plantType: null, // 'tropical', 'suculenta', 'ornamental', 'hortaliça'
    hasReminder: false, // plantas com lembretes de rega
  });

  // Buscar informações do usuário atual
  useEffect(() => {
    const getCurrentUser = async () => {
      try {
        console.log("Tentando obter usuário atual...");
        const { data: userData } = await auth.getCurrentUser();
        console.log("Dados do usuário obtidos:", userData);
        if (userData?.user) {
          console.log("ID do usuário:", userData.user.id);
          setUserInfo(userData.user);
        } else {
          console.log("Usuário não autenticado ou dados não encontrados");
          // Definir viewMode como 'community' se o usuário não estiver logado
          if (viewMode === 'personal') {
            setViewMode('community');
            Alert.alert(
              'Não logado', 
              'Você precisa estar logado para ver suas plantas. Mostrando plantas da comunidade.',
              [{ text: 'OK' }, { text: 'Fazer Login', onPress: () => navigation.navigate('Login') }]
            );
          }
        }
      } catch (error) {
        console.error('Erro ao obter usuário atual:', error);
        // Em caso de erro, também mudamos para visão da comunidade
        if (viewMode === 'personal') {
          setViewMode('community');
          Alert.alert(
            'Erro de Autenticação', 
            'Não foi possível verificar seu login. Mostrando plantas da comunidade.',
            [{ text: 'OK' }, { text: 'Fazer Login', onPress: () => navigation.navigate('Login') }]
          );
        }
      }
    };
    
    getCurrentUser();
  }, [navigation]);

  const loadPlants = useCallback(async () => {
    try {
      let query;
      
      // Verificar se o usuário está autenticado
      if (!userInfo && viewMode === 'personal') {
        // Obter usuário atual diretamente ao invés de confiar apenas no estado
        const { data: freshUserData } = await auth.getCurrentUser();
        
        if (freshUserData?.user) {
          // Se conseguirmos obter o usuário atual, atualizamos o estado
          setUserInfo(freshUserData.user);
          
          // Buscar plantas do usuário recém-obtido
          console.log("Usando dados frescos do usuário:", freshUserData.user.id);
          query = supabase
            .from('plants')
            .select('*')
            .eq('user_id', freshUserData.user.id)
            .order('created_at', { ascending: false });
        } else {
          // Se mesmo após a tentativa de obter o usuário atual não conseguirmos,
          // então informamos ao usuário e mudamos para visão da comunidade
          console.log("Usuário não autenticado mesmo após tentativa de refresh");
          Alert.alert(
            'Sessão Expirada', 
            'Sua sessão expirou ou você não está logado. Por favor, faça login novamente para ver suas plantas.',
            [{ text: 'OK' }, { text: 'Login', onPress: () => navigation.navigate('Login') }]
          );
          
          setViewMode('community');
          setPlants([]);
          setLoading(false);
          setRefreshing(false);
          return;
        }
      } else if (viewMode === 'personal' && userInfo) {
        // Buscar apenas plantas do usuário atual do estado
        console.log("Buscando plantas do usuário:", userInfo.id);
        query = supabase
          .from('plants')
          .select('*')
          .eq('user_id', userInfo.id)
          .order('created_at', { ascending: false });
      } else {
        // Buscar plantas de todos os usuários para a visão da comunidade
        console.log("Buscando plantas da comunidade (todas as plantas)");
        query = supabase
          .from('plants')
          .select('*')
          .order('created_at', { ascending: false });
          
        // Não filtramos por user_id para mostrar todas as plantas na visão da comunidade
      }
      
      const { data, error } = await query;
      
      if (error) {
        console.error('Erro ao carregar plantas:', error);
        Alert.alert('Erro', 'Falha ao carregar plantas: ' + error.message);
        return;
      }
      
      if (data?.length === 0 && viewMode === 'personal') {
        Alert.alert(
          'Nenhuma planta encontrada', 
          'Você ainda não cadastrou nenhuma planta na sua coleção pessoal.'
        );
      }
      
      const plantsData = data || [];
      setPlants(plantsData);
      setFilteredPlants(plantsData);
    } catch (error) {
      console.error('Erro inesperado ao carregar plantas:', error);
      Alert.alert('Erro', 'Erro inesperado ao carregar plantas');
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  }, [viewMode, userInfo, navigation]);

  useEffect(() => {
    loadPlants();
  }, [loadPlants]);
  
  // Função para buscar plantas (igual SearchScreen - SEM useEffect!)
  const searchPlant = () => {
    if (!plants || plants.length === 0) {
      setFilteredPlants([]);
      setSearched(true);
      return;
    }
    
    setSearched(true);
    let filtered = [...plants];
    
    // Aplicar filtro de texto
    const term = (searchTextRef.current || '').trim();
    if (term) {
      const searchLower = term.toLowerCase();
      filtered = filtered.filter(plant => {
        const commonName = (plant.common_name || '').toLowerCase();
        const scientificName = (plant.scientific_name || '').toLowerCase();
        const family = (plant.family || '').toLowerCase();
        const location = (plant.location_name || '').toLowerCase();
        const city = (plant.city || '').toLowerCase();
        
        return commonName.includes(searchLower) || 
               scientificName.includes(searchLower) || 
               family.includes(searchLower) || 
               location.includes(searchLower) || 
               city.includes(searchLower);
      });
    }
  
    // Aplicar filtro de família
    if (filters.family) {
      const familyLower = filters.family.toLowerCase();
      filtered = filtered.filter(plant => 
        plant.family && plant.family.toLowerCase().includes(familyLower)
      );
    }
    
    // Aplicar filtro de tipo
    if (filters.plantType) {
      filtered = filtered.filter(plant => {
        const description = (plant.wiki_description || '').toLowerCase();
        const commonName = (plant.common_name || '').toLowerCase();
        
        switch (filters.plantType) {
          case 'tropical':
            return description.includes('tropical') || commonName.includes('tropical');
          case 'suculenta':
            return description.includes('suculenta') || commonName.includes('suculenta');
          case 'ornamental':
            return description.includes('ornamental') || commonName.includes('ornamental');
          case 'hortalica':
            return description.includes('hortaliça') || description.includes('hortalica') || 
                   commonName.includes('hortaliça') || commonName.includes('hortalica');
          default:
            return true;
        }
      });
    }
    
    // Aplicar filtro de lembrete
    if (filters.hasReminder) {
      filtered = filtered.filter(plant => 
        plant.reminder_enabled === true || plant.reminder_notification_id
      );
    }
    
    setFilteredPlants(filtered);
  };
  
  // Função para ver todas as plantas
  const fetchAllPlants = () => {
    setSearchTerm('');
    if (searchInputRef.current?.clear) {
      searchInputRef.current.clear();
    }
    searchTextRef.current = '';
    setSearched(false);
    setFilteredPlants(plants);
    setFilters({
      family: null,
      plantType: null,
      hasReminder: false,
    });
  };

  const onRefresh = () => {
    setRefreshing(true);
    loadPlants();
    fetchAllPlants();
  };
  
  const clearFilters = () => {
    setSearchText('');
    setFilters({
      family: null,
      plantType: null,
      hasReminder: false,
    });
    setShowFilters(false);
  };
  
  const toggleViewMode = () => {
    setViewMode(prev => prev === 'personal' ? 'community' : 'personal');
    setLoading(true);
  };

  const PlantItem = React.memo(({ item }) => {
    const isInCommunityView = viewMode === 'community';
    const isYourPlant = userInfo && item.user_id === userInfo.id;

    return (
      <TouchableOpacity 
        style={[
          styles.plantItem,
          isInCommunityView && isYourPlant && styles.myPlantInCommunity
        ]}
        onPress={() => navigation.navigate('PlantDetail', { plant: item })}
        activeOpacity={0.8}
      >
        <Image 
          source={resolveImageSource(item.image_data)} 
          style={styles.plantImage}
          resizeMode="cover"
        />
        <View style={styles.plantInfo}>
          <Text style={styles.commonName} numberOfLines={2}>
            {item.common_name || 'Nome não disponível'}
          </Text>
          <Text style={styles.scientificName} numberOfLines={1}>
            {item.scientific_name || 'Nome científico não disponível'}
          </Text>
          
          {/* Mostrar indicação do proprietário na visualização da comunidade */}
          {isInCommunityView && (
            <View style={styles.userInfoContainer}>
              <Feather 
                name={isYourPlant ? "user" : "users"} 
                size={14} 
                color={isYourPlant ? Colors.success : Colors.primary[500]} 
              />
              <Text 
                style={[
                  styles.userName, 
                  isYourPlant && { color: Colors.success }
                ]} 
                numberOfLines={1}
              >
                {isYourPlant ? 'Sua planta' : 'Comunidade'}
              </Text>
            </View>
          )}
          
          {/* Badge destacada para plantas do usuário na comunidade */}
          {isInCommunityView && isYourPlant && (
            <View style={styles.ownerBadge}>
              <Text style={styles.ownerBadgeText}>Sua</Text>
            </View>
          )}
          
          <View style={styles.locationContainer}>
            <Feather name="map-pin" size={14} color={Colors.text.tertiary} />
            <Text style={styles.location} numberOfLines={1}>
              {item.city || 'Local não disponível'}
            </Text>
          </View>
          
          {item.reminder_enabled ? (
            <View style={styles.reminderBadge}>
              <Feather name="bell" size={12} color={Colors.text.inverse} />
              <Text style={styles.reminderText}>
                {`Rega a cada ${item.watering_frequency_days || '?'} dia(s)`}
              </Text>
            </View>
          ) : null}
          
          {item.notes ? (
            <Text style={styles.notesPreview} numberOfLines={2}>
              {item.notes}
            </Text>
          ) : null}
        </View>
      </TouchableOpacity>
    );
  });

  const renderHeader = () => (
    <View style={styles.headerContent}>
      <View style={styles.headerRow}>
        <TouchableOpacity 
          style={styles.backButton} 
          onPress={() => navigation.goBack()}
        >
          <Feather name="arrow-left" size={24} color={Colors.text.secondary} />
        </TouchableOpacity>
        <View style={styles.headerTitleContainer}>
          <Text style={styles.headerTitle}>
            {viewMode === 'personal' ? 'Minha Coleção de Plantas' : 'Plantas da Comunidade'}
          </Text>
          <Text style={styles.headerSubtitle}>
            {viewMode === 'community' 
              ? `${filteredPlants.length} ${filteredPlants.length === 1 ? 'planta compartilhada' : 'plantas compartilhadas'} pela comunidade`
              : `${filteredPlants.length} ${filteredPlants.length === 1 ? 'planta encontrada' : 'plantas encontradas'} na sua coleção`
            }
          </Text>
        </View>
      </View>
      
      {/* Barra de pesquisa - Estilo SearchScreen */}
      <View style={styles.searchContainerNew}>
        <View style={styles.inputContainer}>
          <Feather name="tag" size={20} color="#94A3B8" style={styles.inputIcon} />
          <TextInput
            ref={searchInputRef}
            style={styles.input}
            placeholder="Digite o nome da planta (ex: Rosa, Girassol)..."
            placeholderTextColor="#94A3B8"
            onChangeText={(t) => { searchTextRef.current = t; }}
            onSubmitEditing={searchPlant}
          />
        </View>

        <View style={styles.buttonContainer}>
          <TouchableOpacity style={styles.searchButtonNew} onPress={searchPlant}>
            <Feather name="search" size={20} color="#FFFFFF" />
            <Text style={styles.buttonText}>Buscar</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.viewAllButton} onPress={fetchAllPlants}>
            <Feather name="list" size={20} color="#16A34A" />
            <Text style={[styles.buttonText, {color: "#16A34A"}]}>Ver Todas</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* Mostrar botões de alternância APENAS na tela de plantas pessoais */}
      {initialMode === 'personal' && viewMode === 'personal' && (
        <View style={styles.viewToggleContainer}>
          <TouchableOpacity 
            style={[
              styles.viewToggleButton, 
              styles.viewToggleButtonActive
            ]}
          >
            <Feather 
              name="user" 
              size={16} 
              color={Colors.primary[500]} 
            />
            <Text 
              style={[
                styles.viewToggleText, 
                styles.viewToggleTextActive
              ]}
            >
              Minhas Plantas
            </Text>
          </TouchableOpacity>
          
          <TouchableOpacity 
            style={styles.viewToggleButton}
            onPress={toggleViewMode}
          >
            <Feather 
              name="users" 
              size={16} 
              color={Colors.text.tertiary} 
            />
            <Text style={styles.viewToggleText}>
              Comunidade
            </Text>
          </TouchableOpacity>
        </View>
      )}
    </View>
  );

  const renderEmptyState = () => (
    <View style={styles.centerContainer}>
      {viewMode === 'personal' ? (
        // Estado vazio para a visualização pessoal
        <>
          <Feather name="plus-square" size={64} color={Colors.neutral[300]} />
          <Text style={styles.emptyText}>Nenhuma planta na sua coleção</Text>
          <Text style={styles.emptySubtext}>Adicione sua primeira planta para começar!</Text>
          <TouchableOpacity 
            style={styles.emptyButton}
            onPress={() => navigation.navigate('PhotoScreen')}
          >
            <Feather name="camera" size={18} color={Colors.text.inverse} />
            <Text style={styles.emptyButtonText}>Identificar Planta</Text>
          </TouchableOpacity>
        </>
      ) : (
        // Estado vazio para a visualização da comunidade
        <>
          <Feather name="users" size={64} color={Colors.neutral[300]} />
          <Text style={styles.emptyText}>Comunidade vazia</Text>
          <Text style={styles.emptySubtext}>Seja o primeiro a compartilhar uma planta!</Text>
          <TouchableOpacity 
            style={styles.emptyButton}
            onPress={() => navigation.navigate('PhotoScreen')}
          >
            <Feather name="camera" size={18} color={Colors.text.inverse} />
            <Text style={styles.emptyButtonText}>Identificar Planta</Text>
          </TouchableOpacity>
        </>
      )}
    </View>
  );

  if (loading) {
    return (
      <View style={styles.centerContainer}>
        <ActivityIndicator size="large" color={Colors.primary[500]} />
        <Text style={styles.loadingText}>Carregando sua coleção...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={Colors.background.secondary} />
      <FlatList
        data={filteredPlants}
        renderItem={({ item }) => <PlantItem item={item} />}
        keyExtractor={(item) => item.id.toString()}
        ListHeaderComponent={renderHeader}
        ListEmptyComponent={renderEmptyState}
        contentContainerStyle={styles.listContainer}
        refreshControl={
          <RefreshControl 
            refreshing={refreshing} 
            onRefresh={onRefresh}
            colors={[Colors.primary[500]]}
            tintColor={Colors.primary[500]}
          />
        }
        showsVerticalScrollIndicator={true}
        persistentScrollbar={true}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: Colors.background.secondary,
    height: '100%',
  },
  listContainer: {
    paddingHorizontal: Spacing.lg,
    paddingBottom: Spacing['2xl'],
  },
  headerContent: {
    paddingVertical: Spacing.xl,
    paddingTop: Spacing['2xl'],
    alignItems: 'flex-start',
    paddingHorizontal: Spacing.lg,
    width: '100%',
  },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
  },
  backButton: { 
    padding: 10, 
    borderRadius: 20, 
    backgroundColor: Colors.background.primary,
    marginRight: Spacing.md,
    ...Shadows.md,
  },
  headerTitleContainer: {
    flex: 1,
  },
  headerTitle: {
    ...Typography.styles.h2,
    color: Colors.text.primary,
  },
  headerSubtitle: {
    ...Typography.styles.body,
    color: Colors.text.secondary,
    marginTop: Spacing.xs,
  },
  plantItem: {
    backgroundColor: Colors.background.primary,
    borderRadius: BorderRadius.xl,
    marginBottom: Spacing.lg,
    ...Shadows.md,
    flexDirection: 'row',
    alignItems: 'center',
    overflow: 'hidden',
  },
  myPlantInCommunity: {
    borderLeftWidth: 4,
    borderLeftColor: Colors.success,
  },
  ownerBadge: {
    position: 'absolute',
    top: 8,
    right: 8,
    backgroundColor: Colors.success,
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  ownerBadgeText: {
    color: 'white',
    fontSize: 12,
    fontWeight: '600',
  },
  plantImage: {
    width: 100,
    height: '100%',
    minHeight: 120,
  },
  plantInfo: {
    flex: 1,
    padding: Spacing.lg,
  },
  commonName: {
    ...Typography.styles.bodyMedium,
    color: Colors.primary[600],
    marginBottom: Spacing.xs,
  },
  scientificName: {
    ...Typography.styles.caption,
    fontStyle: 'italic',
    color: Colors.text.secondary,
    marginBottom: Spacing.md,
  },
  userInfoContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: Spacing.sm,
  },
  userName: {
    marginLeft: Spacing.xs,
    color: Colors.text.secondary,
    fontWeight: '500',
    fontSize: 14,
  },
  locationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 'auto',
  },
  location: {
    ...Typography.styles.small,
    marginLeft: Spacing.xs,
  },
  reminderBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'flex-start',
    backgroundColor: Colors.primary[500],
    borderRadius: BorderRadius.full,
    paddingHorizontal: Spacing.sm,
    paddingVertical: Spacing.xs,
    marginTop: Spacing.sm,
    gap: Spacing.xs,
  },
  reminderText: {
    ...Typography.styles.small,
    color: Colors.text.inverse,
  },
  notesPreview: {
    ...Typography.styles.caption,
    color: Colors.text.secondary,
    marginTop: Spacing.xs,
  },
  centerContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: Colors.background.secondary,
    paddingHorizontal: Spacing.xl,
  },
  loadingText: {
    ...Typography.styles.body,
    marginTop: Spacing.lg,
    color: Colors.text.secondary,
  },
  emptyText: {
    ...Typography.styles.h3,
    textAlign: 'center',
    marginTop: Spacing.lg,
    color: Colors.text.secondary,
  },
  emptySubtext: {
    ...Typography.styles.body,
    textAlign: 'center',
    marginTop: Spacing.sm,
    marginBottom: Spacing.xl,
    color: Colors.text.tertiary,
  },
  emptyButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Colors.primary[500],
    borderRadius: BorderRadius.full,
    paddingHorizontal: Spacing.xl,
    paddingVertical: Spacing.lg,
    ...Shadows.md,
  },
  emptyButtonText: {
    ...Typography.styles.bodyMedium,
    color: Colors.text.inverse,
    marginLeft: Spacing.sm,
  },
  // Estilos para os componentes de filtro e busca
  searchContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginHorizontal: Spacing.md,
    marginVertical: Spacing.sm,
    paddingHorizontal: Spacing.md,
    paddingVertical: 8,
    backgroundColor: Colors.background.primary,
    borderRadius: BorderRadius.lg,
    borderWidth: 1,
    borderColor: Colors.neutral[300],
  },
  searchInput: {
    flex: 1,
    height: 36,
    fontSize: 16,
    color: Colors.text.primary,
    marginLeft: Spacing.xs,
  },
  // Novos estilos SearchScreen
  searchContainerNew: { 
    marginTop: 16, 
    marginHorizontal: 0,
    backgroundColor: '#FFFFFF', 
    borderRadius: 12, 
    padding: 16, 
    shadowColor: "#000", 
    shadowOffset: { width: 0, height: 2 }, 
    shadowOpacity: 0.05, 
    shadowRadius: 8, 
    elevation: 5, 
    borderWidth: 1, 
    borderColor: '#f1f5f9',
    width: '100%',
    alignSelf: 'stretch'
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#e2e8f0',
    paddingHorizontal: 12,
    marginBottom: 16,
  },
  inputIcon: {
    marginRight: 8,
  },
  input: {
    flex: 1,
    height: 50,
    fontSize: 16,
    color: '#1E293B',
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    gap: 12,
    marginBottom: 12,
  },
  searchButtonNew: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#22C55E',
    paddingVertical: 14,
    borderRadius: 8,
  },
  viewAllButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#DCFCE7',
    paddingVertical: 14,
    borderRadius: 8,
  },
  buttonText: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: 'bold',
    marginLeft: 8,
  },
  filterButtonOld: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#F8FAFC',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#e2e8f0',
  },
  filterButtonText: {
    marginLeft: 8,
    fontSize: 14,
    fontWeight: '600',
    color: '#475569',
  },
  filterButtonActive: {
    backgroundColor: Colors.primary[50],
  },
  filterPanel: {
    backgroundColor: Colors.background.primary,
    marginHorizontal: Spacing.md,
    marginVertical: Spacing.xs,
    padding: 12,
    borderRadius: BorderRadius.md,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  filterActions: {
    marginTop: 10,
  },
  applyFiltersButton: {
    backgroundColor: Colors.primary[500],
    paddingVertical: 10,
    borderRadius: BorderRadius.sm,
    alignItems: 'center',
  },
  applyFiltersText: {
    color: Colors.text.inverse,
    fontWeight: '600',
  },
  filterHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  filterTitle: {
    fontSize: 15,
    fontWeight: '600',
    color: Colors.text.primary,
  },
  clearFilterText: {
    fontSize: 13,
    color: Colors.primary[500],
  },
  filterSectionTitle: {
    fontSize: 13,
    fontWeight: '600',
    color: Colors.text.primary,
    marginBottom: 6,
    marginTop: 4,
  },
  filterOptions: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginBottom: 6,
    gap: 6,
  },
  filterOption: {
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: BorderRadius.sm,
    backgroundColor: Colors.neutral[200],
  },
  filterOptionActive: {
    backgroundColor: Colors.primary[100],
  },
  filterOptionText: {
    fontSize: 12,
    color: Colors.text.secondary,
  },
  filterOptionTextActive: {
    color: Colors.primary[600],
    fontWeight: 'bold',
  },
  locationFilterOption: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: Spacing.xs,
    marginBottom: Spacing.xs,
  },
  toggleOption: {
    width: 40,
    height: 20,
    borderRadius: 10,
    backgroundColor: Colors.neutral[300],
    marginHorizontal: Spacing.sm,
    justifyContent: 'center',
  },
  toggleOptionActive: {
    backgroundColor: Colors.primary[500],
  },
  toggleCircle: {
    width: 16,
    height: 16,
    borderRadius: 8,
    backgroundColor: Colors.background.primary,
    marginLeft: 2,
  },
  toggleCircleActive: {
    marginLeft: 22,
  },
  toggleText: {
    fontSize: 14,
    color: Colors.text.secondary,
  },
  viewToggleContainer: {
    flexDirection: 'row',
    backgroundColor: Colors.background.secondary,
    borderRadius: BorderRadius.lg,
    padding: 4,
    marginHorizontal: Spacing.md,
    marginTop: Spacing.md,
    marginBottom: Spacing.sm,
  },
  viewToggleButton: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: BorderRadius.md,
  },
  viewToggleButtonActive: {
    backgroundColor: Colors.background.primary,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.1,
    shadowRadius: 2,
    elevation: 1,
  },
  viewToggleText: {
    fontSize: 14,
    fontWeight: '500',
    color: Colors.text.tertiary,
    marginLeft: 6,
  },
  viewToggleTextActive: {
    color: Colors.primary[500],
    fontWeight: '600',
  },
});

export default PlantGallery;