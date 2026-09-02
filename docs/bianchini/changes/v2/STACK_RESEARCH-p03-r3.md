# Stack Research — P03-R3 prova composta do launcher

Research mode: targeted_web

Motivo: a semântica de tools locais do SDK .NET e a separação entre help e execução normal da CLI Stryker são versionáveis; a evidence P03-R2 determina a correção do contrato, mas não substitui a documentação da forma suportada de invocação.

## Stack detectada

- SDK isolado `8.0.424` em `/home/arthur/.dotnet-scanplant-8`, runtime `Microsoft.NETCore.App 8.0.30`, aplicação e MutationHarness `net8.0`.
- `.config/dotnet-tools.json` declara `dotnet-stryker` `4.16.0`; a evidence P03-R2 materializou no CLI home final um resolver para `/home/arthur/.nuget/packages/dotnet-stryker/4.16.0/tools/net8.0/any/Stryker.CLI.dll`.
- O transcript P03-R2 de `dotnet tool run dotnet-stryker -- --help` identificou Stryker, exibiu usage/options e encerrou com exit `0`, sem `Version: 4.16.0`.

## Fontes primárias

- Fonte primária: .NET tools — invocação de tool local.
  URL: https://learn.microsoft.com/en-us/dotnet/core/tools/global-tools
  Acessado em: 2026-09-02
  Aplicação: mantém `dotnet tool run <COMMAND_NAME>` como forma longa para tool local no escopo do manifest.

- Fonte primária: dotnet tool install — armazenamento de tools locais.
  URL: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-tool-install
  Acessado em: 2026-09-02
  Aplicação: sustenta que resolver/shim pertence ao CLI home; o restore e o launcher precisam compartilhar esse ambiente.

- Fonte primária: Stryker.NET release `dotnet-stryker@4.16.0`.
  URL: https://github.com/stryker-mutator/stryker-net/releases/tag/dotnet-stryker%404.16.0
  Acessado em: 2026-09-02
  Aplicação: mantém a versão fixada, sem upgrade ou troca de ferramenta.

- Fonte primária: Stryker.NET configuration.
  URL: https://stryker-mutator.io/docs/stryker-net/configuration/
  Acessado em: 2026-09-02
  Aplicação: separa argumentos/configuração de análise de um caminho de help sem entrada mutacional.

## Decisões aplicadas

- A versão é provada por manifest, restore offline, conteúdo do resolver no CLI home final, existência do executável apontado sob o cache NuGet autorizado e hash SHA-256 do binário quando calculável; nenhum sinal isolado basta.
- O launcher prova resolução/início por lifecycle, exit `0` e help textual de Stryker; não exige banner de versão que o help não promete.
- O mesmo manifesto de ambiente e run-dir é comparado em restore, launcher, harness e campanha. `dotnet tool list --local` pode ser registrado somente como corroborante.

## Alternativas rejeitadas

- Exigir `Version: 4.16.0` de `--help` — o transcript P03-R2 mostra que este texto não é contrato do caminho de help.
- Usar `dotnet tool list --local` como prova única — não prova resolução no CLI home final.
- Executar Stryker em modo normal, configuração sentinela, restore com rede, instalação global ou atualização — amplia escopo ou pode iniciar análise.

## Riscos e lacunas

- Ausência de qualquer elo da prova composta bloqueia antes da campanha e conserva `campaign_count=0`.
- A campanha continua ação irreversível separada, limitada a uma execução e dependente de autorização humana posterior.
