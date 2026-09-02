# Escopo aprovado — P03-R5: contrato do MutationHarness

## Decisão e classificação

O blocker factual `B-P03-R4-MUTATIONHARNESS-CWD-ARTIFACTS` é um `material_change` invalidante: `bm.py change-policy --public-contract-change --plan-command --file-location --critical-invariant` retornou `invalidate_package_and_replan_affected_scope`, `plan_invalidating: true` e `reapproval_required: true`.

P03-R5 é o replanejamento mínimo do contrato operacional. P03-R1, P03-R2, P03-R3 e P03-R4, inclusive o blocker e sua evidence, permanecem históricos e imutáveis. A mudança não abre ciclo global, não muda `planning_version: v2` e não aplica patch de produto, teste ou harness.

## Resultado autorizado para planejar

Definir uma nova execução futura, autocontida e não consumidora, que:

1. fixa separadamente o cwd do launcher e o cwd do MutationHarness;
2. materializa explicitamente, sem rede, os assets e outputs `net8.0` requeridos pelo harness;
3. só então executa o gate final `dotnet test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore` no cwd real do harness;
4. exige `23/23`, evidência por fase, igualdade ambiental comum e `campaign_count=0`.

## Limites imutáveis

Não alterar código de produto, fonte do MutationHarness, testes, projetos, dependências, `.config/dotnet-tools.json`, SDK, runtimes, Stryker, targets, concurrency, reporters, thresholds, seam, campanha ou contadores. Não autorizar campanha. Não executar nesta rodada comandos .NET, restore, build, test, launcher, Stryker ou MutationHarness.

O ambiente futuro preserva resolução portátil R4: `host_home` capturado antes de sanitizar, `resolved_toolchain_root=$host_home/.dotnet-scanplant-8`, SDK `8.0.424`, runtimes `Microsoft.NETCore.App 8.0.30` e `Microsoft.AspNetCore.App 8.0.30`, Stryker `4.16.0`, `NUGET_PACKAGES=$host_home/.nuget/packages`, sem download, rede, instalação, symlink, cópia ou fallback.
