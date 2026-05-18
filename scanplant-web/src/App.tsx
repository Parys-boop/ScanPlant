import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, useNavigate } from 'react-router-dom';
import LoadingScreen from './pages/LoadingScreen';
import ScreenPasso from './pages/ScreenPasso';
import LoginScreen from './pages/LoginScreen';
import RegisterScreen from './pages/RegisterScreen';
import HomeScreen from './pages/HomeScreen';
import PhotoScreen from './pages/PhotoScreen';
import PlantGallery from './pages/PlantGallery';
import SearchScreen from './pages/SearchScreen';
import ChatListScreen from './pages/ChatListScreen';
import ChatScreen from './pages/ChatScreen';
import ProfileSettingsScreen from './pages/ProfileSettingsScreen';
import PlantDetailScreen from './pages/PlantDetailScreen';
import UserListScreen from './pages/UserListScreen';
import PlantAssistantChat from './pages/PlantAssistantChat';
import FavoritesScreen from './pages/FavoritesScreen';

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
  // Simple check for token
  const token = localStorage.getItem('@scanplant_token');
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  return <>{children}</>;
};

function App() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simula carregamento inicial
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 2000); // 2 segundos de loading

    return () => clearTimeout(timer);
  }, []);

  if (isLoading) {
    return <LoadingScreen />;
  }

  return (
    <Router>
      <div className="font-sans text-gray-900 h-full min-h-screen">
        <Routes>
          <Route path="/instructions" element={<ScreenPasso />} />
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/register" element={<RegisterScreen />} />
          
          <Route path="/" element={
            <ProtectedRoute>
              <HomeScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/photo" element={
            <ProtectedRoute>
              <PhotoScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/gallery" element={
            <ProtectedRoute>
              <PlantGallery />
            </ProtectedRoute>
          } />
           <Route path="/plant/:id" element={
            <ProtectedRoute>
              <PlantDetailScreen />
            </ProtectedRoute>
          } />

          <Route path="/search" element={
            <ProtectedRoute>
              <SearchScreen />
            </ProtectedRoute>
          } />

          <Route path="/favorites" element={
            <ProtectedRoute>
              <FavoritesScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/profile" element={
            <ProtectedRoute>
              <ProfileSettingsScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/chats" element={
            <ProtectedRoute>
              <ChatListScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/users" element={
            <ProtectedRoute>
              <UserListScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/chat/:chatId" element={
            <ProtectedRoute>
              <ChatScreen />
            </ProtectedRoute>
          } />
          
          <Route path="/plant-assistant" element={
            <ProtectedRoute>
              <PlantAssistantChat />
            </ProtectedRoute>
          } />

          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
      <InitialRedirect />
    </Router>
  );
}

// Componente para redirecionar na primeira vez
const InitialRedirect = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const hasSeenInstructions = localStorage.getItem('@scanplant_seen_instructions');
    const token = localStorage.getItem('@scanplant_token');
    
    if (!hasSeenInstructions && !token && window.location.pathname === '/') {
      navigate('/instructions');
    }
  }, [navigate]);

  return null;
};

export default App;
