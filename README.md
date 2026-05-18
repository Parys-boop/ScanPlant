# 🌱 ScanPlant - Projeto Completo

Sistema completo de identificação e gerenciamento de plantas com IA.

---

## 📁 Estrutura do Projeto

```
ScanPlant Front + BackEnd/
│
├── 📱 ScanPlant-Final/              # FRONT-END (React Native + Expo)
│   ├── components/                  # Telas e componentes
│   │   ├── apiConfig.js            # ⚠️ CONFIGURE AQUI A URL DA API
│   │   ├── api.js                  # Cliente da API
│   │   └── ...
│   ├── App.js                      # Ponto de entrada
│   └── package.json                # Dependências
│
├── 🔧 ScanPlantAPI/                 # BACK-END (C# .NET 8)
│   └── ScanPlantAPI/
│       ├── Controllers/            # Endpoints da API
│       ├── Models/                 # Modelos de dados
│       ├── Services/               # Lógica de negócio
│       ├── Program.cs              # Configuração da API
│       ├── appsettings.json        # ⚠️ CONFIGURE AQUI O BANCO
│       └── get-ip.ps1             # Script para descobrir IP
│
└── 📚 Documentação/
    ├── INICIO_RAPIDO.md            # ⭐ COMECE AQUI
    ├── CONEXAO_FRONT_BACK.md       # Guia completo
    ├── CHECKLIST_CONEXAO.md        # Checklist passo a passo
    └── COMANDOS_UTEIS.md           # Referência de comandos
```

---

## 🚀 Como Começar?

### **Se é sua primeira vez:**
1. 📖 Leia: `INICIO_RAPIDO.md` (3 minutos)
2. ✅ Siga: `CHECKLIST_CONEXAO.md` (15 minutos)
3. 🎉 Execute o projeto!

### **Se já configurou antes:**
1. Inicie o back-end: `dotnet run --launch-profile http`
2. Inicie o front-end: `npx expo start`
3. Conecte seu celular ou navegador

---

## 📋 Pré-requisitos Mínimos

