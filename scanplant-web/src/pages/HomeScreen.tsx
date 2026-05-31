import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Icons } from '../components/Icons';

export default function HomeScreen() {
  const navigate = useNavigate();
  const [showBrandText, setShowBrandText] = useState(false);
  const [logoFailed, setLogoFailed] = useState(false);

  const handleLogoLoad = (event: React.SyntheticEvent<HTMLImageElement>) => {
    const img = event.currentTarget;
    const ratio = img.naturalHeight > 0 ? img.naturalWidth / img.naturalHeight : 0;
    // Logos muito "quadradas" tendem a ser apenas ícone; nesse caso exibimos texto ao lado.
    setShowBrandText(ratio > 0 && ratio < 1.35);
  };

  return (
    <div className="min-h-screen bg-white">
      {/* Header com logo, assistente botânico e botão de perfil */}
      <header className="bg-white border-b border-[var(--color-border-light)]">
        <div className="responsive-shell flex justify-between items-center gap-3 py-3 sm:py-4 lg:py-4">
          <div className="flex items-center gap-2 min-w-0">
            {!logoFailed && (
              <img
                src="/imagemlogotcc.png"
                alt="ScanPlant Logo"
                className="h-8 sm:h-10 lg:h-12 xl:h-14 w-auto max-w-[220px] object-contain shrink-0"
                onLoad={handleLogoLoad}
                onError={() => setLogoFailed(true)}
              />
            )}
            {(logoFailed || showBrandText) && (
              <span className="font-bold text-sm sm:text-base lg:text-xl text-gray-800 whitespace-nowrap">
                ScanPlant
              </span>
            )}
          </div>

          <div className="flex items-center gap-2 sm:gap-4 lg:gap-5 shrink-0">
            <button 
              onClick={() => navigate('/plant-assistant')}
              className="flex items-center gap-1 sm:gap-2 bg-[rgba(0,150,136,0.85)] text-white px-2 sm:px-3 lg:px-4 py-1.5 lg:py-2 rounded-full font-bold border-[1.5px] border-[rgba(255,255,255,0.6)] whitespace-nowrap"
              style={{ boxShadow: 'var(--shadow-md)' }}
            >
              <div className="w-6 h-6 sm:w-7 sm:h-7 lg:w-8 lg:h-8 rounded-full bg-[rgba(255,255,255,0.3)] flex items-center justify-center">
                <span className="text-sm sm:text-base">🌿</span>
              </div>
              <span className="text-xs sm:text-sm lg:text-base">Assistente</span>
            </button>
            
            <button 
              onClick={() => navigate('/profile')}
              className="w-9 h-9 sm:w-10 sm:h-10 lg:w-11 lg:h-11 bg-[var(--color-primary-100)] rounded-full flex items-center justify-center text-[var(--color-primary-600)] text-lg sm:text-xl shrink-0"
              style={{ boxShadow: 'var(--shadow-md)' }}
            >
              ⚙
            </button>
          </div>
        </div>
      </header>

      <div className="overflow-y-auto pb-12 md:pb-16">
        <div className="responsive-shell">
          {/* Logo Container */}
          <div className="flex flex-col items-center lg:items-start pt-6 sm:pt-8 md:pt-10 lg:pt-12 pb-8 sm:pb-10 md:pb-12 lg:pb-8 px-2">
            <h2 className="text-xl sm:text-2xl md:text-3xl lg:text-4xl font-semibold text-[var(--color-text-primary)] text-center lg:text-left mb-2">
              Bem-vindo ao ScanPlant
            </h2>
            <p className="text-sm md:text-base lg:text-lg text-[var(--color-text-secondary)] text-center lg:text-left max-w-[280px] md:max-w-[520px] lg:max-w-[760px]">
              Descubra o mundo das plantas com inteligência artificial
            </p>
          </div>

          {/* Action Cards */}
          <div className="mb-10 md:mb-12">
            <div className="mb-4 lg:mb-6 lg:grid lg:grid-cols-12 lg:gap-5 lg:items-stretch xl:items-start">
              {/* Primary Card */}
              <button 
                onClick={() => navigate('/photo')}
                className="w-full bg-[var(--color-primary-500)] rounded-2xl p-6 sm:p-8 lg:px-8 lg:py-7 xl:px-9 xl:py-7 flex flex-col items-center mb-6 lg:mb-0 border border-[var(--color-primary-400)] lg:col-span-7 lg:min-h-[300px] xl:min-h-[272px] 2xl:min-h-[286px]"
                style={{ boxShadow: 'var(--shadow-xl)' }}
              >
                {/* Mobile mantém o layout atual */}
                <div className="flex flex-col items-center lg:hidden">
                  <div 
                    className="w-[62px] h-[62px] sm:w-[70px] sm:h-[70px] rounded-full bg-[var(--color-primary-400)] flex items-center justify-center mb-4 sm:mb-6 border-2 border-[var(--color-primary-300)]"
                    style={{ boxShadow: 'var(--shadow-md)' }}
                  >
                    <span className="text-2xl sm:text-[28px]">❋</span>
                  </div>
                  <h3 className="text-lg sm:text-xl font-semibold text-white mb-2 text-center">Identificar Planta</h3>
                  <p className="text-sm sm:text-base text-[var(--color-primary-100)] text-center max-w-[560px]">
                    Tire uma foto e descubra informações detalhadas
                  </p>
                </div>

                {/* Variante experimental para desktop */}
                <div className="hidden lg:flex w-full h-full xl:h-auto flex-col items-start text-left">
                  <div className="flex items-center gap-3 mb-3 xl:mb-4">
                    <span className="w-11 h-11 xl:w-12 xl:h-12 rounded-full bg-[var(--color-primary-400)] border-2 border-[var(--color-primary-300)] flex items-center justify-center text-xl xl:text-2xl shrink-0">
                      🌿
                    </span>
                    <h3 className="text-[30px] xl:text-[34px] 2xl:text-[36px] font-semibold text-white leading-tight">Identificar Planta</h3>
                  </div>
                  <p className="text-lg xl:text-[19px] text-[var(--color-primary-100)] leading-relaxed max-w-[660px] mb-5 xl:mb-6">
                    Tire uma foto e descubra informações detalhadas sobre qualquer planta utilizando inteligência artificial.
                  </p>
                  <span className="inline-flex items-center px-5 xl:px-6 py-2.5 xl:py-3 rounded-xl bg-white/95 text-[var(--color-primary-600)] text-[15px] xl:text-base font-semibold shadow-[0_8px_18px_rgba(15,23,42,0.18)] border border-white/90">
                    Identificar Agora
                  </span>
                </div>
              </button>

              <div className="grid grid-cols-2 gap-3 lg:gap-4 lg:col-span-5">
                <button 
                  onClick={() => navigate('/gallery?mode=personal')}
                  className="bg-white rounded-2xl p-3 sm:p-4 lg:p-5 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px] lg:min-h-[185px]"
                  style={{ boxShadow: 'var(--shadow-lg)' }}
                >
                  <div 
                    className="w-[48px] h-[48px] sm:w-[55px] sm:h-[55px] lg:w-[62px] lg:h-[62px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 lg:mb-3 border-[1.5px] border-[var(--color-primary-300)]"
                    style={{ boxShadow: 'var(--shadow-sm)' }}
                  >
                    <span className="text-xl sm:text-2xl lg:text-3xl">🌱</span>
                  </div>
                  <h4 className="text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text-primary)] mb-1 text-center">Minhas Plantas</h4>
                  <p className="text-xs sm:text-sm text-[var(--color-text-tertiary)] text-center">Sua coleção</p>
                </button>

                <button 
                  onClick={() => navigate('/gallery?mode=community')}
                  className="bg-white rounded-2xl p-3 sm:p-4 lg:p-5 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px] lg:min-h-[185px]"
                  style={{ boxShadow: 'var(--shadow-lg)' }}
                >
                  <div 
                    className="w-[48px] h-[48px] sm:w-[55px] sm:h-[55px] lg:w-[62px] lg:h-[62px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 lg:mb-3 border-[1.5px] border-[var(--color-primary-300)]"
                    style={{ boxShadow: 'var(--shadow-sm)' }}
                  >
                    <span className="text-xl sm:text-2xl lg:text-3xl">👥</span>
                  </div>
                  <h4 className="text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text-primary)] mb-1 text-center">Comunidade</h4>
                  <p className="text-xs sm:text-sm text-[var(--color-text-tertiary)] text-center">Plantas compartilhadas</p>
                </button>

                <button 
                  onClick={() => navigate('/search')}
                  className="bg-white rounded-2xl p-3 sm:p-4 lg:p-5 flex flex-col items-center border border-[var(--color-primary-100)] min-h-[130px] lg:min-h-[185px]"
                  style={{ boxShadow: 'var(--shadow-lg)' }}
                >
                  <div 
                    className="w-[48px] h-[48px] sm:w-[55px] sm:h-[55px] lg:w-[62px] lg:h-[62px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 lg:mb-3 border-[1.5px] border-[var(--color-primary-300)]"
                    style={{ boxShadow: 'var(--shadow-sm)' }}
                  >
                    <span className="text-xl sm:text-2xl lg:text-3xl">🔍</span>
                  </div>
                  <h4 className="text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text-primary)] mb-1 text-center">Explorar</h4>
                  <p className="text-xs sm:text-sm text-[var(--color-text-tertiary)] text-center">Buscar plantas</p>
                </button>

                <button 
                  onClick={() => navigate('/chats')}
                  className="bg-white rounded-2xl p-3 sm:p-4 lg:p-5 flex flex-col items-center border-2 border-[var(--color-primary-400)] min-h-[130px] lg:min-h-[185px] relative overflow-visible"
                  style={{ boxShadow: 'var(--shadow-lg)' }}
                >
                  <span 
                    className="absolute -top-2 -right-2 bg-[var(--color-primary-500)] text-white text-[10px] font-bold px-2 py-0.5 rounded-full z-10"
                    style={{ boxShadow: 'var(--shadow-sm)', letterSpacing: '0.5px' }}
                  >
                    NOVO
                  </span>
                  <div 
                    className="w-[48px] h-[48px] sm:w-[55px] sm:h-[55px] lg:w-[62px] lg:h-[62px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mb-2 lg:mb-3 border-[1.5px] border-[var(--color-primary-300)]"
                    style={{ boxShadow: 'var(--shadow-sm)' }}
                  >
                    <span className="text-xl sm:text-2xl lg:text-3xl">💬</span>
                  </div>
                  <h4 className="text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text-primary)] mb-1 text-center">Chat</h4>
                  <p className="text-xs sm:text-sm text-[var(--color-text-tertiary)] text-center">Converse com outros</p>
                </button>
              </div>
            </div>

            <button
              onClick={() => navigate('/favorites')}
              className="w-full bg-white rounded-2xl p-3 sm:p-4 lg:p-5 flex items-center border border-[var(--color-primary-100)] min-h-[92px] lg:min-h-[112px]"
              style={{ boxShadow: 'var(--shadow-lg)' }}
            >
              <div
                className="w-[48px] h-[48px] sm:w-[55px] sm:h-[55px] lg:w-[62px] lg:h-[62px] rounded-full bg-[var(--color-primary-100)] flex items-center justify-center mr-3 sm:mr-4 lg:mr-5 border-[1.5px] border-[var(--color-primary-300)] text-[var(--color-primary-600)] shrink-0"
                style={{ boxShadow: 'var(--shadow-sm)' }}
              >
                <Icons.Star size={24} />
              </div>
              <div className="flex-1 text-left min-w-0">
                <h4 className="text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text-primary)] mb-1">Favoritos</h4>
                <p className="text-xs sm:text-sm text-[var(--color-text-tertiary)]">Plantas que voce quer acompanhar</p>
              </div>
              <Icons.ChevronRight size={22} className="text-[var(--color-text-tertiary)]" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
