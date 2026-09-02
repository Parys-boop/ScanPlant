# Escopo aprovado — revisão formal P03-R4: portabilidade ambiental entre hosts equivalentes

## Objetivo único

Replanejar exclusivamente a incompatibilidade material confirmada do contrato ambiental P03-R3: os paths externos absolutos pertenciam ao host anterior. P03-R4 torna portável a **resolução inicial** desses recursos entre hosts equivalentes, sem enfraquecer a igualdade material dos valores já resolvidos dentro de uma execução.

## Fatos históricos imutáveis

P03-R1 e P03-R2 permanecem históricos blocked; P03-R1 consumiu sua campanha histórica e P03-R2 não iniciou campanha. P03-R3 continua aprovado e historicamente correto sob o seu contrato rígido, mas não é executável neste host: ele fixa literalmente `/home/arthur/.dotnet-scanplant-8` e `/home/arthur/.nuget/packages`, que não existem aqui. Isto é incompatibilidade contratual/ambiental, não falha de produto, ausência técnica de SDK/runtime/Stryker, nem falha do host atual.

No host atual, o HOME natural é `/home/administradorarthur`; existem localmente o SDK `8.0.424`, `Microsoft.NETCore.App` e `Microsoft.AspNetCore.App` `8.0.30` em `<host-home>/.dotnet-scanplant-8`, e o cache local `dotnet-stryker` `4.16.0` em `<host-home>/.nuget/packages/dotnet-stryker/4.16.0`. O manifest versionado continua declarando `dotnet-stryker` `4.16.0`. Nenhum download foi necessário para este diagnóstico; o diagnóstico e o planejamento não consomem campanha.

## Escopo estrito P03-R4

- Antes de qualquer preflight futuro, capturar o `host_home` natural **antes** de sanitizar `HOME`; ele deve ser diretório absoluto existente, não symlink e legível. Resolver somente `resolved_toolchain_root=$host_home/.dotnet-scanplant-8`, `resolved_dotnet_host_path=$resolved_toolchain_root/dotnet` e `resolved_nuget_packages=$host_home/.nuget/packages`.
- Validar localmente, sem download, rede, instalação, cópia ou symlink: SDK `8.0.424`, runtimes `Microsoft.NETCore.App`/`Microsoft.AspNetCore.App` `8.0.30`, tool manifest `4.16.0`, package e executável da tool `4.16.0`, e legibilidade/executabilidade dos paths resolvidos. Ausência ou divergência para antes de restore, launcher, MutationHarness e campanha.
- Congelar em um manifesto por `run-dir` os valores resolvidos e o ambiente final. Entre restore, launcher, MutationHarness e eventual campanha, devem ser idênticos: `resolved DOTNET_ROOT`, `resolved DOTNET_HOST_PATH`, `resolved NUGET_PACKAGES`, SDK, runtimes, tool version, `PATH` final, `DOTNET_CLI_HOME`, `HOME` sanitizado, `TMPDIR`, `LANG`, `LC_ALL`, cwd e run-dir. A resolução pode variar somente entre hosts equivalentes, nunca entre fases da mesma execução.
- Preservar SDK `8.0.424`, runtime `Microsoft.NETCore.App 8.0.30`, Stryker `4.16.0`, `net8.0`, os dois mutation targets existentes, concurrency `1`, reporters, thresholds, risk seam `external-fallback`, `23/23`, no máximo uma campanha e autorização humana separada.

## Limites e binding

Não alterar produção, testes, MutationHarness, dependências, `.config/dotnet-tools.json`, filtros, thresholds, configuração de campanha, worktrees, evidence histórica, P01, P02 ou release. Não substituir o username antigo pelo atual. Não executar nesta rodada `dotnet`, restore, launcher, MutationHarness, Stryker, mutation-evidence verify, build, testes, aplicação, Docker, banco, rede de aplicação, staging, commit ou push.

A aprovação humana única de P03-R4 autoriza somente os preflights não consumidores. Mesmo após passarem, campanha exige autorização humana explícita, separada, posterior e vinculada ao `HEAD` executável. Para a campanha futura, `revision == expected_revision == HEAD` executável, aprovado, commitado, sincronizado, limpo e `0/0`; ela não se vincula ao HEAD que elaborou este plano.
