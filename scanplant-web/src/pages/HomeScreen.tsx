import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Icons } from '../components/Icons';

export default function HomeScreen() {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-white">
      {/* Header com logo, assistente botânico e botão de perfil */}
      <header className="flex justify-between items-center px-6 py-4 bg-white border-b border-[var(--color-border-light)]">
        <img 
          src="/imagemlogotcc.png" 
          alt="ScanPlant Logo" 
          className="h-[60px] w-[110px] object-contain"
          onError={(e) => {
            // Fallback se a imagem não carregar
            e.currentTarget.style.display = 'none';
            e.currentTarget.parentElement?.querySelector('.fallback-logo')?.classList.remove('hidden');
          }}
        />
        <div className="fallback-logo hidden font-bold text-xl text-gray-800">ScanPlant</div>
        
        <div className="flex items-center gap-4">
          <button 
            onClick={() => navigate('/plant-assistant')}
            className="flex items-center gap-1 bg-[rgba(0,150,136,0.85)] text-white px-2 py-1 rounded-full font-bold border-[1.5px] border-[rgba(255,255,255,0.6)]"
            style={{ boxShadow: 'var(--shadow-md)' }}
          >
            <div className="w-7 h-7 rounded-full bg-[rgba(255,255,255,0.3)] flex items-center justify-center">
              <span className="text-base">🌿</span>
            </div>
            <span className="text-sm">Assistente</span>
          </button>
          
          <button 
            onClick={() => navigate('/profile')}
            className="w-10 h-10 bg-[var(--color-primary-100)] rounded-full flex items-center justify-center text-[var(--color-primary-600)] text-xl"
            style={{ boxShadow: 'var(--shadow-md)' }}
          >
            ⚙
          </button>
        </div>
      </header>

      <div className="overflow-y-auto pb-16">
        <div className="px-6">
          {/* Logo Container */}
          <div className="flex flex-col items-center pt-8 pb-12 px-6">
            <h2 className="text-2xl font-semibold text-[var(--color-text-primary)] text-center mb-2">
              Bem-vindo ao ScanPlant
            </h2>
            <p className="text-sm text-[var(--color-text-secondary)] text-center max-w-[280px]">
              Descubra o mundo das plantas com inteligência artificial
            </p>
          </div>

          {/* Action Cards */}
          <div className="mb-12">
            {/* Primary Card */}
            <button 
              onClick={() => navigate('/photo')}
              className="w-full bg-[var(--color-primary-500)] rounded-2xl p-8 flex flex-col items-center mb-6 border border-[var(--color-primary-400)]"
              style={{ boxShadow: 'var(--shadow-xl)' }}
            >
              <div 
                className="w-[70px] h-[70px] rounded-full bg-[var(--color-primary-400)] flex items-center justify-center mb-6 border-2 border-[var(--color-primary-300)]"
                style={{ boxShadow: 'var(--shadow-md)' }}
              >
                <span className="text-[28px]">❋</span>
              </div>
              <h3 className="text-xl font-semibold text-white mb-2">Identificar Planta</h3>
              <p className="text-base text-[var(--color-primary-100)] text-center">
                Tire uma foto e descubra informações detalhadas
              </p>
            </button>

            {/* Secondary Cards Row 1 */}
            <div className="flex gap-2 mb-4">
              <button 
                onClick={() => navigate('/gallery?mode=personal')}
                className="flex-1 bg-white rounded-2xl p-4 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px]"
                style={{ boxShadow: 'var(--shadow-lg)' }}
              >
                <div 
                  className="w-[55px] h-[55px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 border-[1.5px] border-[var(--color-primary-300)]"
                  style={{ boxShadow: 'var(--shadow-sm)' }}
                >
                  <span className="text-2xl">🌱</span>
                </div>
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1 text-center">Minhas Plantas</h4>
                <p className="text-xs text-[var(--color-text-tertiary)] text-center">Sua coleção</p>
              </button>

              <button 
                onClick={() => navigate('/gallery?mode=community')}
                className="flex-1 bg-white rounded-2xl p-4 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px]"
                style={{ boxShadow: 'var(--shadow-lg)' }}
              >
                <div 
                  className="w-[55px] h-[55px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 border-[1.5px] border-[var(--color-primary-300)]"
                  style={{ boxShadow: 'var(--shadow-sm)' }}
                >
                  <span className="text-2xl">👥</span>
                </div>
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1 text-center">Comunidade</h4>
                <p className="text-xs text-[var(--color-text-tertiary)] text-center">Plantas compartilhadas</p>
              </button>
            </div>

            {/* Secondary Cards Row 2 */}
            <div className="flex gap-2">
              <button 
                onClick={() => navigate('/search')}
                className="flex-1 bg-white rounded-2xl p-4 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px]"
                style={{ boxShadow: 'var(--shadow-lg)' }}
              >
                <div 
                  className="w-[55px] h-[55px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 border-[1.5px] border-[var(--color-primary-300)]"
                  style={{ boxShadow: 'var(--shadow-sm)' }}
                >
                  <span className="text-2xl">🔍</span>
                </div>
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1 text-center">Explorar</h4>
                <p className="text-xs text-[var(--color-text-tertiary)] text-center">Buscar plantas</p>
              </button>

              <button 
                onClick={() => navigate('/chats')}
                className="flex-1 bg-white rounded-2xl p-4 flex flex-col items-center border-2 border-[var(--color-primary-400)] min-h-[130px] relative overflow-visible"
                style={{ boxShadow: 'var(--shadow-lg)' }}
              >
                <span 
                  className="absolute -top-2 -right-2 bg-[var(--color-primary-500)] text-white text-[10px] font-bold px-2 py-0.5 rounded-full z-10"
                  style={{ boxShadow: 'var(--shadow-sm)', letterSpacing: '0.5px' }}
                >
                  NOVO
                </span>
                <div 
                  className="w-[55px] h-[55px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 border-[1.5px] border-[var(--color-primary-300)]"
                  style={{ boxShadow: 'var(--shadow-sm)' }}
                >
                  <span className="text-2xl">💬</span>
                </div>
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1 text-center">Chat</h4>
                <p className="text-xs text-[var(--color-text-tertiary)] text-center">Converse com outros</p>
              </button>
            </div>
          </div>

          {/* Features */}
          <div 
            className="bg-white rounded-2xl p-8 border border-[var(--color-primary-100)] mt-4 mb-8"
            style={{ boxShadow: 'var(--shadow-lg)' }}
          >
            <h3 className="text-xl font-semibold text-[var(--color-text-primary)] mb-6">Recursos</h3>
            
            {/* Novos recursos */}
            <div className="flex items-center mb-6">
              <span className="w-10 h-10 flex items-center justify-center text-2xl mr-4 bg-[var(--color-primary-50)] rounded-full text-[var(--color-primary-700)]">
                💬
              </span>
              <div className="flex-1">
                <div className="flex items-center mb-1">
                  <h4 className="text-base font-medium text-[var(--color-text-primary)] mr-2">
                    Chat com a Comunidade
                  </h4>
                  <span className="bg-[var(--color-primary-500)] text-white text-[8px] font-bold px-1 py-0.5 rounded-full">
                    NOVO
                  </span>
                </div>
                <p className="text-sm text-[var(--color-text-secondary)]">
                  Converse com outros entusiastas de plantas sobre suas dúvidas
                </p>
              </div>
            </div>
            
            <div className="flex items-center mb-6">
              <span className="w-10 h-10 flex items-center justify-center text-2xl mr-4 bg-[var(--color-primary-50)] rounded-full text-[var(--color-primary-700)]">
                🔍
              </span>
              <div className="flex-1">
                <div className="flex items-center mb-1">
                  <h4 className="text-base font-medium text-[var(--color-text-primary)] mr-2">
                    Exploração Aprimorada
                  </h4>
                  <span className="bg-[var(--color-primary-500)] text-white text-[8px] font-bold px-1 py-0.5 rounded-full">
                    NOVO
                  </span>
                </div>
                <p className="text-sm text-[var(--color-text-secondary)]">
                  Interface melhorada para descobrir novas espécies de plantas
                </p>
              </div>
            </div>
            
            {/* Recursos existentes */}
            <div className="flex items-center mb-6">
              <span className="w-8 flex items-center justify-center text-2xl mr-4">❋</span>
              <div className="flex-1">
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1">
                  Identificação Precisa
                </h4>
                <p className="text-sm text-[var(--color-text-secondary)]">
                  IA avançada para identificar milhares de espécies
                </p>
              </div>
            </div>

            <div className="flex items-center mb-6">
              <span className="w-8 flex items-center justify-center text-2xl mr-4">⌖</span>
              <div className="flex-1">
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1">
                  Localização GPS
                </h4>
                <p className="text-sm text-[var(--color-text-secondary)]">
                  Registre onde encontrou cada planta
                </p>
              </div>
            </div>

            <div className="flex items-center">
              <span className="w-8 flex items-center justify-center text-2xl mr-4">✓</span>
              <div className="flex-1">
                <h4 className="text-base font-medium text-[var(--color-text-primary)] mb-1">
                  Coleção Pessoal
                </h4>
                <p className="text-sm text-[var(--color-text-secondary)]">
                  Mantenha um registro de suas descobertas
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}