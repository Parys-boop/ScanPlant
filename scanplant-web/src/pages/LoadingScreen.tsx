import React from 'react';

const LoadingScreen = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-[#BED9A7] opacity-80">
      <img
        src="/imagemlogotcc.png"
        alt="ScanPlant Logo"
        className="w-32 h-48 mb-40 object-contain"
      />
      <div className="flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-4 border-[#4CAF50]"></div>
      </div>
      <p className="mt-5 text-3xl font-bold text-black text-center">
        CARREGANDO
      </p>
    </div>
  );
};

export default LoadingScreen;
