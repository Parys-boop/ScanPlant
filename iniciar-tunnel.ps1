# Script para iniciar o Cloudflare Tunnel automaticamente
# Execute este script sempre que quiser expor a API

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Iniciando Cloudflare Tunnel" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se cloudflared está instalado
if (-not (Get-Command cloudflared -ErrorAction SilentlyContinue)) {
    Write-Host "cloudflared não encontrado. Instalando..." -ForegroundColor Yellow
    Write-Host ""
    
    try {
        winget install --id Cloudflare.cloudflared --silent --accept-package-agreements --accept-source-agreements
        
        Write-Host ""
        Write-Host "✓ cloudflared instalado com sucesso!" -ForegroundColor Green
        Write-Host ""
        Write-Host "IMPORTANTE: Feche e abra um novo PowerShell para usar o cloudflared" -ForegroundColor Yellow
        Write-Host "Depois execute o script novamente." -ForegroundColor Yellow
        Write-Host ""
        Read-Host "Pressione Enter para sair"
        exit 0
    } catch {
        Write-Host ""
        Write-Host "ERRO ao instalar cloudflared!" -ForegroundColor Red
        Write-Host "Tente manualmente: winget install --id Cloudflare.cloudflared" -ForegroundColor Yellow
        exit 1
    }
}

# Verifica se a API está rodando
Write-Host "Verificando se a API está rodando na porta 5041..." -ForegroundColor Yellow
$apiRunning = Test-NetConnection -ComputerName localhost -Port 5041 -WarningAction SilentlyContinue -InformationLevel Quiet

if (-not $apiRunning) {
    Write-Host "AVISO: API não está rodando em localhost:5041" -ForegroundColor Red
    Write-Host "Inicie a API primeiro com:" -ForegroundColor Yellow
    Write-Host "  cd ScanPlantAPI\ScanPlantAPI" -ForegroundColor White
    Write-Host "  dotnet run" -ForegroundColor White
    Write-Host ""
    $continuar = Read-Host "Deseja continuar mesmo assim? (S/N)"
    if ($continuar -ne "S" -and $continuar -ne "s") {
        exit 1
    }
}

Write-Host ""
Write-Host "Iniciando tunnel..." -ForegroundColor Green
Write-Host "Aguarde a URL do tunnel aparecer abaixo:" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Inicia o tunnel
cloudflared tunnel --url http://localhost:5041

# Este ponto só é alcançado se o tunnel for interrompido
Write-Host ""
Write-Host "Tunnel encerrado." -ForegroundColor Yellow
