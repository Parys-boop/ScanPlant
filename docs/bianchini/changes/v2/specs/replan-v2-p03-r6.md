# Replanejamento v2 — P03-R6: isolamento de teste da campanha

## Objetivo e estado histórico

P03-R6 corrige somente o contrato operacional que a tentativa U-008 de R5 invalidou. A evidence externa em `/tmp/p03-r5-u007.h8rfIr` permanece imutável: Stryker 4.16.0 iniciou sob SDK 8.0.424, `TestProjects=[]` selecionou `ScanPlantAPI.Tests.csproj`, a solução versionada alcançou `net10.0` e o build inicial falhou com `NETSDK1045` antes de qualquer mutante ou mutation-report. O contador acumulado é `1` e U-008 está consumida. (D-013, D-016, P-016)

P03-R6 não muda P01/P02, produção, testes, `.csproj`, `TargetFrameworks`, a solução versionada, dependências, SDK/runtime, Stryker, pacote/feed de 79 itens, reporters, thresholds, concurrency ou os dois arquivos mutáveis. SDK 10 é proibido. (D-016, A-007)

## Contexto de campanha isolado

O executor R6 cria no novo run-dir, nunca no repositório, uma solução temporária com exatamente estes membros em `net8.0`:

1. `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj` como projeto fonte;
2. `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj` como único projeto de testes.

Antes de build ou Stryker, o launcher calcula SHA-256 da solução e configuração, valida que o texto contém somente esses membros e rejeita `ScanPlantAPI.sln`, `ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj` ou `net10.0`. O comando Stryker recebe tanto a solução temporária quanto `--test-project` para o harness e `--project` para a API, além de `--target-framework net8.0`. Dessa forma, `TestProjects` não pode ficar vazio e a solução multi-target não entra no grafo. (D-014, D-015, P-014, P-015, SD-006)

S-006 confirma por inspeção do log terminal e dos três projetos que este isolamento resolve a seleção incorreta sem mudar o SDK ou o grafo versionado.

## Preflight corretivo e executor

Após aprovação do pacote R6 e commit documental final, no WSL normal e no ambiente R5 já validado, um novo run-dir executa somente: validação de binding/head e cache isolado existente; geração/auditoria do contexto temporário; sintaxe e SHA-256 do launcher/configuração; build `--no-restore` da solução temporária; e `dotnet test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore` no cwd do harness, exigindo 23/23. Nenhuma aquisição, resolução de integridade, inventário de 79 pacotes, restore de tool, launcher `--help` ou preflight R5 completo se repete. Falha para antes de U-009 e mantém `campaign_count=1`. (A-007, P-017)

## U-009, binding e parada

Somente depois desse preflight, U-009 explícita pode iniciar uma nova campanha distinta. O launcher descobre e fixa o commit documental final então existente; ele exige `revision == expected_revision == HEAD == upstream`, branch `bm/v2-p03`, árvore limpa e `0/0`. Não se vincula ao HEAD de elaboração `716ef26` depois que a documentação for commitada.

O launcher grava atomicamente a única transição `1 -> 2` antes de invocar Stryker. Seu resultado usa apenas output no run-dir, cache/CLI home isolados, concurrency `1`, Stryker `4.16.0`, net8.0, o harness explícito e exclusivamente `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`. Falha após início preserva `campaign_count=2`, U-009 consumida e bloqueio terminal, sem retry. (P-016, U-009)
