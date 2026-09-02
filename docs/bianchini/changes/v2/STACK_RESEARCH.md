# Stack Research — P03-R2 launcher gate

Research mode: targeted_web

Motivo: a decisão depende de semântica versionável do SDK .NET para tools locais e da CLI Stryker `4.16.0`; a evidência local explica o defeito, mas não é suficiente para escolher a prova não mutacional.

## Stack detectada

- SDK isolado: `8.0.424` em `/home/arthur/.dotnet-scanplant-8`; runtime `Microsoft.NETCore.App 8.0.30`; aplicação e MutationHarness `net8.0`.
- Tool local: `.config/dotnet-tools.json` fixa o comando `dotnet-stryker` em `4.16.0`.
- Launcher efetivo histórico: `dotnet tool run dotnet-stryker -- ...`, a partir de `ScanPlantAPI/ScanPlantAPI`; o config de mutação usa caminhos relativos `Services/...`.

## Fontes primárias

- Fonte primária: .NET tools — invocação de tool local.
  URL: https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools
  Acessado em: 2026-09-02
  Aplicação: confirma `dotnet tool run <COMMAND_NAME>` como forma longa de invocar tool local dentro do escopo do manifest.

- Fonte primária: dotnet tool install — armazenamento de tools locais.
  URL: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install
  Acessado em: 2026-09-02
  Aplicação: confirma que tools locais usam o NuGet global e shims em `$HOME/.dotnet/toolResolverCache`; portanto `DOTNET_CLI_HOME` sanitizado precisa conter resolver materializado para o ambiente final.

- Fonte primária: Stryker.NET release `dotnet-stryker@4.16.0`.
  URL: https://github.com/stryker-mutator/stryker-net/releases/tag/dotnet-stryker%404.16.0
  Acessado em: 2026-09-02
  Aplicação: confirma a versão fixada; não autoriza upgrade ou troca de ferramenta.

- Fonte primária: Stryker.NET configuration.
  URL: https://stryker-mutator.io/docs/stryker-net/configuration/
  Acessado em: 2026-09-02
  Aplicação: confirma que a execução normal inicia análise/mutação a partir de projeto/configuração; por isso o gate de launcher não fornece `--project`, `--config-file`, `--mutate` nem `--output`.

## Decisões aplicadas

- Usar `dotnet tool restore` estritamente offline no `DOTNET_CLI_HOME` que a campanha reutilizará, seguido de `dotnet tool run dotnet-stryker -- --help`; o segundo comando prova resolução e início real sem fornecer entrada de mutação.
- Correlacionar manifest fixado, shim do resolver, banner `Version: 4.16.0`, lifecycle e exit code `0`; nenhuma das verificações isoladas basta.
- Preservar o precedente P03 de cwd `ScanPlantAPI/ScanPlantAPI`, `--project ScanPlantAPI.csproj`, `net8.0`, concorrência `1` e dois caminhos `Services/...`.

## Alternativas rejeitadas

- `dotnet tool list --local` ou somente inspeção de manifest/cache — identifica intenção/arquivos, mas não prova que o launcher inicia no CLI home final.
- Configuração sentinela que entra no Stryker — pode atravessar análise de projeto e não é necessária para provar resolução.
- Restore com fonte/rede, instalação global ou atualização de tool — extrapola o escopo e viola o requisito offline.

## Riscos e lacunas

- A ajuda deve produzir o banner e lifecycle esperados no ambiente final; qualquer divergência é bloqueio pré-campanha, não autorização para adaptar argumentos.
- A campanha continua uma ação irreversível distinta do preflight e exige autorização humana depois dos gates.
