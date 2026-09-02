# P03-R2 — evidence seletiva P01 com gate real do launcher

**Mecanismo formal:** revisão versionada de P03 após `material_change` por impossibilidade externa comprovada no launcher de P03-R1. Substitui somente a entrega bloqueada de P03; P01, P02 e a evidence P03-R1 são históricos imutáveis.

## Contrato de execução e limites

O executor trabalha em linked worktree v2 aprovada, com árvore limpa e sem rede de aplicação. O ambiente sanitizado é reconstituído uma vez e seu manifesto de variáveis é a fonte única para os dois preflights e, se autorizada, para a campanha: `DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8`, `DOTNET_HOST_PATH=$DOTNET_ROOT/dotnet`, `DOTNET_MULTILEVEL_LOOKUP=0`, `DOTNET_CLI_HOME=<run-dir>/cli-home`, `NUGET_PACKAGES=/home/arthur/.nuget/packages`, `PATH=$DOTNET_ROOT:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin`, `HOME=<run-dir>/home`, `TMPDIR=<run-dir>/tmp`, `LANG=C` e `LC_ALL=C`. O launcher, o preflight do harness e a campanha usam exatamente esses valores e o mesmo `run-dir`; a diferença material em variável, SDK, runtime, `DOTNET_CLI_HOME`, `NUGET_PACKAGES`, `PATH`, cwd ou manifesto interrompe antes da campanha.

O único `dotnet tool restore` permitido é `dotnet tool restore --configfile <run-dir>/NuGet.Config` no ambiente acima, com `<packageSources><clear /></packageSources>` e sem URL. Ele somente pode usar o pacote já presente em `NUGET_PACKAGES`; qualquer tentativa/necessidade de download ou rede falha o gate. A restauração cria o resolver cache sob o `DOTNET_CLI_HOME` final; não se reutiliza o cache de outro HOME. A prova de launcher não é `tool list` nem inspeção de diretório: depois da restauração offline, no cwd efetivo `ScanPlantAPI/ScanPlantAPI`, executar `$DOTNET tool run dotnet-stryker -- --help`, registrar stdout/stderr, PID/lifecycle e exit code `0`, e exigir o banner `Version: 4.16.0`. O comando não recebe `--project`, `--config-file`, `--mutate` ou `--output`; portanto não analisa projeto nem inicia mutação. O precedente v3 registra esta forma canônica de `dotnet tool run ... -- --help`; a documentação .NET confirma a forma longa para tools locais.

### Tarefa 1 — Preflights não consumidores comprovam o launcher e o harness finais

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-004, A-003, P-004, P-005, U-004, S-002, SD-002

**Test seams:** local-tool resolver, ambiente .NET sanitizado, MutationHarness net8.0

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2.md#p03-r2-launcher-resolution-gate, docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md#contrato-pos-entrega

**Files:** Permitidos somente `artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/`, `artifacts/bianchini/v2/ledgers/P01.md` e `docs/living/PROJECT_STATE.md`, depois de cada gate produzir resultado factual. Proibidos `ScanPlantAPI/`, `ScanPlant-Final/`, `.config/dotnet-tools.json`, componentes do método, filtros, thresholds e qualquer evidence P03-R1.

**Contract:** Antes de campanha, registrar `revision == expected_revision == HEAD` do worktree aprovado, branch/upstream sem divergência e árvore limpa; `dotnet --list-sdks` deve conter somente o SDK esperado na raiz declarada para a seleção, e `dotnet --list-runtimes` deve conter `Microsoft.NETCore.App 8.0.30`. Confirmar manifest local com `dotnet-stryker` `4.16.0`, restaurar o tool apenas offline no `DOTNET_CLI_HOME` final, e exigir simultaneamente (a) resolver shim/cache localizado sob esse CLI home apontando ao pacote `4.16.0`, (b) transcript de `$DOTNET tool run dotnet-stryker -- --help` com banner `Version: 4.16.0`, PID/lifecycle observável e exit code `0`, e (c) nenhum diretório de resultado, relatório ou contador de mutação. Em seguida executar o MutationHarness existente com `$DOTNET test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore`, exigindo artefatos restaurados/construídos, lifecycle observável, exit `0` e `23/23` aprovados. Se esses artefatos não existirem, o restore offline e build Debug/net8.0 do harness são permitidos uma única vez antes do teste; download/rede ou qualquer mudança bloqueia. Ambos os preflights são não consumidores e registram `campaign_count=0`.

