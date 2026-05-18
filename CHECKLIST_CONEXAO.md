# ✅ Checklist de Conexão Front-end + Back-end

Use este checklist para garantir que tudo está configurado corretamente.

---

## 📦 PASSO 1: Verificar Instalações

### Back-end
- [ ] .NET 8 SDK instalado
  ```powershell
  dotnet --version
  # Deve mostrar: 8.0.x
  ```

- [ ] PostgreSQL instalado e rodando
  ```powershell
  Get-Service -Name postgresql*
  # Status deve ser "Running"
  ```

- [ ] Banco de dados ScanPlantDB criado
  - Use pgAdmin ou DBeaver para verificar

### Front-end
- [ ] Node.js 18+ instalado
  ```powershell
  node --version
  # Deve mostrar: v18.x.x ou superior
  ```

- [ ] Expo CLI instalado
  ```powershell
  npx expo --version
  # Deve mostrar a versão do Expo
  ```

- [ ] Expo Go instalado no celular (se for testar em dispositivo físico)

---

## 🔧 PASSO 2: Configurar o Back-end

### Banco de Dados
- [ ] Arquivo `appsettings.json` configurado
  - [ ] Host correto (localhost)
  - [ ] Port correto (5432)
  - [ ] Database correto (ScanPlantDB)
  - [ ] Username correto
  - [ ] Password correto

### Porta da API
- [ ] Arquivo `launchSettings.json` configurado
  - [ ] Porta 5041 configurada
  - [ ] Listening em 0.0.0.0 (não em localhost)
  - [ ] Profile "http" disponível

### Teste da API
- [ ] Executar: `dotnet run --launch-profile http`
- [ ] Abrir: http://localhost:5041/swagger
- [ ] Swagger carrega sem erros
- [ ] Consegue expandir os endpoints

---

## 🌐 PASSO 3: Descobrir IP (para celular)

### Se for testar no CELULAR:
- [ ] Executar script: `.\get-ip.ps1`
- [ ] Anotar o IP mostrado (ex: 192.168.0.100)
- [ ] Testar no navegador: http://SEU_IP:5041/swagger
- [ ] Swagger abre normalmente

### Se for testar no NAVEGADOR:
- [ ] Usar localhost:5041 (pular este passo)

---

## 📱 PASSO 4: Configurar o Front-end

### Arquivo apiConfig.js
- [ ] Abrir: `ScanPlant-Final\components\apiConfig.js`
- [ ] Escolher a configuração adequada:
  
  **Para NAVEGADOR ou EMULADOR iOS:**
  - [ ] Descomentar: `BASE_URL: 'http://localhost:5041/api'`
  
  **Para EMULADOR ANDROID:**
  - [ ] Descomentar: `BASE_URL: 'http://10.0.2.2:5041/api'`
  
  **Para CELULAR (Expo Go):**
  - [ ] Descomentar: `BASE_URL: 'http://SEU_IP:5041/api'`
  - [ ] Substituir SEU_IP pelo IP descoberto no Passo 3
  - [ ] Exemplo: `'http://192.168.0.100:5041/api'`

- [ ] Salvar o arquivo

### Verificações
- [ ] Arquivo salvo corretamente
- [ ] Apenas UMA linha de BASE_URL descomentada
- [ ] URL termina com `/api` (SEM barra no final)
- [ ] Formato correto: `http://` no início

---

## 🚀 PASSO 5: Executar os Projetos

### Ordem de execução (IMPORTANTE!)
1. **PRIMEIRO: Back-end**
   - [ ] Abrir PowerShell no diretório: `ScanPlantAPI\ScanPlantAPI`
   - [ ] Executar: `dotnet run --launch-profile http`
   - [ ] Aguardar mensagem: "Now listening on: http://0.0.0.0:5041"
   - [ ] Manter este terminal aberto

