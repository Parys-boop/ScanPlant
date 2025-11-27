# Script para fazer build e deploy rapido
# Execute este script apos atualizar o codigo

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Build e Deploy - ScanPlant Web" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$webPath = Join-Path $scriptDir "scanplant-web"

# Verifica se a pasta existe
if (-not (Test-Path $webPath)) {
    Write-Host "ERRO: Pasta scanplant-web nao encontrada!" -ForegroundColor Red
    exit 1
}

# Build
Write-Host "1. Fazendo build do frontend..." -ForegroundColor Yellow
Push-Location $webPath

npm run build

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERRO no build!" -ForegroundColor Red
    Pop-Location
    exit 1
}

Write-Host ""
Write-Host "Build concluido com sucesso!" -ForegroundColor Green

# Deploy
Write-Host ""
Write-Host "2. Fazendo deploy no Vercel..." -ForegroundColor Yellow
Write-Host ""

vercel --prod

Pop-Location

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host "   Deploy concluido!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "URL permanente: https://scanplant-web.vercel.app" -ForegroundColor Cyan
    Write-Host ""
} else {
    Write-Host ""
    Write-Host "ERRO no deploy!" -ForegroundColor Red
    exit 1
}
