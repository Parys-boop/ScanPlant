import React, { useState, useRef, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { GoogleGenAI } from "@google/genai";

const GEMINI_API_KEY = 'AIzaSyBj5g4N4bo7uEmd3c6C9ypgQugIAUbwvXo';

const Colors = {
  primary: { 50: '#f0fdf4', 100: '#dcfce7', 500: '#22c55e', 600: '#16a34a' },
  text: { primary: '#1E293B', secondary: '#475569', tertiary: '#94A3B8', inverse: '#FFFFFF' },
  background: { primary: '#FFFFFF', secondary: '#F8FAFC' },
  neutral: { 50: '#f9fafb', 100: '#f3f4f6' },
};

const PLANT_RESPONSES = {
  default: "Olá! Sou o assistente virtual do ScanPlant. Como posso ajudar com suas plantas hoje?",
  greeting: ["Olá! Como posso ajudar?", "Oi! Precisa de ajuda com plantas?", "Olá, sou o assistente do ScanPlant!"],
  notFound: "Desculpe, não tenho informações específicas sobre isso. Tente perguntar sobre rega, luz, plantio ou cuidados gerais com plantas.",
  
  water: [
    "A maioria das plantas precisa ser regada quando a camada superior do solo estiver seca. Evite encharcar as raízes.",
    "A frequência de rega depende do tipo de planta. Plantas suculentas precisam de menos água, enquanto plantas tropicais geralmente precisam de mais.",
    "Uma dica para rega: coloque seu dedo no solo até a primeira junta. Se estiver seco, está na hora de regar!"
  ],
  
  light: [
    "A maioria das plantas de interior precisa de luz indireta brilhante. Luz solar direta pode queimar as folhas de algumas plantas.",
    "Plantas com folhas variegadas (com manchas ou listras) geralmente precisam de mais luz para manter seus padrões.",
    "Se sua planta está esticada em direção à luz, provavelmente precisa ser movida para um local mais iluminado."
  ],
  
  soil: [
    "Um bom solo deve ter drenagem adequada. Adicionar perlita ou areia pode ajudar a melhorar a drenagem.",
    "A maioria das plantas de interior cresce bem em solo comum para vasos com um pouco de composto orgânico.",
    "Fertilizantes líquidos diluídos são ótimos para plantas de interior, utilize na metade da concentração recomendada."
  ],
  
  problems: [
    "Folhas amarelando geralmente indicam excesso de água ou falta de nutrientes.",
    "Pontas marrons nas folhas podem indicar ar muito seco ou excesso de fertilizante.",
    "Manchas brancas ou teias podem ser sinais de pragas como cochonilha ou ácaros. Examine a planta de perto."
  ],
};

const generateResponse = async (question: string): Promise<string> => {
  try {
    const ai = new GoogleGenAI({ apiKey: GEMINI_API_KEY });
    
    const prompt = `Você é um assistente especializado em cuidados com plantas. Responda de forma clara, amigável e em português brasileiro a seguinte pergunta sobre plantas: "${question}". Seja conciso (máximo 3-4 frases) e prático.`;
    
    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: prompt,
    });

    return response.text || PLANT_RESPONSES.notFound;
  } catch (error) {
    console.error('Erro na API Gemini:', error);
    
    // Fallback para respostas predefinidas em caso de erro
    const q = question.toLowerCase();
    
    if (q.includes('olá') || q.includes('oi') || q.includes('bom dia') || q.includes('boa tarde') || q.includes('boa noite')) {
      return PLANT_RESPONSES.greeting[Math.floor(Math.random() * PLANT_RESPONSES.greeting.length)];
    }
    
    if (q.includes('água') || q.includes('regar') || q.includes('rega')) {
      return PLANT_RESPONSES.water[Math.floor(Math.random() * PLANT_RESPONSES.water.length)];
    }
    
    if (q.includes('sol') || q.includes('luz') || q.includes('iluminação')) {
      return PLANT_RESPONSES.light[Math.floor(Math.random() * PLANT_RESPONSES.light.length)];
    }
    
    if (q.includes('solo') || q.includes('terra') || q.includes('fertilizante') || q.includes('adubo')) {
      return PLANT_RESPONSES.soil[Math.floor(Math.random() * PLANT_RESPONSES.soil.length)];
    }
    
    if (q.includes('problema') || q.includes('doença') || q.includes('praga') || 
        q.includes('amarelando') || q.includes('morrendo') || q.includes('murcha')) {
      return PLANT_RESPONSES.problems[Math.floor(Math.random() * PLANT_RESPONSES.problems.length)];
    }
    
    return PLANT_RESPONSES.notFound;
  }
};

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'bot';
}