- ✅ **Windows 10/11**
- ✅ **.NET 8 SDK** - [Download](https://dotnet.microsoft.com/download/dotnet/8.0)
- ✅ **PostgreSQL** - [Download](https://www.postgresql.org/download/)
- ✅ **Node.js 18+** - [Download](https://nodejs.org/)
- ✅ **Expo Go** (no celular) - [Android](https://play.google.com/store/apps/details?id=host.exp.exponent) | [iOS](https://apps.apple.com/app/expo-go/id982107779)

---

## ⚡ Início Rápido (3 comandos)

### 1. Back-end
```powershell
cd "ScanPlantAPI\ScanPlantAPI"
dotnet run --launch-profile http
```

### 2. Descobrir IP (para celular)
```powershell
.\get-ip.ps1
```

### 3. Front-end
```powershell
cd "ScanPlant-Final"
npx expo start
```

**Configure `apiConfig.js` com o IP mostrado antes de executar o passo 3!**

---

## 🔧 Configuração Essencial

### 1. Banco de Dados (appsettings.json)
```json
"ConnectionStrings": {
  "DefaultConnection": "Host=localhost;Port=5432;Database=ScanPlantDB;Username=SEU_USUARIO;Password=SUA_SENHA"
}
```

### 2. URL da API (apiConfig.js)
```javascript
// Para CELULAR: Use seu IP
BASE_URL: 'http://192.168.0.100:5041/api',

// Para NAVEGADOR: Use localhost
BASE_URL: 'http://localhost:5041/api',
```

---

## 🎯 Testando a Conexão

1. **API funcionando?**
   - Abra: http://localhost:5041/swagger
   - ✅ Deve mostrar a documentação

2. **App conectando?**
   - Crie uma conta no app
   - ✅ Se funcionar, está tudo OK!

3. **Logs:**
   - Back-end: Console do PowerShell
   - Front-end: Console do Expo

---

## 🐛 Problemas Comuns

| Problema | Solução |
|----------|---------|
| ❌ Network request failed | Verifique IP em `apiConfig.js` |
| ❌ Erro de banco de dados | Verifique PostgreSQL e credenciais |
| ❌ Porta 5041 em uso | `netstat -ano \| findstr :5041` e mate o processo |
| ❌ Firewall bloqueando | Desabilite temporariamente para testar |

**Mais soluções**: Veja `CONEXAO_FRONT_BACK.md`

---

## 📚 Documentação Completa

### Para Iniciantes:
1. 📄 **INICIO_RAPIDO.md** - Guia em 3 passos
2. ✅ **CHECKLIST_CONEXAO.md** - Checklist detalhado

### Para Referência:
3. 📖 **CONEXAO_FRONT_BACK.md** - Documentação completa
4. 🛠️ **COMANDOS_UTEIS.md** - Referência de comandos
5. 💡 **apiConfig.examples.js** - Exemplos de configuração

---

## 🏗️ Tecnologias Utilizadas

### Back-end
- ✨ **.NET 8** - Framework web
- 🗄️ **PostgreSQL** - Banco de dados
- 🔐 **ASP.NET Identity** - Autenticação
- 🎫 **JWT** - Tokens de autenticação
- 📝 **Entity Framework Core** - ORM

### Front-end
- ⚛️ **React Native** - Framework mobile
- 📱 **Expo** - Plataforma de desenvolvimento
- 🎨 **React Navigation** - Navegação
- 💾 **AsyncStorage** - Armazenamento local

---

## 🌟 Funcionalidades

- ✅ Autenticação de usuários (registro/login)
- ✅ Gerenciamento de perfil
- ✅ Cadastro de plantas com foto
- ✅ Galeria de plantas
- ✅ Sistema de chat entre usuários
- ✅ Geolocalização de plantas
- ✅ Lembretes de rega
- ✅ Assistente virtual com IA

---

## 📸 Como Usar

### 1. Criar Conta
- Abra o app
- Clique em "Criar Conta"
- Preencha seus dados
- Pronto!

### 2. Adicionar Planta
- Tire uma foto ou escolha da galeria
- O sistema identifica automaticamente
- Revise e salve

### 3. Gerenciar Plantas
- Veja sua coleção
- Configure lembretes de rega
- Adicione notas

### 4. Chat
- Converse com outros usuários
- Troque experiências
- Tire dúvidas

---

## 🔒 Segurança

- 🔐 Senhas criptografadas com hash
- 🎫 Autenticação via JWT
- 🔒 Endpoints protegidos
- ✅ Validação de dados
- 🛡️ CORS configurado

---

## 📊 Endpoints da API

### Autenticação
- `POST /api/auth/register` - Criar conta
- `POST /api/auth/login` - Login
- `GET /api/auth/me` - Usuário atual
- `PUT /api/auth/profile` - Atualizar perfil

### Plantas
- `GET /api/plants` - Listar todas
- `GET /api/plants/my` - Minhas plantas
- `POST /api/plants` - Adicionar planta
- `PUT /api/plants/{id}` - Atualizar
- `DELETE /api/plants/{id}` - Deletar

### Chat
- `GET /api/chats` - Meus chats
- `POST /api/chats` - Criar chat
- `GET /api/messages/chat/{id}` - Mensagens
- `POST /api/messages` - Enviar mensagem

**Documentação completa**: http://localhost:5041/swagger

---

## 🛠️ Comandos Rápidos

### Back-end
```powershell
# Executar
dotnet run --launch-profile http

# Com auto-reload
dotnet watch run --launch-profile http

# Aplicar migrations
dotnet ef database update
```

### Front-end
```powershell
# Instalar dependências
npm install

# Executar
npx expo start

# Limpar cache
npx expo start -c
```

**Mais comandos**: Veja `COMANDOS_UTEIS.md`

---

## 🚀 Próximos Passos

Após configurar tudo:

1. ✅ Teste todas as funcionalidades
2. 📝 Customize o design
3. 🔧 Ajuste configurações
4. 🚀 Deploy em produção (opcional)

---

## 📞 Suporte

Se encontrar problemas:

1. 🔍 Consulte a documentação apropriada
2. ✅ Use o `CHECKLIST_CONEXAO.md`
3. 🐛 Verifique os logs de erro
4. 🔄 Reinicie tudo

---

## 📝 Notas Importantes

- ⚠️ **Sempre** inicie o back-end ANTES do front-end
- ⚠️ Celular e PC devem estar na **mesma rede Wi-Fi**
- ⚠️ Firewall pode bloquear conexões
- ⚠️ IP pode mudar se sua rede usar DHCP
- ⚠️ PostgreSQL deve estar rodando antes da API

---

## 🎓 Aprendizado

Este projeto demonstra:
- ✅ Arquitetura REST API
- ✅ Autenticação JWT
- ✅ ORM com Entity Framework
- ✅ React Native/Expo
- ✅ Integração Front-end/Back-end
- ✅ Banco de dados relacional
- ✅ Sistema de chat em tempo real

---

## 📅 Versão

**Versão**: 1.0.0  
**Data**: Novembro 2025  
**Status**: Em desenvolvimento

---

## 🙏 Créditos

Desenvolvido para aprendizado e portfólio.

---

## 🎯 Objetivo do Projeto

Sistema completo de gerenciamento de plantas que permite:
- Identificar plantas por foto
- Gerenciar coleção pessoal
- Conectar com outros entusiastas
- Aprender sobre botanica
- Organizar cuidados com as plantas

---

**Desenvolvido com ❤️ e ☕**

---

## 📖 Índice de Documentação

1. **INICIO_RAPIDO.md** - Comece aqui! (3 min)
2. **CHECKLIST_CONEXAO.md** - Guia passo a passo completo
3. **CONEXAO_FRONT_BACK.md** - Documentação técnica detalhada
4. **COMANDOS_UTEIS.md** - Referência de comandos
5. **apiConfig.examples.js** - Exemplos de configuração de URL

**Escolha o documento adequado ao seu nível de experiência!**

---

✨ **Dica**: Marque este arquivo como favorito para referência rápida!
