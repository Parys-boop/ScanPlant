# Script para iniciar API e Tunnel automaticamente
# Execute este script para subir tudo de uma vez

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Iniciando ScanPlant (API + Tunnel)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Procurar cloudflared
$cloudflaredPath = Get-Command cloudflared -ErrorAction SilentlyContinue

if (-not $cloudflaredPath) {
    # Tentar caminho do WinGet
    $wingetPath = "$env:LOCALAPPDATA\Microsoft\WinGet\Packages\Cloudflare.cloudflared_Microsoft.Winget.Source_8wekyb3d8bbwe\cloudflared.exe"
    
    if (Test-Path $wingetPath) {
        $cloudflaredPath = $wingetPath
        Write-Host "cloudflared encontrado em: $cloudflaredPath" -ForegroundColor Green
    } else {
        Write-Host "cloudflared nao encontrado!" -ForegroundColor Red
        Write-Host "Instale com: winget install --id Cloudflare.cloudflared" -ForegroundColor Yellow
        Write-Host "Depois feche e abra um novo PowerShell" -ForegroundColor Yellow
        exit 1
    }
} else {
    $cloudflaredPath = $cloudflaredPath.Source
}

# Verifica se dotnet esta instalado
if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) {
    Write-Host "ERRO: .NET SDK nao encontrado!" -ForegroundColor Red
    Write-Host "Instale de: https://dotnet.microsoft.com/download" -ForegroundColor Yellow
    exit 1
}

Write-Host "1. Iniciando API em nova janela..." -ForegroundColor Green
$apiPath = Join-Path $scriptDir "ScanPlantAPI\ScanPlantAPI"
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$apiPath'; Write-Host 'Iniciando API...' -ForegroundColor Cyan; dotnet run"

Write-Host "2. Aguardando API inicializar (10 segundos)..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

Write-Host "3. Verificando se API esta respondendo..." -ForegroundColor Yellow
$tentativas = 0
$maxTentativas = 5
$apiOk = $false

while ($tentativas -lt $maxTentativas -and -not $apiOk) {
    $tentativas++
    Write-Host "   Tentativa $tentativas de $maxTentativas..." -ForegroundColor Gray
    
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:5041/api/auth/test" -Method GET -TimeoutSec 3 -ErrorAction SilentlyContinue
        $apiOk = $true
        Write-Host "   API esta respondendo!" -ForegroundColor Green
    } catch {
        if ($tentativas -lt $maxTentativas) {
            Start-Sleep -Seconds 3
        }
    }
}

if (-not $apiOk) {
    Write-Host "   AVISO: API pode nao estar pronta ainda" -ForegroundColor Yellow
    Write-Host "   Mas vamos continuar..." -ForegroundColor Gray
}

Write-Host ""
Write-Host "4. Iniciando Cloudflare Tunnel em nova janela..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$scriptDir'; Write-Host 'Iniciando Cloudflare Tunnel...' -ForegroundColor Cyan; Write-Host ''; & '$cloudflaredPath' tunnel --url http://localhost:5041"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Tudo iniciado!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Duas janelas foram abertas:" -ForegroundColor White
Write-Host "  1. API rodando em http://localhost:5041" -ForegroundColor Cyan
Write-Host "  2. Tunnel expondo a API via HTTPS" -ForegroundColor Cyan
Write-Host ""
Write-Host "IMPORTANTE:" -ForegroundColor Yellow
Write-Host "  - Copie a URL do tunnel que aparece na janela" -ForegroundColor White
Write-Host "  - Execute: .\atualizar-tunnel.ps1 -TunnelUrl 'https://sua-url.trycloudflare.com'" -ForegroundColor White
Write-Host ""
Write-Host "Mantenha esta janela aberta para ver os logs." -ForegroundColor Gray
Write-Host "Pressione qualquer tecla para encerrar tudo..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
