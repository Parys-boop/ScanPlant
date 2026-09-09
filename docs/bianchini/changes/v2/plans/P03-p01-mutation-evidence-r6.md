# P03-R6 — isolamento corretivo do projeto de testes da campanha

P03-R5/U-008 é histórico terminal: `campaign_count=1`, U-008 consumida, nenhum mutante/report e nenhuma repetição permitida. R6 é uma entrega documental e operacional nova, restrita a impedir seleção automática do projeto multi-target; não altera produto, testes ou projetos versionados.

### Tarefa 1 — Preflight corretivo do contexto net8 isolado

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-013, D-014, D-015, D-016, A-007, P-014, P-015, P-016, P-017, S-006, SD-006

**Test seams:** mutation-observability, harness-project-resolution, external-fallback

**Spec refs:** `replan-v2-p03-r6.md#contexto-de-campanha-isolado`, `replan-v2-p03-r6.md#preflight-corretivo-e-executor`

**Files:** somente launcher, configuração, solução temporária e evidence no novo run-dir R6; nenhum arquivo versionado de produto/projeto/configuração.

**Contract:** Depois de aprovação e commit documental final R6, no WSL normal, partir de `campaign_count=1`. Reutilizar como pré-condições verificáveis o SDK 8.0.424, Stryker 4.16.0, pacote/feed offline de 79 pacotes e preflight R5 aprovado, sem repetir aquisição, inventário, integrity resolution, tool restore ou launcher `--help`. Gerar solução temporária com apenas API e MutationHarness; exigir paths exatos, `net8.0`, ausência de solução versionada, projeto multi-target e `net10.0`; configurar `--test-project` explícito. Validar binding ao commit documental final, launcher/config por SHA-256 e sintaxe; construir somente o contexto temporário com `--no-restore`; executar o harness canônico `--framework net8.0 --no-build --no-restore` e exigir 23/23. Qualquer falha encerra antes de U-009 e preserva contador 1.

**Verification:** no WSL normal, transcript evidencia membros da solução temporária, zero ocorrências de `ScanPlantAPI.Tests.csproj`/`net10.0`, SHA-256 e sintaxe do launcher/config, build exit 0 e MutationHarness `Passed: 23`, `Failed: 0`, `Total: 23`; `git diff --check` antes/depois prova nenhuma escrita versionada.

**Done when:** novo run-dir R6 autocontido contém binding ao commit documental final, ambiente isolado reutilizado, solução/config/launcher auditados, build net8 do contexto e harness 23/23; campaign_count continua 1 e U-009 não foi consumida.

### Tarefa 2 — Campanha única U-009 no grafo isolado

**Execution:** strict

**Review:** per_task

**Change:** infrastructure

**Readiness refs:** D-013, D-014, D-015, D-016, A-007, P-014, P-015, P-016, U-009, SD-006

**Test seams:** mutation-observability, external-fallback

**Spec refs:** `replan-v2-p03-r6.md#contexto-de-campanha-isolado`, `replan-v2-p03-r6.md#u-009-binding-e-parada`

**Files:** evidence nova no run-dir R6 e destinos canônicos de evidence após verificação; nunca produção, testes, projetos, TargetFrameworks, manifest ou cache global.

**Contract:** Somente após Tarefa 1 passar e U-009 humana explícita, repetir binding ao commit documental final, branch, upstream, limpeza e 0/0. O launcher verifica que não existe marcador R6 prévio, transita atomicamente `campaign_count=1 -> 2` uma única vez e executa Stryker 4.16.0 no WSL normal com a solução temporária, API net8, MutationHarness explícito, concurrency 1, reporters/thresholds existentes e somente os dois targets. Não usa SDK 10, solução versionada ou projeto multi-target. Depois, produzir report/classificações/verifier somente se seus inputs reais existirem. Falha após transição preserva 2 e não inicia retry.

**Verification:** evidence registra autorização U-009, command line integral, seleção explícita do harness, solução de dois membros, `TestProjects` não vazio, configuração/targets, transição única 1->2, lifecycle, report/classificações reais e `mutation-evidence verify`; `git diff --check`.

**Done when:** uma única campanha U-009 gera evidence verificável do grafo isolado no commit final. Qualquer falha pós-início é terminal com `campaign_count=2`.
