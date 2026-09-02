# Delta de especificação — gate de launcher da evidence seletiva

## Contrato pós-entrega

P03-R2 só pode iniciar uma campanha Stryker depois de um preflight não consumidor que resolve e inicia o tool local `dotnet-stryker` `4.16.0` no mesmo ambiente sanitizado final. O preflight prepara o resolver cache de modo offline sob o `DOTNET_CLI_HOME` final e usa `$DOTNET tool run dotnet-stryker -- --help` sem argumento de projeto/configuração/mutação/saída; exige banner de versão, PID/lifecycle e exit `0`, e registra `campaign_count=0`.

O MutationHarness net8.0 é outro preflight não consumidor e deve observar `23/23` testes antes de uma campanha. A campanha é uma ação distinta, humana e explicitamente autorizada, limitada a uma execução com `net8.0`, concorrência `1`, `required_selective`, seam `external-fallback` e somente `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`, a partir de `ScanPlantAPI/ScanPlantAPI`.

No instante da campanha, `revision == expected_revision == HEAD` limpo, aprovado e sincronizado; sem release candidate, `mutation-evidence verify` deriva o expected revision do HEAD. Falha em qualquer preflight não consome campanha; falha após início mantém P01/P03-R2 bloqueados, sem retry e com release pending. (D-004, A-003, P-003, P-004, P-005, U-004, S-002, SD-002)
