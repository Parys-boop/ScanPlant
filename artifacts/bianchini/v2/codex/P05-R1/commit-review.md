# Review Package

- Base: `c7012b942c36fe93fb136a376a1a73093f1e5aaa`
- Head: `42559189f4d3dcbdec192fecaac2c06e2a0fd31b`
- Brief: `artifacts/bianchini/v2/codex/P05-R1/task-brief.md` (a2d2098a903af653572d1dc9145f60f5972c6bca641806cfd08bce1d4228d45a)
- Report: `artifacts/bianchini/v2/codex/P05-R1/implementation-report.md` (94952c02302af34e1444e3ecb938787c1a2f710bde7b7920623779e4cb06a0cf)
- Security notice: sanitização heurística; 0 ocorrência(s) removida(s). Revise antes de compartilhar.

## Commits

```text
4255918 feat(p05-r1): quarantine ambiguous aliases
```

## Stat

```text
.../bianchini/v2/codex/P05-R1/FINAL_REVIEW.md      |   77 +
 .../v2/codex/P05-R1/baseline-findings.json         |   19 +
 .../codex/P05-R1/baseline-implementation-report.md |   12 +
 .../bianchini/v2/codex/P05-R1/baseline-review.md   |   25 +
 .../bianchini/v2/codex/P05-R1/checkpoint.json      |  141 ++
 .../v2/codex/P05-R1/closure-verification.json      |  317 ++++
 .../bianchini/v2/codex/P05-R1/commit-findings.json |    3 +
 .../bianchini/v2/codex/P05-R1/commit-review.md     |    7 +
 .../v2/codex/P05-R1/human-acceptance.json          |   33 +
 .../v2/codex/P05-R1/implementation-report.md       |   50 +
 artifacts/bianchini/v2/codex/P05-R1/task-brief.md  |  102 ++
 .../v2/codex/convergence/P05-R1/.proofs/T1.json    |   33 +
 .../codex/convergence/P05-R1/.proofs/T1.json.lock  |    0
 .../bianchini/v2/codex/convergence/P05-R1/T1.json  |   88 +
 .../v2/codex/convergence/P05-R1/T1.json.bak        |   75 +
 .../bianchini/v2/evidence/P05-f1-man01/SHA256SUMS  |   12 +-
 .../v2/evidence/P05-f1-man01/taxonomy-review.md    |  173 +-
 .../evidence/P05-f1-man01/validation-report.json   | 1897 +++++++++-----------
 artifacts/bianchini/v2/ledgers/P05.md              |  107 ++
 docs/living/PROJECT_STATE.md                       |   34 +-
 docs/phase1/F1-MAN01-offline-class-manifest.md     |   50 +-
 docs/phase1/offline-class-manifest.v1.json         |   26 +-
 scripts/phase1/test_offline_manifest.py            |  167 +-
 scripts/phase1/validate_offline_manifest.py        |   13 +-
 24 files changed, 2301 insertions(+), 1160 deletions(-)
```

## Diff

