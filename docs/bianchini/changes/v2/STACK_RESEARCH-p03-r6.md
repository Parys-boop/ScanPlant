# Stack Research — P03-R6 isolamento do projeto de testes

Research mode: repo_only

Motivo: a decisão é determinada pelo grafo local de projetos, o log factual da tentativa U-008 e versões já congeladas; não há dependência, API ou versão nova a pesquisar.

## Stack detectada

- SDK isolado: `8.0.424`; runtime de campanha: `net8.0`.
- Tool local: `dotnet-stryker` `4.16.0`, cuja integridade e feed offline de 79 pacotes já foram aprovados.
- API: `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj`, `net8.0`.
- Harness: `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj`, `net8.0`, com `ProjectReference` para a API.
- Projeto não autorizado para a campanha R6: `ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj`, `net8.0;net10.0`.

## Inventário local

- Manifests: `.config/dotnet-tools.json`, os três `.csproj` e `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln`.
- Lockfiles: nenhum altera o grafo contratado.
- CI: `.github/workflows/deploy.yml` é somente web e não participa do fluxo .NET.
- Testes: a complementação WSL em `/tmp/p03-r5-u007.h8rfIr/host-completion/mutation-harness.log` registra 23/23 do harness.
- Padrões locais: P03-R5 já congelou cache/feed isolados, `net8.0`, concurrency `1`, e os dois mutate paths.

## Decisões aplicadas

- S-006 confirma que o log terminal e o grafo local bastam para distinguir o harness do projeto multi-target.
- O launcher R6 gerará somente no run-dir uma solução temporária com dois membros: API e MutationHarness. Ele a passará explicitamente ao Stryker.
- O comando de campanha declarará o harness por `--test-project` e conservará `--project` para a API, ambos em `net8.0`.
- Antes de build ou Stryker, o preflight verificará a lista exata de membros da solução temporária e rejeitará `ScanPlantAPI.sln`, `ScanPlantAPI.Tests.csproj` e qualquer referência a `net10.0`.
- O preflight e a campanha usarão WSL normal; o sandbox Codex não é executor apto para o socket local do VSTest.

## Alternativas rejeitadas

- SDK 10: viola o SDK 8.0.424 congelado e não corrige a seleção do projeto.
- Alterar `TargetFrameworks` ou a solução versionada: muda produção/projeto sem necessidade e está fora do escopo.
- Deixar `TestProjects` vazio: R5 provou que a seleção automática alcança o projeto multi-target.

## Riscos e lacunas

- Stryker deve respeitar simultaneamente a solução temporária e `--test-project`; por isso o preflight R6 constrói o mesmo contexto e valida o launcher/configuração antes de U-009.
- Não há permissão para redownload, novo inventário de feed, alteração de cache global ou nova campanha antes de U-009.
