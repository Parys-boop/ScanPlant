import React, { useState, useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  FlatList,
  TouchableOpacity,
  SafeAreaView,
  KeyboardAvoidingView,
  Platform,
  Image,
  ActivityIndicator,
  Alert,
  ScrollView,
} from 'react-native';
import { chats, messages, auth, database } from './api';
import { Feather } from '@expo/vector-icons';
import { Colors, Typography, Spacing, BorderRadius, Shadows, BaseStyles } from './styles/DesignSystem';

const PLACEHOLDER_IMAGE = require('../assets/placeholder.png');

// Função para resolver fontes de imagem (igual à do PlantGallery)
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

const ChatScreen = ({ route, navigation }) => {
  const { chatId: existingChatId, otherUserId, otherUserName } = route.params;
  
  const [messagesList, setMessagesList] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [loading, setLoading] = useState(true);
  const [sending, setSending] = useState(false);
  const [chatId, setChatId] = useState(existingChatId);
  const [currentUser, setCurrentUser] = useState(null);
  const [otherUserProfile, setOtherUserProfile] = useState({ name: otherUserName, avatarUrl: null });
  const [otherUserPlants, setOtherUserPlants] = useState([]);
  const [loadingPlants, setLoadingPlants] = useState(false);
  
  const flatListRef = useRef();
  
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

  // Buscar dados do outro usuário
  useEffect(() => {
    const fetchOtherUser = async () => {
      if (!otherUserId) return;
      
      try {
        const { data, error } = await auth.getUserById(otherUserId);
        if (error) throw error;
        
        if (data) {
          setOtherUserProfile({
            name: data.name || otherUserName,
            avatarUrl: data.avatarUrl || data.avatar_url || null,
            bio: data.bio,
            city: data.city,
          });
        }
      } catch (error) {
        console.error('Erro ao buscar dados do outro usuário:', error);
      }
    };
    
    fetchOtherUser();
  }, [otherUserId, otherUserName]);
  
  // Buscar plantas do outro usuário
  useEffect(() => {
    const fetchOtherUserPlants = async () => {
      if (!otherUserId) return;
      
      setLoadingPlants(true);
      try {
        const { data, error } = await database.select('plants', '*', { user_id: otherUserId });
        if (error) throw error;
        setOtherUserPlants(data || []);
      } catch (error) {
        console.error('Erro ao buscar plantas do outro usuário:', error);
      } finally {
        setLoadingPlants(false);
      }
    };
    
    fetchOtherUserPlants();
  }, [otherUserId]);
  
  // Buscar ou criar conversa e mensagens
  useEffect(() => {
    if (!currentUser) return;
    
    const fetchOrCreateChat = async () => {
      setLoading(true);
      try {
        let currentChatId = existingChatId;
        
        // Se não temos um chatId, criar ou obter um
        if (!currentChatId) {
          const { data: chatData, error: chatError } = await chats.createOrGet(otherUserId);
          if (chatError) throw chatError;
          currentChatId = chatData.id;
          setChatId(currentChatId);
        }
        
        // Buscar mensagens do chat
        const { data: messagesData, error: messagesError } = await messages.list(currentChatId);
        if (messagesError) throw messagesError;
        
        setMessagesList(messagesData || []);
      } catch (error) {
        console.error('Erro ao buscar/criar chat:', error);
        Alert.alert('Erro', 'Não foi possível carregar as mensagens.');
      } finally {
        setLoading(false);
      }
    };
    
    fetchOrCreateChat();
    
    // Poll a cada 3 segundos para novas mensagens
    const interval = setInterval(() => {
      if (chatId) {
        fetchMessages();
      }
    }, 3000);
    
    return () => clearInterval(interval);
  }, [currentUser, existingChatId, otherUserId, chatId]);
  
  // Função auxiliar para buscar mensagens
  const fetchMessages = async () => {
    if (!chatId) return;
    
    try {
      const { data, error } = await messages.list(chatId);
      if (!error && data) {
        setMessagesList(data);
      }
    } catch (error) {
      console.error('Erro ao atualizar mensagens:', error);
    }
  };
  
  // Enviar mensagem
  const sendMessage = async () => {
    if (!newMessage.trim() || !currentUser || !chatId) return;
    
    const messageText = newMessage.trim();
    setNewMessage('');
    setSending(true);
    
    try {
      const { data, error } = await messages.send(chatId, messageText);
      
      if (error) throw error;
      
      // Adicionar mensagem à lista
      setMessagesList(prev => [...prev, data]);
      
      // Rolar para o fim
      setTimeout(() => {
        flatListRef.current?.scrollToEnd({ animated: true });
      }, 100);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      Alert.alert('Erro', 'Não foi possível enviar a mensagem.');
      setNewMessage(messageText);
    } finally {
      setSending(false);
    }
  };
  
  // Renderizar uma mensagem
  const renderMessage = ({ item }) => {
    const isMine = currentUser && item.senderId === currentUser.id;
    
    return (
      <View style={[
        styles.messageContainer,
        isMine ? styles.myMessageContainer : styles.otherMessageContainer
      ]}>
        <View style={[
          styles.messageBubble,
          isMine ? styles.myMessageBubble : styles.otherMessageBubble
        ]}>
          <Text style={[
            styles.messageText,
            isMine ? styles.myMessageText : styles.otherMessageText
          ]}>
            {item.content}
          </Text>
        </View>
        <Text style={styles.messageTime}>
          {new Date(item.createdAt).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </Text>
      </View>
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
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity 
          style={styles.backButton} 
          onPress={() => navigation.goBack()}
        >
          <Feather name="arrow-left" size={24} color={Colors.text.secondary} />
        </TouchableOpacity>
        
        <View style={styles.profileButton}>
          <Image
            source={otherUserProfile?.avatarUrl ? resolveImageSource(otherUserProfile.avatarUrl) : PLACEHOLDER_IMAGE}
            style={styles.avatar}
          />
          <View style={styles.profileInfo}>
            <Text style={styles.username} numberOfLines={1}>
              {otherUserProfile?.name || otherUserName}
            </Text>
            <Text style={styles.status}>
              {otherUserProfile?.city || 'Entusiasta de plantas'}
            </Text>
          </View>
        </View>
        
        <View style={{ width: 40 }} />
      </View>
      
      <KeyboardAvoidingView 
        style={styles.keyboardAvoidingContainer}
        behavior={Platform.OS === 'ios' ? 'padding' : undefined}
        keyboardVerticalOffset={Platform.OS === 'ios' ? 100 : 0}
      >
        {/* Lista de mensagens */}
        {messagesList.length === 0 ? (
          <View style={styles.emptyContainer}>
            <Feather name="message-square" size={64} color={Colors.neutral[300]} />
            <Text style={styles.emptyText}>Nenhuma mensagem ainda</Text>
            <Text style={styles.emptySubtext}>
              Inicie uma conversa para trocar dicas e tirar dúvidas sobre plantas!
            </Text>
          </View>
        ) : (
          <FlatList
            ref={flatListRef}
            data={messagesList}
            keyExtractor={(item) => item.id.toString()}
            renderItem={renderMessage}
            contentContainerStyle={styles.messagesList}
          />
        )}
        
        {/* Input para nova mensagem */}
        <View style={styles.inputContainer}>
          <TextInput
            style={styles.input}
            placeholder="Digite sua mensagem..."
            value={newMessage}
            onChangeText={setNewMessage}
            multiline
          />
          <TouchableOpacity 
            style={[
              styles.sendButton,
              (!newMessage.trim() || sending) && styles.sendButtonDisabled
            ]}
            onPress={sendMessage}
            disabled={!newMessage.trim() || sending}
          >
            {sending ? (
              <ActivityIndicator size="small" color={Colors.text.inverse} />
            ) : (
              <Feather name="send" size={20} color={Colors.text.inverse} />
            )}
          </TouchableOpacity>
        </View>
      </KeyboardAvoidingView>
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
    paddingHorizontal: Spacing.md,
    paddingVertical: Spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: Colors.neutral[200],
  },
  backButton: {
    padding: Spacing.xs,
  },
  profileButton: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    marginHorizontal: Spacing.md,
  },
  avatar: {
    width: 40,
    height: 40,
    borderRadius: 20,
    marginRight: Spacing.md,
  },
  profileInfo: {
    flex: 1,
  },
  username: {
    ...Typography.bodyMedium,
    color: Colors.text.primary,
  },
  status: {
    ...Typography.caption,
    color: Colors.success,
  },
  keyboardAvoidingContainer: {
    flex: 1,
  },
  messagesList: {
    padding: Spacing.md,
  },
  messageContainer: {
    marginBottom: Spacing.md,
    maxWidth: '80%',
  },
  myMessageContainer: {
    alignSelf: 'flex-end',
  },
  otherMessageContainer: {
    alignSelf: 'flex-start',
  },
  messageBubble: {
    borderRadius: BorderRadius.lg,
    padding: Spacing.md,
    ...Shadows.sm,
  },
  myMessageBubble: {
    backgroundColor: Colors.primary[500],
    borderBottomRightRadius: 4,
  },
  otherMessageBubble: {
    backgroundColor: Colors.background.secondary,
    borderBottomLeftRadius: 4,
  },
  messageText: {
    ...Typography.body,
  },
  myMessageText: {
    color: Colors.text.inverse,
  },
  otherMessageText: {
    color: Colors.text.primary,
  },
  messageTime: {
    ...Typography.caption,
    color: Colors.text.tertiary,
    alignSelf: 'flex-end',
    marginTop: 4,
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: Spacing.md,
    borderTopWidth: 1,
    borderTopColor: Colors.neutral[200],
    backgroundColor: Colors.background.primary,
  },
  input: {
    flex: 1,
    backgroundColor: Colors.background.secondary,
    borderRadius: BorderRadius.lg,
    paddingHorizontal: Spacing.md,
    paddingVertical: Platform.OS === 'ios' ? Spacing.md : Spacing.sm,
    maxHeight: 120,
    ...Typography.body,
  },
  sendButton: {
    backgroundColor: Colors.primary[500],
    borderRadius: BorderRadius.full,
    width: 40,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: Spacing.md,
  },
  sendButtonDisabled: {
    backgroundColor: Colors.primary[300],
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
});

export default ChatScreen;