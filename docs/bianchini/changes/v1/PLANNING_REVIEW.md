{
  "verdict": "passed",
  "findings": [
    {
      "id": "NOTE-R1-001",
      "severity": "note",
      "summary": "P01-R1 é uma revisão material limitada aos sobreviventes e à cobertura de segurança do seam já bloqueado.",
      "evidence": "O plano inventaria 982, 1010, 1012, 1020, 1026 e 1028 e classifica os 15 no-coverage; conserva os dois arquivos de produção permitidos e não inclui mobile, web, Nominatim, migration, provider ou rede."
    },
    {
      "id": "NOTE-R1-002",
      "severity": "note",
      "summary": "O breaker não é dispensado nem reiniciado.",
      "evidence": "P01-R1 registra o contador histórico external-fallback em 3/3, o redesenho prévio consumido e uma única execução corretiva sem loop automático; nova falha material volta ao supervisor."
    },
    {
      "id": "NOTE-R1-003",
      "severity": "note",
      "summary": "Os comandos previstos são reproduzíveis e permanecem seletivos.",
      "evidence": "Harness net8.0, SDK isolado 8.0.424 e dotnet-stryker 4.16.0 executam sem solution mode, concorrência 1 e somente ExternalFallbackUploadValidator.cs e ExternalFallbackService.cs."
    }
  ]
}
