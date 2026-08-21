[CmdletBinding()]
param([string]$ApiBaseUrl = 'http://127.0.0.1:5041')

$ErrorActionPreference = 'Stop'
$pass = 0
$fail = 0
$token = $null

function Invoke-Request([string]$Method, [string]$Path, $Body, [hashtable]$Headers = @{}) {
    $parameters = @{ Uri = "$ApiBaseUrl$Path"; Method = $Method; UseBasicParsing = $true; ErrorAction = 'Stop'; Headers = $Headers }
    if ($null -ne $Body) { $parameters.ContentType = 'application/json'; $parameters.Body = ($Body | ConvertTo-Json -Compress) }
    try {
        $response = Invoke-WebRequest @parameters
        return [pscustomobject]@{ Status = [int]$response.StatusCode; Content = $response.Content }
    } catch [System.Net.WebException] {
        $response = $_.Exception.Response
        if (-not $response) { throw }
        $reader = New-Object IO.StreamReader($response.GetResponseStream())
        try { $content = $reader.ReadToEnd() } finally { $reader.Dispose() }
        return [pscustomobject]@{ Status = [int]$response.StatusCode; Content = $content }
    }
}

function Assert-Status([string]$Name, $Response, [int[]]$Expected) {
    if ($Expected -contains $Response.Status) { $script:pass++; Write-Output "PASS $Name ($($Response.Status))" }
    else { $script:fail++; Write-Output "FAIL $Name (HTTP $($Response.Status))" }
}

try {
    $health = Invoke-Request GET '/health' $null
    $healthBody = $health.Content | ConvertFrom-Json
    if ($health.Status -ne 200 -or $healthBody.environment -ne 'phase0') { throw 'A API não confirmou o ambiente isolado da Fase 0.' }
    Assert-Status 'health' $health @(200)

    $id = [Guid]::NewGuid().ToString('N')
    $email = "phase0-$id@example.invalid"
    $password = "Aa1$id"
    $registration = Invoke-Request POST '/api/auth/register' @{ email = $email; password = $password; name = 'Smoke Phase0' }
    Assert-Status 'register' $registration @(200)
    $duplicate = Invoke-Request POST '/api/auth/register' @{ email = $email; password = $password; name = 'Smoke Phase0' }
    Assert-Status 'duplicate-register' $duplicate @(409)
    $login = Invoke-Request POST '/api/auth/login' @{ email = $email; password = $password }
    Assert-Status 'login' $login @(200)

    if ($login.Status -eq 200) {
        $token = ($login.Content | ConvertFrom-Json).token
        $headers = @{ Authorization = "Bearer $token" }
        Assert-Status 'auth-me' (Invoke-Request GET '/api/auth/me' $null $headers) @(200)
        Assert-Status 'chats' (Invoke-Request GET '/api/chats' $null $headers) @(200)
        Assert-Status 'auth-users' (Invoke-Request GET '/api/auth/users' $null $headers) @(200)
        Assert-Status 'plants' (Invoke-Request GET '/api/plants' $null $headers) @(200)
    }
} catch {
    $fail++
    Write-Output 'FAIL smoke initialization or isolated API verification.'
} finally {
    $token = $null
    $password = $null
    Remove-Item Env:PGPASSWORD -ErrorAction SilentlyContinue
}

Write-Output "Resumo: PASS=$pass FAIL=$fail"
if ($fail -gt 0) { exit 1 }
