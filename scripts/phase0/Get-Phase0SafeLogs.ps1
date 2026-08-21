[CmdletBinding()]
param([int]$Lines = 200)

$ErrorActionPreference = 'Stop'
if (-not (Get-Command adb -ErrorAction SilentlyContinue)) { throw 'adb não encontrado.' }

adb logcat -d -t $Lines | Select-String -Pattern 'scanplant|expo|reactnative|AndroidRuntime' | ForEach-Object {
    $line = $_.Line
    $line = $line -replace '(?i)Bearer\s+[A-Za-z0-9._-]+', 'Bearer [REDACTED]'
    $line = $line -replace '(?i)(password|senha|token|authorization)\s*[:=]\s*[^\s,]+', '$1=[REDACTED]'
    Write-Output $line
}