2. **SEGUNDO: Front-end**
   - [ ] Abrir OUTRO PowerShell no diretório: `ScanPlant-Final`
   - [ ] Executar: `npm install` (primeira vez)
   - [ ] Executar: `npx expo start`
   - [ ] Aguardar aparecer o QR code
   - [ ] Manter este terminal aberto

---

## 🔗 PASSO 6: Conectar o App

### No Navegador (Web)
- [ ] Pressionar `w` no terminal do Expo
- [ ] Navegador abre automaticamente
- [ ] App carrega sem erros

### No Celular (Expo Go)
- [ ] Celular e PC na MESMA rede Wi-Fi
- [ ] Abrir app Expo Go no celular
- [ ] Escanear o QR code mostrado no terminal
- [ ] App carrega no celular

### No Emulador
- [ ] Android: Pressionar `a` no terminal do Expo
- [ ] iOS: Pressionar `i` no terminal do Expo
- [ ] Emulador abre e app carrega

---

## ✅ PASSO 7: Testar a Conexão

### Teste Visual
- [ ] App abre a tela de login
- [ ] Não aparece erro "Network request failed"
- [ ] Botões respondem ao toque

### Teste de Criação de Conta
- [ ] Clicar em "Criar Conta"
- [ ] Preencher:
  - Nome: Teste
  - Email: teste@teste.com
  - Senha: SENHA_DE_TESTE
- [ ] Clicar em "Cadastrar"
- [ ] Aguardar resposta
- [ ] ✅ Se funcionar: CONEXÃO OK!
- [ ] ❌ Se der erro: Veja os logs

### Verificar Logs

**Back-end (Terminal do dotnet run):**
- [ ] Aparecem requisições POST /api/auth/register
- [ ] Status 200 ou 201
- [ ] Sem erros de exceção

**Front-end (Terminal do Expo):**
- [ ] Aparecem logs de requisição
- [ ] URL correta sendo usada
- [ ] Sem erros de Network

---

## 🐛 PASSO 8: Solução de Problemas

### Se o app não conecta:

#### Verificação 1: API funcionando?
- [ ] Abrir: http://localhost:5041/swagger
- [ ] ✅ Se abrir: API OK
- [ ] ❌ Se não abrir: Problema no back-end

#### Verificação 2: IP correto?
- [ ] Conferir IP no `apiConfig.js`
- [ ] Testar IP no navegador do PC: http://SEU_IP:5041/swagger
- [ ] ✅ Se abrir: IP correto
- [ ] ❌ Se não abrir: IP errado ou firewall bloqueando

#### Verificação 3: Mesma rede?
- [ ] PC e celular conectados na mesma rede Wi-Fi?
- [ ] Não use dados móveis no celular
- [ ] Não use VPN

#### Verificação 4: Firewall?
- [ ] Windows Firewall está bloqueando?
- [ ] Teste: Desabilitar temporariamente
  ```powershell
  # Como admin
  Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
  
  # Após testar, habilite novamente
  Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
  ```

#### Verificação 5: Porta ocupada?
- [ ] Verificar se porta 5041 está livre
  ```powershell
  netstat -ano | findstr :5041
  ```
- [ ] Se aparecer algo, outro programa está usando
- [ ] Mate o processo ou mude a porta

---

## 🎉 CONCLUSÃO

### Tudo funcionando se:
- ✅ API responde em http://localhost:5041/swagger
- ✅ App carrega sem erros
- ✅ Consegue criar conta
- ✅ Consegue fazer login
- ✅ Consegue adicionar plantas

### Se ainda não funciona:
1. 📋 Revise TODOS os itens deste checklist
2. 📖 Leia o arquivo CONEXAO_FRONT_BACK.md
3. 🔍 Verifique os logs de erro
4. 🔄 Reinicie tudo e tente novamente

---

## 📞 Dúvidas?

Verifique os arquivos:
- `CONEXAO_FRONT_BACK.md` - Documentação completa
- `INICIO_RAPIDO.md` - Guia resumido
- `apiConfig.examples.js` - Exemplos de configuração

---

**Última atualização**: Novembro 2025