```diff
diff --git a/artifacts/bianchini/v2/codex/P05-R1/FINAL_REVIEW.md b/artifacts/bianchini/v2/codex/P05-R1/FINAL_REVIEW.md
new file mode 100644
index 0000000..dd24481
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/FINAL_REVIEW.md
@@ -0,0 +1,77 @@
+# Revisão humana dos bytes finais — P05-R1 / U-201
+
+Status: pending. Nenhum aceite de bytes finais atribuído ao responsável.
+
+## Commit local de aprovação
+
+`c7012b942c36fe93fb136a376a1a73093f1e5aaa` — chore(p05-r1): approve alias quarantine plan.
+Árvore limpa após commit; 14 arquivos de planejamento/aprovação, nenhum de implementação:
+
+- `artifacts/bianchini/v2/approval/manifest-p05-r1.sha256`
+- `artifacts/bianchini/v2/ledgers/P05.md`
+- `artifacts/bianchini/v2/planning/checker-p05-r1.jsonl`
+- `artifacts/bianchini/v2/planning/p05-r1-policy.json`
+- `artifacts/bianchini/v2/planning/p05-r1-preflight.json`
+- `docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md`
+- `docs/bianchini/changes/v2/READINESS-p05-r1.md`
+- `docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md`
+- `docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md`
+- `docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md`
+- `docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md`
+- `docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md`
+- `docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md`
+- `docs/living/PROJECT_STATE.md`
+
+## Resultado para aceite
+
+- Manifesto 1.1.0, schema/normalização 1, roster byte a byte preservado.
+- Quatro homônimos quarantined: Aloe maculata, Aloe variegata, Ficus clusiifolia e Ficus cordata.
+- Cada um retorna None/null, inclusive caixa/whitespace normalizados; reinserção é rejeitada.
+- Evidência mantém autoria relacionada, autoria/táxon conflitantes, fontes, motivo e estado.
+- Igualdade de conjuntos/mapeamentos: 83 preliminares menos quatro = 79 aliases; 12 canônicos;
+  91 chaves únicas, 14 classes na mesma ordem, proteções fora do namespace científico.
+- Nomes comuns, IDs, índices, definições e demais aliases preservados.
+- 94/94 testes passaram; 81 anteriores preservados, 13 novos, zero skips. CLI e 7/7 checksums OK.
+- Python 3.14.4 -B; diferença histórica 3.12.3 registrada, sem alterar contrato.
+- Fontes taxonômicas reutilizadas de 2026-09-11; nenhuma consulta nova.
+
+## Hashes dos sete artefatos
+
+| Arquivo | SHA-256 |
+|---|---|
+| `artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json` | `350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b` |
+| `artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md` | `272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23` |
+| `artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json` | `f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee` |
+| `docs/phase1/F1-MAN01-offline-class-manifest.md` | `adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24` |
+| `docs/phase1/offline-class-manifest.v1.json` | `bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c` |
+| `scripts/phase1/test_offline_manifest.py` | `88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe` |
+| `scripts/phase1/validate_offline_manifest.py` | `d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed` |
+
+SHA-256 do arquivo SHA256SUMS: `9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e`.
+Ele fixa conjuntamente os sete artefatos; verificação reproduzível na raiz:
+
+```bash
+sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
+```
+
+## Limites e estados
+
+Pacotes históricos preservados: P05
+`246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5`;
+P05-R1 `6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f`.
+A regra contratual está na spec/delta P05-R1 congelados. Sincronização de current/specs
+somente no encerramento regular do ciclo conforme o plano, sem release/homologação agora.
+
+Uma rodada de correção, zero redesigns. Sidecar
+`artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json` permanece fixing:
+B1 corrigido na working tree e formalmente aberto no baseline até prova do commit autorizado.
+Sem nova classificação stopped, sem aprovação de convergência simulada e sem replanejamento.
+
+P05 blocked; P05-R1 in_progress; U-201 aguardando aceite humano dos bytes. P01/P03-R6
+blocked-terminal, P02/P04 completed e release pending preservados. Implementação unstaged,
+sem commit de implementação, push, merge, providers ou alterações no worktree antigo/backup.
+
+## Decisão solicitada no único gate final
+
+Aceite humano dos bytes identificados por estes hashes e autorização de commit e push.
+Registrar a resposta por append; não editar retrospectivamente este pacote de bytes.
diff --git a/artifacts/bianchini/v2/codex/P05-R1/baseline-findings.json b/artifacts/bianchini/v2/codex/P05-R1/baseline-findings.json
new file mode 100644
index 0000000..53bc1b5
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/baseline-findings.json
@@ -0,0 +1,19 @@
+{
+  "findings": [
+    {
+      "id": "B1",
+      "severity": "important",
+      "disposition": "blocker",
+      "title": "Quatro homônimos ainda resolvem no baseline",
+      "approved_requirement": "retornar None para",
+      "root_cause": "Mapa científico não aplica a inelegibilidade authorless aprovada em P05-R1",
+      "proof_id": "proof-93c13d6b0c1affb7122f227180990597",
+      "material_impact": "Binômio comprovadamente ambíguo retorna class_id",
+      "reachable_scenario": "Chamar resolve_scientific_name com qualquer dos quatro homônimos no manifesto preliminar",
+      "risk_seam": "offline-manifest-contract",
+      "structural": false,
+      "structural_class": null,
+      "structural_evidence": null
+    }
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P05-R1/baseline-implementation-report.md b/artifacts/bianchini/v2/codex/P05-R1/baseline-implementation-report.md
new file mode 100644
index 0000000..5f0b3f6
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/baseline-implementation-report.md
@@ -0,0 +1,12 @@
+# Implementer Report
+
+- Brief: `artifacts/bianchini/v2/codex/P05-R1/task-brief.md`
+- Status: IN_PROGRESS
+
+## Changes
+
+## Verification
+
+## Decisions
+
+## Concerns
diff --git a/artifacts/bianchini/v2/codex/P05-R1/baseline-review.md b/artifacts/bianchini/v2/codex/P05-R1/baseline-review.md
new file mode 100644
index 0000000..a3edc4b
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/baseline-review.md
@@ -0,0 +1,25 @@
+# Review Package
+
+- Base: `c7012b942c36fe93fb136a376a1a73093f1e5aaa`
+- Head: `c7012b942c36fe93fb136a376a1a73093f1e5aaa`
+- Brief: `artifacts/bianchini/v2/codex/P05-R1/task-brief.md` (a2d2098a903af653572d1dc9145f60f5972c6bca641806cfd08bce1d4228d45a)
+- Report: `artifacts/bianchini/v2/codex/P05-R1/baseline-implementation-report.md` (8b5a9e70e0f8cb04fe3af6f68c97f867a9a115a0c4ad317d0bd3f13ead82bc3a)
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
diff --git a/artifacts/bianchini/v2/codex/P05-R1/checkpoint.json b/artifacts/bianchini/v2/codex/P05-R1/checkpoint.json
new file mode 100644
index 0000000..b997951
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/checkpoint.json
@@ -0,0 +1,141 @@
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
+      "status": "blocked",
+      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
+    },
+    {
+      "id": "P05-R1",
+      "status": "in_progress",
+      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
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
+  "next_action": "Concluir validações finais, commit autorizado da implementação, provas/revisão do guard nesse SHA e encerramento documental P05/P05-R1; publicar bm/v2-p05-r1 em push único sem força. Aceite U-201 registrado; release pending.",
+  "workspace": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
+  "git": {
+    "branch": "bm/v2-p05-r1",
+    "head": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+    "dirty": true
+  },
+  "ledger_tail": [
+    "por classe comprovada contra 77e93a e hash do baseline: 83−4=79, 12 canônicos, 91 chaves.",
+    "Quarentena mantém as duas autorias, táxon conflitante, fontes, motivo e estado explícito;",
+    "fontes de 2026-09-11 reutilizadas, sem rede taxonômica ou fato botânico novo inferido.",
+    "",
+    "Detalhe reversível: guarda normalizada no validador existente, schema inalterado;",
+    "bm change-policy sem flags retornou implementation_detail/continuar. Adaptação",
+    "operacional por instrução humana de manter implementação sem commit: change-policy",
+    "--plan-command retornou bounded_amendment, plan_invalidating false, sem reapproval.",
+    "Guard decision registrou o motivo: proof executa somente commit real, portanto não",
+    "submeter delta fictício ou marcar B1/gates/complete com provas do baseline. Sidecar",
+    "artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json fica fixing; B1 resolvido na",
+    "working tree, confirmação no commit posterior aguarda autorização. A parada é o gate",
+    "humano final solicitado; não categoria stopped nem impossibilidade de implementação.",
+    "",
+    "A spec/delta aplicáveis já formalizam inelegibilidade de entidades nomenclaturais",
+    "distintas sob mesma chave authorless. Permanecem congelados junto aos dois digests;",
+    "current/specs é sincronização prevista somente no encerramento regular, fora desta",
+    "rodada sem release/homologação. Não houve novo plano ou revisão do pacote aprovado.",
+    "",
+    "### Gates da working tree",
+    "",
+    "Python 3.14.4 -B, stdlib; histórico Python 3.12.3 registrado sem mudar contrato.",
+    "Cwd raiz deste workspace. Comandos/exit codes/horários/digests de stdout/stderr e",
+    "hashes dos seis inputs constam em validation-report.json; seu próprio hash é externo.",
+    "",
+    "- unittest discover scripts/phase1 test_offline_manifest.py: 94/94 passed.",
+    "- CLI validate_offline_manifest.py: exit 0, 1.1.0, 12 species, 2 protection, 14 classes,",
+    "  79 aliases e 91 chaves; testes incluem reintrodução nas 12 classes e normalização.",
+    "- route v2, repo-hygiene, workspace check, planning-audit --strict (checker 1 vigente),",
+    "  validate-state e snapshots P05-R1/histórico P05: todos exit 0.",
+    "- Parse estrito global: 120 arquivos JSON/JSONL/estado/sidecar antes dos últimos",
+    "  artefatos de checkpoint; sete exceções históricas de transporte idênticas ao HEAD,",
+    "  sintaxe válida após normalização apenas em memória. Nenhuma exceção em arquivo alterado.",
+    "- UTF-8 sem BOM/LF/newline e whitespace dos novos/modificados: passed; lock vazio",
+    "  operacional do guard não é documento textual. Blocos JSON novos também estritos.",
+    "- Varredura de padrões de segredos/PII e revisão do delta: sem achados em adições;",
+    "  URLs sintéticas existentes não são credenciais. Sem valor sensível em diagnóstico.",
+    "- git diff --check e índice vazio: exit 0. Roster, 12 classes e oito campos imutáveis",
+    "  por comparação com baseline; ledger prefixo exato do commit; P01/P03/P02/P04/release preservados.",
+    "- SHA256SUMS após geração do relatório: 7/7 OK, exit 0.",
+    "",
+    "Manifesto final SHA-256: bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c.",
+    "Roster SHA-256: 350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b.",
+    "SHA256SUMS SHA-256: 9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e.",
+    "Os sete hashes completos e lista de arquivos do commit estão em codex/P05-R1/FINAL_REVIEW.md.",
+    "",
+    "P05 continua blocked, P05-R1 in_progress, U-201 política/pacote aprovados e bytes",
+    "finais aguardando aceite. Nenhuma aprovação de bytes simulada. Implementação unstaged,",
+    "nenhum commit de implementação/push/merge, provider, credencial, imagem, dataset,",
+    "treino, modelo, produto, .NET/npm/Android/Docker/banco/Stryker, instalação ou release.",
+    "Worktree bm/v2-p03 e backup externo não editados/removidos. Próximo passo único:",
+    "aceite humano dos bytes finais e autorização para commit e push.",
+    "",
+    "Conferência final após checkpoint/revisão: 121 arquivos JSON/JSONL/estado/sidecar",
+    "com sintaxe estrita, sete exceções históricas de transporte preservadas, três blocos",
+    "JSON novos/modificados válidos; zero achados de segredos/PII nas adições. Nove arquivos",
+    "rastreados modificados e 11 artefatos operacionais novos, todos unstaged; índice vazio.",
+    "Os sete hashes finais permanecem idênticos aos de FINAL_REVIEW.md e SHA256SUMS passou",
+    "7/7 novamente. validate-state e ambos os snapshots passaram após o estado final.",
+    "Backup externo: sha256sum -c --strict BACKUP-SHA256SUMS, somente leitura no diretório",
+    "do backup, exit 0, 9/9 OK. Worktree antigo continua em a34da4/bm/v2-p03, sem edição.",
+    "json.tool do relatório também passou; nenhum novo teste ou mudança de implementação",
+    "após o GREEN final, apenas registros mínimos de revisão/checkpoint.",
+    "",
+    "## 2026-09-14T22:57:38.859020+00:00 — Aceite humano reafirmado e retomada do encerramento",
+    "",
+    "O responsável reafirmou explicitamente o aceite dos oito SHA-256 e a autorização dos",
+    "dois commits previstos e de um único push sem força da branch bm/v2-p05-r1. Registro",
+    "completo dos hashes: artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json.",
+    "U-201 resolved/consumed. Os registros pending nos artefatos selados são históricos;",
+    "este append registra o aceite posterior sem alterar nenhum dos oito bytes aceitos.",
+    "",
+    "Retomada no HEAD c7012b942c36fe93fb136a376a1a73093f1e5aaa, índice vazio, nove",
+    "modificados e 11 novos idênticos ao backup pré-commit. BACKUP-SHA256SUMS 10/10,",
+    "tar íntegro e correspondência 20/20. Branch remota P05-R1 ausente; referências",
+    "P03 807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2 e checkpoint P05",
+    "77e93a221dad3115c301b10317b626c236a3ba84 preservadas.",
+    "",
+    "P05/P05-R1 aguardam apenas a prova formal do commit autorizado; não se antecipa",
+    "conclusão do guard. Planejamento congelado, P01/P03-R6, P02/P04 e release preservados."
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P05-R1/closure-verification.json b/artifacts/bianchini/v2/codex/P05-R1/closure-verification.json
new file mode 100644
index 0000000..eb14e9b
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/closure-verification.json
@@ -0,0 +1,317 @@
+{
+  "schema_version": 1,
+  "plan": "P05-R1",
+  "status": "final_validations_passed",
+  "recorded_at": "2026-09-14T22:57:38.859020+00:00",
+  "acceptance": "artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json",
+  "accepted_sha256": {
+    "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json": "f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee",
+    "docs/phase1/F1-MAN01-offline-class-manifest.md": "adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24",
+    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
+    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS": "9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e"
+  },
+  "precommit_backup": {
+    "path": "/home/administradorarthur/code/scanplant-handoffs/p05-r1-precommit-c7012b-20260914",
+    "backup_checksum_entries_passed": 10,
+    "tar_and_current_files_matched": 20,
+    "backup_manifest_sha256": "fa7c374347da49af0cca7a83aa7f71cc6adc0469fc68d4fdb0c351c255200cbb"
+  },
+  "commit_allowlists": {
+    "implementation": [
+      "artifacts/bianchini/v2/codex/P05-R1/FINAL_REVIEW.md",
+      "artifacts/bianchini/v2/codex/P05-R1/baseline-findings.json",
+      "artifacts/bianchini/v2/codex/P05-R1/baseline-implementation-report.md",
+      "artifacts/bianchini/v2/codex/P05-R1/baseline-review.md",
+      "artifacts/bianchini/v2/codex/P05-R1/checkpoint.json",
+      "artifacts/bianchini/v2/codex/P05-R1/closure-verification.json",
+      "artifacts/bianchini/v2/codex/P05-R1/commit-findings.json",
+      "artifacts/bianchini/v2/codex/P05-R1/commit-review.md",
+      "artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json",
+      "artifacts/bianchini/v2/codex/P05-R1/implementation-report.md",
+      "artifacts/bianchini/v2/codex/P05-R1/task-brief.md",
+      "artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json",
+      "artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json.lock",
+      "artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json",
+      "artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json.bak",
+      "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
+      "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md",
+      "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json",
+      "artifacts/bianchini/v2/ledgers/P05.md",
+      "docs/living/PROJECT_STATE.md",
+      "docs/phase1/F1-MAN01-offline-class-manifest.md",
+      "docs/phase1/offline-class-manifest.v1.json",
+      "scripts/phase1/test_offline_manifest.py",
+      "scripts/phase1/validate_offline_manifest.py"
+    ]
+  },
+  "guard_commit_review": "pending implementation commit",
+  "publication": "pending",
+  "validation_runs": [
+    {
+      "at": "2026-09-14T22:58:08.920451+00:00",
+      "head": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+      "commands": [
+        {
+          "command": [
+            "python3",
+            "-B",
+            "-m",
+            "unittest",
+            "discover",
+            "-s",
+            "scripts/phase1",
+            "-p",
+            "test_offline_manifest.py",
+            "-v"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:06.833159+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+          "stderr_sha256": "0d833ee0553d4323a1f2267a9b5523e750751763316861a975008f28b1a670ff"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "scripts/phase1/validate_offline_manifest.py",
+            "--manifest",
+            "docs/phase1/offline-class-manifest.v1.json",
+            "--roster",
+            "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:06.922882+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "route",
+            "docs/living/PROJECT_STATE.md"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:07.133571+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "fd146f208e19de491b812e1ecf1535149d4170d4ec102245e88f0be8c498b799",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "repo-hygiene",
+            "check",
+            "--repo",
+            "."
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:07.310398+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "workspace",
+            "check",
+            "--repo",
+            "."
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:07.535714+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "4dc3faa7d541187e8e4de6b061195268e6f19aef3cc16e44e095e4eed0fa9f5a",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "planning-audit",
+            "docs/living/PROJECT_STATE.md",
+            "--root",
+            ".",
+            "--strict"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:07.770561+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "5267127254e4fee589df096cf92a6221db28e9255192bcd3f0bd7ed21f28bdc7",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "validate-state",
+            "docs/living/PROJECT_STATE.md"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:07.973004+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "snapshot",
+            "verify",
+            "docs/living/PROJECT_STATE.md",
+            "--root",
+            "."
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.197234+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "8d86d39d2bee4a2ea0b53a651a8fbf7a942a299846d8c48a6ceb8113b7327c34",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+            "snapshot",
+            "verify",
+            "/tmp/p05-r1-initial-state.json",
+            "--root",
+            "."
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.435360+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "c42061e0db297374c6fe69265b1aad94b175f1a708fe2d0989c0ebcecfac91ca",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "git",
+            "diff",
+            "--check"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.446581+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "git",
+            "diff",
+            "--cached",
+            "--exit-code"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.449515+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "sha256sum",
+            "-c",
+            "--strict",
+            "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.843797+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "python3",
+            "-B",
+            "-m",
+            "json.tool",
+            "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.908989+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "4a88e75f5ad0ca8a31da59ab1a95901dd008673e46c452c36c2d92789abbe500",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        },
+        {
+          "command": [
+            "git",
+            "diff",
+            "--check",
+            "c7012b942c36fe93fb136a376a1a73093f1e5aaa"
+          ],
+          "cwd": ".",
+          "executed_at": "2026-09-14T22:58:08.920392+00:00",
+          "exit_code": 0,
+          "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+          "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+        }
+      ],
+      "tests": {
+        "passed": 94,
+        "failed": 0,
+        "errors": 0,
+        "skipped": 0
+      },
+      "cli": {
+        "aliases": 79,
+        "classes": 14,
+        "manifest_sha256": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+        "manifest_version": "1.1.0",
+        "normalization_version": "1",
+        "protection": 2,
+        "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+        "schema_version": 1,
+        "scientific_keys": 91,
+        "species": 12,
+        "valid": true
+      },
+      "sets": {
+        "baseline_aliases": 83,
+        "quarantined": 4,
+        "final_aliases": 79,
+        "canonicals": 12,
+        "scientific_keys": 91,
+        "per_class_mapping_preserved": true,
+        "all_other_values_preserved": true
+      },
+      "checksums_passed": 7,
+      "accepted_hashes_preserved": 8,
+      "strict_json_files": 124,
+      "legacy_transport_exceptions_unchanged": [
+        "ScanPlantAPI/ScanPlantAPI/Properties/launchSettings.json",
+        "artifacts/bianchini/v1/evidence/P01-R1-final-sanitized-inconclusive/mutation-report.json",
+        "artifacts/bianchini/v2/evidence/P01-manual-final-v3/results/reports/mutation-report.json",
+        "artifacts/bianchini/v2/evidence/P01-manual-final-v5/results/reports/mutation-report.json",
+        "scanplant-web/metadata.json",
+        "scanplant-web/tsconfig.json",
+        "scanplant-web/tsconfig.node.json"
+      ],
+      "delta_findings": [],
+      "checker": "passed via planning-audit --strict; approved round unchanged",
+      "snapshots": "P05 and P05-R1 passed",
+      "prior_plans_and_release_preserved": true,
+      "ledger_append_only": true
+    }
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P05-R1/commit-findings.json b/artifacts/bianchini/v2/codex/P05-R1/commit-findings.json
new file mode 100644
index 0000000..2ef5648
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/commit-findings.json
@@ -0,0 +1,3 @@
+{
+  "findings": []
+}
diff --git a/artifacts/bianchini/v2/codex/P05-R1/commit-review.md b/artifacts/bianchini/v2/codex/P05-R1/commit-review.md
new file mode 100644
index 0000000..6102d7d
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/commit-review.md
@@ -0,0 +1,7 @@
+# Revisão do encerramento P05/P05-R1
+
+O delta remove somente quatro aliases ambíguos, valida sua quarentena e passa o manifesto para 1.1.0. Os oito hashes aceitos foram conferidos. Roster, normalização, classes, aliases elegíveis e pacotes aprovados permanecem preservados.
+
+Aceite humano: human-acceptance.json. Revisão inline da única unidade grouped. B1 está corrigido na working tree; a resolução formal requer o mesmo comando RED executado pelo guard no commit da implementação. O pacote Git e os proof_ids serão registrados após esse commit. Não há finding bloqueante novo identificado no delta revisado.
+
+Validações pré-commit: 94/94 testes, CLI 1.1.0 válida, conjuntos 83/4/79/12/91, 7/7 checksums e oito hashes aceitos preservados. Parse estrito de 124 documentos, com sete exceções históricas de transporte idênticas ao baseline; nenhuma exceção no delta. Checker vigente, audit estrito, validate-state, snapshots P05 e P05-R1, workspace e higiene aprovados. Varredura do delta sem achados; ledger append-only. Detalhes reproduzíveis em closure-verification.json.
diff --git a/artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json b/artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json
new file mode 100644
index 0000000..5de280a
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json
@@ -0,0 +1,33 @@
+{
+  "schema_version": 1,
+  "plans": [
+    "P05",
+    "P05-R1"
+  ],
+  "action": "U-201",
+  "status": "accepted",
+  "recorded_at": "2026-09-14T22:57:38.859020+00:00",
+  "approved_by": "responsável humano",
+  "source": "Prompt humano de retomada desta sessão: aprovação humana dos bytes e autorização para commit e push permanecem válidas; oito SHA-256 explicitamente reafirmados.",
+  "approval_commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+  "accepted_sha256": {
+    "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json": "f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee",
+    "docs/phase1/F1-MAN01-offline-class-manifest.md": "adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24",
+    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
+    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS": "9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e"
+  },
+  "authorization": {
+    "implementation_commit": "feat(p05-r1): quarantine ambiguous aliases",
+    "closure_commit_if_documentary_only": "chore(p05-r1): close manifest review",
+    "single_non_force_push": "git push --set-upstream origin bm/v2-p05-r1",
+    "release": false,
+    "homologation": false
+  },
+  "historical_evidence": "validation-report.json, taxonomy-review.md e FINAL_REVIEW.md registram o gate anterior; este aceite posterior os complementa sem reescrever os bytes aceitos.",
+  "u201_status": "resolved",
+  "u201_authorization": "consumed"
+}
diff --git a/artifacts/bianchini/v2/codex/P05-R1/implementation-report.md b/artifacts/bianchini/v2/codex/P05-R1/implementation-report.md
new file mode 100644
index 0000000..736c2a6
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/implementation-report.md
@@ -0,0 +1,50 @@
+# Implementer Report — P05-R1 / T1
+
+- Brief: `artifacts/bianchini/v2/codex/P05-R1/task-brief.md`
+- Status: IMPLEMENTED_WORKING_TREE; pending final human bytes acceptance.
+- Approval commit: `c7012b942c36fe93fb136a376a1a73093f1e5aaa` (planning/approval only).
+
+## Changes
+
+Removed exactly four authorless homonyms from synonyms; manifest_version 1.1.0.
+The scientific map rejects normalized quarantined names with E_NAME_QUARANTINED.
+A valid manifest resolves the four to None. Schema/normalization/roster, all class
+identities, IDs/order/common names/protections and other aliases remain unchanged.
+Updated taxonomy evidence, F1-MAN01 docs, report and seven-file checksum seal.
+Frozen applicable spec/delta already define the rule and remain byte-identical.
+The current-spec target is reserved for cycle close as explicitly planned, not this gate.
+
+## Verification
+
+Python 3.14.4 -B, stdlib only; historical evidence used 3.12.3. RED baseline proof:
+proof-93c13d6b0c1affb7122f227180990597, exit 1 at approval commit. Expanded pre-fix suite
+ran 92 tests with 91 failing assertions/subtests; no production integration exercised.
+Final GREEN: 94 tests, zero failures/errors/skips; 81 prior tests plus 13 new tests.
+Exact baseline set/mapping equality: 83 minus the four quarantined = 79 aliases;
+12 canonicals remain, 91 unique scientific keys. Reintroduction tested in all 12
+species and through normalized alias/canonical paths. Authorship is never stripped.
+CLI, strict JSON/JSONL, snapshots, state, audit and checksums passed.
+Read validation-report.json and FINAL_REVIEW.md for actual commands, hashes and limits.
+
+## Decisions
+
+One fix round in the same T1 sidecar, zero redesigns and no deferred hardening.
+Known-homonym exclusion is a small normalized set in the existing validator; evidence
+retains authorship and conflicts separately without changing manifest schema.
+bm change-policy with no flags: implementation_detail; with --plan-command for
+postponing commit-bound proof: bounded_amendment, no invalidation/reapproval.
+User instruction forbids implementation staging/commit before the final gate.
+Therefore guard remains fixing with B1 formally open against baseline; B1 is corrected
+and verified in the hashed working tree. Do not fake submit-delta, green commit proofs,
+review or complete. After authorization, submit the actual commit and recheck its proofs
+in this same sidecar; this is not a new plan or another implementation round.
+The one-task grouped brief is emitted by bm as kind task (one unit digest), not group;
+preserve the official digest without inventing another task/group.
+
+## Concerns and final boundary
+
+No unresolved implementation defect found in final local review. Human acceptance
+of final bytes and permission for commit/push are pending. P05 blocked, P05-R1 in_progress,
+U-201 open only for final bytes acceptance; prior plans and release preserved.
+No push, merge, product integration, provider, credential use, taxonomy network,
+installation, runtime stack, mutation campaign, old-worktree or external-backup edit.
diff --git a/artifacts/bianchini/v2/codex/P05-R1/task-brief.md b/artifacts/bianchini/v2/codex/P05-R1/task-brief.md
new file mode 100644
index 0000000..1b2c3e4
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P05-R1/task-brief.md
@@ -0,0 +1,102 @@
+# Task Brief 1
+
+- Plan: `docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md`
+- Plan SHA-256: `625164b23b6cab84ec1512c95987cb4f74936374c49fd4b9f9b35c1a46e3b666`
+- Kind: `task`
+- Group ID: `n/a`
+- Group SHA-256: `7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6`
+- Unit `1` SHA-256: `7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6`
+
+### Tarefa 1 — Mapa inequívoco, quarentena rastreável e bytes finais aceitos
+
+**Execution:** grouped
+
+**Review:** plan_gate
+
+**Change:** parser
+
+**Readiness refs:** D-211, D-212, D-213, A-211, P-211, P-212, P-213, U-201, SD-201
+
+**Test seams:** normalize_name; scientific_map; resolve_scientific_name; validate_manifest;
+CLI documental; associação de aliases/canônicos por class_id e roster.
+
+**Spec refs:** docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#regra-pública-e-estados,
+docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#invariantes-e-contagem,
+docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#versionamento-e-arquitetura,
+docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#verificação-e-aceite,
+docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#formato-e-identidade,
+docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#referências-e-elegibilidade,
+docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#quarentena-e-resolução,
+docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#versão-e-compatibilidade,
+docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#verificação-evidência-e-aceite.
+
+**Files:** alterar futuramente docs/phase1/offline-class-manifest.v1.json,
+scripts/phase1/validate_offline_manifest.py, scripts/phase1/test_offline_manifest.py,
+docs/phase1/F1-MAN01-offline-class-manifest.md,
+artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md,
+artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json,
+artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS;
+append artifacts/bianchini/v2/ledgers/P05.md e atualizar docs/living/PROJECT_STATE.md
+somente por fatos. Roster approved-species-roster.json é entrada imutável, sem edição.
+Nenhum arquivo acima é alterado nesta rodada de planejamento, exceto append de planejamento
+no ledger e estado. Planos/specs/manifestações de aprovação históricas e current/specs preservados.
+
+**Contract:** depois de aprovação explícita do pacote, autorização separada de execução,
+pacote commitado e workspace v2 válido, remover somente Aloe maculata, Aloe variegata,
+Ficus clusiifolia e Ficus cordata de synonyms e do mapa científico, retornar None para
+essas entradas normalizadas no manifesto válido e rejeitar reintrodução no mapa/validação.
+Manter registros quarantined com autoria associada, autoria conflitante, identidade,
+fontes, motivo e vínculo U-201, preservando sinonímia da fonte. Não acrescentar autoria
+às chaves ou remover autoria recebida. Novo homônimo bloqueia aceitação até revisão explícita.
+Implementar proposta minor 1.1.0, schema/normalização 1. Preservar integralmente os 12
+canônicos, nomes comuns, IDs/ordem/índices/proteções e roster. Baseline para comparação:
+manifesto do commit 77e93a221dad3115c301b10317b626c236a3ba84, SHA-256
+39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5.
+Não alterar nenhuma outra regra de elegibilidade já aprovada ou retirar alias elegível.
+
+**Verification:** cwd raiz de workspace v2 válido, Python stdlib e Git já disponíveis;
+registrar `python3 --version`. No gate fast executar
+`python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'`
+e `python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`.
+Ambos exit 0; CLI deve reportar 12 species, 2 protection, 14 classes, versão 1.1.0
+e hashes corretos. Testes antes/depois da correção devem tornar visível a falha original
+dos quatro nomes, preservando regressões. No gate plan, executar a mesma suíte e CLI
+após últimas alterações, `python3 -B -m json.tool artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json`,
+`sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS` (7/7),
+`git diff --check`, parse JSON estrito do relatório/manifesto/roster (sem chaves duplicadas,
+NaN/Infinity/números não finitos), UTF-8/LF/newline, paths, segredos e revisão humana.
+Usar strict_load já existente também no teste do relatório; json.tool isolado não prova
+JSON estrito. Inspecionar diff completo e untracked. Não executar gates de produto/release.
+
+Matriz obrigatória dentro da suíte documental e revisão da mesma unidade:
+
+| Caso | Resultado exigido |
+|---|---|
+| 12 canônicos + todos os aliases não ambíguos | class_id esperado, sem alteração |
+| Quatro Q, cada um e variantes de caixa/whitespace Unicode | None; ausentes de scientific_map |
+| Reinserir cada Q como alias em qualquer classe | rejeição explícita; nenhuma associação silenciosa |
+| Autoria recebida e nomes comuns/proteções | sem remoção de autoria ou resolução indevida |
+| Colisões normalizadas canônico/alias, intra/interclasse | erro de contrato |
+| Conjuntos e mapeamentos por classe | A0 com 83; Q com 4; Afinal = A0 menos Q, sem adições/trocas |
+| Contagem derivada | 79 aliases, 91 chaves com canônicos; Aloe 11→9, Ficus 12→10 |
+| Roster, IDs, ordem, canônicos/comuns e definições | igualdade com baseline, hash roster preservado |
+| Evidência de cada Q | quarantined, ambas autorias, identidade conflitante, fontes e motivo |
+| Todos os demais aliases | fonte oficial e elegibilidade individual; novo conflito bloqueia |
+| Versão/schema/normalização | 1.1.0 / 1 / 1 em manifesto, validator, testes, docs e relatório |
+
+Prova de conjuntos deve ler baseline imutável pelo Git ou fixture derivada identificada
+pelo hash acima; não gerar expectativa do próprio manifesto modificado. Reconciliar por
+classe e conjunto normalizado, não só subtração numérica. Teste de reintrodução deve
+adulterar dados em memória e observar falha, sem persistir mudança em manifesto real.
+Fixtures 1.0.0 legadas não podem mascarar expectativa 1.1.0 no novo gate. Manter regressões
+aplicáveis de JSON/Unicode, formatos, fontes, tipos, erros CLI e ausência de escrita/rede.
+
+**Done when:** gates passam, alterações limitadas à regra e artefatos autorizados;
+evidência e relatório reconciliam aliases e versão, sete hashes conferem, e responsável
+aceita explicitamente bytes finais/hashes após revisão U-201. Sem esse aceite, P05-R1
+e P05 não são completed e U-201 permanece aberta; decisão de política não dá aceite
+de bytes. Registrar parecer real em append depois da selagem. Manter P01/P03-R6
+blocked-terminal, P02/P04 completed, release pending. Não sincronizar current/specs,
+fechar ciclo, instalar ferramentas ou realizar integração de produto, imagens, dataset,
+treino, modelo, provider, credencial, .NET, npm, Android, Docker, banco ou Stryker.
+Esta rodada encerra no pedido de aprovação do pacote, antes de staging/commit/push/implementação.
diff --git a/artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json b/artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json
new file mode 100644
index 0000000..2ab0f9e
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json
@@ -0,0 +1,33 @@
+{
+  "created_at": "2026-09-14T22:32:23.179640Z",
+  "plan_id": "P05-R1",
+  "planning_version": "v2",
+  "proofs": {
+    "proof-93c13d6b0c1affb7122f227180990597": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import json,sys; from pathlib import Path; sys.path.insert(0,\"scripts/phase1\"); import validate_offline_manifest as v; m=json.loads(Path(\"docs/phase1/offline-class-manifest.v1.json\").read_text()); q=(\"Aloe maculata\",\"Aloe variegata\",\"Ficus clusiifolia\",\"Ficus cordata\"); results={n:v.resolve_scientific_name(m,n) for n in q}; print(json.dumps(results)); assert all(x is None for x in results.values()), \"U-201: quarantined homonyms still resolve\""
+      ],
+      "commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+      "created_at": "2026-09-14T22:32:23.168306Z",
+      "cwd": ".",
+      "exit_code": 1,
+      "plan_id": "P05-R1",
+      "planning_version": "v2",
+      "proof_id": "proof-93c13d6b0c1affb7122f227180990597",
+      "signature": "0c17efbf9c2dc42ce2535792e92d0d5b1fb0afd9bc67580bf36d0ca7193d487d",
+      "spawn_error": false,
+      "stderr_sha256": "ffb6c34b0f74a24adc718ff0f215c8672cd046c0ed183e5fe2109095447d88c6",
+      "stdout_sha256": "26bf728c1a8950c3be541ad5592dcfe586dc146e30efeb65257875c73b188ac0",
+      "timed_out": false,
+      "timeout_seconds": 60.0,
+      "unit_id": "T1"
+    }
+  },
+  "repository_root": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
+  "store_version": 1,
+  "unit_id": "T1",
+  "updated_at": "2026-09-14T22:32:23.179671Z"
+}
diff --git a/artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json.lock b/artifacts/bianchini/v2/codex/convergence/P05-R1/.proofs/T1.json.lock
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json b/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json
new file mode 100644
index 0000000..b5096f1
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json
@@ -0,0 +1,88 @@
+{
+  "blockers": {
+    "B1": {
+      "approved_requirement": "retornar None para",
+      "disposition": "blocker",
+      "id": "B1",
+      "material_impact": "Binômio comprovadamente ambíguo retorna class_id",
+      "proof_id": "proof-93c13d6b0c1affb7122f227180990597",
+      "reachable_scenario": "Chamar resolve_scientific_name com qualquer dos quatro homônimos no manifesto preliminar",
+      "review_commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+      "risk_seam": "offline-manifest-contract",
+      "root_cause": "Mapa científico não aplica a inelegibilidade authorless aprovada em P05-R1",
+      "severity": "important",
+      "source": "initial",
+      "status": "open",
+      "structural": false,
+      "structural_class": null,
+      "structural_evidence": null,
+      "title": "Quatro homônimos ainda resolvem no baseline"
+    }
+  },
+  "created_at": "2026-09-14T22:33:58.037955Z",
+  "decisions": [
+    {
+      "at": "2026-09-14T22:37:13.754336Z",
+      "kind": "internal",
+      "result": "automatic",
+      "summary": "Instrução humana exige bytes finais unstaged e nenhum commit da implementação. B1 corrigido e testes GREEN na working tree; submit-delta/review/gates do guard esperam commit futuro autorizado. Não simular proof verde do HEAD baseline. bm change-policy --plan-command: bounded_amendment, sem replanejamento. Encerrar somente no gate humano final solicitado."
+    }
+  ],
+  "deferred_hardening": [],
+  "delta_submissions": 0,
+  "events": [
+    {
+      "action": "review_frozen",
+      "at": "2026-09-14T22:33:58.037984Z",
+      "blockers": [
+        "B1"
+      ],
+      "hardening": 0
+    },
+    {
+      "action": "phase_transition",
+      "at": "2026-09-14T22:33:58.201067Z",
+      "command": "fix",
+      "source": "review_frozen",
+      "target": "fixing"
+    },
+    {
+      "action": "fix_started",
+      "at": "2026-09-14T22:33:58.201100Z",
+      "blockers": [
+        "B1"
+      ],
+      "round": 1,
+      "summary": "Aplicar a regra de quarentena aprovada, versão 1.1.0, testes e evidência na única unidade P05-R1; manter implementação sem commit até aceite humano."
+    },
+    {
+      "action": "decision",
+      "at": "2026-09-14T22:37:13.754420Z",
+      "kind": "internal",
+      "result": "automatic"
+    }
+  ],
+  "fix_rounds": 1,
+  "gates": {},
+  "last_review_head": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+  "pending_delta": null,
+  "phase": "fixing",
+  "plan_id": "P05-R1",
+  "planning_version": "v2",
+  "redesign_count": 0,
+  "repository_root": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
+  "required_gates": [
+    "contract-tests",
+    "manifest-cli",
+    "documentary-integrity"
+  ],
+  "schema_version": 2,
+  "seam": "offline-manifest-contract",
+  "task_brief": "artifacts/bianchini/v2/codex/P05-R1/task-brief.md",
+  "task_brief_digest": "a2d2098a903af653572d1dc9145f60f5972c6bca641806cfd08bce1d4228d45a",
+  "unit_digest": "7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6",
+  "unit_id": "T1",
+  "unit_identity": "4d8b8ba543addad3dabda2347f1df3a93733b6f76f4168d8c269ef554ebcf09b",
+  "unit_identity_source": "task_brief",
+  "updated_at": "2026-09-14T22:37:13.754426Z"
+}
diff --git a/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json.bak b/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json.bak
new file mode 100644
index 0000000..0d0eef6
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json.bak
@@ -0,0 +1,75 @@
+{
+  "blockers": {
+    "B1": {
+      "approved_requirement": "retornar None para",
+      "disposition": "blocker",
+      "id": "B1",
+      "material_impact": "Binômio comprovadamente ambíguo retorna class_id",
+      "proof_id": "proof-93c13d6b0c1affb7122f227180990597",
+      "reachable_scenario": "Chamar resolve_scientific_name com qualquer dos quatro homônimos no manifesto preliminar",
+      "review_commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+      "risk_seam": "offline-manifest-contract",
+      "root_cause": "Mapa científico não aplica a inelegibilidade authorless aprovada em P05-R1",
+      "severity": "important",
+      "source": "initial",
+      "status": "open",
+      "structural": false,
+      "structural_class": null,
+      "structural_evidence": null,
+      "title": "Quatro homônimos ainda resolvem no baseline"
+    }
+  },
+  "created_at": "2026-09-14T22:33:58.037955Z",
+  "decisions": [],
+  "deferred_hardening": [],
+  "delta_submissions": 0,
+  "events": [
+    {
+      "action": "review_frozen",
+      "at": "2026-09-14T22:33:58.037984Z",
+      "blockers": [
+        "B1"
+      ],
+      "hardening": 0
+    },
+    {
+      "action": "phase_transition",
+      "at": "2026-09-14T22:33:58.201067Z",
+      "command": "fix",
+      "source": "review_frozen",
+      "target": "fixing"
+    },
+    {
+      "action": "fix_started",
+      "at": "2026-09-14T22:33:58.201100Z",
+      "blockers": [
+        "B1"
+      ],
+      "round": 1,
+      "summary": "Aplicar a regra de quarentena aprovada, versão 1.1.0, testes e evidência na única unidade P05-R1; manter implementação sem commit até aceite humano."
+    }
+  ],
+  "fix_rounds": 1,
+  "gates": {},
+  "last_review_head": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+  "pending_delta": null,
+  "phase": "fixing",
+  "plan_id": "P05-R1",
+  "planning_version": "v2",
+  "redesign_count": 0,
+  "repository_root": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
+  "required_gates": [
+    "contract-tests",
+    "manifest-cli",
+    "documentary-integrity"
+  ],
+  "schema_version": 2,
+  "seam": "offline-manifest-contract",
+  "task_brief": "artifacts/bianchini/v2/codex/P05-R1/task-brief.md",
+  "task_brief_digest": "a2d2098a903af653572d1dc9145f60f5972c6bca641806cfd08bce1d4228d45a",
+  "unit_digest": "7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6",
+  "unit_id": "T1",
+  "unit_identity": "4d8b8ba543addad3dabda2347f1df3a93733b6f76f4168d8c269ef554ebcf09b",
+  "unit_identity_source": "task_brief",
+  "updated_at": "2026-09-14T22:33:58.201102Z"
+}
diff --git a/artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS b/artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
index 0e4d774..b49ddf6 100644
--- a/artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
+++ b/artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
@@ -1,7 +1,7 @@
 350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b  artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json
