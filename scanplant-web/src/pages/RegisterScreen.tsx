import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { auth } from '../api';

export default function RegisterScreen() {
  const navigate = useNavigate();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!name || !email || !password) {
      setError('Por favor, preencha todos os campos!');
      setSuccess('');
      return;
    }

    if (password.length < 6) {
      setError('Sua senha deve ter pelo menos 6 caracteres!');
      setSuccess('');
      return;
    }

    // Validar se a senha contém letras e números
    const temLetras = /[a-zA-Z]/.test(password);
    const temNumeros = /[0-9]/.test(password);
    
    if (!temLetras || !temNumeros) {
      setError('A senha deve conter letras E números!');
      setSuccess('');
      return;
    }

    setLoading(true);
    setError('');

    try {
      console.log('📝 Tentando criar conta:', email, 'Nome:', name);
      
      const { data, error: apiError } = await auth.signUp(email, password, name);
      
      console.log('📥 Resposta do cadastro:', { data, error: apiError });
      
      if (apiError) {
        console.error('❌ Erro no cadastro:', apiError);
        const errorMsg = apiError.message || apiError.toString();
        
        if (errorMsg.includes('already') || errorMsg.includes('registered')) {
          setError('Já existe uma conta com este email.');
          setSuccess('');
        } else if (errorMsg.includes('network') || errorMsg.includes('fetch')) {
          setError('Erro de conexão! Verifique sua internet.');
          setSuccess('');
        } else {
          setError(`Erro: ${errorMsg}`);
          setSuccess('');
        }
      } else {
        console.log('✅ Conta criada com sucesso!');
        setSuccess('Conta criada com sucesso! Faça login para continuar.');
        setError('');
        setName('');
        setEmail('');
        setPassword('');
        
        setTimeout(() => {
          navigate('/login');
        }, 2000);
      }
    } catch (err) {
      console.error('❌ Exceção ao criar conta:', err);
      setError('Erro de conexão! Verifique sua internet.');
      setSuccess('');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#E9F5DB] to-white flex flex-col items-center justify-center p-4 sm:p-6">
      <div className="w-full max-w-sm md:max-w-md flex flex-col py-8">
        <img 
          src="/imagemlogotcc.png" 
          alt="ScanPlant Logo" 
          className="w-[88px] h-[132px] sm:w-[100px] sm:h-[150px] object-contain mb-5 self-center"
          onError={(e) => {
            e.currentTarget.style.display = 'none';
            e.currentTarget.parentElement?.querySelector('.fallback-logo')?.classList.remove('hidden');
          }}
        />
        <div className="fallback-logo hidden w-20 h-20 bg-[#4A6C35] rounded-full mb-5 self-center flex items-center justify-center text-white text-2xl font-bold">
          SP
        </div>

        <h1 className="text-2xl sm:text-[28px] font-bold text-[#333] mb-2 text-center">Crie sua conta</h1>
        <p className="text-sm sm:text-base text-[#666] mb-8 sm:mb-10 text-center">É rápido e fácil!</p>

        <form onSubmit={handleRegister} className="w-full space-y-4 sm:space-y-5">
          {/* Nome Input */}
          <div className="flex items-center bg-[#F4F4F4] rounded-xl h-[50px] px-4 border border-[#E8E8E8]">
            <svg 
              width="20" 
              height="20" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="#A9A9A9" 
              strokeWidth="2" 
              strokeLinecap="round" 
              strokeLinejoin="round"
              className="mr-2.5"
            >
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
              <circle cx="12" cy="7" r="4"></circle>
            </svg>
            <input
              type="text"
              placeholder="Nome completo"
              className="flex-1 h-full bg-transparent border-none outline-none text-base text-[#333] placeholder-[#A9A9A9]"
              value={name}
              onChange={(e) => setName(e.target.value)}
              autoCapitalize="words"
              required
            />
          </div>

          {/* Email Input */}
          <div className="flex items-center bg-[#F4F4F4] rounded-xl h-[50px] px-4 border border-[#E8E8E8]">
            <svg 
              width="20" 
              height="20" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="#A9A9A9" 
              strokeWidth="2" 
              strokeLinecap="round" 
              strokeLinejoin="round"
              className="mr-2.5"
            >
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
              <polyline points="22,6 12,13 2,6"></polyline>
            </svg>
            <input
              type="email"
              placeholder="Email"
              className="flex-1 h-full bg-transparent border-none outline-none text-base text-[#333] placeholder-[#A9A9A9]"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              autoCapitalize="none"
              required
            />
          </div>

          {/* Password Input */}
          <div className="flex items-center bg-[#F4F4F4] rounded-xl h-[50px] px-4 border border-[#E8E8E8]">
            <svg 
              width="20" 
              height="20" 
              viewBox="0 0 24 24" 
              fill="none" 
              stroke="#A9A9A9" 
              strokeWidth="2" 
              strokeLinecap="round" 
              strokeLinejoin="round"
              className="mr-2.5"
            >
              <rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect>
              <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
            </svg>
            <input
              type="password"
              placeholder="Senha (letras e números, mín. 6)"
              className="flex-1 h-full bg-transparent border-none outline-none text-base text-[#333] placeholder-[#A9A9A9]"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          {error && (
            <p className="text-[#D9534F] text-center text-sm">{error}</p>
          )}

          {success && (
            <p className="text-[#5CB85C] text-center text-sm">{success}</p>
          )}

          <button
            type="submit"
            disabled={loading}
              className="w-full bg-[#4A6C35] text-white py-3.5 sm:py-4 rounded-xl font-bold text-sm sm:text-base mt-2.5 disabled:opacity-70"
              style={{ 
                boxShadow: '0px 2px 2.62px rgba(0, 0, 0, 0.23)'
              }}
          >
            {loading ? 'Criando...' : 'Criar Conta'}
          </button>

          <button
            type="button"
            onClick={() => navigate('/login')}
            className="w-full bg-transparent text-[#4A6C35] py-3.5 sm:py-4 rounded-xl font-bold text-sm sm:text-base mt-3 border border-[#4A6C35]"
          >
            Voltar
          </button>
        </form>
      </div>
    </div>
  );
}
