import React from 'react';
import { useNavigate } from 'react-router-dom';
import { Camera, Sun, CheckCircle, Shield } from 'lucide-react';

interface InstructionStepProps {
  Icon: React.ElementType;
  title: string;
  description: string;
}

const InstructionStep: React.FC<InstructionStepProps> = ({ Icon, title, description }) => (
  <div className="flex items-start sm:items-center mb-6 last:mb-0">
    <Icon className="w-6 h-6 sm:w-7 sm:h-7 text-[#4A6C35] mr-4 sm:mr-5 flex-shrink-0 mt-1 sm:mt-0" />
    <div className="flex-1">
      <h3 className="text-base sm:text-lg font-semibold text-gray-800 mb-1.5">{title}</h3>
      <p className="text-sm text-gray-600 leading-relaxed">{description}</p>
    </div>
  </div>
);

const ScreenPasso = () => {
  const navigate = useNavigate();

  const handlePress = () => {
    localStorage.setItem('@scanplant_seen_instructions', 'true');
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#E9F5DB] to-white flex items-center justify-center p-4 sm:p-6 md:p-8">
      <div className="w-full max-w-md md:max-w-2xl lg:max-w-3xl flex flex-col items-center justify-around min-h-screen md:min-h-0 py-6 sm:py-8 md:py-10 gap-8">
        
        {/* Header */}
        <div className="flex flex-col items-center w-full">
          <div className="w-24 h-24 sm:w-28 sm:h-28 rounded-full bg-white flex items-center justify-center mb-5 shadow-lg">
            <Shield className="w-14 h-14 sm:w-16 sm:h-16 text-[#4A6C35]" />
          </div>
          <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-gray-800 text-center mb-2.5">
            Como Tirar a Foto Perfeita
          </h1>
          <p className="text-sm sm:text-base text-gray-600 text-center max-w-[95%] md:max-w-[80%] leading-snug">
            Siga estas dicas para garantir uma análise precisa da sua planta.
          </p>
        </div>

        {/* Card com instruções */}
        <div className="bg-white rounded-2xl py-6 px-4 sm:px-5 md:px-6 w-full shadow-lg min-h-[300px] flex flex-col justify-around">
          <InstructionStep
            Icon={Camera}
            title="Enquadramento"
            description="Certifique-se de que a folha ou a área afetada esteja bem focada e centralizada na foto."
          />
          <InstructionStep
            Icon={Sun}
            title="Iluminação Ideal"
            description="Fotografe em um local com boa luz natural, evitando sombras fortes e o uso de flash."
          />
          <InstructionStep
            Icon={CheckCircle}
            title="Foco e Nitidez"
            description="Toque na tela para focar e mantenha o celular firme para obter uma imagem nítida e clara."
          />
        </div>

        {/* Botão */}
        <button
          onClick={handlePress}
          className="bg-[#4A6C35] text-white py-3.5 sm:py-4 w-full rounded-xl font-bold text-sm sm:text-base shadow-md hover:bg-[#3d5a2b] transition-colors"
        >
          OK, ENTENDI
        </button>
        
      </div>
    </div>
  );
};

export default ScreenPasso;
