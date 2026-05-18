# 🛠️ Comandos Úteis - ScanPlant

Referência rápida de comandos para desenvolvimento.

---

## 🔧 Back-end (API C#)

### Navegar para o diretório
```powershell
cd "c:\Users\sh050\OneDrive\Documentos\ScanPlant Front + BackEnd\ScanPlantAPI\ScanPlantAPI"
```

### Executar a API
```powershell
# Modo normal
dotnet run --launch-profile http

# Com auto-reload (recompila ao salvar)
dotnet watch run --launch-profile http

# Em modo release
dotnet run --launch-profile http --configuration Release
```

### Gerenciar Banco de Dados
```powershell
# Criar nova migration
dotnet ef migrations add NomeDaMigration

# Aplicar migrations
dotnet ef database update

# Remover última migration (se não aplicada ainda)
dotnet ef migrations remove

# Listar migrations
dotnet ef migrations list

# Recriar banco do zero (CUIDADO: apaga dados)
dotnet ef database drop
dotnet ef database update
```

### Gerenciar Pacotes
```powershell
# Restaurar pacotes
dotnet restore

# Adicionar pacote
dotnet add package NomeDoPacote

# Atualizar todos os pacotes
dotnet restore --force

# Listar pacotes instalados
dotnet list package
```

### Limpar e Recompilar
```powershell
# Limpar build
dotnet clean

# Rebuild completo
dotnet clean ; dotnet build
```

### Descobrir IP Local
```powershell
# Script automático
.\get-ip.ps1

# Manual
ipconfig

# Só mostrar IPs IPv4
ipconfig | Select-String "IPv4"
```

### Verificar Porta 5041
```powershell
# Ver o que está usando a porta
netstat -ano | findstr :5041

# Matar processo na porta (substitua PID)
taskkill /PID <PID> /F

# Verificar se a porta está livre
Test-NetConnection -ComputerName localhost -Port 5041
```

### Logs e Debug
```powershell
# Ver logs do .NET
dotnet run --verbosity detailed

# Executar com variável de ambiente customizada
$env:ASPNETCORE_ENVIRONMENT="Development" ; dotnet run
```

---

## 📱 Front-end (React Native / Expo)

### Navegar para o diretório
```powershell
cd "c:\Users\sh050\OneDrive\Documentos\ScanPlant Front + BackEnd\ScanPlant-Final"
```

### Instalar e Gerenciar Dependências
```powershell
# Instalar todas as dependências
npm install

# Instalar pacote específico
npm install nome-do-pacote

# Instalar como dev dependency
npm install --save-dev nome-do-pacote

# Atualizar dependências
npm update

# Verificar vulnerabilidades
npm audit

# Corrigir vulnerabilidades
npm audit fix
```

### Executar o App
```powershell
# Iniciar Expo (escolher opção depois)
npx expo start

# Limpar cache e iniciar
npx expo start -c

# Iniciar direto no web
npx expo start --web

# Iniciar em modo túnel (funciona sem estar na mesma rede)
npx expo start --tunnel

# Iniciar com host específico
npx expo start --host tunnel
```

### Abrir em Diferentes Plataformas
```powershell
# Após npx expo start, pressione:
# w - Web browser
# a - Android emulator
# i - iOS simulator
# r - Reload app
# m - Menu de dev
```

### Limpar e Resetar
```powershell
# Limpar cache do Expo
npx expo start -c

# Limpar cache do npm
npm cache clean --force

# Deletar node_modules e reinstalar
Remove-Item -Recurse -Force node_modules ; npm install

# Reset completo
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm install
npx expo start -c
```

### Build e Publicação
```powershell
# Build para Android (APK)
npx expo build:android

# Build para iOS
npx expo build:ios

# Publicar no Expo
npx expo publish
```

### Verificar Configuração
```powershell
# Ver versão do Expo
npx expo --version

# Ver diagnóstico
npx expo doctor

# Ver configuração do app
Get-Content app.json
```

---

## 🗄️ PostgreSQL

### Gerenciar Serviço
```powershell
# Ver status do serviço
Get-Service -Name postgresql*

# Iniciar serviço
Start-Service postgresql-x64-16  # Ajuste o nome conforme sua versão

# Parar serviço
Stop-Service postgresql-x64-16

# Reiniciar serviço
Restart-Service postgresql-x64-16
```

### Conectar ao PostgreSQL
```powershell
# Via psql (se estiver no PATH)
psql -U postgres -d ScanPlantDB

# Listar bancos de dados
psql -U postgres -c "\l"

# Executar query
psql -U postgres -d ScanPlantDB -c "SELECT * FROM \"AspNetUsers\";"
```

### Backup e Restore
```powershell
# Fazer backup
pg_dump -U postgres -d ScanPlantDB > backup.sql

# Restaurar backup
psql -U postgres -d ScanPlantDB < backup.sql

# Backup com data
$date = Get-Date -Format "yyyyMMdd_HHmmss"
pg_dump -U postgres -d ScanPlantDB > "backup_$date.sql"
```

---

## 🔥 Firewall do Windows

### Verificar Status
```powershell
# Ver status do firewall
Get-NetFirewallProfile | Select-Object Name, Enabled

# Ver regras para porta 5041
Get-NetFirewallRule | Where-Object {$_.DisplayName -like "*5041*"}
```

