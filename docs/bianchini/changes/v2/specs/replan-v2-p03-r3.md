# Replanejamento v2 — P03-R3: prova composta do launcher

## Objetivo e limites

P03-R3 é a revisão formal mínima do contrato bloqueado de P03-R2. P01 permanece blocked-terminal e P02 permanece completed. A revisão não muda produto, testes, dependências, MutationHarness, ferramenta, filtros, thresholds, providers, banco, credenciais ou evidence histórica. P03-R1, P03-R2 e `preflight-run-ZBwbUU` são imutáveis; P03-R2 bloqueou corretamente sob seu contrato vigente, sem campanha. (D-001, D-002, D-005, A-001, P-001, P-002)

## Prova composta de identidade da tool

No run sanitizado final, a identidade aceita somente a combinação de: manifest local declarando `dotnet-stryker` `4.16.0`; restore offline de exit `0` com sources limpas; resolver cache sob o mesmo `DOTNET_CLI_HOME` com `Name=dotnet-stryker`, `Version=4.16.0`, `TargetFramework=net8.0` e `PathToExecutable` sob o `NUGET_PACKAGES` autorizado em `dotnet-stryker/4.16.0/`; existência desse alvo; e SHA-256 do executável/package quando aplicável. `dotnet tool list --local` é no máximo evidência complementar. (D-005, A-004, P-006, S-003, SD-003)

## Resolução real e ambiente sanitizado

O restore, launcher, harness e campanha reutilizam um único run-dir e o mesmo manifesto de `DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8`, `DOTNET_HOST_PATH`, `DOTNET_MULTILEVEL_LOOKUP=0`, `DOTNET_CLI_HOME`, `NUGET_PACKAGES=/home/arthur/.nuget/packages`, `PATH`, `HOME`, `TMPDIR`, `LANG=C`, `LC_ALL=C` e cwd `ScanPlantAPI/ScanPlantAPI` quando aplicável. Divergência material interrompe antes da campanha. O launcher é exatamente `dotnet tool run dotnet-stryker -- --help`; deve ter PID/lifecycle, exit `0` e help textual que identifica/usa a CLI Stryker, correlacionado ao resolver, mas não precisa imprimir banner de versão. (D-005, P-006, P-007, SD-003)

## Não mutacional, MutationHarness e campanha condicional

O launcher recebe nenhum `--project`, `--config-file`, `--mutate` ou `--output`. Sua evidence comprova nenhum projeto analisado, mutant, mutation-report, results/output de campanha e `campaign_count=0`. Só então o MutationHarness existente pode ser preparado offline se necessário e rodar com `net8.0 --no-build --no-restore`, lifecycle/exit confiáveis e `23/23`, sem alterar o contador. A campanha futura única exige U-005 posterior e preserva Stryker `4.16.0`, SDK `8.0.424`, runtime `8.0.30`, net8.0, concurrency `1`, `required_selective`, seam `external-fallback` e os dois paths autorizados. (A-004, P-005, P-006, P-007, U-005, SD-003)

## Binding, contadores e parada

Não há binding ao HEAD de elaboração. Imediatamente antes da campanha e no verificador, `revision == expected_revision == HEAD` executável, que deve estar aprovado, commitado, sincronizado com upstream, limpo e em divergência `0/0`. Antes da campanha, qualquer lacuna de identidade, resolver, help/lifecycle/exit, ambiente, rede/download, harness, binding ou necessidade de mudança para com `campaign_count=0`. Ao iniciar a única campanha, o contador passa a `1`; qualquer falha posterior interrompe definitivamente, sem retry. (P-003, P-005, P-006, P-007, U-005)
