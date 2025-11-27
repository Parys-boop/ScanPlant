# Script para parar a API e o Tunnel
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Parando ScanPlant (API + Tunnel)" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Parar processos do dotnet (API)
Write-Host "Parando API..." -ForegroundColor Yellow
$dotnetProcesses = Get-Process -Name "ScanPlantAPI" -ErrorAction SilentlyContinue
if ($dotnetProcesses) {
    $dotnetProcesses | Stop-Process -Force
    Write-Host "  API parada" -ForegroundColor Green
} else {
    Write-Host "  API nao estava rodando" -ForegroundColor Gray
}

# Parar processos do cloudflared (Tunnel)
Write-Host ""
Write-Host "Parando Tunnel..." -ForegroundColor Yellow
$tunnelProcesses = Get-Process -Name "cloudflared" -ErrorAction SilentlyContinue
if ($tunnelProcesses) {
    $tunnelProcesses | Stop-Process -Force
    Write-Host "  Tunnel parado" -ForegroundColor Green
} else {
    Write-Host "  Tunnel nao estava rodando" -ForegroundColor Gray
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Tudo parado!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Agora voce pode executar: .\iniciar-tudo.ps1" -ForegroundColor White