### Criar Regra para Porta 5041
```powershell
# Como Administrator
New-NetFirewallRule -DisplayName "ScanPlant API" -Direction Inbound -LocalPort 5041 -Protocol TCP -Action Allow
```

### Desabilitar Temporariamente (para teste)
```powershell
# Como Administrator - CUIDADO!
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False

# Habilitar novamente
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True
```

---

## 🌐 Rede e Conectividade

### Testar Conexão
```powershell
# Testar se API está respondendo
Invoke-WebRequest -Uri "http://localhost:5041/swagger" -Method GET

# Testar do seu IP
Invoke-WebRequest -Uri "http://SEU_IP:5041/swagger" -Method GET

# Ping
ping localhost
ping SEU_IP
```

### Ver Informações de Rede
```powershell
# Ver IP de todas as interfaces
Get-NetIPAddress -AddressFamily IPv4 | Format-Table

# Ver adaptadores de rede
Get-NetAdapter

# Ver gateway padrão
Get-NetRoute -DestinationPrefix "0.0.0.0/0"
```

---

## 🧹 Limpeza Geral

### Limpar Tudo (Back-end)
```powershell
cd ScanPlantAPI\ScanPlantAPI
dotnet clean
Remove-Item -Recurse -Force bin, obj
dotnet restore
dotnet build
```

### Limpar Tudo (Front-end)
```powershell
cd ScanPlant-Final
Remove-Item -Recurse -Force node_modules
Remove-Item package-lock.json
npm cache clean --force
npm install
```

### Script de Reset Completo
```powershell
# Crie um arquivo reset-all.ps1 com:

Write-Host "Limpando Back-end..." -ForegroundColor Yellow
cd "ScanPlantAPI\ScanPlantAPI"
dotnet clean
Remove-Item -Recurse -Force bin, obj -ErrorAction SilentlyContinue
dotnet restore

Write-Host "Limpando Front-end..." -ForegroundColor Yellow
cd "..\..\ScanPlant-Final"
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
Remove-Item package-lock.json -ErrorAction SilentlyContinue
npm install

Write-Host "Limpeza concluída!" -ForegroundColor Green
```

---

## 🔍 Debug e Troubleshooting

### Ver Logs em Tempo Real
```powershell
# Back-end: Console já mostra automaticamente

# Front-end: Abrir DevTools
# No navegador: F12
# No Expo: Shake o dispositivo > Debug Remote JS
```

### Testar Endpoints Manualmente
```powershell
# Testar registro
$body = @{
    email = "teste@teste.com"
    password = "SENHA_DE_TESTE"
    name = "Teste"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5041/api/auth/register" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"

# Testar login
$body = @{
    email = "teste@teste.com"
    password = "SENHA_DE_TESTE"
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5041/api/auth/login" `
    -Method POST `
    -Body $body `
    -ContentType "application/json"
```

### Verificar Variáveis de Ambiente
```powershell
# Ver todas
Get-ChildItem Env:

# Ver específica
$env:ASPNETCORE_ENVIRONMENT

# Definir temporariamente
$env:ASPNETCORE_ENVIRONMENT = "Development"
```

---

## 📊 Monitoramento

### Ver Processos
```powershell
# Processos do .NET
Get-Process | Where-Object {$_.ProcessName -like "*dotnet*"}

# Processos do Node
Get-Process | Where-Object {$_.ProcessName -like "*node*"}

# Uso de memória
Get-Process | Sort-Object WorkingSet -Descending | Select-Object -First 10
```

### Ver Conexões de Rede
```powershell
# Todas as conexões
Get-NetTCPConnection

# Só porta 5041
Get-NetTCPConnection | Where-Object {$_.LocalPort -eq 5041}

# Conexões estabelecidas
Get-NetTCPConnection | Where-Object {$_.State -eq "Established"}
```

---

## 🚀 Atalhos Úteis

### Aliases do PowerShell
```powershell
# Adicione ao seu perfil do PowerShell:
# notepad $PROFILE

# Aliases úteis
function api { cd "c:\Users\sh050\OneDrive\Documentos\ScanPlant Front + BackEnd\ScanPlantAPI\ScanPlantAPI" }
function app { cd "c:\Users\sh050\OneDrive\Documentos\ScanPlant Front + BackEnd\ScanPlant-Final" }
function runapi { api ; dotnet run --launch-profile http }
function runapp { app ; npx expo start }
function cleanall { api ; dotnet clean ; app ; Remove-Item -Recurse -Force node_modules }
```

### Script de Start Rápido
```powershell
# Crie um arquivo start-dev.ps1 com:

Write-Host "Iniciando ScanPlant..." -ForegroundColor Cyan

# Iniciar API em uma nova janela
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'ScanPlantAPI\ScanPlantAPI' ; dotnet run --launch-profile http"

# Aguardar API iniciar
Start-Sleep -Seconds 5

# Iniciar Front-end em outra janela
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd 'ScanPlant-Final' ; npx expo start"

Write-Host "Projetos iniciados!" -ForegroundColor Green
```

---

## 📝 Notas

- Execute comandos como **Administrator** quando necessário
- Sempre verifique o diretório atual antes de executar comandos
- Use `Tab` para autocompletar caminhos
- Use `Ctrl+C` para parar processos em execução
- Mantenha backups antes de operações destrutivas

---

**Dica**: Salve este arquivo como referência e use Ctrl+F para buscar comandos rapidamente!
