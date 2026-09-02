# Delta de especificação — gate do MutationHarness P03-R5

O contrato pós-entrega separa valores ambientais comuns dos cwd congelados por fase. `launcher_cwd` pode ser `ScanPlantAPI/ScanPlantAPI`; `harness_preparation_cwd` e `harness_final_cwd` são `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness`. A igualdade exige todos os valores comuns e cada cwd contra seu valor de fase previamente declarado; não exige cwd igual entre fases distintas.

O projeto canônico é `ScanPlantAPI.MutationHarness.csproj` no cwd do harness. Antes de seu gate final, um novo run-dir R5 registra restore offline com `NuGet.Config` sem fontes e build net8.0 `--no-restore`, incluindo evidence de ausência de rede, assets e outputs. Só com ambas as fases aprovadas o comando final `dotnet test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore` pode executar e deve entregar `23/23`.

Falha em qualquer fase para antes da campanha e preserva `campaign_count=0`. R5 repete as provas não consumidoras em evidence nova; não reaproveita R4. SDK `8.0.424`, runtimes `8.0.30`, Stryker `4.16.0`, targets, concurrency `1`, reporters, thresholds, seam e exigência de autorização humana separada para campanha não mudam. (D-010, D-011, D-012, A-006, P-011, P-012, P-013, U-007, U-008, S-005, SD-005)