-7edda0086889a406c75d1198cd27a87bfc376c1e39f05a4ab69af5a8c3281ddf  artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md
-9ff4a73e1158535e245b67e928a73ee33686047a32185078efb33eab4ca9a662  artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json
-77afe6fd3350134af57201417df5bbd377b7b9e96b177ef0b9791a66d49f2280  docs/phase1/F1-MAN01-offline-class-manifest.md
-39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5  docs/phase1/offline-class-manifest.v1.json
-5c2b93a368173dd02ff5a2f23c2017fef9e1beef383cc12b88f77b347f42564b  scripts/phase1/test_offline_manifest.py
-d9010fd498b28b371c68160c5a7341714638dcd1320e8a01fd256314ab96618b  scripts/phase1/validate_offline_manifest.py
+272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23  artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md
+f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee  artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json
+adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24  docs/phase1/F1-MAN01-offline-class-manifest.md
+bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c  docs/phase1/offline-class-manifest.v1.json
+88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe  scripts/phase1/test_offline_manifest.py
+d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed  scripts/phase1/validate_offline_manifest.py
diff --git a/artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md b/artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md
index 37a8fdb..8148624 100644
--- a/artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md
+++ b/artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md
@@ -1,15 +1,21 @@
 # Revisão taxonômica P05/F1-MAN01

-Registro UTC: 2026-09-11T19:05:33Z. Responsável pela decisão de produto: responsável humano.
+Registro histórico UTC: 2026-09-11T19:05:33Z. Responsável pela decisão de produto: responsável humano.

-## Decisao humana corrigida U-201
+Estado atual P05-R1: política de quarentena e versão 1.1.0 aprovadas pelo responsável;
+implementação documental verificada, aceite humano dos bytes finais pendente.
+Fontes reutilizadas da consulta de 2026-09-11, sem nova consulta taxonômica em rede.
+As tabelas distinguem 79 aliases resolvíveis de quatro binômios quarantined. Os registros
+de decisão anteriores abaixo são históricos; a política vigente está na seção Quarentena authorless.
+
+## Histórico — decisão humana corrigida U-201 de 2026-09-11

 Transcrição da decisão corrigida; substitui somente a política anterior ainda não materializada. O timestamp é o momento real deste registro, não uma estimativa do envio da mensagem.

 SHA-256 do texto UTF-8 entre as cercas, incluindo newline final: `8ba368f75fead7272018915181348f6572cc564379ed75529168a0000f63a7e9`.

 ```text
 Corrijo e substituo integralmente a parte referente aos sinônimos da minha decisão humana anterior.

 A lista das 12 espécies, seus nomes comuns, a ordem das classes e as duas proteções continuam aprovadas sem alteração. Somente a política de sinônimos da declaração anterior é revogada e substituída pela política compatível com o contrato P05 congelado.

@@ -65,23 +71,23 @@ Política de sinônimos aprovada:

 5. `Kalanchoe globulifera var. coccinea` está expressamente excluído porque é infraspecífico e não satisfaz o formato binomial exigido pelo contrato.

 6. Os sinônimos enumerados na minha declaração anterior não formam uma allowlist nem um conjunto congelado. Aquela enumeração está substituída integralmente por esta política derivada da fonte e da spec aprovada.

 7. Os nomes comuns aprovados são somente rótulos pt-BR do produto. Eles não são nomes científicos, sinônimos taxonômicos ou IDs canônicos.

 Esta decisão humana corrigida resolve U-201 somente se o mecanismo de change-policy confirmar que ela é compatível com o contrato P05 já aprovado.
 ```

-## Compatibilidade e fonte
+## Compatibilidade histórica e fonte

