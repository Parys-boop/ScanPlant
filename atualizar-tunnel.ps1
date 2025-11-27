# Script para atualizar a URL do tunnel no codigo e fazer redeploy
# Execute este script apos copiar a nova URL do tunnel

param(
    [Parameter(Mandatory=$true)]
    [string]$TunnelUrl
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Remove barra no final se houver
$TunnelUrl = $TunnelUrl.TrimEnd('/')

# Valida URL
if (-not ($TunnelUrl -match '^https://.*\.trycloudflare\.com$')) {
    Write-Host "ERRO: URL invalida!" -ForegroundColor Red
    Write-Host "Formato esperado: https://xxx.trycloudflare.com" -ForegroundColor Yellow
    Write-Host "Exemplo: https://blocking-vocals-isolated-thee.trycloudflare.com" -ForegroundColor Gray
    exit 1
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Atualizando Tunnel URL" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Nova URL: $TunnelUrl" -ForegroundColor Green
Write-Host ""

# Atualiza apiConfig.ts
$apiConfigPath = Join-Path $scriptDir "scanplant-web\src\apiConfig.ts"
Write-Host "1. Atualizando apiConfig.ts..." -ForegroundColor Yellow

$content = Get-Content $apiConfigPath -Raw

# Procura por padrao de URL do Cloudflare
$pattern = "return 'https://[^']*\.trycloudflare\.com/api'"
$replacement = "return '$TunnelUrl/api'"

if ($content -match $pattern) {
    $newContent = $content -replace $pattern, $replacement
    Set-Content -Path $apiConfigPath -Value $newContent -NoNewline
    Write-Host "   apiConfig.ts atualizado" -ForegroundColor Green
} else {
    Write-Host "   ERRO: Padrao nao encontrado em apiConfig.ts" -ForegroundColor Red
    Write-Host "   Atualize manualmente a URL para: $TunnelUrl/api" -ForegroundColor Yellow
    exit 1
}

# Build do frontend
Write-Host ""
Write-Host "2. Fazendo build do frontend..." -ForegroundColor Yellow
$webPath = Join-Path $scriptDir "scanplant-web"
Push-Location $webPath

npm run build

if ($LASTEXITCODE -ne 0) {
    Write-Host "   ERRO no build!" -ForegroundColor Red
    Pop-Location
    exit 1
}

Write-Host "   Build concluido" -ForegroundColor Green

# Deploy no Vercel
Write-Host ""
Write-Host "3. Fazendo deploy no Vercel..." -ForegroundColor Yellow
Write-Host ""

vercel --prod

Pop-Location

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Deploy concluido!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "URL do Tunnel: $TunnelUrl" -ForegroundColor Cyan
Write-Host ""
Write-Host "LEMBRETE:" -ForegroundColor Yellow
Write-Host "  - Mantenha a janela do tunnel aberta" -ForegroundColor White
Write-Host "  - Mantenha a API rodando" -ForegroundColor White
Write-Host "  - Esta URL muda toda vez que reiniciar o tunnel" -ForegroundColor White