export default function PlantAssistantChat() {
  const navigate = useNavigate();
  const [messages, setMessages] = useState<Message[]>([
    { id: '1', text: PLANT_RESPONSES.default, sender: 'bot' }
  ]);
  const [inputText, setInputText] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (inputText.trim() === '') return;
    
    const userMessage: Message = { id: Date.now().toString(), text: inputText, sender: 'user' };
    const currentQuestion = inputText;
    setMessages(prev => [...prev, userMessage]);
    setInputText('');
    
    // Adiciona mensagem de "digitando..."
    const typingMessage: Message = { 
      id: 'typing', 
      text: 'Digitando...', 
      sender: 'bot' 
    };
    setMessages(prev => [...prev, typingMessage]);
    
    try {
      const responseText = await generateResponse(currentQuestion);
      
      // Remove mensagem de "digitando..." e adiciona resposta real
      setMessages(prev => {
        const filtered = prev.filter(msg => msg.id !== 'typing');
        return [...filtered, { 
          id: Date.now().toString(), 
          text: responseText, 
          sender: 'bot' 
        }];
      });
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      setMessages(prev => {
        const filtered = prev.filter(msg => msg.id !== 'typing');
        return [...filtered, { 
          id: Date.now().toString(), 
          text: PLANT_RESPONSES.notFound, 
          sender: 'bot' 
        }];
      });
    }
  };

  return (
    <div style={{ minHeight: '100vh', backgroundColor: Colors.background.primary, display: 'flex', flexDirection: 'column' }}>
      {/* Header */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '16px 24px',
        borderBottom: '1px solid ' + Colors.neutral[100],
        backgroundColor: Colors.background.primary
      }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
          <div style={{
            width: 40,
            height: 40,
            borderRadius: 20,
            backgroundColor: Colors.primary[50],
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            border: '1px solid ' + Colors.primary[100]
          }}>
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={Colors.primary[500]} strokeWidth="2">
              <rect x="4" y="4" width="16" height="16" rx="2"/>
              <rect x="9" y="9" width="6" height="6"/>
              <line x1="9" y1="1" x2="9" y2="4"/>
              <line x1="15" y1="1" x2="15" y2="4"/>
              <line x1="9" y1="20" x2="9" y2="23"/>
              <line x1="15" y1="20" x2="15" y2="23"/>
              <line x1="20" y1="9" x2="23" y2="9"/>
              <line x1="20" y1="14" x2="23" y2="14"/>
              <line x1="1" y1="9" x2="4" y2="9"/>
              <line x1="1" y1="14" x2="4" y2="14"/>
            </svg>
          </div>
          <div>
            <div style={{ fontWeight: '500', fontSize: 16, color: Colors.text.primary }}>
              Especialista Botânico
            </div>
            <div style={{ fontSize: 14, color: Colors.text.tertiary }}>
              Pergunte sobre cuidados com plantas
            </div>
          </div>
        </div>
        <button
          onClick={() => navigate(-1)}
          style={{
            padding: 8,
            borderRadius: '50%',
            backgroundColor: Colors.neutral[100],
            border: 'none',
            cursor: 'pointer',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
        >
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke={Colors.text.secondary} strokeWidth="2">
            <line x1="18" y1="6" x2="6" y2="18"/>
            <line x1="6" y1="6" x2="18" y2="18"/>
          </svg>
        </button>
      </div>

      {/* Messages */}
      <div style={{ 
        flex: 1, 
        overflowY: 'auto', 
        padding: 24,
        display: 'flex',
        flexDirection: 'column',
        gap: 16
      }}>
        {messages.map((msg) => (
          <div
            key={msg.id}
            style={{
              maxWidth: '80%',
              alignSelf: msg.sender === 'user' ? 'flex-end' : 'flex-start',
              padding: 16,
              borderRadius: 12,
              backgroundColor: msg.sender === 'user' ? Colors.primary[500] : Colors.neutral[100],
              color: msg.sender === 'user' ? Colors.text.inverse : Colors.text.primary,
              fontSize: 16,
              lineHeight: '22px'
            }}
          >
            {msg.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={sendMessage}>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          padding: 16,
          gap: 12,
          borderTop: '1px solid ' + Colors.neutral[100]
        }}>
          <textarea
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendMessage();
              }
            }}
            placeholder="Digite sua pergunta..."
            rows={1}
            style={{
              flex: 1,
              padding: 12,
              backgroundColor: Colors.neutral[50],
              borderRadius: 12,
              border: 'none',
              outline: 'none',
              fontSize: 16,
              fontFamily: 'inherit',
              resize: 'none',
              maxHeight: 100
            }}
          />
          <button
            type="submit"
            style={{
              width: 44,
              height: 44,
              borderRadius: 22,
              backgroundColor: Colors.primary[50],
              border: '1px solid ' + Colors.primary[100],
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke={Colors.primary[600]} strokeWidth="2">
              <line x1="22" y1="2" x2="11" y2="13"/>
              <polygon points="22 2 15 22 11 13 2 9 22 2"/>
            </svg>
          </button>
        </div>
      </form>
    </div>
  );
}
