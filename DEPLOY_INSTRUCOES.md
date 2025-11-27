# ScanPlant - Instruções de Deploy

## Status Atual
- **Frontend**: Vercel (https://scan-plant-front-back-na6ydhihs-samuel05015s-projects.vercel.app)
- **Backend**: Local + Cloudflare Tunnel
- **Database**: PostgreSQL local

---

## 🚀 Início Rápido

### Opção 1: Script Automático (Recomendado)

#### 1. Inicie tudo de uma vez
```powershell
.\iniciar-tudo.ps1
```
Este script vai:
- Abrir uma janela com a API rodando
- Abrir outra janela com o Cloudflare Tunnel
- Verificar se está tudo funcionando

#### 2. Copie a URL do tunnel
Na janela do tunnel, vai aparecer algo como:
```
https://xxx-yyy-zzz.trycloudflare.com
```

#### 3. Atualize e faça deploy
```powershell
.\atualizar-tunnel.ps1 -TunnelUrl "https://xxx-yyy-zzz.trycloudflare.com"
```
Este script vai:
- Atualizar o `apiConfig.ts` automaticamente
- Fazer build do frontend
- Fazer deploy no Vercel

---

## 🛠️ Opção 2: Passo a Passo Manual

### 1. Iniciar a API
```powershell
cd ScanPlantAPI\ScanPlantAPI
dotnet run
```

### 2. Iniciar o Tunnel
Em outra janela:
```powershell
.\iniciar-tunnel.ps1
# OU
cloudflared tunnel --url http://localhost:5041
```

### 3. Atualizar o Frontend
Copie a URL do tunnel e edite `scanplant-web/src/apiConfig.ts`:
```typescript
// Encontre esta linha e substitua a URL:
return 'https://SUA-URL-AQUI.trycloudflare.com/api'
```

### 4. Build e Deploy
```powershell
cd scanplant-web
npm run build
vercel --prod
```

---

## 📝 Scripts Disponíveis

| Script | Descrição | Como usar |
|--------|-----------|-----------|
| `iniciar-tudo.ps1` | Inicia API e Tunnel automaticamente | `.\iniciar-tudo.ps1` |
| `iniciar-tunnel.ps1` | Inicia apenas o Tunnel com verificações | `.\iniciar-tunnel.ps1` |
| `atualizar-tunnel.ps1` | Atualiza URL, build e deploy | `.\atualizar-tunnel.ps1 -TunnelUrl "https://xxx.trycloudflare.com"` |

---

## ⚠️ Importante

### Lembre-se sempre:
- ✅ A URL do tunnel **muda toda vez** que você reinicia
- ✅ Precisa manter **duas janelas abertas** (API e Tunnel)
- ✅ Use os scripts para facilitar o processo
- ✅ O `atualizar-tunnel.ps1` faz tudo automaticamente

### Primeira vez usando?
1. Instale o Cloudflared:
```powershell
winget install --id Cloudflare.cloudflared
```

2. Verifique se está instalado:
```powershell
cloudflared --version
```

---

## 🔄 Fluxo Completo Resumido

```powershell
# 1. Inicie tudo
.\iniciar-tudo.ps1

# 2. Copie a URL do tunnel que aparece

# 3. Atualize e faça deploy
.\atualizar-tunnel.ps1 -TunnelUrl "https://SUA-URL.trycloudflare.com"

# Pronto! ✨
```

---

## 🆘 Solução de Problemas

### Tunnel não inicia
```powershell
# Verifique se cloudflared está instalado
cloudflared --version

# Se não estiver, instale:
winget install --id Cloudflare.cloudflared
```

### API não responde
```powershell
# Verifique se está rodando
Test-NetConnection -ComputerName localhost -Port 5041

# Reinicie a API
cd ScanPlantAPI\ScanPlantAPI
dotnet run
```

### Deploy falha
```powershell
# Verifique se está logado no Vercel
vercel whoami

# Se não estiver, faça login:
vercel login
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
