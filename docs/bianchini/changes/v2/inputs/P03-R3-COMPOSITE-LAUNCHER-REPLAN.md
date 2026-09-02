# Escopo aprovado — revisão formal P03-R3: prova composta do launcher

## Objetivo

Replanejar exclusivamente a entrega bloqueada de P03-R2. A revisão substitui o gate impossível que exigia `Version: 4.16.0` no stdout de `dotnet tool run dotnet-stryker -- --help` por uma prova composta, factual e não mutacional de identidade da tool, resolução real do launcher e ausência de mutation analysis.

## Fatos históricos imutáveis

P03-R1 e P03-R2 permanecem históricos. P03-R1 consumiu sua campanha `1/1` e falhou antes de mutation analysis porque o resolver não existia no CLI home sanitizado. P03-R2 não executou campanha: o restore offline terminou com exit `0`, materializou o resolver local `dotnet-stryker` `4.16.0` no CLI home final e o único launcher `--help` terminou com exit `0`, PID/lifecycle e ajuda real do Stryker. P03-R2 bloqueou somente porque o contrato então vigente exigia o banner literal `Version: 4.16.0`, ausente no caminho de help. O digest agregado da run histórica `preflight-run-ZBwbUU` é `cba24f19e17666608797375be8cea833f92d552ba286ee2ab8bfeadaf44c74b6`; `campaign_count=0`.

## Escopo limitado de P03-R3

- Antes de aceitar o launcher, provar conjuntamente: `.config/dotnet-tools.json` declara `dotnet-stryker` `4.16.0`; restore offline no `DOTNET_CLI_HOME` final tem exit `0`; resolver cache do mesmo CLI home declara `Name=dotnet-stryker`, `Version=4.16.0`, `TargetFramework=net8.0` e `PathToExecutable` sob `NUGET_PACKAGES/dotnet-stryker/4.16.0/`; o executável existe; e registrar SHA-256 dele quando o ambiente o permitir. `dotnet tool list --local`, se usado, é complementar e nunca prova única.
- No mesmo ambiente final, usar exatamente `dotnet tool run dotnet-stryker -- --help` para provar processo observado, PID/lifecycle, exit `0`, stdout de help compatível com a CLI Stryker e correspondência com o resolver materializado. O help não deve provar versão por banner.
- O launcher não recebe `--project`, `--config-file`, `--mutate` ou `--output`; a evidence deve provar nenhum projeto analisado, mutant criado, mutation-report, results/output de campanha e `campaign_count=0`.
- Somente após o launcher composto passar, preparar offline o MutationHarness se necessário e executar o harness existente em `net8.0`, `--no-build --no-restore`, com `23/23`; isto também mantém `campaign_count=0`.
- Uma campanha futura, e somente uma, continua condicionada a autorização humana explícita e posterior. Mantém Stryker `4.16.0`, SDK `8.0.424`, runtime `8.0.30`, `net8.0`, concurrency `1`, policy `required_selective`, seam `external-fallback` e somente `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`.

## Limites e binding

O ambiente sanitizado é único e materialmente idêntico no restore, launcher, harness e eventual campanha: mesmo run-dir, `DOTNET_ROOT`, `DOTNET_HOST_PATH`, `DOTNET_MULTILEVEL_LOOKUP`, `DOTNET_CLI_HOME`, `NUGET_PACKAGES`, `PATH`, `HOME`, `TMPDIR`, `LANG`, `LC_ALL` e cwd efetivo. A evidence futura só pode executar quando `revision == expected_revision == HEAD` executável, com HEAD aprovado, commitado, sincronizado, árvore limpa e divergência `0/0`; ela não é vinculada ao HEAD de elaboração `80b7ca2bc93209301b9f69e88c727ec7f43cbffb`.

Não alterar produção, testes, MutationHarness, dependências, manifest local, filtros, thresholds, provider, banco, credenciais, créditos, rede de aplicação, componentes do método ou evidence histórica. Não executar nesta rodada launcher, restore, MutationHarness, Stryker, campanha, mutation testing, commit, push, merge, rebase ou PR.

## Aprovação necessária

Este escopo autoriza somente planejamento. A aprovação humana única do pacote P03-R3 é necessária antes dos preflights não consumidores. Após todos passarem, uma segunda autorização humana explícita, separada e vinculada ao HEAD executável é necessária para iniciar uma única campanha. Sem ela, a campanha não começa.
