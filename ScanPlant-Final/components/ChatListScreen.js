import React, { useState, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  TouchableOpacity,
  Image,
  ActivityIndicator,
  SafeAreaView,
  StatusBar,
  Alert,
  ScrollView,
  Platform,
} from 'react-native';
import { chats, auth, database } from './api';
import { Feather } from '@expo/vector-icons';
import { Colors, Typography, Spacing, BorderRadius, Shadows, BaseStyles } from './styles/DesignSystem';

const PLACEHOLDER_IMAGE = require('../assets/placeholder.png');

// Função para resolver fontes de imagem
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

const ChatListScreen = ({ navigation }) => {
  const [chatsList, setChatsList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [currentUser, setCurrentUser] = useState(null);

  // Obter o usuário atual
  useEffect(() => {
    const getUser = async () => {
      try {
        const { data, error } = await auth.getCurrentUser();
        if (error) throw error;
        setCurrentUser(data.user);
      } catch (error) {
        console.error('Erro ao obter usuário atual:', error);
      }
    };
    
    getUser();
  }, []);

  // Buscar chats do usuário
  useEffect(() => {
    if (!currentUser) return;
    
    const fetchChats = async () => {
      setLoading(true);
      try {
        const { data, error } = await chats.list();
        
        if (error) throw error;
        
        console.log('📨 Chats recebidos:', JSON.stringify(data, null, 2));
        
        // Processar dados dos chats
        if (data && data.length > 0) {
          const processedChats = data.map(chat => {
            // Extrair dados do outro participante
            const otherParticipant = chat.otherParticipant || chat.OtherParticipant;
            const otherUserId = otherParticipant?.id || chat.otherUserId;
            const otherUserName = otherParticipant?.name || otherParticipant?.Name || 'Usuário';
            const otherUserAvatar = otherParticipant?.avatarUrl || otherParticipant?.AvatarUrl;
            
            console.log('👥 Processando chat:', {
              chatId: chat.id,
              otherUserId,
              otherUserName,
              otherUserAvatar
            });
            
            return {
              ...chat,
              otherUserId: otherUserId,
              otherUserName: otherUserName,
              otherUserAvatar: otherUserAvatar
            };
          });
          
          setChatsList(processedChats);
        } else {
          setChatsList([]);
        }
      } catch (error) {
        console.error('Erro ao buscar chats:', error);
        setChatsList([]);
      } finally {
        setLoading(false);
      }
    };
    
    fetchChats();
    
    // Poll a cada 5 segundos para atualizar chats
    const interval = setInterval(fetchChats, 5000);
    
    return () => clearInterval(interval);
  }, [currentUser]);
  
  // Função para truncar a mensagem longa
  const truncateMessage = (message, maxLength = 35) => {
    if (!message) return '';
    return message.length > maxLength ? message.substring(0, maxLength) + '...' : message;
  };
  
  // Renderizar item da lista de chats
  const renderChatItem = ({ item }) => {
    const messageTime = item.lastMessageTime ? new Date(item.lastMessageTime) : new Date();
    const now = new Date();
    const isToday = messageTime.toDateString() === now.toDateString();
    
    const timeString = isToday
      ? messageTime.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      : messageTime.toLocaleDateString();
    
    // Usar dados já processados do chat
    const displayName = item.otherUserName || 'Usuário';
    const displayAvatar = item.otherUserAvatar;
    
    console.log('👤 Renderizando chat:', { 
      chatId: item.id,
      otherUserId: item.otherUserId, 
      displayName,
      displayAvatar: displayAvatar ? '✅' : '❌'
    });
    
    return (
      <TouchableOpacity
        style={styles.chatItem}
        onPress={() => navigation.navigate('Chat', {
          chatId: item.id,
          otherUserId: item.otherUserId,
          otherUserName: displayName
        })}
      >
        <View style={styles.avatarContainer}>
          <Image
            source={displayAvatar ? resolveImageSource(displayAvatar) : PLACEHOLDER_IMAGE}
            style={styles.avatar}
          />
          {item.unreadCount > 0 && (
            <View style={styles.unreadBadge}>
              <Text style={styles.unreadText}>{item.unreadCount}</Text>
            </View>
          )}
        </View>
        
        <View style={styles.chatInfo}>
          <View style={styles.chatHeader}>
            <Text style={styles.username} numberOfLines={1}>
              {displayName}
            </Text>
            <Text style={styles.timeText}>{timeString}</Text>
          </View>
          
          <View style={styles.messagePreviewContainer}>
            {item.lastMessage ? (
              <>
                {item.isLastMessageFromMe && (
                  <Text style={styles.messageSender}>Você: </Text>
                )}
                <Text 
                  style={[
                    styles.lastMessage, 
                    item.unreadCount > 0 && !item.isLastMessageFromMe ? styles.unreadMessage : null
                  ]} 
                  numberOfLines={1}
                >
                  {truncateMessage(item.lastMessage)}
                </Text>
                {item.isLastMessageFromMe && item.unreadCount === 0 && (
                  <Feather 
                    name="check" 
                    size={14} 
                    color={Colors.primary[400]} 
                    style={styles.readIcon} 
                  />
                )}
              </>
            ) : (
              <Text style={styles.lastMessage} numberOfLines={1}>
                Iniciar uma conversa...
              </Text>
            )}
          </View>
        </View>
      </TouchableOpacity>
    );
  };

  if (loading) {
    return (
      <SafeAreaView style={styles.loadingContainer}>
        <ActivityIndicator size="large" color={Colors.primary[500]} />
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor={Colors.background.primary} />
      
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity 
          style={styles.backButton} 
          onPress={() => navigation.goBack()}
        >
          <Feather name="arrow-left" size={24} color={Colors.text.secondary} />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Conversas</Text>
        <TouchableOpacity
          style={styles.newChatButton}
          onPress={() => navigation.navigate('UserList')}
        >
          <Feather name="edit" size={20} color={Colors.primary[500]} />
        </TouchableOpacity>
      </View>
      
      {/* Lista de conversas */}
      {chatsList.length === 0 ? (
        <View style={styles.emptyContainer}>
          <Feather name="message-circle" size={64} color={Colors.neutral[300]} />
          <Text style={styles.emptyText}>Nenhuma conversa ainda</Text>
          <Text style={styles.emptySubtext}>
            Inicie uma conversa com outro dono de plantas para trocar dicas e tirar dúvidas!
          </Text>
          <TouchableOpacity
            style={styles.startChatButton}
            onPress={() => navigation.navigate('UserList')}
          >
            <Text style={styles.startChatButtonText}>Nova Conversa</Text>
          </TouchableOpacity>
        </View>
      ) : (
        <FlatList
          data={chatsList}
          keyExtractor={(item) => item.id.toString()}
          renderItem={renderChatItem}
          contentContainerStyle={styles.chatList}
        />
      )}
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    ...BaseStyles.container,
  },
  loadingContainer: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: Colors.background.primary,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: Spacing.lg,
    paddingVertical: Spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: Colors.neutral[200],
  },
  backButton: {
    padding: Spacing.xs,
  },
  headerTitle: {
    ...Typography.h5,
    color: Colors.text.primary,
  },
  newChatButton: {
    padding: Spacing.xs,
  },
  chatList: {
    paddingVertical: Spacing.md,
  },
  chatItem: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    paddingHorizontal: Spacing.lg,
    paddingVertical: Spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: Colors.neutral[100],
    backgroundColor: Colors.background.primary,
    marginHorizontal: Spacing.xs,
    marginVertical: Spacing.xs / 2,
    borderRadius: BorderRadius.md,
  },
  avatarContainer: {
    position: 'relative',
    marginRight: Spacing.md,
  },
  avatar: {
    width: 50,
    height: 50,
    borderRadius: 25,
  },
  unreadBadge: {
    position: 'absolute',
    top: 0,
    right: 0,
    backgroundColor: Colors.primary[500],
    borderRadius: 10,
    minWidth: 18,
    height: 18,
    justifyContent: 'center',
    alignItems: 'center',
  },
  unreadText: {
    color: Colors.text.inverse,
    fontSize: 10,
    fontWeight: 'bold',
  },
  chatInfo: {
    flex: 1,
  },
  chatHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 4,
  },
  username: {
    ...Typography.bodyMedium,
    color: Colors.text.primary,
    flex: 1,
  },
  timeText: {
    ...Typography.caption,
    color: Colors.text.tertiary,
    marginLeft: Spacing.sm,
  },
  messagePreviewContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: Spacing.xs / 2,
    width: '100%',
  },
  messageSender: {
    ...Typography.bodyMedium,
    color: Colors.text.secondary,
    marginRight: 2,
  },
  readIcon: {
    marginLeft: 4,
  },
  lastMessage: {
    ...Typography.body,
    color: Colors.text.secondary,
    flex: 1,
    marginRight: Spacing.xs,
  },
  unreadMessage: {
    ...Typography.bodyMedium,
    color: Colors.text.primary,
  },
  emptyContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingHorizontal: Spacing.xl,
  },
  emptyText: {
    ...Typography.h5,
    color: Colors.text.secondary,
    marginTop: Spacing.lg,
  },
  emptySubtext: {
    ...Typography.body,
    color: Colors.text.tertiary,
    marginTop: Spacing.md,
    textAlign: 'center',
  },
  startChatButton: {
    marginTop: Spacing.xl,
    backgroundColor: Colors.primary[500],
    paddingHorizontal: Spacing.xl,
    paddingVertical: Spacing.md,
    borderRadius: BorderRadius.lg,
  },
  startChatButtonText: {
    ...Typography.buttonText,
    color: Colors.text.inverse,
  },
  scrollView: {
    flex: 1,
  },
  setupContainer: {
    flex: 1,
    alignItems: 'center',
    padding: Spacing.xl,
    paddingTop: Spacing['2xl'],
  },
  setupTitle: {
    ...Typography.h4,
    color: Colors.text.primary,
    marginTop: Spacing.lg,
    marginBottom: Spacing.md,
  },
  setupText: {
    ...Typography.body,
    color: Colors.text.secondary,
    textAlign: 'center',
    marginBottom: Spacing.xl,
  },
  setupInstructions: {
    ...Typography.bodyMedium,
    color: Colors.text.primary,
    marginBottom: Spacing.md,
  },
  setupSteps: {
    alignSelf: 'stretch',
    backgroundColor: Colors.background.secondary,
    borderRadius: BorderRadius.lg,
    padding: Spacing.lg,
    marginBottom: Spacing.xl,
  },
  setupStep: {
    ...Typography.body,
    color: Colors.text.secondary,
    marginBottom: Spacing.sm,
  },
  setupCodePath: {
    ...Typography.bodyMedium,
    color: Colors.primary[600],
    backgroundColor: Colors.primary[50],
    padding: Spacing.sm,
    borderRadius: BorderRadius.md,
    marginTop: Spacing.xs,
    marginBottom: Spacing.xs,
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
  },
  setupNote: {
    ...Typography.caption,
    color: Colors.warning,
    textAlign: 'center',
  },
});

export default ChatListScreen;