-`bm.py change-policy` sem flags de alteração: implementation_detail; plan_invalidating=false; reapproval_required=false. A comparação considerou exclusivamente esta decisão corrigida. Nenhum plano/spec/digest de aprovação foi alterado.
+Resultado histórico da decisão de 2026-09-11 (anterior a P05-R1): `bm.py change-policy` sem flags de alteração: implementation_detail; plan_invalidating=false; reapproval_required=false. A comparação considerou exclusivamente esta decisão corrigida. Nenhum plano/spec/digest de aprovação foi alterado.

 Fonte primária: POWO/Kew, seção Synonyms diretamente subordinada ao registro da espécie aceita, consultada em 2026-09-11. O recorte não percorre sinônimos de variedades/subespécies aceitas, que representam táxons subordinados distintos. Não transfere aliases entre ranks por inferência. Todos os binomiais dessa seção são relacionados abaixo; autorias e notas nomenclaturais ficam nesta evidência, fora das chaves normalizadas. Nomes ilegítimos ou não validamente publicados ainda listados como sinônimos não são automaticamente apagados: a spec não estabelece filtro por validade nomenclatural. A revisão final deve avaliar ambiguidades sem confundir validade do nome com aceitação do táxon.

 Consulta textual; nenhum corpo de resposta externa, foto, dataset ou arquivo de modelo persistido. As listas e observações são transcrição factual de nomes, não reprodução de páginas.

 ## 1. Epipremnum aureum

 Nome aceito: **Epipremnum aureum (Linden & André) G.S.Bunting**. Nome comum aprovado: jiboia. [POWO](https://powo.science.kew.org/taxon/87014-1), consulta 2026-09-11. Sinônimos diretos: 4; binomiais: 4; excluídos pelo formato: 0.

 | Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
@@ -138,24 +144,24 @@ Nome aceito: **Aloe vera (L.) Burm.f.**. Nome comum aprovado: babosa. [POWO](htt
 |---|---|---|---|
 | Aloe perfoliata var. vera | L. | homotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe barbadensis | Mill. | heterotypic | incluído |
 | Aloe barbadensis var. chinensis | Haw. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe chinensis | Loudon | heterotypic | incluído |
 | Aloe elongata | Murray | heterotypic | incluído |
 | Aloe flava | Pers. | heterotypic | incluído |
 | Aloe indica | Royle | heterotypic | incluído |
 | Aloe lanzae | Tod. | heterotypic | incluído |
 | Aloe littoralis | J.Koenig ex Baker; not validly publ. | heterotypic | incluído |
-| Aloe maculata | Forssk.; nom. illeg. homonym. post. | heterotypic | incluído |
+| Aloe maculata | Forssk.; nom. illeg. homonym. post. | heterotypic | quarantined: homônimo sem autoria inelegível |
 | Aloe perfoliata var. barbadensis | (Mill.) Aiton | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe rubescens | DC. | heterotypic | incluído |
-| Aloe variegata | Forssk.; nom. illeg. homonym. post. | heterotypic | incluído |
+| Aloe variegata | Forssk.; nom. illeg. homonym. post. | heterotypic | quarantined: homônimo sem autoria inelegível |
 | Aloe vera var. chinensis | (Loudon) Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe vera var. lanzae | Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe vera var. littoralis | J.Koenig ex Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Aloe vulgaris | Lam. | heterotypic | incluído |

 ## 7. Chlorophytum comosum

 Nome aceito: **Chlorophytum comosum (Thunb.) Jacques**. Nome comum aprovado: clorofito. [POWO](https://powo.science.kew.org/taxon/532810-1), consulta 2026-09-11. Sinônimos diretos: 37; binomiais: 34; excluídos pelo formato: 3.

 | Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
@@ -214,22 +220,22 @@ Nome aceito: **Codiaeum variegatum (L.) Rumph. ex A.Juss.**. Nome comum aprovado
 ## 9. Ficus elastica

 Nome aceito: **Ficus elastica Roxb. ex Hornem.**. Nome comum aprovado: falsa-seringueira. [POWO](https://powo.science.kew.org/taxon/60458499-2), consulta 2026-09-11. Sinônimos diretos: 22; binomiais: 12; excluídos pelo formato: 10.

 | Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
 |---|---|---|---|
 | Stilpnophyllum elasticum | (Roxb. ex Hornem.) Drury | homotypic | incluído |
 | Urostigma elasticum | (Roxb. ex Hornem.) Miq. | homotypic | incluído |
 | Visiania elastica | (Roxb. ex Hornem.) Gasp. | homotypic | incluído |
 | Macrophthalma elastica | (Roxb. ex Hornem.) Gasp. | homotypic | incluído |
-| Ficus clusiifolia | Summerh.; nom. illeg. homonym. post. | heterotypic | incluído |
-| Ficus cordata | Kunth & C.D.Bouché; nom. illeg. homonym. post. | heterotypic | incluído |
+| Ficus clusiifolia | Summerh.; nom. illeg. homonym. post. | heterotypic | quarantined: homônimo sem autoria inelegível |
+| Ficus cordata | Kunth & C.D.Bouché; nom. illeg. homonym. post. | heterotypic | quarantined: homônimo sem autoria inelegível |
 | Ficus elastica var. belgica | L.H.Bailey & E.Z.Bailey | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. benghalensis | Blume | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. decora | Guillaumin | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. karet | (Miq.) Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. minor | Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. odorata | (Miq.) Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. rubra | L.H.Bailey & E.Z.Bailey | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. rubrinervis | Sata; without a Latin descr. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus elastica var. variegata | W.Bull | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
 | Ficus karet | (Miq.) King | heterotypic | incluído |
@@ -269,29 +275,156 @@ Nome aceito: **Tradescantia zebrina Regel**. Nome comum aprovado: lambari-roxo.
 |---|---|---|---|
 | Commelina zebrina | (Regel) André | homotypic | incluído |
 | Cyanotis zebrina | (Regel) Nees | homotypic | incluído |

 ## Exclusões de táxons subordinados e antiga enumeração

 As variedades e subespécies aceitas relacionadas nas páginas de Dracaena trifasciata, Codiaeum variegatum, Nephrolepis exaltata e Tradescantia zebrina não são aliases. Em particular, Zebrina pendula e Tradescantia pendula da declaração revogada apontam no POWO para Tradescantia zebrina var. zebrina; não constam nos dois sinônimos diretos da espécie atualmente selecionada. A variedade nominal foi consultada em 2026-09-11 em https://powo.science.kew.org/taxon/77170928-1. Também não incorporados desse registro subordinado: Cyanotis vittata, Tradescantia argentea, Tradescantia tricolor e Zebrina purpusii; nem Cyanotis vittata vittata, Zebrina pendula f. quadricolor ou Zebrina pendula var. quadricolor. Não são aliases automaticamente herdados.

 Kalanchoe globulifera var. coccinea está excluído expressamente e pelo formato. Homônimos entre nomes comuns das 12 classes: nenhum. Os nomes comuns não são utilizados por resolve_scientific_name.

-## Revisão humana final
+## Quarentena authorless — política vigente P05-R1 / U-201
+
+Um alias binomial sem autoria é inelegível quando sua mesma forma normalizada identifica
+entidades nomenclaturais distintas nas fontes consideradas. Os quatro nomes abaixo foram
+excluídos somente das chaves resolvíveis. Continuam como sinônimos nomenclaturais nas
+fontes citadas; a quarentena não revoga essa relação. Os outros táxons são evidência de
+conflito, não espécies novas do produto nem referências órfãs a inserir no manifesto.
+
+Aprovação humana do pacote P05-R1:
+`6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f`.
+A decisão aprovou explicitamente a versão 1.1.0, quatro quarantined, 79 aliases e 91
+chaves, preservando roster, 12 identidades, IDs/índices, nomes comuns e proteções.
+Somente binômios inequívocos nas fontes aplicáveis são elegíveis. Outro homônimo
+encontrado bloqueia aceitação até revisão explícita, sem associação silenciosa.
+Não remover autoria recebida, incluir autoria nas chaves, preferir classe ou usar contexto/fuzzy.
+
+```json
+{
+  "quarantined_aliases": [
+    {
+      "name": "Aloe maculata",
+      "normalized_authorless_name": "aloe maculata",
+      "related_class_id": "species_06",
+      "related_canonical_name": "Aloe vera",
+      "related_authorship": "Forssk.",
+      "conflicting_authorship": "All.",
+      "conflicting_taxon": "Aloe maculata (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/530017-1",
+        "https://powo.science.kew.org/taxon/77122815-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Aloe variegata",
+      "normalized_authorless_name": "aloe variegata",
+      "related_class_id": "species_06",
+      "related_canonical_name": "Aloe vera",
+      "related_authorship": "Forssk.",
+      "conflicting_authorship": "L.",
+      "conflicting_taxon": "Gonialoe variegata",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/530017-1",
+        "https://powo.science.kew.org/taxon/530009-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Ficus clusiifolia",
+      "normalized_authorless_name": "ficus clusiifolia",
+      "related_class_id": "species_09",
+      "related_canonical_name": "Ficus elastica",
+      "related_authorship": "Summerh.",
+      "conflicting_authorship": "Schott",
+      "conflicting_taxon": "Ficus clusiifolia (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/60458499-2",
+        "https://powo.science.kew.org/taxon/852625-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Ficus cordata",
+      "normalized_authorless_name": "ficus cordata",
+      "related_class_id": "species_09",
+      "related_canonical_name": "Ficus elastica",
+      "related_authorship": "Kunth & C.D.Bouché",
+      "conflicting_authorship": "Thunb.",
+      "conflicting_taxon": "Ficus cordata (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/60458499-2",
+        "https://powo.science.kew.org/taxon/852662-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    }
+  ]
+}
+```

-Status: blocked_pending_human_taxonomy. A decisão de produto foi recebida; o aceite dos bytes finais não foi concedido. A conferência complementar confirmou ambiguidade taxonômica nos quatro binomiais abaixo. O manifesto já materializado é preliminar e não pode ser entregue como contrato aceito. Não foram removidos aliases silenciosamente nem incluídas autorias nas chaves. Nenhum parecer approved/rejected foi atribuído ao responsável para estes bytes.
+## Reconciliação e revisão dos aliases restantes

-| Chave sem autoria | Nome listado para a classe do rascunho | Outro nome e táxon oficial |
-|---|---|---|
-| Aloe maculata | Forssk., sinônimo de Aloe vera | [Aloe maculata All., espécie aceita distinta](https://powo.science.kew.org/taxon/77122815-1) |
-| Aloe variegata | Forssk., sinônimo de Aloe vera | [Aloe variegata L., sinônimo de Gonialoe variegata](https://powo.science.kew.org/taxon/530009-1) |
-| Ficus clusiifolia | Summerh., sinônimo de Ficus elastica | [Ficus clusiifolia Schott, espécie aceita distinta](https://powo.science.kew.org/taxon/852625-1) |
-| Ficus cordata | Kunth & C.D.Bouché, sinônimo de Ficus elastica | [Ficus cordata Thunb., espécie aceita distinta](https://powo.science.kew.org/taxon/852662-1) |
+Baseline do manifesto: commit `77e93a221dad3115c301b10317b626c236a3ba84`, SHA-256
+`39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5`.
+As 83 chaves preliminares eram internamente únicas, mas quatro têm homônimos externos
+comprovados. Diferença exata de conjuntos: Afinal = A0 menos Q, sem qualquer alias
+adicionado, trocado de classe ou removido além de Q. Resultado: 79 aliases resolvíveis,
+12 canônicos preservados e 91 chaves científicas únicas. As proteções ficam fora do mapa.

-Consulta complementar real em 2026-09-11, somente textual. Esses quatro nomes históricos estão presentes na seção primária como homônimos posteriores ilegítimos. Remover a autoria, como exige a chave binomial, torna indistinguíveis os nomes ligados a táxons diferentes. Não há colisão entre as 12 classes, mas isso não resolve a ambiguidade demonstrada. Os outros táxons desta tabela são evidência de conflito, não novas espécies do produto, candidatos ou referências órfãs a inserir no manifesto.
+| class_id | Preliminares | quarantined | Resolvíveis |
+|---|---|---|---|
+| species_01 | 4 | 0 | 4 |
+| species_02 | 6 | 0 | 6 |
+| species_03 | 3 | 0 | 3 |
+| species_04 | 0 | 0 | 0 |
+| species_05 | 1 | 0 | 1 |
+| species_06 | 11 | 2 | 9 |
+| species_07 | 34 | 0 | 34 |
+| species_08 | 5 | 0 | 5 |
+| species_09 | 12 | 2 | 10 |
+| species_10 | 1 | 0 | 1 |
+| species_11 | 4 | 0 | 4 |
+| species_12 | 2 | 0 | 2 |
+| Total | 83 | 4 | 79 |
+
+Conferência documental local: os 79 registros incluídos nas tabelas acima preservam
+autoria, relação e fonte oficial da mesma classe; todos coincidem com os aliases
+restantes do manifesto e seus ref_ids. Nenhuma nova fonte, taxon ou alias foi inferido.
+Ausência de homonímia externa desconhecida não é comprovada por unicidade interna;
+qualquer nova evidência conflitante exige a fronteira de revisão explícita aprovada.
+
+## Revisão humana final

-Aplica-se a cláusula congelada: "Fonte indisponível, nome ambíguo, sinonímia conflitante, gênero/cultivar sem espécie ou dois itens humanos para o mesmo táxon bloqueiam a entrega na mesma U-201." O change-policy da decisão corrigida permanece implementation_detail; a política humana é compatível, mas a conferência de dados revelou esta fronteira. U-201 tem entrada de escopo registrada, porém permanece aberta quanto à ambiguidade e ao aceite dos bytes. P05 fica blocked, incompleto; não houve alteração de plano/spec ou replanejamento. A quantidade 83 é a população preliminar estrutural, não um conjunto taxonômico final aprovado.
+Status: pending_final_bytes_acceptance. A decisão taxonômica de tratamento e o pacote
+estão aprovados; o aceite dos bytes finais produzidos nesta execução ainda não foi dado.
+Os quatro retornam None/null no manifesto 1.1.0 válido. Reintrodução como alias ou
+canônico provoca E_NAME_QUARANTINED na construção do mapa, inclusive após normalização;
+não há resolução para outra classe ou proteção. Nomes malformados continuam rejeitados
+pelas regras anteriores de formato/Unicode.

-Os hashes do manifesto e roster a submeter à revisão são registrados abaixo e em SHA256SUMS. P05 não pode ser completed enquanto faltar esse aceite.
+Conferir as 12 classes, os 79 aliases, os quatro conflitos e estes hashes. Registrar o
+parecer humano posterior em append no ledger para não alterar os bytes já submetidos.
+P05 e P05-R1 permanecem incompletos até esse aceite; nenhum approved/rejected de bytes
+foi atribuído ao responsável pelo executor.

-Manifesto SHA-256: `39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5`.
+Manifesto SHA-256: `bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c`.
 Roster SHA-256: `350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b`.
diff --git a/artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json b/artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json
index c1acff3..8d0db39 100644
--- a/artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json
+++ b/artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json
@@ -1,1171 +1,926 @@
 {
   "schema_version": 1,
-  "plan": "P05",
+  "plan": "P05-R1",
   "functional_id": "F1-MAN01",
-  "recorded_at_utc": "2026-09-11T19:20:18Z",
-  "python_version": "3.12.3",
-  "validation_scope": "Uncommitted preliminary working-tree artifact. Structural validation passed; taxonomic semantic gate BLOCKED. Not a canonical accepted contract or guard-owned proof.",
-  "initial_checkpoint": {
-    "repository": "Parys-boop/ScanPlant",
-    "branch": "bm/v2-p03",
-    "upstream": "origin/bm/v2-p03",
-    "head": "807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2",
-    "upstream_sha": "807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2",
-    "remote_sha": "807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2",
-    "divergence": [
-      0,
-      0
-    ],
-    "clean": true
-  },
-  "execution_workspace": {
-    "path": "/tmp/scanplant-p05-workspace",
-    "branch": "bm/v2-p05",
-    "head": "807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2",
-    "separate_worktree": true
-  },
-  "change_policy": {
-    "classification": "implementation_detail",
-    "comparison": "Only corrected human decision; previous unmaterialized synonym enumeration revoked. Contract already requires source-derived eligible binomials; all material-change flags false. No membership/order/schema/plan changes.",
-    "plan_invalidating": false,
-    "reapproval_required": false
-  },
-  "human_decision": {
-    "role": "responsável humano",
-    "recorded_at_utc": "2026-09-11T19:05:33Z",
-    "decision_text_sha256": "8ba368f75fead7272018915181348f6572cc564379ed75529168a0000f63a7e9",
-    "evidence": "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md",
-    "scope_input": "recorded_and_policy_compatible",
-    "final_bytes_review": "blocked_pending_human_taxonomy"
+  "status": "automated_passed_human_acceptance_pending",
+  "generated_at": "2026-09-14T22:39:58.574587+00:00",
+  "approval_commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+  "planning_digest": "6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f",
+  "historical_p05_digest": "246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5",
+  "tested_revision": {
+    "head": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+    "scope": "uncommitted working tree",
+    "implementation_committed": false,
+    "input_files_sha256": {
+      "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+      "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+      "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed",
+      "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
+      "docs/phase1/F1-MAN01-offline-class-manifest.md": "adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24",
+      "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23"
+    }
   },
-  "counts": {
-    "species": 12,
-    "protection": 2,
-    "classes": 14,
-    "indices": [
-      0,
-      1,
-      2,
-      3,
-      4,
-      5,
-      6,
-      7,
-      8,
-      9,
-      10,
-      11,
-      12,
-      13
-    ],
-    "direct_source_infraspecific_exclusions": 24,
-    "preliminary_binomial_synonyms": 83,
-    "ambiguous_binomials_pending": 4
+  "runtime": {
+    "python": "3.14.4",
+    "historical_python": "3.12.3",
+    "bytecode_disabled": true,
+    "contract_changed_for_runtime": false,
+    "dependencies": "stdlib only"
   },
-  "synonyms_by_species": [
-    {
-      "index": 0,
-      "name": "Epipremnum aureum",
-      "preliminary_binomials": 4
-    },
-    {
-      "index": 1,
-      "name": "Monstera deliciosa",
-      "preliminary_binomials": 6
-    },
-    {
-      "index": 2,
-      "name": "Zamioculcas zamiifolia",
-      "preliminary_binomials": 3
-    },
-    {
-      "index": 3,
-      "name": "Spathiphyllum wallisii",
-      "preliminary_binomials": 0
-    },
-    {
-      "index": 4,
-      "name": "Dracaena trifasciata",
-      "preliminary_binomials": 1
-    },
-    {
-      "index": 5,
-      "name": "Aloe vera",
-      "preliminary_binomials": 11
-    },
-    {
-      "index": 6,
-      "name": "Chlorophytum comosum",
-      "preliminary_binomials": 34
-    },
-    {
-      "index": 7,
-      "name": "Codiaeum variegatum",
-      "preliminary_binomials": 5
-    },
-    {
-      "index": 8,
-      "name": "Ficus elastica",
-      "preliminary_binomials": 12
-    },
-    {
-      "index": 9,
-      "name": "Kalanchoe blossfeldiana",
-      "preliminary_binomials": 1
-    },
-    {
-      "index": 10,
-      "name": "Nephrolepis exaltata",
-      "preliminary_binomials": 4
-    },
-    {
-      "index": 11,
-      "name": "Tradescantia zebrina",
-      "preliminary_binomials": 2
-    }
-  ],
-  "exclusions": {
-    "policy": "Direct species Synonyms section, no recursive inheritance from accepted subordinate taxa. Infraspecific names excluded; no common names as aliases.",
-    "details": "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md",
-    "explicitly_excluded": "Kalanchoe globulifera var. coccinea",
-    "subordinate_binomials_not_included": [
-      "Zebrina pendula",
-      "Tradescantia pendula",
-      "Cyanotis vittata",
-      "Tradescantia argentea",
-      "Tradescantia tricolor",
-      "Zebrina purpusii"
+  "tests": {
+    "passed": 94,
+    "failed": 0,
+    "errors": 0,
+    "skipped": 0,
+    "previous_tests_preserved": 81,
+    "new_tests": 13,
+    "individual_results": [
+      {
+        "test": "test_all_seventy_nine_eligible_aliases_resolve",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_all_seventy_nine_eligible_aliases_resolve",
+        "result": "passed"
+      },
+      {
+        "test": "test_all_twelve_canonicals_resolve",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_all_twelve_canonicals_resolve",
+        "result": "passed"
+      },
+      {
+        "test": "test_authorship_is_not_removed",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_authorship_is_not_removed",
+        "result": "passed"
+      },
+      {
+        "test": "test_canonical_reintroduction_is_rejected",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_canonical_reintroduction_is_rejected",
+        "result": "passed"
+      },
+      {
+        "test": "test_exact_alias_sets_and_counts",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_exact_alias_sets_and_counts",
+        "result": "passed"
+      },
+      {
+        "test": "test_fixture_reintroduction_rejected_in_every_species",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_fixture_reintroduction_rejected_in_every_species",
+        "result": "passed"
+      },
+      {
+        "test": "test_no_normalized_collisions_and_protections_excluded",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_no_normalized_collisions_and_protections_excluded",
+        "result": "passed"
+      },
+      {
+        "test": "test_normalized_quarantined_inputs_return_none",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_normalized_quarantined_inputs_return_none",
+        "result": "passed"
+      },
+      {
+        "test": "test_only_approved_manifest_changes",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_only_approved_manifest_changes",
+        "result": "passed"
+      },
+      {
+        "test": "test_preliminary_version_is_no_longer_accepted",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_preliminary_version_is_no_longer_accepted",
+        "result": "passed"
+      },
+      {
+        "test": "test_real_validator_version_and_counts",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_real_validator_version_and_counts",
+        "result": "passed"
+      },
+      {
+        "test": "test_scientific_map_rejects_normalized_reintroduction",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_scientific_map_rejects_normalized_reintroduction",
+        "result": "passed"
+      },
+      {
+        "test": "test_taxonomy_evidence_preserves_conflicts_and_eligible_aliases",
+        "class": "test_offline_manifest.ApprovedQuarantineTests.test_taxonomy_evidence_preserves_conflicts_and_eligible_aliases",
+        "result": "passed"
+      },
+      {
+        "test": "test_cli_no_network_or_writes",
+        "class": "test_offline_manifest.ManifestContractTests.test_cli_no_network_or_writes",
+        "result": "passed"
+      },
+      {
+        "test": "test_cli_valid_invalid_inaccessible_and_invocation",
+        "class": "test_offline_manifest.ManifestContractTests.test_cli_valid_invalid_inaccessible_and_invocation",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_cross_canonical",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_cross_canonical",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_equals_canonical",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_equals_canonical",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_infraspecific",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_infraspecific",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_inter_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_inter_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_intra_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_intra_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_no_reference",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_no_reference",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_alias_reference_missing",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_alias_reference_missing",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_array_order",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_array_order",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_authority_invalid",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_authority_invalid",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_canonical_authorship",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_canonical_authorship",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_canonical_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_canonical_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_canonical_hybrid",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_canonical_hybrid",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_canonical_lowercase",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_canonical_lowercase",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_canonical_whitespace",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_canonical_whitespace",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_class_wrong_type",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_class_wrong_type",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_classes_wrong_type",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_classes_wrong_type",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_common_empty",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_common_empty",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_common_intra_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_common_intra_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_control_character",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_control_character",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_date_future",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_date_future",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_date_impossible",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_date_impossible",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_display_outside_common",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_display_outside_common",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_extra_alias_field",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_extra_alias_field",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_extra_class_field",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_extra_class_field",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_extra_root_field",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_extra_root_field",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_hash_wrong",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_hash_wrong",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_id_common_name",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_id_common_name",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_id_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_id_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_boolean",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_boolean",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_float",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_float",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_missing",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_missing",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_outside",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_outside",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_index_string",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_index_string",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_invisible_character",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_invisible_character",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_manifest_version",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_manifest_version",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_name_wrong_type",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_name_wrong_type",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_normalization_version",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_normalization_version",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_absent",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_absent",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_alias",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_alias",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_as_species",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_as_species",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_definition_empty",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_definition_empty",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_label",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_label",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_scientific_name",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_scientific_name",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_protection_swapped",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_protection_swapped",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_reference_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_reference_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_reference_id_format",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_reference_id_format",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_reference_list_duplicate",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_reference_list_duplicate",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_reference_list_empty",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_reference_list_empty",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_reference_orphan",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_reference_orphan",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_renumbered_order",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_renumbered_order",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_schema_2",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_schema_2",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_schema_bool",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_schema_bool",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_species_11",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_species_11",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_species_13",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_species_13",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_species_as_protection",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_species_as_protection",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_species_definition",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_species_definition",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_species_order_with_indices_preserved",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_species_order_with_indices_preserved",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_synonyms_wrong_type",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_synonyms_wrong_type",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_total_13",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_total_13",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_total_15",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_total_15",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_empty_userinfo",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_empty_userinfo",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_fragment",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_fragment",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_homepage",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_homepage",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_query",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_query",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_unofficial",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_unofficial",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_userinfo",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_userinfo",
+        "result": "passed"
+      },
+      {
+        "test": "test_negative_url_whitespace",
+        "class": "test_offline_manifest.ManifestContractTests.test_negative_url_whitespace",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_alias_and_case_whitespace",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_alias_and_case_whitespace",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_common_homonym_separate_namespace",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_common_homonym_separate_namespace",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_complete_contract",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_complete_contract",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_nfc_and_idempotence",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_nfc_and_idempotence",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_rename_preserves_roster_via_alias",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_rename_preserves_roster_via_alias",
+        "result": "passed"
+      },
+      {
+        "test": "test_positive_unknown_and_protection_are_not_scientific",
+        "class": "test_offline_manifest.ManifestContractTests.test_positive_unknown_and_protection_are_not_scientific",
+        "result": "passed"
+      },
+      {
+        "test": "test_normalization_invalid_inputs",
+        "class": "test_offline_manifest.RosterAndTransportTests.test_normalization_invalid_inputs",
+        "result": "passed"
+      },
+      {
+        "test": "test_roster_duplicate_json_keys_rejected",
+        "class": "test_offline_manifest.RosterAndTransportTests.test_roster_duplicate_json_keys_rejected",
+        "result": "passed"
+      },
+      {
+        "test": "test_roster_negative_cases",
+        "class": "test_offline_manifest.RosterAndTransportTests.test_roster_negative_cases",
+        "result": "passed"
+      },
+      {
+        "test": "test_strict_transport_rejections",
+        "class": "test_offline_manifest.RosterAndTransportTests.test_strict_transport_rejections",
+        "result": "passed"
+      }
     ]
   },
-  "hashes": {
-    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
-    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "7edda0086889a406c75d1198cd27a87bfc376c1e39f05a4ab69af5a8c3281ddf",
-    "docs/phase1/offline-class-manifest.v1.json": "39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5",
-    "docs/phase1/F1-MAN01-offline-class-manifest.md": "77afe6fd3350134af57201417df5bbd377b7b9e96b177ef0b9791a66d49f2280",
-    "scripts/phase1/validate_offline_manifest.py": "d9010fd498b28b371c68160c5a7341714638dcd1320e8a01fd256314ab96618b",
-    "scripts/phase1/test_offline_manifest.py": "5c2b93a368173dd02ff5a2f23c2017fef9e1beef383cc12b88f77b347f42564b"
-  },
-  "approved_planning_digest": "246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5",
   "commands": [
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
         "-m",
         "unittest",
         "discover",
-        "-v",
         "-s",
         "scripts/phase1",
         "-p",
-        "test_offline_manifest.py"
+        "test_offline_manifest.py",
+        "-v"
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:56.381445+00:00",
       "exit_code": 0,
-      "tests_run": 81
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stderr_sha256": "cf1307ababed09562e1181d8ecaa47ae621e304c3e290ffc203f8ed6c76445cf"
     },
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
         "scripts/phase1/validate_offline_manifest.py",
         "--manifest",
         "docs/phase1/offline-class-manifest.v1.json",
         "--roster",
         "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:56.481824+00:00",
       "exit_code": 0,
-      "result": {
-        "classes": 14,
-        "manifest_sha256": "39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5",
-        "manifest_version": "1.0.0",
-        "normalization_version": "1",
-        "protection": 2,
-        "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
-        "schema_version": 1,
-        "species": 12,
-        "valid": true
-      }
+      "stdout_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
-        "/home/aluno/.agents/skills/_shared/scripts/bm.py",
-        "change-policy"
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "route",
+        "docs/living/PROJECT_STATE.md"
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:56.714305+00:00",
       "exit_code": 0,
-      "result": {
-        "action": "decide_reversibly_record_if_material_and_continue",
-        "classification": "implementation_detail",
-        "extra_review_required": false,
-        "plan_files_mutable": false,
-        "plan_invalidating": false,
-        "reapproval_required": false,
-        "redesign_allowed": false
-      }
+      "stdout_sha256": "fd146f208e19de491b812e1ecf1535149d4170d4ec102245e88f0be8c498b799",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
-        "/home/aluno/.agents/skills/_shared/scripts/bm.py",
-        "validate-state",
-        "docs/living/PROJECT_STATE.md"
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "repo-hygiene",
+        "check",
+        "--repo",
+        "."
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:56.943063+00:00",
       "exit_code": 0,
-      "result": {
-        "method_version": 2,
-        "valid": true
-      }
+      "stdout_sha256": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+    },
+    {
+      "command": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "workspace",
+        "check",
+        "--repo",
+        "."
+      ],
+      "cwd": ".",
+      "executed_at": "2026-09-14T22:39:57.167555+00:00",
+      "exit_code": 0,
+      "stdout_sha256": "4dc3faa7d541187e8e4de6b061195268e6f19aef3cc16e44e095e4eed0fa9f5a",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
-        "/home/aluno/.agents/skills/_shared/scripts/bm.py",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
         "planning-audit",
         "docs/living/PROJECT_STATE.md",
         "--root",
         ".",
         "--strict"
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:57.444210+00:00",
       "exit_code": 0,
-      "result": {
-        "budget_exceeded": [],
-        "limits": {
-          "execution_units": 40,
-          "max_execution_unit_words": 8000,
-          "max_plan_words": 16000,
-          "plans": 16,
-          "platforms": 6,
-          "shared_context_words": 24000
-        },
-        "metrics": {
-          "execution_units": 6,
-          "max_execution_unit_words": 526,
-          "max_plan_words": 607,
-          "package_words": 15358,
-          "plans": 5,
-          "platforms": 2,
-          "shared_context_words": 1937
-        },
-        "profile": "standard",
-        "quality_contract": "planning-quality-v2",
-        "readiness": {
-          "counts": {
-            "assumptions": 6,
-            "decisions": 12,
-            "design_surfaces": 0,
-            "pitfalls": 12,
-            "spec_deltas": 4,
-            "spikes": 3,
-            "user_actions": 4
-          },
-          "coverage_gaps": [],
-          "design": null,
-          "design_required": false,
-          "scope_digest": "581b4bcc7b5ff777c9fd6b8e655862bb780b7d5f69e228056b3d644a94b5d9e3",
-          "spec_deltas": [
-            {
-              "id": "SD-001",
-              "source": "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
-              "target": "docs/bianchini/current/specs/replan-v2.md"
-            },
-            {
-              "id": "SD-006",
-              "source": "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
-              "target": "docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md"
-            },
-            {
-              "id": "SD-101",
-              "source": "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
-              "target": "docs/bianchini/current/specs/provider-benchmark-decision.md"
-            },
-            {
-              "id": "SD-201",
-              "source": "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
-              "target": "docs/bianchini/current/specs/offline-class-manifest.md"
-            }
-          ],
-          "status": "ready"
-        },
-        "recommended_profile": "standard",
-        "research_mode": "repo_only",
-        "valid": true,
-        "warnings": []
-      }
+      "stdout_sha256": "5267127254e4fee589df096cf92a6221db28e9255192bcd3f0bd7ed21f28bdc7",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
+    },
+    {
+      "command": [
+        "python3",
+        "-B",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "validate-state",
+        "docs/living/PROJECT_STATE.md"
+      ],
+      "cwd": ".",
+      "executed_at": "2026-09-14T22:39:57.655173+00:00",
+      "exit_code": 0,
+      "stdout_sha256": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
-        "/home/aluno/.agents/skills/_shared/scripts/bm.py",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
         "snapshot",
         "verify",
         "docs/living/PROJECT_STATE.md",
         "--root",
         "."
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:57.910941+00:00",
       "exit_code": 0,
-      "result": {
-        "algorithm": "sha256-manifest-v1",
-        "digest": "246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5",
-        "manifest": "/tmp/scanplant-p05-workspace/artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256"
-      }
+      "stdout_sha256": "8d86d39d2bee4a2ea0b53a651a8fbf7a942a299846d8c48a6ceb8113b7327c34",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
-        "sha256sum",
-        "-c",
-        "--strict",
-        "artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256"
-      ],
-      "cwd": ".",
-      "exit_code": 0,
-      "entries_ok": 23
-    },
-    {
-      "argv": [
-        "/usr/bin/python3",
+      "command": [
+        "python3",
         "-B",
-        "/home/aluno/.agents/skills/_shared/scripts/bm.py",
-        "repo-hygiene",
-        "check",
-        "--repo",
+        "/home/administradorarthur/.agents/skills/_shared/scripts/bm.py",
+        "snapshot",
+        "verify",
+        "/tmp/p05-r1-initial-state.json",
+        "--root",
         "."
       ],
       "cwd": ".",
+      "executed_at": "2026-09-14T22:39:58.159554+00:00",
       "exit_code": 0,
-      "result": {
-        "ignore_rule": "/.superpowers/",
-        "tracked_root_artifacts": [],
-        "valid": true
-      }
+      "stdout_sha256": "c42061e0db297374c6fe69265b1aad94b175f1a708fe2d0989c0ebcecfac91ca",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "argv": [
+      "command": [
         "git",
         "diff",
         "--check"
       ],
       "cwd": ".",
-      "exit_code": 0
-    }
-  ],
-  "test_results": [
-    {
-      "test": "test_cli_no_network_or_writes",
-      "result": "ok"
-    },
-    {
-      "test": "test_cli_valid_invalid_inaccessible_and_invocation",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_cross_canonical",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_equals_canonical",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_infraspecific",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_inter_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_intra_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_no_reference",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_alias_reference_missing",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_array_order",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_authority_invalid",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_canonical_authorship",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_canonical_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_canonical_hybrid",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_canonical_lowercase",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_canonical_whitespace",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_class_wrong_type",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_classes_wrong_type",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_common_empty",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_common_intra_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_control_character",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_date_future",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_date_impossible",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_display_outside_common",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_extra_alias_field",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_extra_class_field",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_extra_root_field",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_hash_wrong",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_id_common_name",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_id_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_boolean",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_float",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_missing",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_outside",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_index_string",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_invisible_character",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_manifest_version",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_name_wrong_type",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_normalization_version",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_absent",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_alias",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_as_species",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_definition_empty",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_label",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_scientific_name",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_protection_swapped",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_reference_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_reference_id_format",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_reference_list_duplicate",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_reference_list_empty",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_reference_orphan",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_renumbered_order",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_schema_2",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_schema_bool",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_species_11",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_species_13",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_species_as_protection",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_species_definition",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_species_order_with_indices_preserved",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_synonyms_wrong_type",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_total_13",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_total_15",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_empty_userinfo",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_fragment",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_homepage",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_query",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_unofficial",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_userinfo",
-      "result": "ok"
-    },
-    {
-      "test": "test_negative_url_whitespace",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_alias_and_case_whitespace",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_common_homonym_separate_namespace",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_complete_contract",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_nfc_and_idempotence",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_rename_preserves_roster_via_alias",
-      "result": "ok"
-    },
-    {
-      "test": "test_positive_unknown_and_protection_are_not_scientific",
-      "result": "ok"
-    },
-    {
-      "test": "test_normalization_invalid_inputs",
-      "result": "ok"
-    },
-    {
-      "test": "test_roster_duplicate_json_keys_rejected",
-      "result": "ok"
-    },
-    {
-      "test": "test_roster_negative_cases",
-      "result": "ok"
+      "executed_at": "2026-09-14T22:39:58.167874+00:00",
+      "exit_code": 0,
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     },
     {
-      "test": "test_strict_transport_rejections",
-      "result": "ok"
+      "command": [
+        "git",
+        "diff",
+        "--cached",
+        "--exit-code"
+      ],
+      "cwd": ".",
+      "executed_at": "2026-09-14T22:39:58.172312+00:00",
+      "exit_code": 0,
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
     }
   ],
-  "negative_expected_codes": [
-    {
-      "case": "total_13",
-      "expected_code": "E_CLASS_COUNT",
-      "result": "passed"
-    },
-    {
-      "case": "total_15",
-      "expected_code": "E_CLASS_COUNT",
-      "result": "passed"
-    },
-    {
-      "case": "species_11",
-      "expected_code": "E_KIND",
-      "result": "passed"
-    },
-    {
-      "case": "species_13",
-      "expected_code": "E_KIND",
-      "result": "passed"
-    },
-    {
-      "case": "protection_absent",
-      "expected_code": "E_CLASS_ID",
-      "result": "passed"
-    },
-    {
-      "case": "protection_duplicate",
-      "expected_code": "E_CLASS_ID",
-      "result": "passed"
-    },
-    {
-      "case": "protection_swapped",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "index_missing",
-      "expected_code": "E_FIELDS",
-      "result": "passed"
-    },
-    {
-      "case": "index_duplicate",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "index_outside",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "index_boolean",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "index_string",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "index_float",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "array_order",
-      "expected_code": "E_INDEX",
-      "result": "passed"
-    },
-    {
-      "case": "renumbered_order",
-      "expected_code": "E_ROSTER_MAPPING",
-      "result": "passed"
-    },
-    {
-      "case": "id_duplicate",
-      "expected_code": "E_CLASS_ID",
-      "result": "passed"
-    },
-    {
-      "case": "id_common_name",
-      "expected_code": "E_CLASS_ID",
-      "result": "passed"
-    },
-    {
-      "case": "canonical_duplicate",
-      "expected_code": "E_NAME_COLLISION",
-      "result": "passed"
-    },
-    {
-      "case": "alias_equals_canonical",
-      "expected_code": "E_NAME_COLLISION",
-      "result": "passed"
-    },
-    {
-      "case": "alias_cross_canonical",
-      "expected_code": "E_NAME_COLLISION",
-      "result": "passed"
-    },
-    {
-      "case": "alias_intra_duplicate",
-      "expected_code": "E_NAME_COLLISION",
-      "result": "passed"
-    },
-    {
-      "case": "alias_inter_duplicate",
-      "expected_code": "E_NAME_COLLISION",
-      "result": "passed"
-    },
-    {
-      "case": "alias_no_reference",
-      "expected_code": "E_EMPTY",
-      "result": "passed"
-    },
-    {
-      "case": "alias_reference_missing",
-      "expected_code": "E_REF_MISSING",
-      "result": "passed"
-    },
-    {
-      "case": "alias_infraspecific",
-      "expected_code": "E_BINOMIAL",
-      "result": "passed"
-    },
-    {
-      "case": "canonical_authorship",
-      "expected_code": "E_BINOMIAL",
-      "result": "passed"
-    },
-    {
-      "case": "canonical_hybrid",
-      "expected_code": "E_BINOMIAL",
-      "result": "passed"
-    },
-    {
-      "case": "canonical_lowercase",
-      "expected_code": "E_BINOMIAL",
-      "result": "passed"
-    },
-    {
-      "case": "canonical_whitespace",
-      "expected_code": "E_BINOMIAL",
-      "result": "passed"
-    },
-    {
-      "case": "common_intra_duplicate",
-      "expected_code": "E_COMMON_DUPLICATE",
-      "result": "passed"
-    },
-    {
-      "case": "common_empty",
-      "expected_code": "E_DISPLAY_NAME",
-      "result": "passed"
-    },
-    {
-      "case": "display_outside_common",
-      "expected_code": "E_DISPLAY_NAME",
-      "result": "passed"
-    },
-    {
-      "case": "invisible_character",
-      "expected_code": "E_UNICODE",
-      "result": "passed"
-    },
-    {
-      "case": "control_character",
-      "expected_code": "E_UNICODE",
-      "result": "passed"
-    },
-    {
-      "case": "protection_as_species",
-      "expected_code": "E_KIND",
-      "result": "passed"
-    },
-    {
-      "case": "species_as_protection",
-      "expected_code": "E_KIND",
-      "result": "passed"
-    },
-    {
-      "case": "protection_scientific_name",
-      "expected_code": "E_PROTECTION",
-      "result": "passed"
-    },
-    {
-      "case": "protection_alias",
-      "expected_code": "E_PROTECTION",
-      "result": "passed"
-    },
-    {
-      "case": "protection_label",
-      "expected_code": "E_PROTECTION",
-      "result": "passed"
-    },
-    {
-      "case": "protection_definition_empty",
-      "expected_code": "E_EMPTY",
-      "result": "passed"
-    },
-    {
-      "case": "species_definition",
-      "expected_code": "E_SPECIES_DEFINITION",
-      "result": "passed"
-    },
-    {
-      "case": "schema_2",
-      "expected_code": "E_SCHEMA",
-      "result": "passed"
-    },
-    {
-      "case": "schema_bool",
-      "expected_code": "E_SCHEMA",
-      "result": "passed"
-    },
-    {
-      "case": "manifest_version",
-      "expected_code": "E_VERSION",
-      "result": "passed"
-    },
-    {
-      "case": "normalization_version",
-      "expected_code": "E_VERSION",
-      "result": "passed"
-    },
-    {
-      "case": "hash_wrong",
-      "expected_code": "E_ROSTER_HASH",
-      "result": "passed"
-    },
-    {
-      "case": "extra_root_field",
-      "expected_code": "E_FIELDS",
-      "result": "passed"
-    },
-    {
-      "case": "extra_class_field",
-      "expected_code": "E_FIELDS",
-      "result": "passed"
-    },
-    {
-      "case": "extra_alias_field",
-      "expected_code": "E_FIELDS",
-      "result": "passed"
-    },
-    {
-      "case": "classes_wrong_type",
-      "expected_code": "E_ARRAY",
-      "result": "passed"
-    },
-    {
-      "case": "class_wrong_type",
-      "expected_code": "E_OBJECT",
-      "result": "passed"
-    },
-    {
-      "case": "synonyms_wrong_type",
-      "expected_code": "E_ARRAY",
-      "result": "passed"
-    },
-    {
-      "case": "name_wrong_type",
-      "expected_code": "E_STRING",
-      "result": "passed"
-    },
-    {
-      "case": "reference_duplicate",
-      "expected_code": "E_REF_DUPLICATE",
-      "result": "passed"
-    },
-    {
-      "case": "reference_orphan",
-      "expected_code": "E_REF_ORPHAN",
-      "result": "passed"
-    },
-    {
-      "case": "reference_id_format",
-      "expected_code": "E_REF_ID",
-      "result": "passed"
-    },
-    {
-      "case": "reference_list_duplicate",
-      "expected_code": "E_REF_DUPLICATE",
-      "result": "passed"
-    },
-    {
-      "case": "reference_list_empty",
-      "expected_code": "E_EMPTY",
-      "result": "passed"
-    },
-    {
-      "case": "date_impossible",
-      "expected_code": "E_DATE",
-      "result": "passed"
-    },
-    {
-      "case": "date_future",
-      "expected_code": "E_DATE_FUTURE",
-      "result": "passed"
-    },
-    {
-      "case": "url_unofficial",
-      "expected_code": "E_URL_AUTHORITY",
-      "result": "passed"
-    },
-    {
-      "case": "url_homepage",
-      "expected_code": "E_URL_AUTHORITY",
-      "result": "passed"
-    },
-    {
-      "case": "url_query",
-      "expected_code": "E_URL",
-      "result": "passed"
-    },
-    {
-      "case": "url_fragment",
-      "expected_code": "E_URL",
-      "result": "passed"
-    },
-    {
-      "case": "url_userinfo",
-      "expected_code": "E_URL",
-      "result": "passed"
-    },
-    {
-      "case": "url_empty_userinfo",
-      "expected_code": "E_URL",
-      "result": "passed"
-    },
-    {
-      "case": "url_whitespace",
-      "expected_code": "E_URL",
-      "result": "passed"
-    },
-    {
-      "case": "authority_invalid",
-      "expected_code": "E_URL_AUTHORITY",
-      "result": "passed"
+  "cli_result": {
+    "aliases": 79,
+    "classes": 14,
+    "manifest_sha256": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+    "manifest_version": "1.1.0",
+    "normalization_version": "1",
+    "protection": 2,
+    "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+    "schema_version": 1,
+    "scientific_keys": 91,
+    "species": 12,
+    "valid": true
+  },
+  "red_baseline": {
+    "proof_id": "proof-93c13d6b0c1affb7122f227180990597",
+    "commit": "c7012b942c36fe93fb136a376a1a73093f1e5aaa",
+    "exit_code": 1,
+    "subsequent_working_tree_red": "92 tests, 91 failing assertions/subtests before implementation"
+  },
+  "alias_reconciliation": {
+    "baseline_commit": "77e93a221dad3115c301b10317b626c236a3ba84",
+    "baseline_manifest_sha256": "39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5",
+    "preliminary_count": 83,
+    "quarantined_count": 4,
+    "resolvable_aliases": 79,
+    "canonicals": 12,
+    "scientific_keys": 91,
+    "exact_set_difference": [
+      "aloe maculata",
+      "aloe variegata",
+      "ficus clusiifolia",
+      "ficus cordata"
+    ],
+    "unexpected_additions": [],
+    "remaining_alias_class_mapping_unchanged": true,
+    "all_other_manifest_values_unchanged": true,
+    "per_class": [
+      {
+        "class_id": "species_01",
+        "preliminary_aliases": 4,
+        "resolvable_aliases": 4
+      },
+      {
+        "class_id": "species_02",
+        "preliminary_aliases": 6,
+        "resolvable_aliases": 6
+      },
+      {
+        "class_id": "species_03",
+        "preliminary_aliases": 3,
+        "resolvable_aliases": 3
+      },
+      {
+        "class_id": "species_04",
+        "preliminary_aliases": 0,
+        "resolvable_aliases": 0
+      },
+      {
+        "class_id": "species_05",
+        "preliminary_aliases": 1,
+        "resolvable_aliases": 1
+      },
+      {
+        "class_id": "species_06",
+        "preliminary_aliases": 11,
+        "resolvable_aliases": 9
+      },
+      {
+        "class_id": "species_07",
+        "preliminary_aliases": 34,
+        "resolvable_aliases": 34
+      },
+      {
+        "class_id": "species_08",
+        "preliminary_aliases": 5,
+        "resolvable_aliases": 5
+      },
+      {
+        "class_id": "species_09",
+        "preliminary_aliases": 12,
+        "resolvable_aliases": 10
+      },
+      {
+        "class_id": "species_10",
+        "preliminary_aliases": 1,
+        "resolvable_aliases": 1
+      },
+      {
+        "class_id": "species_11",
+        "preliminary_aliases": 4,
+        "resolvable_aliases": 4
+      },
+      {
+        "class_id": "species_12",
+        "preliminary_aliases": 2,
+        "resolvable_aliases": 2
+      }
+    ]
+  },
+  "quarantine": [
+    {
+      "name": "Aloe maculata",
+      "normalized_authorless_name": "aloe maculata",
+      "related_class_id": "species_06",
+      "related_canonical_name": "Aloe vera",
+      "related_authorship": "Forssk.",
+      "conflicting_authorship": "All.",
+      "conflicting_taxon": "Aloe maculata (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/530017-1",
+        "https://powo.science.kew.org/taxon/77122815-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Aloe variegata",
+      "normalized_authorless_name": "aloe variegata",
+      "related_class_id": "species_06",
+      "related_canonical_name": "Aloe vera",
+      "related_authorship": "Forssk.",
+      "conflicting_authorship": "L.",
+      "conflicting_taxon": "Gonialoe variegata",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/530017-1",
+        "https://powo.science.kew.org/taxon/530009-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Ficus clusiifolia",
+      "normalized_authorless_name": "ficus clusiifolia",
+      "related_class_id": "species_09",
+      "related_canonical_name": "Ficus elastica",
+      "related_authorship": "Summerh.",
+      "conflicting_authorship": "Schott",
+      "conflicting_taxon": "Ficus clusiifolia (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/60458499-2",
+        "https://powo.science.kew.org/taxon/852625-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
+    },
+    {
+      "name": "Ficus cordata",
+      "normalized_authorless_name": "ficus cordata",
+      "related_class_id": "species_09",
+      "related_canonical_name": "Ficus elastica",
+      "related_authorship": "Kunth & C.D.Bouché",
+      "conflicting_authorship": "Thunb.",
+      "conflicting_taxon": "Ficus cordata (espécie aceita distinta)",
+      "source_urls": [
+        "https://powo.science.kew.org/taxon/60458499-2",
+        "https://powo.science.kew.org/taxon/852662-1"
+      ],
+      "consulted_on": "2026-09-11",
+      "status": "quarantined",
+      "reason": "A forma binomial normalizada sem autoria identifica entidades nomenclaturais distintas; inelegível como chave authorless do ScanPlant.",
+      "nomenclatural_synonymy_retained": true,
+      "scientific_resolution": null,
+      "decision_ref": "U-201 / P05-R1"
     }
   ],
-  "pending_gates": [
-    "Resolve documented taxonomic ambiguity at U-201 without silent contract changes",
-    "Final human taxonomic review tied to manifest/roster bytes",
-    "Codex commit-bound convergence proof unavailable while staging/commit prohibited"
-  ],
-  "final_plan_status": "blocked",
-  "release_status": "pending",
-  "staged": false,
-  "committed": false,
-  "pushed": false,
-  "u201_status": "scope_input_recorded_taxonomy_blocked_final_review_pending",
+  "quarantined_resolutions": {
+    "Aloe maculata": null,
+    "Aloe variegata": null,
+    "Ficus clusiifolia": null,
+    "Ficus cordata": null
+  },
   "taxonomy_gate": {
-    "status": "blocked",
-    "reason": "Four authorless binomials refer to distinct taxa depending on authorship; the frozen spec blocks delivery at U-201. No silent alias removal or contract modification.",
-    "names": [
-      "Aloe maculata",
-      "Aloe variegata",
-      "Ficus clusiifolia",
-      "Ficus cordata"
-    ],
-    "consulted_on": "2026-09-11",
-    "evidence": "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md"
+    "policy": "approved",
+    "evidence": "updated_from_existing_official_sources",
+    "source_consulted_on": "2026-09-11",
+    "network_consultation_this_run": false,
+    "final_human_bytes_acceptance": "pending"
   },
-  "repository_documentary_scan": {
-    "command": [
-      "python3",
-      "-B",
-      "/tmp/p05-final-audit.py"
-    ],
-    "cwd": ".",
-    "exit_code": 0,
-    "json_files": 113,
-    "strict_transport_passed": 106,
-    "preexisting_transport_exceptions": [
-      {
-        "path": "ScanPlantAPI/ScanPlantAPI/Properties/launchSettings.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": true,
-        "final_newline": true
-      },
-      {
-        "path": "artifacts/bianchini/v1/evidence/P01-R1-final-sanitized-inconclusive/mutation-report.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      },
-      {
-        "path": "artifacts/bianchini/v2/evidence/P01-manual-final-v3/results/reports/mutation-report.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      },
-      {
-        "path": "artifacts/bianchini/v2/evidence/P01-manual-final-v5/results/reports/mutation-report.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      },
-      {
-        "path": "scanplant-web/metadata.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      },
-      {
-        "path": "scanplant-web/tsconfig.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      },
-      {
-        "path": "scanplant-web/tsconfig.node.json",
-        "status": "preexisting_transport_exception",
-        "code": "E_ENCODING",
-        "unchanged_from_head": true,
-        "strict_syntax_after_in_memory_transport_normalization": "passed",
-        "bom": false,
-        "final_newline": false
-      }
-    ],
+  "documentary_scan": {
     "all_json_syntax_valid": true,
-    "changed_files": [
-      "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
-      "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
-      "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md",
-      "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json",
-      "artifacts/bianchini/v2/ledgers/P05.md",
-      "docs/living/PROJECT_STATE.md",
-      "docs/phase1/F1-MAN01-offline-class-manifest.md",
-      "docs/phase1/offline-class-manifest.v1.json",
-      "scripts/phase1/test_offline_manifest.py",
-      "scripts/phase1/validate_offline_manifest.py"
+    "json_jsonl_files": 120,
+    "preexisting_transport_exceptions_unchanged": [
+      "ScanPlantAPI/ScanPlantAPI/Properties/launchSettings.json",
+      "artifacts/bianchini/v1/evidence/P01-R1-final-sanitized-inconclusive/mutation-report.json",
+      "artifacts/bianchini/v2/evidence/P01-manual-final-v3/results/reports/mutation-report.json",
+      "artifacts/bianchini/v2/evidence/P01-manual-final-v5/results/reports/mutation-report.json",
+      "scanplant-web/metadata.json",
+      "scanplant-web/tsconfig.json",
+      "scanplant-web/tsconfig.node.json"
     ],
-    "utf8_lf_final_newline_whitespace_changed_files": "passed",
+    "changed_utf8_lf_final_newline": "passed",
+    "guard_empty_lock": "operational lock, not text evidence",
+    "secret_pii_findings": [],
     "scope_check": "passed",
     "ledger_append_only": true,
-    "secret_pii_pattern_findings": [],
-    "scan_limits": "Pattern scan plus manual review; no exhaustive guarantee for arbitrary secrets. Synthetic test URL userinfo is not a credential.",
-    "binary_image_dataset_external_response_diff": "none; authorized text paths and manual content review",
-    "reproduction": "Enumerate git ls-files --cached --others --exclude-standard; strict_load JSON or each JSONL line. Inspect legacy transport exceptions in memory for strict syntax and compare byte-for-byte with HEAD. Scan modified/untracked authorized paths for UTF-8/BOM/CR/newline/whitespace and common private-key/token/email/CPF/JWT patterns without echoing values."
-  },
-  "final_state_validation": {
-    "command": [
-      "python3",
-      "-B",
-      "/home/aluno/.agents/skills/_shared/scripts/bm.py",
-      "validate-state",
-      "docs/living/PROJECT_STATE.md"
-    ],
-    "cwd": ".",
-    "exit_code": 0,
-    "plan_status_checked": "blocked"
+    "historical_packages_unchanged": true,
+    "roster_unchanged": true,
+    "prior_plans_and_release_preserved": true
   },
   "checksum_validation": {
     "command": [
       "sha256sum",
       "-c",
       "--strict",
       "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS"
     ],
-    "cwd": ".",
     "coverage": 7,
-    "note": "Self-referential report hash excluded from this JSON; final seal is verified externally and its actual result appended to ledger."
-  }
+    "note": "Report cannot contain its own final hash. Seven-file seal and actual checksum result recorded externally after generation."
+  },
+  "convergence": {
+    "sidecar": "artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json",
+    "fix_rounds_used": 1,
+    "redesigns": 0,
+    "working_tree_B1": "corrected and tested",
+    "commit_bound_B1": "open until authorized implementation commit and proof",
+    "phase": "fixing",
+    "reason": "User explicitly requires uncommitted implementation at final human gate; no fabricated commit proof."
+  },
+  "human_review": {
+    "status": "pending",
+    "request": "Accept final bytes and authorize implementation commit/push",
+    "approved_by": null
+  },
+  "release_status": "pending",
+  "implementation_staged": false,
+  "implementation_committed": false,
+  "pushed": false,
+  "pending_gates": [
+    "final human bytes acceptance",
+    "authorized implementation commit then commit-bound Codex proof/review"
+  ]
 }
diff --git a/artifacts/bianchini/v2/ledgers/P05.md b/artifacts/bianchini/v2/ledgers/P05.md
index be2c349..7341867 100644
--- a/artifacts/bianchini/v2/ledgers/P05.md
+++ b/artifacts/bianchini/v2/ledgers/P05.md
@@ -339,10 +339,117 @@ mudança contratual nova nem autorização para alterar os digests históricos.

 Checker aplicável será revalidado pelo planning-audit e snapshot contra a passagem 1
 aprovada; não criar outra passagem sem mudança factual no pacote. Registrar aprovação
 altera apenas estado e este append, ambos fora do manifesto congelado.

 Validações da aprovação: planning-audit --strict (inclui checker vigente), validate-state,
 snapshot verify P05-R1/histórico P05, workspace check, repo-hygiene e git diff --check
 passaram. Os 14 arquivos passaram em JSON/JSONL/blocos JSON estritos e UTF-8/LF/newline;
 varredura do delta sem segredos/dados pessoais novos. Oito artefatos de implementação
 permanecem byte a byte conforme preflight. Ambos os digests aprovados estão inalterados.
+
+## 2026-09-14T22:42:13.330871+00:00 — P05-R1 implementado; gate humano dos bytes finais
+
+Commit local único do planejamento/aprovação: c7012b942c36fe93fb136a376a1a73093f1e5aaa, título
+chore(p05-r1): approve alias quarantine plan; 14 arquivos exatos, sem implementação.
+Git status vazio após o commit; workspace resume confirmou identity v2-p05-r1,
+linked worktree seguro na branch bm/v2-p05-r1. Nenhum push ou merge.
+
+Brief/report/checkpoint e revisão em artifacts/bianchini/v2/codex/P05-R1/.
+Brief oficial --tasks 1 emitiu kind task por unidade única, unit_digest
+7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6;
+modo grouped/plan_gate preservado, nenhuma tarefa/grupo artificial.
+Policy parser low/standard confirmou modo e mutation not_required; nenhum contador
+histórico P01/P03 alterado. Guard da skill usada para sidecar T1, sem campos de
+convergência adicionados ao PROJECT_STATE.
+
+RED baseline: proof-93c13d6b0c1affb7122f227180990597 do guard, exit 1 real no commit
+c7012b942c36fe93fb136a376a1a73093f1e5aaa; os quatro homônimos resolviam. Freeze consolidou B1
+no seam offline-manifest-contract; fix round 1 iniciou a correção da única unidade.
+Teste expandido antes da implementação: 92 testes, 91 falhas em asserções/subcasos.
+Depois da correção e inclusão da verificação de evidência: 94/94, zero erro/falha/skip;
+81 testes anteriores preservados, 13 novos. Nenhuma rodada adicional, redesign ou hardening.
+
+Removidos somente os quatro aliases de synonyms. scientific_map rejeita suas formas
+normalizadas como alias/canônico com E_NAME_QUARANTINED, sem normalização nova.
+Manifesto válido resolve os quatro para None. Versionamento 1.1.0 aplicado; fontes,
+roster, demais campos/classes e aliases inalterados. Igualdade de conjuntos e mapa
+por classe comprovada contra 77e93a e hash do baseline: 83−4=79, 12 canônicos, 91 chaves.
+Quarentena mantém as duas autorias, táxon conflitante, fontes, motivo e estado explícito;
+fontes de 2026-09-11 reutilizadas, sem rede taxonômica ou fato botânico novo inferido.
+
+Detalhe reversível: guarda normalizada no validador existente, schema inalterado;
+bm change-policy sem flags retornou implementation_detail/continuar. Adaptação
+operacional por instrução humana de manter implementação sem commit: change-policy
+--plan-command retornou bounded_amendment, plan_invalidating false, sem reapproval.
+Guard decision registrou o motivo: proof executa somente commit real, portanto não
+submeter delta fictício ou marcar B1/gates/complete com provas do baseline. Sidecar
+artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json fica fixing; B1 resolvido na
+working tree, confirmação no commit posterior aguarda autorização. A parada é o gate
+humano final solicitado; não categoria stopped nem impossibilidade de implementação.
+
+A spec/delta aplicáveis já formalizam inelegibilidade de entidades nomenclaturais
+distintas sob mesma chave authorless. Permanecem congelados junto aos dois digests;
+current/specs é sincronização prevista somente no encerramento regular, fora desta
+rodada sem release/homologação. Não houve novo plano ou revisão do pacote aprovado.
+
+### Gates da working tree
+
+Python 3.14.4 -B, stdlib; histórico Python 3.12.3 registrado sem mudar contrato.
+Cwd raiz deste workspace. Comandos/exit codes/horários/digests de stdout/stderr e
+hashes dos seis inputs constam em validation-report.json; seu próprio hash é externo.
+
+- unittest discover scripts/phase1 test_offline_manifest.py: 94/94 passed.
+- CLI validate_offline_manifest.py: exit 0, 1.1.0, 12 species, 2 protection, 14 classes,
+  79 aliases e 91 chaves; testes incluem reintrodução nas 12 classes e normalização.
+- route v2, repo-hygiene, workspace check, planning-audit --strict (checker 1 vigente),
+  validate-state e snapshots P05-R1/histórico P05: todos exit 0.
+- Parse estrito global: 120 arquivos JSON/JSONL/estado/sidecar antes dos últimos
+  artefatos de checkpoint; sete exceções históricas de transporte idênticas ao HEAD,
+  sintaxe válida após normalização apenas em memória. Nenhuma exceção em arquivo alterado.
+- UTF-8 sem BOM/LF/newline e whitespace dos novos/modificados: passed; lock vazio
+  operacional do guard não é documento textual. Blocos JSON novos também estritos.
+- Varredura de padrões de segredos/PII e revisão do delta: sem achados em adições;
+  URLs sintéticas existentes não são credenciais. Sem valor sensível em diagnóstico.
+- git diff --check e índice vazio: exit 0. Roster, 12 classes e oito campos imutáveis
+  por comparação com baseline; ledger prefixo exato do commit; P01/P03/P02/P04/release preservados.
+- SHA256SUMS após geração do relatório: 7/7 OK, exit 0.
+
+Manifesto final SHA-256: bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c.
+Roster SHA-256: 350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b.
+SHA256SUMS SHA-256: 9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e.
+Os sete hashes completos e lista de arquivos do commit estão em codex/P05-R1/FINAL_REVIEW.md.
+
+P05 continua blocked, P05-R1 in_progress, U-201 política/pacote aprovados e bytes
+finais aguardando aceite. Nenhuma aprovação de bytes simulada. Implementação unstaged,
+nenhum commit de implementação/push/merge, provider, credencial, imagem, dataset,
+treino, modelo, produto, .NET/npm/Android/Docker/banco/Stryker, instalação ou release.
+Worktree bm/v2-p03 e backup externo não editados/removidos. Próximo passo único:
+aceite humano dos bytes finais e autorização para commit e push.
+
+Conferência final após checkpoint/revisão: 121 arquivos JSON/JSONL/estado/sidecar
+com sintaxe estrita, sete exceções históricas de transporte preservadas, três blocos
+JSON novos/modificados válidos; zero achados de segredos/PII nas adições. Nove arquivos
+rastreados modificados e 11 artefatos operacionais novos, todos unstaged; índice vazio.
+Os sete hashes finais permanecem idênticos aos de FINAL_REVIEW.md e SHA256SUMS passou
+7/7 novamente. validate-state e ambos os snapshots passaram após o estado final.
+Backup externo: sha256sum -c --strict BACKUP-SHA256SUMS, somente leitura no diretório
+do backup, exit 0, 9/9 OK. Worktree antigo continua em a34da4/bm/v2-p03, sem edição.
+json.tool do relatório também passou; nenhum novo teste ou mudança de implementação
+após o GREEN final, apenas registros mínimos de revisão/checkpoint.
+
+## 2026-09-14T22:57:38.859020+00:00 — Aceite humano reafirmado e retomada do encerramento
+
+O responsável reafirmou explicitamente o aceite dos oito SHA-256 e a autorização dos
+dois commits previstos e de um único push sem força da branch bm/v2-p05-r1. Registro
+completo dos hashes: artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json.
+U-201 resolved/consumed. Os registros pending nos artefatos selados são históricos;
+este append registra o aceite posterior sem alterar nenhum dos oito bytes aceitos.
+
+Retomada no HEAD c7012b942c36fe93fb136a376a1a73093f1e5aaa, índice vazio, nove
+modificados e 11 novos idênticos ao backup pré-commit. BACKUP-SHA256SUMS 10/10,
+tar íntegro e correspondência 20/20. Branch remota P05-R1 ausente; referências
+P03 807fd3bf5f81d4b4b33dbc325891f6ee1d3a52d2 e checkpoint P05
+77e93a221dad3115c301b10317b626c236a3ba84 preservadas.
+
+P05/P05-R1 aguardam apenas a prova formal do commit autorizado; não se antecipa
+conclusão do guard. Planejamento congelado, P01/P03-R6, P02/P04 e release preservados.
diff --git a/docs/living/PROJECT_STATE.md b/docs/living/PROJECT_STATE.md
index e704384..3c346d5 100644
--- a/docs/living/PROJECT_STATE.md
+++ b/docs/living/PROJECT_STATE.md
@@ -5,21 +5,21 @@
   "planning_status": "approved",
   "execution_policy": "adaptive",
   "assurance_profile": "standard",
   "architecture_audit": "optional",
   "architecture_audit_status": "not_run",
   "manual_pdf": "scope",
   "scope": {
     "status": "approved",
     "source": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md",
     "approved_at": "2026-09-14T22:30:45.431487+00:00",
-    "authorization_scope": "Aprovação humana explícita nesta sessão do digest P05-R1 6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f, quarentena de quatro homônimos, versão 1.1.0, 79 aliases e 91 chaves. Autorizados commit local único de planejamento e execução completa da unidade. Implementação permanece unstaged, sem commit ou push até aceite humano final dos bytes."
+    "authorization_scope": "Aprovação humana explícita nesta sessão do digest P05-R1 6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f, quarentena de quatro homônimos, versão 1.1.0, 79 aliases e 91 chaves. Autorizados commit local único de planejamento e execução completa da unidade. Implementação permanece unstaged, sem commit ou push até aceite humano final dos bytes. Aceite humano posterior dos oito hashes e autorização explícita dos dois commits de encerramento e push único reafirmados na retomada; registro artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json."
   },
   "planning": {
     "quality_version": 2,
     "research_mode": "repo_only",
     "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md",
     "readiness": "docs/bianchini/changes/v2/READINESS-p05-r1.md",
     "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md",
     "spec": "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
     "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md",
     "checker": {
@@ -194,21 +194,21 @@
       "gates": [
         "approved-species-roster",
         "manifest-contract-validation",
         "taxonomic-human-review",
         "documentary-integrity"
       ]
     },
     {
       "id": "P05-R1",
       "path": "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
-      "status": "approved",
+      "status": "in_progress",
       "risk": "low",
       "execution": "grouped",
       "review": "plan_gate",
       "test_seams": [
         "offline-manifest-contract",
         "normalize_name",
         "scientific_map",
         "resolve_scientific_name"
       ],
       "depends_on": [
@@ -222,33 +222,33 @@
         "documentary-integrity"
       ]
     }
   ],
   "verification": {
     "fast": {
       "commands": [
         "python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'",
         "python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
       ],
-      "status": "pending",
-      "scope": "P05-R1 futuro: aliases authorless/quarentena, conjunto 83 menos 4 comprovado, minor 1.1.0 e aceite final. Não executado nesta rodada; provas do baseline não certificam a mudança."
+      "status": "passed",
+      "scope": "P05-R1 working tree Python 3.14.4 -B: 94/94 testes documentais (81 anteriores + 13 novos), CLI 1.1.0, 79 aliases, 12 canônicos, 91 chaves; hashes em validation-report.json. Não é prova de commit da implementação."
     },
     "plan": {
       "commands": [
         "python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'",
         "python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
         "python3 -B -m json.tool artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json",
         "sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
         "git diff --check"
       ],
       "status": "pending",
-      "scope": "P05-R1 futuro: aliases authorless/quarentena, conjunto 83 menos 4 comprovado, minor 1.1.0 e aceite final. Não executado nesta rodada; provas do baseline não certificam a mudança."
+      "scope": "Aceite humano dos oito hashes recebido; gates finais e provas vinculadas ao commit da implementação pendentes. Evidências posteriores em artifacts/bianchini/v2/codex/P05-R1/closure-verification.json."
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
@@ -259,21 +259,26 @@
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
+    "plan_id": "P05-R1",
+    "unit": "1",
+    "workspace": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
+    "gate": "commit-bound-final-verification"
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
@@ -299,33 +304,23 @@
     },
     {
       "id": "B-P03-R5-U008-TERMINAL-TEST-PROJECT-SELECTION",
       "summary": "U-008 iniciou Stryker com TestProjects vazio; ScanPlantAPI.sln selecionou ScanPlantAPI.Tests.csproj multi-target, NETSDK1045 ocorreu antes de mutantes, campaign_count=1 e U-008 foi consumida sem retry.",
       "evidence": "artifacts/bianchini/v2/checkpoints/P03-R5-U008-terminal-attempt-716ef26.json"
     },
     {
       "id": "B-P03-R6-U009-TERMINAL-VSTEST-CONNECTION",
       "summary": "P03-R6/U-009 foi invocada uma única vez via Bash: campaign_count=2, campaign_executed=true, U-008=consumed_non_reusable, U-009=consumed, exit_code=134 e failure_stage=campaign. Stryker 4.16.0 iniciou, mas falhou ao conectar a vstest.console após 90 segundos antes de produzir mutantes, mutation-report ou mutation score. Falha posterior ao marcador é terminal e não admite retry R6.",
       "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909"
-    },
-    {
-      "id": "B-P05-FINAL-HUMAN-REVIEW",
-      "summary": "U-201: aprovação do pacote P05-R1/digest recebida; falta produzir e aceitar humanamente os bytes finais e hashes. Não completar P05 antes desse aceite.",
-      "evidence": "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md"
-    },
-    {
-      "id": "B-P05-U201-TAXONOMIC-HOMONYMS",
-      "summary": "Política e pacote P05-R1 aprovados pelo responsável; implementação autorizada. Homônimos serão removidos apenas das chaves authorless, com quarentena preservada. Aceite dos bytes finais continua pendente.",
-      "evidence": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md"
     }
   ],
-  "next_action": "Criar somente o commit local chore(p05-r1): approve alias quarantine plan com pacote e registros mínimos; executar P05-R1 no workspace isolado. Ao final, deixar implementação unstaged e aguardar aceite humano dos bytes/hashes e autorização de commit/push; preservar P01/P03-R6, P02/P04 e release.",
+  "next_action": "Concluir validações finais, commit autorizado da implementação, provas/revisão do guard nesse SHA e encerramento documental P05/P05-R1; publicar bm/v2-p05-r1 em push único sem força. Aceite U-201 registrado; release pending.",
   "continuity_decision": {
     "recommended_alternative": "A",
     "status": "approved",
     "next_milestone": "F1-API01",
     "proposed_plan": "P04",
     "document": "docs/bianchini/changes/v2/POST-U009-DELIBERATION.md",
     "release_authorized": false,
     "new_mutation_campaign_authorized": false
   },
   "terminal_campaign": {
@@ -360,25 +355,26 @@
     "execution_status": "completed",
     "state_at_revision": "a34da4dd34eea58921862f0d0fa2d0016be5ce31",
     "note": "Registro histórico, não revalidar manifesto antigo contra ledger/evidências vivos posteriores."
   },
   "next_milestone_proposal": {
     "plan": "P05",
     "functional_id": "F1-MAN01",
     "title": "Manifesto canônico das 12 espécies offline, sinônimos e duas classes de proteção",
     "status": "blocked",
     "roster_boundary": "U-201",
-    "u201_status": "quarantine_plan_approved_execution_authorized_final_bytes_pending",
+    "u201_status": "resolved_consumed",
     "execution_authorized": true,
     "release_authorized": false,
     "new_mutation_campaign_authorized": false,
-    "replan": "P05-R1"
+    "replan": "P05-R1",
+    "human_acceptance": "artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json"
   },
   "prior_p05_approval": {
     "status": "approved",
     "approved_at": "2026-09-11T18:23:11Z",
     "approved_by": "responsável humano",
     "approved_plans": [
       "P01",
       "P02",
       "P03",
       "P04",
diff --git a/docs/phase1/F1-MAN01-offline-class-manifest.md b/docs/phase1/F1-MAN01-offline-class-manifest.md
index 988776a..a1d9c3e 100644
--- a/docs/phase1/F1-MAN01-offline-class-manifest.md
+++ b/docs/phase1/F1-MAN01-offline-class-manifest.md
@@ -1,14 +1,14 @@
-# F1-MAN01 — contrato offline 1.0.0
+# F1-MAN01 — contrato offline 1.1.0

-Estado: implementação documental preliminar bloqueada em U-201 por quatro
-binomiais homônimos; revisão humana dos bytes finais pendente.
+Estado: P05-R1 implementado e validado na árvore de trabalho; os quatro homônimos
+estão quarantined e inelegíveis no mapa. Aceite humano dos bytes finais pendente em U-201.
 O manifesto não está liberado para consumo por produto ou treinamento.

 ## Entrada, identidade e ordem

 A decisão humana corrigida de U-201 está transcrita em
 `artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md` e materializada
 em `approved-species-roster.json` no mesmo diretório. O registro usa a data UTC
 real e o papel responsável humano. A antiga enumeração de sinônimos foi revogada;
 não constitui allowlist. O digest histórico do planejamento continua
 `246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5`.
@@ -31,21 +31,21 @@ não constitui allowlist. O digest histórico do planejamento continua
 | 14 | 13 | imagem_invalida | proteção | Imagem inválida |

 As primeiras cinco posições preservam o piloto; as sete novas seguem a ordem
 alfabética aprovada. A ordem humana é determinística e não representa confiança,
 prioridade ou parentesco. IDs opacos não derivam de nomes ou sinônimos. Nenhuma
 ordenação automática posterior pode mudar os índices. As proteções não são espécies.

 ## Formato e resolução

 `offline-class-manifest.v1.json` usa schema_version inteiro 1, manifest_version
-string 1.0.0 e normalization_version string 1. O hash do roster corresponde aos
+string 1.1.0 e normalization_version string 1. O hash do roster corresponde aos
 bytes exatos da entrada registrada. Objetos são fechados; tipos não são coercíveis.
 JSON deve ser UTF-8 sem BOM, LF, com newline final, sem chaves duplicadas ou números
 não finitos. Cada espécie contém nome científico binomial sem autoria, rótulo
 pt-BR, nomes comuns, sinônimos referenciados e fontes taxonômicas datadas.

 Normalização: NFC, trim, colapso de whitespace Unicode em espaço ASCII e casefold,
 nesta ordem. Não remove acentos, pontuação ou autoria; não faz aproximação.
 Controles não whitespace e formatação invisível são inválidos. Chaves repetidas,
 mesmo na própria classe, são erro. Nomes comuns pertencem a outro namespace;
 homônimos entre espécies seriam documentados, sem resolução científica implícita.
@@ -54,68 +54,86 @@ No roster real os 12 rótulos comuns são distintos.
 As funções públicas em `scripts/phase1/validate_offline_manifest.py` são
 `normalize_name(texto)` e `resolve_scientific_name(manifesto_validado, texto)`.
 A segunda recebe um manifesto já validado; retorna class_id por igualdade exata,
 ou None (null em uma serialização JSON) para texto desconhecido. Não retorna
 proteção para ausência de correspondência. O catálogo de aliases se limita ao
 escopo aprovado; não é um resolvedor taxonômico universal. Autorias e homônimos
 nomenclaturais estão explicitados na revisão taxonômica para aceite humano.

 Sinônimos provêm da seção direta Synonyms da espécie aceita no POWO. A evidência
 relaciona cada nome, autoria, relação e exclusão; não herda sinônimos de variedades
-ou subespécies. São 83 aliases binomiais preliminares; quatro têm ambiguidade
-comprovada na revisão e não foram aceitos como chaves finais. Spathiphyllum wallisii tem lista vazia
+ou subespécies. O baseline tinha 83 aliases binomiais. A diferença exata de conjuntos removeu
+somente Aloe maculata, Aloe variegata, Ficus clusiifolia e Ficus cordata, preservados
+na evidência como quarantined com ambas as autorias, táxon conflitante, fontes e motivo.
+São exatamente 79 aliases resolvíveis e, com os 12 canônicos, 91 chaves científicas.
+Um alias sem autoria é inelegível se a mesma forma normalizada identifica entidades
+nomenclaturais distintas nas fontes consideradas. Quarentena não nega sinonímia da fonte.
+Os quatro retornam None/null, inclusive com caixa/whitespace normalizados; sua reinserção
+no mapa provoca E_NAME_QUARANTINED. Outro homônimo encontrado bloqueia aceitação até
+revisão explícita. Nenhum outro alias elegível foi removido. Spathiphyllum wallisii tem lista vazia
 justificada pela página consultada. Nenhum nome infraspecífico é alias.

 ## Proteções e consumidores futuros

 `outra_planta` designa imagem utilizável de planta cuja identidade de referência
 está fora das 12 espécies. Não é um nome de espécie nem consequência automática
 de baixa confiança. `imagem_invalida` designa conteúdo sem planta ou sem informação
 suficiente para atribuição botânica única: vazio, objeto não vegetal, enquadramento
 insuficiente ou mistura sem alvo inequívoco. Bytes ilegíveis são erro de entrada.

 Treino e inferência futuros deverão usar as mesmas 14 posições, IDs e SHA-256.
 Catálogo futuro vinculará as 12 espécies por class_id e não inventará cuidados
 para proteções. Nenhum consumidor, tensor, modelo ou fluxo híbrido é implementado.
 Não há afirmação de acurácia, latência, compatibilidade medida com Redmi A5 ou
 disponibilidade comprovada de imagens.

 Versionamento: mudança estrutural altera schema_version; quantidade, identidade
 ou ordem exigem major e aprovação de escopo; alteração da resolução de nomes
 exige minor e revisão de colisões; metadados sem efeito na resolução podem ser patch.
-Cada versão aceita fixa os hashes dos bytes, sem regeneração silenciosa.
+P05-R1 aplica o incremento minor 1.0.0 → 1.1.0 aprovado, pois mudou a resolução sem
+mudar identidade, quantidade ou ordem das classes; schema_version e normalization_version
+permanecem 1. Cada versão aceita fixa os hashes dos bytes, sem regeneração silenciosa.

 ## Validação reproduzível

-Python 3.12, somente biblioteca padrão, cwd na raiz do workspace:
+Python 3.14.4 disponível nesta execução, com -B e somente biblioteca padrão; evidência
+histórica usou Python 3.12.3. Essa diferença não altera o contrato. Cwd na raiz do workspace:

 ```bash
 python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'
 python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json
 sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
 git diff --check
 ```

 A CLI não escreve arquivos, não usa rede ou cache. Exit 0 indica contrato válido;
 1, contrato inválido; 2, invocação inválida ou arquivo inacessível. Diagnósticos
 contêm código e caminho JSON sem eco de valores de entrada. Sucesso informa
-contagens, versões e hashes. Os testes usam espécies sintéticas em memória e
-arquivos temporários; não constituem corpus ou campanha de mutação.
+contagens, versões e hashes. Os testes usam espécies sintéticas em memória,
+arquivos temporários e o manifesto histórico preso ao hash para provar conjuntos; não constituem corpus ou campanha de mutação.

 Resultados individuais, comandos e hashes constam em `validation-report.json`.
 SHA256SUMS cobre os sete artefatos contratados, sem incluir a si mesmo, estado ou
 ledger. Conferência automática de formato não verifica a semântica botânica da URL.

 ## Fronteira de aceite

 A aprovação humana recebida autoriza o escopo e a execução; não contém o aceite
 dos bytes produzidos depois dela. A revisão final deve conferir 12/12 identidades,
 cada alias/fonte, nomes comuns, ordem, IDs e proteções, e registrar approved/rejected,
 papel, data e hashes de manifesto/roster. O executor não substitui esse parecer.
 P05 permanece incompleto até esse gate.

-As provas do overlay Codex são presas a um commit real. Como staging e commit foram
-expressamente proibidos, não é possível atestar estas alterações não commitadas
-por `review_guard.py proof`. Não há sidecar ou aprovação de convergência simulados.
-As validações aqui registradas são da working tree. O plano congelado, as specs,
-o snapshot de 23 arquivos e o digest histórico foram preservados. P01/P03-R6
-continuam blocked-terminal, P02/P04 completed e release pending.
+As provas do overlay Codex são presas a commits reais. A prova RED do baseline está
+registrada no guard para o commit local de aprovação
+`c7012b942c36fe93fb136a376a1a73093f1e5aaa`. A implementação permanece unstaged e sem
+commit por instrução humana; seus testes GREEN e hashes são evidência da árvore de
+trabalho. Não se declara convergência de um commit ainda inexistente. O sidecar T1
+aguarda submissão do delta após autorização de commit, sem replanejar a unidade.
+
+Os pacotes P05 e P05-R1, suas specs/deltas e manifestos históricos permanecem congelados.
+A regra está formalizada no delta SD-201 aplicável de P05-R1; current/specs só será
+sincronizada no encerramento regular previsto no plano. Nenhum release ou homologação
+é executado agora. P01/P03-R6 continuam blocked-terminal, P02/P04 completed, release pending.
+
+Digest P05-R1 aprovado:
+`6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f`.
diff --git a/docs/phase1/offline-class-manifest.v1.json b/docs/phase1/offline-class-manifest.v1.json
index 59eb517..53078e1 100644
--- a/docs/phase1/offline-class-manifest.v1.json
+++ b/docs/phase1/offline-class-manifest.v1.json
@@ -1,13 +1,13 @@
 {
   "schema_version": 1,
-  "manifest_version": "1.0.0",
+  "manifest_version": "1.1.0",
   "normalization_version": "1",
   "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
   "references": [
     {
       "ref_id": "kew_species_01",
       "authority": "kew_powo",
       "url": "https://powo.science.kew.org/taxon/87014-1",
       "consulted_on": "2026-09-11",
       "title": "Epipremnum aureum (Linden & André) G.S.Bunting"
     },
@@ -298,38 +298,26 @@
           "ref_ids": [
             "kew_species_06"
           ]
         },
         {
           "name": "Aloe littoralis",
           "ref_ids": [
             "kew_species_06"
           ]
         },
-        {
-          "name": "Aloe maculata",
-          "ref_ids": [
-            "kew_species_06"
-          ]
-        },
         {
           "name": "Aloe rubescens",
           "ref_ids": [
             "kew_species_06"
           ]
         },
-        {
-          "name": "Aloe variegata",
-          "ref_ids": [
-            "kew_species_06"
-          ]
-        },
         {
           "name": "Aloe vulgaris",
           "ref_ids": [
             "kew_species_06"
           ]
         }
       ],
       "taxonomy_ref_ids": [
         "kew_species_06"
       ],
@@ -604,32 +592,20 @@
     {
       "index": 8,
       "class_id": "species_09",
       "kind": "species",
       "scientific_name": "Ficus elastica",
       "display_name": "falsa-seringueira",
       "common_names": [
         "falsa-seringueira"
       ],
       "synonyms": [
-        {
-          "name": "Ficus clusiifolia",
-          "ref_ids": [
-            "kew_species_09"
-          ]
-        },
-        {
-          "name": "Ficus cordata",
-          "ref_ids": [
-            "kew_species_09"
-          ]
-        },
         {
           "name": "Ficus karet",
           "ref_ids": [
             "kew_species_09"
           ]
         },
         {
           "name": "Ficus skytinodermis",
           "ref_ids": [
             "kew_species_09"
diff --git a/scripts/phase1/test_offline_manifest.py b/scripts/phase1/test_offline_manifest.py
index ef8ce1a..fc6fb98 100644
--- a/scripts/phase1/test_offline_manifest.py
+++ b/scripts/phase1/test_offline_manifest.py
@@ -1,36 +1,37 @@
 """Documentary contract tests: synthetic taxa, stdlib, no product integration."""

 from copy import deepcopy
 import hashlib
 import json
 from pathlib import Path
+import re
 import subprocess
 import sys
 import tempfile
 import unittest

 import validate_offline_manifest as validator


 def encode(value):
     return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


 def fixture():
     names = [f"Test{letter} alba" for letter in "abcdefghijkl"]
     roster = {"schema_version": 1, "status": "approved", "approval_ref": "synthetic approval",
               "approved_on": "2020-01-01", "species": [
                   {"index": i, "approved_name": name, "source_ref": "synthetic fixture"}
                   for i, name in enumerate(names)]}
     raw = encode(roster)
-    manifest = {"schema_version": 1, "manifest_version": "1.0.0", "normalization_version": "1",
+    manifest = {"schema_version": 1, "manifest_version": "1.1.0", "normalization_version": "1",
                 "roster_sha256": hashlib.sha256(raw).hexdigest(), "references": [
                     {"ref_id": "synthetic_ref", "authority": "kew_powo",
                      "url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:87014-1",
                      "consulted_on": "2020-01-01", "title": "Synthetic structural reference"}],
                 "classes": []}
     for i, name in enumerate(names):
         manifest["classes"].append({
             "index": i, "class_id": f"species_{i + 1:02}", "kind": "species",
             "scientific_name": name, "display_name": "rótulo",
             "common_names": ["rótulo"], "synonyms": [],
@@ -279,12 +280,176 @@ class RosterAndTransportTests(unittest.TestCase):
         with self.assertRaises(validator.ContractError) as caught:
             validator.validate_manifest(manifest, b'{"schema_version":1,"schema_version":1}\n')
         self.assertEqual(caught.exception.code, "E_JSON_DUPLICATE_KEY")

     def test_normalization_invalid_inputs(self):
         for value in [None, 1, "", " \t\n", "a\u0000", "a\u200b", "a\ud800"]:
             with self.subTest(value=repr(value)), self.assertRaises(validator.ContractError):
                 validator.normalize_name(value)


+class ApprovedQuarantineTests(unittest.TestCase):
+    """Compare the real contract to an independently pinned, pre-quarantine baseline."""
+
+    ROOT = Path(__file__).resolve().parents[2]
+    MANIFEST = "docs/phase1/offline-class-manifest.v1.json"
+    ROSTER = "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
+    BASE = "77e93a221dad3115c301b10317b626c236a3ba84"
+    BASE_SHA256 = "39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5"
+    QUARANTINED = ("Aloe maculata", "Aloe variegata", "Ficus clusiifolia", "Ficus cordata")
+
+    @classmethod
+    def setUpClass(cls):
+        raw = subprocess.check_output(["git", "show", cls.BASE + ":" + cls.MANIFEST], cwd=cls.ROOT)
+        if hashlib.sha256(raw).hexdigest() != cls.BASE_SHA256:
+            raise AssertionError("Historical baseline hash mismatch")
+        cls.baseline = validator.strict_load(raw)
+        cls.manifest = validator.strict_load((cls.ROOT / cls.MANIFEST).read_bytes())
+        cls.roster_bytes = (cls.ROOT / cls.ROSTER).read_bytes()
+
+    @staticmethod
+    def aliases(manifest):
+        return {validator.normalize_name(alias["name"]): item["class_id"]
+                for item in manifest["classes"] for alias in item["synonyms"]}
+
+    def test_exact_alias_sets_and_counts(self):
+        before, after = self.aliases(self.baseline), self.aliases(self.manifest)
+        quarantined = {validator.normalize_name(name) for name in self.QUARANTINED}
+        self.assertEqual(len(before), 83)
+        self.assertTrue(quarantined <= before.keys())
+        self.assertEqual(before.keys() - after.keys(), quarantined)
+        self.assertEqual(after, {key: value for key, value in before.items() if key not in quarantined})
+        self.assertEqual(sum(len(c["synonyms"]) for c in self.manifest["classes"]), 79)
+        self.assertEqual(len(after), 79)
+        self.assertEqual(len(validator.scientific_map(self.manifest)), 91)
+
+    def test_only_approved_manifest_changes(self):
+        expected = deepcopy(self.baseline)
+        expected["manifest_version"] = "1.1.0"
+        for item in expected["classes"]:
+            item["synonyms"] = [a for a in item["synonyms"] if a["name"] not in self.QUARANTINED]
+        self.assertEqual(self.manifest, expected)
+        historical_roster = subprocess.check_output(
+            ["git", "show", self.BASE + ":" + self.ROSTER], cwd=self.ROOT)
+        self.assertEqual(self.roster_bytes, historical_roster)
+        self.assertEqual(hashlib.sha256(self.roster_bytes).hexdigest(), self.manifest["roster_sha256"])
+
+    def test_all_twelve_canonicals_resolve(self):
+        species = self.baseline["classes"][:12]
+        self.assertEqual(len(species), 12)
+        for item in species:
+            with self.subTest(name=item["scientific_name"]):
+                self.assertEqual(validator.resolve_scientific_name(self.manifest, item["scientific_name"]),
+                                 item["class_id"])
+
+    def test_all_seventy_nine_eligible_aliases_resolve(self):
+        expected = {key: value for key, value in self.aliases(self.baseline).items()
+                    if key not in {validator.normalize_name(n) for n in self.QUARANTINED}}
+        self.assertEqual(len(expected), 79)
+        for name, class_id in expected.items():
+            with self.subTest(name=name):
+                self.assertEqual(validator.resolve_scientific_name(self.manifest, name), class_id)
+
+    def test_normalized_quarantined_inputs_return_none(self):
+        for name in self.QUARANTINED:
+            for value in (name, name.upper(), "\t" + name.lower().replace(" ", "\u2003\n") + "\u00a0"):
+                with self.subTest(name=name, variant=value):
+                    self.assertIsNone(validator.resolve_scientific_name(self.manifest, value))
+                    self.assertNotIn(validator.normalize_name(value), validator.scientific_map(self.manifest))
+
+    def test_fixture_reintroduction_rejected_in_every_species(self):
+        for name in self.QUARANTINED:
+            for index in range(12):
+                with self.subTest(name=name, index=index):
+                    manifest, roster = fixture()
+                    manifest["classes"][index]["synonyms"].append({"name": name, "ref_ids": ["synthetic_ref"]})
+                    with self.assertRaises(validator.ContractError) as caught:
+                        validator.validate_manifest(manifest, roster)
+                    self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")
+
+    def test_scientific_map_rejects_normalized_reintroduction(self):
+        for name in self.QUARANTINED:
+            for value in (name, name.upper(), "\t" + name.replace(" ", "\u00a0\n") + " "):
+                for field in ("synonyms", "scientific_name"):
+                    with self.subTest(name=name, value=value, field=field):
+                        manifest, _ = fixture()
+                        if field == "synonyms":
+                            manifest["classes"][0][field].append({"name": value, "ref_ids": ["synthetic_ref"]})
+                        else:
+                            manifest["classes"][0][field] = value
+                        with self.assertRaises(validator.ContractError) as caught:
+                            validator.scientific_map(manifest)
+                        self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")
+
+    def test_canonical_reintroduction_is_rejected(self):
+        for name in self.QUARANTINED:
+            with self.subTest(name=name):
+                manifest, roster = fixture()
+                manifest["classes"][0]["scientific_name"] = name
+                with self.assertRaises(validator.ContractError) as caught:
+                    validator.validate_manifest(manifest, roster)
+                self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")
+
+    def test_authorship_is_not_removed(self):
+        for name in self.QUARANTINED + ("Epipremnum aureum", "Sansevieria trifasciata"):
+            with self.subTest(name=name):
+                value = name + " L."
+                self.assertTrue(validator.normalize_name(value).endswith(" l."))
+                self.assertIsNone(validator.resolve_scientific_name(self.manifest, value))
+
+    def test_no_normalized_collisions_and_protections_excluded(self):
+        keys = [validator.normalize_name(name) for item in self.manifest["classes"][:12]
+                for name in [item["scientific_name"]] + [a["name"] for a in item["synonyms"]]]
+        self.assertEqual(len(keys), len(set(keys)))
+        for item in self.manifest["classes"]:
+            for name in [item["class_id"], item["display_name"]] + item["common_names"]:
+                with self.subTest(name=name):
+                    self.assertIsNone(validator.resolve_scientific_name(self.manifest, name))
+        self.assertEqual(self.manifest["classes"][12:], self.baseline["classes"][12:])
+        self.assertEqual([c["index"] for c in self.manifest["classes"]], list(range(14)))
+
+    def test_real_validator_version_and_counts(self):
+        result = validator.validate_manifest(self.manifest, self.roster_bytes)
+        self.assertEqual(result["manifest_version"], "1.1.0")
+        self.assertEqual((result["aliases"], result["scientific_keys"]), (79, 91))
+        self.assertEqual((result["species"], result["protection"], result["classes"]), (12, 2, 14))
+
+    def test_preliminary_version_is_no_longer_accepted(self):
+        manifest, roster = fixture()
+        manifest["manifest_version"] = "1.0.0"
+        with self.assertRaises(validator.ContractError) as caught:
+            validator.validate_manifest(manifest, roster)
+        self.assertEqual(caught.exception.code, "E_VERSION")
+
+    def test_taxonomy_evidence_preserves_conflicts_and_eligible_aliases(self):
+        path = self.ROOT / "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md"
+        text = path.read_text(encoding="utf-8")
+        blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
+        self.assertEqual(len(blocks), 1)
+        records = validator.strict_load((blocks[0] + "\n").encode("utf-8"))["quarantined_aliases"]
+        self.assertEqual(len(records), 4)
+        self.assertEqual({r["name"] for r in records}, set(self.QUARANTINED))
+        authors = {"Aloe maculata": ("Forssk.", "All."), "Aloe variegata": ("Forssk.", "L."),
+                   "Ficus clusiifolia": ("Summerh.", "Schott"),
+                   "Ficus cordata": ("Kunth & C.D.Bouché", "Thunb.")}
+        for record in records:
+            with self.subTest(name=record["name"]):
+                self.assertEqual(record["status"], "quarantined")
+                self.assertEqual((record["related_authorship"], record["conflicting_authorship"]),
+                                 authors[record["name"]])
+                self.assertEqual(record["normalized_authorless_name"], validator.normalize_name(record["name"]))
+                self.assertTrue(record["conflicting_taxon"])
+                self.assertTrue(record["reason"])
+                self.assertTrue(record["nomenclatural_synonymy_retained"])
+                self.assertIsNone(record["scientific_resolution"])
+                self.assertEqual(record["consulted_on"], "2026-09-11")
+                self.assertEqual(len(record["source_urls"]), 2)
+                self.assertTrue(all(url.startswith("https://powo.science.kew.org/taxon/")
+                                    for url in record["source_urls"]))
+                self.assertEqual(record["related_class_id"], self.aliases(self.baseline)[record["normalized_authorless_name"]])
+        included = re.findall(r"^\| ([^|]+) \| [^|]+ \| [^|]+ \| incluído \|$", text, re.M)
+        self.assertEqual(len(included), 79)
+        self.assertEqual({validator.normalize_name(n) for n in included}, self.aliases(self.manifest).keys())
+
+
 if __name__ == "__main__":
     unittest.main()
diff --git a/scripts/phase1/validate_offline_manifest.py b/scripts/phase1/validate_offline_manifest.py
index e61f863..9f01014 100644
--- a/scripts/phase1/validate_offline_manifest.py
+++ b/scripts/phase1/validate_offline_manifest.py
@@ -15,20 +15,25 @@ from urllib.parse import unquote, urlsplit
 BINOMIAL = re.compile(r"[A-Z][a-z]+ [a-z]+(?:-[a-z]+)*", re.ASCII)
 REF_ID = re.compile(r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", re.ASCII)
 HEX = re.compile(r"[0-9a-f]{64}", re.ASCII)
 ROOT_KEYS = {"schema_version", "manifest_version", "normalization_version",
              "roster_sha256", "references", "classes"}
 CLASS_KEYS = {"index", "class_id", "kind", "scientific_name", "display_name",
               "common_names", "synonyms", "taxonomy_ref_ids", "definition"}
 ROSTER_KEYS = {"schema_version", "status", "approval_ref", "approved_on", "species"}
 PROTECTIONS = (("outra_planta", "Outra planta"),
                ("imagem_invalida", "Imagem inválida"))
+# U-201 / P05-R1: normalized authorless names with proven nomenclatural homonyms.
+# Authorship, conflicting taxa and dated sources remain in taxonomy-review.md.
+QUARANTINED_SCIENTIFIC_NAMES = frozenset({
+    "aloe maculata", "aloe variegata", "ficus clusiifolia", "ficus cordata",
+})


 class ContractError(ValueError):
     """Diagnostics deliberately contain no untrusted input values."""

     def __init__(self, code, path):
         self.code, self.path = code, path
         super().__init__(f"{code} {path}")


@@ -167,37 +172,39 @@ def validate_reference(ref, path):


 def scientific_map(manifest):
     """Build only the scientific namespace and reject ambiguous keys."""
     result = {}
     for i, item in enumerate(manifest["classes"]):
         if item["kind"] != "species":
             continue
         for name in [item["scientific_name"]] + [s["name"] for s in item["synonyms"]]:
             key = normalize_name(name)
+            require(key not in QUARANTINED_SCIENTIFIC_NAMES,
+                    "E_NAME_QUARANTINED", f"$.classes[{i}]")
             require(key not in result, "E_NAME_COLLISION", f"$.classes[{i}]")
             result[key] = item["class_id"]
     return result


 def resolve_scientific_name(manifest, name):
     """Resolve against a validated manifest; unknown text returns None."""
     return scientific_map(manifest).get(normalize_name(name))


 def validate_manifest(manifest, roster_bytes):
     roster = strict_load(roster_bytes, "$.roster")
     validate_roster(roster)
     obj(manifest, ROOT_KEYS, "$")
     require(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1,
             "E_SCHEMA", "$.schema_version")
-    require(manifest["manifest_version"] == "1.0.0", "E_VERSION", "$.manifest_version")
+    require(manifest["manifest_version"] == "1.1.0", "E_VERSION", "$.manifest_version")
     require(manifest["normalization_version"] == "1", "E_VERSION", "$.normalization_version")
     digest = hashlib.sha256(roster_bytes).hexdigest()
     require(type(manifest["roster_sha256"]) is str and HEX.fullmatch(manifest["roster_sha256"])
             and manifest["roster_sha256"] == digest, "E_ROSTER_HASH", "$.roster_sha256")
     refs = {}
     for i, ref in enumerate(array(manifest["references"], "$.references", True)):
         path = f"$.references[{i}]"
         validate_reference(ref, path)
         require(ref["ref_id"] not in refs, "E_REF_DUPLICATE", path)
         refs[ref["ref_id"]] = ref
@@ -245,21 +252,23 @@ def validate_manifest(manifest, roster_bytes):
             spath = f"{path}.synonyms[{j}]"
             obj(synonym, {"name", "ref_ids"}, spath)
             binomial(synonym["name"], spath + ".name")
             ref_list(synonym["ref_ids"], spath + ".ref_ids")
     names = scientific_map(manifest)
     for i, entry in enumerate(roster["species"]):
         require(names.get(normalize_name(entry["approved_name"])) == f"species_{i + 1:02}",
                 "E_ROSTER_MAPPING", f"$.roster.species[{i}].approved_name")
     require(used == set(refs), "E_REF_ORPHAN", "$.references")
     return {"valid": True, "species": 12, "protection": 2, "classes": 14,
-            "schema_version": 1, "manifest_version": "1.0.0", "normalization_version": "1",
+            "aliases": sum(len(item["synonyms"]) for item in classes),
+            "scientific_keys": len(names),
+            "schema_version": 1, "manifest_version": "1.1.0", "normalization_version": "1",
             "roster_sha256": digest}


 def main(argv=None):
     parser = argparse.ArgumentParser(description=__doc__)
     parser.add_argument("--manifest", required=True, type=Path)
     parser.add_argument("--roster", required=True, type=Path)
     args = parser.parse_args(argv)
     try:
         raw = args.manifest.read_bytes()
```

## Resultado da revisão Codex inline

Delta c7012b942c36fe93fb136a376a1a73093f1e5aaa → 42559189f4d3dcbdec192fecaac2c06e2a0fd31b revisado contra o brief e B1 congelado. A guarda normalizada rejeita os quatro nomes como alias/canônico; o manifesto os remove preservando os demais dados. A suíte cobre retorno None, reintrodução em todas as espécies, variantes normalizadas, mapeamento por classe, conjuntos, roster e evidência taxonômica. Nenhuma regressão bloqueante identificada no delta.

- B1-resolution: `proof-7a33abd871b9817a5dd122551336b9f5`.
- contract-tests: `proof-101608561adcb06229ef1f6b6c0d455f`.
- manifest-cli: `proof-afc8d8f8bc8ca1ec283f2428600826d6`.
- documentary-integrity: `proof-d4ba1fd44f964889d0a0575cd1aa1047`.

B1 reproduzido pelo mesmo argv/cwd do RED histórico e resolvido pela prova verde desse commit. Findings formais em commit-findings.json. Aceite humano dos oito hashes registrado em human-acceptance.json.
