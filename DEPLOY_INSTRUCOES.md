# ScanPlant - Deploy Completo

## ⚠️ IMPORTANTE: Backend precisa estar acessível via HTTPS

O frontend no Vercel está em HTTPS, então o backend também precisa estar acessível via HTTPS.

## Solução 1: Usar ngrok (Recomendado para testes)

### Passo 1: Inicie sua API localmente
```bash
cd ScanPlantAPI/ScanPlantAPI
dotnet run
```

### Passo 2: Em outro terminal, exponha a API com ngrok
```bash
ngrok http 5041
```

### Passo 3: Copie a URL HTTPS que o ngrok gera (exemplo: https://abc123.ngrok.io)

### Passo 4: Configure no Vercel
No painel do Vercel (https://vercel.com/samuel05015s-projects/scan-plant-front-back-end/settings/environment-variables):

1. Adicione uma variável de ambiente:
   - Nome: `VITE_API_URL`
   - Valor: `https://SEU-NGROK-URL/api` (exemplo: https://abc123.ngrok.io/api)

2. Faça um novo deploy:
```bash
cd "c:\Users\sh050\OneDrive\Documentos\ScanPlant Front + BackEnd"
vercel --prod
```

## Solução 2: Deploy do Backend (Produção)

Para produção real, você precisa fazer deploy do backend ASP.NET em:
- Azure App Service (recomendado para .NET)
- AWS Elastic Beanstalk
- Railway
- Render

### Deploy no Azure (Exemplo)
```bash
# Instalar Azure CLI
# https://docs.microsoft.com/cli/azure/install-azure-cli

# Login
az login

# Criar App Service
az webapp up --name scanplant-api --runtime "DOTNETCORE:8.0"
```

## Teste Local

Para testar localmente (sem deploy):
```bash
# Terminal 1: API
cd ScanPlantAPI/ScanPlantAPI
dotnet run

# Terminal 2: Frontend
cd scanplant-web
npm run dev
```

Acesse: http://localhost:5173
