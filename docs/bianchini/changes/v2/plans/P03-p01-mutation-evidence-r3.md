# P03-R3 — evidence seletiva P01 com prova composta do launcher

**Mecanismo formal:** revisão versionada de P03 após `material_change` por impossibilidade externa comprovada no contrato de banner de P03-R2. Substitui somente a entrega bloqueada; P01, P02, P03-R1, P03-R2 e toda evidence histórica permanecem imutáveis.

## Contrato de execução e limites

O executor usa linked worktree v2 aprovada, com árvore limpa e sem rede de aplicação. Um único ambiente sanitizado final é materializado uma vez e seu manifesto/digest é reutilizado sem alteração material no restore, launcher, harness e campanha: `DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8`, `DOTNET_HOST_PATH=$DOTNET_ROOT/dotnet`, `DOTNET_MULTILEVEL_LOOKUP=0`, `DOTNET_CLI_HOME=<run-dir>/cli-home`, `NUGET_PACKAGES=/home/arthur/.nuget/packages`, `PATH=$DOTNET_ROOT:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`, `HOME=<run-dir>/home`, `TMPDIR=<run-dir>/tmp`, `LANG=C`, `LC_ALL=C` e cwd `ScanPlantAPI/ScanPlantAPI` para launcher/campanha. Toda comparação registra igualdade do manifesto, SDK `8.0.424`, runtime `8.0.30`, run-dir, CLI home, NuGet packages, PATH e cwd; diferença material para antes da campanha.

O único restore de tool permitido usa `dotnet tool restore --configfile <run-dir>/NuGet.Config`, com `<packageSources><clear /></packageSources>` e sem URL. Download, source ou rede bloqueiam. Nenhuma unidade altera produção, testes, MutationHarness, dependências, `.config/dotnet-tools.json`, filtros, thresholds, componentes do método ou evidence P03-R1/P03-R2.

### Tarefa 1 — Preflights não consumidores provam identidade, resolução e harness final

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-005, A-004, P-003, P-005, P-006, P-007, U-005, S-003, SD-003

**Test seams:** local-tool resolver, ambiente .NET sanitizado, MutationHarness net8.0

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md#prova-composta-de-identidade-da-tool, docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md#resolução-real-e-ambiente-sanitizado, docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md#não-mutacional-mutationharness-e-campanha-condicional

**Files:** Somente `artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/`, `artifacts/bianchini/v2/ledgers/P01.md` e `docs/living/PROJECT_STATE.md`, depois de cada resultado factual. São proibidos produção, testes, MutationHarness, dependências, manifest local, filtros, thresholds e evidence histórica.

**Contract:** Antes de qualquer execução, registrar `campaign_count=0`, `revision == expected_revision == HEAD` aprovado, commitado, sincronizado, limpo e `0/0`; SDK `8.0.424` e runtime `Microsoft.NETCore.App 8.0.30`. Registrar manifest local `dotnet-stryker=4.16.0`, restore offline exit `0`, resolver sob o CLI home final com `Name`, `Version=4.16.0`, `TargetFramework=net8.0` e `PathToExecutable` em `NUGET_PACKAGES/dotnet-stryker/4.16.0/`, existência do alvo e SHA-256 do executável/package quando aplicável. `dotnet tool list --local`, se registrado, é complementar. No mesmo manifesto/cwd, executar exatamente `$DOTNET tool run dotnet-stryker -- --help`, registrar PID/lifecycle, exit `0`, stdout que identifica Stryker e usage/help compatível, e vincular esse processo ao mesmo resolver; nunca exigir `Version: 4.16.0` no stdout. Confirmar que a linha de comando não possui `--project`, `--config-file`, `--mutate` ou `--output`, e que não há projeto analisado, mutants, mutation-report, results/output ou campanha. Só depois preparar offline o MutationHarness se necessário e executar `$DOTNET test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore`, exigindo lifecycle/exit confiáveis e `23/23`; o contador continua `0`.

**Verification:** `python3 /home/arthur/.agents/skills/_shared/scripts/bm.py policy --profile standard --risk high --change infrastructure --manual-pdf scope --round 1 --risk-seam external-fallback --seam-round 3`; preflights sanitizados acima; `git diff --check`.

**Done when:** evidence contém manifest/digest de ambiente, manifest local/digest, restore offline, conteúdo e hash do resolver, existência e SHA-256 do executável/package quando aplicável, lifecycle/stdout/stderr do launcher real, prova de ausência de mutação, igualdade de ambiente, harness `23/23`, revision binding e `campaign_count=0`. Qualquer falha mantém P01 blocked-terminal, deixa P03-R3 blocked e impede a Tarefa 2.

### Tarefa 2 — Uma campanha seletiva autorizada produz evidence verificável

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-005, A-004, P-003, P-005, P-006, P-007, U-005, SD-003

**Test seams:** external-fallback, mutation-observability

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md#não-mutacional-mutationharness-e-campanha-condicional, docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md#binding-contadores-e-parada

**Files:** Somente `artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/`, `artifacts/bianchini/v2/ledgers/P01.md` e `docs/living/PROJECT_STATE.md`, após Tarefa 1 passada e U-005 registrada. Produção, testes, MutationHarness, dependências, manifest local, filtros, thresholds e evidence histórica são proibidos.

**Contract:** Só após Tarefa 1 e autorização humana explícita separada U-005, confirmar novamente `revision == expected_revision == HEAD` executável aprovado, commitado, sincronizado, limpo e `0/0`, e igualdade exata com o ambiente final já evidenciado. Executar uma única campanha, mudando `campaign_count` de `0` para `1`, no cwd `ScanPlantAPI/ScanPlantAPI`: `$DOTNET tool run dotnet-stryker -- --config-file <run-dir>/stryker-config.json --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --reporter json --reporter cleartext --reporter progress --verbosity trace --log-to-file --skip-version-check --output <run-dir>/results`. O config temporário contém somente os paths `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`. Após relatório e classificações legítimas, executar `bm.py mutation-evidence verify` com `--revision "$HEAD"`; sem RC, o expected revision é o HEAD do instante de execução.

**Verification:** a campanha única acima; `python3 /home/arthur/.agents/skills/_shared/scripts/bm.py mutation-evidence verify --state docs/living/PROJECT_STATE.md --root . --plan P03 --risk-seam external-fallback --tool stryker --command "$(tr '\n' ' ' < artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/campaign/command.txt)" --report artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/results/reports/mutation-report.json --classifications artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/mutation-classifications.json --revision "$(git rev-parse HEAD)" --output artifacts/bianchini/v2/evidence/P03-p01-mutation-r3/mutation-evidence.json`; `git diff --check`.

**Done when:** a única campanha tem lifecycle/exit confiáveis, relatório e classificações legítimos do escopo exato, `mutation-evidence verify` passa no HEAD executável e a revisão humana aplicável é concluída. Qualquer falha após início mantém P01/P03-R3 blocked e release pending; não inicia segunda campanha.

## Regra de parada

Antes da campanha, parar com `campaign_count=0` se identidade `4.16.0`, resolver, existência/hash aplicável, launcher/help/lifecycle/exit, igualdade de ambiente, ausência de mutação, rede/download, MutationHarness `23/23`, revision binding ou imutabilidade de código/teste/dependência/filtro/threshold falharem. Depois de a campanha começar, registrar `campaign_count=1` e parar definitivamente em qualquer falha, relatório ausente, escopo inválido, `revision-mismatch` ou mutante material não classificado; não há retry automático.
