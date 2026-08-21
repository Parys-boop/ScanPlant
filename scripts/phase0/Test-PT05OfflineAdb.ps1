[CmdletBinding()]
param(
    [int]$TimeoutSeconds = 20,
    [string]$PackageName = 'com.parysboop.scanplant'
)

$ErrorActionPreference = 'Stop'
if (-not (Get-Command adb -ErrorAction SilentlyContinue)) { throw 'adb não encontrado.' }

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$evidenceDirectory = Join-Path $repoRoot 'evidence\pt05'
New-Item -ItemType Directory -Force -Path $evidenceDirectory | Out-Null
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$logFile = Join-Path $evidenceDirectory "pt05-$stamp.log"
$screenshotFile = Join-Path $evidenceDirectory "pt05-$stamp.png"

$devices = @(adb devices | Select-String -Pattern '^\S+\s+device$' | ForEach-Object { ($_ -split '\s+')[0] })
if ($devices.Count -ne 1) { throw "É necessário exatamente um Android autorizado; encontrados: $($devices.Count)." }

$wifiBefore = (adb shell settings get global wifi_on).Trim()
$dataBefore = (adb shell settings get global mobile_data).Trim()
$reverseBefore = @(adb reverse --list)
$deviceScreenshot = "/sdcard/pt05-$stamp.png"

function Restore-DeviceState {
    if ($wifiBefore -eq '1') { adb shell svc wifi enable | Out-Null } else { adb shell svc wifi disable | Out-Null }
    if ($dataBefore -eq '1') { adb shell svc data enable | Out-Null } else { adb shell svc data disable | Out-Null }
    adb reverse --remove-all | Out-Null
    foreach ($line in $reverseBefore) {
        $parts = $line -split '\s+'
        if ($parts.Count -ge 3) { adb reverse $parts[-2] $parts[-1] | Out-Null }
        elseif ($parts.Count -ge 2) { adb reverse $parts[0] $parts[1] | Out-Null }
    }
}

try {
    $metro = Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:8081/status' -TimeoutSec 5
    $metroStatus = if ($metro.Content -is [byte[]]) { [Text.Encoding]::UTF8.GetString($metro.Content) } else { [string]$metro.Content }
    if ($metroStatus -notmatch 'packager-status:running') { throw 'Metro não confirmou prontidão em tcp:8081.' }
    adb logcat -c
    adb reverse --remove-all | Out-Null
    adb reverse tcp:8081 tcp:8081 | Out-Null
    $reverse = @(adb reverse --list | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if ($reverse.Count -ne 1 -or $reverse[0] -notmatch 'tcp:8081\s+tcp:8081') { throw 'Somente a reversão USB tcp:8081 deve permanecer ativa.' }

    adb shell svc wifi disable | Out-Null
    adb shell svc data disable | Out-Null
    Start-Sleep -Seconds 2
    adb shell am force-stop $PackageName | Out-Null
    adb shell am start -W -a android.intent.action.VIEW -d 'exp+scanplant://expo-development-client/?url=http%3A%2F%2F127.0.0.1%3A8081' | Out-Null

    $deadline = (Get-Date).AddSeconds($TimeoutSeconds)
    $mounted = $null
    $resultLine = $null
    while ((Get-Date) -lt $deadline) {
        if (-not $mounted) { $mounted = @(adb logcat -d -v brief | Select-String -SimpleMatch 'PT05_STAGE {"stage":"screen-mounted"' | Select-Object -Last 1) }
        $resultLine = @(adb logcat -d -v brief | Select-String -SimpleMatch 'PT05_RESULT' | Select-Object -Last 1)
        if ($mounted.Count -gt 0 -and $resultLine.Count -gt 0) { break }
        Start-Sleep -Milliseconds 500
    }
    if (-not $mounted) { throw "PT05_STAGE screen-mounted não apareceu em $TimeoutSeconds segundos." }
    if (-not $resultLine) { throw "PT05_RESULT não apareceu em $TimeoutSeconds segundos." }

    adb logcat -d -v time | Select-String -Pattern 'PT05_RESULT|scanplant|AndroidRuntime|ReactNativeJS' | ForEach-Object {
        $line = $_.Line
        $line = $line -replace '(?i)Bearer\s+[A-Za-z0-9._-]+', 'Bearer [REDACTED]'
        $line = $line -replace '(?i)(password|senha|token|authorization)\s*[:=]\s*[^\s,]+', '$1=[REDACTED]'
        $line
    } | Set-Content -LiteralPath $logFile -Encoding utf8
    adb shell screencap -p $deviceScreenshot | Out-Null
    adb pull $deviceScreenshot $screenshotFile | Out-Null
    adb shell rm -f $deviceScreenshot | Out-Null
    if (-not (Test-Path $screenshotFile) -or (Get-Item $screenshotFile).Length -eq 0) { throw 'Falha ao capturar screenshot.' }

    $jsonText = ($resultLine[-1].Line -replace '^.*PT05_RESULT\s+', '')
    $result = $jsonText | ConvertFrom-Json
    if ($result.status -eq 'error' -or -not $result.passed) { throw "A prova PT-05 não foi aprovada: $jsonText" }
    Write-Output "PASS PT-05 offline. Log: $logFile Screenshot: $screenshotFile"
} finally {
    Restore-DeviceState
}
