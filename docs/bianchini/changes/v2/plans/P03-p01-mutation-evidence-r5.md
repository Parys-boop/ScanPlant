# P03-R5 — contrato de preparation e gate do MutationHarness

**Mecanismo formal:** replanejamento mínimo após `material_change` invalidante de R4. O breaker acumulado do seam `mutation-observability` permanece no round 3; R5 é desenho documental de contrato e não autoriza patch de produto/harness ou campanha.

## Limites de execução

Um executor futuro usa novo run-dir R5 e repete host validation, restore offline de tool e launcher não mutacional, todos sob o ambiente portátil R4 preservado. A execução nunca altera produção, testes, MutationHarness, `.csproj`, dependências, manifest, SDK/runtime/tool, targets, concurrency, reporters ou thresholds. Sem U-007, nada executa; campanha continua fora deste plano.

### Tarefa 1 — Prepara e verifica o MutationHarness sem consumir campanha

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-009, D-010, D-011, D-012, A-006, P-011, P-012, P-013, U-007, U-008, S-005, SD-005

**Test seams:** harness-project-resolution, offline-artifact-preparation, external-fallback

**Spec refs:** `replan-v2-p03-r5.md#ambiente-portátil-comum-e-cwd-congelado-por-fase`, `replan-v2-p03-r5.md#preparation-e-gate-final-do-mutationharness`, `replan-v2-p03-r5.md#evidence-repetição-e-campanha`

**Files:** somente evidence nova em `artifacts/bianchini/v2/evidence/P03-p01-mutation-r5/`, ledger P01 e estado factual após execução. Nunca source/configuração de produto, harness, projeto ou dependência.

**Contract:** depois de U-007, registrar `campaign_count=0`, frozen common environment e cwd por fase. Repetir em run-dir novo os preflights não consumidores R4. No cwd `<repo>/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness`, criar `NuGet.Config` de run-dir com fontes limpas; executar `$DOTNET_HOST_PATH restore ScanPlantAPI.MutationHarness.csproj --configfile <run-dir>/NuGet.Config --ignore-failed-sources`; depois `$DOTNET_HOST_PATH build ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-restore`. Registrar no-network proof, lifecycle, exit, assets e outputs. Só se ambos passarem, executar `$DOTNET_HOST_PATH test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore` nesse cwd e exigir `23/23`. Qualquer falha, drift, rede/download, asset ausente ou resultado diferente para antes da campanha.

**Verification:** `python3 <bm.py> policy --profile standard --risk high --change infrastructure --risk-seam mutation-observability --seam-round 3`; checksums da evidence; igualdade ambiental por fase; final `23/23`; `git diff --check`.

**Done when:** R5 evidence autocontida mostra common environment congelado, cwds declarados, repetição dos preflights, restore/build offline separados, artifacts net8.0, final no-build/no-restore `23/23`, binding aplicável e `campaign_count=0`. Nenhuma campanha é iniciada.

## Regra de parada

R5 não autoriza campanha. Mesmo com Tarefa 1 aprovada, a campanha exige U-008 posterior vinculada ao HEAD executável. `revision == expected_revision == HEAD` só é avaliado para a futura autorização; não se vincula ao HEAD de elaboração. Falha de preparation ou harness mantém P01 blocked-terminal, P03-R5 blocked e release pending.
