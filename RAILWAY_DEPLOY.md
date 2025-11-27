# Railway .NET Deployment

Este projeto está configurado para deploy no Railway.

## Como fazer deploy:

### Opção 1: Via GitHub (Recomendado)

1. Faça commit e push de tudo para o GitHub:
```bash
git add .
git commit -m "Configuração para Railway"
git push
```

2. Acesse: https://railway.app/
3. Faça login com sua conta GitHub
4. Clique em "New Project"
5. Selecione "Deploy from GitHub repo"
6. Escolha o repositório `ScanPlant`
7. Railway detectará automaticamente o Dockerfile
8. Clique em "Deploy"

### Configurar variáveis de ambiente no Railway:

No painel do Railway, adicione estas variáveis:
- `ASPNETCORE_URLS`: `http://0.0.0.0:$PORT`
- `ASPNETCORE_ENVIRONMENT`: `Production`

### Obter a URL da API:

Após o deploy, Railway fornecerá uma URL pública (exemplo: `https://scanplant-api-production.up.railway.app`)

### Atualizar o frontend:

1. Copie a URL da API do Railway
2. No Vercel, adicione a variável de ambiente:
   - Nome: `VITE_API_URL`
   - Valor: `https://sua-url-railway.up.railway.app/api`
3. Faça um novo deploy do frontend

---

## Opção 2: Via Railway CLI

```bash
# Login
railway login

# Iniciar projeto
railway init

# Deploy
railway up
```

---

## Custos

Railway oferece:
- $5 de crédito grátis por mês
- Suficiente para testes e desenvolvimento
- Para produção, considere o plano pago ($5/mês)
