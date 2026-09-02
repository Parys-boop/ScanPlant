# P03-R4 — evidence seletiva P01 com recursos externos portáveis

**Mecanismo formal:** revisão versionada mínima após `material_change` por impossibilidade externa do contrato rígido P03-R3. P03-R3, P03-R2, P03-R1, P01, P02 e toda evidence histórica são imutáveis. Esta revisão não contém patch de produto nem consome campanha.

## Contrato de execução e limites

No linked worktree canônico isolado, obter `host_home` antes de sanitizar `HOME`; validar que é natural, absoluto, existente, legível, diretório e não symlink. Derivar `resolved_toolchain_root=$host_home/.dotnet-scanplant-8`, `DOTNET_ROOT=$resolved_toolchain_root`, `DOTNET_HOST_PATH=$resolved_toolchain_root/dotnet` e `NUGET_PACKAGES=$host_home/.nuget/packages`. Validar localmente SDK `8.0.424`, runtimes `Microsoft.NETCore.App` e `Microsoft.AspNetCore.App` `8.0.30`, manifest/tool package/executável `dotnet-stryker 4.16.0` e paths legíveis/executáveis; ausência, rede, download, instalação, symlink, cópia ou fallback de dotnet para antes de toda execução.

Depois, congelar um único manifesto e run-dir: `DOTNET_MULTILEVEL_LOOKUP=0`, `DOTNET_CLI_HOME=<run-dir>/cli-home`, `HOME=<run-dir>/home`, `TMPDIR=<run-dir>/tmp`, `LANG=C`, `LC_ALL=C`, `PATH=$resolved_toolchain_root:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin` e cwd P03 existente. O `host_home` só prova proveniência/resolução; não é o HOME sanitizado. Restore, launcher, MutationHarness e eventual campanha comparam a igualdade exata de cada valor resolvido/congelado, versões, PATH, CLI home, HOME sanitizado, TMPDIR, locale, cwd e run-dir. Produção, testes, MutationHarness, dependências, manifest, targets, filtros, thresholds, reporters, concurrency e evidence histórica são proibidos de mudar.

### Tarefa 1 — Preflights não consumidores sob contrato portátil congelado

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-006, D-007, D-008, A-005, P-008, P-009, P-010, U-006, S-004, SD-004

**Test seams:** host-home resolver, ambiente .NET sanitizado, local-tool resolver, MutationHarness net8.0

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md#resolução-portátil-antes-da-sanitização, docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md#ambiente-sanitizado-e-igualdade-material-congelada, docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md#preflights-campanha-e-segurança

**Files:** Somente novo evidence sob `artifacts/bianchini/v2/evidence/P03-p01-mutation-r4/`, ledger P01 e estado, após resultado factual. Nunca arquivos de produto/configuração/harness/dependência nem evidence histórica.

**Contract:** Após aprovação P03-R4, e antes de restore, registrar `campaign_count=0`, host_home e os três paths resolvidos. Provar localmente as versões e que nenhum download é necessário. No ambiente final congelado, executar somente o restore offline permitido, o launcher composto existente sem argumentos mutacionais e a prova de não mutação; depois o MutationHarness existente `net8.0 --no-build --no-restore` exige `23/23`. Registrar manifesto por fase e igualdade material. Nenhuma destas etapas muda o contador. Falha, path ausente, versão divergente, rede/download, fallback, symlink/cópia, diferença de manifesto, launcher/harness inválido ou binding inválido para antes da campanha.

**Verification:** `python3 <bm.py> policy --profile standard --risk high --change infrastructure --manual-pdf scope --round 1 --risk-seam external-fallback --seam-round 3` (registrar breaker sem contorná-lo); preflights contratados somente após aprovação humana; `git diff --check`.

**Done when:** evidence nova contém host_home, paths derivados, provas locais sem download, manifesto congelado, igualdade por fase, prova composta existente, ausência de mutação, harness `23/23`, revision binding aplicável e `campaign_count=0`. Sem aprovação humana, a tarefa não inicia.

### Tarefa 2 — Uma campanha seletiva explicitamente autorizada mantém contrato congelado

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-006, D-007, D-008, A-005, P-009, P-010, U-006, SD-004

**Test seams:** external-fallback, mutation-observability

**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md#preflights-campanha-e-segurança, docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md#binding-workspace-e-policy

**Files:** Somente evidence P03-R4, ledger P01 e estado após Tarefa 1/U-006. Nenhum arquivo de produto, teste, harness, dependência, manifest, target, filtro ou threshold.

**Contract:** Depois de Tarefa 1 e de autorização humana U-006 separada, verificar novamente `revision == expected_revision == HEAD` executável aprovado, commitado, sincronizado, limpo e `0/0`; reutilizar o manifesto final idêntico. Iniciar uma única campanha com Stryker `4.16.0`, `net8.0`, concurrency `1`, reporters/thresholds existentes e exclusivamente `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`; somente no início `campaign_count` muda `0 -> 1`. Executar o verifier existente apenas após campanha, nunca nesta rodada de planejamento.

**Verification:** campanha única e `mutation-evidence verify` definidos pelo contrato já aprovado, somente após U-006; `git diff --check`.

**Done when:** uma única campanha autorizada gera evidence verificável do escopo exato e do HEAD executável. Falha após início mantém `campaign_count=1`, P01 blocked-terminal, release pending e não inicia retry.

## Regra de parada

P03-R4 não autoriza preflight sem aprovação e nunca autoriza campanha por si. Antes de campanha, qualquer ausência/diferença de path ou versão, presença de workaround/rede/download, divergência ambiental, falha do launcher/harness, falta de `23/23`, binding ou autorização mantém `campaign_count=0`. O policy do seam histórico registra breaker no round acumulado 3; ele não é apagado por esta revisão e proíbe qualquer patch novo sem o redesenho canônico aplicável. Depois de iniciar a campanha, qualquer falha é terminal com `campaign_count=1`.
