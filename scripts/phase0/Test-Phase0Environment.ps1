[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'

function Require-Command([string]$Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Ferramenta obrigatória não encontrada: $Name"
    }
}

Require-Command node
Require-Command npm.cmd
Require-Command dotnet
Require-Command adb

$postgres = Get-Service -Name 'postgresql*' -ErrorAction SilentlyContinue | Where-Object Status -eq 'Running'
if (-not $postgres) { throw 'Nenhum serviço PostgreSQL em execução foi encontrado.' }

$devices = @(adb devices | Select-String -Pattern '^\S+\s+device$' | ForEach-Object { ($_ -split '\s+')[0] })
if ($devices.Count -ne 1) { throw "É necessário exatamente um Android autorizado; encontrados: $($devices.Count)." }

foreach ($port in 5041, 8081) {
    $listeners = @(Get-NetTCPConnection -State Listen -LocalPort $port -ErrorAction SilentlyContinue)
    foreach ($listener in $listeners) {
        $process = Get-Process -Id $listener.OwningProcess -ErrorAction SilentlyContinue
        Write-Output "PORT $port em uso por PID $($listener.OwningProcess) ($($process.ProcessName))."
    }
}

adb reverse tcp:8081 tcp:8081 | Out-Null
adb reverse tcp:5041 tcp:5041 | Out-Null
$reverse = @(adb reverse --list)
foreach ($required in 'tcp:8081 tcp:8081', 'tcp:5041 tcp:5041') {
    if (-not ($reverse -match [regex]::Escape($required))) { throw "adb reverse não confirmado para $required." }
}

Write-Output 'PASS ambiente: Node, npm.cmd, .NET, PostgreSQL, ADB e reversões USB prontos.'
