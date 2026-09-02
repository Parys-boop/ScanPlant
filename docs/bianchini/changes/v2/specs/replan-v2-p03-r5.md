# Replanejamento v2 — P03-R5: contrato do MutationHarness

## Objetivo e limites

P03-R5 corrige exclusivamente o contrato que R4 provou inválido: o projeto do MutationHarness não existe no cwd do launcher e os artifacts `net8.0` requeridos pelo gate final estavam ausentes. R4 permanece evidência factual blocked; P01 permanece blocked-terminal, P02 completed, release pending, `active_execution=null`, campanha não autorizada e `campaign_count=0`. Não há patch de produto, harness, teste, projeto, dependência ou configuração. (D-009, P-013)

## Ambiente portátil comum e cwd congelado por fase

Antes de sanitizar, capturar `host_home` natural; derivar `resolved_toolchain_root=$host_home/.dotnet-scanplant-8`, `DOTNET_ROOT`, `DOTNET_HOST_PATH=$resolved_toolchain_root/dotnet` e `NUGET_PACKAGES=$host_home/.nuget/packages`. Congelar `DOTNET_MULTILEVEL_LOOKUP=0`, `DOTNET_CLI_HOME=<run-dir>/cli-home`, `HOME=<run-dir>/home`, `TMPDIR=<run-dir>/tmp`, `LANG=C`, `LC_ALL=C`, `PATH` com o toolchain na frente, SDK `8.0.424`, ambos runtimes `8.0.30`, Stryker `4.16.0` e run-dir. Não há download, rede, instalação, symlink, cópia ou fallback.

Esses valores comuns devem ser idênticos em restore de tool, launcher, harness preparation, harness final e futura campanha. Cwds são campos congelados de fase: `restore_tool_cwd=<repo>`, `launcher_cwd=<repo>/ScanPlantAPI/ScanPlantAPI`, `harness_preparation_cwd=<repo>/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness`, `harness_final_cwd` igual ao anterior e `campaign_cwd` somente se uma autorização futura o definir. Cwd declarado diferente não é drift; qualquer valor comum ou cwd não declarado é material e interrompe. (D-012, P-012)

## Preparation e gate final do MutationHarness

Após as validações R5 autocontidas do host, tool restore offline e launcher não mutacional, criar no run-dir um `NuGet.Config` que limpa todas as fontes. No cwd do harness real, executar pelo dotnet resolvido: `dotnet restore ScanPlantAPI.MutationHarness.csproj --configfile <run-dir>/NuGet.Config --ignore-failed-sources`; registrar lifecycle, ambiente, no-network proof, `obj/project.assets.json` e exit. Se falhar, parar.

Depois, no mesmo cwd e ambiente, executar `dotnet build ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-restore`; registrar lifecycle, ambiente, outputs do harness e do `ProjectReference`, hashes/metadata e exit. Se falhar ou o output esperado `bin/Debug/net8.0/ScanPlantAPI.Tests.dll` não existir, parar.

Somente então executar no mesmo cwd o gate final: `dotnet test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore`. Ele deve encerrar `0` e provar `23/23`. Não há restore/build implícito nesse gate. Falha impede campanha e mantém `campaign_count=0`. (D-010, D-011, A-006, P-011, S-005, SD-005)

## Evidence, repetição e campanha

R5 produz um novo run-dir sob `artifacts/bianchini/v2/evidence/P03-p01-mutation-r5/`; não reutiliza R4 como evidence executiva. Como run-dir é autocontido, host validation, tool restore offline e launcher não mutacional são repetidos no R5 antes da preparation. O launcher conserva seu cwd próprio; não há obrigação de compartilhá-lo com o harness.

R5 não contém campanha. Apenas uma autorização humana posterior U-008, depois de todos os gates e binding futuro `revision == expected_revision == HEAD` aprovado/commitado/sincronizado/limpo `0/0`, poderia autorizar uma campanha e então definir seu cwd congelado. Targets `ExternalFallbackUploadValidator.cs` e `ExternalFallbackService.cs`, concurrency `1`, reporters, thresholds, Stryker e seam permanecem imutáveis. O breaker acumulado 3 não é resetado: `bm.py policy` mostrou `breaker=true`, sem finding estrutural e sem `redesign_required`; R5 é somente redesenho documental, sem patch de seam. (U-007, U-008, P-013)
