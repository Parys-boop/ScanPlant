[CmdletBinding()]
param(
    [string]$DbHost = '127.0.0.1',
    [int]$DbPort = 5432,
    [string]$DbUser = 'postgres',
    [Security.SecureString]$DbPassword
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$apiDirectory = Join-Path $repoRoot 'ScanPlantAPI\ScanPlantAPI'
if (-not (Get-Command dotnet -ErrorAction SilentlyContinue)) { throw 'dotnet não encontrado.' }
if (-not $DbPassword) { $DbPassword = Read-Host 'Senha do PostgreSQL' -AsSecureString }

$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($DbPassword)
try {
    $password = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr)
    $connectionString = "Host=$DbHost;Port=$DbPort;Database=ScanPlantPhase0;Username=$DbUser;Password=$password"
    $bytes = New-Object byte[] 64
    $rng = [Security.Cryptography.RandomNumberGenerator]::Create()
    try { $rng.GetBytes($bytes) } finally { $rng.Dispose() }
    $jwtKey = [Convert]::ToBase64String($bytes)

    $info = New-Object System.Diagnostics.ProcessStartInfo
    $info.FileName = 'dotnet'
    $info.Arguments = 'run --launch-profile http'
    $info.WorkingDirectory = $apiDirectory
    $info.UseShellExecute = $false
    $info.EnvironmentVariables['ConnectionStrings__DefaultConnection'] = $connectionString
    $info.EnvironmentVariables['JWT__KEY'] = $jwtKey
    $info.EnvironmentVariables['Phase0__Enabled'] = 'true'
    $process = [System.Diagnostics.Process]::Start($info)
    if (-not $process) { throw 'Não foi possível iniciar a API.' }
    Write-Output "API Fase 0 iniciada (PID $($process.Id)). O banco legado não foi selecionado."
} finally {
    if ($bstr -ne [IntPtr]::Zero) { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
    Remove-Variable password, connectionString, jwtKey, bytes -ErrorAction SilentlyContinue
    Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
}