**Verification:** `python3 /home/arthur/.agents/skills/_shared/scripts/bm.py policy --profile standard --risk high --change infrastructure --manual-pdf scope --round 1 --risk-seam external-fallback --seam-round 3`; preflight sanitizado descrito no contrato; `git diff --check`.

**Done when:** evidence contém o manifesto do ambiente, digest do manifesto/local-tool manifest, versões SDK/runtime/tool, transcript e exit code do launcher real, prova de ausência de mutação, preflight do harness `23/23`, revision binding e `campaign_count=0`. Qualquer falha mantém P01 blocked-terminal e impede a Tarefa 2.

### Tarefa 2 — Uma campanha seletiva autorizada produz evidence verificável

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-004, A-003, P-003, P-004, P-005, U-004, SD-002

**Test seams:** external-fallback, mutation-observability

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2.md#p03-r2-campanha-condicional, docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md#contrato-pos-entrega

**Files:** Permitidos somente `artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/`, `artifacts/bianchini/v2/ledgers/P01.md` e `docs/living/PROJECT_STATE.md`, após autorização humana U-004 e verificadores passarem. Proibidos produção, testes, MutationHarness, dependências, `.config/dotnet-tools.json`, filtros, thresholds, METHOD_CONTRACT, bm.py, bm_mutation.py e evidências históricas.

**Contract:** Somente após Tarefa 1 passada e U-004 documentada, executar exatamente uma campanha (`campaign_count` muda de `0` para `1`) no mesmo ambiente manifestado e cwd `ScanPlantAPI/ScanPlantAPI`: `$DOTNET tool run dotnet-stryker -- --config-file <run-dir>/stryker-config.json --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --reporter json --reporter cleartext --reporter progress --verbosity trace --log-to-file --skip-version-check --output <run-dir>/results`. O config temporário tem somente `stryker-config.mutate` com os caminhos relativos ao projeto efetivo `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`; o comando não usa provider, banco, credencial, crédito ou rede de aplicação. Após relatório bruto e classificações legítimas, executar `bm.py mutation-evidence verify` com `--revision "$HEAD"`; como `release.candidate` continua nulo, o verificador instalado deriva `expected_revision` do HEAD atual. Logo a evidence precisa registrar `revision == expected_revision == HEAD` limpo, aprovado e sincronizado no instante de execução, não o HEAD de elaboração deste plano.

**Verification:** campanha única acima; `python3 /home/arthur/.agents/skills/_shared/scripts/bm.py mutation-evidence verify --state docs/living/PROJECT_STATE.md --root . --plan P03 --risk-seam external-fallback --tool stryker --command "$(tr '\n' ' ' < artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/campaign/command.txt)" --report artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/results/reports/mutation-report.json --classifications artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/mutation-classifications.json --revision "$(git rev-parse HEAD)" --output artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/mutation-evidence.json`; `git diff --check`.

**Done when:** a campanha única termina com lifecycle e exit code confiáveis; o relatório é do escopo exato; normalização/classificações são legítimas; `mutation-evidence verify` passa com o binding atual; revisão humana aprova a transição documental. Se não, P01 permanece blocked-terminal, P03-R2 fica blocked, release permanece pending e nenhuma segunda campanha é iniciada.

## Regra de parada

Antes da campanha, parar sem consumir autorização se a resolução real do launcher não for `4.16.0`, lifecycle/exit code não for confiável, o ambiente efetivo divergir do manifesto, SDK/runtime divergirem, o resolver exigir rede/download, o MutationHarness falhar, revision binding falhar ou houver necessidade de código, teste, dependência, filtro ou threshold. Depois que a campanha iniciar, registrar `campaign_count=1` e parar definitivamente em qualquer falha, relatório ausente, scope inválido, `revision-mismatch` ou mutante material não classificado; não há retry automático.
