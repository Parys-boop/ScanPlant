# Review Package

- Base: `822954421019ad611d4d14dc5461cc7a495b7db4`
- Head: `a2dfd8805527e6323334fcc0a7b7f45c63c7d3c9`
- Brief: `artifacts/bianchini/v2/codex/P07/task-brief.md` (a479d6e9bc2e60b9031690ef5994b9f3a3e1c95e86f1fc508f55bb72bf358e11)
- Report: `artifacts/bianchini/v2/codex/P07/commit-review-report.md` (1ae9c6f9e52b35080dc3b9ed4952a0080534028c525b9934494ec0124d5a58dc)
- Security notice: sanitização heurística; 1 ocorrência(s) removida(s). Revise antes de compartilhar.

## Commits

```text
a2dfd88 feat(p07): add traceable dataset curation
```

## Stat

```text
.../v2/codex/P07/acceptance-manifest.json          |  38 ++
 artifacts/bianchini/v2/codex/P07/checkpoint.json   |  94 ++++
 artifacts/bianchini/v2/codex/P07/final-audit.json  |  31 ++
 .../bianchini/v2/codex/P07/implementer-report.md   |  25 +
 artifacts/bianchini/v2/codex/P07/review-package.md |  39 ++
 artifacts/bianchini/v2/codex/P07/task-brief.md     |  30 ++
 artifacts/bianchini/v2/codex/P07/verification.json | 207 ++++++++
 .../bianchini/v2/codex/P07/verify_working_tree.py  | 124 +++++
 artifacts/bianchini/v2/ledgers/P07.md              |  28 ++
 artifacts/phase1/p07/summary.json                  | 273 +++++++++++
 docs/living/PROJECT_STATE.md                       |  21 +-
 docs/phase1/P07-curation.md                        |  45 ++
 scripts/phase1/curate_p07.py                       | 534 +++++++++++++++++++++
 scripts/phase1/test_curate_p07.py                  | 476 ++++++++++++++++++
 14 files changed, 1957 insertions(+), 8 deletions(-)
```

## Diff

