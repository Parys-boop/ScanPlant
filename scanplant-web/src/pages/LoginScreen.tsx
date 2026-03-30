import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { auth } from '../api';

export default function LoginScreen() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    
    try {
      const { data, error: apiError } = await auth.signIn(email, password);
      
      if (apiError) {
        switch (apiError.message) {
          case 'Invalid login credentials':
            setError('Email ou senha incorretos!');
            break;
          case 'Email not confirmed':
            setError('Email não confirmado! Verifique sua caixa de entrada.');
            break;
          default:
            setError('Ocorreu um erro! Tente novamente.');
            break;
        }
      } else {
        setError('');
        setSuccess('');
        
        // Verificar se é o primeiro login desta sessão
        const isFirstLogin = localStorage.getItem('@scanplant_first_login');
        
        if (isFirstLogin === 'true') {
          localStorage.removeItem('@scanplant_first_login');
          navigate('/instructions');
        } else {
          navigate('/');
        }
      }
    } catch (err) {
      setError('Erro de conexão! Verifique sua internet.');
    } finally {
      setLoading(false);
    }
  };

  const handleResetPassword = async () => {
    if (!email) {
      setError('Digite seu email para redefinir a senha.');
      setSuccess('');
      return;
    }

    try {
      const { data, error: apiError } = await auth.api.resetPasswordForEmail(email);
      
      if (apiError) {
        setError('Erro ao enviar email. Verifique o endereço.');
        setSuccess('');
      } else {
        setSuccess('Email de redefinição de senha enviado!');
        setError('');
      }
    } catch (err) {
      setError('Erro de conexão! Verifique sua internet.');
      setSuccess('');
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#E9F5DB] to-white flex flex-col">
      {/* Back Button */}
      <button 
        onClick={() => navigate(-1)}
        className="absolute top-12 left-5 z-10 p-2 rounded-full bg-[rgba(255,255,255,0.7)]"
      >
        <svg 
          width="24" 
          height="24" 
          viewBox="0 0 24 24" 
          fill="none" 
          stroke="#475569" 
          strokeWidth="2" 
          strokeLinecap="round" 
          strokeLinejoin="round"
        >
          <line x1="19" y1="12" x2="5" y2="12"></line>
          <polyline points="12 19 5 12 12 5"></polyline>
        </svg>
      </button>

      <div className="flex-1 flex items-center justify-center px-6">
        <div className="w-full max-w-sm flex flex-col items-center">
          {/* Logo */}
          <img 
            src="/imagemlogotcc.png" 
            alt="ScanPlant Logo" 
            className="w-[100px] h-[150px] object-contain mb-5"
            onError={(e) => {
              // Fallback se a imagem não carregar
              e.currentTarget.style.display = 'none';
              e.currentTarget.parentElement?.querySelector('.fallback-logo')?.classList.remove('hidden');
            }}
          />
          <div className="fallback-logo hidden w-24 h-24 bg-[#4A6C35] rounded-full mb-5 flex items-center justify-center text-white text-3xl font-bold">
            SP
          </div>

          <h1 className="text-[28px] font-bold text-[#333] mb-2">Bem-vindo de volta!</h1>
          <p className="text-base text-[#666] mb-10">Faça login para continuar</p>

          <form onSubmit={handleLogin} className="w-full space-y-5">
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
                placeholder="Senha"
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
              className="w-full bg-[#4A6C35] text-white py-4 rounded-xl font-bold text-base mt-2.5 disabled:opacity-70"
              style={{ 
                boxShadow: '0px 2px 2.62px rgba(0, 0, 0, 0.23)'
              }}
            >
              {loading ? 'Entrando...' : 'Entrar'}
            </button>
          </form>

          <button 
            onClick={handleResetPassword}
            className="mt-5 text-[#4A6C35] text-sm"
          >
            Esqueceu a senha?
          </button>

          <button
            onClick={() => navigate('/register')}
            className="mt-5 text-[#4A6C35] text-sm"
          >
            Não tem uma conta? <span className="font-bold">Crie uma aqui.</span>
          </button>
        </div>
      </div>
    </div>
  );
}