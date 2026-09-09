# Delta de especificação — isolamento do projeto de testes da campanha P03-R6

A campanha P03 aceita somente uma solução temporária criada no run-dir com a API `net8.0` e `ScanPlantAPI.MutationHarness.csproj` `net8.0`. O Stryker recebe `--solution <temporary-net8-solution>`, `--project <API csproj>` e `--test-project <MutationHarness csproj>`; `TestProjects=[]`, `ScanPlantAPI.sln`, `ScanPlantAPI.Tests.csproj` e `net10.0` são condições de bloqueio antes de build ou mutação.

O preflight corretivo no WSL normal prova a seleção, a solução, sintaxe/SHA-256, build `--no-restore` do contexto e o harness final `23/23`. Ele reutiliza gates imutáveis R5 e mantém `campaign_count=1`.

U-008 é histórica e consumida. U-009 posterior, única e ligada ao commit documental final pode permitir a transição atômica `1 -> 2`; falha posterior não admite retry. Código, projetos versionados, TargetFrameworks, SDK 8.0.424, Stryker 4.16.0, cache isolado, concurrency 1, reporters, thresholds e os dois mutation targets não mudam. (D-014, D-015, P-014, P-015, P-016, U-009, SD-006)
