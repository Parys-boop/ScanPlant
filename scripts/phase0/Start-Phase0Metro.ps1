[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$frontEnd = Join-Path $repoRoot 'ScanPlant-Final'
& (Join-Path $PSScriptRoot 'Test-Phase0Environment.ps1')

$info = New-Object System.Diagnostics.ProcessStartInfo
$info.FileName = $env:ComSpec
$info.Arguments = '/c npx.cmd expo start --dev-client --localhost --clear'
$info.WorkingDirectory = $frontEnd
$info.UseShellExecute = $false
$process = [System.Diagnostics.Process]::Start($info)
if (-not $process) { throw 'Não foi possível iniciar o Metro.' }

Start-Sleep -Seconds 3
adb shell monkey -p com.parysboop.scanplant 1 | Out-Null
Write-Output "Metro iniciado (PID $($process.Id)); Development Client solicitado via ADB."
