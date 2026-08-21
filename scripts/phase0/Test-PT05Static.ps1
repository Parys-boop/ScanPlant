[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$frontEnd = Join-Path $repoRoot 'ScanPlant-Final'

Push-Location $frontEnd
try {
    npm.cmd run validate:pt05
    if ($LASTEXITCODE -ne 0) { throw 'Validação estática PT-05 falhou.' }
} finally {
    Pop-Location
}
