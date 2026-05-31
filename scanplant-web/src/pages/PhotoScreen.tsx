import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { auth, database } from '../api';
import { generateGeminiText, parseGeminiJson } from '../gemini';

// --- CONFIGURAÇÕES E CONSTANTES ---
const PLANT_ID_API_KEY = import.meta.env.VITE_PLANT_ID_API_KEY || '';
const PLANT_ID_API_URL = 'https://api.plant.id/v2/identify';
const REVERSE_GEOCODING_API_URL = 'https://nominatim.openstreetmap.org/reverse';

interface PlantData {
  scientific_name: string;
  family: string;
  genus: string;
  common_name: string;
  description: string;
  care_instructions: string;
  watering_frequency_days: number | null;
  watering_frequency_text: string;
}

interface LocationData {
  latitude: number;
  longitude: number;
  accuracy?: number;
}

export default function PhotoScreen() {
  const navigate = useNavigate();
  const videoRef = useRef<HTMLVideoElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);

  // --- ESTADOS DO COMPONENTE ---
  const [facing, setFacing] = useState<'user' | 'environment'>('environment');
  const [plantData, setPlantData] = useState<PlantData | null>(null);
  const [image, setImage] = useState<string | null>(null);
  const [location, setLocation] = useState<LocationData | null>(null);
  const [loading, setLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState('');
  const [exactLocation, setExactLocation] = useState('');
  const [cityName, setCityName] = useState('');
  const [gettingLocation, setGettingLocation] = useState(false);
  const [locationError, setLocationError] = useState('');
  const [reminderEnabled, setReminderEnabled] = useState(false);
  const [reminderFrequencyDays, setReminderFrequencyDays] = useState<number | null>(null);
  const [reminderFrequencyInput, setReminderFrequencyInput] = useState('');
  const [notes, setNotes] = useState('');
  const [stream, setStream] = useState<MediaStream | null>(null);
  const [cameraActive, setCameraActive] = useState(true);
  const [shareLocation, setShareLocation] = useState(false);
  const [shareInCommunity, setShareInCommunity] = useState(false);

  useEffect(() => {
    if (!shareInCommunity && shareLocation) {
      setShareLocation(false);
    }
  }, [shareInCommunity, shareLocation]);

  // --- LÓGICA DE PERMISSÕES E LOCALIZAÇÃO ---
  useEffect(() => {
    getLocation();
    startCamera();
  }, []);

  useEffect(() => {
    if (plantData?.watering_frequency_days) {
      const freqNumber = Math.max(1, Math.round(Number(plantData.watering_frequency_days)) || 1);
      setReminderFrequencyDays(freqNumber);
      setReminderFrequencyInput(String(freqNumber));
      setReminderEnabled(false);
      setNotes('');
    }
  }, [plantData?.watering_frequency_days]);

  useEffect(() => {
    return () => {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
    };
  }, [stream]);

  useEffect(() => {
    if (facing && cameraActive) {
      startCamera();
    }
  }, [facing]);

  const getLocation = () => {
    if ('geolocation' in navigator) {
      setGettingLocation(true);
      setLocationError('');
      console.log('Solicitando permissão de localização...');
      navigator.geolocation.getCurrentPosition(
        async (position) => {
          console.log('Localização obtida:', position.coords);
          const coords = {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude,
            accuracy: position.coords.accuracy,
          };
          setLocation(coords);
          try {
            const { exactLocation, city } = await getLocationName(coords.latitude, coords.longitude);
            console.log('Endereço definido:', { exactLocation, city });
            setExactLocation(exactLocation);
            setCityName(city);
          } finally {
            setGettingLocation(false);
          }
        },
        (error) => {
          console.error('Erro ao obter localização:', error);
          setGettingLocation(false);
          const message = getLocationErrorMessage(error);
          setLocationError(message);
          alert(message);
        },
        {
          enableHighAccuracy: true,
          timeout: 20000,
          maximumAge: 0
        }
      );
    } else {
      const message = 'Geolocalização não é suportada pelo seu navegador.';
      setLocationError(message);
      alert(message);
    }
  };

  const getLocationErrorMessage = (error: GeolocationPositionError) => {
    if (error.code === error.PERMISSION_DENIED) {
      return 'Permissão de localização negada. Ative a localização no navegador para registrar onde a planta foi encontrada.';
    }
    if (error.code === error.POSITION_UNAVAILABLE) {
      return 'Não foi possível obter sua localização agora. Verifique GPS/Wi-Fi e tente novamente.';
    }
    if (error.code === error.TIMEOUT) {
      return 'Tempo esgotado ao buscar localização. Tente novamente em um local com melhor sinal.';
    }
    return 'Não foi possível obter a localização.';
  };

  const getLocationName = async (latitude: number, longitude: number) => {
    try {
      console.log('Buscando endereço para coordenadas:', latitude, longitude);
      const response = await fetch(`${REVERSE_GEOCODING_API_URL}?lat=${latitude}&lon=${longitude}&format=json&addressdetails=1&zoom=18&accept-language=pt-BR`);
      if (!response.ok) {
        throw new Error(`Reverse geocoding falhou: ${response.status}`);
      }
      const data = await response.json();
      console.log('Resposta da API de geocodificação:', data);
      
      if (data && data.address) {
        const address = data.address;
        const city = address.city || address.town || address.village || address.municipality || address.city_district || address.county || address.state || 'Cidade Não Disponível';
        const state = address.state || '';
        const road = address.road || address.street || address.pedestrian || address.footway || address.path || '';
        const houseNumber = address.house_number || '';
        const neighborhood = address.neighbourhood || address.suburb || address.city_district || '';
        
        // Montar endereço: apenas rua e número (sem bairro)
        let exactLocationParts = [];
        if (road) {
          if (houseNumber) {
            exactLocationParts.push(`${road}, ${houseNumber}`);
          } else {
            exactLocationParts.push(road);
          }
        }
        if (!road && neighborhood) {
          exactLocationParts.push(neighborhood);
        }
        
        const exactLocation = exactLocationParts.length > 0 
          ? exactLocationParts.join(', ') 
          : (data.display_name || `${city}, ${state}`).split(',').slice(0, 2).join(', ').trim();
        
        console.log('Endereço processado:', { exactLocation, city });
        return { exactLocation: exactLocation || 'Endereço não disponível', city };
      }
    } catch (error) {
      console.error('Erro ao buscar nome da localização:', error);
    }
    return { exactLocation: 'Endereço não disponível', city: 'Cidade não disponível' };
  };

  const startCamera = async () => {
    try {
      if (stream) {
        stream.getTracks().forEach(track => track.stop());
      }
      
      const newStream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: facing },
        audio: false
      });
      
      setStream(newStream);
      
      if (videoRef.current) {
        videoRef.current.srcObject = newStream;
      }
    } catch (error) {
      console.error('Erro ao acessar câmera:', error);
      // Fallback for demo if camera fails (e.g. desktop without cam)
      // alert('Não foi possível acessar a câmera. Verifique as permissões.');
    }
  };

  // --- LÓGICA DE IDENTIFICAÇÃO (PLANT.ID + GEMINI AI) ---
  const identifyPlant = async (base64Image: string) => {
    if (!PLANT_ID_API_KEY) {
      alert('Chave da Plant.id não configurada. Defina VITE_PLANT_ID_API_KEY no arquivo .env.local.');
      return;
    }

    setLoading(true);
    setPlantData(null);
    setLoadingMessage('Analisando imagem...');

    try {
      const response = await fetch(PLANT_ID_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Api-Key': PLANT_ID_API_KEY
        },
        body: JSON.stringify({
          images: [base64Image],
          modifiers: ['similar_images'],
          plant_details: ['common_names', 'taxonomy', 'wiki_description']
        })
      });

      if (!response.ok) throw new Error('Erro na API Plant.id');
      const plantIdData = await response.json();

      if (plantIdData.suggestions && plantIdData.suggestions.length > 0) {
        const suggestion = plantIdData.suggestions[0];
        const plantDetails = suggestion.plant_details || {};
        const taxonomy = plantDetails.taxonomy || {};
        const scientificName =
          plantDetails.scientific_name ||
          taxonomy.scientific_name ||
          suggestion.plant_name ||
          'Nome científico não disponível';

        const plantIdFallback: PlantData = {
          scientific_name: scientificName,
          family: taxonomy.family || 'Não encontrada',
          genus: taxonomy.genus || 'Não encontrado',
          common_name: plantDetails.common_names?.[0] || suggestion.plant_name || scientificName,
          description: plantDetails.wiki_description?.value || 'Descrição não encontrada',
          care_instructions: 'Consulte um especialista para cuidados detalhados.',
          watering_frequency_days: null,
          watering_frequency_text: 'Frequência não fornecida',
        };

        setLoadingMessage('Buscando informações com IA...');
        const aiInfo = await fetchPlantInfoWithAI(scientificName, plantIdFallback);

        setPlantData({
          scientific_name: scientificName,
          family: aiInfo.family,
          genus: aiInfo.genus,
          common_name: aiInfo.common_name,
          description: aiInfo.description,
          care_instructions: aiInfo.care_instructions,
          watering_frequency_days: aiInfo.watering_frequency_days,
          watering_frequency_text: aiInfo.watering_frequency_text,
        });
      } else {
        alert('Nenhuma sugestão de planta encontrada.');
      }
    } catch (error: any) {
      alert(`Erro: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  const fetchPlantInfoWithAI = async (scientificName: string, fallback: PlantData) => {
    const sanitizeText = (value: any, fallbackValue: string) => {
      if (typeof value === 'string' && value.trim().length > 0) {
        return value.trim();
      }
      return fallbackValue;
    };

    const sanitizeNumber = (value: any, fallbackValue: number | null) => {
      const numberValue = Number(value);
      if (!Number.isFinite(numberValue) || numberValue <= 0) {
        return fallbackValue;
      }
      return Math.round(numberValue);
    };

    try {
      const prompt = `Forneça dados botânicos resumidos, dicas de cuidados e a frequência de rega da planta ${scientificName} em português brasileiro. Responda SOMENTE em formato JSON válido com esta estrutura exata: {"common_name": string, "family": string, "genus": string, "description": string, "care_instructions": string, "watering_frequency_text": string, "watering_frequency_days": number}. "watering_frequency_days" deve ser um número inteiro representando o intervalo recomendado em dias entre regas. Se não souber alguma informação, use null.`;

      const content = await generateGeminiText(prompt, {
        responseMimeType: 'application/json',
        temperature: 0.1,
      });
      const parsed = parseGeminiJson(content);

      return {
        common_name: sanitizeText(parsed?.common_name, fallback.common_name),
        family: sanitizeText(parsed?.family, fallback.family),
        genus: sanitizeText(parsed?.genus, fallback.genus),
        description: sanitizeText(parsed?.description, fallback.description),
        care_instructions: sanitizeText(parsed?.care_instructions, fallback.care_instructions),
        watering_frequency_text: sanitizeText(parsed?.watering_frequency_text, fallback.watering_frequency_text),
        watering_frequency_days: sanitizeNumber(parsed?.watering_frequency_days, fallback.watering_frequency_days),
      };
    } catch (error) {
      console.error('Erro na API Gemini:', error);
      return fallback;
    }
  };

  // --- FUNÇÕES DE CÂMERA E GALERIA ---
  const takePicture = () => {
    if (!videoRef.current || !canvasRef.current) return;
    
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const context = canvas.getContext('2d');
    
    if (!context) return;
    
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    context.drawImage(video, 0, 0);
    
    const imageData = canvas.toDataURL('image/jpeg', 0.7);
    setImage(imageData);
    setCameraActive(false);
    getLocation();
    
    if (stream) {
      stream.getTracks().forEach(track => track.stop());
    }
    
    identifyPlant(imageData);
  };

  const pickImage = async () => {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.onchange = async (e: any) => {
      const file = e.target?.files?.[0];
      if (!file) return;
      
      const reader = new FileReader();
      reader.onload = (event) => {
        const imageData = event.target?.result as string;
        setImage(imageData);
        getLocation();
        identifyPlant(imageData);
      };
      reader.readAsDataURL(file);
    };
    input.click();
  };

  const handleReminderToggle = (value: boolean) => {
    if (value && !reminderFrequencyDays) {
      const fallback = 3;
      setReminderFrequencyDays(fallback);
      setReminderFrequencyInput(String(fallback));
    }
    setReminderEnabled(value);
  };

  const handleFrequencyInputChange = (text: string) => {
    setReminderFrequencyInput(text);
    const numericValue = Number(text.replace(/[^0-9]/g, ''));
    if (Number.isFinite(numericValue) && numericValue > 0) {
      setReminderFrequencyDays(Math.round(numericValue));
    }
  };

  // --- AÇÕES DO USUÁRIO ---
  const handleCancel = () => {
    setImage(null);
    setPlantData(null);
    setReminderEnabled(false);
    setReminderFrequencyDays(null);
    setReminderFrequencyInput('');
    setNotes('');
    setLocationError('');
    setShareLocation(false);
    setShareInCommunity(false);
    setCameraActive(true);
    setFacing('environment');
  };

  const openInMaps = () => {
    if (!location) return;
    const { latitude, longitude } = location;
    const url = `https://www.google.com/maps?q=${latitude},${longitude}`;
    window.open(url, '_blank');
  };

  // --- FUNÇÃO DE SALVAR ---
  const saveData = async () => {
    if (!plantData || !location || !image) {
      alert('Dados Incompletos: Aguarde a identificação da planta e a localização estarem prontas.');
      return;
    }

    if (reminderEnabled && (!reminderFrequencyDays || reminderFrequencyDays <= 0)) {
      alert('Intervalo inválido: Informe em quantos dias deseja receber o lembrete de rega.');
      return;
    }

    setLoading(true);
    setLoadingMessage('Salvando na sua coleção...');

    try {
      const { data: userData } = await auth.getCurrentUser();
      if (!userData?.user?.id) {
        throw new Error('Usuário não está logado.');
      }

      const plantRecord = {
        scientific_name: plantData.scientific_name,
        common_name: plantData.common_name,
        wiki_description: plantData.description,
        care_instructions: plantData.care_instructions,
        family: plantData.family,
        genus: plantData.genus,
        latitude: location.latitude,
        longitude: location.longitude,
        city: cityName.trim() || 'Cidade não informada',
        location_name: exactLocation.trim() || 'Local não informado',
        image_data: image,
        watering_frequency_days: reminderEnabled ? reminderFrequencyDays : plantData.watering_frequency_days,
        watering_frequency_text: plantData.watering_frequency_text,
        reminder_enabled: reminderEnabled,
        notes: notes,
        is_location_public: shareInCommunity && shareLocation,
        is_in_community: shareInCommunity,
        user_id: userData.user.id,
      };

      const { error } = await database.insert('plants', plantRecord);

      if (error) throw error;

      alert('Sucesso: Planta salva na sua coleção!');
      navigate('/home');
    } catch (error: any) {
      console.error('Erro ao salvar:', error);
      alert(`Erro ao Salvar: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  // --- RENDERIZAÇÃO ---
  return (
    <div className="min-h-screen bg-[#F8FAFC]">
      <div className="overflow-y-auto pb-20 sm:pb-24" style={{ minHeight: '100vh' }}>
        <div className="responsive-shell py-4 sm:py-6">
          {/* Header com botão voltar */}
          <div className="flex items-center gap-2 sm:gap-3 mb-5 sm:mb-6">
            <button 
              onClick={() => navigate(-1)}
              className="p-2 rounded-full bg-[#F1F5F9] mr-2"
            >
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#475569" strokeWidth="2">
                <line x1="19" y1="12" x2="5" y2="12"></line>
                <polyline points="12 19 5 12 12 5"></polyline>
              </svg>
            </button>
            <div className="flex-1 text-center">
              <h1 className="text-2xl sm:text-[28px] font-bold text-[#1E293B] leading-tight">Identificar Planta</h1>
              <p className="text-sm sm:text-base text-[#64748B] mt-1">Capture ou selecione uma foto para análise</p>
            </div>
          </div>

          <div className="lg:grid lg:grid-cols-12 lg:gap-5 xl:gap-6 lg:items-start">
            <div className="lg:col-span-7 xl:col-span-8">
              <div className="lg:max-w-[820px] lg:mx-auto">
                {/* Área de Imagem/Câmera */}
                {image ? (
                  <div className="h-[240px] sm:h-[300px] md:h-[360px] lg:h-[320px] xl:h-[360px] rounded-2xl overflow-hidden mb-4 relative">
                    <img src={image} alt="Plant" className="w-full h-full object-cover" />
                    <button onClick={handleCancel} className="absolute top-2 right-2 bg-white/80 p-2 rounded-full text-red-500 font-bold">✕</button>
                  </div>
                ) : cameraActive ? (
                  <div className="h-[240px] sm:h-[300px] md:h-[360px] lg:h-[320px] xl:h-[360px] rounded-2xl overflow-hidden bg-black mb-4 relative">
                    <video ref={videoRef} autoPlay playsInline muted className="w-full h-full object-cover" />
                    <canvas ref={canvasRef} style={{ display: 'none' }} />
                  </div>
                ) : (
                  <div className="h-[240px] sm:h-[300px] md:h-[360px] lg:h-[320px] xl:h-[360px] rounded-2xl bg-gray-200 flex items-center justify-center mb-4">
                    <button 
                      onClick={() => setCameraActive(true)}
                      className="bg-[#4CAF50] text-white px-6 py-3 rounded-lg font-bold"
                    >
                      Ativar Câmera
                    </button>
                  </div>
                )}

                {/* Controles */}
                <div className="flex justify-between sm:justify-around lg:justify-center items-center mb-4 gap-3 sm:gap-4 lg:gap-10">
                  <button onClick={pickImage} className="p-3 lg:p-3.5 rounded-full lg:bg-white lg:shadow-sm">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#475569" strokeWidth="2">
                      <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                      <circle cx="8.5" cy="8.5" r="1.5"></circle>
                      <polyline points="21 15 16 10 5 21"></polyline>
                    </svg>
                  </button>
                  <button 
                    onClick={takePicture}
                    disabled={!cameraActive || !!image}
                    className="w-[64px] h-[64px] sm:w-[70px] sm:h-[70px] lg:w-[74px] lg:h-[74px] rounded-full bg-[#4CAF50] flex items-center justify-center disabled:opacity-50 disabled:bg-gray-400 shrink-0"
                  >
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" strokeWidth="2">
                      <path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path>
                      <circle cx="12" cy="13" r="4"></circle>
                    </svg>
                  </button>
                  <button 
                    onClick={() => setFacing(f => f === 'environment' ? 'user' : 'environment')}
                    className="p-3 lg:p-3.5 rounded-full lg:bg-white lg:shadow-sm"
                  >
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#475569" strokeWidth="2">
                      <polyline points="23 4 23 10 17 10"></polyline>
                      <polyline points="1 20 1 14 7 14"></polyline>
                      <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
                    </svg>
                  </button>
                </div>

                {/* Loading */}
                {loading && (
                  <div className="flex flex-col items-center my-6">
                    <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-[#4CAF50]"></div>
                    <p className="mt-3 text-base text-[#475569]">{loadingMessage}</p>
                  </div>
                )}
              </div>
            </div>

            {/* Card de Localização */}
            <div className="bg-white rounded-xl p-4 mb-4 shadow-sm lg:col-span-5 xl:col-span-4 lg:mt-0 lg:sticky lg:top-6">
            <h2 className="text-lg font-bold text-[#1E293B] mb-3 pb-2 border-b border-[#F1F5F9]">Localização da Captura</h2>
            {location ? (
              <>
                <InfoRow icon="📍" label="Endereço sugerido" value={exactLocation || 'Local não informado'} />
                <InfoRow icon="☀️" label="Cidade sugerida" value={cityName || 'Cidade não informada'} />
                <InfoRow icon="🧭" label="Coordenadas" value={`${location.latitude.toFixed(5)}, ${location.longitude.toFixed(5)}`} />
                {typeof location.accuracy === 'number' && (
                  <p className={`text-[13px] mb-3 ${location.accuracy > 100 ? 'text-[#B45309]' : 'text-[#64748B]'}`}>
                    Precisão aproximada: {Math.round(location.accuracy)}m
                    {location.accuracy > 100 ? '. Pode estar imprecisa; confira no mapa e corrija abaixo.' : ''}
                  </p>
                )}

                <label className="block text-sm text-[#475569] mb-1.5">Corrigir endereço/local</label>
                <input
                  type="text"
                  value={exactLocation}
                  onChange={(e) => setExactLocation(e.target.value)}
                  placeholder="Ex.: Rua das Flores, 123"
                  className="w-full border border-[#E2E8F0] rounded-lg px-3 py-2.5 text-base text-[#0F172A] mb-3"
                />

                <label className="block text-sm text-[#475569] mb-1.5">Corrigir cidade</label>
                <input
                  type="text"
                  value={cityName}
                  onChange={(e) => setCityName(e.target.value)}
                  placeholder="Ex.: São Paulo"
                  className="w-full border border-[#E2E8F0] rounded-lg px-3 py-2.5 text-base text-[#0F172A] mb-3"
                />
                <div className="flex flex-col sm:flex-row gap-2">
                  <button
                    onClick={getLocation}
                    disabled={gettingLocation}
                    className="flex-1 bg-[#DCFCE7] text-[#16A34A] font-bold py-3 rounded-lg disabled:opacity-60"
                  >
                    {gettingLocation ? 'Atualizando...' : 'Atualizar localização'}
                  </button>
                  <button
                    onClick={openInMaps}
                    className="flex-1 bg-[#F1F5F9] text-[#334155] font-bold py-3 rounded-lg"
                  >
                    Abrir mapa
                  </button>
                </div>
              </>
            ) : (
              <>
                <p className="text-base text-[#64748B]">
                  {gettingLocation ? 'Obtendo localização...' : (locationError || 'Localização ainda não obtida.')}
                </p>
                <button
                  onClick={getLocation}
                  disabled={gettingLocation}
                  className="w-full bg-[#DCFCE7] text-[#16A34A] font-bold py-3 rounded-lg mt-3 disabled:opacity-60"
                >
                  {gettingLocation ? 'Buscando...' : 'Tentar novamente'}
                </button>
              </>
            )}
            </div>
          </div>

          {/* Card de Lembrete */}
          <div className="bg-white rounded-xl p-4 mb-4 shadow-sm">
            <div className="flex justify-between items-center mb-3">
              <h2 className="text-lg font-bold text-[#1E293B]">Lembrete de Rega</h2>
              <div className="flex items-center gap-2">
                <span className="text-sm text-[#475569]">{reminderEnabled ? 'Ativado' : 'Desativado'}</span>
                <label className="relative inline-block w-12 h-6">
                  <input
                    type="checkbox"
                    checked={reminderEnabled}
                    onChange={(e) => handleReminderToggle(e.target.checked)}
                    className="sr-only peer"
                  />
                  <span className="absolute cursor-pointer inset-0 bg-[#CBD5F5] rounded-full peer-checked:bg-[#86EFAC] transition-colors"></span>
                  <span className="absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition-transform peer-checked:translate-x-6"></span>
                </label>
              </div>
            </div>
            <p className="text-sm text-[#64748B] mb-3">
              {plantData?.watering_frequency_text || 'A IA recomendará a frequência ideal após a identificação.'}
            </p>
            {reminderEnabled && (
              <>
                <label className="block text-sm text-[#475569] mb-1.5">Intervalo entre regas (em dias)</label>
                <input
                  type="number"
                  value={reminderFrequencyInput}
                  onChange={(e) => handleFrequencyInputChange(e.target.value)}
                  placeholder="Ex.: 3"
                  className="w-full border border-[#E2E8F0] rounded-lg px-3 py-2.5 text-base text-[#0F172A]"
                />
                <p className="text-[13px] text-[#475569] mt-2">
                  Você receberá notificações a cada {reminderFrequencyDays || '?'} dia(s).
                </p>
              </>
            )}
          </div>

          {/* Card de Resultado */}
          {plantData && (
            <div className="bg-white rounded-xl p-4 mb-4 shadow-sm">
              <h2 className="text-lg font-bold text-[#1E293B] mb-3 pb-2 border-b border-[#F1F5F9]">Resultado da Análise</h2>
              <InfoRow icon="🍃" label="Nome Científico" value={plantData.scientific_name} isItalic />
              <InfoRow icon="🏷️" label="Nome Popular" value={plantData.common_name} />
              <InfoRow icon="📖" label="Família" value={plantData.family} />
              <InfoRow icon="🔖" label="Gênero" value={plantData.genus} />
              <InfoRow icon="📝" label="Descrição" value={plantData.description} isMultiline />
              <InfoRow icon="💧" label="Guia de Cuidados" value={plantData.care_instructions} isMultiline />
            </div>
          )}

          {/* Card de Anotações */}
          <div className="bg-white rounded-xl p-4 mb-4 shadow-sm">
            <h2 className="text-lg font-bold text-[#1E293B] mb-3 pb-2 border-b border-[#F1F5F9]">Anotações da Planta</h2>
            <p className="text-[13px] text-[#94A3B8] mb-2">Registre observações específicas.</p>
            <textarea
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              placeholder="Ex.: Prefere luz indireta de manhã e pouca água no inverno."
              className="w-full border border-[#E2E8F0] rounded-xl p-3 min-h-[120px] text-base text-[#1E293B]"
            />
          </div>

          {/* Card de Privacidade */}
          <div className="bg-white rounded-xl p-4 mb-4 shadow-sm">
            <h2 className="text-lg font-bold text-[#1E293B] mb-1">Privacidade</h2>
            <p className="text-[13px] text-[#94A3B8] mb-4">
              Escolha se esta planta fica só na sua coleção ou se também aparece para a comunidade.
            </p>

            <div className="flex justify-between items-start mb-4 pb-4 border-b border-[#F1F5F9]">
              <div className="flex-1 pr-4">
                <p className="text-sm font-semibold text-[#1E293B]">Compartilhar com a comunidade</p>
                <p className="text-xs text-[#64748B] mt-0.5">
                  Desativado: a planta fica salva apenas para você. Ativado: outras pessoas podem ver a planta na galeria pública.
                </p>
              </div>
              <label className="relative inline-block w-12 h-6 flex-shrink-0">
                <input
                  type="checkbox"
                  checked={shareInCommunity}
                  onChange={(e) => setShareInCommunity(e.target.checked)}
                  className="sr-only peer"
                />
                <span className="absolute cursor-pointer inset-0 bg-[#CBD5E1] rounded-full peer-checked:bg-[#4CAF50] transition-colors"></span>
                <span className="absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition-transform peer-checked:translate-x-6"></span>
              </label>
            </div>

            <div className={`flex justify-between items-start ${shareInCommunity ? '' : 'opacity-50'}`}>
              <div className="flex-1 pr-4">
                <p className="text-sm font-semibold text-[#1E293B]">Mostrar localização da planta</p>
                <p className="text-xs text-[#64748B] mt-0.5">
                  Use apenas se for seguro. Se a planta estiver em casa ou em um local privado, deixe desativado.
                </p>
                {!shareInCommunity && (
                  <p className="text-xs text-[#16A34A] mt-2">
                    Disponível somente quando a planta for compartilhada com a comunidade.
                  </p>
                )}
              </div>
              <label className="relative inline-block w-12 h-6 flex-shrink-0">
                <input
                  type="checkbox"
                  checked={shareInCommunity && shareLocation}
                  disabled={!shareInCommunity}
                  onChange={(e) => setShareLocation(e.target.checked)}
                  className="sr-only peer"
                />
                <span className="absolute cursor-pointer inset-0 bg-[#CBD5E1] rounded-full peer-checked:bg-[#4CAF50] transition-colors peer-disabled:cursor-not-allowed"></span>
                <span className="absolute left-1 top-1 w-4 h-4 bg-white rounded-full transition-transform peer-checked:translate-x-6"></span>
              </label>
            </div>
          </div>

          {/* Botões de Ação */}
          <div className="flex flex-col sm:flex-row gap-3 mt-4">
            <button
              onClick={saveData}
              disabled={!plantData || loading}
              className="flex-1 bg-[#4CAF50] text-white font-bold py-3.5 rounded-lg disabled:opacity-50"
            >
              Salvar Planta
            </button>
            <button
              onClick={handleCancel}
              className="flex-1 bg-[#F1F5F9] text-[#475569] font-bold py-3.5 rounded-lg"
            >
              Cancelar
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

const InfoRow = ({ icon, label, value, isItalic, isMultiline }: any) => (
  <div className="flex mb-3">
    <span className="text-lg mr-3">{icon}</span>
    <div className="flex-1 min-w-0">
      <p className="text-sm text-[#94A3B8] mb-0.5">{label}</p>
      <p className={`text-base text-[#334155] ${isItalic ? 'italic' : ''} ${isMultiline ? 'leading-[22px]' : ''}`}>
        {value}
      </p>
    </div>
  </div>
);