```diff
diff --git a/artifacts/bianchini/v2/codex/P07/acceptance-manifest.json b/artifacts/bianchini/v2/codex/P07/acceptance-manifest.json
new file mode 100644
index 0000000..7f749b1
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/acceptance-manifest.json
@@ -0,0 +1,38 @@
+{
+  "acceptance": "pending",
+  "base_revision": "822954421019ad611d4d14dc5461cc7a495b7db4",
+  "branch": "bm/v2-p07",
+  "external_files": {
+    "analysis.json": "6f857cb52ad60fc596834698dd77ffb10d830d5cf907d10479b12ed76ee56338",
+    "curation.draft.json": "7b27bb37bf62b5a100407948154cec0a3a2c88214396c134a91872180559bc0c",
+    "human-decisions.json": "0d81616cd8ab79e2d8614a93b15ff7fdcc5f3e7f6f6adfa8c681afb3d697e195",
+    "report.draft.md": "6e054680bbbbb17bf01e720aaec6e48024655cbbef73bada11abac9724a4ef6d",
+    "source-before.json": "eda50f599cd7e1bba996ae8e25760073903b122ff181ef38cb401804278b125c",
+    "summary.draft.json": "97c73477c4f5d6eabce2fd3f4333fb7c92725466bf7e1b41c31140a825c57353",
+    "verification.json": "a6d549a770474f889662c5c54d1fd8a86816115dbfba294102bca8cd4247363f"
+  },
+  "external_root": "/home/administradorarthur/datasets/scanplant/p07-curation-20260928",
+  "files": {
+    "artifacts/bianchini/v2/codex/P07/checkpoint.json": "65b498f383c884b7e176013e288ac88b2d8aa8584c8d85f4c9a2f24c1928e0c6",
+    "artifacts/bianchini/v2/codex/P07/final-audit.json": "32b50e69c82e1b7d1c7e620b2749c836c42ea825ef76d34500ce03f33e65dc39",
+    "artifacts/bianchini/v2/codex/P07/implementer-report.md": "46e6bfd097ecd0f49ed744e1e2c4eb19b04254aa86d9740ffabcf336528c35ee",
+    "artifacts/bianchini/v2/codex/P07/review-package.md": "35b10e87b3934787a6dcbf93919cb33dd46711d2c5c31a75973e449a3bd4d423",
+    "artifacts/bianchini/v2/codex/P07/task-brief.md": "a479d6e9bc2e60b9031690ef5994b9f3a3e1c95e86f1fc508f55bb72bf358e11",
+    "artifacts/bianchini/v2/codex/P07/verification.json": "c4345937da7ef013099d2717a90f2329efcae01822015a5f3a055dfe3d37b6e0",
+    "artifacts/bianchini/v2/codex/P07/verify_working_tree.py": "22a4502ecf7c65f15110ced8d91466ab77ba30cb2a7b5d99d27d51ed1532367f",
+    "artifacts/bianchini/v2/ledgers/P07.md": "8ee3f71284d1183f4e1cfd8e75f94f5dda455e5eb425f12b6229812b63b1f0a3",
+    "artifacts/phase1/p07/summary.json": "97c73477c4f5d6eabce2fd3f4333fb7c92725466bf7e1b41c31140a825c57353",
+    "docs/living/PROJECT_STATE.md": "086188cb1936ce52d8b2656efeb2849e0a7728c365153f4de31ca2bf77ea768a",
+    "docs/phase1/P07-curation.md": "cf885806aab637889b0b81a5076815b5d8ae13858b30e058e2f704d27d88d137",
+    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
+    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5"
+  },
+  "guard_commit_review": "not_run",
+  "kind": "p07_final_working_bytes_pending_human_acceptance",
+  "planning_digest": "2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3",
+  "schema_version": 1,
+  "self_digest_rule": "SHA-256 of this manifest binds all listed Git working files and external files; manifest excluded from its own file map.",
+  "training_authorized": false,
+  "usable": 0,
+  "workspace": "/tmp/scanplant-p07-workspace"
+}
diff --git a/artifacts/bianchini/v2/codex/P07/checkpoint.json b/artifacts/bianchini/v2/codex/P07/checkpoint.json
new file mode 100644
index 0000000..a4bb015
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/checkpoint.json
@@ -0,0 +1,94 @@
+{
+  "method_version": 2,
+  "planning_status": "approved",
+  "approval": "approved",
+  "plans": [
+    {
+      "id": "P01",
+      "status": "blocked",
+      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
+    },
+    {
+      "id": "P02",
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P02.md"
+    },
+    {
+      "id": "P03",
+      "status": "blocked",
+      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
+    },
+    {
+      "id": "P04",
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P04.md"
+    },
+    {
+      "id": "P05",
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
+    },
+    {
+      "id": "P05-R1",
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
+    },
+    {
+      "id": "P07",
+      "status": "in_progress",
+      "ledger": "artifacts/bianchini/v2/ledgers/P07.md"
+    }
+  ],
+  "release": {
+    "status": "pending",
+    "platforms": [
+      "ASP.NET Core .NET 8",
+      "Android Expo/React Native"
+    ],
+    "profiles": [
+      "Release"
+    ],
+    "candidate": null,
+    "final_gate": "homologar-sistema",
+    "homologation": "pending",
+    "final_review": "pending",
+    "delivery": "pending"
+  },
+  "next_action": "Decisão humana única sobre os 17 pareceres P07 e os bytes finais na worktree existente; U-701/U-702 pendentes. Nenhuma aprovação para dataset ou treinamento; release pending. Staging/commit/push não autorizados nesta rodada.",
+  "workspace": "/tmp/scanplant-p07-workspace",
+  "git": {
+    "branch": "bm/v2-p07",
+    "head": "822954421019ad611d4d14dc5461cc7a495b7db4",
+    "dirty": true
+  },
+  "ledger_tail": [
+    "# Ledger P07 — append-only",
+    "",
+    "## Retomada da unidade 1 — 2026-09-30",
+    "",
+    "- Plano congelado: `docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md`.",
+    "- Digest aprovado: `2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3`.",
+    "- Base revision e HEAD: `822954421019ad611d4d14dc5461cc7a495b7db4`.",
+    "- Workspace existente: `/tmp/scanplant-p07-workspace`; branch `bm/v2-p07`.",
+    "- Perfil standard; garantia aprovada slice/per_slice; uma única unidade em rodada agrupada solicitada pelo responsável.",
+    "- Identidade da unidade: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`.",
+    "- Ambiente existente Python 3.14.4/Pillow 12.3.0; todos os caminhos temporários localizados; nada reiniciado.",
+    "- Fonte e resultados externos existentes reconciliados; 29 arquivos P06, 17 imagens, hashes iguais ao registro inicial.",
+    "",
+    "## Ajustes limitados e evidências",
+    "",
+    "`bm.py change-policy --plan-command --file-location` retornou `bounded_amendment`, sem reaprovação nem mutação do plano. O helper operacional de verificação fica em `artifacts/bianchini/v2/codex/P07/verify_working_tree.py`. O interpretador concreto é o ambiente existente. `--review-draft` preserva as propostas sem substituí-las por decisão humana; `--finalize` real aguarda U-701. Nenhuma unidade ou entrega foi criada.",
+    "",
+    "Dois testes de regressão na retomada falharam antes da correção: relatório recarregado de JSON alterava a ordem das contagens; rejeição de duplicata não exigia parecer explícito do par. Correções locais preservam os bytes externos já persistidos. RED: 38 testes, duas falhas. GREEN final: 38/38 P07 e 162/162 na suíte afetada. Não houve novo ciclo formal do guard.",
+    "",
+    "`verification.json` registra argv/cwd/horário/exit code/stdout/stderr e hashes do código/testes. Validador P05, estado, snapshot aprovado, auditoria estrita, checksums P05/P06, repo-hygiene, workspace e diff-check passaram. Reexecução real: bytes e mtimes iguais, 136 pares, nenhuma alteração P06. A evidência integral dos 17 hashes antes/depois está no `verification.json` externo.",
+    "",
+    "## Revisão e fronteira de autoridade",
+    "",
+    "Propostas existentes preservadas: 8 needs_botanical_review, 7 needs_human_review, 2 rejected_quality; demais estados zero. `usable=0`, treinamento não autorizado. Nenhuma confirmação botânica pericial. U-701/U-702 aguardam a decisão humana única solicitada para o fim desta rodada.",
+    "",
+    "Guard não iniciado sobre o delta não commitado. `proof` cria checkout/worktree de commit; `review-package` base..HEAD não inclui untracked. Executar esses proofs sobre HEAD alegaria evidência de código ausente; criar commit/nova worktree violaria instrução humana. Não há sidecar nem fase terminal, blockers congelados, fix rounds ou redesign formal registrados. Não chamar `freeze`, `complete` ou `stop` para simular fechamento. O pacote de revisão deixa explícita essa limitação e referencia os hashes de trabalho. Verificação local concluída; conclusão formal permanece pendente.",
+    "",
+    "O estado vivo só registra progresso da execução e aceite pendente; nenhum campo de convergência foi transplantado para PROJECT_STATE. Repositório principal permanece limpo na baseline; índices vazios. Plano canônico já reconciliado no planejamento permanece congelado. P01–P06/P05-R1, current_specs e release pending preservados."
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P07/final-audit.json b/artifacts/bianchini/v2/codex/P07/final-audit.json
new file mode 100644
index 0000000..f69a706
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/final-audit.json
@@ -0,0 +1,31 @@
+{
+  "all_checks_passed": true,
+  "diff_check_including_untracked": true,
+  "guard_formal_review": "pending_not_run",
+  "historical_tracked_files_unchanged": true,
+  "human_acceptance": "pending",
+  "index_empty": true,
+  "inspected_files": [
+    "artifacts/bianchini/v2/codex/P07/checkpoint.json",
+    "artifacts/bianchini/v2/codex/P07/implementer-report.md",
+    "artifacts/bianchini/v2/codex/P07/review-package.md",
+    "artifacts/bianchini/v2/codex/P07/task-brief.md",
+    "artifacts/bianchini/v2/codex/P07/verification.json",
+    "artifacts/bianchini/v2/codex/P07/verify_working_tree.py",
+    "artifacts/bianchini/v2/ledgers/P07.md",
+    "artifacts/phase1/p07/summary.json",
+    "docs/living/PROJECT_STATE.md",
+    "docs/phase1/P07-curation.md",
+    "scripts/phase1/curate_p07.py",
+    "scripts/phase1/test_curate_p07.py"
+  ],
+  "main_repository_clean": true,
+  "no_binary_or_image_or_environment_paths": true,
+  "p06_closure_preserved": true,
+  "prior_plan_states_preserved": true,
+  "real_private_review_strings_in_git": 0,
+  "release_pending": true,
+  "sanitized_summary_allowlist": true,
+  "scope": "working_tree_pre_acceptance",
+  "secret_pattern_findings": 0
+}
diff --git a/artifacts/bianchini/v2/codex/P07/implementer-report.md b/artifacts/bianchini/v2/codex/P07/implementer-report.md
new file mode 100644
index 0000000..bab6bf8
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/implementer-report.md
@@ -0,0 +1,25 @@
+# Implementer Report
+
+- Brief: `artifacts/bianchini/v2/codex/P07/task-brief.md`
+- Status: TECHNICAL_VERIFICATION_PASSED_HUMAN_ACCEPTANCE_PENDING
+- Base: `822954421019ad611d4d14dc5461cc7a495b7db4`
+
+## Changes
+
+Retomada dos scripts e resultados existentes; nenhum reinício. Mecanismo de análise determinística, reconciliação dos 17 IDs/SHA/classes, 136 pares, pareceres externos, barreira de decisão humana, resumo sanitizado e idempotência. Criados resumo, documentação de operação, ledger, evidências e checkpoint na mesma unidade. Preservados plano/delta/spec, imagens, P06 e todos os históricos.
+
+## Verification
+
+38 testes P07 e 162 testes afetados/históricos passaram. Verificações executáveis e resultados completos em `verification.json`. Código e testes identificados por SHA-256. Reexecução externa preservou bytes/mtimes; 29 arquivos P06 intactos. Resumo reconciliado, JSON estrito e 136 pares exatos. Validação P05, estado, snapshot, auditoria estrita, checksums, higiene, workspace e diff-check aprovados.
+
+## Decisions
+
+Modelo de autoridade explícito: propostas do agente continuam rascunhos; nenhuma decisão humana inventada. 8 pendências botânicas, 7 humanas, 2 propostas de rejeição por qualidade, zero aprovações. U-701/U-702 não consumidas. `--finalize` testado apenas em fixtures; operação real usa `--review-draft`. A CLI `bm.py report --brief ... --output ...` já havia criado este relatório; a retomada preenche o artefato existente após conferir `--help`.
+
+Ajuste limitado `bounded_amendment` registrado no ledger. Duas regressões reproduzidas e corrigidas: ordem do relatório recarregado e exigência de parecer do par para rejeitar duplicata. Nenhuma proposta externa reescrita. Garantia slice/per_slice preservada na rodada agrupada solicitada.
+
+## Concerns
+
+Aceite humano dos 17 pareceres e bytes pendente. Espécies não confirmadas pericialmente; possíveis redundâncias manuais e privacidade continuam pendentes no externo. Todas as classes sem candidato aprovado; quatro sem candidato adquirido.
+
+Guard formal indisponível nesta rodada: código não commitado; `proof` exige checkout de commit e cria outra worktree, ações proibidas. Nenhum proof_id, sidecar ou conclusão formal foi inventado. O pacote CLI de revisão mostra somente base..HEAD (delta vazio) e é complementado por referências aos bytes de trabalho. Evidências locais não equivalem a provas do commit. Não houve staging, commit ou publicação.
diff --git a/artifacts/bianchini/v2/codex/P07/review-package.md b/artifacts/bianchini/v2/codex/P07/review-package.md
new file mode 100644
index 0000000..9fd7d1f
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/review-package.md
@@ -0,0 +1,39 @@
+# Review Package
+
+- Base: `822954421019ad611d4d14dc5461cc7a495b7db4`
+- Head: `HEAD`
+- Brief: `artifacts/bianchini/v2/codex/P07/task-brief.md` (a479d6e9bc2e60b9031690ef5994b9f3a3e1c95e86f1fc508f55bb72bf358e11)
+- Report: `artifacts/bianchini/v2/codex/P07/implementer-report.md` (46e6bfd097ecd0f49ed744e1e2c4eb19b04254aa86d9740ffabcf336528c35ee)
+- Security notice: sanitização heurística; 0 ocorrência(s) removida(s). Revise antes de compartilhar.
+
+## Commits
+
+```text
+
+```
+
+## Stat
+
+```text
+
+```
+
+## Diff
+
+```diff
+
+```
+
+## Escopo efetivamente revisado nesta rodada
+
+O diff base..HEAD acima está vazio porque staging e commit estão proibidos. Ele não representa os arquivos de trabalho P07. Não foi usado para aprovar o guard. Revisão técnica local dos arquivos abaixo e dos testes/evidências; aceite humano pendente.
+
+- `scripts/phase1/curate_p07.py` — SHA-256 `8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307`
+- `scripts/phase1/test_curate_p07.py` — SHA-256 `421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5`
+- `artifacts/phase1/p07/summary.json` — SHA-256 `97c73477c4f5d6eabce2fd3f4333fb7c92725466bf7e1b41c31140a825c57353`
+- `docs/phase1/P07-curation.md` — SHA-256 `cf885806aab637889b0b81a5076815b5d8ae13858b30e058e2f704d27d88d137`
+- `docs/living/PROJECT_STATE.md` — SHA-256 `086188cb1936ce52d8b2656efeb2849e0a7728c365153f4de31ca2bf77ea768a`
+
+Revisão local: identidade/reconciliação, 136 pares, fórmulas e fronteiras, autoridade humana, duplicatas, projeção sanitizada, preservação da origem, lock/persistência e reexecução. Dois defeitos concretos corrigidos com testes RED/GREEN antes desta avaliação final. Nenhum defeito material conhecido permanece nos bytes atuais. Essa avaliação não é o verdict formal do guard nem consome U-701/U-702.
+
+`proof` exige commit e cria worktree; ambos incompatíveis com esta rodada. Sem sidecar, proof_id, blockers congelados, fix rounds ou redesign formal. Fase do guard não iniciada; não declarar completed/parked/stopped.
diff --git a/artifacts/bianchini/v2/codex/P07/task-brief.md b/artifacts/bianchini/v2/codex/P07/task-brief.md
new file mode 100644
index 0000000..7f09015
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/task-brief.md
@@ -0,0 +1,30 @@
+# Task Brief 1
+
+- Plan: `docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md`
+- Plan SHA-256: `8aee1fb59866c780b45f955b7123ed124e02274b9ac9c620068fffe61554594f`
+- Kind: `task`
+- Group ID: `n/a`
+- Group SHA-256: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`
+- Unit `1` SHA-256: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`
+
+### Tarefa 1 — 17 análises reconciliadas, pareceres humanos e relatório rastreável
+
+**Execution:** slice
+
+**Review:** per_slice
+
+**Change:** workflow
+
+**Readiness refs:** D-701, D-702, D-703, D-704, A-701, A-702, P-701, P-702, P-703, U-701, U-702, U-703, S-701, SD-701
+
+**Test seams:** `curate_p07` CLI de leitura/análise/finalização; parser estrito de `state.json`/manifesto/decisões; reconciliação Q/R/SHA/class_id; métricas de luminância/nitidez; dHash/Hamming 136 pares; transição análise→parecer→estado; projeção sanitizada e reexecução idempotente.
+
+**Spec refs:** `docs/bianchini/changes/v2/specs/p07-curation-change.md#entradas-identidade-e-integridade`, `#análise-técnica-determinística`, `#estados-e-autoridade`, `#saídas-concorrência-e-idempotência`, `#gate-e-aceite`; `docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md#análise-e-duplicidade`, `#revisão-estados-e-prova`, `#persistência-e-visibilidade`. D-702, D-703, SD-701.
+
+**Files:** criar futuramente `scripts/phase1/curate_p07.py`, `scripts/phase1/test_curate_p07.py`, `artifacts/phase1/p07/summary.json`, `docs/phase1/P07-curation.md`, `artifacts/bianchini/v2/ledgers/P07.md` (append-only após criação). Atualizar minimamente `docs/living/PROJECT_STATE.md` no gate, mantendo todos os estados anteriores, e a cronologia de `docs/PLANO_CANONICO_IA_HIBRIDA.md` já incluída no pacote de planejamento. Resultados integrais futuros ficam **fora do Git** em diretório novo separado do P06: `analysis.json`, `human-decisions.json`, `curation.json`, `report.md`. Não alterar `scripts/phase1/acquire_commons.py`, manifesto P05, P06, planos/ledgers/evidências antigos, imagens, `current_specs` ou aplicações. D-704, P-701, P-703.
+
+**Contract:** com acesso U-703, verificar fontes externas em leitura, conjunto exato de 17 aceitos e decisões Q01–Q17/R01–R17, SHA-256 e versões. Falha bloqueia sem saída final nem substituição. Gerar análise determinística para todos: decodificação, dimensões, razão, luminância/exposição, variância Laplaciana e flags nos limiares congelados; comparar 136 pares por SHA/dHash 64/Hamming. Testes sintéticos fixam cálculo e fronteiras; flags apenas sinalizam. Revisar em resolução original os critérios humanos de enquadramento, oclusão, múltiplas espécies, representatividade, privacidade e rótulo botânico. U-701 produz 17 pareceres, inclusive pendências legítimas, com responsável/timestamp/justificativa/evidência. Finalizar somente após validar que nenhum `approved_for_dataset` veio de algoritmo ou de decisão P06, que toda rejeição humana tem motivo e que todos os pares sinalizados foram resolvidos ou explicitamente mantidos pendentes. Preservar bytes P06 e atribuição/licença/origem; saída externa atômica e idempotente. Resumo Git usa allowlist de campos sem PII; relatório expõe zero aprovação e classes vazias como resultados válidos, nunca suficiência de treino. U-702 aceita hashes finais antes de commit/push. P-701, P-702, P-703, A-701, A-702.
+
+**Verification:** no cwd raiz do workspace aprovado, com Python do ambiente isolado Pillow 12.3.0 disponível na execução: `python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'` e `python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'`, exit 0; `python -B scripts/phase1/curate_p07.py --source /home/administradorarthur/datasets/scanplant/p06-recovery-20260928 --output /home/administradorarthur/datasets/scanplant/p07-curation-20260928 --analyze-only`, exit 0 após U-703; depois de U-701, mesma CLI com `--finalize --decisions /home/administradorarthur/datasets/scanplant/p07-curation-20260928/human-decisions.json`, exit 0 e reexecução byte-idêntica. Validar `python -B -m json.tool artifacts/phase1/p07/summary.json`, `python3 -B /home/administradorarthur/.agents/skills/_shared/scripts/bm.py validate-state docs/living/PROJECT_STATE.md`, `python3 -B /home/administradorarthur/.agents/skills/_shared/scripts/bm.py snapshot verify docs/living/PROJECT_STATE.md --root .`, `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS`, `git diff --check` e inspeção dos arquivos Git alterados contra segredos/PII/binários. `SHA256SUMS` externo P06 e os 17 hashes são conferidos antes/depois; comparar os bytes dos manifestos/snapshots históricos ao HEAD, sem exigir que um manifesto antigo recalcule arquivos vivos intencionalmente atualizados. Nenhum comando de produto, mutação, release ou rede de aquisição.
+
+**Done when:** 17/17 fontes reconciliadas e byte-iguais antes/depois; 17/17 análises e pareceres humanos vinculados, 136 pares calculados, JSON estrito, relatório externo e resumo Git coerentes, estados válidos com justificativas, nenhum dado pessoal/imagem no Git, reexecução idempotente, testes/gates aprovados e U-702 registra aceite explícito dos bytes finais. Zero `approved_for_dataset`, pendências botânicas e classes vazias são permitidos. Ausência de U-701/U-702 ou integridade divergente mantém P07 não concluído; nenhuma promoção, commit, push ou reabertura histórica é inferida.
diff --git a/artifacts/bianchini/v2/codex/P07/verification.json b/artifacts/bianchini/v2/codex/P07/verification.json
new file mode 100644
index 0000000..3f7f1a3
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/verification.json
@@ -0,0 +1,207 @@
+{
+  "base_revision": "822954421019ad611d4d14dc5461cc7a495b7db4",
+  "commands": [
+    {
+      "argv": [
+        "/tmp/scanplant-p07-env/bin/python",
+        "-B",
+        "-m",
+        "unittest",
+        "discover",
+        "-s",
+        "scripts/phase1",
+        "-p",
+        "test_curate_p07.py"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "p07_tests",
+      "started_at": "2026-09-30T21:27:10.714321+00:00",
+      "stderr": "......................................\n----------------------------------------------------------------------\nRan 38 tests in 2.451s\n\nOK\n",
+      "stdout": ""
+    },
+    {
+      "argv": [
+        "/tmp/scanplant-p07-env/bin/python",
+        "-B",
+        "-m",
+        "unittest",
+        "discover",
+        "-s",
+        "scripts/phase1",
+        "-p",
+        "test_*.py"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "affected_and_historical_tests",
+      "started_at": "2026-09-30T21:27:13.278030+00:00",
+      "stderr": "..................................................................................................................................................................\n----------------------------------------------------------------------\nRan 162 tests in 3.695s\n\nOK\n",
+      "stdout": ""
+    },
+    {
+      "argv": [
+        "/tmp/scanplant-p07-env/bin/python",
+        "-B",
+        "scripts/phase1/validate_offline_manifest.py",
+        "--manifest",
+        "docs/phase1/offline-class-manifest.v1.json",
+        "--roster",
+        "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "class_manifest",
+      "started_at": "2026-09-30T21:27:17.151909+00:00",
+      "stderr": "",
+      "stdout": "{\"aliases\": 79, \"classes\": 14, \"manifest_sha256\": \"bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c\", \"manifest_version\": \"1.1.0\", \"normalization_version\": \"1\", \"protection\": 2, \"roster_sha256\": \"350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b\", \"schema_version\": 1, \"scientific_keys\": 91, \"species\": 12, \"valid\": true}\n"
+    },
+    {
+      "argv": [
+        "/tmp/scanplant-p07-env/bin/python",
+        "-B",
+        "-m",
+        "json.tool",
+        "artifacts/phase1/p07/summary.json"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "summary_json",
+      "started_at": "2026-09-30T21:27:17.200706+00:00",
+      "stderr": "",
+      "stdout": "{\n    \"classes_without_approved\": [\n        \"species_01\",\n        \"species_02\",\n        \"species_03\",\n        \"species_04\",\n        \"species_05\",\n        \"species_06\",\n        \"species_07\",\n        \"species_08\",\n        \"species_09\",\n        \"species_10\",\n        \"species_11\",\n        \"species_12\",\n        \"outra_planta\",\n        \"imagem_invalida\"\n    ],\n    \"classes_without_candidates\": [\n        \"species_04\",\n        \"species_08\",\n        \"outra_planta\",\n        \"imagem_invalida\"\n    ],\n    \"comparison_count\": 136,\n    \"counts\": {\n        \"approved_for_dataset\": 0,\n        \"needs_botanical_review\": 8,\n        \"needs_human_review\": 7,\n        \"rejected_duplicate\": 0,\n        \"rejected_label\": 0,\n        \"rejected_privacy\": 0,\n        \"rejected_quality\": 2\n    },\n    \"coverage\": [\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_01\",\n            \"name\": \"Epipremnum aureum\",\n            \"pending\": 1,\n            \"rejected\": 1\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 1,\n            \"class_id\": \"species_02\",\n            \"name\": \"Monstera deliciosa\",\n            \"pending\": 1,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_03\",\n            \"name\": \"Zamioculcas zamiifolia\",\n            \"pending\": 2,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 0,\n            \"class_id\": \"species_04\",\n            \"name\": \"Spathiphyllum wallisii\",\n            \"pending\": 0,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_05\",\n            \"name\": \"Dracaena trifasciata\",\n            \"pending\": 2,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 1,\n            \"class_id\": \"species_06\",\n            \"name\": \"Aloe vera\",\n            \"pending\": 1,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_07\",\n            \"name\": \"Chlorophytum comosum\",\n            \"pending\": 1,\n            \"rejected\": 1\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 0,\n            \"class_id\": \"species_08\",\n            \"name\": \"Codiaeum variegatum\",\n            \"pending\": 0,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_09\",\n            \"name\": \"Ficus elastica\",\n            \"pending\": 2,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 1,\n            \"class_id\": \"species_10\",\n            \"name\": \"Kalanchoe blossfeldiana\",\n            \"pending\": 1,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_11\",\n            \"name\": \"Nephrolepis exaltata\",\n            \"pending\": 2,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 2,\n            \"class_id\": \"species_12\",\n            \"name\": \"Tradescantia zebrina\",\n            \"pending\": 2,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 0,\n            \"class_id\": \"outra_planta\",\n            \"name\": \"Outra planta\",\n            \"pending\": 0,\n            \"rejected\": 0\n        },\n        {\n            \"approved\": 0,\n            \"candidates\": 0,\n            \"class_id\": \"imagem_invalida\",\n            \"name\": \"Imagem inv\\u00e1lida\",\n            \"pending\": 0,\n            \"rejected\": 0\n        }\n    ],\n    \"records\": [\n        {\n            \"class_id\": \"species_01\",\n            \"id\": \"Q01\",\n            \"review_id\": \"R01\",\n            \"sha256\": \"b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_01\",\n            \"id\": \"Q02\",\n            \"review_id\": \"R02\",\n            \"sha256\": \"cc04b39c60ff068344be25f1b6c1d1d3628afe3272edba4794b5e8fdab8188c5\",\n            \"state\": \"rejected_quality\"\n        },\n        {\n            \"class_id\": \"species_02\",\n            \"id\": \"Q03\",\n            \"review_id\": \"R03\",\n            \"sha256\": \"2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_03\",\n            \"id\": \"Q04\",\n            \"review_id\": \"R04\",\n            \"sha256\": \"7beac71d4fd1901559b36e041469666e1376dbf4b3eb761b9fec5fc8f48403bf\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_03\",\n            \"id\": \"Q05\",\n            \"review_id\": \"R05\",\n            \"sha256\": \"0fa0c0fe80f1fe1f90e2e1a8f81e6d5146a0956afe1ca00ba45c4f410b3e96b6\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_05\",\n            \"id\": \"Q06\",\n            \"review_id\": \"R06\",\n            \"sha256\": \"38fdf4d90431956bccf426e9ec4b0281d9441fd968766add985832f4f900b251\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_05\",\n            \"id\": \"Q07\",\n            \"review_id\": \"R07\",\n            \"sha256\": \"4aa046916264dc5d892121b1d9cc3dd5212bb9bb1bc50e999376d023286a9550\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_06\",\n            \"id\": \"Q08\",\n            \"review_id\": \"R08\",\n            \"sha256\": \"09d9fb06033b07a8305c2f46a6d6e292b090ca66e4a8b8668a5ea0a610c3766b\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_07\",\n            \"id\": \"Q09\",\n            \"review_id\": \"R09\",\n            \"sha256\": \"e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_07\",\n            \"id\": \"Q10\",\n            \"review_id\": \"R10\",\n            \"sha256\": \"bbccd447a0f4713cd86685b0e358733941a44a38d58447989f36bb9db42c6856\",\n            \"state\": \"rejected_quality\"\n        },\n        {\n            \"class_id\": \"species_09\",\n            \"id\": \"Q11\",\n            \"review_id\": \"R11\",\n            \"sha256\": \"0440649cc6d6f7246f9858b79b408dc7c683fd6fac3c25695281cf5219b95847\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_09\",\n            \"id\": \"Q12\",\n            \"review_id\": \"R12\",\n            \"sha256\": \"ade5fe488454b574c5048aafc80abc74a914e59e53a8ecb70e997b8c5aa21f88\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_10\",\n            \"id\": \"Q13\",\n            \"review_id\": \"R13\",\n            \"sha256\": \"a51f75db036a8fc96ec3929e514525eb2757763d6204dc8d2688f4c270a4e9e8\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_11\",\n            \"id\": \"Q14\",\n            \"review_id\": \"R14\",\n            \"sha256\": \"816faa9cc87e736ea2293c887728a9d2ecac6a46396ed675ce7716ca7623d457\",\n            \"state\": \"needs_botanical_review\"\n        },\n        {\n            \"class_id\": \"species_11\",\n            \"id\": \"Q15\",\n            \"review_id\": \"R15\",\n            \"sha256\": \"d5a93acdc94d279cf38fff53bca0a06615351aebbfb26c8a620cbdddc1ae370b\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_12\",\n            \"id\": \"Q16\",\n            \"review_id\": \"R16\",\n            \"sha256\": \"8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b\",\n            \"state\": \"needs_human_review\"\n        },\n        {\n            \"class_id\": \"species_12\",\n            \"id\": \"Q17\",\n            \"review_id\": \"R17\",\n            \"sha256\": \"91524bde4f0351530c0818612a52bbc75fa59dca2aa0709f7a8a6273376d26b2\",\n            \"state\": \"needs_botanical_review\"\n        }\n    ],\n    \"schema_version\": 1,\n    \"stage\": \"agent_proposals_pending_human\",\n    \"training_authorized\": false,\n    \"training_sufficiency\": \"not_demonstrated\"\n}\n"
+    },
+    {
+      "argv": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "validate-state",
+        "docs/living/PROJECT_STATE.md"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "state",
+      "started_at": "2026-09-30T21:27:17.239999+00:00",
+      "stderr": "",
+      "stdout": "{\n  \"method_version\": 2,\n  \"valid\": true\n}\n"
+    },
+    {
+      "argv": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "snapshot",
+        "verify",
+        "docs/living/PROJECT_STATE.md",
+        "--root",
+        "."
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "planning_snapshot",
+      "started_at": "2026-09-30T21:27:17.354517+00:00",
+      "stderr": "",
+      "stdout": "{\n  \"algorithm\": \"sha256-manifest-v1\",\n  \"digest\": \"2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3\",\n  \"manifest\": \"/tmp/scanplant-p07-workspace/artifacts/bianchini/v2/approval/manifest-p07.sha256\"\n}\n"
+    },
+    {
+      "argv": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "planning-audit",
+        "docs/living/PROJECT_STATE.md",
+        "--root",
+        ".",
+        "--strict"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "strict_planning_audit",
+      "started_at": "2026-09-30T21:27:17.511190+00:00",
+      "stderr": "",
+      "stdout": "{\n  \"budget_exceeded\": [],\n  \"limits\": {\n    \"execution_units\": 40,\n    \"max_execution_unit_words\": 8000,\n    \"max_plan_words\": 16000,\n    \"plans\": 16,\n    \"platforms\": 6,\n    \"shared_context_words\": 24000\n  },\n  \"metrics\": {\n    \"execution_units\": 8,\n    \"max_execution_unit_words\": 859,\n    \"max_plan_words\": 926,\n    \"package_words\": 41506,\n    \"plans\": 7,\n    \"platforms\": 2,\n    \"shared_context_words\": 996\n  },\n  \"profile\": \"standard\",\n  \"quality_contract\": \"planning-quality-v2\",\n  \"readiness\": {\n    \"counts\": {\n      \"assumptions\": 9,\n      \"decisions\": 19,\n      \"design_surfaces\": 0,\n      \"pitfalls\": 18,\n      \"spec_deltas\": 5,\n      \"spikes\": 4,\n      \"user_actions\": 7\n    },\n    \"coverage_gaps\": [],\n    \"design\": null,\n    \"design_required\": false,\n    \"scope_digest\": \"fb6d796b6c7c2b34fe77b11414abd325ace538eb3153e069b014e3cd72a2b61b\",\n    \"spec_deltas\": [\n      {\n        \"id\": \"SD-001\",\n        \"source\": \"docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md\",\n        \"target\": \"docs/bianchini/current/specs/replan-v2.md\"\n      },\n      {\n        \"id\": \"SD-006\",\n        \"source\": \"docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md\",\n        \"target\": \"docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md\"\n      },\n      {\n        \"id\": \"SD-101\",\n        \"source\": \"docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md\",\n        \"target\": \"docs/bianchini/current/specs/provider-benchmark-decision.md\"\n      },\n      {\n        \"id\": \"SD-201\",\n        \"source\": \"docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md\",\n        \"target\": \"docs/bianchini/current/specs/offline-class-manifest.md\"\n      },\n      {\n        \"id\": \"SD-701\",\n        \"source\": \"docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md\",\n        \"target\": \"docs/bianchini/current/specs/traceable-dataset-curation.md\"\n      }\n    ],\n    \"status\": \"ready\"\n  },\n  \"recommended_profile\": \"standard\",\n  \"research_mode\": \"targeted_web\",\n  \"valid\": true,\n  \"warnings\": []\n}\n"
+    },
+    {
+      "argv": [
+        "sha256sum",
+        "-c",
+        "--strict",
+        "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "historical_checksums",
+      "started_at": "2026-09-30T21:27:17.662489+00:00",
+      "stderr": "",
+      "stdout": "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json: OK\nartifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md: OK\nartifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json: OK\ndocs/phase1/F1-MAN01-offline-class-manifest.md: OK\ndocs/phase1/offline-class-manifest.v1.json: OK\nscripts/phase1/test_offline_manifest.py: OK\nscripts/phase1/validate_offline_manifest.py: OK\n"
+    },
+    {
+      "argv": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "repo-hygiene",
+        "check",
+        "--repo",
+        "."
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "repo_hygiene",
+      "started_at": "2026-09-30T21:27:17.667606+00:00",
+      "stderr": "",
+      "stdout": "{\n  \"ignore_rule\": \"/.superpowers/\",\n  \"tracked_root_artifacts\": [],\n  \"valid\": true\n}\n"
+    },
+    {
+      "argv": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "workspace",
+        "check",
+        "--repo",
+        "."
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "workspace",
+      "started_at": "2026-09-30T21:27:17.784842+00:00",
+      "stderr": "",
+      "stdout": "{\n  \"branch\": \"bm/v2-p07\",\n  \"common_dir\": \"/home/administradorarthur/code/scanplant-current/ScanPlant/.git\",\n  \"git_dir\": \"/home/administradorarthur/code/scanplant-current/ScanPlant/.git/worktrees/scanplant-p07-workspace\",\n  \"safe\": true\n}\n"
+    },
+    {
+      "argv": [
+        "git",
+        "diff",
+        "--check"
+      ],
+      "cwd": "/tmp/scanplant-p07-workspace",
+      "exit_code": 0,
+      "gate": "diff_check",
+      "started_at": "2026-09-30T21:27:17.906459+00:00",
+      "stderr": "",
+      "stdout": ""
+    },
+    {
+      "argv": [
+        "sha256sum",
+        "-c",
+        "--strict",
+        "/home/administradorarthur/datasets/scanplant/p06-recovery-20260928/SHA256SUMS"
+      ],
+      "cwd": "/home/administradorarthur/datasets/scanplant/p06-recovery-20260928",
+      "exit_code": 0,
+      "gate": "p06_checksums",
+      "started_at": "2026-09-30T21:27:17.956359+00:00",
+      "stderr": "",
+      "stdout": ".lock: OK\ncoverage.json: OK\ninventory.json: OK\nmanifest.jsonl: OK\nquarantine/0440649cc6d6f7246f9858b79b408dc7c683fd6fac3c25695281cf5219b95847.jpg: OK\nquarantine/09d9fb06033b07a8305c2f46a6d6e292b090ca66e4a8b8668a5ea0a610c3766b.jpg: OK\nquarantine/0fa0c0fe80f1fe1f90e2e1a8f81e6d5146a0956afe1ca00ba45c4f410b3e96b6.jpg: OK\nquarantine/2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6.jpg: OK\nquarantine/38fdf4d90431956bccf426e9ec4b0281d9441fd968766add985832f4f900b251.jpg: OK\nquarantine/4aa046916264dc5d892121b1d9cc3dd5212bb9bb1bc50e999376d023286a9550.jpg: OK\nquarantine/7beac71d4fd1901559b36e041469666e1376dbf4b3eb761b9fec5fc8f48403bf.jpg: OK\nquarantine/816faa9cc87e736ea2293c887728a9d2ecac6a46396ed675ce7716ca7623d457.jpg: OK\nquarantine/8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b.jpg: OK\nquarantine/91524bde4f0351530c0818612a52bbc75fa59dca2aa0709f7a8a6273376d26b2.jpg: OK\nquarantine/a51f75db036a8fc96ec3929e514525eb2757763d6204dc8d2688f4c270a4e9e8.jpg: OK\nquarantine/ade5fe488454b574c5048aafc80abc74a914e59e53a8ecb70e997b8c5aa21f88.jpg: OK\nquarantine/b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a.jpg: OK\nquarantine/bbccd447a0f4713cd86685b0e358733941a44a38d58447989f36bb9db42c6856.jpg: OK\nquarantine/cc04b39c60ff068344be25f1b6c1d1d3628afe3272edba4794b5e8fdab8188c5.jpg: OK\nquarantine/d5a93acdc94d279cf38fff53bca0a06615351aebbfb26c8a620cbdddc1ae370b.jpg: OK\nquarantine/e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048.jpg: OK\nreview-2026-09-28/human-decisions.json: OK\nreview-2026-09-28/index.html: OK\nreview-2026-09-28/report.md: OK\nreview-2026-09-28/review.json: OK\nreview-2026-09-28/verification.json: OK\nrun-metadata.json: OK\nstate.json: OK\n"
+    }
+  ],
+  "evidence_kind": "uncommitted_working_tree_not_guard_proof",
+  "guard_proofs": "not_run_no_commit_or_new_worktree_authorized",
+  "human_acceptance": "pending",
+  "implementation_sha256": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
+  "schema_version": 1,
+  "tests_sha256": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5"
+}
diff --git a/artifacts/bianchini/v2/codex/P07/verify_working_tree.py b/artifacts/bianchini/v2/codex/P07/verify_working_tree.py
new file mode 100644
index 0000000..0ca0745
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P07/verify_working_tree.py
@@ -0,0 +1,124 @@
+"""P07 evidence for uncommitted working bytes, never a review_guard proof.
+
+Run with the existing Pillow 12.3.0 interpreter. --external verifies and reruns
+already persisted drafts without changing their bytes; never accepts proposals.
+"""
+import argparse
+from datetime import datetime, timezone
+import hashlib
+from itertools import combinations
+import json
+from pathlib import Path
+import subprocess
+import sys
+
+ROOT = Path(__file__).resolve().parents[5]
+sys.path.insert(0, str(ROOT / 'scripts/phase1'))
+import curate_p07 as c
+
+BASE = '822954421019ad611d4d14dc5461cc7a495b7db4'
+SOURCE = Path('/home/administradorarthur/datasets/scanplant/p06-recovery-20260928')
+OUTPUT = SOURCE.parent / 'p07-curation-20260928'
+BM = '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py'
+EXTERNAL_INITIAL = {
+    'analysis.json': '6f857cb52ad60fc596834698dd77ffb10d830d5cf907d10479b12ed76ee56338',
+    'curation.draft.json': '7b27bb37bf62b5a100407948154cec0a3a2c88214396c134a91872180559bc0c',
+    'human-decisions.json': '0d81616cd8ab79e2d8614a93b15ff7fdcc5f3e7f6f6adfa8c681afb3d697e195',
+    'report.draft.md': '6e054680bbbbb17bf01e720aaec6e48024655cbbef73bada11abac9724a4ef6d',
+    'source-before.json': 'eda50f599cd7e1bba996ae8e25760073903b122ff181ef38cb401804278b125c',
+    'summary.draft.json': '97c73477c4f5d6eabce2fd3f4333fb7c92725466bf7e1b41c31140a825c57353',
+}
+
+
+def external():
+    before = c.strict_load((OUTPUT / 'source-before.json').read_bytes())
+    assert c.tree_hashes(SOURCE) == before
+    assert all(c.sha((OUTPUT / n).read_bytes()) == h for n, h in EXTERNAL_INITIAL.items())
+    a = c.strict_load((OUTPUT / 'analysis.json').read_bytes())
+    d = c.strict_load((OUTPUT / 'human-decisions.json').read_bytes())
+    r = c.strict_load((OUTPUT / 'curation.draft.json').read_bytes())
+    assert c.curate(a, d, draft=True) == r
+    assert c.report(r) == (OUTPUT / 'report.draft.md').read_bytes()
+    assert c.encode(c.summary(r)) == (OUTPUT / 'summary.draft.json').read_bytes()
+    assert (ROOT / 'artifacts/phase1/p07/summary.json').read_bytes() == (OUTPUT / 'summary.draft.json').read_bytes()
+    assert a['source_hashes'] == before
+    assert a['pairs'] == [c.compare_pair(x, y) for x, y in combinations(a['records'], 2)]
+    assert len(a['pairs']) == len({p['pair_id'] for p in a['pairs']}) == 136
+    assert {x['sha256'] for x in a['records']} == {h for p, h in before.items() if p.startswith('quarantine/')}
+    assert [x['id'] for x in a['records']] == c.IDS
+    assert d['authority'] == 'agent_proposal' and r['counts']['approved_for_dataset'] == 0
+    assert all(not x['botanical']['expert_confirmation'] for x in d['decisions'])
+    assert all(x['usable'] == 0 for x in c.strict_load((SOURCE / 'coverage.json').read_bytes())['classes'])
+    old_hashes = c.tree_hashes(OUTPUT)
+    old_mtimes = {n: (OUTPUT / n).stat().st_mtime_ns for n in old_hashes}
+    # Same CLI as approved analysis, and bounded draft variant until U-701.
+    commands = [
+        [sys.executable, '-B', 'scripts/phase1/curate_p07.py', '--source', str(SOURCE), '--output', str(OUTPUT), '--analyze-only'],
+        [sys.executable, '-B', 'scripts/phase1/curate_p07.py', '--source', str(SOURCE), '--output', str(OUTPUT), '--review-draft', '--decisions', str(OUTPUT / 'human-decisions.json')],
+    ]
+    runs = []
+    for command in commands:
+        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
+        assert run.returncode == 0, (command, run.stderr)
+        runs.append({'argv': command, 'exit_code': run.returncode, 'stdout': run.stdout.strip()})
+    assert old_hashes == c.tree_hashes(OUTPUT)
+    assert old_mtimes == {n: (OUTPUT / n).stat().st_mtime_ns for n in old_hashes}
+    after = c.tree_hashes(SOURCE)
+    assert before == after and len(after) == 29
+    result = {
+        'source_files_unchanged': 29, 'images_unchanged': 17,
+        'images': [{'id': x['id'], 'sha256_before': before[x['stored_path']],
+                    'sha256_after': after[x['stored_path']]} for x in a['records']],
+        'comparison_count': 136, 'minimum_hamming': min(p['hamming_distance'] for p in a['pairs']),
+        'automatic_duplicate_signals': sum(p['signal'] != 'no_algorithmic_signal' for p in a['pairs']),
+        'visual_pairs': [{'pair_id': p['pair_id'], 'hamming_distance': p['hamming_distance']}
+                         for p in a['pairs'] if p['pair_id'] in {'Q01-Q02', 'Q14-Q15'}],
+        'counts': r['counts'], 'human_acceptance': 'pending', 'usable': 0,
+        'idempotence': {'bytes_equal': True, 'mtimes_equal': True, 'commands': runs},
+        'external_artifacts': EXTERNAL_INITIAL,
+    }
+    # Idempotent evidence write, no source mutation or backups.
+    c.persist(OUTPUT, {'verification.json': c.encode(result)})
+    print(json.dumps({'external': 'passed', 'images': 17, 'pairs': 136, 'idempotence': 'bytes_and_mtimes_equal'}))
+
+
+def gates():
+    commands = [
+        ('p07_tests', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_curate_p07.py']),
+        ('affected_and_historical_tests', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py']),
+        ('class_manifest', [sys.executable, '-B', 'scripts/phase1/validate_offline_manifest.py', '--manifest', 'docs/phase1/offline-class-manifest.v1.json', '--roster', 'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json']),
+        ('summary_json', [sys.executable, '-B', '-m', 'json.tool', 'artifacts/phase1/p07/summary.json']),
+        ('state', ['python3', '-B', BM, 'validate-state', 'docs/living/PROJECT_STATE.md']),
+        ('planning_snapshot', ['python3', '-B', BM, 'snapshot', 'verify', 'docs/living/PROJECT_STATE.md', '--root', '.']),
+        ('strict_planning_audit', ['python3', '-B', BM, 'planning-audit', 'docs/living/PROJECT_STATE.md', '--root', '.', '--strict']),
+        ('historical_checksums', ['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS']),
+        ('repo_hygiene', ['python3', '-B', BM, 'repo-hygiene', 'check', '--repo', '.']),
+        ('workspace', ['python3', '-B', BM, 'workspace', 'check', '--repo', '.']),
+        ('diff_check', ['git', 'diff', '--check']),
+        ('p06_checksums', ['sha256sum', '-c', '--strict', str(SOURCE / 'SHA256SUMS')]),
+    ]
+    results = []
+    for name, argv in commands:
+        cwd = SOURCE if name == 'p06_checksums' else ROOT
+        start = datetime.now(timezone.utc).isoformat()
+        run = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=180)
+        results.append({'gate': name, 'argv': argv, 'cwd': str(cwd), 'started_at': start,
+                        'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
+        print(name, run.returncode, flush=True)
+    evidence = {'schema_version': 1, 'evidence_kind': 'uncommitted_working_tree_not_guard_proof',
+                'base_revision': BASE, 'implementation_sha256': c.sha((ROOT / 'scripts/phase1/curate_p07.py').read_bytes()),
+                'tests_sha256': c.sha((ROOT / 'scripts/phase1/test_curate_p07.py').read_bytes()),
+                'commands': results, 'human_acceptance': 'pending', 'guard_proofs': 'not_run_no_commit_or_new_worktree_authorized'}
+    target = ROOT / 'artifacts/bianchini/v2/codex/P07/verification.json'
+    assert not target.exists(), 'Preserve prior evidence; diagnose before rerunning gates.'
+    target.write_bytes(c.encode(evidence))
+    assert all(x['exit_code'] == 0 for x in results), 'gate_failed'
+
+
+if __name__ == '__main__':
+    parser = argparse.ArgumentParser(description=__doc__)
+    parser.add_argument('--external', action='store_true')
+    parser.add_argument('--gates', action='store_true')
+    args = parser.parse_args()
+    assert args.external != args.gates, 'Choose exactly one operation'
+    external() if args.external else gates()
diff --git a/artifacts/bianchini/v2/ledgers/P07.md b/artifacts/bianchini/v2/ledgers/P07.md
new file mode 100644
index 0000000..a474cc2
--- /dev/null
+++ b/artifacts/bianchini/v2/ledgers/P07.md
@@ -0,0 +1,28 @@
+# Ledger P07 — append-only
+
+## Retomada da unidade 1 — 2026-09-30
+
+- Plano congelado: `docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md`.
+- Digest aprovado: `2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3`.
+- Base revision e HEAD: `822954421019ad611d4d14dc5461cc7a495b7db4`.
+- Workspace existente: `/tmp/scanplant-p07-workspace`; branch `bm/v2-p07`.
+- Perfil standard; garantia aprovada slice/per_slice; uma única unidade em rodada agrupada solicitada pelo responsável.
+- Identidade da unidade: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`.
+- Ambiente existente Python 3.14.4/Pillow 12.3.0; todos os caminhos temporários localizados; nada reiniciado.
+- Fonte e resultados externos existentes reconciliados; 29 arquivos P06, 17 imagens, hashes iguais ao registro inicial.
+
+## Ajustes limitados e evidências
+
+`bm.py change-policy --plan-command --file-location` retornou `bounded_amendment`, sem reaprovação nem mutação do plano. O helper operacional de verificação fica em `artifacts/bianchini/v2/codex/P07/verify_working_tree.py`. O interpretador concreto é o ambiente existente. `--review-draft` preserva as propostas sem substituí-las por decisão humana; `--finalize` real aguarda U-701. Nenhuma unidade ou entrega foi criada.
+
+Dois testes de regressão na retomada falharam antes da correção: relatório recarregado de JSON alterava a ordem das contagens; rejeição de duplicata não exigia parecer explícito do par. Correções locais preservam os bytes externos já persistidos. RED: 38 testes, duas falhas. GREEN final: 38/38 P07 e 162/162 na suíte afetada. Não houve novo ciclo formal do guard.
+
+`verification.json` registra argv/cwd/horário/exit code/stdout/stderr e hashes do código/testes. Validador P05, estado, snapshot aprovado, auditoria estrita, checksums P05/P06, repo-hygiene, workspace e diff-check passaram. Reexecução real: bytes e mtimes iguais, 136 pares, nenhuma alteração P06. A evidência integral dos 17 hashes antes/depois está no `verification.json` externo.
+
+## Revisão e fronteira de autoridade
+
+Propostas existentes preservadas: 8 needs_botanical_review, 7 needs_human_review, 2 rejected_quality; demais estados zero. `usable=0`, treinamento não autorizado. Nenhuma confirmação botânica pericial. U-701/U-702 aguardam a decisão humana única solicitada para o fim desta rodada.
+
+Guard não iniciado sobre o delta não commitado. `proof` cria checkout/worktree de commit; `review-package` base..HEAD não inclui untracked. Executar esses proofs sobre HEAD alegaria evidência de código ausente; criar commit/nova worktree violaria instrução humana. Não há sidecar nem fase terminal, blockers congelados, fix rounds ou redesign formal registrados. Não chamar `freeze`, `complete` ou `stop` para simular fechamento. O pacote de revisão deixa explícita essa limitação e referencia os hashes de trabalho. Verificação local concluída; conclusão formal permanece pendente.
+
+O estado vivo só registra progresso da execução e aceite pendente; nenhum campo de convergência foi transplantado para PROJECT_STATE. Repositório principal permanece limpo na baseline; índices vazios. Plano canônico já reconciliado no planejamento permanece congelado. P01–P06/P05-R1, current_specs e release pending preservados.
diff --git a/artifacts/phase1/p07/summary.json b/artifacts/phase1/p07/summary.json
new file mode 100644
index 0000000..337fe9c
--- /dev/null
+++ b/artifacts/phase1/p07/summary.json
@@ -0,0 +1,273 @@
+{
+  "classes_without_approved": [
+    "species_01",
+    "species_02",
+    "species_03",
+    "species_04",
+    "species_05",
+    "species_06",
+    "species_07",
+    "species_08",
+    "species_09",
+    "species_10",
+    "species_11",
+    "species_12",
+    "outra_planta",
+    "imagem_invalida"
+  ],
+  "classes_without_candidates": [
+    "species_04",
+    "species_08",
+    "outra_planta",
+    "imagem_invalida"
+  ],
+  "comparison_count": 136,
+  "counts": {
+    "approved_for_dataset": 0,
+    "needs_botanical_review": 8,
+    "needs_human_review": 7,
+    "rejected_duplicate": 0,
+    "rejected_label": 0,
+    "rejected_privacy": 0,
+    "rejected_quality": 2
+  },
+  "coverage": [
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_01",
+      "name": "Epipremnum aureum",
+      "pending": 1,
+      "rejected": 1
+    },
+    {
+      "approved": 0,
+      "candidates": 1,
+      "class_id": "species_02",
+      "name": "Monstera deliciosa",
+      "pending": 1,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_03",
+      "name": "Zamioculcas zamiifolia",
+      "pending": 2,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 0,
+      "class_id": "species_04",
+      "name": "Spathiphyllum wallisii",
+      "pending": 0,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_05",
+      "name": "Dracaena trifasciata",
+      "pending": 2,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 1,
+      "class_id": "species_06",
+      "name": "Aloe vera",
+      "pending": 1,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_07",
+      "name": "Chlorophytum comosum",
+      "pending": 1,
+      "rejected": 1
+    },
+    {
+      "approved": 0,
+      "candidates": 0,
+      "class_id": "species_08",
+      "name": "Codiaeum variegatum",
+      "pending": 0,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_09",
+      "name": "Ficus elastica",
+      "pending": 2,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 1,
+      "class_id": "species_10",
+      "name": "Kalanchoe blossfeldiana",
+      "pending": 1,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_11",
+      "name": "Nephrolepis exaltata",
+      "pending": 2,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 2,
+      "class_id": "species_12",
+      "name": "Tradescantia zebrina",
+      "pending": 2,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 0,
+      "class_id": "outra_planta",
+      "name": "Outra planta",
+      "pending": 0,
+      "rejected": 0
+    },
+    {
+      "approved": 0,
+      "candidates": 0,
+      "class_id": "imagem_invalida",
+      "name": "Imagem inválida",
+      "pending": 0,
+      "rejected": 0
+    }
+  ],
+  "records": [
+    {
+      "class_id": "species_01",
+      "id": "Q01",
+      "review_id": "R01",
+      "sha256": "b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_01",
+      "id": "Q02",
+      "review_id": "R02",
+      "sha256": "cc04b39c60ff068344be25f1b6c1d1d3628afe3272edba4794b5e8fdab8188c5",
+      "state": "rejected_quality"
+    },
+    {
+      "class_id": "species_02",
+      "id": "Q03",
+      "review_id": "R03",
+      "sha256": "2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_03",
+      "id": "Q04",
+      "review_id": "R04",
+      "sha256": "7beac71d4fd1901559b36e041469666e1376dbf4b3eb761b9fec5fc8f48403bf",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_03",
+      "id": "Q05",
+      "review_id": "R05",
+      "sha256": "0fa0c0fe80f1fe1f90e2e1a8f81e6d5146a0956afe1ca00ba45c4f410b3e96b6",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_05",
+      "id": "Q06",
+      "review_id": "R06",
+      "sha256": "38fdf4d90431956bccf426e9ec4b0281d9441fd968766add985832f4f900b251",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_05",
+      "id": "Q07",
+      "review_id": "R07",
+      "sha256": "4aa046916264dc5d892121b1d9cc3dd5212bb9bb1bc50e999376d023286a9550",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_06",
+      "id": "Q08",
+      "review_id": "R08",
+      "sha256": "09d9fb06033b07a8305c2f46a6d6e292b090ca66e4a8b8668a5ea0a610c3766b",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_07",
+      "id": "Q09",
+      "review_id": "R09",
+      "sha256": "e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_07",
+      "id": "Q10",
+      "review_id": "R10",
+      "sha256": "bbccd447a0f4713cd86685b0e358733941a44a38d58447989f36bb9db42c6856",
+      "state": "rejected_quality"
+    },
+    {
+      "class_id": "species_09",
+      "id": "Q11",
+      "review_id": "R11",
+      "sha256": "0440649cc6d6f7246f9858b79b408dc7c683fd6fac3c25695281cf5219b95847",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_09",
+      "id": "Q12",
+      "review_id": "R12",
+      "sha256": "ade5fe488454b574c5048aafc80abc74a914e59e53a8ecb70e997b8c5aa21f88",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_10",
+      "id": "Q13",
+      "review_id": "R13",
+      "sha256": "a51f75db036a8fc96ec3929e514525eb2757763d6204dc8d2688f4c270a4e9e8",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_11",
+      "id": "Q14",
+      "review_id": "R14",
+      "sha256": "816faa9cc87e736ea2293c887728a9d2ecac6a46396ed675ce7716ca7623d457",
+      "state": "needs_botanical_review"
+    },
+    {
+      "class_id": "species_11",
+      "id": "Q15",
+      "review_id": "R15",
+      "sha256": "d5a93acdc94d279cf38fff53bca0a06615351aebbfb26c8a620cbdddc1ae370b",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_12",
+      "id": "Q16",
+      "review_id": "R16",
+      "sha256": "8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b",
+      "state": "needs_human_review"
+    },
+    {
+      "class_id": "species_12",
+      "id": "Q17",
+      "review_id": "R17",
+      "sha256": "91524bde4f0351530c0818612a52bbc75fa59dca2aa0709f7a8a6273376d26b2",
+      "state": "needs_botanical_review"
+    }
+  ],
+  "schema_version": 1,
+  "stage": "agent_proposals_pending_human",
+  "training_authorized": false,
+  "training_sufficiency": "not_demonstrated"
+}
diff --git a/docs/living/PROJECT_STATE.md b/docs/living/PROJECT_STATE.md
index f2ec628..3cadb5a 100644
--- a/docs/living/PROJECT_STATE.md
+++ b/docs/living/PROJECT_STATE.md
@@ -237,21 +237,21 @@
       "gates": [
         "authorless-quarantine-contract",
         "alias-set-reconciliation",
         "taxonomic-human-review",
         "documentary-integrity"
       ]
     },
     {
       "id": "P07",
       "path": "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md",
-      "status": "approved",
+      "status": "in_progress",
       "risk": "medium",
       "execution": "slice",
       "review": "per_slice",
       "test_seams": [
         "p07-source-integrity",
         "p07-quality-triage",
         "p07-perceptual-pairs",
         "p07-human-decision",
         "p07-sanitized-output"
       ],
@@ -266,31 +266,31 @@
         "idempotence-and-sanitization",
         "final-human-acceptance"
       ]
     }
   ],
   "verification": {
     "fast": {
       "commands": [
         "python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'"
       ],
-      "status": "pending",
-      "scope": "P07: fixtures sintéticas e regressão focada; executáveis após implementação autorizada."
+      "status": "passed",
+      "scope": "P07: 38 testes sintéticos aprovados; resultados e hashes em artifacts/bianchini/v2/codex/P07/verification.json. Evidência dos bytes de trabalho, não proof de commit."
     },
     "plan": {
       "commands": [
         "python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'",
         "python -B -m json.tool artifacts/phase1/p07/summary.json",
         "git diff --check"
       ],
       "status": "pending",
-      "scope": "P07: suite afetada, JSON estrito, reconciliação dos 17 e revisão humana/aceite por evidência no ledger; sem gate de release."
+      "scope": "Gates técnicos P07 verificados nos bytes de trabalho; aceite humano U-701/U-702 e revisão formal do guard pendentes. Não declarar completed."
     },
     "release": {
       "commands": [
         "git diff --check"
       ],
       "status": "blocked",
       "reason": "Não é gate suficiente de release. P01/P03 blocked-terminal; garantia seletiva/lifecycle, fingerprint, suítes/build aplicáveis e homologação não foram liberados nem substituídos por P04."
     }
   },
   "release": {
@@ -301,21 +301,26 @@
     ],
     "profiles": [
       "Release"
     ],
     "candidate": null,
     "final_gate": "homologar-sistema",
     "homologation": "pending",
     "final_review": "pending",
     "delivery": "pending"
   },
-  "active_execution": null,
+  "active_execution": {
+    "plan_id": "P07",
+    "unit": "1",
+    "workspace": "/tmp/scanplant-p07-workspace",
+    "gate": "human-17-decisions-and-final-human-acceptance"
+  },
   "telemetry": {
     "enabled": false,
     "path": "artifacts/bianchini/v2/telemetry.jsonl"
   },
   "blockers": [
     {
       "id": "B-P01-OBS-TERMINAL",
       "summary": "P03-R1 consumiu 1/1 campanha e falhou no resolver do local tool antes de mutação. P01 permanece blocked-terminal.",
       "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json"
     },
@@ -343,21 +348,21 @@
       "id": "B-P03-R5-U008-TERMINAL-TEST-PROJECT-SELECTION",
       "summary": "U-008 iniciou Stryker com TestProjects vazio; ScanPlantAPI.sln selecionou ScanPlantAPI.Tests.csproj multi-target, NETSDK1045 ocorreu antes de mutantes, campaign_count=1 e U-008 foi consumida sem retry.",
       "evidence": "artifacts/bianchini/v2/checkpoints/P03-R5-U008-terminal-attempt-716ef26.json"
     },
     {
       "id": "B-P03-R6-U009-TERMINAL-VSTEST-CONNECTION",
       "summary": "P03-R6/U-009 foi invocada uma única vez via Bash: campaign_count=2, campaign_executed=true, U-008=consumed_non_reusable, U-009=consumed, exit_code=134 e failure_stage=campaign. Stryker 4.16.0 iniciou, mas falhou ao conectar a vstest.console após 90 segundos antes de produzir mutantes, mutation-report ou mutation score. Falha posterior ao marcador é terminal e não admite retry R6.",
       "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909"
     }
   ],
-  "next_action": "Planejamento P07 aprovado e autorizado para publicação; execução da curadoria depende de autorização posterior. P01/P03-R6 blocked-terminal e release pending preservados.",
+  "next_action": "Decisão humana única sobre os 17 pareceres P07 e os bytes finais na worktree existente; U-701/U-702 pendentes. Nenhuma aprovação para dataset ou treinamento; release pending. Staging/commit/push não autorizados nesta rodada.",
   "continuity_decision": {
     "recommended_alternative": "A",
     "status": "approved",
     "next_milestone": "F1-API01",
     "proposed_plan": "P04",
     "document": "docs/bianchini/changes/v2/POST-U009-DELIBERATION.md",
     "release_authorized": false,
     "new_mutation_campaign_authorized": false,
     "historical_only": true
   },
@@ -391,22 +396,22 @@
     "manifest_path": "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
     "manifest_digest": "9657abcbb1520701a59bbd8fcecf34ff5d7a34fb901ad5d84defd6df34a31d23",
     "execution_status": "completed",
     "state_at_revision": "a34da4dd34eea58921862f0d0fa2d0016be5ce31",
     "note": "Registro histórico, não revalidar manifesto antigo contra ledger/evidências vivos posteriores."
   },
   "next_milestone_proposal": {
     "plan": "P07",
     "functional_id": "P07",
     "title": "Curadoria rastreável das 17 imagens externas preservadas pelo P06",
-    "status": "approved",
-    "execution_authorized": false,
+    "status": "in_progress",
+    "execution_authorized": true,
     "release_authorized": false,
     "usable_baseline": 0,
     "source_commit": "3f0beaad06bfdd9b4f069a6f5f668ce9e9b93d97"
   },
   "prior_p05_approval": {
     "status": "approved",
     "approved_at": "2026-09-11T18:23:11Z",
     "approved_by": "responsável humano",
     "approved_plans": [
       "P01",
diff --git a/docs/phase1/P07-curation.md b/docs/phase1/P07-curation.md
new file mode 100644
index 0000000..c035ed5
--- /dev/null
+++ b/docs/phase1/P07-curation.md
@@ -0,0 +1,45 @@
+# P07 — curadoria rastreável, aguardando aceite humano
+
+A execução existente foi retomada na worktree `/tmp/scanplant-p07-workspace`, branch `bm/v2-p07`, base `822954421019ad611d4d14dc5461cc7a495b7db4`. O planejamento continua congelado no digest `2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3`.
+
+As 17 fontes externas foram reconciliadas com P06, incluindo Q/R, classe candidata, SHA-256 e proveniência. Imagens e resultados integrais permanecem externos. Os 29 arquivos P06 continuam byte-iguais ao inventário inicial. Autoria, licença e origem permanecem nos resultados externos.
+
+O resumo em `artifacts/phase1/p07/summary.json` é uma projeção de **propostas do agente**, sem decisão humana registrada. As três avaliações favoráveis antigas do P06 não foram promovidas. `usable=0`, `approved_for_dataset=0`, treinamento não autorizado e suficiência para treinamento não demonstrada.
+
+| Estado proposto | Quantidade |
+| --- | ---: |
+| approved_for_dataset | 0 |
+| rejected_quality | 2 |
+| rejected_duplicate | 0 |
+| rejected_privacy | 0 |
+| rejected_label | 0 |
+| needs_botanical_review | 8 |
+| needs_human_review | 7 |
+
+Há 136 comparações SHA/dHash horizontal 64 bits, sem sinal automático de duplicidade nos limiares aprovados. Distância mínima 21. Q01–Q02 e Q14–Q15 permanecem pares visuais pendentes, ambos com distância 35. Nenhum item foi rejeitado automaticamente.
+
+As 14 classes seguem sem candidato aprovado. `species_04`, `species_08`, `outra_planta` e `imagem_invalida` não têm candidato adquirido. Ausência de aprovação ou classes vazias não invalida o processo de curadoria.
+
+## Operação reproduzível
+
+Dependência única: Pillow 12.3.0, com biblioteca padrão Python. Ambiente existente `/tmp/scanplant-p07-env`; nenhuma dependência adicional instalada na retomada.
+
+```bash
+/tmp/scanplant-p07-env/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'
+/tmp/scanplant-p07-env/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
+/tmp/scanplant-p07-env/bin/python -B artifacts/bianchini/v2/codex/P07/verify_working_tree.py --external
+```
+
+38 testes P07 e 162 testes afetados/históricos passaram. JSON estrito, métricas/fronteiras, SHA/dHash, colisões, pares manuais, barreira de aprovação humana, duplicatas, integridade, trava, escrita atômica e idempotência estão cobertos. A reexecução real de análise e rascunho preservou bytes e mtimes; a finalização humana foi testada somente com fixtures sintéticas.
+
+O modo `--review-draft --decisions <arquivo>` permite preparar o resultado para aceite sem alegar decisão humana. `--finalize` recusa `authority=agent_proposal`. Os arquivos `.draft` são deliberados: U-701 ainda não foi consumida. As propostas persistidas e seus timestamps não foram reescritos.
+
+Resultados integrais: `/home/administradorarthur/datasets/scanplant/p07-curation-20260928/`. Incluem `analysis.json`, `human-decisions.json` (conteúdo explicitamente marcado `agent_proposal`), `curation.draft.json`, `report.draft.md`, `summary.draft.json`, `source-before.json` e `verification.json`. Não copiar os relatórios integrais para o Git.
+
+## Limites de fechamento
+
+P07 permanece `in_progress`. U-701 requer confirmação dos 17 pareceres; U-702 requer aceite dos bytes finais. Avaliação do agente não constitui confirmação botânica pericial. Todos os arquivos físicos permanecem em quarentena.
+
+A revisão formal do guard não foi executada: seu `proof` cria uma worktree a partir de um commit; a implementação permanece não commitada e a rodada proíbe nova worktree/staging/commit. As evidências registram hashes dos bytes de trabalho, não `proof_id` de um commit que não contém a implementação. Nenhum sidecar terminal foi fabricado. A revisão técnica local e os gates estão documentados em `artifacts/bianchini/v2/codex/P07/`.
+
+P01–P06/P05-R1 e seus históricos foram preservados; `current_specs` não foi sincronizado. `release=pending`. P08 não iniciado. Não houve staging, commit, push, merge ou tag.
diff --git a/scripts/phase1/curate_p07.py b/scripts/phase1/curate_p07.py
new file mode 100644
index 0000000..dca2e13
--- /dev/null
+++ b/scripts/phase1/curate_p07.py
@@ -0,0 +1,534 @@
+"""P07: read-only source reconciliation, deterministic triage and reviewed decisions.
+
+No network, image writes, automatic approval, or P06 mutation. Pillow==12.3.0.
+Human decisions are inputs; agent proposals can only create explicitly draft results.
+"""
+import argparse
+from collections import Counter
+from contextlib import contextmanager
+from datetime import datetime
+import fcntl
+import hashlib
+from io import BytesIO
+from itertools import combinations
+import json
+import math
+import os
+from pathlib import Path
+import platform
+import re
+import stat
+import sys
+import tempfile
+import warnings
+
+import PIL
+from PIL import Image
+
+ROOT = Path(__file__).resolve().parents[2]
+CLASS_MANIFEST = ROOT / "docs/phase1/offline-class-manifest.v1.json"
+STATES = ("approved_for_dataset", "rejected_quality", "rejected_duplicate",
+          "rejected_privacy", "rejected_label", "needs_botanical_review", "needs_human_review")
+IDS = [f"Q{i:02}" for i in range(1, 18)]
+RUN = "p06-recovery-20260928"
+SHA = re.compile(r"[0-9a-f]{64}")
+PRIVACY = ("people", "faces", "plates", "vehicles", "residences", "documents", "other_identifiable")
+VISUAL = ("framing", "occlusion", "multiple_species", "representativeness")
+GATES = ("integrity", "provenance", "quality", "privacy", "uniqueness", "botanical_label")
+METHOD = {
+    "algorithm": "p07-triage-v1", "pillow": "12.3.0", "luminance_size": [256, 256],
+    "resize": "LANCZOS", "laplacian": "4c-left-right-up-down; interior; population_variance",
+    "dhash": "horizontal-v1; L 9x8; right>left; row-major; first-bit-most-significant",
+    "thresholds": {"minimum_side_lt": 224, "aspect_gt": 3.0, "mean_lt": 40,
+                   "mean_gt": 215, "dark_lte": 15, "bright_gte": 240,
+                   "extreme_fraction_gte": 0.25, "laplacian_variance_lt": 100,
+                   "near_distance_lte": 6, "borderline_distance_lte": 10}}
+RECORD_KEYS = set("attribution_html attribution_required author author_html botanical_validation_performed class_id copyrighted credit_html declared_mime declared_size file_url license license_id license_url page_id page_url privacy_status query reason restrictions result sequence sha256 source_sha1 source_sha256 source_timestamp stored_path timestamp title transformation visual_review_performed".split())
+P06_DECISION_KEYS = set("assistant_visual_review_performed botanical_assessment class_id decision decision_id expert_taxonomic_confirmation manifest_attribution_license_origin_coherent original_resolution_review physical_location privacy_assessment quality_and_framing rationale review_id sha256 stored_path training_authorized".split())
+
+
+class CurationError(ValueError):
+    """Safe diagnostics contain stable codes, never private input values."""
+
+
+def require(condition, code):
+    if not condition:
+        raise CurationError(code)
+
+
+def sha(raw):
+    return hashlib.sha256(raw).hexdigest()
+
+
+def encode(value):
+    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
+                       allow_nan=False) + "\n").encode("utf-8")
+
+
+def strict_load(raw):
+    def pairs(items):
+        result = {}
+        for key, value in items:
+            require(key not in result, "duplicate_json_key")
+            result[key] = value
+        return result
+    def constant(_):
+        raise CurationError("nonfinite_json")
+    try:
+        require(type(raw) is bytes and not raw.startswith(b"\xef\xbb\xbf"), "json_encoding")
+        require(b"\r" not in raw and raw.endswith(b"\n"), "json_utf8_lf")
+        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)
+        # Reject exponent overflow too (1e999 is not a parse_constant token).
+        def finite(v):
+            if type(v) is float:
+                require(math.isfinite(v), "nonfinite_json")
+            elif type(v) is dict:
+                for x in v.values():
+                    finite(x)
+            elif type(v) is list:
+                for x in v:
+                    finite(x)
+        finite(value)
+        return value
+    except (UnicodeError, json.JSONDecodeError):
+        raise CurationError("invalid_json") from None
+
+
+def obj(value, keys):
+    require(type(value) is dict and set(value) == set(keys), "object_fields")
+
+
+def text(value):
+    require(type(value) is str and bool(value.strip()), "nonempty_text")
+
+
+def no_symlinks(path):
+    path = Path(os.path.abspath(path))
+    require(not any(p.is_symlink() for p in (path, *path.parents)), "symlink")
+    return path
+
+
+def read_file(path):
+    path = no_symlinks(path)
+    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
+    with os.fdopen(fd, "rb") as stream:
+        require(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), "not_regular_file")
+        return stream.read()
+
+
+def tree_hashes(root):
+    root = no_symlinks(root)
+    require(root.is_dir(), "source_missing")
+    result = {}
+    for path in sorted(root.rglob("*")):
+        no_symlinks(path)
+        if path.is_dir():
+            continue
+        result[path.relative_to(root).as_posix()] = sha(read_file(path))
+    return result
+
+
+def reconcile(source, class_manifest=CLASS_MANIFEST):
+    """Reconcile all P06 witnesses before any image decoding."""
+    source = no_symlinks(source)
+    before = tree_hashes(source)
+    load = lambda name: strict_load(read_file(source / name))
+    inventory = load("inventory.json")
+    require(type(inventory) is list, "inventory_type")
+    inv = {}
+    for item in inventory:
+        obj(item, {"path", "bytes", "sha256"})
+        path = item["path"]
+        require(type(path) is str and path not in inv and path in before, "inventory_set")
+        require(type(item["bytes"]) is int and item["bytes"] == (source / path).stat().st_size,
+                "inventory_size")
+        require(item["sha256"] == before[path], "inventory_hash")
+        inv[path] = item["sha256"]
+    require(set(inv) == set(before) - {"inventory.json", "SHA256SUMS"}, "inventory_coverage")
+    checksums = {}
+    for line in read_file(source / "SHA256SUMS").decode("ascii").splitlines():
+        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
+        require(match is not None, "checksum_syntax")
+        digest, name = match.groups()
+        require(name not in checksums and before.get(name) == digest, "checksum_mismatch")
+        checksums[name] = digest
+    require(set(checksums) == set(before) - {"SHA256SUMS"}, "checksum_coverage")
+    classes_raw = read_file(class_manifest)
+    canonical = strict_load(classes_raw)
+    require(canonical["manifest_version"] == "1.1.0", "class_manifest_version")
+    classes = [{"class_id": c["class_id"], "name": c["scientific_name"] or c["display_name"]}
+               for c in canonical["classes"]]
+    class_ids = {c["class_id"] for c in classes}
+    require(len(classes) == len(class_ids) == 14, "class_set")
+    state = load("state.json")
+    obj(state, {"schema_version", "canonical_manifest_sha256", "records", "searches"})
+    require(type(state["schema_version"]) is int and state["schema_version"] == 1, "state_schema")
+    require(state["canonical_manifest_sha256"] == sha(classes_raw), "class_manifest_hash")
+    manifest = [strict_load(line + b"\n") for line in read_file(source / "manifest.jsonl").splitlines()]
+    require(type(state["records"]) is list and state["records"] == manifest, "state_manifest_mismatch")
+    require(type(state["searches"]) is dict and set(state["searches"]) == class_ids, "search_classes")
+    for search in state["searches"].values():
+        obj(search, {"continuation", "exhausted", "pages_fetched", "status"})
+        require(type(search["exhausted"]) is bool and type(search["pages_fetched"]) is int,
+                "search_types")
+        if search["continuation"] is not None:
+            obj(search["continuation"], {"continue", "gsroffset"})
+    accepted = {}
+    for i, record in enumerate(manifest, 1):
+        require(type(record) is dict and set(record) <= RECORD_KEYS, "record_fields")
+        require(type(record.get("sequence")) is int and record["sequence"] == i, "sequence")
+        require(record.get("class_id") in class_ids, "record_class")
+        if record.get("result") != "accepted":
+            continue
+        obj(record, RECORD_KEYS)
+        digest = record["sha256"]
+        require(type(digest) is str and SHA.fullmatch(digest) and digest not in accepted, "accepted_hash_set")
+        require(record["stored_path"] == f"quarantine/{digest}.jpg", "stored_path")
+        require(before.get(record["stored_path"]) == digest, "image_hash")
+        for key in ("license", "license_id", "license_url", "page_url", "file_url", "author"):
+            text(record[key])
+        accepted[digest] = record
+    actual = {p for p in before if p.startswith("quarantine/")}
+    require(len(accepted) == 17 and actual == {r["stored_path"] for r in accepted.values()}, "image_set_17")
+    coverage = load("coverage.json")
+    obj(coverage, set("accepted_cap_per_class accepted_semantics canonical_manifest_sha256 classes failure_count_semantics manifest_jsonl_sha256 page_budget_per_class_per_run schema_version status training_ready visual_review_performed".split()))
+    require(coverage["canonical_manifest_sha256"] == sha(classes_raw) and
+            coverage["manifest_jsonl_sha256"] == before["manifest.jsonl"], "coverage_hash")
+    require(coverage["training_ready"] is False, "source_training_flag")
+    require(type(coverage["classes"]) is list and len(coverage["classes"]) == 14, "coverage_classes")
+    seen_classes = set()
+    for c in coverage["classes"]:
+        obj(c, set("accepted class_id consulted deferred deferred_reasons failure_reasons failures name pages_fetched quarantined query reasons rejected status usable".split()))
+        require(c["class_id"] in class_ids and c["class_id"] not in seen_classes, "coverage_class_set")
+        seen_classes.add(c["class_id"])
+        count = sum(r["class_id"] == c["class_id"] for r in accepted.values())
+        require(type(c["accepted"]) is int and c["accepted"] == count and
+                type(c["quarantined"]) is int and c["quarantined"] == count and
+                type(c["usable"]) is int and c["usable"] == 0, "coverage_counts")
+    prior = load("review-2026-09-28/human-decisions.json")
+    obj(prior, set("confirmation_source decisions human_grouped_decision_confirmed notice p06_status recorded_at release_status remote_metadata_requeried review_method run_id schema_version totals training_ready".split()))
+    require(prior["run_id"] == RUN and prior["human_grouped_decision_confirmed"] is True and
+            prior["training_ready"] is False, "prior_run")
+    require(type(prior["decisions"]) is list and len(prior["decisions"]) == 17, "prior_count")
+    records, seen = [], set()
+    for i, d in enumerate(sorted(prior["decisions"], key=lambda x: x["decision_id"]), 1):
+        obj(d, P06_DECISION_KEYS)
+        require(d["decision_id"] == f"Q{i:02}" and d["review_id"] == f"R{i:02}", "qr_mapping")
+        digest = d["sha256"]
+        require(digest in accepted and digest not in seen, "decision_hash_set")
+        seen.add(digest)
+        r = accepted[digest]
+        require(d["class_id"] == r["class_id"] and d["stored_path"] == r["stored_path"], "decision_identity")
+        require(d["decision"] in {"aprovar_para_curadoria_futura", "manter_em_quarentena", "rejeitar"}, "prior_decision")
+        require(d["training_authorized"] is False and d["physical_location"] == "quarantine", "prior_quarantine")
+        records.append({"id": d["decision_id"], "review_id": d["review_id"], "sha256": digest,
+                        "class_id": d["class_id"], "stored_path": d["stored_path"],
+                        "prior_p06_decision": d["decision"], "provenance": r})
+    require(Counter(d["decision"] for d in prior["decisions"]) == prior["totals"], "prior_counts")
+    metadata = load("run-metadata.json")
+    require(metadata.get("run_id") == RUN and metadata.get("totals", {}).get("accepted") == 17,
+            "metadata_run")
+    return before, records, classes
+
+
+def flags_for(width, height, mean, dark, bright, variance):
+    checks = [(min(width, height) < 224, "small_dimension"),
+              (max(width, height) / min(width, height) > 3, "extreme_aspect"),
+              (mean < 40, "dark_mean"), (mean > 215, "bright_mean"),
+              (dark >= .25, "dark_fraction"), (bright >= .25, "bright_fraction"),
+              (variance < 100, "low_laplacian_variance")]
+    return [name for condition, name in checks if condition]
+
+
+def laplacian_variance(pixels, width, height):
+    require(width >= 3 and height >= 3 and len(pixels) == width * height, "laplacian_shape")
+    values = [4 * pixels[y * width + x] - pixels[y * width + x - 1] - pixels[y * width + x + 1]
+              - pixels[(y - 1) * width + x] - pixels[(y + 1) * width + x]
+              for y in range(1, height - 1) for x in range(1, width - 1)]
+    n, total, squares = len(values), sum(values), sum(v * v for v in values)
+    return (squares * n - total * total) / (n * n)
+
+
+def dhash(image):
+    pixels = list(image.convert("L").resize((9, 8), Image.Resampling.LANCZOS).get_flattened_data())
+    bits = 0
+    for y in range(8):
+        for x in range(8):
+            bits = (bits << 1) | (pixels[y * 9 + x + 1] > pixels[y * 9 + x])
+    return f"{bits:016x}"
+
+
+def metrics(raw):
+    require(PIL.__version__ == "12.3.0", "pillow_version")
+    try:
+        with warnings.catch_warnings():
+            warnings.simplefilter("error", Image.DecompressionBombWarning)
+            with Image.open(BytesIO(raw)) as check:
+                require(check.format == "JPEG" and getattr(check, "n_frames", 1) == 1, "image_format")
+                check.verify()
+            with Image.open(BytesIO(raw)) as image:
+                image.load()
+                width, height = image.size
+                gray = image.convert("L").resize((256, 256), Image.Resampling.LANCZOS)
+                pixels = list(gray.get_flattened_data())
+                mean = sum(pixels) / len(pixels)
+                dark = sum(x <= 15 for x in pixels) / len(pixels)
+                bright = sum(x >= 240 for x in pixels) / len(pixels)
+                variance = laplacian_variance(pixels, 256, 256)
+                return {"decode": "ok", "format": image.format, "width": width, "height": height,
+                        "aspect": max(width, height) / min(width, height), "mean_luminance": mean,
+                        "dark_fraction": dark, "bright_fraction": bright,
+                        "laplacian_variance": variance, "dhash64": dhash(image),
+                        "flags": flags_for(width, height, mean, dark, bright, variance)}
+    except (OSError, ValueError, Image.DecompressionBombWarning, Image.DecompressionBombError):
+        return {"decode": "failed", "format": None, "width": None, "height": None, "aspect": None,
+                "mean_luminance": None, "dark_fraction": None, "bright_fraction": None,
+                "laplacian_variance": None, "dhash64": None, "flags": ["decode_failed"]}
+
+
+def compare_pair(a, b):
+    ah, bh = a["technical"]["dhash64"], b["technical"]["dhash64"]
+    distance = None if ah is None or bh is None else (int(ah, 16) ^ int(bh, 16)).bit_count()
+    if a["sha256"] == b["sha256"]:
+        signal = "exact_duplicate"
+    elif distance is None:
+        signal = "needs_human_review"
+    else:
+        signal = ("near_duplicate_candidate" if distance <= 6 else
+                  "borderline_visual_pair" if distance <= 10 else "no_algorithmic_signal")
+    return {"pair_id": a["id"] + "-" + b["id"], "left": a["id"], "right": b["id"],
+            "hamming_distance": distance, "signal": signal}
+
+
+def analyze(source, class_manifest=CLASS_MANIFEST):
+    before, records, classes = reconcile(source, class_manifest)
+    for record in records:
+        raw = read_file(Path(source) / record["stored_path"])
+        require(sha(raw) == record["sha256"], "image_changed_before_decode")
+        record["technical"] = metrics(raw)
+    pairs = [compare_pair(a, b) for a, b in combinations(records, 2)]
+    require(len(pairs) == 136, "pair_count")
+    require(tree_hashes(source) == before, "source_changed")
+    return {"schema_version": 1, "run_id": RUN, "method": METHOD,
+            "python": platform.python_version(), "source_hashes": before,
+            "classes": classes, "records": records, "pairs": pairs,
+            "comparison_count": 136, "training_sufficiency": "not_demonstrated"}
+
+
+def validate_decisions(value, analysis, *, draft=False):
+    obj(value, {"schema_version", "run_id", "analysis_sha256", "authority", "decisions"})
+    require(type(value["schema_version"]) is int and value["schema_version"] == 1, "decision_schema")
+    require(value["run_id"] == RUN and value["analysis_sha256"] == sha(encode(analysis)), "decision_analysis")
+    require(value["authority"] == ("agent_proposal" if draft else "human"), "human_authority_required")
+    entries = value["decisions"]
+    require(type(entries) is list and len(entries) == 17, "decision_count")
+    fields = {"id", "review_id", "sha256", "class_id", "state", "reviewer_id", "reviewer_role",
+              "timestamp", "rationale", "visual", "privacy", "botanical", "gates",
+              "pair_reviews", "duplicate_of", "original_resolution_review"}
+    result = []
+    for index, d in enumerate(sorted(entries, key=lambda x: x.get("id", ""))):
+        obj(d, fields)
+        record = analysis["records"][index]
+        require(all(d[k] == record[k] for k in ("id", "review_id", "sha256", "class_id")), "decision_identity")
+        require(type(d["state"]) is str and d["state"] in STATES, "decision_state")
+        require(d["reviewer_role"] == ("agent" if draft else "human"), "reviewer_role")
+        for key in ("reviewer_id", "timestamp", "rationale"):
+            text(d[key])
+        try:
+            stamp = datetime.fromisoformat(d["timestamp"])
+            require(stamp.utcoffset() is not None, "timestamp_timezone")
+        except ValueError:
+            raise CurationError("timestamp") from None
+        require(type(d["original_resolution_review"]) is bool, "original_review_type")
+        obj(d["visual"], VISUAL)
+        for v in d["visual"].values():
+            text(v)
+        obj(d["privacy"], {*PRIVACY, "assessment"})
+        for key in PRIVACY:
+            require(d["privacy"][key] in {"not_observed", "present", "uncertain"}, "privacy_value")
+        text(d["privacy"]["assessment"])
+        obj(d["botanical"], {"status", "evidence", "expert_confirmation"})
+        require(d["botanical"]["status"] in {"sufficient", "insufficient", "incompatible"}, "botanical_status")
+        text(d["botanical"]["evidence"])
+        require(type(d["botanical"]["expert_confirmation"]) is bool, "botanical_type")
+        obj(d["gates"], GATES)
+        require(all(type(v) is str and v in {"sufficient", "insufficient", "pending"}
+                    for v in d["gates"].values()), "gate_values")
+        applicable = {p["pair_id"] for p in analysis["pairs"] if d["id"] in (p["left"], p["right"])
+                      and p["signal"] != "no_algorithmic_signal"}
+        require(type(d["pair_reviews"]) is list, "pair_reviews")
+        possible = {p["pair_id"] for p in analysis["pairs"] if d["id"] in (p["left"], p["right"])}
+        reviewed = set()
+        for p in d["pair_reviews"]:
+            obj(p, {"pair_id", "outcome", "rationale"})
+            require(p["pair_id"] in possible and p["pair_id"] not in reviewed, "pair_review_set")
+            reviewed.add(p["pair_id"])
+            require(p["outcome"] in {"distinct", "duplicate", "pending"}, "pair_outcome")
+            text(p["rationale"])
+        require(applicable <= reviewed, "missing_pair_review")
+        require(d["duplicate_of"] is None or (d["duplicate_of"] in IDS and d["duplicate_of"] != d["id"]), "duplicate_reference")
+        if d["state"] == "approved_for_dataset":
+            require(not draft, "no_agent_approval")
+            require(d["original_resolution_review"] and record["technical"]["decode"] == "ok", "approval_decode_review")
+            require(all(v == "sufficient" for v in d["gates"].values()) and
+                    d["botanical"]["status"] == "sufficient", "approval_gates")
+            require(all(d["privacy"][k] == "not_observed" for k in PRIVACY), "approval_privacy")
+            require(all(p["outcome"] == "distinct" for p in d["pair_reviews"]), "approval_pairs")
+        if d["state"] == "rejected_duplicate":
+            require(d["duplicate_of"] is not None, "duplicate_reference_required")
+            pair_id = "-".join(sorted((d["id"], d["duplicate_of"])))
+            require(d["gates"]["uniqueness"] == "insufficient" and
+                    any(p["pair_id"] == pair_id and p["outcome"] == "duplicate"
+                        for p in d["pair_reviews"]), "duplicate_pair_evidence")
+        else:
+            require(d["duplicate_of"] is None, "unexpected_duplicate_reference")
+        if d["state"] == "needs_botanical_review":
+            require(d["botanical"]["status"] == "insufficient", "botanical_pending")
+        if d["state"] == "rejected_quality":
+            require(d["gates"]["quality"] == "insufficient", "quality_rejection_evidence")
+        if d["state"] == "rejected_privacy":
+            require(d["gates"]["privacy"] == "insufficient" and
+                    any(d["privacy"][k] != "not_observed" for k in PRIVACY), "privacy_rejection_evidence")
+        if d["state"] == "rejected_label":
+            require(d["gates"]["botanical_label"] == "insufficient" and
+                    d["botanical"]["status"] == "incompatible", "label_rejection_evidence")
+        if d["state"] == "needs_human_review":
+            require("pending" in d["gates"].values(), "human_pending_reason")
+        result.append(d)
+    by_id = {d["id"]: d for d in result}
+    for d in result:
+        if d["state"] == "rejected_duplicate":
+            require(by_id[d["duplicate_of"]]["state"] in
+                    {"approved_for_dataset", "needs_botanical_review", "needs_human_review"}, "duplicate_keeper")
+        for p in d["pair_reviews"]:
+            other = next(q for q in p["pair_id"].split("-") if q != d["id"])
+            peer = next((x for x in by_id[other]["pair_reviews"] if x["pair_id"] == p["pair_id"]), None)
+            require(peer is not None and peer["outcome"] == p["outcome"], "inconsistent_pair_reviews")
+    return result
+
+
+def curate(analysis, decisions, *, draft=False):
+    checked = validate_decisions(decisions, analysis, draft=draft)
+    records = [{**r, "review": d} for r, d in zip(analysis["records"], checked)]
+    counts = {s: sum(d["state"] == s for d in checked) for s in STATES}
+    coverage = []
+    for c in analysis["classes"]:
+        selected = [d for d in checked if d["class_id"] == c["class_id"]]
+        coverage.append({**c, "candidates": len(selected), "approved": sum(d["state"] == "approved_for_dataset" for d in selected),
+                         "rejected": sum(d["state"].startswith("rejected_") for d in selected),
+                         "pending": sum(d["state"].startswith("needs_") for d in selected)})
+    return {"schema_version": 1, "run_id": RUN, "stage": "agent_proposals_pending_human" if draft else "human_decisions_recorded",
+            "analysis_sha256": sha(encode(analysis)), "decisions_sha256": sha(encode(decisions)),
+            "source_hashes": analysis["source_hashes"], "method": analysis["method"], "python": analysis["python"],
+            "records": records, "pairs": analysis["pairs"], "comparison_count": len(analysis["pairs"]),
+            "counts": counts, "coverage": coverage,
+            "classes_without_candidates": [c["class_id"] for c in coverage if c["candidates"] == 0],
+            "classes_without_approved": [c["class_id"] for c in coverage if c["approved"] == 0],
+            "training_sufficiency": "not_demonstrated", "training_authorized": False,
+            "final_bytes_human_acceptance": "pending"}
+
+
+def summary(curation):
+    """Only closed, validated identifiers/enums/counts: never copy prose or provenance."""
+    return {k: curation[k] for k in ("schema_version", "stage", "counts", "comparison_count", "coverage",
+            "classes_without_candidates", "classes_without_approved", "training_sufficiency", "training_authorized")} | {
+            "records": [{"id": r["id"], "review_id": r["review_id"], "sha256": r["sha256"],
+                         "class_id": r["class_id"], "state": r["review"]["state"]} for r in curation["records"]]}
+
+
+def report(curation):
+    lines = ["# P07 — pareceres de curadoria", "", "Stage: " + curation["stage"], "",
+             "Zero aprovações é válido. Suficiência para treinamento não demonstrada; treinamento não autorizado.",
+             "Pareceres do agente exigem aceite humano. Não constituem perícia botânica.", "",
+             f"Comparações: {curation['comparison_count']}; contagens: {json.dumps({state: curation['counts'][state] for state in STATES})}", ""]
+    for r in curation["records"]:
+        lines += ["## " + r["id"], "", "```json", encode(r).decode().rstrip(), "```", ""]
+    return ("\n".join(lines) + "\n").encode()
+
+
+@contextmanager
+def output_lock(output, source):
+    output, source = no_symlinks(output), no_symlinks(source)
+    require(output != source and source not in output.parents and output not in source.parents, "output_source_overlap")
+    require(not any((p / ".git").is_file() or (p / ".git/HEAD").is_file() for p in (output, *output.parents)), "output_inside_git")
+    output.mkdir(parents=True, exist_ok=True)
+    lock_path = no_symlinks(output / ".p07.lock")
+    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
+    with os.fdopen(fd, "a+b") as lock:
+        try:
+            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
+        except BlockingIOError:
+            raise CurationError("output_locked") from None
+        try:
+            yield output
+        finally:
+            fcntl.flock(lock, fcntl.LOCK_UN)
+
+
+def persist(output, files):
+    # Precheck ALL targets before replacing any. Never silently change prior bytes.
+    for name, raw in files.items():
+        target = no_symlinks(output / name)
+        require(not target.exists() or read_file(target) == raw, "output_conflict_new_version_required")
+    for name, raw in files.items():
+        target = output / name
+        if target.exists():
+            continue
+        fd, temporary = tempfile.mkstemp(prefix=".p07-", dir=output)
+        try:
+            with os.fdopen(fd, "wb") as stream:
+                stream.write(raw)
+                stream.flush()
+                os.fsync(stream.fileno())
+            os.replace(temporary, target)
+        finally:
+            if os.path.exists(temporary):
+                os.unlink(temporary)
+    fd = os.open(output, os.O_RDONLY | os.O_DIRECTORY)
+    try:
+        os.fsync(fd)
+    finally:
+        os.close(fd)
+
+
+def run(source, output, *, decisions_path=None, draft=False, class_manifest=CLASS_MANIFEST):
+    with output_lock(output, source) as destination:
+        analysis = analyze(source, class_manifest)
+        files = {"analysis.json": encode(analysis)}
+        if decisions_path is not None:
+            decisions_raw = read_file(decisions_path)
+            decisions = strict_load(decisions_raw)
+            result = curate(analysis, decisions, draft=draft)
+            suffix = ".draft" if draft else ""
+            files.update({f"curation{suffix}.json": encode(result), f"report{suffix}.md": report(result),
+                          f"summary{suffix}.json": encode(summary(result))})
+            require(read_file(decisions_path) == decisions_raw, "decisions_changed")
+        require(tree_hashes(source) == analysis["source_hashes"], "source_changed_before_publish")
+        persist(destination, files)
+        return {"images": 17, "comparisons": 136, "mode": "analyze" if decisions_path is None else
+                ("agent_draft" if draft else "human_finalization"), "files": sorted(files)}
+
+
+def main(argv=None):
+    parser = argparse.ArgumentParser(description=__doc__)
+    parser.add_argument("--source", required=True, type=Path)
+    parser.add_argument("--output", required=True, type=Path)
+    mode = parser.add_mutually_exclusive_group(required=True)
+    mode.add_argument("--analyze-only", action="store_true")
+    mode.add_argument("--finalize", action="store_true")
+    mode.add_argument("--review-draft", action="store_true")
+    parser.add_argument("--decisions", type=Path)
+    args = parser.parse_args(argv)
+    if bool(args.decisions) != (args.finalize or args.review_draft):
+        parser.error("decisions required only for finalize/review-draft")
+    try:
+        result = run(args.source, args.output, decisions_path=args.decisions, draft=args.review_draft)
+    except (CurationError, OSError, KeyError, TypeError, UnicodeError) as error:
+        print(json.dumps({"error": str(error) if isinstance(error, CurationError) else "invalid_or_inaccessible_input"}), file=sys.stderr)
+        return 2
+    print(json.dumps(result, sort_keys=True))
+    return 0
+
+
+if __name__ == "__main__":
+    raise SystemExit(main())
diff --git a/scripts/phase1/test_curate_p07.py b/scripts/phase1/test_curate_p07.py
new file mode 100644
index 0000000..43206fd
--- /dev/null
+++ b/scripts/phase1/test_curate_p07.py
@@ -0,0 +1,476 @@
+"""P07 public seams; synthetic images only, no external corpus or network."""
+from copy import deepcopy
+from io import BytesIO
+import json
+from pathlib import Path
+import tempfile
+import unittest
+from unittest.mock import patch
+
+from PIL import Image
+import curate_p07 as c
+
+
+def jpeg(value):
+    out = BytesIO()
+    Image.new("RGB", (24, 16), (value * 10, value * 5, value * 3)).save(out, format="JPEG")
+    return out.getvalue()
+
+
+def source_fixture(root):
+    root.mkdir()
+    (root / "quarantine").mkdir()
+    (root / "review-2026-09-28").mkdir()
+    classes = json.loads(c.CLASS_MANIFEST.read_text())["classes"]
+    records, decisions = [], []
+    for i in range(1, 18):
+        raw = jpeg(i)
+        digest = c.sha(raw)
+        stored = f"quarantine/{digest}.jpg"
+        (root / stored).write_bytes(raw)
+        record = dict.fromkeys(c.RECORD_KEYS, "synthetic")
+        record.update(sequence=i, result="accepted", sha256=digest, class_id="species_01",
+                      stored_path=stored, botanical_validation_performed=False,
+                      visual_review_performed=False)
+        records.append(record)
+        d = dict.fromkeys(c.P06_DECISION_KEYS, False)
+        d.update(decision_id=f"Q{i:02}", review_id=f"R{i:02}", sha256=digest, class_id="species_01",
+                 decision="aprovar_para_curadoria_futura", stored_path=stored, physical_location="quarantine")
+        decisions.append(d)
+    manifest = b"".join((json.dumps(r, sort_keys=True) + "\n").encode() for r in records)
+    (root / "manifest.jsonl").write_bytes(manifest)
+    canonical_sha = c.sha(c.CLASS_MANIFEST.read_bytes())
+    write = lambda name, value: (root / name).write_bytes(c.encode(value))
+    write("state.json", {"schema_version": 1, "records": records, "canonical_manifest_sha256": canonical_sha,
+                         "searches": {x["class_id"]: {"continuation": None, "exhausted": False,
+                                      "pages_fetched": 1, "status": "finished"} for x in classes}})
+    cv = []
+    for x in classes:
+        v = dict.fromkeys("accepted class_id consulted deferred deferred_reasons failure_reasons failures name pages_fetched quarantined query reasons rejected status usable".split(), 0)
+        v.update(class_id=x["class_id"], accepted=17 if x["class_id"] == "species_01" else 0,
+                 quarantined=17 if x["class_id"] == "species_01" else 0)
+        cv.append(v)
+    coverage = dict.fromkeys("accepted_cap_per_class accepted_semantics canonical_manifest_sha256 classes failure_count_semantics manifest_jsonl_sha256 page_budget_per_class_per_run schema_version status training_ready visual_review_performed".split(), 0)
+    coverage.update(canonical_manifest_sha256=canonical_sha, classes=cv, manifest_jsonl_sha256=c.sha(manifest),
+                    training_ready=False)
+    write("coverage.json", coverage)
+    prior = dict.fromkeys("confirmation_source decisions human_grouped_decision_confirmed notice p06_status recorded_at release_status remote_metadata_requeried review_method run_id schema_version totals training_ready".split(), "fixture")
+    prior.update(decisions=decisions, run_id=c.RUN, human_grouped_decision_confirmed=True, training_ready=False,
+                 totals={"aprovar_para_curadoria_futura": 17})
+    write("review-2026-09-28/human-decisions.json", prior)
+    write("run-metadata.json", {"run_id": c.RUN, "totals": {"accepted": 17}})
+    rehash(root)
+
+
+def rehash(root):
+    inventory = [{"path": str(p.relative_to(root)), "sha256": c.sha(p.read_bytes()), "bytes": p.stat().st_size}
+                 for p in sorted(root.rglob("*")) if p.is_file() and p.name not in {"inventory.json", "SHA256SUMS"}]
+    (root / "inventory.json").write_bytes(c.encode(inventory))
+    lines = [f"{c.sha(p.read_bytes())}  {p.relative_to(root)}\n" for p in sorted(root.rglob("*"))
+             if p.is_file() and p.name != "SHA256SUMS"]
+    (root / "SHA256SUMS").write_text("".join(lines))
+
+
+def decisions_for(analysis, draft=False):
+    decisions = []
+    for r in analysis["records"]:
+        d = {k: r[k] for k in ("id", "review_id", "sha256", "class_id")}
+        d.update(state="needs_botanical_review", reviewer_id="synthetic-reviewer",
+                 reviewer_role="agent" if draft else "human", timestamp="2026-09-30T12:00:00+00:00",
+                 rationale="Insufficient species evidence", original_resolution_review=True,
+                 visual=dict.fromkeys(c.VISUAL, "Synthetic observation"),
+                 privacy={**dict.fromkeys(c.PRIVACY, "not_observed"), "assessment": "Synthetic privacy review"},
+                 botanical={"status": "insufficient", "evidence": "No taxonomic evidence", "expert_confirmation": False},
+                 gates=dict.fromkeys(c.GATES, "pending"), duplicate_of=None,
+                 pair_reviews=[{"pair_id": p["pair_id"], "outcome": "pending", "rationale": "Collision review pending"}
+                               for p in analysis["pairs"] if r["id"] in (p["left"], p["right"])
+                               and p["signal"] != "no_algorithmic_signal"])
+        decisions.append(d)
+    return {"schema_version": 1, "run_id": c.RUN, "analysis_sha256": c.sha(c.encode(analysis)),
+            "authority": "agent_proposal" if draft else "human", "decisions": decisions}
+
+
+class MetricsTests(unittest.TestCase):
+    def test_invalid_decoder(self):
+        self.assertEqual(c.metrics(b"not an image")["decode"], "failed")
+
+    def test_mpo_and_non_jpeg_not_accepted(self):
+        out = BytesIO()
+        Image.new("RGB", (10, 10)).save(out, format="PNG")
+        self.assertEqual(c.metrics(out.getvalue())["decode"], "failed")
+
+    def test_dimensions_flat_luminance_and_laplacian(self):
+        m = c.metrics(jpeg(10))
+        self.assertEqual((m["width"], m["height"]), (24, 16))
+        self.assertEqual(m["laplacian_variance"], 0)
+        self.assertEqual(m["dhash64"], "0000000000000000")
+        self.assertIn("low_laplacian_variance", m["flags"])
+        self.assertNotIn("decision", m)
+
+    def test_signed_laplacian_known_values(self):
+        # 3x3 interiors of 5x5 checkerboard alternate +/-1020: population var.
+        pixels = [255 * ((x + y) % 2) for y in range(5) for x in range(5)]
+        expected = (9 * 1020**2 * 9 - 1020**2) / 81
+        self.assertEqual(c.laplacian_variance(pixels, 5, 5), expected)
+        self.assertEqual(c.laplacian_variance([7] * 25, 5, 5), 0)
+
+    def test_dhash_bit_order_and_strict_greater(self):
+        im = Image.new("L", (9, 8))
+        im.putdata([x * 20 for _ in range(8) for x in range(9)])
+        self.assertEqual(c.dhash(im), "ffffffffffffffff")
+        im.putdata([160 - x * 20 for _ in range(8) for x in range(9)])
+        self.assertEqual(c.dhash(im), "0000000000000000")
+        im.putdata([0, 255, 0, 0, 0, 0, 0, 0, 0] + [0] * 63)
+        self.assertEqual(c.dhash(im), "8000000000000000")
+
+    def test_near_duplicate_synthetic_bytes_different(self):
+        a, b = jpeg(10), jpeg(11)
+        self.assertNotEqual(c.sha(a), c.sha(b))
+        result = c.compare_pair({"id": "Q01", "sha256": c.sha(a), "technical": c.metrics(a)},
+                                {"id": "Q02", "sha256": c.sha(b), "technical": c.metrics(b)})
+        self.assertEqual(result["signal"], "near_duplicate_candidate")
+        self.assertEqual(result["hamming_distance"], 0)
+        self.assertNotIn("decision", result)
+
+    def test_exact_duplicate_precedes_perceptual_signal(self):
+        a = {"id": "Q01", "sha256": "same", "technical": {"dhash64": "0" * 16}}
+        b = {"id": "Q02", "sha256": "same", "technical": {"dhash64": "f" * 16}}
+        self.assertEqual(c.compare_pair(a, b)["signal"], "exact_duplicate")
+
+    def test_textured_near_duplicate_and_different_color_collision(self):
+        im = Image.new("RGB", (90, 80))
+        im.putdata([(x * 2, y * 2, (x + y) % 255) for y in range(80) for x in range(90)])
+        blobs = []
+        for quality in (90, 95):
+            stream = BytesIO()
+            im.save(stream, format="JPEG", quality=quality)
+            blobs.append(stream.getvalue())
+        self.assertNotEqual(c.sha(blobs[0]), c.sha(blobs[1]))
+        a, b = [dict(id=f"Q{i+1:02}", sha256=c.sha(raw), technical=c.metrics(raw)) for i, raw in enumerate(blobs)]
+        self.assertLessEqual(c.compare_pair(a, b)["hamming_distance"], 6)
+        self.assertEqual(c.dhash(Image.new("RGB", (20, 20), "red")),
+                         c.dhash(Image.new("RGB", (20, 20), "blue")))
+
+    def test_hamming_all_boundaries(self):
+        for distance, expected in [(0, "near_duplicate_candidate"), (6, "near_duplicate_candidate"),
+                                   (7, "borderline_visual_pair"), (10, "borderline_visual_pair"),
+                                   (11, "no_algorithmic_signal"), (64, "no_algorithmic_signal")]:
+            a = {"id": "Q01", "sha256": "a", "technical": {"dhash64": "0" * 16}}
+            b = {"id": "Q02", "sha256": "b", "technical": {"dhash64": f"{(1 << distance) - 1:016x}"}}
+            self.assertEqual(c.compare_pair(a, b)["signal"], expected)
+            self.assertEqual(c.compare_pair(a, b)["hamming_distance"], distance)
+
+    def test_missing_hash_is_human_review(self):
+        a = {"id": "Q01", "sha256": "a", "technical": {"dhash64": None}}
+        b = {"id": "Q02", "sha256": "b", "technical": {"dhash64": "0" * 16}}
+        self.assertEqual(c.compare_pair(a, b)["signal"], "needs_human_review")
+
+    def test_quality_boundary_operators(self):
+        self.assertEqual(c.flags_for(224, 672, 40, .249, .249, 100), [])
+        self.assertEqual(c.flags_for(224, 672, 215, .249, .249, 100), [])
+        self.assertIn("small_dimension", c.flags_for(223, 400, 100, 0, 0, 100))
+        self.assertIn("extreme_aspect", c.flags_for(224, 673, 100, 0, 0, 100))
+        for mean, flag in [(39.999, "dark_mean"), (215.001, "bright_mean")]:
+            self.assertIn(flag, c.flags_for(224, 224, mean, 0, 0, 100))
+        self.assertIn("dark_fraction", c.flags_for(224, 224, 100, .25, 0, 100))
+        self.assertIn("bright_fraction", c.flags_for(224, 224, 100, 0, .25, 100))
+        self.assertIn("low_laplacian_variance", c.flags_for(224, 224, 100, 0, 0, 99.999))
+
+    def test_exposure_pixel_thresholds(self):
+        for luminance, dark, bright in [(15, 1, 0), (16, 0, 0), (239, 0, 0), (240, 0, 1)]:
+            out = BytesIO()
+            Image.new("L", (256, 256), luminance).save(out, format="JPEG", quality=100)
+            m = c.metrics(out.getvalue())
+            self.assertEqual((m["dark_fraction"], m["bright_fraction"]), (dark, bright))
+
+
+class ReviewTests(unittest.TestCase):
+    @classmethod
+    def setUpClass(cls):
+        cls.tmp = tempfile.TemporaryDirectory()
+        cls.source = Path(cls.tmp.name) / "source"
+        source_fixture(cls.source)
+        cls.analysis = c.analyze(cls.source)
+
+    @classmethod
+    def tearDownClass(cls):
+        cls.tmp.cleanup()
+
+    def test_all_136_unique_pairs_no_decisions(self):
+        a = self.analysis
+        self.assertEqual(len(a["records"]), 17)
+        self.assertEqual(len({p["pair_id"] for p in a["pairs"]}), 136)
+        self.assertEqual([r["id"] for r in a["records"]], c.IDS)
+        self.assertTrue(all("decision" not in r for r in a["records"]))
+
+    def test_zero_approved_human_reviews_are_valid(self):
+        out = c.curate(self.analysis, decisions_for(self.analysis))
+        self.assertEqual(out["counts"]["needs_botanical_review"], 17)
+        self.assertEqual(out["counts"]["approved_for_dataset"], 0)
+        self.assertFalse(out["training_authorized"])
+        self.assertEqual(len(out["classes_without_approved"]), 14)
+
+    def test_agent_draft_explicit_and_cannot_finalize(self):
+        decisions = decisions_for(self.analysis, True)
+        out = c.curate(self.analysis, decisions, draft=True)
+        self.assertEqual(out["stage"], "agent_proposals_pending_human")
+        with self.assertRaisesRegex(c.CurationError, "human_authority_required"):
+            c.curate(self.analysis, decisions)
+
+    def test_agent_never_approves(self):
+        d = decisions_for(self.analysis, True)
+        d["decisions"][0]["state"] = "approved_for_dataset"
+        with self.assertRaisesRegex(c.CurationError, "no_agent_approval"):
+            c.curate(self.analysis, d, draft=True)
+
+    def test_approval_requires_botanical_quality_privacy_pairs(self):
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["state"] = "approved_for_dataset"
+        with self.assertRaises(c.CurationError):
+            c.curate(self.analysis, d)
+        for x in d["decisions"]:
+            x["gates"] = dict.fromkeys(c.GATES, "sufficient")
+            x["botanical"]["status"] = "sufficient"
+            x["state"] = "approved_for_dataset"
+            for p in x["pair_reviews"]:
+                p["outcome"] = "distinct"
+        self.assertEqual(c.curate(self.analysis, d)["counts"]["approved_for_dataset"], 17)
+        for key in c.GATES:
+            bad = deepcopy(d)
+            bad["decisions"][0]["gates"][key] = "pending"
+            with self.assertRaises(c.CurationError):
+                c.curate(self.analysis, bad)
+        bad = deepcopy(d)
+        bad["decisions"][0]["privacy"]["faces"] = "uncertain"
+        with self.assertRaises(c.CurationError):
+            c.curate(self.analysis, bad)
+
+    def test_no_p06_auto_promotion(self):
+        out = c.curate(self.analysis, decisions_for(self.analysis))
+        self.assertTrue(all(r["prior_p06_decision"] == "aprovar_para_curadoria_futura" for r in out["records"]))
+        self.assertEqual(out["counts"]["approved_for_dataset"], 0)
+
+    def test_decision_fields_identity_and_types(self):
+        for key, value in [("id", "Q02"), ("review_id", "R02"), ("sha256", "a" * 64),
+                           ("class_id", "species_02"), ("state", "approved"),
+                           ("reviewer_role", "agent"), ("timestamp", "2026-09-30T00:00:00"),
+                           ("rationale", ""), ("original_resolution_review", "true")]:
+            with self.subTest(key=key):
+                d = decisions_for(self.analysis)
+                d["decisions"][0][key] = value
+                with self.assertRaises(c.CurationError):
+                    c.curate(self.analysis, d)
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["unknown"] = 1
+        with self.assertRaises(c.CurationError):
+            c.curate(self.analysis, d)
+
+    def test_missing_or_duplicate_decision(self):
+        for mutation in (lambda d: d["decisions"].pop(),
+                         lambda d: d["decisions"].__setitem__(1, d["decisions"][0])):
+            d = decisions_for(self.analysis)
+            mutation(d)
+            with self.assertRaises(c.CurationError):
+                c.curate(self.analysis, d)
+
+    def test_missing_and_inconsistent_pair_reviews(self):
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["pair_reviews"].pop()
+        with self.assertRaisesRegex(c.CurationError, "missing_pair_review"):
+            c.curate(self.analysis, d)
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["pair_reviews"][0]["outcome"] = "distinct"
+        with self.assertRaisesRegex(c.CurationError, "inconsistent_pair_reviews"):
+            c.curate(self.analysis, d)
+
+    def test_report_roundtrip_is_byte_identical(self):
+        result = c.curate(self.analysis, decisions_for(self.analysis))
+        self.assertEqual(c.report(result), c.report(c.strict_load(c.encode(result))))
+
+    def test_duplicate_rejection_requires_explicit_pair_decision(self):
+        d = decisions_for(self.analysis)
+        d["decisions"][0].update(state="rejected_duplicate", duplicate_of="Q02")
+        with self.assertRaisesRegex(c.CurationError, "duplicate_pair_evidence"):
+            c.curate(self.analysis, d)
+
+    def test_duplicate_rejection_requires_keeper(self):
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["state"] = "rejected_duplicate"
+        with self.assertRaisesRegex(c.CurationError, "duplicate_reference_required"):
+            c.curate(self.analysis, d)
+        d["decisions"][0]["duplicate_of"] = "Q02"
+        d["decisions"][0]["gates"]["uniqueness"] = "insufficient"
+        for entry in d["decisions"][:2]:
+            next(p for p in entry["pair_reviews"] if p["pair_id"] == "Q01-Q02")["outcome"] = "duplicate"
+        self.assertEqual(c.curate(self.analysis, d)["counts"]["rejected_duplicate"], 1)
+        d["decisions"][1]["state"] = "rejected_quality"
+        d["decisions"][1]["gates"]["quality"] = "insufficient"
+        with self.assertRaisesRegex(c.CurationError, "duplicate_keeper"):
+            c.curate(self.analysis, d)
+
+    def test_manual_pair_without_algorithmic_signal_is_reviewable(self):
+        a = deepcopy(self.analysis)
+        for p in a["pairs"]:
+            p["signal"] = "no_algorithmic_signal"
+        d = decisions_for(a)
+        pair = {"pair_id": "Q01-Q02", "outcome": "pending", "rationale": "Visual scene overlap"}
+        d["decisions"][0]["pair_reviews"] = [pair]
+        d["decisions"][1]["pair_reviews"] = [deepcopy(pair)]
+        self.assertEqual(c.curate(a, d)["counts"]["needs_botanical_review"], 17)
+        d["decisions"][1]["pair_reviews"] = []
+        with self.assertRaisesRegex(c.CurationError, "inconsistent_pair_reviews"):
+            c.curate(a, d)
+
+    def test_rejected_label_and_privacy_need_matching_evidence(self):
+        for state in ("rejected_quality", "rejected_label", "rejected_privacy"):
+            d = decisions_for(self.analysis)
+            d["decisions"][0]["state"] = state
+            with self.assertRaises(c.CurationError):
+                c.curate(self.analysis, d)
+
+    def test_summary_excludes_private_text_and_origin(self):
+        d = decisions_for(self.analysis)
+        d["decisions"][0]["rationale"] = "PRIVATE_SENTINEL [REDACTED EMAIL] plate123"
+        result = c.curate(self.analysis, d)
+        raw = c.encode(c.summary(result))
+        for secret in (b"PRIVATE_SENTINEL", b"email@", b"plate123", b"provenance", b"reviewer_id", b"synthetic-reviewer"):
+            self.assertNotIn(secret, raw)
+        self.assertEqual(set(c.summary(result)["records"][0]), {"id", "review_id", "sha256", "class_id", "state"})
+
+
+class PersistenceTests(unittest.TestCase):
+    def setUp(self):
+        self.temp = tempfile.TemporaryDirectory()
+        self.addCleanup(self.temp.cleanup)
+        self.root = Path(self.temp.name)
+        self.source = self.root / "source"
+        self.output = self.root / "output"
+        source_fixture(self.source)
+
+    def test_analysis_then_human_finalize_idempotent(self):
+        before = c.tree_hashes(self.source)
+        c.run(self.source, self.output)
+        a = c.strict_load((self.output / "analysis.json").read_bytes())
+        decisions = self.output / "human-decisions.json"
+        decisions.write_bytes(c.encode(decisions_for(a)))
+        c.run(self.source, self.output, decisions_path=decisions)
+        first = c.tree_hashes(self.output)
+        mtimes = {p: (self.output / p).stat().st_mtime_ns for p in first}
+        c.run(self.source, self.output, decisions_path=decisions)
+        self.assertEqual(first, c.tree_hashes(self.output))
+        self.assertEqual(mtimes, {p: (self.output / p).stat().st_mtime_ns for p in first})
+        self.assertEqual(before, c.tree_hashes(self.source))
+
+    def test_draft_does_not_create_final_files(self):
+        c.run(self.source, self.output)
+        a = c.strict_load((self.output / "analysis.json").read_bytes())
+        d = self.output / "human-decisions.json"
+        d.write_bytes(c.encode(decisions_for(a, True)))
+        c.run(self.source, self.output, decisions_path=d, draft=True)
+        self.assertTrue((self.output / "curation.draft.json").exists())
+        self.assertFalse((self.output / "curation.json").exists())
+        with self.assertRaises(c.CurationError):
+            c.run(self.source, self.output, decisions_path=d)
+
+    def test_modified_image_missing_extra_symlink_block(self):
+        image = next((self.source / "quarantine").iterdir())
+        old = image.read_bytes()
+        image.write_bytes(old + b"modified")
+        with self.assertRaises(c.CurationError):
+            c.run(self.source, self.output)
+        image.write_bytes(old)
+        extra = self.source / "quarantine/extra.jpg"
+        extra.write_bytes(old)
+        rehash(self.source)
+        with self.assertRaisesRegex(c.CurationError, "image_set_17"):
+            c.run(self.source, self.output)
+        extra.unlink()
+        image.unlink()
+        with self.assertRaises(c.CurationError):
+            c.run(self.source, self.output)
+        image.symlink_to(self.source / "manifest.jsonl")
+        with self.assertRaisesRegex(c.CurationError, "symlink"):
+            c.run(self.source, self.output)
+        self.assertFalse((self.output / "analysis.json").exists())
+
+    def test_state_manifest_mismatch_even_with_updated_checksums(self):
+        state = c.strict_load((self.source / "state.json").read_bytes())
+        state["records"][0]["class_id"] = "species_02"
+        (self.source / "state.json").write_bytes(c.encode(state))
+        rehash(self.source)
+        with self.assertRaisesRegex(c.CurationError, "state_manifest_mismatch"):
+            c.analyze(self.source)
+
+    def test_qr_mapping_error(self):
+        p = self.source / "review-2026-09-28/human-decisions.json"
+        d = c.strict_load(p.read_bytes())
+        d["decisions"][0]["review_id"] = "R02"
+        p.write_bytes(c.encode(d))
+        rehash(self.source)
+        with self.assertRaisesRegex(c.CurationError, "qr_mapping"):
+            c.analyze(self.source)
+
+    def test_source_change_during_decode_no_output(self):
+        original = c.metrics
+        def mutate(raw):
+            value = original(raw)
+            (self.source / "unexpected").write_text("change")
+            return value
+        with patch.object(c, "metrics", side_effect=mutate):
+            with self.assertRaisesRegex(c.CurationError, "source_changed"):
+                c.run(self.source, self.output)
+        self.assertFalse((self.output / "analysis.json").exists())
+
+    def test_output_conflict_preserves_previous_result(self):
+        self.output.mkdir()
+        (self.output / "b").write_bytes(b"old")
+        with self.assertRaisesRegex(c.CurationError, "output_conflict"):
+            c.persist(self.output, {"a": b"new", "b": b"different"})
+        self.assertEqual((self.output / "b").read_bytes(), b"old")
+        self.assertFalse((self.output / "a").exists())
+
+    def test_lock_excludes_concurrent_writer(self):
+        with c.output_lock(self.output, self.source):
+            with self.assertRaisesRegex(c.CurationError, "output_locked"):
+                with c.output_lock(self.output, self.source):
+                    self.fail("lock accepted")
+
+    def test_output_cannot_be_source_or_git_or_symlink(self):
+        for p in (self.source, self.source / "child", self.root):
+            with self.assertRaises(c.CurationError):
+                with c.output_lock(p, self.source):
+                    self.fail("overlap accepted")
+        repo = self.root / "fake-git"
+        repo.mkdir()
+        (repo / ".git").mkdir()
+        (repo / ".git/HEAD").write_text("ref: refs/heads/test\n")
+        with self.assertRaisesRegex(c.CurationError, "output_inside_git"):
+            with c.output_lock(repo / "outputs", self.source):
+                self.fail("git accepted")
+        self.output.symlink_to(repo, target_is_directory=True)
+        with self.assertRaisesRegex(c.CurationError, "symlink"):
+            with c.output_lock(self.output, self.source):
+                self.fail("symlink accepted")
+
+    def test_unknown_state_field_fails_closed(self):
+        path = self.source / "state.json"
+        state = c.strict_load(path.read_bytes())
+        state["unknown"] = 1
+        path.write_bytes(c.encode(state))
+        rehash(self.source)
+        with self.assertRaisesRegex(c.CurationError, "object_fields"):
+            c.analyze(self.source)
+
+
+class StrictJSONTests(unittest.TestCase):
+    def test_reject_nonfinite_duplicate_encoding_and_coercion(self):
+        for raw in (b'{"a":1,"a":2}\n', b'{"a":NaN}\n', b'{"a":Infinity}\n', b'{"a":1e999}\n',
+                    b'{}\r\n', b'{}', b'\xef\xbb\xbf{}\n', b'\xff\n'):
+            with self.subTest(raw=raw), self.assertRaises(c.CurationError):
+                c.strict_load(raw)
+        self.assertEqual(c.strict_load(b'{"a":true}\n'), {"a": True})
+        self.assertEqual(c.strict_load(c.encode({"v": "á"})), {"v": "á"})
+
+
+if __name__ == "__main__":
+    unittest.main()
```
