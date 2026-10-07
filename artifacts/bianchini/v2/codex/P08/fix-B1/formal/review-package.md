# Review Package

- Base: `7981377a433270c9e2072fcafdf89b690988fa08`
- Head: `HEAD`
- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md` (a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36)
- Report: `/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/implementer-report.md` (dc97df858390ac469ff2b24d2406b71580f447dbccd29b6ba4cbbd54af2b8519)
- Security notice: sanitização heurística; 2 ocorrência(s) removida(s). Revise antes de compartilhar.

## Commits

```text
dd595a6 fix(p08): preserve transient iNaturalist failures on resume
```

## Stat

```text
...ected-history-and-selective-mutation.stderr.txt |    5 +
 ...ected-history-and-selective-mutation.stdout.txt |    5 +
 .../v2/codex/P08/closure/approved-bytes.stderr.txt |    0
 .../v2/codex/P08/closure/approved-bytes.stdout.txt |   31 +
 .../P08/closure/canonical-taxonomy.stderr.txt      |    0
 .../P08/closure/canonical-taxonomy.stdout.txt      |    1 +
 .../v2/codex/P08/closure/diff-check.stderr.txt     |    0
 .../v2/codex/P08/closure/diff-check.stdout.txt     |    0
 ...ernal-integrity-and-human-acceptance.stderr.txt |    0
 ...ernal-integrity-and-human-acceptance.stdout.txt |    1 +
 .../v2/codex/P08/closure/focal-adapter.stderr.txt  |    5 +
 .../v2/codex/P08/closure/focal-adapter.stdout.txt  |    0
 .../v2/codex/P08/closure/focal-recovery.stderr.txt |    5 +
 .../v2/codex/P08/closure/focal-recovery.stdout.txt |    0
 .../v2/codex/P08/closure/guard-status.json         |  316 ++
 .../P08/closure/historical-checksums.stderr.txt    |    0
 .../P08/closure/historical-checksums.stdout.txt    |    7 +
 .../P08/closure/implementation-inventory.json      |   42 +
 .../inaturalist-timeout-resumption.stderr.txt      |    5 +
 .../inaturalist-timeout-resumption.stdout.txt      |    1 +
 .../v2/codex/P08/closure/independent-review.json   |   19 +
 .../v2/codex/P08/closure/planning-audit.stderr.txt |    0
 .../v2/codex/P08/closure/planning-audit.stdout.txt |   74 +
 .../codex/P08/closure/planning-snapshot.stderr.txt |    0
 .../codex/P08/closure/planning-snapshot.stdout.txt |    5 +
 .../v2/codex/P08/closure/proof-results.json        |  340 ++
 .../v2/codex/P08/closure/recovery-checkpoint.json  |  103 +
 .../v2/codex/P08/closure/recovery-report.md        |   19 +
 .../v2/codex/P08/closure/repo-hygiene.stderr.txt   |    0
 .../v2/codex/P08/closure/repo-hygiene.stdout.txt   |    5 +
 .../v2/codex/P08/closure/review-package.md         | 3233 ++++++++++++++++++++
 .../v2/codex/P08/closure/state.stderr.txt          |    0
 .../v2/codex/P08/closure/state.stdout.txt          |    4 +
 .../v2/codex/P08/fix-B1/acceptance-digest.txt      |    1 +
 .../v2/codex/P08/fix-B1/acceptance-manifest.sha256 |   74 +
 .../v2/codex/P08/fix-B1/acceptance-package.md      |   40 +
 .../v2/codex/P08/fix-B1/affected-history.json      |   27 +
 .../codex/P08/fix-B1/affected-history.stderr.txt   |    5 +
 .../codex/P08/fix-B1/affected-history.stdout.txt   |    5 +
 .../v2/codex/P08/fix-B1/change-policy.json         |    9 +
 .../bianchini/v2/codex/P08/fix-B1/checkpoint.json  |  116 +
 .../v2/codex/P08/fix-B1/commit-inventory.json      |  393 +++
 .../v2/codex/P08/fix-B1/commit-inventory.txt       |   76 +
 .../codex/P08/fix-B1/evidence-reconciliation.json  |  105 +
 .../v2/codex/P08/fix-B1/external-preserved.json    |   11 +
 .../v2/codex/P08/fix-B1/focal-adapter.json         |   27 +
 .../v2/codex/P08/fix-B1/focal-adapter.stderr.txt   |    5 +
 .../v2/codex/P08/fix-B1/focal-adapter.stdout.txt   |    0
 .../v2/codex/P08/fix-B1/focal-recovery.json        |   27 +
 .../v2/codex/P08/fix-B1/focal-recovery.stderr.txt  |    5 +
 .../v2/codex/P08/fix-B1/focal-recovery.stdout.txt  |    0
 .../v2/codex/P08/fix-B1/guard-before.json          |  316 ++
 .../v2/codex/P08/fix-B1/guard-fix-started.json     |  331 ++
 .../v2/codex/P08/fix-B1/guard-resumed.json         |  331 ++
 .../v2/codex/P08/fix-B1/implementer-report.md      |   22 +
 .../P08/fix-B1/independent-review-assessment.json  |   24 +
 .../v2/codex/P08/fix-B1/independent-review.json    |    3 +
 .../v2/codex/P08/fix-B1/preexisting-inventory.json |   45 +
 .../P08/fix-B1/recovery-documentary-before.patch   |   69 +
 .../bianchini/v2/codex/P08/fix-B1/red-reused.json  |    7 +
 .../v2/codex/P08/fix-B1/regression-green.json      |   30 +
 .../codex/P08/fix-B1/regression-green.stderr.txt   |    8 +
 .../codex/P08/fix-B1/regression-green.stdout.txt   |    0
 .../v2/codex/P08/fix-B1/regression-red.json        |   30 +
 .../v2/codex/P08/fix-B1/regression-red.stderr.txt  |  162 +
 .../v2/codex/P08/fix-B1/regression-red.stdout.txt  |    0
 .../v2/codex/P08/fix-B1/resume-preflight.json      |  116 +
 .../v2/codex/P08/fix-B1/review-package.md          | 2539 +++++++++++++++
 .../v2/codex/P08/fix-B1/security-inspection.json   |  127 +
 .../codex/P08/fix-B1/session-start-inventory.json  |   71 +
 .../v2/codex/convergence/P08/.proofs/1.json        |  297 ++
 .../bianchini/v2/codex/convergence/P08/1.json      |  326 ++
 artifacts/bianchini/v2/ledgers/P08.md              |   23 +
 docs/living/PROJECT_STATE.md                       |   17 +-
 scripts/phase1/recover_p08.py                      |    3 +-
 scripts/phase1/test_recover_p08.py                 |  104 +
 76 files changed, 10146 insertions(+), 7 deletions(-)
```

## Diff

```diff
diff --git a/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt
new file mode 100644
index 0000000..430985d
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt
@@ -0,0 +1,5 @@
+.........................................................................................................................................................................................................................................
+----------------------------------------------------------------------
+Ran 233 tests in 8.825s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt
new file mode 100644
index 0000000..4f2a38f
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt
@@ -0,0 +1,5 @@
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "advance_cursor_before_commit"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 3, "mode": "mutant", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "allow_private_export"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "bypass_expert"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_license", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 8, "material_changes_reached": 8, "mock_calls": 9, "mode": "mutant", "network_calls": 0, "seam": "bypass_license", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "bypass_license"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 2, "mode": "mutant", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "ignore_hash_mismatch"}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt
new file mode 100644
index 0000000..036e32c
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt
@@ -0,0 +1,31 @@
+artifacts/bianchini/v2/codex/P08/audit-final.json: OK
+artifacts/bianchini/v2/codex/P08/checkpoint.json: OK
+artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json: OK
+artifacts/bianchini/v2/codex/P08/continuation-report.md: OK
+artifacts/bianchini/v2/codex/P08/focal-inat-final.txt: OK
+artifacts/bianchini/v2/codex/P08/focal-inat.txt: OK
+artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt: OK
+artifacts/bianchini/v2/codex/P08/full-suite-final.txt: OK
+artifacts/bianchini/v2/codex/P08/full-suite.txt: OK
+artifacts/bianchini/v2/codex/P08/implementer-report.md: OK
+artifacts/bianchini/v2/codex/P08/inat-red.txt: OK
+artifacts/bianchini/v2/codex/P08/manifest.txt: OK
+artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json: OK
+artifacts/bianchini/v2/codex/P08/mutation-evidence.json: OK
+artifacts/bianchini/v2/codex/P08/real-round.json: OK
+artifacts/bianchini/v2/codex/P08/recovery-red.txt: OK
+artifacts/bianchini/v2/codex/P08/resume-inventory.json: OK
+artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt: OK
+artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt: OK
+artifacts/bianchini/v2/codex/P08/roster-hashes.txt: OK
+artifacts/bianchini/v2/codex/P08/task-brief.md: OK
+artifacts/bianchini/v2/codex/P08/verification-final.json: OK
+artifacts/bianchini/v2/codex/P08/verification.json: OK
+artifacts/bianchini/v2/ledgers/P08.md: OK
+artifacts/phase1/p08/summary.json: OK
+docs/phase1/P08-recovery.md: OK
+scripts/phase1/inaturalist_source.py: OK
+scripts/phase1/recover_p08.py: OK
+scripts/phase1/test_inaturalist_source.py: OK
+scripts/phase1/test_p08_mutation.py: OK
+scripts/phase1/test_recover_p08.py: OK
diff --git a/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt
new file mode 100644
index 0000000..e507626
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt
@@ -0,0 +1 @@
+{"aliases": 79, "classes": 14, "manifest_sha256": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c", "manifest_version": "1.1.0", "normalization_version": "1", "protection": 2, "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b", "schema_version": 1, "scientific_keys": 91, "species": 12, "valid": true}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt
new file mode 100644
index 0000000..9dd82c2
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt
@@ -0,0 +1 @@
+{"acceptance": "technical_bytes_only", "approved_for_dataset": 0, "candidate_review": "pending", "candidates_pending": 1088, "external_files_each": 138, "historical_files": 29, "historical_images": 17, "inat": "no_crosswalk", "manifest_sha256": "334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716", "p07_receipt_hashes": 7, "p09_started": false, "read_only_replay_bytes_and_mtimes_unchanged": true, "release": "pending", "result": "passed", "training_authorized": false, "transferred": 0, "usable": 0}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt
new file mode 100644
index 0000000..91f86cb
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt
@@ -0,0 +1,5 @@
+...............
+----------------------------------------------------------------------
+Ran 15 tests in 0.008s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt
new file mode 100644
index 0000000..0173a67
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt
@@ -0,0 +1,5 @@
+...................................................
+----------------------------------------------------------------------
+Ran 51 tests in 2.331s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/guard-status.json b/artifacts/bianchini/v2/codex/P08/closure/guard-status.json
new file mode 100644
index 0000000..bbf6dec
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/guard-status.json
@@ -0,0 +1,316 @@
+{
+  "migrated": false,
+  "next_action": "fix_required",
+  "phase": "review_frozen",
+  "recovered": false,
+  "state": {
+    "blockers": {
+      "B1": {
+        "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+        "disposition": "blocker",
+        "id": "B1",
+        "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+        "review_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "risk_seam": "p08-source-contract",
+        "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+        "severity": "important",
+        "source": "initial",
+        "status": "open",
+        "structural": false,
+        "structural_class": null,
+        "structural_evidence": null,
+        "title": "Timeout de iNaturalist impede a retomada contratada"
+      }
+    },
+    "created_at": "2026-10-07T22:50:20.012004Z",
+    "decisions": [
+      {
+        "at": "2026-10-07T22:50:39.350539Z",
+        "kind": "local_block",
+        "result": "independent_work_continues",
+        "summary": "User explicitly requires ending closure on gate failure without code/test changes, a second commit or push. B1 remains open; no fix round or terminal transition requested. Only P08 closure is authorized."
+      }
+    ],
+    "deferred_hardening": [],
+    "delta_submissions": 0,
+    "events": [
+      {
+        "action": "review_frozen",
+        "at": "2026-10-07T22:50:20.012073Z",
+        "blockers": [
+          "B1"
+        ],
+        "hardening": 0
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.328167Z",
+        "gate": "synthetic-source-contract",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "status": "failed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.716608Z",
+        "gate": "focal-recovery",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.196782Z",
+        "gate": "focal-adapter",
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.767313Z",
+        "gate": "canonical-taxonomy",
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:22.422632Z",
+        "gate": "append-only-integrity-idempotence",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:23.182013Z",
+        "gate": "selective-mutation",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:24.137196Z",
+        "gate": "affected-history",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:25.130279Z",
+        "gate": "p07-17-preserved",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:26.221197Z",
+        "gate": "external-data-integrity",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:27.416911Z",
+        "gate": "final-human-bytes-acceptance",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:28.713376Z",
+        "gate": "approved-bytes",
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:30.017383Z",
+        "gate": "historical-checksums",
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:31.398464Z",
+        "gate": "state",
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:32.841139Z",
+        "gate": "planning-snapshot",
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:34.391837Z",
+        "gate": "planning-audit",
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:35.994322Z",
+        "gate": "repo-hygiene",
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:37.662898Z",
+        "gate": "diff-check",
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "status": "passed"
+      },
+      {
+        "action": "decision",
+        "at": "2026-10-07T22:50:39.350613Z",
+        "kind": "local_block",
+        "result": "independent_work_continues"
+      }
+    ],
+    "fix_rounds": 0,
+    "gates": {
+      "affected-history": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:24.137120Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "append-only-integrity-idempotence": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:22.422590Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "approved-bytes": {
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "recorded_at": "2026-10-07T22:50:28.713298Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "canonical-taxonomy": {
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "recorded_at": "2026-10-07T22:50:21.767168Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "diff-check": {
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "recorded_at": "2026-10-07T22:50:37.662852Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "external-data-integrity": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:26.221150Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "final-human-bytes-acceptance": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:27.416857Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-adapter": {
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "recorded_at": "2026-10-07T22:50:21.196738Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-recovery": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:20.716570Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "historical-checksums": {
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "recorded_at": "2026-10-07T22:50:30.017327Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "p07-17-preserved": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:25.130229Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-audit": {
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "recorded_at": "2026-10-07T22:50:34.391804Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-snapshot": {
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "recorded_at": "2026-10-07T22:50:32.841102Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "repo-hygiene": {
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "recorded_at": "2026-10-07T22:50:35.994266Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "selective-mutation": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:23.181982Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "state": {
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "recorded_at": "2026-10-07T22:50:31.398405Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "synthetic-source-contract": {
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "recorded_at": "2026-10-07T22:50:20.328100Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "failed"
+      }
+    },
+    "last_review_head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "pending_delta": null,
+    "phase": "review_frozen",
+    "plan_id": "P08",
+    "planning_version": "v2",
+    "redesign_count": 0,
+    "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+    "required_gates": [
+      "synthetic-source-contract",
+      "focal-recovery",
+      "focal-adapter",
+      "canonical-taxonomy",
+      "append-only-integrity-idempotence",
+      "selective-mutation",
+      "affected-history",
+      "p07-17-preserved",
+      "external-data-integrity",
+      "final-human-bytes-acceptance",
+      "approved-bytes",
+      "historical-checksums",
+      "state",
+      "planning-snapshot",
+      "planning-audit",
+      "repo-hygiene",
+      "diff-check",
+      "human-botanical-privacy-review",
+      "git-secrets-private-data-images-inspection"
+    ],
+    "schema_version": 2,
+    "seam": "p08-source-contract",
+    "task_brief": "artifacts/bianchini/v2/codex/P08/task-brief.md",
+    "task_brief_digest": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "unit_digest": "33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af",
+    "unit_id": "1",
+    "unit_identity": "2638b0c17436a9e732e54818b20e092e594ffa983a29df86b7c6b355a593404a",
+    "unit_identity_source": "task_brief",
+    "updated_at": "2026-10-07T22:50:39.350618Z"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt
new file mode 100644
index 0000000..dd68c00
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt
@@ -0,0 +1,7 @@
+artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json: OK
+artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md: OK
+artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json: OK
+docs/phase1/F1-MAN01-offline-class-manifest.md: OK
+docs/phase1/offline-class-manifest.v1.json: OK
+scripts/phase1/test_offline_manifest.py: OK
+scripts/phase1/validate_offline_manifest.py: OK
diff --git a/artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json b/artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json
new file mode 100644
index 0000000..142839b
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json
@@ -0,0 +1,42 @@
+{
+  "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "parent": "24de252d27a137281c02cad50533280bb82dd80d",
+  "message": "feat(p08): add bounded traceable dataset recovery",
+  "file_count": 33,
+  "files_sha256": {
+    "artifacts/bianchini/v2/codex/P08/audit-final.json": "4431ab3f00cdeec62fecbb2058f18dcfb63c4d33b223bd5f972726493cb97c80",
+    "artifacts/bianchini/v2/codex/P08/checkpoint.json": "9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230",
+    "artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json": "edce9f48d1a230bfb2aa98072b99f2d8ef28ec30bcc92c87206667a7cae80296",
+    "artifacts/bianchini/v2/codex/P08/continuation-report.md": "fc42eb7ba4a348d0edb206dcf69867ef1bbea45b73a6a4b4a44443b303f5635d",
+    "artifacts/bianchini/v2/codex/P08/final-files.sha256": "5c5c61406db304c42671a727a2016b566b2e5d5fca2c487466f3adebb09055b2",
+    "artifacts/bianchini/v2/codex/P08/focal-inat-final.txt": "2fdf7a432a53fceb691486981be60fcb65192fbaa6b7627e6b3fe3a0c95917bf",
+    "artifacts/bianchini/v2/codex/P08/focal-inat.txt": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+    "artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt": "2685ccaab15660c44c951beb8fe9c19d6d9e9e347b91699628320b87c86b058f",
+    "artifacts/bianchini/v2/codex/P08/full-suite-final.txt": "ed24024f0c3d1b17f96cc32552dd6391462ca11089c74f599305c51d7ec0a660",
+    "artifacts/bianchini/v2/codex/P08/full-suite.txt": "3d6689642da34d73791790f53db3d6b989e16eabbd850972ccfaa176e92b2db0",
+    "artifacts/bianchini/v2/codex/P08/human-acceptance.json": "3650e20c20ceb6ec2b76d55636202a86159ed7fc6ba108239f43edad12ea0d3d",
+    "artifacts/bianchini/v2/codex/P08/implementer-report.md": "b3cb7bb752829b2c95971653c14d460b7e26f2ef095b895f2b33921fe94c1a5b",
+    "artifacts/bianchini/v2/codex/P08/inat-red.txt": "5588c065e674a94b4cfc0f14748eac93d6f2fb0101e5f32a5e992420840eb645",
+    "artifacts/bianchini/v2/codex/P08/manifest.txt": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+    "artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json": "23527bd62c51bdc91b6bf9193ed60bf68a267c0dbd432ac4be88a05fc6f1c315",
+    "artifacts/bianchini/v2/codex/P08/mutation-evidence.json": "55ef68eefb2e85931f2c4a303d161b326bccea87468311ec22db47ee62996ba5",
+    "artifacts/bianchini/v2/codex/P08/real-round.json": "d090bc5706aeff5ae351260208365c2e37a83eec2570b8085a5dbbfd9e78b0af",
+    "artifacts/bianchini/v2/codex/P08/recovery-red.txt": "9d56b591390394d0f50ce1532442a2bc571c26c93329b08a92e518521092fc34",
+    "artifacts/bianchini/v2/codex/P08/resume-inventory.json": "61c61bfa952bc0d2958c9eb1dc4fb053bf30700e9cd67da051679cb9b4f6a19f",
+    "artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+    "artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt": "e885f40ddecec4eef4b0585e1f71e621c9f3188e3aaf84bda2ec2856e74763a2",
+    "artifacts/bianchini/v2/codex/P08/roster-hashes.txt": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+    "artifacts/bianchini/v2/codex/P08/task-brief.md": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "artifacts/bianchini/v2/codex/P08/verification-final.json": "8893c65c032fbb63e54671ad422e661421c5d1ee354ecf2716cb103f1e5ccd3b",
+    "artifacts/bianchini/v2/codex/P08/verification.json": "7de6424ec7e3e7d6cbec51fa4402a5c3d1d5780a8431808891d81be913635296",
+    "artifacts/bianchini/v2/ledgers/P08.md": "d64f79f7adb25303cb636a9a5dac32d21456e6b7f0f381559c9b9f441335ee35",
+    "artifacts/phase1/p08/summary.json": "d1130531abea27c2d6bb157fda7be376b3cefec514b49fb5374c82fcd8cb2c4f",
+    "docs/phase1/P08-recovery.md": "10c454fcc82cf17a8051f37e8ca81defcd3a78ae6f180c8008e4bfb89b0d218b",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/recover_p08.py": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
+    "scripts/phase1/test_recover_p08.py": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
+  },
+  "closure_commit": null
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt
new file mode 100644
index 0000000..cda656f
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt
@@ -0,0 +1,5 @@
+Traceback (most recent call last):
+  File "<string>", line 33, in <module>
+    assert failure['code'] in r.RETRYABLE, 'approved timeout recovery contract violated: timeout became non-retryable '+failure['code']
+           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: approved timeout recovery contract violated: timeout became non-retryable inaturalist_contract_or_evidence
diff --git a/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt
new file mode 100644
index 0000000..a2b9007
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt
@@ -0,0 +1 @@
+{"scenario": "synthetic_inaturalist_timeout", "fake_transport_calls": 1, "actual_failure_code": "inaturalist_contract_or_evidence", "retryable": false, "expected": "preserve retryable timeout for restart", "real_network_calls": 0}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/independent-review.json b/artifacts/bianchini/v2/codex/P08/closure/independent-review.json
new file mode 100644
index 0000000..6e5aad2
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/independent-review.json
@@ -0,0 +1,19 @@
+{
+  "findings": [
+    {
+      "id": "B1",
+      "severity": "important",
+      "disposition": "blocker",
+      "title": "Timeout de iNaturalist impede a retomada contratada",
+      "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+      "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+      "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+      "risk_seam": "p08-source-contract",
+      "structural": false,
+      "structural_class": null,
+      "structural_evidence": null
+    }
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt
new file mode 100644
index 0000000..ecef80e
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt
@@ -0,0 +1,74 @@
+{
+  "budget_exceeded": [],
+  "limits": {
+    "execution_units": 40,
+    "max_execution_unit_words": 8000,
+    "max_plan_words": 16000,
+    "plans": 16,
+    "platforms": 6,
+    "shared_context_words": 24000
+  },
+  "metrics": {
+    "execution_units": 9,
+    "max_execution_unit_words": 859,
+    "max_plan_words": 926,
+    "package_words": 58443,
+    "plans": 8,
+    "platforms": 2,
+    "shared_context_words": 3052
+  },
+  "profile": "standard",
+  "quality_contract": "planning-quality-v2",
+  "readiness": {
+    "counts": {
+      "assumptions": 11,
+      "decisions": 24,
+      "design_surfaces": 0,
+      "pitfalls": 20,
+      "spec_deltas": 6,
+      "spikes": 5,
+      "user_actions": 11
+    },
+    "coverage_gaps": [],
+    "design": null,
+    "design_required": false,
+    "scope_digest": "1ad0136669f82fcf9307b7dce287f544ed256c1205a70e2a717a041867167197",
+    "spec_deltas": [
+      {
+        "id": "SD-001",
+        "source": "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
+        "target": "docs/bianchini/current/specs/replan-v2.md"
+      },
+      {
+        "id": "SD-006",
+        "source": "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
+        "target": "docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md"
+      },
+      {
+        "id": "SD-101",
+        "source": "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
+        "target": "docs/bianchini/current/specs/provider-benchmark-decision.md"
+      },
+      {
+        "id": "SD-201",
+        "source": "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
+        "target": "docs/bianchini/current/specs/offline-class-manifest.md"
+      },
+      {
+        "id": "SD-701",
+        "source": "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md",
+        "target": "docs/bianchini/current/specs/traceable-dataset-curation.md"
+      },
+      {
+        "id": "SD-801",
+        "source": "docs/bianchini/changes/v2/spec-deltas/dataset-recovery.md",
+        "target": "docs/bianchini/current/specs/dataset-recovery.md"
+      }
+    ],
+    "status": "ready"
+  },
+  "recommended_profile": "standard",
+  "research_mode": "targeted_web",
+  "valid": true,
+  "warnings": []
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt
new file mode 100644
index 0000000..195d869
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt
@@ -0,0 +1,5 @@
+{
+  "algorithm": "sha256-manifest-v1",
+  "digest": "6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a",
+  "manifest": "/tmp/bianchini-codex-proof-2r_19xdq/checkout/artifacts/bianchini/v2/approval/manifest-p08.sha256"
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/proof-results.json b/artifacts/bianchini/v2/codex/P08/closure/proof-results.json
new file mode 100644
index 0000000..055b614
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/proof-results.json
@@ -0,0 +1,340 @@
+{
+  "focal-recovery": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_recover_p08.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:34.435704Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "signature": "ccbf3d7d9831f95fb105f1b8b9d4382a5bab457ad919cb8f98b434918233451c",
+      "spawn_error": false,
+      "stderr_sha256": "029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "focal-adapter": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_inaturalist_source.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:34.841212Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+      "signature": "b42a84d6e2cd5c0041db9b996e01533a295aced6438aca3cd2f2452ab555cc68",
+      "spawn_error": false,
+      "stderr_sha256": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "affected-history-and-selective-mutation": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.263570Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "signature": "280df38f125407d5858b1d9c968a6a18de26fe3b3fddf687a4ca4dbd66b4dec7",
+      "spawn_error": false,
+      "stderr_sha256": "4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2",
+      "stdout_sha256": "7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "canonical-taxonomy": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', 'scripts/phase1/validate_offline_manifest.py', '--manifest', 'docs/phase1/offline-class-manifest.v1.json', '--roster', 'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.600584Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+      "signature": "c0be870c5d94d8a7264d5e42e1f140cdd4b1cba9ca136d8a5110f3ff1125aa46",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "historical-checksums": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.900475Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+      "signature": "c4539628b78879335d57d375116a9bf931c3571610dbe4106adfcb1d69cd76a5",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "approved-bytes": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/codex/P08/final-files.sha256'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:45.189731Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+      "signature": "83789522da0c5613b99e18365492df068d5982d32567e2a44073a318974b0a0c",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "state": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'validate-state', 'docs/living/PROJECT_STATE.md'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:45.619629Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+      "signature": "fc41aa66e57b3d2d64474b889c055d7581a9c625026ac460cc5708396f54304a",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "planning-snapshot": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'snapshot', 'verify', 'docs/living/PROJECT_STATE.md', '--root', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:46.107195Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+      "signature": "b3104b168241884cf6566475d3efd78d7b5167aac29f5cbfc44cfa40b08de48a",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "planning-audit": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'planning-audit', 'docs/living/PROJECT_STATE.md', '--root', '.', '--strict'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:46.591855Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+      "signature": "17e577bbc1b14304f173dc8f552214961c75fd6785919903f0bd57c0cfe89a67",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "repo-hygiene": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'repo-hygiene', 'check', '--repo', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:47.034159Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+      "signature": "46e89f991049e8ec6e4f9900816ae614bf9885e5f07b1aa064ae09f42af557d7",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "diff-check": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['git', 'diff', '--check', '7981377a433270c9e2072fcafdf89b690988fa08^', '7981377a433270c9e2072fcafdf89b690988fa08'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:47.350328Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+      "signature": "394655e43777b80248adc3067337221413d6378cccccc69d7fd7c6923b57efaa",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "external-integrity-and-human-acceptance": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport sys,json,hashlib,stat,fcntl,subprocess,re\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nroot=Path.cwd();base=Path('/home/administradorarthur/datasets/scanplant');data=base/'p08-recovery-20261005';backup=base/'p08-recovery-20261005-backup';source=base/'p06-recovery-20260928'\\nreceipt=json.loads((root/'artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_bytes())\\nassert receipt['decision']=='accepted' and receipt['authority']=='human' and receipt['scope']=='technical_and_documentary_bytes_only'\\nassert receipt['approved_git_delivery_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/final-files.sha256')\\nassert receipt['approved_checkpoint_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json')\\nassert receipt['baseline']==subprocess.check_output(['git','rev-parse','HEAD^'],text=True).strip()\\nassert receipt['counts']==dict(candidates_pending=1088,transferred=0,p08_images=0,approved_for_dataset=0,usable=0)\\nassert receipt['zero_transfer_result_accepted'] is True and receipt['U-803']=='candidate_opinions_pending'\\nfor k in ['candidate_approval','download_authorized','authorship_confirmation','rights_approval','botanical_confirmation','privacy_approval','duplicate_decisions_conclusive','training_authorized','partition_authorized','p09_started']:assert receipt[k] is False,k\\nassert receipt['release']=='pending'\\nbefore={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nmanifest=json.loads((data/'final-manifest.json').read_bytes())\\nfor folder in [data,backup]:\\n assert h(folder/'final-manifest.json')==receipt['approved_external_manifest_sha256']=='334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716'\\n actual={str(p.relative_to(folder)):h(p) for p in folder.rglob('*') if p.is_file() and p.name not in ['.lock','final-manifest.json']}\\n assert actual==manifest['files'] and len(actual)==137\\n assert stat.S_IMODE(folder.stat().st_mode)==0o700\\n for p in folder.rglob('*'):\\n  assert not p.is_symlink()\\n  assert stat.S_IMODE(p.stat().st_mode)==(0o700 if p.is_dir() else 0o600)\\n  assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif'}\\nassert (data/'.lock').read_bytes()==b''\\nconfig=r.load(r.read(data/'config.json'));assert r.sha(r.encode(config))==manifest['config_sha256']\\nassert manifest['runtime_code_sha256']==r.fingerprint()\\nassert manifest['code_sha256']==config['code_sha256']\\nassert config['code_sha256']['recover_p08.py']==r.HTML_ORDER_PREDECESSOR\\nwith (data/'.lock').open('rb') as lock,patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')),patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')):\\n fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)\\n ds=r.Dataset(data,config);ds.replay();ds.verify_objects()\\n assert ds.events[0]['data']==config\\n assert {'from':config['code_sha256'],'to':r.fingerprint(),'reason':'deterministic_review_html_key_order'} in ds.select('code_compatibility')\\n assert r.verify(ds,source)==0\\n hashes,images=r.historical(source);assert len(hashes)==29 and len(images)==17\\n records=ds.records();summary=ds.summary()\\n assert len(records)==1088 and summary==r.load(r.read(data/'summary.json'))==r.load(r.read(root/'artifacts/phase1/p08/summary.json'))\\n assert summary['usable']==0 and summary['training_authorized'] is False and summary['partition_authorized'] is False\\n assert all(x['state']!='approved_for_dataset' and not x.get('original_sha256') and not x.get('sanitized_sha256') for x in records)\\n assert len(ds.select('page'))==len(ds.select('cursor'))==120 and not ds.select('committed') and not ds.select('received') and not ds.select('source_failure')\\n assert all(x['status']=='no_crosswalk' for x in summary['coverage'] if x['source']=='inaturalist' and x['class_id'].startswith('species_'))\\n assert len(summary['coverage'])==28 and all(x['transferred']==x['approved']==0 for x in summary['coverage'])\\n review=r.load(r.read(data/'human-review.json'));objects=r.load(r.read(data/'object-hashes.json'));decisions=r.load(r.read(data/'decisions.template.json'))\\n assert len(review['candidates'])==len(objects)==len(decisions['decisions'])==1088\\n assert {x['candidate_id'] for x in review['candidates']}=={x['candidate_id'] for x in records}=={x['candidate_id'] for x in decisions['decisions']}\\n assert all(x['reviewer'] is None and x['expert_confirmation'] is False for x in decisions['decisions'])\\n assert r.read(data/'Attributions.jsonl')==b''\\n assert len(ds.select('request'))==120\\n for n in ['historical-before.json','historical-before-after.json']:\\n  historical=r.load(r.read(data/n));assert len(historical)==17\\n # Replay and verification are read-only: no acquisition/inspection/finalization invocation.\\n ds2=r.Dataset(data,config);ds2.replay();assert ds2.events==ds.events and ds2.summary()==summary\\nassert before=={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nprint(json.dumps({'result':'passed','external_files_each':138,'manifest_sha256':receipt['approved_external_manifest_sha256'],'historical_files':29,'historical_images':17,'p07_receipt_hashes':7,'candidates_pending':1088,'transferred':0,'approved_for_dataset':0,'usable':0,'read_only_replay_bytes_and_mtimes_unchanged':True,'acceptance':'technical_bytes_only','candidate_review':'pending','inat':'no_crosswalk','training_authorized':False,'release':'pending','p09_started':False},sort_keys=True))\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:37:03.153530Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "signature": "4ae6d337898ce8a32f222812c01f26946f924718e986f00b0270d995a0c4d1d3",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  },
+  "inaturalist-timeout-resumption": {
+    "proof": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"import sys,tempfile,json\\nfrom pathlib import Path\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nimport test_inaturalist_source as fixture\\n\\nclass TimeoutTransport:\\n    def __init__(self): self.calls=0\\n    def get(self,*args,**kwargs):\\n        self.calls+=1\\n        raise r.RecoveryError('timeout')\\n\\nwith tempfile.TemporaryDirectory(prefix='p08-synthetic-resume-') as tmp:\\n    dataset=Path(tmp)/'synthetic'\\n    config=r.default_config(offline=True)\\n    cls=r.canonical()[0]\\n    crosswalk=fixture.crosswalk()\\n    evidence=b'synthetic reviewed crosswalk evidence\\\\n'\\n    crosswalk['taxonomy_ref_ids']=cls['taxonomy_ref_ids']\\n    crosswalk['evidence'].update(path='evidence/crosswalk.json',sha256=r.sha(evidence))\\n    config['crosswalk'][cls['class_id']]=crosswalk\\n    transport=TimeoutTransport()\\n    with patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')),patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')):\\n        with r.Dataset(dataset,config,offline=True) as ds:\\n            r.persist(ds.path('evidence/crosswalk.json'),evidence,immutable=True)\\n            # Real conditional acquisition boundary; only the transport is fake.\\n            status=r.acquire_inat(ds,cls,transport,None)\\n            failure=ds.select('source_failure')[-1]\\n            assert transport.calls==1, 'crosswalk did not reach fake transport'\\n            assert status=='source_blocked'\\n            print(json.dumps({'scenario':'synthetic_inaturalist_timeout','fake_transport_calls':transport.calls,'actual_failure_code':failure['code'],'retryable':failure['code'] in r.RETRYABLE,'expected':'preserve retryable timeout for restart','real_network_calls':0}),flush=True)\\n            assert failure['code'] in r.RETRYABLE, 'approved timeout recovery contract violated: timeout became non-retryable '+failure['code']\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:47:42.806328Z",
+      "cwd": ".",
+      "exit_code": 1,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "signature": "a874b5d9a9ba6c5a874bf486f0cfb1de9e57d9f965c46158bc70932de7122f92",
+      "spawn_error": false,
+      "stderr_sha256": "ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d",
+      "stdout_sha256": "ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof_id": "proof-6928ea925e6f438e3873543389326106",
+    "proof_store": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json b/artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json
new file mode 100644
index 0000000..8f0f6e4
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json
@@ -0,0 +1,103 @@
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
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P07.md"
+    },
+    {
+      "id": "P08",
+      "status": "blocked",
+      "ledger": "artifacts/bianchini/v2/ledgers/P08.md"
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
+  "next_action": "P08 closure blocked by synthetic iNaturalist timeout resumption proof-6928ea925e6f438e3873543389326106. Await separate instruction for any code/test change. No second commit or push. 1088 candidates pending; zero transfers, approved_for_dataset=0, usable=0; real iNaturalist no_crosswalk. Training unauthorized; release pending; P09 not started.",
+  "workspace": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+  "git": {
+    "branch": "bm/v2-p08",
+    "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "dirty": true
+  },
+  "ledger_tail": [
+    "# P08 execution ledger",
+    "",
+    "- Approved package: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`.",
+    "- Base revision: `24de252d27a137281c02cad50533280bb82dd80d`; P07 base `b6844f9129d9edf862ae7958d8f043d9bdd5bd84`.",
+    "- Workspace: `/tmp/scanplant-p08-execution`; branch `bm/v2-p08`.",
+    "- Method installation: active .agents, version 3.2.0, v2-standalone.",
+    "- Profile standard; technical mode strict/per_task, data-transform, one unit `1`; authorized grouped operational round.",
+    "- Explicit current user authorization supersedes historical planning-only scope, grants implementation and bounded collection, prohibits staging/commit/push/release.",
+    "- Preflight: root/branch/HEAD/upstream/remote, clean index/tree, only three known starting worktrees, snapshot and manifest, strict planning audit and hygiene passed. P07/guard completed, usable=0; P08 approved/unstarted, release pending, P09 absent. Python 3.14.4/Pillow 12.3.0 available.",
+    "- P06: 29 files, SHA256SUMS passed; 17/17 image hashes match P07 closure. All seven final external P07 hashes match. No historical mutation.",
+    "- `bm change-policy --file-location`: bounded_amendment; evidence artifacts and temporary execution workspace location recorded, approved plan immutable.",
+    "- RED: recovery-red.txt and inat-red.txt record missing-module failures before implementation. GREEN initial focal runs passed.",
+    "- Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.",
+    "- Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.",
+    "- Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint.",
+    "",
+    "- Continuation recovered the exact checkpoint digest and eleven untracked files; existing workspace reused, baseline HEAD unchanged, no upstream.",
+    "- Final continuation evidence: artifacts/bianchini/v2/codex/P08/continuation-report.md and verification-final.json. 51 recovery + 15 adapter focal tests; 233 full historical/affected tests; five selective mutations killed, zero survivors.",
+    "- Real Commons round: 120 successful metadata requests, 1090 class associations/1088 unique candidates, all pending, no media transfer. iNaturalist no_crosswalk, zero requests. P07 17/17 bytes and mtimes preserved.",
+    "- Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.",
+    "- External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.",
+    "- Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending.",
+    "",
+    "## Closure recovery — 2026-10-07",
+    "",
+    "- Same branch recovered through Git prune (only obsolete registration) and Method workspace create/resume into persistent `.worktrees/ScanPlant/p08`; HEAD `7981377a433270c9e2072fcafdf89b690988fa08`, parent `24de252d27a137281c02cad50533280bb82dd80d`; one own commit.",
+    "- No prior P08 sidecar/proof store recovered from surviving official worktrees/Git; common proof signing key exists, contents not exposed. Uncommitted evidence formerly in lost checkout is unavailable; committed historical logs are preserved but are not current guard proofs.",
+    "- All approved implementation bytes/receipt and both external manifests verified. Historical checkpoint digests remain immutable; new recovery records are separate.",
+    "- 51 recovery, 15 adapter, 233 affected/history tests passed; five selective mutants killed. External 138-file datasets, 29 historical source files, 17 images and seven P07 receipts match; read-only replay preserves bytes/mtimes.",
+    "- Independent review reproduced B1 using `proof-6928ea925e6f438e3873543389326106`: transient iNaturalist timeout loses retry classification. Guard sidecar: `artifacts/bianchini/v2/codex/convergence/P08/1.json`; see closure/guard-status.json and independent-review.json.",
+    "- Owner mandates halt on failure: no fixes, no second commit, no staging/push. Remaining final Git private-data inspection and candidate human review are not claimed passed. Evidence/state changes remain uncommitted for inspection.",
+    "- 1088 candidates pending; zero transfer/approved/usable. Real iNaturalist no_crosswalk; rights/botanical/privacy authority remains pending. Training unauthorized, release pending, P09 not started."
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/recovery-report.md b/artifacts/bianchini/v2/codex/P08/closure/recovery-report.md
new file mode 100644
index 0000000..b13d881
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/recovery-report.md
@@ -0,0 +1,19 @@
+# P08 closure recovery — blocked
+
+Method 3.2.0 from ~/.agents/skills. Existing implementation preserved; no implementation, collection, downloads, staging, new commit or push in this recovery.
+
+The missing /tmp checkout was recovered on the same branch at the persistent worktree returned by workspace resume. Git prune dry-run identified exactly one obsolete administrative record, which alone was removed. All three surviving worktrees were clean. Local branch has one implementation commit above its expected parent. Remote branch was absent on both read-only checks.
+
+No earlier P08 sidecar or proof store was recoverable in the official surviving worktree/Git locations; their existence in the lost checkout cannot be established. Committed historical RED/GREEN/mutation logs, both checkpoints, task brief and human acceptance survive. They are historical evidence, not reused as signed current-commit proofs. The common guard signing key survives; no key material was exposed.
+
+Approved final-files manifest digest 5c5c61406db304c42671a727a2016b566b2e5d5fca2c487466f3adebb09055b2 and accepted continuation-checkpoint digest edce9f48d1a230bfb2aa98072b99f2d8ef28ec30bcc92c87206667a7cae80296 matched. Historical resume-inventory fingerprints predate subsequent implementation changes and do not replace final-files. External original config code fingerprint is the documented HTML-order predecessor; runtime_code_sha256 matches the implementation, with journaled code_compatibility. Existing human acceptance was neither rewritten nor regenerated.
+
+All 33 implementation paths are inventoried in implementation-inventory.json. Only a documentary append to its ledger and P08 state updates were made during this halted closure; code, tests, receipt and original checkpoint files remain byte-identical. final-files continues to describe the implementation commit; its historical ledger digest does not describe the later appended recovery entry.
+
+Fresh guard proofs: focal recovery 51 passed; adapter 15 passed; affected/historical suite 233 passed, including five killed selective mutations. Canonical manifest, historical checksums, approved bytes, state, snapshot, strict planning audit, hygiene and diff-check passed. External manifest digest 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716 matches both 138-file datasets; primary also has empty .lock. P06 29 files, P07 17 images/seven receipt hashes verified. Read-only journal replay and verification preserve dataset bytes and mtimes. No real queries/downloads or human dataset approval occurred.
+
+Independent reviewer p08_independent_review first noted the conditional timeout issue; before freeze, a synthetic proof established a violation of the approved mechanism, and the reviewer consolidated B1. This is the first frozen review, not a fabricated past approval. Proof proof-6928ea925e6f438e3873543389326106 exited 1: acquire_inat converted timeout to inaturalist_contract_or_evidence, which is outside RETRYABLE. Real iNaturalist is still blocked by absent crosswalk; the bug did not modify preserved data.
+
+Guard: review_frozen, next_action fix_required, B1 open, zero fix rounds/redesign; no terminal completed/stopped state. Owner explicitly forbids code/test correction during this closure and requires halt on gate failure. Therefore no second commit or push. Final Git secrets/private-data/images inspection remains not_run after the halt, and no human rights/botanical/privacy review is claimed. There is no fabricated stop category; the nonterminal blocker is preserved.
+
+1088 pending, zero transferred/approved_for_dataset/usable. Human receipt accepts technical/documentary bytes and zero-transfer result only. Training unauthorized; release pending; P09 not started. Local HEAD unchanged, upstream unset, remote branch absent; upstream divergence is unavailable, not 0/0.
diff --git a/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt
new file mode 100644
index 0000000..dae0c61
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt
@@ -0,0 +1,5 @@
+{
+  "ignore_rule": "/.superpowers/",
+  "tracked_root_artifacts": [],
+  "valid": true
+}
diff --git a/artifacts/bianchini/v2/codex/P08/closure/review-package.md b/artifacts/bianchini/v2/codex/P08/closure/review-package.md
new file mode 100644
index 0000000..7a947c9
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/review-package.md
@@ -0,0 +1,3233 @@
+# Review Package
+
+- Base: `24de252d27a137281c02cad50533280bb82dd80d`
+- Head: `7981377a433270c9e2072fcafdf89b690988fa08`
+- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md` (a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36)
+- Report: `artifacts/bianchini/v2/codex/P08/continuation-report.md` (fc42eb7ba4a348d0edb206dcf69867ef1bbea45b73a6a4b4a44443b303f5635d)
+- Security notice: sanitização heurística; 2 ocorrência(s) removida(s). Revise antes de compartilhar.
+
+## Commits
+
+```text
+7981377 feat(p08): add bounded traceable dataset recovery
+```
+
+## Stat
+
+```text
+artifacts/bianchini/v2/codex/P08/audit-final.json  |  18 +
+ artifacts/bianchini/v2/codex/P08/checkpoint.json   |  86 +++
+ .../v2/codex/P08/continuation-checkpoint.json      |  93 +++
+ .../bianchini/v2/codex/P08/continuation-report.md  |  46 ++
+ .../bianchini/v2/codex/P08/final-files.sha256      |  31 +
+ .../bianchini/v2/codex/P08/focal-inat-final.txt    |   5 +
+ artifacts/bianchini/v2/codex/P08/focal-inat.txt    |   5 +
+ .../v2/codex/P08/focal-recovery-final.txt          |   5 +
+ .../bianchini/v2/codex/P08/full-suite-final.txt    |  10 +
+ artifacts/bianchini/v2/codex/P08/full-suite.txt    |  10 +
+ .../bianchini/v2/codex/P08/human-acceptance.json   |  42 ++
+ .../bianchini/v2/codex/P08/implementer-report.md   |  11 +
+ artifacts/bianchini/v2/codex/P08/inat-red.txt      |  20 +
+ artifacts/bianchini/v2/codex/P08/manifest.txt      |   1 +
+ .../v2/codex/P08/mutation-evidence-final.json      | 141 ++++
+ .../bianchini/v2/codex/P08/mutation-evidence.json  | 141 ++++
+ artifacts/bianchini/v2/codex/P08/real-round.json   |   1 +
+ artifacts/bianchini/v2/codex/P08/recovery-red.txt  |  20 +
+ .../bianchini/v2/codex/P08/resume-inventory.json   |  20 +
+ .../P08/resumed-test_inaturalist_source.py.txt     |   5 +
+ .../v2/codex/P08/resumed-test_recover_p08.py.txt   |  33 +
+ artifacts/bianchini/v2/codex/P08/roster-hashes.txt |   7 +
+ artifacts/bianchini/v2/codex/P08/task-brief.md     |  25 +
+ .../bianchini/v2/codex/P08/verification-final.json |  71 ++
+ artifacts/bianchini/v2/codex/P08/verification.json |  82 +++
+ artifacts/bianchini/v2/ledgers/P08.md              |  22 +
+ artifacts/phase1/p08/summary.json                  |   1 +
+ docs/phase1/P08-recovery.md                        |  35 +
+ scripts/phase1/inaturalist_source.py               | 259 ++++++++
+ scripts/phase1/recover_p08.py                      | 737 +++++++++++++++++++++
+ scripts/phase1/test_inaturalist_source.py          | 158 +++++
+ scripts/phase1/test_p08_mutation.py                | 145 ++++
+ scripts/phase1/test_recover_p08.py                 | 692 +++++++++++++++++++
+ 33 files changed, 2978 insertions(+)
+```
+
+## Diff
+
+```diff
+diff --git a/artifacts/bianchini/v2/codex/P08/audit-final.json b/artifacts/bianchini/v2/codex/P08/audit-final.json
+new file mode 100644
+index 0000000..ca877ea
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/audit-final.json
+@@ -0,0 +1,18 @@
++{
++  "tracked_diff_empty": true,
++  "index_empty": true,
++  "git_diff_check_exit": 0,
++  "untracked_diff_check": "passed_all_files",
++  "secrets_binary_images_temps_private_dataset_paths": "no_findings",
++  "human_candidate_data_in_git": false,
++  "guard": {
++    "exit_code": 2,
++    "stdout": "",
++    "stderr": "erro: sidecar n\u00e3o encontrado: artifacts/bianchini/v2/codex/convergence/P08/1.json\n",
++    "sidecar_exists": false
++  },
++  "status": "## bm/v2-p08\n?? artifacts/bianchini/v2/codex/P08/audit-final.json\n?? artifacts/bianchini/v2/codex/P08/checkpoint.json\n?? artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json\n?? artifacts/bianchini/v2/codex/P08/continuation-report.md\n?? artifacts/bianchini/v2/codex/P08/final-files.sha256\n?? artifacts/bianchini/v2/codex/P08/focal-inat-final.txt\n?? artifacts/bianchini/v2/codex/P08/focal-inat.txt\n?? artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt\n?? artifacts/bianchini/v2/codex/P08/full-suite-final.txt\n?? artifacts/bianchini/v2/codex/P08/full-suite.txt\n?? artifacts/bianchini/v2/codex/P08/implementer-report.md\n?? artifacts/bianchini/v2/codex/P08/inat-red.txt\n?? artifacts/bianchini/v2/codex/P08/manifest.txt\n?? artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json\n?? artifacts/bianchini/v2/codex/P08/mutation-evidence.json\n?? artifacts/bianchini/v2/codex/P08/real-round.json\n?? artifacts/bianchini/v2/codex/P08/recovery-red.txt\n?? artifacts/bianchini/v2/codex/P08/resume-inventory.json\n?? artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt\n?? artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt\n?? artifacts/bianchini/v2/codex/P08/roster-hashes.txt\n?? artifacts/bianchini/v2/codex/P08/task-brief.md\n?? artifacts/bianchini/v2/codex/P08/verification-final.json\n?? artifacts/bianchini/v2/codex/P08/verification.json\n?? artifacts/bianchini/v2/ledgers/P08.md\n?? artifacts/phase1/p08/summary.json\n?? docs/phase1/P08-recovery.md\n?? scripts/phase1/inaturalist_source.py\n?? scripts/phase1/recover_p08.py\n?? scripts/phase1/test_inaturalist_source.py\n?? scripts/phase1/test_p08_mutation.py\n?? scripts/phase1/test_recover_p08.py\n",
++  "file_count": 32,
++  "inventory_basis": "final-files.sha256",
++  "stat_semantics": "all delivery files are untracked additions; git tracked diff --stat is empty"
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/checkpoint.json b/artifacts/bianchini/v2/codex/P08/checkpoint.json
+new file mode 100644
+index 0000000..26d5a1e
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/checkpoint.json
+@@ -0,0 +1,86 @@
++{
++  "method_version": 2,
++  "planning_status": "approved",
++  "approval": "approved",
++  "plans": [
++    {
++      "id": "P01",
++      "status": "blocked",
++      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
++    },
++    {
++      "id": "P02",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P02.md"
++    },
++    {
++      "id": "P03",
++      "status": "blocked",
++      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
++    },
++    {
++      "id": "P04",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P04.md"
++    },
++    {
++      "id": "P05",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
++    },
++    {
++      "id": "P05-R1",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
++    },
++    {
++      "id": "P07",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P07.md"
++    },
++    {
++      "id": "P08",
++      "status": "approved",
++      "ledger": "artifacts/bianchini/v2/ledgers/P08.md"
++    }
++  ],
++  "release": {
++    "status": "pending",
++    "platforms": [
++      "ASP.NET Core .NET 8",
++      "Android Expo/React Native"
++    ],
++    "profiles": [
++      "Release"
++    ],
++    "candidate": null,
++    "final_gate": "homologar-sistema",
++    "homologation": "pending",
++    "final_review": "pending",
++    "delivery": "pending"
++  },
++  "next_action": "Aguardar autorização posterior de execução P08 sobre o plano publicado. Pacote/digest P08 integralmente aprovado; esta rodada autoriza somente registro, staging, commit e push do planejamento. P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed; guard completed sem blockers; usable=0 até decisões humanas válidas; P06/P07 fechados e imutáveis; release pending; active_execution null; treinamento não autorizado; P09 não iniciado.",
++  "workspace": "/tmp/scanplant-p08-execution",
++  "git": {
++    "branch": "bm/v2-p08",
++    "head": "24de252d27a137281c02cad50533280bb82dd80d",
++    "dirty": true
++  },
++  "ledger_tail": [
++    "# P08 execution ledger",
++    "",
++    "- Approved package: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`.",
++    "- Base revision: `24de252d27a137281c02cad50533280bb82dd80d`; P07 base `b6844f9129d9edf862ae7958d8f043d9bdd5bd84`.",
++    "- Workspace: `/tmp/scanplant-p08-execution`; branch `bm/v2-p08`.",
++    "- Method installation: active .agents, version 3.2.0, v2-standalone.",
++    "- Profile standard; technical mode strict/per_task, data-transform, one unit `1`; authorized grouped operational round.",
++    "- Explicit current user authorization supersedes historical planning-only scope, grants implementation and bounded collection, prohibits staging/commit/push/release.",
++    "- Preflight: root/branch/HEAD/upstream/remote, clean index/tree, only three known starting worktrees, snapshot and manifest, strict planning audit and hygiene passed. P07/guard completed, usable=0; P08 approved/unstarted, release pending, P09 absent. Python 3.14.4/Pillow 12.3.0 available.",
++    "- P06: 29 files, SHA256SUMS passed; 17/17 image hashes match P07 closure. All seven final external P07 hashes match. No historical mutation.",
++    "- `bm change-policy --file-location`: bounded_amendment; evidence artifacts and temporary execution workspace location recorded, approved plan immutable.",
++    "- RED: recovery-red.txt and inat-red.txt record missing-module failures before implementation. GREEN initial focal runs passed.",
++    "- Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.",
++    "- Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.",
++    "- Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint."
++  ]
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json b/artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json
+new file mode 100644
+index 0000000..a14a5c8
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json
+@@ -0,0 +1,93 @@
++{
++  "method_version": 2,
++  "planning_status": "approved",
++  "approval": "approved",
++  "plans": [
++    {
++      "id": "P01",
++      "status": "blocked",
++      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
++    },
++    {
++      "id": "P02",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P02.md"
++    },
++    {
++      "id": "P03",
++      "status": "blocked",
++      "ledger": "artifacts/bianchini/v2/ledgers/P01.md"
++    },
++    {
++      "id": "P04",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P04.md"
++    },
++    {
++      "id": "P05",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
++    },
++    {
++      "id": "P05-R1",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P05.md"
++    },
++    {
++      "id": "P07",
++      "status": "completed",
++      "ledger": "artifacts/bianchini/v2/ledgers/P07.md"
++    },
++    {
++      "id": "P08",
++      "status": "approved",
++      "ledger": "artifacts/bianchini/v2/ledgers/P08.md"
++    }
++  ],
++  "release": {
++    "status": "pending",
++    "platforms": [
++      "ASP.NET Core .NET 8",
++      "Android Expo/React Native"
++    ],
++    "profiles": [
++      "Release"
++    ],
++    "candidate": null,
++    "final_gate": "homologar-sistema",
++    "homologation": "pending",
++    "final_review": "pending",
++    "delivery": "pending"
++  },
++  "next_action": "Aguardar autorização posterior de execução P08 sobre o plano publicado. Pacote/digest P08 integralmente aprovado; esta rodada autoriza somente registro, staging, commit e push do planejamento. P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed; guard completed sem blockers; usable=0 até decisões humanas válidas; P06/P07 fechados e imutáveis; release pending; active_execution null; treinamento não autorizado; P09 não iniciado.",
++  "workspace": "/tmp/scanplant-p08-execution",
++  "git": {
++    "branch": "bm/v2-p08",
++    "head": "24de252d27a137281c02cad50533280bb82dd80d",
++    "dirty": true
++  },
++  "ledger_tail": [
++    "# P08 execution ledger",
++    "",
++    "- Approved package: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`.",
++    "- Base revision: `24de252d27a137281c02cad50533280bb82dd80d`; P07 base `b6844f9129d9edf862ae7958d8f043d9bdd5bd84`.",
++    "- Workspace: `/tmp/scanplant-p08-execution`; branch `bm/v2-p08`.",
++    "- Method installation: active .agents, version 3.2.0, v2-standalone.",
++    "- Profile standard; technical mode strict/per_task, data-transform, one unit `1`; authorized grouped operational round.",
++    "- Explicit current user authorization supersedes historical planning-only scope, grants implementation and bounded collection, prohibits staging/commit/push/release.",
++    "- Preflight: root/branch/HEAD/upstream/remote, clean index/tree, only three known starting worktrees, snapshot and manifest, strict planning audit and hygiene passed. P07/guard completed, usable=0; P08 approved/unstarted, release pending, P09 absent. Python 3.14.4/Pillow 12.3.0 available.",
++    "- P06: 29 files, SHA256SUMS passed; 17/17 image hashes match P07 closure. All seven final external P07 hashes match. No historical mutation.",
++    "- `bm change-policy --file-location`: bounded_amendment; evidence artifacts and temporary execution workspace location recorded, approved plan immutable.",
++    "- RED: recovery-red.txt and inat-red.txt record missing-module failures before implementation. GREEN initial focal runs passed.",
++    "- Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.",
++    "- Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.",
++    "- Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint.",
++    "",
++    "- Continuation recovered the exact checkpoint digest and eleven untracked files; existing workspace reused, baseline HEAD unchanged, no upstream.",
++    "- Final continuation evidence: artifacts/bianchini/v2/codex/P08/continuation-report.md and verification-final.json. 51 recovery + 15 adapter focal tests; 233 full historical/affected tests; five selective mutations killed, zero survivors.",
++    "- Real Commons round: 120 successful metadata requests, 1090 class associations/1088 unique candidates, all pending, no media transfer. iNaturalist no_crosswalk, zero requests. P07 17/17 bytes and mtimes preserved.",
++    "- Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.",
++    "- External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.",
++    "- Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending."
++  ]
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/continuation-report.md b/artifacts/bianchini/v2/codex/P08/continuation-report.md
+new file mode 100644
+index 0000000..851b0aa
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/continuation-report.md
+@@ -0,0 +1,46 @@
++# P08 continuation report
++
++## Recovery
++
++Method 3.2.0; skill and three ordered overlay contracts read. Existing workspace resumed, technical mode strict/per_task, one operational grouped round. No new worktree, index update, commit, push or historical source edit.
++
++Checkpoint SHA-256: `9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230`, exact expected bytes, identity and ledger matched. Original checkpoint remains immutable. Planning snapshot verified: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`. Branch `bm/v2-p08`, HEAD/baseline `24de252d27a137281c02cad50533280bb82dd80d`, ancestry satisfied, no upstream. Remote origin is the existing project GitHub repository; local origin/bm/v2-p08-planning matches baseline.
++
++Eleven untracked files existed at recovery; exact paths and SHA-256 are in `resume-inventory.json`. No external P08 dataset existed. No active collector found in host process inspection before the round; dataset exclusive lock enforced. No recoverable prior mutation output or detailed independent reviewer report was present; the implementer report was a skeleton. Historical RED logs and mutation harness preserved. The recovered checkpoint records process state, not implementation hashes or test results.
++
++## Review and corrections
++
++1. Recovered tests exposed two failed assertions: HTTP 200 response bodies failing size checks or timing out were journaled as `ok`. Response outcome now records the actual error; transient body timeouts retry within cumulative quotas.
++2. A failed media transfer could leave its source marked exhausted. Acquisition now records a retryable source failure, reuses the durable page on restart and does not reset quotas.
++3. Durable finalization now requires the inspected candidate and attribution bundle to match hashes/source/author/license before approval; taxonomic and botanical evidence files remain SHA-bound. Tests cover missing/changed evidence, stale mapping/class/author decisions, final-manifest coverage and replay.
++4. Unsupported media are retained as rejected-format metadata without transfer; an empty malformed Commons schema is rejected.
++5. The real first reopened inspection exposed HTML field-order instability. Read-only reconstruction identified `review.html` as the sole differing projection. Sorted key rendering fixes it. An exact predecessor code fingerprint is accepted only with all other code/config/manifest fingerprints unchanged; a durable `code_compatibility` event records predecessor/current hashes. Original config and journal prefix were preserved. `bm change-policy --internal-order` classified this as bounded_amendment; the approved plan is unchanged.
++
++The symptoms of the two earlier findings supplied in the handoff (transient resumption and human/taxonomic/manifest binding) have explicit regression coverage. Their original reviewer IDs/report were not recovered, so no independent-review approval is invented. Review in this continuation was inline against the frozen plan/spec. Current authority remains pending human acceptance.
++
++## Proofs
++
++- Final focused recovery: 51 passed; adapter: 15 passed.
++- Final full historical/affected suite: 233 passed. Full-suite output and command/fingerprint manifests retained.
++- Five selective mutations killed, no material survivor, fresh subprocesses, zero network calls. Initial continuation campaign is preserved; final campaign was necessary after the proven production-code change invalidated its byte fingerprint.
++- Manifest/approved roster validation and SHA256SUMS passed. No unrelated release/.NET mutation campaign was run.
++- Tests cover transport/SSRF, 403, 429/5xx/maxlag, date/seconds Retry-After, request/hour/media/transfer/page quotas, partial body counts, fsync errors, corrupt/truncated journal, symlinks/missing objects, five ingest crash boundaries, process concurrency, EXIF sanitization, original preservation, rights, taxonomy/human binding and dHash boundary comparisons against 17 synthetic prior references.
++- Real acquire and inspect replay are byte+mtime stable after the HTML correction. Real comparison loaded all 17 historical images; no new media existed for pixel pairs. All 17 SHA-256 and mtimes match before/after; exact values in `real-round.json` and the external report.
++
++## Real round
++
++120 Commons metadata requests, 120 pages, 2,127,950 response bytes, zero failed responses/source failures. 1,090 unique class associations, 1,088 distinct media IDs, zero transferred/rejected, 1,088 pending. No original/sanitized P08 image hash exists: no image was downloaded. No new media-to-P07 perceptual pairs exist; this is not a claim of visual distinctness.
++
++Commons database/source-rights clearance remains pending; individual media metadata alone was not promoted to legal clearance. No human authorship, privacy, botanical or dataset release decision was fabricated. iNaturalist: no approved human crosswalk, zero requests/transfers. All twelve species show `no_crosswalk`; two protections are unqueried on both sources. Eleven Commons queries hit the page budget, species_04 exhausted within its query. Per-class results are in `artifacts/phase1/p08/summary.json`; totals are not training sufficiency.
++
++The private human-review JSON/HTML contains every candidate with stable ID, source URLs, declared authorship/license/attribution, evidence hash, absent-media-hash reason, proposed classes, taxonomy, quality/privacy/duplicate status, technical recommendation and pending human decision. Object-hash inventory explicitly records null original/sanitized hashes. There are 138 external files plus the empty lock; the verified private backup contains the same 138 files. Directories 0700/files 0600. The final dataset manifest SHA-256 is `334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716`.
++
++## Guard and authority
++
++`review_guard status` reports no P08 sidecar. Proof execution requires a committed revision and creates a new isolated worktree, both forbidden in this round. No fake proof_id, freeze, completed/stopped state, sidecar edit or method-state change was made. Therefore local tests/byte proofs passed, but formal guard completion and independent commit-bound review remain unavailable. Fix rounds/redesign: none recorded by guard; no claim of terminal completion.
++
++Release pending, active execution state unchanged, current specs/P06/P07/P09 unchanged. Pending: real human per-item decisions (legitimate pending outcomes allowed), rights/qualified botanical/privacy review as applicable, U-804 acceptance of final bytes, and explicit future staging/commit/push authorization. No automatic publication. Suggested commit after acceptance: `feat(p08): add bounded traceable dataset recovery`.
++
++## Audit and inventories
++
++`resume-inventory.json` identifies every preexisting file; `final-files.sha256` inventories exact final changed/untracked Git bytes, excluding itself. Its own SHA-256 is the Git-delivery digest. `audit-final.json` records hygiene, diff checks, guard status and index state. The original checkpoint is preserved; `continuation-checkpoint.json` is newly emitted by the CLI. External filenames and all hashes are in private `final-manifest.json`; no raw source responses, item URLs, authors, images or review HTML were copied into Git.
+diff --git a/artifacts/bianchini/v2/codex/P08/final-files.sha256 b/artifacts/bianchini/v2/codex/P08/final-files.sha256
+new file mode 100644
+index 0000000..9cfa969
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/final-files.sha256
+@@ -0,0 +1,31 @@
++4431ab3f00cdeec62fecbb2058f18dcfb63c4d33b223bd5f972726493cb97c80  artifacts/bianchini/v2/codex/P08/audit-final.json
++9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230  artifacts/bianchini/v2/codex/P08/checkpoint.json
++edce9f48d1a230bfb2aa98072b99f2d8ef28ec30bcc92c87206667a7cae80296  artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json
++fc42eb7ba4a348d0edb206dcf69867ef1bbea45b73a6a4b4a44443b303f5635d  artifacts/bianchini/v2/codex/P08/continuation-report.md
++2fdf7a432a53fceb691486981be60fcb65192fbaa6b7627e6b3fe3a0c95917bf  artifacts/bianchini/v2/codex/P08/focal-inat-final.txt
++edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0  artifacts/bianchini/v2/codex/P08/focal-inat.txt
++2685ccaab15660c44c951beb8fe9c19d6d9e9e347b91699628320b87c86b058f  artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt
++ed24024f0c3d1b17f96cc32552dd6391462ca11089c74f599305c51d7ec0a660  artifacts/bianchini/v2/codex/P08/full-suite-final.txt
++3d6689642da34d73791790f53db3d6b989e16eabbd850972ccfaa176e92b2db0  artifacts/bianchini/v2/codex/P08/full-suite.txt
++b3cb7bb752829b2c95971653c14d460b7e26f2ef095b895f2b33921fe94c1a5b  artifacts/bianchini/v2/codex/P08/implementer-report.md
++5588c065e674a94b4cfc0f14748eac93d6f2fb0101e5f32a5e992420840eb645  artifacts/bianchini/v2/codex/P08/inat-red.txt
++0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe  artifacts/bianchini/v2/codex/P08/manifest.txt
++23527bd62c51bdc91b6bf9193ed60bf68a267c0dbd432ac4be88a05fc6f1c315  artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json
++55ef68eefb2e85931f2c4a303d161b326bccea87468311ec22db47ee62996ba5  artifacts/bianchini/v2/codex/P08/mutation-evidence.json
++d090bc5706aeff5ae351260208365c2e37a83eec2570b8085a5dbbfd9e78b0af  artifacts/bianchini/v2/codex/P08/real-round.json
++9d56b591390394d0f50ce1532442a2bc571c26c93329b08a92e518521092fc34  artifacts/bianchini/v2/codex/P08/recovery-red.txt
++61c61bfa952bc0d2958c9eb1dc4fb053bf30700e9cd67da051679cb9b4f6a19f  artifacts/bianchini/v2/codex/P08/resume-inventory.json
++c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc  artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt
++e885f40ddecec4eef4b0585e1f71e621c9f3188e3aaf84bda2ec2856e74763a2  artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt
++850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3  artifacts/bianchini/v2/codex/P08/roster-hashes.txt
++a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36  artifacts/bianchini/v2/codex/P08/task-brief.md
++8893c65c032fbb63e54671ad422e661421c5d1ee354ecf2716cb103f1e5ccd3b  artifacts/bianchini/v2/codex/P08/verification-final.json
++7de6424ec7e3e7d6cbec51fa4402a5c3d1d5780a8431808891d81be913635296  artifacts/bianchini/v2/codex/P08/verification.json
++d64f79f7adb25303cb636a9a5dac32d21456e6b7f0f381559c9b9f441335ee35  artifacts/bianchini/v2/ledgers/P08.md
++d1130531abea27c2d6bb157fda7be376b3cefec514b49fb5374c82fcd8cb2c4f  artifacts/phase1/p08/summary.json
++10c454fcc82cf17a8051f37e8ca81defcd3a78ae6f180c8008e4bfb89b0d218b  docs/phase1/P08-recovery.md
++bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366  scripts/phase1/inaturalist_source.py
++61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65  scripts/phase1/recover_p08.py
++bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e  scripts/phase1/test_inaturalist_source.py
++ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad  scripts/phase1/test_p08_mutation.py
++d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926  scripts/phase1/test_recover_p08.py
+diff --git a/artifacts/bianchini/v2/codex/P08/focal-inat-final.txt b/artifacts/bianchini/v2/codex/P08/focal-inat-final.txt
+new file mode 100644
+index 0000000..a4a4934
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/focal-inat-final.txt
+@@ -0,0 +1,5 @@
++...............
++----------------------------------------------------------------------
++Ran 15 tests in 0.009s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/focal-inat.txt b/artifacts/bianchini/v2/codex/P08/focal-inat.txt
+new file mode 100644
+index 0000000..070e7a6
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/focal-inat.txt
+@@ -0,0 +1,5 @@
++...............
++----------------------------------------------------------------------
++Ran 15 tests in 0.007s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt b/artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt
+new file mode 100644
+index 0000000..539f5da
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt
+@@ -0,0 +1,5 @@
++...................................................
++----------------------------------------------------------------------
++Ran 51 tests in 2.829s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/full-suite-final.txt b/artifacts/bianchini/v2/codex/P08/full-suite-final.txt
+new file mode 100644
+index 0000000..79b88ed
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/full-suite-final.txt
+@@ -0,0 +1,10 @@
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "advance_cursor_before_commit"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 3, "mode": "mutant", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "allow_private_export"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "bypass_expert"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_license", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 8, "material_changes_reached": 8, "mock_calls": 9, "mode": "mutant", "network_calls": 0, "seam": "bypass_license", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "bypass_license"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 2, "mode": "mutant", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65", "tests_run": 1, "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"}, "selective_mutation": "ignore_hash_mismatch"}
++.........................................................................................................................................................................................................................................
++----------------------------------------------------------------------
++Ran 233 tests in 10.514s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/full-suite.txt b/artifacts/bianchini/v2/codex/P08/full-suite.txt
+new file mode 100644
+index 0000000..e70a8b0
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/full-suite.txt
+@@ -0,0 +1,10 @@
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "selective_mutation": "advance_cursor_before_commit"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 3, "mode": "mutant", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "selective_mutation": "allow_private_export"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "selective_mutation": "bypass_expert"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_license", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "mutant": {"errors": 0, "failures": 8, "material_changes_reached": 8, "mock_calls": 9, "mode": "mutant", "network_calls": 0, "seam": "bypass_license", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "selective_mutation": "bypass_license"}
++{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 2, "mode": "mutant", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57", "tests_run": 1, "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"}, "selective_mutation": "ignore_hash_mismatch"}
++.......................................................................................................................................................................................................................................
++----------------------------------------------------------------------
++Ran 231 tests in 9.984s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/human-acceptance.json b/artifacts/bianchini/v2/codex/P08/human-acceptance.json
+new file mode 100644
+index 0000000..b7c5bdb
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/human-acceptance.json
+@@ -0,0 +1,42 @@
++{
++  "schema_version": 1,
++  "plan": "P08",
++  "authority": "human",
++  "source": "explicit_user_instruction_in_current_session",
++  "recorded_at": "2026-10-05T23:15:31.700977+00:00",
++  "scope": "technical_and_documentary_bytes_only",
++  "decision": "accepted",
++  "U-804": "technical_bytes_accepted",
++  "U-803": "candidate_opinions_pending",
++  "approved_git_delivery_sha256": "5c5c61406db304c42671a727a2016b566b2e5d5fca2c487466f3adebb09055b2",
++  "approved_external_manifest_sha256": "334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716",
++  "approved_checkpoint_sha256": "edce9f48d1a230bfb2aa98072b99f2d8ef28ec30bcc92c87206667a7cae80296",
++  "baseline": "24de252d27a137281c02cad50533280bb82dd80d",
++  "counts": {
++    "candidates_pending": 1088,
++    "transferred": 0,
++    "p08_images": 0,
++    "approved_for_dataset": 0,
++    "usable": 0
++  },
++  "candidate_approval": false,
++  "download_authorized": false,
++  "authorship_confirmation": false,
++  "rights_approval": false,
++  "botanical_confirmation": false,
++  "privacy_approval": false,
++  "duplicate_decisions_conclusive": false,
++  "training_authorized": false,
++  "partition_authorized": false,
++  "release": "pending",
++  "p09_started": false,
++  "zero_transfer_result_accepted": true,
++  "experimental_sufficiency": "not_demonstrated",
++  "publication_authorization": {
++    "implementation_commit": true,
++    "closure_commit": "only_after_guard_passed_and_no_material_blockers",
++    "push": "one_normal_push_only_after_both_valid_commits_guard_completed_and_clean_tree",
++    "force_push": false
++  },
++  "preservation": "Approved 32 files and external dataset remain unchanged; this separate receipt does not approve any candidate."
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/implementer-report.md b/artifacts/bianchini/v2/codex/P08/implementer-report.md
+new file mode 100644
+index 0000000..a5376c7
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/implementer-report.md
+@@ -0,0 +1,11 @@
++# Implementer Report
++
++- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md`
++- Status: PENDING_HUMAN_ACCEPTANCE
++- Full report: `continuation-report.md`
++- Recovery inventory: `resume-inventory.json`
++- Final tests: `verification-final.json`; 51 focal recovery, 15 adapter, 233 full suite.
++- Final selective mutations: `mutation-evidence-final.json`; five killed, zero material survivors.
++- Real collection: `real-round.json`; 1088 unique candidates pending, zero transferred/usable.
++- Formal guard unavailable for uncommitted working bytes; no false commit-bound proof.
++- No staging, commit, push, release or historical dataset mutation.
+diff --git a/artifacts/bianchini/v2/codex/P08/inat-red.txt b/artifacts/bianchini/v2/codex/P08/inat-red.txt
+new file mode 100644
+index 0000000..cea80c5
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/inat-red.txt
+@@ -0,0 +1,20 @@
++E
++======================================================================
++ERROR: test_inaturalist_source (unittest.loader._FailedTest.test_inaturalist_source)
++----------------------------------------------------------------------
++ImportError: Failed to import test module: test_inaturalist_source
++Traceback (most recent call last):
++  File "/usr/lib/python3.14/unittest/loader.py", line 426, in _find_test_path
++    module = self._get_module_from_name(name)
++  File "/usr/lib/python3.14/unittest/loader.py", line 367, in _get_module_from_name
++    __import__(name)
++    ~~~~~~~~~~^^^^^^
++  File "/tmp/scanplant-p08-execution/scripts/phase1/test_inaturalist_source.py", line 4, in <module>
++    from inaturalist_source import ContractError, build_query, parse_page, photo_record
++ModuleNotFoundError: No module named 'inaturalist_source'
++
++
++----------------------------------------------------------------------
++Ran 1 test in 0.000s
++
++FAILED (errors=1)
+diff --git a/artifacts/bianchini/v2/codex/P08/manifest.txt b/artifacts/bianchini/v2/codex/P08/manifest.txt
+new file mode 100644
+index 0000000..e507626
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/manifest.txt
+@@ -0,0 +1 @@
++{"aliases": 79, "classes": 14, "manifest_sha256": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c", "manifest_version": "1.1.0", "normalization_version": "1", "protection": 2, "roster_sha256": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b", "schema_version": 1, "scientific_keys": 91, "species": 12, "valid": true}
+diff --git a/artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json b/artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json
+new file mode 100644
+index 0000000..53e4478
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json
+@@ -0,0 +1,141 @@
++{
++  "runs": [
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "advance_cursor_before_commit",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 1,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "advance_cursor_before_commit",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "selective_mutation": "advance_cursor_before_commit"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "allow_private_export",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 3,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "allow_private_export",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "selective_mutation": "allow_private_export"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "bypass_expert",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 1,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "bypass_expert",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "selective_mutation": "bypass_expert"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "bypass_license",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 8,
++        "material_changes_reached": 8,
++        "mock_calls": 9,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "bypass_license",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "selective_mutation": "bypass_license"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "ignore_hash_mismatch",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 2,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "ignore_hash_mismatch",
++        "source_sha256": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++        "tests_run": 1,
++        "tests_sha256": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926"
++      },
++      "selective_mutation": "ignore_hash_mismatch"
++    }
++  ],
++  "material_survivors": 0,
++  "reason_repeated": "production fingerprint changed by proven journal-reopen HTML defect; prior evidence preserved"
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/mutation-evidence.json b/artifacts/bianchini/v2/codex/P08/mutation-evidence.json
+new file mode 100644
+index 0000000..40d9d1b
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/mutation-evidence.json
+@@ -0,0 +1,141 @@
++{
++  "runs": [
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "advance_cursor_before_commit",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 1,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "advance_cursor_before_commit",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "selective_mutation": "advance_cursor_before_commit"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "allow_private_export",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 3,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "allow_private_export",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "selective_mutation": "allow_private_export"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "bypass_expert",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 1,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "bypass_expert",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "selective_mutation": "bypass_expert"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "bypass_license",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 8,
++        "material_changes_reached": 8,
++        "mock_calls": 9,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "bypass_license",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "selective_mutation": "bypass_license"
++    },
++    {
++      "baseline": {
++        "errors": 0,
++        "failures": 0,
++        "material_changes_reached": 0,
++        "mock_calls": 0,
++        "mode": "baseline",
++        "network_calls": 0,
++        "seam": "ignore_hash_mismatch",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "mutant": {
++        "errors": 0,
++        "failures": 1,
++        "material_changes_reached": 1,
++        "mock_calls": 2,
++        "mode": "mutant",
++        "network_calls": 0,
++        "seam": "ignore_hash_mismatch",
++        "source_sha256": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++        "tests_run": 1,
++        "tests_sha256": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96"
++      },
++      "selective_mutation": "ignore_hash_mismatch"
++    }
++  ],
++  "material_survivors": 0,
++  "source": "full-suite.txt"
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/real-round.json b/artifacts/bianchini/v2/codex/P08/real-round.json
+new file mode 100644
+index 0000000..f4052b8
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/real-round.json
+@@ -0,0 +1 @@
++{"backup_verified":true,"counts":{"acquire_exit":0,"examined_class_associations":1090,"failed_responses":0,"inat_requests":0,"integrity_exit":0,"media_requests":0,"p07_preserved":17,"pending":1088,"real_acquire_idempotent":true,"real_inspect_idempotent":true,"rejected":0,"request_count":120,"response_bytes":2127950,"source_failures":0,"transferred":0,"unique_candidates":1088,"usable":0},"external_file_count":138,"external_manifest_sha256":"334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716","historical_images":[{"id":"Q01","mtime_ns_after":1790635696972056223,"mtime_ns_before":1790635696972056223,"sha256_after":"b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a","sha256_before":"b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a"},{"id":"Q02","mtime_ns_after":1790635698837256434,"mtime_ns_before":1790635698837256434,"sha256_after":"cc04b39c60ff068344be25f1b6c1d1d3628afe3272edba4794b5e8fdab8188c5","sha256_before":"cc04b39c60ff068344be25f1b6c1d1d3628afe3272edba4794b5e8fdab8188c5"},{"id":"Q03","mtime_ns_after":1790635701100891598,"mtime_ns_before":1790635701100891598,"sha256_after":"2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6","sha256_before":"2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6"},{"id":"Q04","mtime_ns_after":1790635703351777011,"mtime_ns_before":1790635703351777011,"sha256_after":"7beac71d4fd1901559b36e041469666e1376dbf4b3eb761b9fec5fc8f48403bf","sha256_before":"7beac71d4fd1901559b36e041469666e1376dbf4b3eb761b9fec5fc8f48403bf"},{"id":"Q05","mtime_ns_after":1790635704652998875,"mtime_ns_before":1790635704652998875,"sha256_after":"0fa0c0fe80f1fe1f90e2e1a8f81e6d5146a0956afe1ca00ba45c4f410b3e96b6","sha256_before":"0fa0c0fe80f1fe1f90e2e1a8f81e6d5146a0956afe1ca00ba45c4f410b3e96b6"},{"id":"Q06","mtime_ns_after":1790635707394205230,"mtime_ns_before":1790635707394205230,"sha256_after":"38fdf4d90431956bccf426e9ec4b0281d9441fd968766add985832f4f900b251","sha256_before":"38fdf4d90431956bccf426e9ec4b0281d9441fd968766add985832f4f900b251"},{"id":"Q07","mtime_ns_after":1790635708988768554,"mtime_ns_before":1790635708988768554,"sha256_after":"4aa046916264dc5d892121b1d9cc3dd5212bb9bb1bc50e999376d023286a9550","sha256_before":"4aa046916264dc5d892121b1d9cc3dd5212bb9bb1bc50e999376d023286a9550"},{"id":"Q08","mtime_ns_after":1790635932743919560,"mtime_ns_before":1790635932743919560,"sha256_after":"09d9fb06033b07a8305c2f46a6d6e292b090ca66e4a8b8668a5ea0a610c3766b","sha256_before":"09d9fb06033b07a8305c2f46a6d6e292b090ca66e4a8b8668a5ea0a610c3766b"},{"id":"Q09","mtime_ns_after":1790635712835314298,"mtime_ns_before":1790635712835314298,"sha256_after":"e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048","sha256_before":"e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048"},{"id":"Q10","mtime_ns_after":1790635713648736138,"mtime_ns_before":1790635713648736138,"sha256_after":"bbccd447a0f4713cd86685b0e358733941a44a38d58447989f36bb9db42c6856","sha256_before":"bbccd447a0f4713cd86685b0e358733941a44a38d58447989f36bb9db42c6856"},{"id":"Q11","mtime_ns_after":1790635717242536946,"mtime_ns_before":1790635717242536946,"sha256_after":"0440649cc6d6f7246f9858b79b408dc7c683fd6fac3c25695281cf5219b95847","sha256_before":"0440649cc6d6f7246f9858b79b408dc7c683fd6fac3c25695281cf5219b95847"},{"id":"Q12","mtime_ns_after":1790635718641678957,"mtime_ns_before":1790635718641678957,"sha256_after":"ade5fe488454b574c5048aafc80abc74a914e59e53a8ecb70e997b8c5aa21f88","sha256_before":"ade5fe488454b574c5048aafc80abc74a914e59e53a8ecb70e997b8c5aa21f88"},{"id":"Q13","mtime_ns_after":1790635721391534883,"mtime_ns_before":1790635721391534883,"sha256_after":"a51f75db036a8fc96ec3929e514525eb2757763d6204dc8d2688f4c270a4e9e8","sha256_before":"a51f75db036a8fc96ec3929e514525eb2757763d6204dc8d2688f4c270a4e9e8"},{"id":"Q14","mtime_ns_after":1790635723698070985,"mtime_ns_before":1790635723698070985,"sha256_after":"816faa9cc87e736ea2293c887728a9d2ecac6a46396ed675ce7716ca7623d457","sha256_before":"816faa9cc87e736ea2293c887728a9d2ecac6a46396ed675ce7716ca7623d457"},{"id":"Q15","mtime_ns_after":1790635938137987340,"mtime_ns_before":1790635938137987340,"sha256_after":"d5a93acdc94d279cf38fff53bca0a06615351aebbfb26c8a620cbdddc1ae370b","sha256_before":"d5a93acdc94d279cf38fff53bca0a06615351aebbfb26c8a620cbdddc1ae370b"},{"id":"Q16","mtime_ns_after":1790635940958095232,"mtime_ns_before":1790635940958095232,"sha256_after":"8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b","sha256_before":"8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b"},{"id":"Q17","mtime_ns_after":1790635942193340097,"mtime_ns_before":1790635942193340097,"sha256_after":"91524bde4f0351530c0818612a52bbc75fa59dca2aa0709f7a8a6273376d26b2","sha256_before":"91524bde4f0351530c0818612a52bbc75fa59dca2aa0709f7a8a6273376d26b2"}],"human_acceptance":"pending","original_object_count":0,"sanitized_object_count":0}
+diff --git a/artifacts/bianchini/v2/codex/P08/recovery-red.txt b/artifacts/bianchini/v2/codex/P08/recovery-red.txt
+new file mode 100644
+index 0000000..2b4b9b0
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/recovery-red.txt
+@@ -0,0 +1,20 @@
++E
++======================================================================
++ERROR: test_recover_p08 (unittest.loader._FailedTest.test_recover_p08)
++----------------------------------------------------------------------
++ImportError: Failed to import test module: test_recover_p08
++Traceback (most recent call last):
++  File "/usr/lib/python3.14/unittest/loader.py", line 426, in _find_test_path
++    module = self._get_module_from_name(name)
++  File "/usr/lib/python3.14/unittest/loader.py", line 367, in _get_module_from_name
++    __import__(name)
++    ~~~~~~~~~~^^^^^^
++  File "/tmp/scanplant-p08-execution/scripts/phase1/test_recover_p08.py", line 13, in <module>
++    import recover_p08 as r
++ModuleNotFoundError: No module named 'recover_p08'
++
++
++----------------------------------------------------------------------
++Ran 1 test in 0.000s
++
++FAILED (errors=1)
+diff --git a/artifacts/bianchini/v2/codex/P08/resume-inventory.json b/artifacts/bianchini/v2/codex/P08/resume-inventory.json
+new file mode 100644
+index 0000000..8819c69
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/resume-inventory.json
+@@ -0,0 +1,20 @@
++{
++  "checkpoint_sha256": "9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230",
++  "files": {
++    "artifacts/bianchini/v2/codex/P08/checkpoint.json": "9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230",
++    "artifacts/bianchini/v2/codex/P08/implementer-report.md": "3e3d88e1c7afca1e297118a81566cb99d4ca4db0dd699d27641f0582c1c097e1",
++    "artifacts/bianchini/v2/codex/P08/inat-red.txt": "5588c065e674a94b4cfc0f14748eac93d6f2fb0101e5f32a5e992420840eb645",
++    "artifacts/bianchini/v2/codex/P08/recovery-red.txt": "9d56b591390394d0f50ce1532442a2bc571c26c93329b08a92e518521092fc34",
++    "artifacts/bianchini/v2/codex/P08/task-brief.md": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
++    "artifacts/bianchini/v2/ledgers/P08.md": "ba0f37d1dd745003415f9d3e1681f00617af449e2ffb434cb3fd82cf3169984a",
++    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
++    "scripts/phase1/recover_p08.py": "9bea9e78b26f2228f803a528051521274108986a7d0230dd4980e471e254a414",
++    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
++    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
++    "scripts/phase1/test_recover_p08.py": "7e5c8e0be922bc50dabac16479b6b42312e63a43df7d89c141219895d5a59534"
++  },
++  "head": "24de252d27a137281c02cad50533280bb82dd80d",
++  "upstream": null,
++  "prior_mutation_report": "not_found",
++  "dataset_p08_existed": false
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt b/artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt
+new file mode 100644
+index 0000000..91f86cb
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt
+@@ -0,0 +1,5 @@
++...............
++----------------------------------------------------------------------
++Ran 15 tests in 0.008s
++
++OK
+diff --git a/artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt b/artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt
+new file mode 100644
+index 0000000..4a615b4
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt
+@@ -0,0 +1,33 @@
++................................FF...
++======================================================================
++FAIL: test_oversized_response_counts_received_bytes_and_failure (test_recover_p08.TransportTests.test_oversized_response_counts_received_bytes_and_failure)
++----------------------------------------------------------------------
++Traceback (most recent call last):
++  File "/tmp/scanplant-p08-execution/scripts/phase1/test_recover_p08.py", line 432, in test_oversized_response_counts_received_bytes_and_failure
++    self.assertEqual(ds.select('response')[0]['code'], 'response_size')
++    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
++AssertionError: 'ok' != 'response_size'
++- ok
+++ response_size
++
++
++======================================================================
++FAIL: test_partial_timeout_counts_bytes_on_every_retry (test_recover_p08.TransportTests.test_partial_timeout_counts_bytes_on_every_retry)
++----------------------------------------------------------------------
++Traceback (most recent call last):
++  File "/tmp/scanplant-p08-execution/scripts/phase1/test_recover_p08.py", line 445, in test_partial_timeout_counts_bytes_on_every_retry
++    self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
++    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
++AssertionError: Lists differ: ['ok', 'ok', 'ok'] != ['timeout', 'timeout', 'timeout']
++
++First differing element 0:
++'ok'
++'timeout'
++
++- ['ok', 'ok', 'ok']
+++ ['timeout', 'timeout', 'timeout']
++
++----------------------------------------------------------------------
++Ran 37 tests in 1.798s
++
++FAILED (failures=2)
+diff --git a/artifacts/bianchini/v2/codex/P08/roster-hashes.txt b/artifacts/bianchini/v2/codex/P08/roster-hashes.txt
+new file mode 100644
+index 0000000..dd68c00
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/roster-hashes.txt
+@@ -0,0 +1,7 @@
++artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json: OK
++artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md: OK
++artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json: OK
++docs/phase1/F1-MAN01-offline-class-manifest.md: OK
++docs/phase1/offline-class-manifest.v1.json: OK
++scripts/phase1/test_offline_manifest.py: OK
++scripts/phase1/validate_offline_manifest.py: OK
+diff --git a/artifacts/bianchini/v2/codex/P08/task-brief.md b/artifacts/bianchini/v2/codex/P08/task-brief.md
+new file mode 100644
+index 0000000..f66bd52
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/task-brief.md
+@@ -0,0 +1,25 @@
++# Task Brief 1
++
++- Plan: `docs/bianchini/changes/v2/plans/P08-dataset-recovery.md`
++- Plan SHA-256: `1d7e4dd67033c9ff28ebf5a2463c12b5ff7b9795b2701b899addafc12ba1acfe`
++- Kind: `task`
++- Group ID: `n/a`
++- Group SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`
++- Unit `1` SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`
++
++### Tarefa 1 — obter e preservar candidatos com decisões rastreáveis e aceite final
++
++**Execution:** strict
++**Review:** per_task
++**Change:** data-transform
++**Readiness refs:** D-801, D-802, D-803, D-804, D-805, A-801, A-802, P-801, P-802, U-801, U-802, U-803, U-804, S-801, SD-801
++**Test seams:** p08-source-contract, p08-taxonomic-map, p08-journal-integrity, p08-sanitization, p08-human-approval.
++**Spec refs:** docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md §1 autoridade; §2 arquitetura/CLI; §3 fontes/limites; §4 taxonomia/consultas; §5 direitos/storage; §6 journal; §7 triagem/estados; §8 resultado; §9 testes/aceite.
++**Files:** criar scripts/phase1/recover_p08.py, scripts/phase1/inaturalist_source.py, scripts/phase1/test_recover_p08.py, scripts/phase1/test_inaturalist_source.py, scripts/phase1/test_p08_mutation.py, docs/phase1/P08-recovery.md, artifacts/phase1/p08/summary.json e artifacts/bianchini/v2/ledgers/P08.md; atualizar somente campos P08 de docs/living/PROJECT_STATE.md no fechamento futuro. Ler funções puras acquire_commons.py/curate_p07.py, requirements-p06.txt, manifesto canônico/roster e evidências P07; esses arquivos históricos permanecem inalterados. Config, crosswalk, imagens, journal, decisões e atribuição somente no diretório externo autorizado por U-802.
++**Contract:** cumprir integralmente §§1–9 da spec. Após U-801 e autorização separada de implementação, construir extensão delimitada com stdlib/Pillow existente. RED deve comprovar que cada fronteira nova falha antes da implementação; GREEN cobre fixtures e replay. Não promover confiança comunitária a perícia, licença abreviada a autorização, título a taxon ID ou sanitização a privacidade. Commons+iNaturalist condicionais; demais fontes blocked, tetos 100 candidatos/20 transferências por fonte/classe, limites cumulativos de bytes/páginas/requisições. Preservar original servido e sanitizado por SHA, sem alegar original de câmera iNaturalist. Journal precede side effects e não reescreve eventos. A mesma entrega incorpora correção mínima do estado P07 publicado, já materializada documentalmente neste pacote.
++**Verification:** no cwd da worktree P08, usar Python persistente P07 3.14.4/Pillow12.3.0. Fast: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_recover_p08.py'` e o mesmo comando com `test_inaturalist_source.py`; esses dois arquivos são entregáveis futuros, não testes alegadamente existentes. Plan: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'`, incluindo harness seletivo test_p08_mutation.py criado na entrega; `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`; `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS`; `git diff --check`. Gate espera saída 0, todos contratos executados, zero sobrevivente material dos cinco desvios §9, não número arbitrário de testes. Ambiente ausente bloqueia, não instalar automaticamente. Rede real só após U-802/U-803 e contratos offline passed; verify futuro prova journal, hashes/P07 17/17, aceites e allowlist. Gate release histórico continua blocked e não será executado ou substituído por unittest.
++**Done when:** uma rodada autorizada contábil para as 14 classes, com esgotamento/limite/bloqueio por fonte explícito, originais/sanitizados/backup íntegros, P07 17/17 preservados, testes e revisão independente passed, parecer humano final por item incluindo pendências legítimas, atribuição completa e recibo U-804 do digest final. Falta de perito mantém pendências, podendo aceitar resultado zero; falta de autorização de execução/aceite ou falha de integridade impede completed. Zero aprovado e treinamento bloqueado são resultados válidos; nenhum mínimo de piloto, suficiência, split ou treino será criado.
++
++Sequência dentro da unidade: confirmar autorização/workspace/baseline; validar manifesto/crosswalk/config; produzir RED/GREEN do percurso completo fake; implementar transporte/journal/curadoria/exportação limitados; executar regressão/mutação seletiva/revisão; somente com U-802, autorizar efeitos externos em rodada limitada; inspecionar/reconciliar com P07; obter U-803 por item e preservar inconclusões; gerar relatórios/backup/manifesto de bytes; obter U-804 e encerrar documentalmente. Revisão humana de fonte/ID/licença é requisito antes do download quando necessário. Não inventar prova para ultrapassar essas pausas.
++
++A-801/A-802 limitam incerteza: fontes podem não fornecer candidatos elegíveis nem IDs/licenças suficientemente documentados. Fallback é fonte/item bloqueado e resultado vazio, sem expandir API/host/licença. P-801 impede aceite indevido; P-802 exige lock/durabilidade/hash/allowlist. U-801 autoriza somente pacote; U-802 ambiente e rede, U-803 qualificação/crosswalk/parecer, U-804 bytes finais. Sem staging, commit, push, merge/tag ou execução nesta sessão de planejamento. Sem autorização futura explícita dessas operações.
+diff --git a/artifacts/bianchini/v2/codex/P08/verification-final.json b/artifacts/bianchini/v2/codex/P08/verification-final.json
+new file mode 100644
+index 0000000..4a169b6
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/verification-final.json
+@@ -0,0 +1,71 @@
++{
++  "code_sha256": {
++    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
++    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
++    "scripts/phase1/recover_p08.py": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
++    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
++    "scripts/phase1/test_recover_p08.py": "d136edc1d7d9b1a9d455d9b631cea9447d581bf0d8b5c7ad8a9cc003ab842926",
++    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed",
++    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
++    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5",
++    "scripts/phase1/test_acquire_commons.py": "3d7781ef2e70f9ee57331cff72848ac3b61be3c9ec33f627ae8c8b4fb01d622e",
++    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
++    "scripts/phase1/acquire_commons.py": "ddd2bf5d5f6c7e75fe090af8fd0313a9785fefccb30ee3a62b070a48f0ba6046"
++  },
++  "commands": [
++    {
++      "name": "focal-recovery-final",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "-m",
++        "unittest",
++        "discover",
++        "-s",
++        "scripts/phase1",
++        "-p",
++        "test_recover_p08.py"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:22:22.372156+00:00",
++      "exit_code": 0,
++      "output_sha256": "2685ccaab15660c44c951beb8fe9c19d6d9e9e347b91699628320b87c86b058f"
++    },
++    {
++      "name": "focal-inat-final",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "-m",
++        "unittest",
++        "discover",
++        "-s",
++        "scripts/phase1",
++        "-p",
++        "test_inaturalist_source.py"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:22:25.531434+00:00",
++      "exit_code": 0,
++      "output_sha256": "2fdf7a432a53fceb691486981be60fcb65192fbaa6b7627e6b3fe3a0c95917bf"
++    },
++    {
++      "name": "full-suite-final",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "-m",
++        "unittest",
++        "discover",
++        "-s",
++        "scripts/phase1",
++        "-p",
++        "test_*.py"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:22:25.638852+00:00",
++      "exit_code": 0,
++      "output_sha256": "ed24024f0c3d1b17f96cc32552dd6391462ca11089c74f599305c51d7ec0a660"
++    }
++  ]
++}
+diff --git a/artifacts/bianchini/v2/codex/P08/verification.json b/artifacts/bianchini/v2/codex/P08/verification.json
+new file mode 100644
+index 0000000..ac0181c
+--- /dev/null
++++ b/artifacts/bianchini/v2/codex/P08/verification.json
+@@ -0,0 +1,82 @@
++{
++  "code_sha256": {
++    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
++    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
++    "scripts/phase1/recover_p08.py": "14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57",
++    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
++    "scripts/phase1/test_recover_p08.py": "f8597b8a8906eb6c4db0b7a20d6a5c3fd579988355e62860fc16c195e93bad96",
++    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed",
++    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
++    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5",
++    "scripts/phase1/test_acquire_commons.py": "3d7781ef2e70f9ee57331cff72848ac3b61be3c9ec33f627ae8c8b4fb01d622e",
++    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
++    "scripts/phase1/acquire_commons.py": "ddd2bf5d5f6c7e75fe090af8fd0313a9785fefccb30ee3a62b070a48f0ba6046"
++  },
++  "commands": [
++    {
++      "name": "focal-inat",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "-m",
++        "unittest",
++        "discover",
++        "-s",
++        "scripts/phase1",
++        "-p",
++        "test_inaturalist_source.py"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:14:43.510828+00:00",
++      "exit_code": 0,
++      "output_sha256": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0"
++    },
++    {
++      "name": "full-suite",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "-m",
++        "unittest",
++        "discover",
++        "-s",
++        "scripts/phase1",
++        "-p",
++        "test_*.py"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:14:43.619197+00:00",
++      "exit_code": 0,
++      "output_sha256": "3d6689642da34d73791790f53db3d6b989e16eabbd850972ccfaa176e92b2db0"
++    },
++    {
++      "name": "manifest",
++      "argv": [
++        "$P08_PY",
++        "-B",
++        "scripts/phase1/validate_offline_manifest.py",
++        "--manifest",
++        "docs/phase1/offline-class-manifest.v1.json",
++        "--roster",
++        "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:14:53.986164+00:00",
++      "exit_code": 0,
++      "output_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe"
++    },
++    {
++      "name": "roster-hashes",
++      "argv": [
++        "sha256sum",
++        "-c",
++        "--strict",
++        "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS"
++      ],
++      "cwd": ".",
++      "started_at": "2026-10-05T22:14:54.074770+00:00",
++      "exit_code": 0,
++      "output_sha256": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3"
++    }
++  ]
++}
+diff --git a/artifacts/bianchini/v2/ledgers/P08.md b/artifacts/bianchini/v2/ledgers/P08.md
+new file mode 100644
+index 0000000..cd17c62
+--- /dev/null
++++ b/artifacts/bianchini/v2/ledgers/P08.md
+@@ -0,0 +1,22 @@
++# P08 execution ledger
++
++- Approved package: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`.
++- Base revision: `24de252d27a137281c02cad50533280bb82dd80d`; P07 base `b6844f9129d9edf862ae7958d8f043d9bdd5bd84`.
++- Workspace: `/tmp/scanplant-p08-execution`; branch `bm/v2-p08`.
++- Method installation: active .agents, version 3.2.0, v2-standalone.
++- Profile standard; technical mode strict/per_task, data-transform, one unit `1`; authorized grouped operational round.
++- Explicit current user authorization supersedes historical planning-only scope, grants implementation and bounded collection, prohibits staging/commit/push/release.
++- Preflight: root/branch/HEAD/upstream/remote, clean index/tree, only three known starting worktrees, snapshot and manifest, strict planning audit and hygiene passed. P07/guard completed, usable=0; P08 approved/unstarted, release pending, P09 absent. Python 3.14.4/Pillow 12.3.0 available.
++- P06: 29 files, SHA256SUMS passed; 17/17 image hashes match P07 closure. All seven final external P07 hashes match. No historical mutation.
++- `bm change-policy --file-location`: bounded_amendment; evidence artifacts and temporary execution workspace location recorded, approved plan immutable.
++- RED: recovery-red.txt and inat-red.txt record missing-module failures before implementation. GREEN initial focal runs passed.
++- Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.
++- Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.
++- Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint.
++
++- Continuation recovered the exact checkpoint digest and eleven untracked files; existing workspace reused, baseline HEAD unchanged, no upstream.
++- Final continuation evidence: artifacts/bianchini/v2/codex/P08/continuation-report.md and verification-final.json. 51 recovery + 15 adapter focal tests; 233 full historical/affected tests; five selective mutations killed, zero survivors.
++- Real Commons round: 120 successful metadata requests, 1090 class associations/1088 unique candidates, all pending, no media transfer. iNaturalist no_crosswalk, zero requests. P07 17/17 bytes and mtimes preserved.
++- Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.
++- External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.
++- Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending.
+diff --git a/artifacts/phase1/p08/summary.json b/artifacts/phase1/p08/summary.json
+new file mode 100644
+index 0000000..caad1c6
+--- /dev/null
++++ b/artifacts/phase1/p08/summary.json
+@@ -0,0 +1 @@
++{"counts":{"needs_botanical_review":1,"needs_license_review":1087},"coverage":[{"approved":0,"candidate_cap":100,"class_id":"species_01","expert_validated":0,"found":91,"license_valid":0,"pending":91,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_01","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_02","expert_validated":0,"found":96,"license_valid":0,"pending":96,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_02","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_03","expert_validated":0,"found":98,"license_valid":0,"pending":98,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_03","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_04","expert_validated":0,"found":92,"license_valid":0,"pending":92,"rejected":0,"source":"commons","status":"exhausted_within_query","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_04","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_05","expert_validated":0,"found":82,"license_valid":0,"pending":82,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_05","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_06","expert_validated":0,"found":86,"license_valid":0,"pending":86,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_06","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_07","expert_validated":0,"found":96,"license_valid":0,"pending":96,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_07","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_08","expert_validated":0,"found":88,"license_valid":0,"pending":88,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_08","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_09","expert_validated":0,"found":70,"license_valid":0,"pending":70,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_09","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_10","expert_validated":0,"found":95,"license_valid":0,"pending":95,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_10","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_11","expert_validated":0,"found":98,"license_valid":0,"pending":98,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_11","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_12","expert_validated":0,"found":98,"license_valid":0,"pending":98,"rejected":0,"source":"commons","status":"budget_reached","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":100,"class_id":"species_12","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"no_crosswalk","technical_integrity":0,"transfer_cap":20,"transferred":0},{"approved":0,"candidate_cap":0,"class_id":"outra_planta","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"commons","status":"protection_not_queried","technical_integrity":0,"transfer_cap":0,"transferred":0},{"approved":0,"candidate_cap":0,"class_id":"outra_planta","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"protection_not_queried","technical_integrity":0,"transfer_cap":0,"transferred":0},{"approved":0,"candidate_cap":0,"class_id":"imagem_invalida","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"commons","status":"protection_not_queried","technical_integrity":0,"transfer_cap":0,"transferred":0},{"approved":0,"candidate_cap":0,"class_id":"imagem_invalida","expert_validated":0,"found":0,"license_valid":0,"pending":0,"rejected":0,"source":"inaturalist","status":"protection_not_queried","technical_integrity":0,"transfer_cap":0,"transferred":0}],"minimum_experimental_pilot":null,"partition_authorized":false,"production_sufficiency":"not_demonstrated","schema_version":1,"scientific_sufficiency":"not_demonstrated","stage":"pending_human_acceptance","training_authorized":false,"training_status":"blocked","unique_objects":1088,"usable":0}
+diff --git a/docs/phase1/P08-recovery.md b/docs/phase1/P08-recovery.md
+new file mode 100644
+index 0000000..943869b
+--- /dev/null
++++ b/docs/phase1/P08-recovery.md
+@@ -0,0 +1,35 @@
++# P08 — recuperação limitada
++
++A rodada permanece `pending_human_acceptance`, com `usable=0`. P06/P07 são entradas somente de leitura; nenhuma partição, treino, publicação ou release é autorizada. O plano aprovado permanece congelado.
++
++## Operação
++
++Usar o ambiente Python 3.14.4/Pillow 12.3.0 já aprovado. Definir `P08_PY`, `P08_ROOT` e `P07_SOURCE` para os caminhos privados do recibo externo; nunca versionar dados, configuração privada, decisões, imagens ou HTML.
++
++```bash
++"$P08_PY" -B scripts/phase1/recover_p08.py acquire --config "$P08_ROOT/config.json" --output "$P08_ROOT"
++"$P08_PY" -B scripts/phase1/recover_p08.py inspect --output "$P08_ROOT" --p07-source "$P07_SOURCE"
++"$P08_PY" -B scripts/phase1/recover_p08.py verify --output "$P08_ROOT" --p07-source "$P07_SOURCE"
++```
++
++O arquivo de configuração é imutável por fingerprint. A primeira configuração é produzida pela função `default_config()` e arquivada pelo journal. `acquire` retoma páginas duráveis; uma repetição sem trabalho pendente não baixa nem reescreve arquivos. Código 0 representa rodada limitada contabilizada; 1 indica fonte indisponível; 2 indica configuração, schema, hash ou IO inválido. Esses códigos não representam aceite humano.
++
++`finalize --decisions` só consome pareceres humanos reais. `verify --acceptance` exige recibo humano vinculado ao SHA-256 do manifesto final e à cobertura exata dos arquivos, excluindo o próprio recibo. Não executar esses modos com decisões preenchidas pelo agente.
++
++## Autoridade e fontes
++
++Commons consulta apenas nomes científicos canônicos. A rodada atual permite descoberta de metadados e mantém o exame de direitos adicional pendente; nenhum campo `passed` de aprovação jurídica foi inventado. Licença individual, autoria, URL legal, proveniência e direitos adicionais são gates separados. iNaturalist permanece `no_crosswalk`: não houve consulta, ID inventado ou transferência. Seu adaptador continua coberto por testes sintéticos.
++
++Sem prova de direitos, o candidato fica `needs_license_review`, sem original nem sanitizado. Hashes ausentes têm motivo explícito no pacote privado. Proteções permanecem vazias e sem consultas. Zero utilizável e classes vazias não demonstram suficiência para treinamento.
++
++## Integridade e revisão
++
++Journal canônico encadeado por SHA-256, intenção e reservas antes de rede, lock exclusivo, quotas cumulativas e persistência com fsync protegem a retomada. Corrupção/linha truncada bloqueia; não reparar ou truncar automaticamente. Originais e sanitizados são objetos separados e imutáveis. Comparação de hashes/dHash com as 17 imagens P07 é obrigatória; sinais perceptuais não constituem decisão humana.
++
++O pacote externo `human-review.json` / `human-review.html` reúne IDs, fonte, autoria/licença/atribuição declaradas, hashes ou razão de ausência, classes propostas, taxonomia, qualidade, privacidade, duplicidade, recomendação técnica e decisões pendentes. Nenhuma imagem é aprovada por título, research grade ou ausência de EXIF.
++
++## Verificação e limites de conclusão
++
++Evidências desta continuação estão em `artifacts/bianchini/v2/codex/P08/`: inventário recuperado, RED recuperado, regressão, mutação seletiva e relatório de continuação. O checkpoint original permanece intacto.
++
++O guard opera commits e cria checkout isolado para `proof`. Esta rodada proíbe novos commits e worktrees; não se representa código untracked como prova do HEAD. Sem sidecar P08, sem `freeze` ou `complete` fictício. As provas locais estão vinculadas aos hashes dos arquivos. Aceite humano dos candidatos e bytes finais, conclusão formal do guard e autorização de staging/commit/push permanecem pendentes.
+diff --git a/scripts/phase1/inaturalist_source.py b/scripts/phase1/inaturalist_source.py
+new file mode 100644
+index 0000000..7883e5a
+--- /dev/null
++++ b/scripts/phase1/inaturalist_source.py
+@@ -0,0 +1,259 @@
++"""Pure iNaturalist v1 adapter for P08; transport and persistence are caller-owned.
++
++Official schema inspected 2026-10-05:
++https://github.com/inaturalist/iNaturalistAPI/blob/main/lib/views/swagger_v1.yml.ejs
++It documents Photo(id, attribution, license_code, url), observations.photos,
++and size variants sharing an extension. A provider original is at most 2048px;
++it is never asserted to be a camera original. No API code proves a CC version.
++
++build_query accepts one reviewed crosswalk entry and one canonical manifest
++class. parse_page returns at most 100 unique photos, counts deferred/duplicates,
++and a *proposed* next cursor; the caller persists that cursor only after all
++items are durably consumed/deferred. It never performs IO or makes approvals.
++photo_record accepts separate human evidence for photo and observation rights;
++without that evidence its download URL is null. All records are PRIVATE data.
++"""
++from datetime import datetime, timezone
++import hashlib
++import re
++from urllib.parse import urlsplit
++
++
++class ContractError(ValueError):
++    """An input cannot satisfy the frozen source contract."""
++
++
++API_URL = "https://api.inaturalist.org/v1/observations"
++SCHEMA_URL = "https://github.com/inaturalist/iNaturalistAPI/blob/main/lib/views/swagger_v1.yml.ejs"
++MEDIA_HOST = "inaturalist-open-data.s3.amazonaws.com"
++LICENSES = {
++    "cc-by": ("4.0", "https://creativecommons.org/licenses/by/4.0/"),
++    "cc0": ("1.0", "https://creativecommons.org/publicdomain/zero/1.0/"),
++}
++
++
++def _text(value):
++    return isinstance(value, str) and bool(value.strip())
++
++
++def _integer(value, minimum=1):
++    return type(value) is int and value >= minimum
++
++
++def _hash(value):
++    return isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) is not None
++
++
++def _date(value):
++    try:
++        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
++        if stamp.tzinfo is None:
++            raise ValueError
++        return stamp.astimezone(timezone.utc)
++    except (ValueError, TypeError, AttributeError) as exc:
++        raise ContractError("invalid_timestamp") from exc
++
++
++def _source_url(value, entity, identifier):
++    return value == f"https://www.inaturalist.org/{entity}/{identifier}"
++
++
++def validate_crosswalk(crosswalk, class_item):
++    """Reject unmapped/protection/alias taxa before any observation request.
++
++    Evidence and reviewer identify the external human-reviewed document;
++    integrity of that document against evidence.sha256 is caller-owned.
++    """
++    if not isinstance(class_item, dict) or class_item.get("kind") != "species":
++        raise ContractError("protection_not_queried")
++    if not isinstance(crosswalk, dict):
++        raise ContractError("no_crosswalk")
++    expected = {"class_id": class_item.get("class_id"), "source": "inaturalist",
++                "namespace": "inaturalist", "scientific_name": class_item.get("scientific_name"),
++                "rank": "species", "status": "active", "synonym_of": None}
++    if any(key not in crosswalk or crosswalk[key] != value for key, value in expected.items()):
++        raise ContractError("crosswalk_identity_conflict")
++    if not _text(expected["scientific_name"]) or not _integer(crosswalk.get("source_taxon_id")):
++        raise ContractError("crosswalk_taxon_missing")
++    if "authorship" not in crosswalk or (not _text(crosswalk["authorship"]) and not (
++            crosswalk["authorship"] is None and _text(crosswalk.get("authorship_missing_reason")))):
++        raise ContractError("crosswalk_authorship_missing")
++    refs = class_item.get("taxonomy_ref_ids")
++    if not refs or crosswalk.get("taxonomy_ref_ids") != refs:
++        raise ContractError("crosswalk_reference_conflict")
++    evidence = crosswalk.get("evidence", {})
++    reviewer = crosswalk.get("reviewer", {})
++    if not isinstance(evidence, dict) or not isinstance(reviewer, dict):
++        raise ContractError("crosswalk_review_missing")
++    if (not _source_url(evidence.get("url"), "taxa", crosswalk["source_taxon_id"])
++            or not _hash(evidence.get("sha256")) or not _text(evidence.get("version"))):
++        raise ContractError("crosswalk_evidence_missing")
++    try:
++        datetime.strptime(evidence.get("date", ""), "%Y-%m-%d")
++    except (TypeError, ValueError) as exc:
++        raise ContractError("crosswalk_evidence_date_missing") from exc
++    if any(not _text(reviewer.get(key)) for key in ("id", "qualification")) or reviewer.get("decision") != "approved":
++        raise ContractError("crosswalk_review_missing")
++    return crosswalk
++
++
++def build_query(crosswalk, class_item, cutoff, id_above=0):
++    """Return official query parameters, never a request or guessed taxon ID.
++
++    created_d2 has date granularity in v1. parse_page separately enforces the
++    exact timestamp cutoff, so later observations cannot enter this round.
++    """
++    entry = validate_crosswalk(crosswalk, class_item)
++    stamp = _date(cutoff)
++    if not _integer(id_above, 0):
++        raise ContractError("invalid_cursor")
++    return {"taxon_id": entry["source_taxon_id"], "photos": "true",
++            "quality_grade": "research", "order_by": "id", "order": "asc",
++            "per_page": 100, "id_above": id_above, "created_d2": stamp.date().isoformat()}
++
++
++def _original_url(photo):
++    value = photo.get("url")
++    if not _text(value):
++        return None
++    try:
++        parsed = urlsplit(value)
++        if (parsed.scheme != "https" or parsed.hostname != MEDIA_HOST or
++                parsed.username is not None or parsed.password is not None or
++                parsed.port not in (None, 443) or parsed.fragment):
++            return None
++    except ValueError:
++        return None
++    # Entire path, ID and extension must match the documented provider scheme.
++    match = re.fullmatch(r"/photos/([1-9][0-9]*)/(?:square|thumb|small|medium|large|original)\.(jpg|jpeg|png)", parsed.path)
++    if not match or int(match.group(1)) != photo["id"]:
++        return None
++    if parsed.query and re.fullmatch(r"[0-9]+", parsed.query) is None:
++        return None
++    return f"https://{MEDIA_HOST}/photos/{photo['id']}/original.{match.group(2)}"
++
++
++def _rights(proof, code, entity, identifier):
++    if not isinstance(proof, dict) or not isinstance(code, str) or code not in LICENSES:
++        return False
++    version, url = LICENSES[code]
++    return (proof.get("license_code") == code and proof.get("version") == version
++            and proof.get("legal_url") == url and _hash(proof.get("evidence_sha256"))
++            and _source_url(proof.get("source_url"), entity, identifier)
++            and proof.get("restrictions") == [])
++
++
++def photo_record(photo, observation, legal_evidence=None):
++    """Normalize a photo without conflating photo, observation and DB rights.
++
++    legal_evidence schema is exemplified in the synthetic contract tests. Both
++    entities need a canonical individual legal URL, version, evidence SHA256,
++    no extra restrictions, and a human-approved ID-bound attribution record.
++    """
++    if not isinstance(photo, dict) or not isinstance(observation, dict):
++        raise ContractError("invalid_photo_schema")
++    if not _integer(photo.get("id")) or not _integer(observation.get("id")):
++        raise ContractError("invalid_source_id")
++    reasons = []
++    proof = legal_evidence if isinstance(legal_evidence, dict) else {}
++    identity_ok = (proof.get("photo_id") == photo["id"] and proof.get("observation_id") == observation["id"]
++                   and proof.get("decision") == "approved"
++                   and all(_text(proof.get(key)) for key in ("reviewer", "author", "licensor", "credit")))
++    try:
++        _date(proof.get("reviewed_at"))
++    except ContractError:
++        identity_ok = False
++    photo_rights = _rights(proof.get("photo"), photo.get("license_code"), "photos", photo["id"])
++    observation_rights = _rights(proof.get("observation"), observation.get("license_code"), "observations", observation["id"])
++    database_rights = proof.get("database_rights") == "compatible"
++    attribution = photo.get("attribution")
++    if not (identity_ok and photo_rights and observation_rights and database_rights and _text(attribution)):
++        reasons.append("needs_license_review")
++    if not observation_rights:
++        reasons.append("observation_rights_unresolved")
++    if not database_rights:
++        reasons.append("database_rights_unresolved")
++    original_url = _original_url(photo)
++    if not original_url:
++        reasons.append("unproven_original_url")
++    media_id = str(photo["id"])
++    return {"source": "inaturalist", "media_id": media_id, "photo_id": photo["id"],
++            "candidate_id": hashlib.sha256(f"inaturalist:{media_id}".encode()).hexdigest(),
++            "observation_id": observation["id"], "license_code": photo.get("license_code"),
++            "observation_license_code": observation.get("license_code"), "credit": attribution,
++            "author": proof.get("author") if identity_ok else None,
++            "licensor": proof.get("licensor") if identity_ok else None,
++            "license_version": proof.get("photo", {}).get("version") if photo_rights else None,
++            "legal_url": proof.get("photo", {}).get("legal_url") if photo_rights else None,
++            "license_evidence_sha256": proof.get("photo", {}).get("evidence_sha256") if photo_rights else None,
++            "observation_license_version": proof.get("observation", {}).get("version") if observation_rights else None,
++            "observation_legal_url": proof.get("observation", {}).get("legal_url") if observation_rights else None,
++            "observation_license_evidence_sha256": proof.get("observation", {}).get("evidence_sha256") if observation_rights else None,
++            "rights_reviewer": proof.get("reviewer") if identity_ok else None,
++            "rights_reviewed_at": proof.get("reviewed_at") if identity_ok else None,
++            "source_page_url": f"https://www.inaturalist.org/photos/{photo['id']}",
++            "observation_page_url": f"https://www.inaturalist.org/observations/{observation['id']}",
++            "file_url": original_url if not reasons else None,
++            "download_allowed": not reasons, "reasons": reasons,
++            "state": "discovered" if not reasons else "needs_license_review",
++            "origin_fidelity": "provider_original", "camera_original_verified": False,
++            "original_url_contract": SCHEMA_URL,
++            "photo_rights_passed": bool(identity_ok and photo_rights),
++            "observation_rights_passed": bool(identity_ok and observation_rights),
++            "database_rights_passed": bool(identity_ok and database_rights)}
++
++
++def parse_page(response, crosswalk, class_item, cutoff, id_above=0):
++    """Parse one page, preserving taxonomic conflicts as pending candidates.
++
++    No raw observations/coordinates are copied. API total_results is metadata,
++    not an examined-count claim. A next cursor is only a suggestion for the
++    durable checkpoint owned by the orchestrator. Duplicate photos do not
++    inflate counts; the photo budget applies to entries examined as well.
++    """
++    build_query(crosswalk, class_item, cutoff, id_above)
++    if not isinstance(response, dict):
++        raise ContractError("invalid_page_schema")
++    rows = response.get("results")
++    if (not isinstance(rows, list) or len(rows) > 100 or type(response.get("page")) is not int or response["page"] != 1
++            or type(response.get("per_page")) is not int or response["per_page"] != 100 or not _integer(response.get("total_results"), 0)
++            or response["total_results"] < len(rows)):
++        raise ContractError("invalid_page_schema")
++    result = {"candidates": [], "deferred_photo_count": 0, "duplicate_photo_count": 0,
++              "next_id_above": id_above, "total_results": response["total_results"], "examined_photo_count": 0}
++    seen = set()
++    last = id_above
++    for observation in rows:
++        if not isinstance(observation, dict) or not _integer(observation.get("id")) or observation["id"] <= last:
++            raise ContractError("regressive_observation_page")
++        last = observation["id"]
++        if _date(observation.get("created_at")) > _date(cutoff):
++            raise ContractError("observation_after_cutoff")
++        photos = observation.get("photos")
++        if not isinstance(photos, list) or not photos or observation.get("quality_grade") != "research":
++            raise ContractError("invalid_observation_schema")
++        taxon = observation.get("taxon")
++        if not isinstance(taxon, dict):
++            raise ContractError("invalid_taxon_schema")
++        exact = (taxon.get("id") == crosswalk["source_taxon_id"] and taxon.get("name") == crosswalk["scientific_name"]
++                 and taxon.get("rank") == "species" and taxon.get("is_active") is True)
++        for photo in photos:
++            if result["examined_photo_count"] >= 100:
++                result["deferred_photo_count"] += 1
++                continue
++            result["examined_photo_count"] += 1
++            candidate = photo_record(photo, observation)
++            if candidate["photo_id"] in seen:
++                result["duplicate_photo_count"] += 1
++                continue
++            seen.add(candidate["photo_id"])
++            candidate.update({"class_id": class_item["class_id"], "source_taxon_id": taxon.get("id"),
++                              "scientific_name": taxon.get("name"), "namespace": "inaturalist",
++                              "taxonomic_confidence": "source_supported" if exact else "conflict"})
++            if not exact:
++                candidate["reasons"].append("needs_taxonomic_mapping")
++                candidate["download_allowed"] = False
++                candidate["file_url"] = None
++            result["candidates"].append(candidate)
++    result["next_id_above"] = last
++    return result
+diff --git a/scripts/phase1/recover_p08.py b/scripts/phase1/recover_p08.py
+new file mode 100644
+index 0000000..3def6c1
+--- /dev/null
++++ b/scripts/phase1/recover_p08.py
+@@ -0,0 +1,737 @@
++"""P08 bounded recovery. Private datasets, append-only journal, explicit human gates.
++
++No training or automatic botanical/privacy approval. P06/P07 are read-only inputs.
++"""
++import argparse
++from collections import Counter
++from datetime import datetime, timezone
++from email.utils import parsedate_to_datetime
++import fcntl
++import hashlib
++from html import escape
++import http.client
++from io import BytesIO
++import ipaddress
++import json
++import os
++from pathlib import Path
++import re
++import shutil
++import socket
++import ssl
++import stat
++import sys
++import time
++from urllib.parse import urlencode, urlsplit, unquote, urljoin
++import PIL
++from PIL import Image
++import acquire_commons as commons
++import inaturalist_source as inat
++from curate_p07 import dhash, flags_for, laplacian_variance
++from validate_offline_manifest import validate_manifest
++
++ROOT = Path(__file__).resolve().parents[2]
++MANIFEST = ROOT/'docs/phase1/offline-class-manifest.v1.json'
++ROSTER = ROOT/'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'
++MAX_BYTES = 20*1024*1024
++SOURCES = ('commons','inaturalist')
++RETRYABLE={'timeout','network_error','response_timeout','http_429','http_500','http_502','http_503','http_504','maxlag','resume_after'}
++STATES = {'discovered','needs_license_review','needs_taxonomic_mapping','deferred_budget','transfer_failed',
++          'quarantined','needs_human_review','needs_privacy_review','needs_botanical_review','needs_duplicate_review',
++          'rejected_license','rejected_format','rejected_quality','rejected_privacy','rejected_label',
++          'rejected_duplicate','approved_for_dataset'}
++LIMITS = {'candidates':100,'transfers':20,'pages':10,'requests':1000,'media_bytes':1024**3,
++          'hour_bytes':256*1024**2,'storage_bytes':2*1024**3,'file_bytes':MAX_BYTES,'wait_seconds':60}
++SHA = re.compile(r'[a-f0-9]{64}')
++# Exact predecessor from the verified real round. The only behavior change is
++# deterministic key ordering in review HTML; config and acquisition stay frozen.
++HTML_ORDER_PREDECESSOR = '14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57'
++
++class RecoveryError(ValueError): pass
++
++def require(condition,code):
++    if not condition: raise RecoveryError(code)
++
++def sha(raw): return hashlib.sha256(raw).hexdigest()
++def encode(value): return (json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
++def now(): return datetime.now(timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
++def load(raw):
++    def pairs(items):
++        d={}
++        for k,v in items:
++            require(k not in d,'duplicate_json_key');d[k]=v
++        return d
++    try: return json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(RecoveryError('nonfinite_json')))
++    except (UnicodeError,ValueError,TypeError): raise RecoveryError('invalid_json') from None
++
++def safe_path(path):
++    p=Path(os.path.abspath(path))
++    require(not any(q.is_symlink() for q in (p,*p.parents)),'symlink')
++    return p
++
++def read(path):
++    p=safe_path(path)
++    with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
++        require(stat.S_ISREG(os.fstat(f.fileno()).st_mode),'not_regular')
++        return f.read()
++
++def fsync_dir(path):
++    fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
++    try: os.fsync(fd)
++    finally: os.close(fd)
++
++def persist(path,raw,immutable=False):
++    path=safe_path(path)
++    if path.exists():
++        old=read(path)
++        if old==raw:return
++        require(not immutable,'immutable_hash_mismatch')
++    part=path.with_name('.'+path.name+'.'+os.urandom(8).hex()+'.part')
++    fd=os.open(part,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
++    with os.fdopen(fd,'wb') as f: f.write(raw);f.flush();os.fsync(f.fileno())
++    if immutable:
++        try: os.link(part,path,follow_symlinks=False)
++        except FileExistsError: require(read(path)==raw,'immutable_hash_mismatch')
++        part.unlink()
++    else: os.replace(part,path)
++    fsync_dir(path.parent)
++
++def tree_fingerprint(root):
++    return {str(p.relative_to(root)):{'sha256':sha(read(p)),'mtime_ns':p.stat().st_mtime_ns}
++            for p in sorted(Path(root).rglob('*')) if p.is_file()}
++
++def fingerprint():
++    return {p.name:sha(read(p)) for p in [Path(__file__),ROOT/'scripts/phase1/inaturalist_source.py',
++                                        ROOT/'scripts/phase1/acquire_commons.py',ROOT/'scripts/phase1/curate_p07.py'] if p.exists()}
++
++def canonical():
++    m=load(read(MANIFEST)); validate_manifest(m,read(ROSTER))
++    # The historic validator raises on contract violations and returns diagnostics.
++    require(m['manifest_version']=='1.1.0' and len(m['classes'])==14,'canonical_manifest')
++    return m['classes']
++
++def default_config(offline=False):
++    return {'schema_version':1,'run_id':'p08-recovery','manifest_sha256':sha(read(MANIFEST)),
++            'code_sha256':fingerprint(),'python':'.'.join(map(str,sys.version_info[:3])),
++            'pillow':PIL.__version__,'offline':offline,'cutoff':now(),'limits':dict(LIMITS),
++            'sources':list(SOURCES),'crosswalk':{},'legal_evidence':{},'source_contracts':{},
++            'user_agent':'ScanPlant-P08/1.0 (https://github.com/Parys-boop/ScanPlant; dataset-recovery)'}
++
++def validate_config(c,offline):
++    require(set(c)==set(default_config(offline)),'config_fields')
++    require(c['schema_version']==1 and c['offline'] is offline,'config_mode')
++    current=fingerprint();previous={**current,'recover_p08.py':HTML_ORDER_PREDECESSOR}
++    require(c['manifest_sha256']==sha(read(MANIFEST)) and c['code_sha256'] in (current,previous),'config_fingerprint')
++    require(c['python']=='.'.join(map(str,sys.version_info[:3])) and c['pillow']==PIL.__version__=='12.3.0','environment')
++    require(c['sources']==list(SOURCES) and set(c['limits'])==set(LIMITS),'sources_limits')
++    for k,v in c['limits'].items():require(type(v)is int and 0<v<=LIMITS[k],'limit')
++    require(isinstance(c['crosswalk'],dict) and isinstance(c['source_contracts'],dict),'config_schema')
++    require(c['user_agent'].startswith('ScanPlant-P08/') and 'https://github.com/Parys-boop/ScanPlant' in c['user_agent'],'user_agent')
++    require(datetime.fromisoformat(c['cutoff'].replace('Z','+00:00')).tzinfo is not None,'cutoff')
++    canonical()
++
++def safe_url(url,source,media=False):
++    require(isinstance(url,str) and not any(ord(c)<33 for c in url),'unsafe_url')
++    p=urlsplit(url); host=({'commons':'upload.wikimedia.org','inaturalist':'inaturalist-open-data.s3.amazonaws.com'} if media else
++                         {'commons':'commons.wikimedia.org','inaturalist':'api.inaturalist.org'})[source]
++    require(p.scheme=='https' and p.netloc==host and not p.fragment and not p.username and not p.password,'unsafe_url')
++    path=unquote(unquote(p.path));require('\\' not in path and '..' not in path.split('/') and path.startswith('/'),'unsafe_path')
++    if not media:require(p.path==('/w/api.php' if source=='commons' else '/v1/observations'),'unsafe_endpoint')
++    else:
++        require(not p.query and Path(path).suffix.lower() in {'.jpg','.jpeg','.png'},'unsafe_media')
++        if source=='inaturalist':require(re.fullmatch(r'/photos/[1-9][0-9]*/original\.(jpg|jpeg|png)',path),'unsafe_media')
++    return url
++
++def public_addresses(host):
++    addresses=list(dict.fromkeys(row[4][0] for row in socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)))
++    require(bool(addresses) and all(ipaddress.ip_address(a).is_global for a in addresses),'nonpublic_address')
++    return addresses
++
++def candidate_id(c): return 'C'+sha((c['source']+':'+str(c['media_id'])).encode())[:24]
++
++def rights(c):
++    allowed={'cc-by-4.0':({'CC BY 4.0'},'https://creativecommons.org/licenses/by/4.0/'),
++             'cc0':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/'),
++             'cc-zero':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/')}
++    rule=allowed.get(c.get('license_id'))
++    if not rule or c.get('license_name') not in rule[0] or c.get('license_url')!=rule[1]:return 'needs_license_review'
++    if not c.get('author') or re.search(r'\b(unknown|anonymous|desconhecid[oa])\b',c['author'],re.I):return 'needs_license_review'
++    if c.get('restrictions') or c.get('rights_consistent') is not True or c.get('database_rights')!='passed':return 'needs_license_review'
++    if not isinstance(c.get('evidence_sha256'),str) or not SHA.fullmatch(c['evidence_sha256']):return 'needs_license_review'
++    return 'passed'
++
++def sanitize(raw,url,mime):
++    try:
++        clean,suffix=commons.sanitize_image(raw,url,mime)
++        with Image.open(BytesIO(clean)) as im:
++            im.load();require(not im.getexif() and not(set(im.info)&{'exif','xmp','XML:com.adobe.xmp','comment','icc_profile','text'}),'sanitization_metadata')
++        return clean,suffix
++    except commons.AcquisitionError:raise RecoveryError('invalid_image') from None
++
++def technical(raw):
++    with Image.open(BytesIO(raw)) as im:
++        im.load();w,h=im.size;px=list(im.convert('L').resize((256,256),Image.Resampling.LANCZOS).get_flattened_data())
++        mean=sum(px)/len(px);dark=sum(x<=15 for x in px)/len(px);bright=sum(x>=240 for x in px)/len(px)
++        var=laplacian_variance(px,256,256)
++        return {'decode':'ok','width':w,'height':h,'format':im.format,'dhash64':dhash(im),'mean_luminance':mean,
++                'dark_fraction':dark,'bright_fraction':bright,'laplacian_variance':var,'flags':flags_for(w,h,mean,dark,bright,var)}
++
++def review_digest(c):return sha(encode({k:v for k,v in c.items() if k not in {'state','decision'}}))
++
++def decide(c,d):
++    require(d.get('authority')=='human' and d.get('reviewer') and d.get('reviewed_at') and d.get('rationale'),'human_authority')
++    require(all(d.get(k)==c.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256']),'decision_hash')
++    require(d.get('evidence_digest')==review_digest(c),'stale_decision')
++    if rights(c)!='passed':return 'needs_license_review'
++    if not c.get('original_sha256') or not c.get('sanitized_sha256') or c.get('technical',{}).get('decode')!='ok':return 'rejected_format'
++    for key,state in [('quality','rejected_quality'),('privacy','rejected_privacy'),('botanical','rejected_label'),('duplicates','rejected_duplicate')]:
++        if d.get(key)=='rejected':return state
++    for key,state in [('quality','needs_human_review'),('privacy','needs_privacy_review'),('botanical','needs_botanical_review'),('duplicates','needs_duplicate_review')]:
++        if d.get(key)!='passed':return state
++    if not (d.get('expert_confirmation') is True and d.get('qualification') and d.get('botanical_evidence') and
++            isinstance(d.get('mapping'),dict) and d['mapping'].get('confidence')=='human_validated' and
++            d['mapping'].get('source_taxon_id') and d['mapping'].get('evidence_sha256')):return 'needs_botanical_review'
++    if len(c['class_ids'])!=1:return 'needs_botanical_review'
++    cls=next(x for x in canonical() if x['class_id']==c['class_ids'][0]);mapping=d['mapping']
++    if any(mapping.get(k)!=v for k,v in {'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],
++                                        'rank':'species','status':'accepted','taxonomy_ref_ids':cls['taxonomy_ref_ids']}.items()):return 'needs_botanical_review'
++    if not mapping.get('namespace') or not SHA.fullmatch(str(mapping.get('evidence_sha256',''))):return 'needs_botanical_review'
++    visual=d.get('visual',{});privacy=d.get('privacy_checks',{})
++    if set(visual)!={'photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'} or not all(v is True for v in visual.values()):return 'needs_human_review'
++    if set(privacy)!={'people','faces','plates','residences','screens_documents','sensitive_location'} or not all(v=='absent' for v in privacy.values()):return 'needs_privacy_review'
++    pairs=c.get('pairs',[])
++    if any(p.get('signal')=='exact_duplicate' for p in pairs):return 'rejected_duplicate'
++    if any(d.get('pair_decisions',{}).get(p['pair_id'])!='distinct' for p in pairs):return 'needs_duplicate_review'
++    return 'approved_for_dataset'
++
++class Dataset:
++    def __init__(self,root,config,offline=False):
++        self.root=safe_path(root);self.config=config;self.offline=offline;self.events=[];self.fd=None
++        validate_config(config,offline);self.config_hash=sha(encode(config))
++        require(ROOT not in self.root.parents and self.root!=ROOT,'dataset_in_git')
++        if not offline:
++            require(Path('/tmp') not in self.root.parents and self.root.name.startswith('p08-'),'private_p08_root')
++            require(shutil.disk_usage(self.root.parent).free>=3*1024**3,'insufficient_disk')
++    def path(self,name):
++        require(isinstance(name,str) and not Path(name).is_absolute() and '..' not in Path(name).parts,'path_escape')
++        return safe_path(self.root/name)
++    def __enter__(self):
++        self.root.mkdir(mode=0o700,parents=False,exist_ok=True)
++        require(stat.S_IMODE(self.root.stat().st_mode)==0o700,'private_permissions')
++        self.fd=os.open(self.path('.lock'),os.O_RDWR|os.O_CREAT|os.O_NOFOLLOW,0o600)
++        try:
++            try:fcntl.flock(self.fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
++            except BlockingIOError:raise RecoveryError('writer_locked') from None
++            for name in ['originals','quarantine','parts','evidence']:
++                self.path(name).mkdir(mode=0o700,exist_ok=True)
++            self.replay()
++            if not self.events:
++                self.append('config',self.config)
++                persist(self.path('config.json'),encode(self.config),True)
++            else:require(self.events[0]['data']==self.config,'config_changed')
++            self.verify_objects()
++            if self.config['code_sha256']!=fingerprint():
++                transition={'from':self.config['code_sha256'],'to':fingerprint(),'reason':'deterministic_review_html_key_order'}
++                if transition not in self.select('code_compatibility'):self.append('code_compatibility',transition)
++            return self
++        except BaseException:
++            os.close(self.fd);self.fd=None;raise
++    def __exit__(self,*args):
++        if self.fd is not None:os.close(self.fd);self.fd=None
++    def replay(self):
++        p=self.path('journal.jsonl')
++        if not p.exists():return
++        raw=read(p);require(not raw or raw.endswith(b'\n'),'journal_partial')
++        prev='0'*64
++        for seq,line in enumerate(raw.splitlines(keepends=True),1):
++            e=load(line);require(set(e)=={'seq','timestamp','event_id','prev_event_hash','event_hash','config_sha256','type','data'},'event_schema')
++            hashed={k:v for k,v in e.items() if k!='event_hash'}
++            require(encode(e)==line and e['seq']==seq and e['prev_event_hash']==prev and sha(encode(hashed))==e['event_hash'],'journal_hash')
++            require(e['config_sha256']==self.config_hash,'config_changed')
++            self.events.append(e);prev=e['event_hash']
++    def append(self,kind,data):
++        require(self.fd is not None,'lock_required')
++        e={'seq':len(self.events)+1,'timestamp':now(),'event_id':os.urandom(16).hex(),
++           'prev_event_hash':self.events[-1]['event_hash'] if self.events else '0'*64,
++           'config_sha256':self.config_hash,'type':kind,'data':data}
++        e['event_hash']=sha(encode(e))
++        fd=os.open(self.path('journal.jsonl'),os.O_WRONLY|os.O_APPEND|os.O_CREAT|os.O_NOFOLLOW,0o600)
++        with os.fdopen(fd,'ab') as f:f.write(encode(e));f.flush();os.fsync(f.fileno())
++        fsync_dir(self.root);self.events.append(e);return e
++    def select(self,kind):return [e['data'] for e in self.events if e['type']==kind]
++    def verify_objects(self):
++        for e in self.events:
++            d=e['data']
++            if e['type'] in {'received','committed'}:
++                for pathkey,hashkey in [('original_path','original_sha256'),('sanitized_path','sanitized_sha256'),('part_path','original_sha256')]:
++                    if d.get(pathkey):require(sha(read(self.path(d[pathkey])))==d[hashkey],'object_hash_mismatch')
++            if e['type']=='evidence':require(sha(read(self.path(d['path'])))==d['sha256'],'evidence_hash_mismatch')
++    def records(self):
++        result={}
++        for e in self.events:
++            if e['type'] in {'committed','classified'}:result[e['data']['candidate_id']]=dict(e['data'])
++        return list(result.values())
++    def record(self,c):return next((x for x in self.records() if x['candidate_id']==candidate_id(c)),None)
++    def classify(self,c,state,reason):
++        r={**c,'candidate_id':candidate_id(c),'state':state,'reasons':[reason]}
++        self.append('classified',r);return r
++    def save_page(self,source,class_id,cursor,candidates,next_cursor):
++        require(source in SOURCES and class_id.startswith('species_'),'page_class')
++        key=sha(encode([source,class_id,cursor]))
++        old=next((p for p in self.select('page') if p['page_id']==key),None)
++        if old:return old
++        ids=[candidate_id(c) for c in candidates];require(len(ids)==len(set(ids)),'duplicate_page_ids')
++        require(len(ids)<= (10 if source=='commons' else 100),'page_size')
++        pages=[p for p in self.select('page') if p['source']==source and p['class_id']==class_id]
++        require(len(pages)<(self.config['limits']['pages'] if source=='commons' else 1),'page_budget')
++        if next_cursor is not None:require(type(next_cursor)is int and next_cursor>cursor,'cursor_regression')
++        page={'page_id':key,'source':source,'class_id':class_id,'cursor':cursor,'next_cursor':next_cursor,'candidates':candidates}
++        self.append('page',page);return page
++    def advance(self,page):
++        if page['page_id'] in [a['page_id'] for a in self.select('cursor')]:return
++        done={x['candidate_id'] for x in self.records()}
++        require(all(candidate_id(c) in done for c in page['candidates']),'cursor_before_commit')
++        self.append('cursor',{'page_id':page['page_id'],'next_cursor':page['next_cursor']})
++    def ingest(self,c,download,crash=lambda _:None):
++        cid=candidate_id(c);old=self.record(c)
++        if old and not (old['state']=='transfer_failed' and set(old.get('reasons',[])) & RETRYABLE):
++            require(old['source']==c['source'] and old['file_url']==c['file_url'],'remote_revision_changed')
++            if not set(c['class_ids']) <= set(old['class_ids']):
++                old['class_ids']=sorted(set(old['class_ids']) | set(c['class_ids']))
++                old.update(state='needs_botanical_review', reasons=['conflicting_class_associations'])
++                old.pop('decision',None)
++                self.append('classified',old);self.project()
++            for field in ['revision_id','source_timestamp','source_sha1']:
++                if c.get(field)!=old.get(field):
++                    raise RecoveryError('remote_revision_changed')
++            self.project()
++            return old
++        require(c['source'] in SOURCES and c['class_ids'] and set(c['class_ids'])<= {x['class_id'] for x in canonical()[:12]},'candidate_class')
++        if rights(c)!='passed':return self.classify(c,'needs_license_review','individual_rights_unproven')
++        try:safe_url(c['file_url'],c['source'],True)
++        except RecoveryError as error:return self.classify(c,'rejected_format',str(error))
++        if c.get('mime') not in {'image/jpeg','image/png'} or (c.get('declared_size') is not None and
++                (type(c['declared_size'])is not int or not 0<c['declared_size']<=self.config['limits']['file_bytes'])):
++            return self.classify(c,'rejected_format','declared_format_or_size')
++        recv=next((x for x in self.select('received') if x['candidate_id']==cid),None)
++        intents=[x for x in self.select('intention') if x['candidate_id']==cid]
++        if not recv:
++            counts={cls:len({x['candidate_id'] for x in self.select('intention') if x['source']==c['source'] and cls in x['class_ids']}) for cls in c['class_ids']}
++            if not intents and any(n>=self.config['limits']['transfers'] for n in counts.values()):return self.classify(c,'deferred_budget','transfer_budget')
++            intent={'candidate_id':cid,'source':c['source'],'class_ids':c['class_ids'],'attempt':len(intents)+1}
++            self.append('intention',intent);crash('intention')
++            try:raw=download(c)
++            except RecoveryError as error:return self.classify(c,'transfer_failed',str(error))
++            require(isinstance(raw,bytes) and 0<len(raw)<=self.config['limits']['file_bytes'],'file_size')
++            part='parts/'+cid+'-'+str(len(intents)+1)+'.part'
++            persist(self.path(part),raw,True)
++            recv={'candidate_id':cid,'part_path':part,'original_sha256':sha(raw)}
++            self.append('received',recv);crash('received')
++        raw=read(self.path(recv['part_path']))
++        require(sha(raw)==recv['original_sha256'],'object_hash_mismatch')
++        original='originals/'+sha(raw)
++        used=sum(p.stat().st_size for base in ['originals','quarantine'] for p in self.path(base).iterdir() if p.is_file())
++        require(used+(0 if self.path(original).exists() else len(raw))+MAX_BYTES<=self.config['limits']['storage_bytes'],'storage_budget')
++        persist(self.path(original),raw,True);crash('original')
++        rec={**c,'candidate_id':cid,'original_sha256':sha(raw),'original_path':original,'state':'needs_human_review',
++             'sanitized_sha256':None,'sanitized_path':None,'technical':{},'reasons':['human_review_required'], 'pairs':[],'resolved_url':c['file_url'],'config_sha256':self.config_hash,'manifest_sha256':self.config['manifest_sha256'],'code_sha256':self.config['code_sha256']}
++        try:
++            if c.get('source_sha1'):require(hashlib.sha1(raw).hexdigest()==c['source_sha1'],'declared_hash_mismatch')
++            require(c.get('declared_size') in (None,len(raw)),'declared_size_mismatch')
++            clean,suffix=sanitize(raw,c['file_url'],c['mime']);rec['technical']=technical(clean)
++            rec['sanitized_sha256']=sha(clean);rec['sanitized_path']='quarantine/'+sha(clean)+suffix
++            persist(self.path(rec['sanitized_path']),clean,True);crash('sanitized')
++        except RecoveryError as error:rec.update(state='rejected_format',reasons=[str(error)])
++        self.append('committed',rec);crash('committed')
++        self.project();return rec
++    def project(self):
++        persist(self.path('records.json'),encode(self.records()))
++        persist(self.path('summary.json'),encode(self.summary()))
++    def summary(self):
++        recs=self.records();coverage=[]
++        for cls in canonical():
++            for source in SOURCES:
++                subset=[r for r in recs if r['source']==source and cls['class_id'] in r['class_ids']]
++                stopped=[x for x in self.select('source_status') if x['source']==source and x['class_id']==cls['class_id']]
++                status=stopped[-1]['status'] if stopped else ('protection_not_queried' if cls['kind']=='protection' else 'not_attempted')
++                coverage.append({'class_id':cls['class_id'],'source':source,'status':status,'candidate_cap':0 if cls['kind']=='protection' else self.config['limits']['candidates'],
++                                 'transfer_cap':0 if cls['kind']=='protection' else self.config['limits']['transfers'], 'found':len(subset),
++                                 'transferred':sum(bool(r.get('original_sha256')) for r in subset),
++                                 'technical_integrity':sum(bool(r.get('sanitized_sha256')) for r in subset),
++                                 'license_valid':sum(rights(r)=='passed' for r in subset),
++                                 'expert_validated':sum(r['state']=='approved_for_dataset' for r in subset),
++                                 'approved':sum(r['state']=='approved_for_dataset' for r in subset),
++                                 'rejected':sum(r['state'].startswith('rejected_') for r in subset),
++                                 'pending':sum(not r['state'].startswith(('approved_','rejected_')) for r in subset)})
++        result={'schema_version':1,'stage':'pending_human_acceptance','coverage':coverage,'counts':dict(sorted(Counter(r['state'] for r in recs).items())),
++                'unique_objects':len(recs),'usable':0,'minimum_experimental_pilot':None,'scientific_sufficiency':'not_demonstrated',
++                'production_sufficiency':'not_demonstrated','training_authorized':False,'partition_authorized':False,'training_status':'blocked'}
++        validate_public(result);return result
++
++PUBLIC_KEYS={'schema_version','stage','coverage','counts','unique_objects','usable','minimum_experimental_pilot','scientific_sufficiency','production_sufficiency','training_authorized','partition_authorized','training_status'}
++COVERAGE_KEYS={'class_id','source','status','candidate_cap','transfer_cap','found','transferred','technical_integrity','license_valid','expert_validated','approved','rejected','pending'}
++STATUSES={'not_attempted','no_crosswalk','source_blocked','exhausted_within_query','budget_reached','all_rejected','review_pending','protection_not_queried'}
++def validate_public(value):
++    require(set(value)==PUBLIC_KEYS,'private_export')
++    require(value['stage']=='pending_human_acceptance' and value['usable']==0 and value['minimum_experimental_pilot'] is None,'public_authority')
++    require(value['training_authorized'] is False and value['partition_authorized'] is False and value['training_status']=='blocked','public_training')
++    require(value['scientific_sufficiency']==value['production_sufficiency']=='not_demonstrated','public_sufficiency')
++    require(set(value['counts'])<=STATES and all(type(v)is int and v>=0 for v in value['counts'].values()),'public_counts')
++    expected=[(c['class_id'],s) for c in canonical() for s in SOURCES]
++    require([(c['class_id'],c['source']) for c in value['coverage']]==expected,'public_classes')
++    for c in value['coverage']:
++        require(set(c)==COVERAGE_KEYS and c['status'] in STATUSES,'private_export')
++        require(all(type(v)is int and v>=0 for k,v in c.items() if k not in {'class_id','source','status'}),'public_types')
++    require(type(value['schema_version'])is int and value['schema_version']==1 and type(value['unique_objects'])is int,'public_schema')
++
++class PinnedHTTPS(http.client.HTTPSConnection):
++    """Pin a validated public address; TLS still verifies the original hostname."""
++    def connect(self):
++        address=public_addresses(self.host)[0]
++        sock=socket.create_connection((address,443),self.timeout)
++        try:self.sock=self._context.wrap_socket(sock,server_hostname=self.host)
++        except BaseException:sock.close();raise
++
++def retry_delay(value,attempt,clock=None):
++    clock=clock or time.time
++    if value:
++        try:
++            delay=int(value) if value.isdecimal() else parsedate_to_datetime(value).timestamp()-clock()
++            return max(0,delay)
++        except (ValueError,TypeError,OverflowError):raise RecoveryError('invalid_retry_after') from None
++    return 2**(attempt+1)
++
++class Transport:
++    def __init__(self,ds):self.ds=ds;self.last=0
++    def get(self,url,source,media=False):
++        require(not self.ds.offline,'offline_network_forbidden')
++        limit=self.ds.config['limits']['file_bytes'] if media else 2*1024**2
++        safe_url(url,source,media)
++        for attempt in range(3):
++            reservations=self.ds.select('request');finished={x['request_id']:x for x in self.ds.select('response')}
++            require(sum(x['source']==source for x in reservations)<self.ds.config['limits']['requests'],'request_budget')
++            media_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'])
++            hour_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations
++                           if x['media'] and x['epoch']>time.time()-3600)
++            if media:
++                require(media_total+limit<=self.ds.config['limits']['media_bytes'],'media_budget')
++                require(hour_total+limit<=self.ds.config['limits']['hour_bytes'],'hour_budget')
++            requests_after=[x for x in self.ds.select('resume_after') if x['source']==source]
++            if requests_after:require(time.time()>=requests_after[-1]['epoch'],'resume_after')
++            delay=max(0,1-(time.time()-reservations[-1]['epoch'])) if reservations else 0
++            if delay:time.sleep(delay)
++            rid=os.urandom(16).hex()
++            self.ds.append('request',{'request_id':rid,'source':source,'media':media,'reserved':limit,'epoch':time.time(),'url':url})
++            received=0;conn=None;status=None;retry=None;code='network_error';spool=None
++            try:
++                p=urlsplit(url);conn=PinnedHTTPS(p.hostname,timeout=20,context=ssl.create_default_context())
++                conn.request('GET',p.path+('?' + p.query if p.query else ''),headers={'User-Agent':self.ds.config['user_agent'],'Accept':'application/json,image/jpeg,image/png','Accept-Encoding':'identity'})
++                response=conn.getresponse();status=response.status
++                if status in {301,302,303,307,308}:
++                    # Validated redirect is reported for explicit source reconciliation; never silently switches objects.
++                    safe_url(urljoin(url,response.getheader('Location','')),source,media)
++                    raise RecoveryError('redirect_requires_reconciliation')
++                if status!=200:
++                    retry=response.getheader('Retry-After');code='http_'+str(status)
++                    raise RecoveryError(code)
++                length=response.getheader('Content-Length')
++                require(not length or length.isdecimal() and int(length)<=limit,'response_size')
++                require(response.getheader('Content-Encoding','identity')=='identity','content_encoding')
++                chunks=[];started=time.monotonic()
++                if media:
++                    require(shutil.disk_usage(self.ds.root).free>=3*1024**3,'insufficient_disk')
++                    spool=os.fdopen(os.open(self.ds.path('parts/request-'+rid+'.part'),os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600),'wb')
++                while True:
++                    require(time.monotonic()-started<=20,'response_timeout')
++                    chunk=response.read(min(65536,limit+1-received))
++                    if not chunk:break
++                    received+=len(chunk);chunks.append(chunk)
++                    if spool:spool.write(chunk);spool.flush();os.fsync(spool.fileno())
++                    require(received<=limit,'response_size')
++                raw=b''.join(chunks)
++                if not media:
++                    data=load(raw)
++                    if isinstance(data,dict) and data.get('error',{}).get('code')=='maxlag':
++                        status=503;retry=response.getheader('Retry-After');raise RecoveryError('maxlag')
++                require(not length or received==int(length),'response_length_mismatch')
++                code='ok'
++                return raw
++            except (OSError,http.client.HTTPException) as error:
++                code='timeout' if isinstance(error,TimeoutError) else 'network_error'
++            except RecoveryError as error:
++                code=str(error)
++                if code not in RETRYABLE:raise
++            finally:
++                if spool:spool.close();fsync_dir(self.ds.path('parts'))
++                if conn:conn.close()
++                self.ds.append('response',{'request_id':rid,'received':received,'status':status,'code':code})
++            if attempt==2:raise RecoveryError(code)
++            delay=retry_delay(retry,attempt)
++            if delay>self.ds.config['limits']['wait_seconds']:
++                self.ds.append('resume_after',{'source':source,'epoch':time.time()+delay})
++                raise RecoveryError('resume_after')
++            time.sleep(delay)
++        raise RecoveryError('transfer_failed')
++
++
++def commons_query(cls,cursor):
++    require(cls['kind']=='species','protection_query')
++    return {'action':'query','format':'json','formatversion':2,'generator':'search','gsrsearch':'"'+cls['scientific_name']+'"',
++            'gsrnamespace':6,'gsrlimit':10,'gsroffset':cursor,'gsrsort':'relevance','prop':'imageinfo|revisions',
++            'rvprop':'ids','iiprop':'url|mime|size|timestamp|sha1|extmetadata','iilimit':1,'iiextmetadatalanguage':'en','iiextmetadatafilter':'Artist|Credit|Attribution|Restrictions|Copyrighted|AttributionRequired|License|LicenseShortName|LicenseUrl|Permission','maxlag':5}
++
++def commons_page(data,cls,evidence,config):
++    require(isinstance(data,dict) and not ('error' in data or 'warnings' in data),'commons_schema')
++    require('query' in data or data.get('batchcomplete') is True,'commons_schema')
++    pages=data.get('query',{}).get('pages',[])
++    require(isinstance(pages,list) and len(pages)<=10,'commons_pages')
++    result=[]
++    for page in pages:
++        try:
++            old=commons.inspect_page(page,cls,'"'+cls['scientific_name']+'"',config['cutoff'])
++            info=page['imageinfo'][0];meta=info.get('extmetadata',{})
++            record={'source':'commons','media_id':str(old['page_id']),'class_ids':[cls['class_id']],
++                    'page_id':old['page_id'],'revision_id':(page.get('revisions') or [{}])[0].get('revid'),
++                    'file_url':old['file_url'],'source_page_url':old['page_url'],'mime':old['declared_mime'],
++                    'declared_size':old['declared_size'],'declared_width':info.get('width'),'declared_height':info.get('height'),
++                    'source_sha1':old['source_sha1'],'source_timestamp':old['source_timestamp'],
++                    'author':old['author'],'license_id':old['license_id'],'license_name':old['license'],
++                    'license_url':old['license_url'],'restrictions':old['restrictions'],
++                    'credit':commons.plain(old['credit_html']),'attribution':commons.plain(old['attribution_html']),
++                    'title':old['title'],'evidence_sha256':evidence,'rights_consistent':False,
++                    'database_rights':'passed' if config['source_contracts'].get('commons',{}).get('database_rights')=='passed' else 'pending',
++                    'mapping':None,'mapping_reason':'source_taxon_id_unproven','scientific_name_received':None,
++                    'taxonomic_confidence':'unmapped','observation_id':None,'origin_fidelity':'provider_original',
++                    'camera_original_verified':False}
++            # Require the actual individual grant, known photographer and coherent authorship/source.
++            record['rights_consistent']=bool(record['revision_id'] and meta.get('LicenseUrl') and meta.get('Artist') and
++                                              not meta.get('Permission',{}).get('value') and 'own work' in record['credit'].lower() and record['source_page_url'].startswith('https://commons.wikimedia.org/wiki/'))
++            result.append(record)
++        except (KeyError,TypeError,ValueError,commons.AcquisitionError):raise RecoveryError('commons_item_schema') from None
++    continuation=data.get('continue');next_cursor=None
++    if continuation is not None:
++        require(isinstance(continuation,dict) and set(continuation)<={'continue','gsroffset'} and type(continuation.get('gsroffset'))is int,'commons_cursor')
++        next_cursor=continuation['gsroffset']
++    return result,next_cursor
++
++
++def acquire_inat(ds,cls,transport,fixture):
++    cid=cls['class_id'];crosswalk=ds.config['crosswalk'][cid]
++    try:
++        query=inat.build_query(crosswalk,cls,ds.config['cutoff'])
++        # A reviewed evidence document must actually be present and match its digest.
++        ev=crosswalk['evidence'];require(sha(read(ds.path(ev['path'])))==ev['sha256'],'crosswalk_evidence_hash')
++        saved=next((p for p in ds.select('page') if p['source']=='inaturalist' and p['class_id']==cid),None)
++        if saved:page=saved
++        else:
++            raw=encode(fixture['inaturalist'][cid]) if fixture is not None else transport.get(inat.API_URL+'?'+urlencode(query),'inaturalist')
++            digest=sha(raw);path='evidence/'+digest+'.json';persist(ds.path(path),raw,True)
++            if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
++            data=load(raw);parsed=inat.parse_page(data,crosswalk,cls,ds.config['cutoff'])
++            by_photo={}
++            for observation in data['results']:
++                for photo in observation['photos']:
++                    by_photo.setdefault(str(photo['id']),(photo,observation))
++            records=[]
++            for initial in parsed['candidates']:
++                media_id=initial['media_id'];photo,observation=by_photo[media_id]
++                proof=ds.config['legal_evidence'].get(media_id)
++                if proof:
++                    for key in ['photo','observation']:
++                        require(sha(read(ds.path(proof[key]['path'])))==proof[key]['evidence_sha256'],'rights_evidence_hash')
++                item=inat.photo_record(photo,observation,proof)
++                eligible=item['download_allowed'] and initial['taxonomic_confidence']=='source_supported'
++                item.update(class_ids=[cid],license_id='cc-by-4.0' if item['license_code']=='cc-by' else item['license_code'],
++                            license_name='CC BY 4.0' if item['license_code']=='cc-by' else 'CC0 1.0',license_url=item['legal_url'],
++                            restrictions='',rights_consistent=eligible,database_rights='passed' if item['database_rights_passed'] else 'pending',
++                            evidence_sha256=item['license_evidence_sha256'],mapping=crosswalk,declared_size=None,
++                            mime='image/png' if (item['file_url'] or '').endswith('.png') else 'image/jpeg',
++                            taxonomic_confidence=initial['taxonomic_confidence'])
++                records.append(item)
++            page=ds.save_page('inaturalist',cid,0,records,None)
++            ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
++                                      'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
++        for c in page['candidates']:
++            ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
++        ds.advance(page)
++        return 'budget_reached'
++    except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
++        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':'inaturalist_contract_or_evidence'})
++        return 'source_blocked'
++
++
++def acquire(ds,fixture=None):
++    transport=Transport(ds)
++    if fixture is not None:require(ds.offline,'fixture_mode')
++    elif ds.offline:raise RecoveryError('fixture_required')
++    for cls in canonical():
++        for source in SOURCES:
++            cid=cls['class_id']
++            statuses=[s for s in ds.select('source_status') if s['source']==source and s['class_id']==cid]
++            if statuses:
++                failed=[e for e in ds.select('source_failure') if e['source']==source and e['class_id']==cid]
++                if statuses[-1]['status']!='source_blocked' or not failed or failed[-1]['code'] not in RETRYABLE:continue
++            status='protection_not_queried'
++            if cls['kind']=='species':
++                if source=='inaturalist' and cid not in ds.config['crosswalk']:
++                    status='no_crosswalk'
++                elif source=='inaturalist':
++                    status=acquire_inat(ds,cls,transport,fixture)
++                else:
++                    cursor=0;status='budget_reached'
++                    for page_index in range(ds.config['limits']['pages']):
++                        saved=next((p for p in ds.select('page') if p['source']==source and p['class_id']==cid and p['cursor']==cursor),None)
++                        try:
++                            if saved:page=saved
++                            else:
++                                if fixture is not None:
++                                    raw=encode(fixture.get(cid,{}).get(str(cursor),{'batchcomplete':True}))
++                                else:raw=transport.get('https://commons.wikimedia.org/w/api.php?'+urlencode(commons_query(cls,cursor)),source)
++                                digest=sha(raw);path='evidence/'+digest+'.json'
++                                persist(ds.path(path),raw,True)
++                                if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
++                                candidates,next_cursor=commons_page(load(raw),cls,digest,ds.config)
++                                page=ds.save_page(source,cid,cursor,candidates,next_cursor)
++                            examined={candidate_id(c) for p in ds.select('page') if p['source']==source and p['class_id']==cid for c in p['candidates']}
++                            require(len(examined)<=ds.config['limits']['candidates'],'candidate_budget')
++                            for c in page['candidates']:
++                                def download(record):
++                                    if fixture is not None:
++                                        require('synthetic_media' in fixture,'fixture_media_missing')
++                                        return read(Path(fixture['synthetic_media'])/str(record['media_id']))
++                                    return transport.get(record['file_url'],source,True)
++                                ds.ingest(c,download)
++                            ds.advance(page)
++                            retryable=[ds.record(c) for c in page['candidates'] if ds.record(c)['state']=='transfer_failed'
++                                       and set(ds.record(c).get('reasons',[])) & RETRYABLE]
++                            if retryable:
++                                raise RecoveryError(retryable[0]['reasons'][0])
++                            if page['next_cursor'] is None:
++                                status='exhausted_within_query';break
++                            cursor=page['next_cursor']
++                        except RecoveryError as error:
++                            ds.append('source_failure',{'source':source,'class_id':cid,'code':str(error)})
++                            status='source_blocked';break
++            ds.append('source_status',{'source':source,'class_id':cid,'status':status})
++    ds.project()
++    return 1 if any(c['status']=='source_blocked' for c in ds.summary()['coverage']) else 0
++
++
++def historical(source):
++    """Read-only verification against the frozen P07 closure (never P07 finalizers)."""
++    source=safe_path(source);closure=load(read(ROOT/'artifacts/bianchini/v2/codex/P07/closure-evidence.json'))
++    p07=source.parent/'p07-curation-20260928'
++    for n,h in closure['external_final_sha256'].items():require(sha(read(p07/n))==h,'p07_reference_hash')
++    before=load(read(p07/'source-before.json'))
++    actual={str(p.relative_to(source)):sha(read(p)) for p in source.rglob('*') if p.is_file()}
++    require(before==actual and len(actual)==29,'p06_source_hashes')
++    records=[]
++    for item in closure['images_before_after']:
++        h=item['sha256_after'];path=source/'quarantine'/f'{h}.jpg';raw=read(path)
++        require(sha(raw)==h,'p07_image_hash')
++        records.append({'candidate_id':item['id'],'sanitized_sha256':h,'technical':technical(raw),'class_ids':[],
++                        'original_sha256':None,'observation_id':None})
++    return actual,records
++
++
++def inspect(ds,source):
++    hashes,prior=historical(source);recs=ds.records();pairs=[]
++    combined=[*prior,*[r for r in recs if r.get('sanitized_sha256')]]
++    for i,a in enumerate(combined):
++        for b in combined[i+1:]:
++            if a['candidate_id'].startswith('Q') and b['candidate_id'].startswith('Q'):continue
++            dist=(int(a['technical']['dhash64'],16)^int(b['technical']['dhash64'],16)).bit_count()
++            exact=bool(a.get('sanitized_sha256')==b.get('sanitized_sha256') or a.get('original_sha256') and a.get('original_sha256')==b.get('original_sha256'))
++            same=bool(a.get('observation_id') and a.get('observation_id')==b.get('observation_id'))
++            signal='exact_duplicate' if exact else 'near_duplicate' if dist<=6 else 'borderline' if dist<=10 else 'same_series' if same else 'no_algorithmic_signal'
++            pairs.append({'pair_id':a['candidate_id']+'-'+b['candidate_id'],'left':a['candidate_id'],'right':b['candidate_id'],'distance':dist,'signal':signal})
++    for rec in recs:
++        related=[p for p in pairs if rec['candidate_id'] in {p['left'],p['right']} and p['signal']!='no_algorithmic_signal']
++        if rec.get('pairs')!=related:
++            rec['pairs']=related;rec.pop('decision',None)
++            if rec.get('sanitized_sha256'):
++                rec['state']='rejected_duplicate' if any(p['signal']=='exact_duplicate' for p in related) else 'needs_duplicate_review' if related else 'needs_human_review'
++            ds.append('classified',rec)
++    ds.project()
++    report={'p07_images':len(prior),'p06_hashes':hashes,'pairs':pairs,'records':recs,'summary':ds.summary()}
++    persist(ds.path('inspection.json'),encode(report))
++    rows=[];attrs=[]
++    for r in recs:
++        image=f'<img loading="lazy" width="240" src="{escape(r["sanitized_path"])}">' if r.get('sanitized_path') else ''
++        detail=escape(json.dumps(r,ensure_ascii=False,indent=2,sort_keys=True))
++        rows.append(f'<article><h2>{r["candidate_id"]}</h2>{image}<pre>{detail}</pre></article>')
++        if r.get('original_sha256'):
++            attrs.append({k:r.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256','author','credit','attribution','title','source_page_url','license_url','restrictions']})
++            attrs[-1]['changes']='EXIF orientation; RGB pixel reconstruction; metadata removal; JPEG quality 95 or PNG; no crop or enhancement'
++    html='<!doctype html><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; img-src \'self\'; style-src \'unsafe-inline\'"><title>P08 private review</title><h1>P08 — pending human review</h1>'+''.join(rows)
++    persist(ds.path('review.html'),html.encode())
++    persist(ds.path('Attributions.jsonl'),b''.join(encode(a) for a in attrs))
++    persist(ds.path('NOTICE.md'),('P08 private attribution bundle; no redistribution authorized.\n\n'+''.join(json.dumps(a,ensure_ascii=False)+'\n\n' for a in attrs)).encode())
++    persist(ds.path('decisions.template.json'),encode({'authority':'human','decisions':[
++        {'candidate_id':r['candidate_id'],'original_sha256':r.get('original_sha256'),'sanitized_sha256':r.get('sanitized_sha256'),
++         'evidence_digest':review_digest(r),'reviewer':None,'reviewed_at':None,'authority':'human','quality':'pending',
++         'privacy':'pending','botanical':'pending','duplicates':'pending','expert_confirmation':False,
++         'qualification':None,'botanical_evidence':None,'mapping':None,'rationale':None} for r in recs]}))
++    return report
++
++
++def finalize(ds,decisions):
++    data=load(read(decisions));require(data.get('authority')=='human' and isinstance(data.get('decisions'),list),'human_authority')
++    ids=[d.get('candidate_id') for d in data['decisions']];require(len(ids)==len(set(ids)),'duplicate_decisions')
++    recs={r['candidate_id']:r for r in ds.records()};require(set(ids)==set(recs),'decision_coverage')
++    for d in data['decisions']:
++        rec=recs[d['candidate_id']]
++        if rec.get('decision')==d:continue
++        state=decide(rec,d)
++        if state=='approved_for_dataset':
++            inspection=load(read(ds.path('inspection.json')))
++            require(inspection.get('p07_images')==17 and any(review_digest(item)==review_digest(rec)
++                    for item in inspection['records']),'inspection_binding')
++            attrs=[load(line) for line in read(ds.path('Attributions.jsonl')).splitlines()]
++            require(any(all(item.get(k)==rec.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256',
++                         'author','license_url','source_page_url']) for item in attrs),'attribution_binding')
++            require(sha(read(ds.path(d['mapping']['evidence_path'])))==d['mapping']['evidence_sha256'],'mapping_evidence_hash')
++            require(sha(read(ds.path(d['botanical_evidence_path'])))==d['botanical_evidence'],'botanical_evidence_hash')
++        rec.update(state=state,decision=d);ds.append('classified',rec)
++    ds.project()
++
++
++def verify(ds,source,acceptance=None):
++    ds.verify_objects();historical(source);validate_public(ds.summary())
++    require(len({(s['source'],s['class_id']) for s in ds.select('source_status')})==28,'incomplete_round')
++    require({p['page_id'] for p in ds.select('page')}=={p['page_id'] for p in ds.select('cursor')},'pending_pages')
++    if acceptance:
++        a=load(read(acceptance));manifest=read(ds.path('final-manifest.json'))
++        require(a.get('decision')=='accepted' and a.get('authority')=='human' and a.get('reviewer') and a.get('reviewed_at') and a.get('manifest_sha256')==sha(manifest),'human_acceptance')
++        files=load(manifest)['files']
++        actual={str(p.relative_to(ds.root)):sha(read(p)) for p in ds.root.rglob('*') if p.is_file() and str(p.relative_to(ds.root)) not in {'.lock','final-manifest.json','acceptance.json'}}
++        require(files==actual,'acceptance_coverage_or_bytes')
++        require({'journal.jsonl','config.json','records.json','summary.json','inspection.json','Attributions.jsonl','NOTICE.md','review.html'} <= set(files),'acceptance_required_files')
++        require(a.get('training_authorized') is False,'acceptance_not_training')
++    return 0
++
++
++def main(argv=None):
++    parser=argparse.ArgumentParser(description=__doc__)
++    sub=parser.add_subparsers(dest='command',required=True)
++    for name in ['acquire','inspect','finalize','verify']:
++        p=sub.add_parser(name);p.add_argument('--output',required=True);p.add_argument('--offline-fixture')
++        if name=='acquire':p.add_argument('--config',required=True)
++        if name in {'inspect','verify'}:p.add_argument('--p07-source',required=True)
++        if name=='finalize':p.add_argument('--decisions',required=True)
++        if name=='verify':p.add_argument('--acceptance')
++    args=parser.parse_args(argv)
++    try:
++        config=load(read(args.config if args.command=='acquire' else Path(args.output)/'config.json'))
++        with Dataset(args.output,config,offline=bool(args.offline_fixture)) as ds:
++            if args.command=='acquire':code=acquire(ds,load(read(args.offline_fixture)) if args.offline_fixture else None)
++            elif args.command=='inspect':inspect(ds,args.p07_source);code=0
++            elif args.command=='finalize':finalize(ds,args.decisions);code=0
++            else:code=verify(ds,args.p07_source,args.acceptance)
++        print(json.dumps({'command':args.command,'status':'passed' if code==0 else 'source_blocked'}));return code
++    except (OSError,ValueError,KeyError,TypeError):
++        print('p08_invalid_config_schema_hash_or_io',file=sys.stderr);return 2
++    except KeyboardInterrupt:
++        print('p08_cancelled_replay_required',file=sys.stderr);return 1
++
++if __name__=='__main__':raise SystemExit(main())
+diff --git a/scripts/phase1/test_inaturalist_source.py b/scripts/phase1/test_inaturalist_source.py
+new file mode 100644
+index 0000000..12e9a91
+--- /dev/null
++++ b/scripts/phase1/test_inaturalist_source.py
+@@ -0,0 +1,158 @@
++"""Synthetic iNaturalist adapter contracts; no network or real identifiers."""
++import copy
++import unittest
++from inaturalist_source import ContractError, build_query, parse_page, photo_record
++
++
++CUTOFF = "2026-10-05T00:00:00Z"
++CLASS = {"class_id": "species_01", "kind": "species", "scientific_name": "Epipremnum aureum", "taxonomy_ref_ids": ["kew_species_01"]}
++
++
++def crosswalk():
++    return {"class_id": "species_01", "source": "inaturalist", "namespace": "inaturalist", "source_taxon_id": 999999001,
++            "scientific_name": CLASS["scientific_name"], "rank": "species", "status": "active", "synonym_of": None,
++            "authorship": None, "authorship_missing_reason": "Not supplied by synthetic source", "taxonomy_ref_ids": ["kew_species_01"],
++            "evidence": {"url": "https://www.inaturalist.org/taxa/999999001", "version": "fixture-v1", "date": "2026-10-04", "sha256": "a" * 64},
++            "reviewer": {"id": "synthetic-reviewer", "qualification": "synthetic botanist", "decision": "approved"}}
++
++
++def observation(identifier=999999002):
++    return {"id": identifier, "created_at": "2026-10-04T00:00:00Z", "quality_grade": "research", "license_code": "cc0",
++            "taxon": {"id": 999999001, "name": CLASS["scientific_name"], "rank": "species", "is_active": True},
++            "photos": [{"id": 999999003, "license_code": "cc-by", "attribution": "Synthetic author, CC BY", "url": "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg"}]}
++
++
++def legal():
++    return {"photo_id": 999999003, "observation_id": 999999002, "reviewer": "synthetic-reviewer", "reviewed_at": CUTOFF,
++            "author": "Synthetic author", "licensor": "Synthetic author", "credit": "Synthetic credit", "decision": "approved",
++            "photo": {"license_code": "cc-by", "version": "4.0", "legal_url": "https://creativecommons.org/licenses/by/4.0/", "evidence_sha256": "b" * 64, "source_url": "https://www.inaturalist.org/photos/999999003", "restrictions": []},
++            "observation": {"license_code": "cc0", "version": "1.0", "legal_url": "https://creativecommons.org/publicdomain/zero/1.0/", "evidence_sha256": "c" * 64, "source_url": "https://www.inaturalist.org/observations/999999002", "restrictions": []},
++            "database_rights": "compatible"}
++
++
++def page(*observations):
++    return {"total_results": len(observations), "page": 1, "per_page": 100, "results": list(observations)}
++
++
++class AdapterTests(unittest.TestCase):
++    def test_query_exact_contract(self):
++        query = build_query(crosswalk(), CLASS, CUTOFF)
++        self.assertEqual(query["taxon_id"], 999999001)
++        self.assertEqual(query["created_d2"], "2026-10-05")
++        self.assertEqual((query["order_by"], query["order"], query["per_page"]), ("id", "asc", 100))
++        self.assertEqual(query["quality_grade"], "research")
++        self.assertEqual(query["photos"], "true")
++
++    def test_crosswalk_required_fields_and_identity(self):
++        for key in crosswalk():
++            entry = crosswalk()
++            del entry[key]
++            if key == "authorship_missing_reason":
++                pass
++            with self.subTest(key=key), self.assertRaises(ContractError):
++                build_query(entry, CLASS, CUTOFF)
++        for key, value in [("scientific_name", "Pothos aureus"), ("namespace", "wikidata"), ("source_taxon_id", True), ("rank", "subspecies"), ("status", "inactive"), ("synonym_of", 9), ("taxonomy_ref_ids", [])]:
++            entry = crosswalk()
++            entry[key] = value
++            with self.subTest(key=key), self.assertRaises(ContractError):
++                build_query(entry, CLASS, CUTOFF)
++
++    def test_protection_never_queries(self):
++        for class_id in ("outra_planta", "imagem_invalida"):
++            with self.assertRaises(ContractError):
++                build_query(crosswalk(), {"class_id": class_id, "kind": "protection"}, CUTOFF)
++
++    def test_cutoff_must_have_timezone(self):
++        with self.assertRaises(ContractError):
++            build_query(crosswalk(), CLASS, "2026-10-05")
++
++    def test_photo_code_alone_never_authorizes(self):
++        obs = observation()
++        result = photo_record(obs["photos"][0], obs)
++        self.assertFalse(result["download_allowed"])
++        self.assertIsNone(result["file_url"])
++        self.assertIn("needs_license_review", result["reasons"])
++        obs["photos"][0]["license_code"] = ["cc-by"]
++        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
++
++    def test_documented_size_mapping_and_individual_evidence(self):
++        obs = observation()
++        result = photo_record(obs["photos"][0], obs, legal())
++        self.assertTrue(result["download_allowed"])
++        self.assertTrue(result["file_url"].endswith("/999999003/original.jpg"))
++        self.assertEqual(result["origin_fidelity"], "provider_original")
++        self.assertFalse(result["camera_original_verified"])
++
++    def test_observation_rights_do_not_inherit_photo_rights(self):
++        obs = observation()
++        obs["license_code"] = "cc-by-nc"
++        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
++
++    def test_legal_proof_must_bind_ids_and_version_author_and_database(self):
++        for field, value in [("photo_id", 9), ("observation_id", 9), ("author", ""), ("licensor", ""), ("credit", ""), ("reviewer", ""), ("database_rights", "unknown")]:
++            proof = legal()
++            proof[field] = value
++            obs = observation()
++            with self.subTest(field=field):
++                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])
++        for field, value in [("version", "3.0"), ("legal_url", "https://creativecommons.org/licenses/by/3.0/"), ("restrictions", ["extra"]), ("evidence_sha256", None), ("source_url", "https://www.inaturalist.org/photos/9")]:
++            proof = legal()
++            proof["photo"][field] = value
++            obs = observation()
++            with self.subTest(field=field):
++                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])
++
++    def test_url_confusion_does_not_generate_original(self):
++        urls = ["http://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com.evil.invalid/photos/999999003/square.jpg", "https://[REDACTED EMAIL]/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com:444/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/9/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/../square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.gif", "https://static.inaturalist.org/photos/999999003/square.jpg"]
++        for url in urls:
++            obs = observation()
++            obs["photos"][0]["url"] = url
++            with self.subTest(url=url):
++                self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
++
++    def test_page_preserves_pending_without_location(self):
++        obs = observation()
++        obs["location"] = "0,0"
++        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
++        self.assertEqual(len(result["candidates"]), 1)
++        self.assertFalse(result["candidates"][0]["download_allowed"])
++        self.assertNotIn("location", result["candidates"][0])
++        self.assertEqual(result["next_id_above"], obs["id"])
++
++    def test_exact_species_and_active_required(self):
++        for key, value in [("id", 999999004), ("name", "Pothos aureus"), ("rank", "subspecies"), ("is_active", False)]:
++            obs = observation()
++            obs["taxon"][key] = value
++            result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
++            self.assertEqual(result["candidates"][0]["taxonomic_confidence"], "conflict")
++            self.assertIn("needs_taxonomic_mapping", result["candidates"][0]["reasons"])
++
++    def test_regressive_duplicate_or_after_cutoff_page_fails(self):
++        for observations in [(observation(), observation()), (observation(999999004), observation()), (dict(observation(), created_at="2026-10-06T00:00:00Z"),)]:
++            with self.assertRaises(ContractError):
++                parse_page(page(*observations), crosswalk(), CLASS, CUTOFF)
++        with self.assertRaises(ContractError):
++            parse_page(page(observation()), crosswalk(), CLASS, CUTOFF, id_above=999999002)
++
++    def test_schema_failures(self):
++        for response in [{}, {"results": []}, dict(page(), per_page=101), dict(page(), page=2), dict(page(), total_results=True), page(dict(observation(), photos=None)), page(dict(observation(), quality_grade="casual"))]:
++            with self.subTest(response=response), self.assertRaises(ContractError):
++                parse_page(response, crosswalk(), CLASS, CUTOFF)
++
++    def test_100_photo_ceiling_with_deferred_accounting(self):
++        obs = observation()
++        obs["photos"] = [dict(obs["photos"][0], id=999999100+i) for i in range(105)]
++        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
++        self.assertEqual(len(result["candidates"]), 100)
++        self.assertEqual(result["deferred_photo_count"], 5)
++
++    def test_duplicate_media_not_inflated(self):
++        obs = observation()
++        obs["photos"].append(copy.deepcopy(obs["photos"][0]))
++        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
++        self.assertEqual(len(result["candidates"]), 1)
++        self.assertEqual(result["duplicate_photo_count"], 1)
++
++
++if __name__ == "__main__":
++    unittest.main()
+diff --git a/scripts/phase1/test_p08_mutation.py b/scripts/phase1/test_p08_mutation.py
+new file mode 100644
+index 0000000..eae0572
+--- /dev/null
++++ b/scripts/phase1/test_p08_mutation.py
+@@ -0,0 +1,145 @@
++"""Selective P08 mutations: five material seams, no global mutation score.
++
++Each focal baseline and mutant runs in a fresh subprocess against a disposable
++source copy. unittest.mock replaces the real public boundary. A shadow call to
++the unchanged boundary confirms the harmful input actually changes behavior;
++mock invocation alone is insufficient. No subprocess may use the network.
++"""
++from contextlib import ExitStack
++import hashlib
++import json
++from pathlib import Path
++import shutil
++import subprocess
++import sys
++import tempfile
++import unittest
++from unittest.mock import patch
++
++
++ROOT = Path(__file__).resolve().parents[2]
++SEAMS = {
++    "bypass_license": ("rights", "test_rights_gate"),
++    "bypass_expert": ("decide", "test_expert_gate"),
++    "ignore_hash_mismatch": ("verify_objects", "test_hash_mismatch"),
++    "advance_cursor_before_commit": ("advance", "test_cursor_gate"),
++    "allow_private_export": ("validate_public", "test_private_export"),
++}
++COPY_FILES = tuple("scripts/phase1/" + name for name in (
++    "recover_p08.py", "test_recover_p08.py", "inaturalist_source.py",
++    "acquire_commons.py", "curate_p07.py", "validate_offline_manifest.py",
++)) + (
++    "docs/phase1/offline-class-manifest.v1.json",
++    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
++)
++
++
++def worker(seam, mode, source):
++    """Return a failing test exit for a killed mutant, never a forged failure."""
++    sys.path.insert(0, str(Path(source)/"scripts/phase1"))
++    import recover_p08 as recovery
++    import test_recover_p08 as contract
++    attribute, focal = SEAMS[seam]
++    owner = recovery.Dataset if attribute in {"verify_objects", "advance"} else recovery
++    original = getattr(owner, attribute)
++    changed = 0
++
++    def replacement(*args, **kwargs):
++        nonlocal changed
++        if attribute in {"rights", "decide"}:
++            forced = "passed" if attribute == "rights" else "approved_for_dataset"
++            try:
++                observed = original(*args, **kwargs)
++            except recovery.RecoveryError:
++                observed = "rejected_by_original"
++            changed += int(observed != forced)
++            return forced
++        try:
++            original(*args, **kwargs)
++        except recovery.RecoveryError as error:
++            # Only the specified risk branch is bypassed. Unexpected errors
++            # must not make a mutant look material or killed for this seam.
++            expected = {"verify_objects": {"object_hash_mismatch", "evidence_hash_mismatch"},
++                        "advance": {"cursor_before_commit"},
++                        "validate_public": {"private_export"}}[attribute]
++            if str(error) not in expected:
++                raise
++            changed += 1
++            if attribute == "advance":
++                dataset, page = args
++                dataset.append("cursor", {"page_id": page["page_id"], "next_cursor": page["next_cursor"]})
++            # Observable no-op validation; the original rejection is suppressed.
++        return None
++
++    with ExitStack() as stack:
++        denied = []
++        for boundary in ("socket.create_connection", "socket.getaddrinfo", "socket.socket.connect", "socket.socket.connect_ex"):
++            denied.append(stack.enter_context(patch(boundary, side_effect=AssertionError("mutation_network_forbidden"))))
++        mocked = None
++        if mode == "mutant":
++            mocked = stack.enter_context(patch.object(owner, attribute, autospec=True, side_effect=replacement))
++        suite = unittest.TestSuite([contract.RecoveryTests(focal)])
++        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
++        report = {"seam": seam, "mode": mode, "tests_run": result.testsRun,
++                  "failures": len(result.failures), "errors": len(result.errors),
++                  "mock_calls": mocked.call_count if mocked is not None else 0,
++                  "material_changes_reached": changed, "network_calls": sum(x.call_count for x in denied),
++                  "source_sha256": hashlib.sha256(Path(recovery.__file__).read_bytes()).hexdigest(),
++                  "tests_sha256": hashlib.sha256(Path(contract.__file__).read_bytes()).hexdigest()}
++    print(json.dumps(report, sort_keys=True))
++    return 0 if result.wasSuccessful() else 1
++
++
++class SelectiveMutationTests(unittest.TestCase):
++    def check_seam(self, seam):
++        with tempfile.TemporaryDirectory(prefix="p08-selective-") as temporary:
++            copied = Path(temporary)/"source"
++            for relative in COPY_FILES:
++                target = copied/relative
++                target.parent.mkdir(parents=True, exist_ok=True)
++                shutil.copyfile(ROOT/relative, target)
++            reports = []
++            for mode in ("baseline", "mutant"):
++                process = subprocess.run(
++                    [sys.executable, "-B", str(Path(__file__).resolve()), "--worker", seam, mode, str(copied)],
++                    cwd=temporary, capture_output=True, text=True, timeout=45,
++                )
++                self.assertIn(process.returncode, (0, 1), process.stderr)
++                report = json.loads(process.stdout)
++                self.assertEqual(report["tests_run"], 1, process.stderr)
++                self.assertEqual(report["errors"], 0, process.stderr)
++                self.assertEqual(report["network_calls"], 0, process.stderr)
++                if mode == "baseline":
++                    self.assertEqual(process.returncode, 0, process.stderr)
++                    self.assertEqual(report["failures"], 0)
++                else:
++                    self.assertEqual(process.returncode, 1, "material mutant survived")
++                    self.assertGreater(report["failures"], 0, process.stderr)
++                    self.assertGreater(report["mock_calls"], 0, "mutated boundary was never called")
++                    self.assertGreater(report["material_changes_reached"], 0, "mutation never changed the approved risk branch")
++                reports.append(report)
++            self.assertEqual(reports[0]["source_sha256"], reports[1]["source_sha256"])
++            self.assertEqual(reports[0]["tests_sha256"], reports[1]["tests_sha256"])
++            print(json.dumps({"selective_mutation": seam, "baseline": reports[0], "mutant": reports[1]}, sort_keys=True))
++        self.assertFalse(copied.exists(), "disposable mutation copy was not removed")
++
++    def test_bypass_license(self):
++        self.check_seam("bypass_license")
++
++    def test_bypass_expert(self):
++        self.check_seam("bypass_expert")
++
++    def test_ignore_hash_mismatch(self):
++        self.check_seam("ignore_hash_mismatch")
++
++    def test_advance_cursor_before_commit(self):
++        self.check_seam("advance_cursor_before_commit")
++
++    def test_allow_private_export(self):
++        self.check_seam("allow_private_export")
++
++
++if __name__ == "__main__":
++    if len(sys.argv) == 5 and sys.argv[1] == "--worker":
++        raise SystemExit(worker(sys.argv[2], sys.argv[3], sys.argv[4]))
++    unittest.main()
+diff --git a/scripts/phase1/test_recover_p08.py b/scripts/phase1/test_recover_p08.py
+new file mode 100644
+index 0000000..aeb8b53
+--- /dev/null
++++ b/scripts/phase1/test_recover_p08.py
+@@ -0,0 +1,692 @@
++"""Public P08 boundaries, synthetic data only; no network in these tests."""
++import copy
++from contextlib import ExitStack
++import io
++import json
++import os
++from pathlib import Path
++import subprocess
++import sys
++import tempfile
++import unittest
++from unittest.mock import patch
++from PIL import Image
++import recover_p08 as r
++
++
++def image_bytes(fmt='JPEG'):
++    out = io.BytesIO()
++    im = Image.new('RGB', (240, 240), (100, 160, 40))
++    exif = Image.Exif(); exif[270] = 'synthetic-private-metadata'; exif[274] = 6
++    im.save(out, format=fmt, exif=exif)
++    return out.getvalue()
++
++
++def candidate(raw=None):
++    raw = raw or image_bytes()
++    return {'source': 'commons', 'media_id': '123', 'class_ids': ['species_01'],
++            'file_url': 'https://upload.wikimedia.org/a/test.jpg',
++            'source_page_url': 'https://commons.wikimedia.org/wiki/File:Test.jpg',
++            'mime': 'image/jpeg', 'declared_size': len(raw), 'source_sha1': __import__('hashlib').sha1(raw).hexdigest(),
++            'author': 'Synthetic fixture', 'license_id': 'cc-by-4.0', 'license_name': 'CC BY 4.0',
++            'license_url': 'https://creativecommons.org/licenses/by/4.0/', 'restrictions': '',
++            'credit': 'Synthetic fixture', 'attribution': 'Synthetic fixture', 'evidence_sha256': 'a'*64,
++            'rights_consistent': True, 'database_rights': 'passed', 'mapping': None,
++            'observation_id': None, 'origin_fidelity': 'provider_original', 'camera_original_verified': False}
++
++
++class DatasetCase:
++    def setUp(self):
++        self.tmp = tempfile.TemporaryDirectory()
++        self.addCleanup(self.tmp.cleanup)
++        self.root = Path(self.tmp.name)/'synthetic'
++        self.config = r.default_config(offline=True)
++
++    def open(self):
++        return r.Dataset(self.root, self.config, offline=True)
++
++
++class RecoveryTests(DatasetCase, unittest.TestCase):
++
++    def test_rights_gate(self):
++        c = candidate()
++        self.assertEqual(r.rights(c), 'passed')
++        for key, val in [('license_url', 'https://creativecommons.org/licenses/by/3.0/'),
++                         ('license_name','CC BY-SA 4.0'),('license_id','cc-by'),
++                         ('author','unknown'),('restrictions','extra'),('rights_consistent',False),
++                         ('evidence_sha256',None),('database_rights','pending')]:
++            with self.subTest(key=key):
++                bad=copy.deepcopy(c); bad[key]=val
++                self.assertNotEqual(r.rights(bad),'passed')
++
++    def test_expert_gate(self):
++        c = candidate(); c.update(candidate_id=r.candidate_id(c),original_sha256='b'*64,sanitized_sha256='c'*64,
++                                technical={'decode':'ok'},pairs=[],state='quarantined')
++        d = {'candidate_id':c['candidate_id'], 'original_sha256':'b'*64,'sanitized_sha256':'c'*64,
++             'evidence_digest':r.review_digest(c),'reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z',
++             'authority':'human','quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
++             'expert_confirmation':False,'qualification':'','botanical_evidence':'','mapping':None,
++             'rationale':'Synthetic decision'}
++        self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
++        for flag in [None, 'true',1]:
++            d['expert_confirmation']=flag
++            self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
++        d['authority']='agent_proposal'
++        with self.assertRaises(r.RecoveryError): r.decide(c,d)
++
++    def test_original_sanitization_resume(self):
++        raw=image_bytes(); c=candidate(raw)
++        with self.open() as ds:
++            rec=ds.ingest(c,lambda _:raw)
++            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)
++            self.assertNotEqual(rec['original_sha256'],rec['sanitized_sha256'])
++            with Image.open(self.root/rec['sanitized_path']) as im:
++                self.assertFalse(im.getexif()); self.assertNotIn('xmp',im.info)
++            before=r.tree_fingerprint(self.root)
++            ds.ingest(c,lambda _:self.fail('repeat download'))
++            self.assertEqual(before,r.tree_fingerprint(self.root))
++        with self.open() as ds:
++            self.assertEqual(len(ds.records()),1)
++            before=r.tree_fingerprint(self.root)
++            ds.ingest(c,lambda _:self.fail('restart download'))
++            self.assertEqual(before,r.tree_fingerprint(self.root))
++            self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')
++
++    def test_hash_mismatch(self):
++        with self.open() as ds:
++            rec=ds.ingest(candidate(),lambda _:image_bytes())
++        (self.root/rec['original_path']).write_bytes(b'corrupt')
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++
++    def test_journal_partial(self):
++        with self.open(): pass
++        with (self.root/'journal.jsonl').open('ab') as f: f.write(b'{')
++        before=(self.root/'journal.jsonl').read_bytes()
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++        self.assertEqual(before,(self.root/'journal.jsonl').read_bytes())
++
++    def test_journal_chain(self):
++        with self.open() as ds: ds.append('test',{'x':1})
++        p=self.root/'journal.jsonl'; raw=p.read_bytes().replace(b'"x":1',b'"x":2');p.write_bytes(raw)
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++
++    def test_lock(self):
++        with self.open():
++            with self.assertRaises(r.RecoveryError):
++                with self.open(): pass
++
++    def test_changed_config(self):
++        with self.open(): pass
++        self.config['limits']['pages']=1
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++
++    def test_symlink(self):
++        self.root.symlink_to(Path(self.tmp.name),target_is_directory=True)
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++
++    def test_cursor_gate(self):
++        with self.open() as ds:
++            page=ds.save_page('commons','species_01',0,[candidate()],None)
++            with self.assertRaises(r.RecoveryError): ds.advance(page)
++            ds.ingest(candidate(),lambda _:image_bytes())
++            ds.advance(page)
++            before=r.tree_fingerprint(self.root);ds.advance(page)
++            self.assertEqual(before,r.tree_fingerprint(self.root))
++
++    def test_private_export(self):
++        with self.open() as ds: value=ds.summary()
++        self.assertEqual(len(value['coverage']),28)
++        self.assertFalse(value['training_authorized'])
++        self.assertEqual(value['usable'],0)
++        r.validate_public(value)
++        for key in ['author','url','gps','free_text']:
++            bad=copy.deepcopy(value);bad[key]='PRIVATE'
++            with self.assertRaises(r.RecoveryError):r.validate_public(bad)
++        bad=copy.deepcopy(value);bad['coverage'][0]['author']='PRIVATE'
++        with self.assertRaises(r.RecoveryError):r.validate_public(bad)
++
++    def test_download_budget_restart(self):
++        self.config['limits']['transfers']=1
++        with self.open() as ds:
++            ds.ingest(candidate(),lambda _:image_bytes())
++        with self.open() as ds:
++            c=candidate();c['media_id']='124'
++            rec=ds.ingest(c,lambda _:self.fail('budget exceeded'))
++            self.assertEqual(rec['state'],'deferred_budget')
++
++    def test_crash_boundaries(self):
++        for stage in ['intention','received','original','sanitized','committed']:
++            with self.subTest(stage=stage),tempfile.TemporaryDirectory() as td:
++                root=Path(td)/'synthetic'
++                with r.Dataset(root,self.config,offline=True) as ds:
++                    def crash(point):
++                        if point==stage: raise RuntimeError('crash')
++                    with self.assertRaises(RuntimeError):ds.ingest(candidate(),lambda _:image_bytes(),crash=crash)
++                with r.Dataset(root,self.config,offline=True) as ds:
++                    rec=ds.ingest(candidate(),lambda _:image_bytes())
++                    self.assertTrue((root/rec['original_path']).exists())
++                    self.assertEqual(len(ds.records()),1)
++                    self.assertEqual(rec['state'],'needs_human_review')
++
++    def test_format_invalid_preserved(self):
++        raw=b'not image';c=candidate(raw)
++        with self.open() as ds:
++            rec=ds.ingest(c,lambda _:raw)
++            self.assertEqual(rec['state'],'rejected_format')
++            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)
++
++    def test_symlink_object(self):
++        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
++        p=self.root/rec['original_path'];raw=p.read_bytes();p.unlink()
++        q=Path(self.tmp.name)/'fixture';q.write_bytes(raw);p.symlink_to(q)
++        with self.assertRaises(r.RecoveryError):
++            with self.open(): pass
++
++    def test_url_boundaries(self):
++        good='https://upload.wikimedia.org/a/a.jpg'
++        self.assertEqual(r.safe_url(good,'commons',True),good)
++        for u in ['http://upload.wikimedia.org/a.jpg','https://upload.wikimedia.org:444/a.jpg',
++                  'https://[REDACTED EMAIL]/a.jpg','https://evil.invalid/a.jpg',
++                  'https://upload.wikimedia.org/%2e%2e/a.jpg','https://upload.wikimedia.org/a.jpg#x']:
++            with self.subTest(u=u),self.assertRaises(r.RecoveryError):r.safe_url(u,'commons',True)
++        with patch('socket.getaddrinfo',return_value=[(2,1,6,'',('127.0.0.1',443))]):
++            with self.assertRaises(r.RecoveryError):r.public_addresses('upload.wikimedia.org')
++
++    def test_metadata_and_dimensions(self):
++        for fmt in ['JPEG','PNG']:
++            raw=image_bytes(fmt);suffix='jpg' if fmt=='JPEG' else 'png'
++            clean,ext=r.sanitize(raw,'https://upload.wikimedia.org/a.'+suffix,'image/'+('jpeg' if fmt=='JPEG' else 'png'))
++            with Image.open(io.BytesIO(clean)) as im:
++                self.assertFalse(im.getexif());self.assertEqual(im.mode,'RGB')
++        with self.assertRaises(r.RecoveryError):r.sanitize(b'', 'https://upload.wikimedia.org/a.jpg','image/jpeg')
++        with self.assertRaises(r.RecoveryError):r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.jpg','image/jpeg')
++
++    def test_cli_invalid_safe(self):
++        p=subprocess.run([sys.executable,'-B',str(r.Path(r.__file__)),'verify','--output',str(self.root),'--p07-source',str(self.root)],capture_output=True,text=True)
++        self.assertEqual(p.returncode,2)
++        self.assertNotIn(str(self.root),p.stderr)
++
++class ExtendedTests(DatasetCase, unittest.TestCase):
++    """Risk neighbors through durable acquisition and transport boundaries."""
++    def test_retry_transfer(self):
++        with self.open() as ds:
++            def fail(_):raise r.RecoveryError('timeout')
++            self.assertEqual(ds.ingest(candidate(),fail)['state'],'transfer_failed')
++        with self.open() as ds:
++            self.assertEqual(ds.ingest(candidate(),lambda _:image_bytes())['state'],'needs_human_review')
++            self.assertEqual(len(ds.select('intention')),2)
++
++    def test_zero_round_replay(self):
++        with self.open() as ds:
++            self.assertEqual(r.acquire(ds,{}),0)
++            ds.project();before=r.tree_fingerprint(self.root)
++            self.assertEqual(r.acquire(ds,{}),0)
++            self.assertEqual(before,r.tree_fingerprint(self.root))
++            coverage=ds.summary()['coverage']
++            self.assertEqual(sum(x['status']=='no_crosswalk' for x in coverage),12)
++            self.assertEqual(sum(x['status']=='protection_not_queried' for x in coverage),4)
++
++    def test_same_object_class_conflict(self):
++        with self.open() as ds:
++            ds.ingest(candidate(),lambda _:image_bytes())
++            c=candidate();c['class_ids']=['species_02']
++            rec=ds.ingest(c,lambda _:self.fail('duplicate download'))
++            self.assertEqual(rec['class_ids'],['species_01','species_02'])
++            self.assertEqual(rec['state'],'needs_botanical_review')
++            self.assertEqual(len(ds.records()),1)
++
++    def test_fsync_failure_preserves_source(self):
++        with self.open() as ds:
++            with patch.object(r.os,'fsync',side_effect=OSError('synthetic full disk')):
++                with self.assertRaises(OSError):ds.ingest(candidate(),lambda _:self.fail('before durable intent'))
++
++    def test_missing_object(self):
++        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
++        (self.root/rec['sanitized_path']).unlink()
++        with self.assertRaises(OSError):
++            with self.open():pass
++
++    def test_png_pixels_and_metrics(self):
++        clean,_=r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.png','image/png')
++        tech=r.technical(clean)
++        self.assertEqual(tech['format'],'PNG')
++        self.assertEqual(len(tech['dhash64']),16)
++        for mean,expected in [(39,True),(40,False),(215,False),(216,True)]:
++            flags=r.flags_for(224,224,mean,0,0,100)
++            self.assertEqual('dark_mean' in flags or 'bright_mean' in flags,expected)
++        self.assertIn('dark_fraction',r.flags_for(224,224,100,.25,0,100))
++        self.assertNotIn('small_dimension',r.flags_for(224,224,100,0,0,100))
++        self.assertIn('small_dimension',r.flags_for(223,224,100,0,0,100))
++        self.assertNotIn('extreme_aspect',r.flags_for(224,672,100,0,0,100))
++        self.assertIn('extreme_aspect',r.flags_for(224,673,100,0,0,100))
++        self.assertIn('low_laplacian_variance',r.flags_for(224,224,100,0,0,99))
++
++    def test_retry_after(self):
++        self.assertEqual(r.retry_delay('120',0),120)
++        self.assertEqual(r.retry_delay(None,0),2)
++        self.assertEqual(r.retry_delay(None,1),4)
++        self.assertEqual(r.retry_delay('Thu, 01 Jan 1970 00:02:00 GMT',0,clock=lambda:0),120)
++        with self.assertRaises(r.RecoveryError):r.retry_delay('invalid',0)
++
++    def test_offline_transport_never_network(self):
++        with self.open() as ds,patch.object(r.socket,'create_connection',side_effect=AssertionError('network')):
++            with self.assertRaises(r.RecoveryError):r.Transport(ds).get('https://commons.wikimedia.org/w/api.php','commons')
++
++    def test_final_positive_authority_and_mapping(self):
++        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
++        cls=r.canonical()[0]
++        d={'authority':'human','reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
++           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
++           'evidence_digest':r.review_digest(c),'expert_confirmation':True,'qualification':'synthetic botanist',
++           'botanical_evidence':'a'*64,'quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
++           'mapping':{'confidence':'human_validated','source_taxon_id':'fixture','namespace':'fixture','evidence_sha256':'a'*64,
++                      'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],'rank':'species','status':'accepted',
++                      'taxonomy_ref_ids':cls['taxonomy_ref_ids']},
++           'visual':dict.fromkeys(['photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'],True),
++           'privacy_checks':dict.fromkeys(['people','faces','plates','residences','screens_documents','sensitive_location'],'absent')}
++        self.assertEqual(r.decide(c,d),'approved_for_dataset')
++        for key in ['scientific_name','class_id','taxonomy_ref_ids','namespace']:
++            bad=copy.deepcopy(d);bad['mapping'][key]=None
++            self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')
++        for gate in ['quality','privacy','botanical','duplicates']:
++            for value in [None,True,'unknown','pending']:
++                bad=copy.deepcopy(d);bad[gate]=value
++                self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')
++
++
++class FakeResponse:
++    def __init__(self, status=200, body=b'{}', headers=None, read_error=None):
++        self.status = status
++        self.body = io.BytesIO(body)
++        self.headers = headers or {}
++        self.read_error = read_error
++        self.read_calls = 0
++
++    def getheader(self, name, default=None):
++        return self.headers.get(name, default)
++
++    def read(self, count):
++        self.read_calls += 1
++        if self.read_error and self.read_calls > 1:
++            raise self.read_error
++        return self.body.read(count)
++
++
++class FakeConnection:
++    def __init__(self, result):
++        self.result = result
++        self.requests = []
++        self.closed = False
++
++    def request(self, *args, **kwargs):
++        self.requests.append((args, kwargs))
++
++    def getresponse(self):
++        if isinstance(self.result, BaseException):
++            raise self.result
++        return self.result
++
++    def close(self):
++        self.closed = True
++
++
++class TransportTests(DatasetCase, unittest.TestCase):
++    api = 'https://commons.wikimedia.org/w/api.php'
++    media = 'https://upload.wikimedia.org/a/synthetic.jpg'
++
++    def transport(self, ds, responses):
++        stack = ExitStack()
++        self.addCleanup(stack.close)
++        connections = [FakeConnection(response) for response in responses]
++        factory = stack.enter_context(patch.object(r, 'PinnedHTTPS', side_effect=connections))
++        stack.enter_context(patch.object(ds, 'offline', False))
++        stack.enter_context(patch.object(r.socket, 'create_connection', side_effect=AssertionError('network_forbidden')))
++        stack.enter_context(patch.object(r.socket, 'getaddrinfo', side_effect=AssertionError('network_forbidden')))
++        clock = [1000.0]
++        stack.enter_context(patch.object(r.time, 'time', side_effect=lambda: clock[0]))
++        stack.enter_context(patch.object(r.time, 'monotonic', side_effect=lambda: clock[0]))
++        sleeps = stack.enter_context(patch.object(r.time, 'sleep', side_effect=lambda value: clock.__setitem__(0, clock[0]+value)))
++        stack.enter_context(patch.object(r.shutil, 'disk_usage', return_value=type('Disk', (), {'free': 4*1024**3})()))
++        return r.Transport(ds), factory, connections, sleeps
++
++    def test_403_never_retries(self):
++        with self.open() as ds:
++            transport, factory, connections, sleeps = self.transport(ds, [FakeResponse(403)])
++            with self.assertRaisesRegex(r.RecoveryError, 'http_403'):
++                transport.get(self.api, 'commons')
++            self.assertEqual(factory.call_count, 1)
++            self.assertEqual(len(ds.select('request')), 1)
++            self.assertEqual(ds.select('response')[0]['status'], 403)
++            self.assertTrue(connections[0].closed)
++            sleeps.assert_not_called()
++
++    def test_429_wait_above_budget_persists_resume_after(self):
++        with self.open() as ds:
++            transport, factory, _, sleeps = self.transport(ds, [FakeResponse(429, headers={'Retry-After': '120'})])
++            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
++                transport.get(self.api, 'commons')
++            self.assertEqual(ds.select('resume_after')[0]['epoch'], 1120)
++            self.assertEqual(factory.call_count, 1)
++            sleeps.assert_not_called()
++            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
++                transport.get(self.api, 'commons')
++            self.assertEqual(factory.call_count, 1)
++            self.assertEqual(len(ds.select('request')), 1)
++
++    def test_timeout_three_attempts_and_cumulative_quota(self):
++        self.config['limits']['requests'] = 3
++        with self.open() as ds:
++            transport, factory, connections, sleeps = self.transport(ds, [TimeoutError('synthetic') for _ in range(3)])
++            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
++                transport.get(self.api, 'commons')
++            self.assertEqual(factory.call_count, 3)
++            self.assertEqual(len(ds.select('request')), 3)
++            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
++            self.assertEqual([call.args[0] for call in sleeps.call_args_list], [2, 4])
++            self.assertTrue(all(connection.closed for connection in connections))
++        with self.open() as ds:
++            transport, factory, _, _ = self.transport(ds, [])
++            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
++                transport.get(self.api, 'commons')
++            factory.assert_not_called()
++
++    def test_request_reservation_survives_crash_without_response(self):
++        self.config['limits']['requests'] = 1
++        with self.open() as ds:
++            ds.append('request', {'request_id': 'synthetic-interrupted', 'source': 'commons', 'media': True,
++                                  'reserved': 16, 'epoch': 1000, 'url': self.media})
++        with self.open() as ds:
++            transport, factory, _, _ = self.transport(ds, [])
++            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
++                transport.get(self.media, 'commons', True)
++            factory.assert_not_called()
++
++    def test_malicious_redirect_does_not_connect_to_destination(self):
++        with self.open() as ds:
++            transport, factory, _, _ = self.transport(ds, [FakeResponse(302, headers={'Location': 'https://127.0.0.1/a'})])
++            with self.assertRaisesRegex(r.RecoveryError, 'unsafe_url'):
++                transport.get(self.api, 'commons')
++            self.assertEqual(factory.call_count, 1)
++            self.assertEqual(ds.select('response')[0]['status'], 302)
++
++    def test_public_hostname_resolving_private_ip_is_rejected_before_connect(self):
++        for ip in ['127.0.0.1', '10.0.0.1', '169.254.169.254', '::1', 'fc00::1']:
++            with self.subTest(ip=ip), patch.object(r.socket, 'getaddrinfo', return_value=[(2, 1, 6, '', (ip, 443))]), patch.object(r.socket, 'create_connection', side_effect=AssertionError('must_not_connect')) as connect:
++                with self.assertRaisesRegex(r.RecoveryError, 'nonpublic_address'):
++                    r.PinnedHTTPS('upload.wikimedia.org', timeout=20).connect()
++                connect.assert_not_called()
++
++    def test_oversized_response_counts_received_bytes_and_failure(self):
++        self.config['limits']['file_bytes'] = 8
++        self.config['limits']['media_bytes'] = 16
++        with self.open() as ds:
++            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'123456789')])
++            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
++                transport.get(self.media, 'commons', True)
++            self.assertEqual(ds.select('response')[0]['received'], 9)
++            self.assertEqual(ds.select('response')[0]['code'], 'response_size')
++            with self.assertRaisesRegex(r.RecoveryError, 'media_budget'):
++                transport.get(self.media, 'commons', True)
++            self.assertEqual(factory.call_count, 1)
++
++    def test_partial_timeout_counts_bytes_on_every_retry(self):
++        self.config['limits']['file_bytes'] = 16
++        with self.open() as ds:
++            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'1234', read_error=TimeoutError('synthetic')) for _ in range(3)])
++            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
++                transport.get(self.media, 'commons', True)
++            self.assertEqual(factory.call_count, 3)
++            self.assertEqual([e['received'] for e in ds.select('response')], [4, 4, 4])
++            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
++
++    def test_declared_oversize_rejected_before_body(self):
++        self.config['limits']['file_bytes'] = 8
++        response = FakeResponse(body=b'123456789', headers={'Content-Length': '9'})
++        with self.open() as ds:
++            transport, _, _, _ = self.transport(ds, [response])
++            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
++                transport.get(self.media, 'commons', True)
++            self.assertEqual(response.read_calls, 0)
++            self.assertEqual(ds.select('response')[0]['received'], 0)
++
++
++class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
++    def test_fake_commons_cli_snapshot_ingest_and_restart(self):
++        raw = image_bytes()
++        c = candidate(raw)
++        media = Path(self.tmp.name)/'media'
++        media.mkdir()
++        (media/'123').write_bytes(raw)
++        fields = {'Artist': 'Synthetic fixture', 'License': 'cc-by-4.0', 'LicenseShortName': 'CC BY 4.0',
++                  'LicenseUrl': c['license_url'], 'Credit': 'Own work', 'Attribution': 'Synthetic fixture'}
++        page = {'pageid': 123, 'ns': 6, 'title': 'File:Synthetic.jpg', 'revisions': [{'revid': 456}],
++                'imageinfo': [{'url': c['file_url'], 'descriptionurl': c['source_page_url'],
++                               'mime': c['mime'], 'size': len(raw), 'width': 240, 'height': 240,
++                               'sha1': c['source_sha1'], 'timestamp': '2026-10-04T00:00:00Z',
++                               'extmetadata': {key: {'value': value} for key, value in fields.items()}}]}
++        fixture = {'species_01': {'0': {'query': {'pages': [page]}, 'continue': {'continue': 'gsroffset||', 'gsroffset': 10}},
++                                  '10': {'batchcomplete': True}}, 'synthetic_media': str(media)}
++        fixture_path = Path(self.tmp.name)/'fixture.json'
++        fixture_path.write_bytes(r.encode(fixture))
++        self.config['source_contracts']['commons'] = {'database_rights': 'passed'}
++        config_path = Path(self.tmp.name)/'run.json'
++        config_path.write_bytes(r.encode(self.config))
++        script = ('import sys\nfrom unittest.mock import patch\n'
++                  'sys.path.insert(0, sys.argv.pop(1))\nimport recover_p08\n'
++                  'with patch("socket.create_connection", side_effect=AssertionError("network_forbidden")), patch("socket.getaddrinfo", side_effect=AssertionError("network_forbidden")):\n'
++                  ' raise SystemExit(recover_p08.main(sys.argv[1:]))\n')
++        argv = [sys.executable, '-B', '-c', script, str(Path(r.__file__).parent), 'acquire', '--config', str(config_path),
++                '--output', str(self.root), '--offline-fixture', str(fixture_path)]
++        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
++        self.assertEqual(process.returncode, 0, process.stderr)
++        self.assertEqual(json.loads(process.stdout)['status'], 'passed')
++        with self.open() as ds:
++            record = ds.records()[0]
++            self.assertEqual(len(ds.records()), 1)
++            self.assertEqual((self.root/record['original_path']).read_bytes(), raw)
++            self.assertEqual(record['state'], 'needs_human_review')
++            self.assertEqual(len(ds.select('intention')), 1)
++            self.assertEqual(len(ds.select('source_status')), 28)
++            for event in ds.select('evidence'):
++                self.assertEqual(r.sha((self.root/event['path']).read_bytes()), event['sha256'])
++            pages = [p for p in ds.select('page') if p['class_id'] == 'species_01']
++            self.assertEqual([p['cursor'] for p in pages], [0, 10])
++            kinds = [event['type'] for event in ds.events]
++            self.assertLess(kinds.index('page'), kinds.index('intention'))
++            self.assertLess(kinds.index('committed'), kinds.index('cursor'))
++        before = r.tree_fingerprint(self.root)
++        (media/'123').unlink()  # A repeated execution must use the durable objects.
++        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
++        self.assertEqual(process.returncode, 0, process.stderr)
++        self.assertEqual(before, r.tree_fingerprint(self.root))
++
++
++class ContinuationProofs(DatasetCase, unittest.TestCase):
++    def test_inspect_html_identical_after_journal_reload(self):
++        with self.open() as ds:
++            ds.ingest(candidate(),lambda _:image_bytes())
++            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
++        before=r.tree_fingerprint(self.root)
++        with self.open() as ds:
++            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
++        self.assertEqual(before,r.tree_fingerprint(self.root))
++
++    def test_exact_projection_predecessor_is_journaled_without_changing_config(self):
++        self.config['code_sha256']['recover_p08.py']=r.HTML_ORDER_PREDECESSOR
++        with self.open() as ds:
++            self.assertEqual(len(ds.select('code_compatibility')),1)
++            self.assertEqual(ds.select('code_compatibility')[0]['to'],r.fingerprint())
++        before=r.tree_fingerprint(self.root)
++        with self.open() as ds:self.assertEqual(len(ds.select('code_compatibility')),1)
++        self.assertEqual(before,r.tree_fingerprint(self.root))
++        self.config['code_sha256']['inaturalist_source.py']='0'*64
++        with self.assertRaisesRegex(r.RecoveryError,'config_fingerprint'):
++            with self.open():pass
++
++    def test_full_round_retries_transient_media_without_requery(self):
++        c=candidate()
++        with self.open() as ds:
++            ds.save_page('commons','species_01',0,[c],None)
++            def fail(_):raise r.RecoveryError('timeout')
++            ds.ingest(c,fail);ds.advance(ds.select('page')[0])
++            ds.append('source_failure',{'source':'commons','class_id':'species_01','code':'timeout'})
++            ds.append('source_status',{'source':'commons','class_id':'species_01','status':'source_blocked'})
++        media=Path(self.tmp.name)/'media';media.mkdir();(media/'123').write_bytes(image_bytes())
++        with self.open() as ds:
++            self.assertEqual(r.acquire(ds,{'synthetic_media':str(media)}),0)
++            self.assertEqual(ds.records()[0]['state'],'needs_human_review')
++            self.assertEqual(len(ds.select('intention')),2)
++            before=r.tree_fingerprint(self.root)
++            self.assertEqual(r.acquire(ds,{}),0)
++            self.assertEqual(before,r.tree_fingerprint(self.root))
++
++    def test_round_marks_failed_media_retryable_instead_of_exhausted(self):
++        with self.open() as ds:
++            ds.save_page('commons','species_01',0,[candidate()],None)
++            with patch.object(r,'read',side_effect=r.RecoveryError('timeout')):
++                # Only the media loader uses read during this cached synthetic page.
++                with patch.object(r,'canonical',return_value=[{'class_id':'species_01','kind':'species'}]), patch.object(r,'validate_public'):
++                    self.assertEqual(r.acquire(ds,{'synthetic_media':self.tmp.name}),1)
++            self.assertEqual(ds.select('source_status')[0]['status'],'source_blocked')
++            self.assertEqual(ds.select('source_failure')[0]['code'],'timeout')
++
++    def test_lock_in_other_process_precedes_network(self):
++        script='''import sys
++from unittest.mock import patch
++sys.path.insert(0,sys.argv[1])
++import recover_p08 as r
++c=r.load(r.read(r.Path(sys.argv[2])/'config.json'))
++with patch('socket.create_connection',side_effect=AssertionError('network')):
++ try:
++  with r.Dataset(sys.argv[2],c,offline=True):raise AssertionError('concurrent writer')
++ except r.RecoveryError as e:
++  assert str(e)=='writer_locked'
++'''
++        with self.open():
++            p=subprocess.run([sys.executable,'-B','-c',script,str(Path(r.__file__).parent),str(self.root)],capture_output=True,text=True)
++            self.assertEqual(p.returncode,0,p.stderr)
++
++    def test_missing_and_changed_taxonomic_evidence_blocks_finalization(self):
++        with self.open() as ds:
++            c=ds.ingest(candidate(),lambda _:image_bytes())
++            # Mock only the pure decision to isolate the durable evidence gate.
++            inspection={'p07_images':17,'records':[c]}
++            r.persist(ds.path('inspection.json'),r.encode(inspection))
++            r.persist(ds.path('Attributions.jsonl'),r.encode(c))
++            r.persist(ds.path('evidence/map'),b'map')
++            r.persist(ds.path('evidence/botanical'),b'botanical')
++            d={'candidate_id':c['candidate_id'],'mapping':{'evidence_path':'evidence/map','evidence_sha256':r.sha(b'map')},
++               'botanical_evidence_path':'evidence/botanical','botanical_evidence':r.sha(b'botanical')}
++            file=Path(self.tmp.name)/'decision.json'
++            file.write_bytes(r.encode({'authority':'human','decisions':[d]}))
++            with patch.object(r,'decide',return_value='approved_for_dataset'):
++                r.persist(ds.path('evidence/map'),b'changed')
++                with self.assertRaisesRegex(r.RecoveryError,'mapping_evidence_hash'):r.finalize(ds,file)
++                self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')
++                r.persist(ds.path('evidence/map'),b'map')
++                r.persist(ds.path('evidence/botanical'),b'changed')
++                with self.assertRaisesRegex(r.RecoveryError,'botanical_evidence_hash'):r.finalize(ds,file)
++                r.persist(ds.path('evidence/botanical'),b'botanical')
++                r.finalize(ds,file)
++                before=r.tree_fingerprint(self.root);r.finalize(ds,file)
++                self.assertEqual(before,r.tree_fingerprint(self.root))
++
++    def test_decision_stale_after_taxonomy_or_class_change(self):
++        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
++        d={'authority':'human','reviewer':'Synthetic','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
++           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
++           'evidence_digest':r.review_digest(c)}
++        for key,value in [('mapping',{'source_taxon_id':123}),('class_ids',['species_02']),('author','Changed')]:
++            changed=copy.deepcopy(c);changed[key]=value
++            with self.assertRaisesRegex(r.RecoveryError,'stale_decision'):r.decide(changed,d)
++
++    def test_acceptance_binds_all_final_files(self):
++        with self.open() as ds:
++            r.acquire(ds,{})
++            for name in ['inspection.json','Attributions.jsonl','NOTICE.md','review.html']:
++                r.persist(ds.path(name),b'{}\n')
++            files={str(p.relative_to(self.root)):r.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file() and p.name!='.lock'}
++            manifest=r.encode({'files':files});r.persist(ds.path('final-manifest.json'),manifest)
++            acceptance=Path(self.tmp.name)/'acceptance.json'
++            acceptance.write_bytes(r.encode({'decision':'accepted','authority':'human','reviewer':'Synthetic',
++                  'reviewed_at':'2026-10-05T00:00:00Z','manifest_sha256':r.sha(manifest),'training_authorized':False}))
++            with patch.object(r,'historical',return_value=({},[])):
++                self.assertEqual(r.verify(ds,self.root,acceptance),0)
++                r.persist(ds.path('new-unbound-file'),b'x')
++                with self.assertRaisesRegex(r.RecoveryError,'acceptance_coverage_or_bytes'):r.verify(ds,self.root,acceptance)
++
++    def test_duplicate_comparison_against_17_with_boundary_distances(self):
++        with self.open() as ds:
++            rec=ds.ingest(candidate(),lambda _:image_bytes())
++            h=int(rec['technical']['dhash64'],16)
++            prior=[{'candidate_id':'Q'+str(i),'sanitized_sha256':'f'*64,'original_sha256':None,'observation_id':None,
++                    'technical':{'dhash64':format(h^((1<<n)-1),'016x')}} for i,n in enumerate([6,7,10,11]+[20]*13)]
++            with patch.object(r,'historical',return_value=({},prior)):
++                report=r.inspect(ds,self.root)
++                self.assertEqual(len(report['pairs']),17)
++                self.assertEqual([p['signal'] for p in report['pairs'][:4]],['near_duplicate','borderline','borderline','no_algorithmic_signal'])
++                before=r.tree_fingerprint(self.root);r.inspect(ds,self.root)
++                self.assertEqual(before,r.tree_fingerprint(self.root))
++                prior[0]['sanitized_sha256']=rec['sanitized_sha256']
++                r.inspect(ds,self.root)
++                self.assertEqual(ds.records()[0]['state'],'rejected_duplicate')
++                self.assertTrue(ds.path(rec['original_path']).exists())
++
++    def test_bad_schema_and_regressive_page(self):
++        with self.assertRaises(r.RecoveryError):r.commons_page({},r.canonical()[0],'a'*64,self.config)
++        with self.open() as ds:
++            with self.assertRaisesRegex(r.RecoveryError,'cursor_regression'):ds.save_page('commons','species_01',10,[],10)
++            for i in range(10):ds.save_page('commons','species_01',i*10,[],None)
++            with self.assertRaisesRegex(r.RecoveryError,'page_budget'):ds.save_page('commons','species_01',100,[],None)
++
++    def test_unsupported_media_classified_without_transfer(self):
++        with self.open() as ds:
++            c=candidate();c['file_url']='https://upload.wikimedia.org/a/a.svg'
++            self.assertEqual(ds.ingest(c,lambda _:self.fail('unsupported media downloaded'))['state'],'rejected_format')
++            self.assertEqual(ds.select('intention'),[])
++
++
++class ExtraTransportProofs(DatasetCase, unittest.TestCase):
++    transport=TransportTests.transport
++    api=TransportTests.api
++    media=TransportTests.media
++    def test_retryable_http_and_maxlag(self):
++        for status,body in [(429,b''),(500,b''),(502,b''),(503,b''),(504,b''),(200,b'{"error":{"code":"maxlag"}}')]:
++            with self.subTest(status=status),tempfile.TemporaryDirectory() as td:
++                with r.Dataset(Path(td)/'synthetic',self.config,offline=True) as ds:
++                    transport,factory,_,sleeps=self.transport(ds,[FakeResponse(status,body,{'Retry-After':'2'}),FakeResponse()])
++                    self.assertEqual(transport.get(self.api,'commons'),b'{}')
++                    self.assertEqual(factory.call_count,2)
++                    self.assertEqual(ds.select('response')[-1]['code'],'ok')
++                    self.assertEqual(sleeps.call_args_list[0].args,(2,))
++
++    def test_hour_and_media_reservations_survive_restart(self):
++        for limit,reason in [('hour_bytes','hour_budget'),('media_bytes','media_budget')]:
++            with self.subTest(limit=limit),tempfile.TemporaryDirectory() as td:
++                config=copy.deepcopy(self.config);config['limits']['file_bytes']=8;config['limits'][limit]=12
++                root=Path(td)/'synthetic'
++                with r.Dataset(root,config,offline=True) as ds:
++                    ds.append('request',{'request_id':'interrupted','source':'commons','media':True,'reserved':8,'epoch':1000})
++                with r.Dataset(root,config,offline=True) as ds:
++                    transport,factory,_,_=self.transport(ds,[])
++                    with self.assertRaisesRegex(r.RecoveryError,reason):transport.get(self.media,'commons',True)
++                    factory.assert_not_called()
++
++    def test_retry_after_http_date_and_cancelled_request_accounting(self):
++        with self.open() as ds:
++            transport,factory,_,_=self.transport(ds,[FakeResponse(503,headers={'Retry-After':'Thu, 01 Jan 1970 00:20:00 GMT'})])
++            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
++            self.assertEqual(ds.select('resume_after')[0]['epoch'],1200)
++        with self.open() as ds:
++            transport,factory,_,_=self.transport(ds,[])
++            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
++            factory.assert_not_called()
++
++
++if __name__ == '__main__':
++    unittest.main()
+```
diff --git a/artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt b/artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt b/artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt
new file mode 100644
index 0000000..818c419
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt
@@ -0,0 +1,4 @@
+{
+  "method_version": 2,
+  "valid": true
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-digest.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-digest.txt
new file mode 100644
index 0000000..b51a2f5
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-digest.txt
@@ -0,0 +1 @@
+d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d  artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256 b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256
new file mode 100644
index 0000000..59e13ce
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256
@@ -0,0 +1,74 @@
+4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2  artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt
+7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6  artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt
+ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5  artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt
+0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe  artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt
+15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5  artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt
+c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc  artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt
+029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b  artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt
+956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0  artifacts/bianchini/v2/codex/P08/closure/guard-status.json
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt
+850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3  artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt
+7d5a07f194b89238e3508418f8a01c23d9fa9c48b07851633923bfa1d4bb59f4  artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json
+ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d  artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt
+ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539  artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt
+c7dd7ddc83182ef6814666a33815aa8eb9703d06575b4b6a1c988945b625c308  artifacts/bianchini/v2/codex/P08/closure/independent-review.json
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt
+b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a  artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt
+f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e  artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt
+89d3ddb5e3202f9e5302f6b16594034261822f1ec010cd4b82c2125d046f713f  artifacts/bianchini/v2/codex/P08/closure/proof-results.json
+ce0639a118bc8199074287dcd4eb1241dcf9065252dbe27c2a0c8b86b417a4a1  artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json
+5b846275cb8106379130786aee919ba7e5660c876f2b8bd51cb8e3e930f0e54a  artifacts/bianchini/v2/codex/P08/closure/recovery-report.md
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt
+d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e  artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt
+279a71c6f422ec2cd4ea96e186c4cc9b0d1c2d25ec64096e94ee58bdd5228948  artifacts/bianchini/v2/codex/P08/closure/review-package.md
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt
+83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4  artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt
+7039b2669e97b9545d424451cfe745d3f182201c88b80fdd858be7cc7de77a45  artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md
+e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f  artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json
+de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac  artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt
+c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687  artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt
+84998da46e2782c76a75b7310063d3926b7b2a71ffb2e3d176b0c1244cef0b54  artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json
+3dab65e6e07bf0ad2bfc426e7afc919bfc10192618e12ea4ccc47cfa9fae76fe  artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json
+32fcf753a20c68b5ccddfad07b283a11264cfbc9099ea5866db609e233453f5f  artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json
+3f7899f68082e8f8bce1e3d0cacd4d8ff811e0e829e0a236fd2c1bebdc4668c8  artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt
+782ee5d0b1d150b10839425a5930ec6174e531ac23c5cfcb329f40b4a3505e61  artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json
+6f6f9a97d3da3a0a1682101b039ae29328515a91d544776c5e8a63d1d3ab1517  artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json
+e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa  artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json
+edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0  artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt
+f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083  artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json
+d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3  artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt
+956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0  artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json
+c84acef69292ab80a7276292012167b52bc7c04cc9689a759318dacc71bc1d17  artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json
+c84acef69292ab80a7276292012167b52bc7c04cc9689a759318dacc71bc1d17  artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json
+29f0379d43191f8030a94edf9496e43a15bbe2a3e636e660ef2ab6392ed28498  artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md
+76d03c0a41bdffd56bd8aa25af3bac683dd6702b720c3a355493301b893d59c1  artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json
+8aa973100a15bf817985395637131e838cf84e427be4792583def923f020f5fa  artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json
+78e3d2077b31f1610af2b8e4710f29e0fc27180b9835677eb989cfd159ae2a0b  artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json
+659d8c1defba1ff49236bc25965b2a90a66fb2b5228dc4e3ed4fd8d40f6ad24b  artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch
+ccf06e3f5681ebb3c34cd83900d1e19cdef5adc3adcb3df1edff9ed7afbc2316  artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json
+25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b  artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json
+6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0  artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt
+2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74  artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json
+075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded  artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt
+e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt
+a8bf22d06b660c169a59aedbe86c4d64199ffc5e0b4067fda8b4a9c1b5c551b1  artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json
+8583b460784bb4749c73c8616a7c3ad73fa0ac36be89faddd865090cd27fc5d7  artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md
+c6262a57ff89539801eaad601c4716ab6f8edb8724507ed7f6c44ea467872be8  artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json
+e106ffc8c99a844a5c7483c511a87c7c741f14a507e1b2c227f1bd80d7ed30b7  artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json
+4124764ea9235d0dca6c5b6042890a9d10c60f2ef06595309e0f5b6a9e8fdcf6  artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json
+c1bf12a234012329aa6c5ffc0347e97cc29438b2fc8e2c295e7bc20766adf0f1  artifacts/bianchini/v2/codex/convergence/P08/1.json
+b05ec6a4c44731c1973f905bc71b96952b270706e4602c78b90f1aa940865547  artifacts/bianchini/v2/ledgers/P08.md
+3639b3bd12e288b79488df30e0ef29144659019b50d61f4c2d289656aff42100  docs/living/PROJECT_STATE.md
+c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7  scripts/phase1/recover_p08.py
+389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239  scripts/phase1/test_recover_p08.py
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md
new file mode 100644
index 0000000..d1ac3fb
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md
@@ -0,0 +1,40 @@
+# P08 B1 — rodada 1, pacote para aceite
+
+Branch bm/v2-p08, HEAD original 7981377a433270c9e2072fcafdf89b690988fa08. Method Bianchini 3.2.0, strict. Sem staging, commit, push, coleta ou download nesta retomada.
+
+## Causa e correção
+
+acquire_inat convertia qualquer falha capturada em inaturalist_contract_or_evidence. Como esse código não pertence a RETRYABLE, acquire ignorava a fonte após um timeout transitório. A correção preserva str(error) somente para RecoveryError já classificado em RETRYABLE. Demais erros continuam bloqueados. O conjunto RETRYABLE não mudou.
+
+## Evidências e revisão
+
+RED histórico proof-6928ea925e6f438e3873543389326106 no SHA original, mais RED dos três testes novos contra produção original (12 assertions falharam). GREEN reutilizado: três testes novos, 54 P08, 15 adaptador, 236 suíte afetada, incluindo cinco mutações seletivas mortas. Todos os hashes de fontes, logs e saídas conferem; demais dependências rastreadas da suíte coincidem com HEAD. Não se repetiu suíte por troca de sessão. evidence-reconciliation.json registra fontes e resultados.
+
+Executados agora: workspace resume/check, route, validate-state, snapshot verify, planning-audit strict, repo-hygiene, git diff --check; reconciliação de hashes; comparação read-only de bytes/mtimes externos; revisão independente e inspeção Git. Nenhum teste ou mutação reexecutado agora.
+
+Os testes exercitam timeout com três tentativas, restart com sucesso na quarta requisição, orçamento cumulativo esgotado sem nova conexão, journal/config preservados, ausência de página/cursor/candidato antes do sucesso, um candidato pendente após sucesso e repetição estável sem duplicação. Contrato/integridade/limites não viram retry.
+
+Revisor independente retornou findings vazio. Revisão técnica passed nos bytes não commitados. Guard preservado em fixing, rodada 1, B1 open, redesign 0, pending_delta null. Não há resolução formal nem gates da correção; os gates no sidecar são históricos, sobre o SHA original. P08 permanece blocked, release pending. O checkpoint oficial copia a prosa histórica do estado; o último bloco do ledger registra a instrução atual, sem inserir campos de convergência em PROJECT_STATE.
+
+## Separação de arquivos
+
+Correção: scripts/phase1/recover_p08.py e scripts/phase1/test_recover_p08.py, idênticos ao início desta retomada. Evidências da rodada e deste aceite estão em fix-B1/.
+
+Recuperação documental anterior: docs/living/PROJECT_STATE.md, bloco Closure recovery do ledger, closure/*, store de proofs e sidecar. Todos preservados; somente um novo bloco foi acrescentado ao ledger. preexisting-inventory.json e recovery-documentary-before.patch separam os bytes anteriores ao fix; session-start-inventory.json registra o ponto desta retomada. O sidecar/backup já haviam mudado pelo fix oficial antes da interrupção e não foram alterados agora.
+
+O inventário exato proposto está em commit-inventory.txt; commit-inventory.json classifica cada path e lista exclusões locais. acceptance-manifest.sha256 contém SHA-256 de todos os arquivos propostos, exceto o próprio manifesto e acceptance-digest.txt. O digest aceito é o SHA-256 dos bytes desse manifesto. O inventário inclui ambos os arquivos derivados; não há autorreferência. O futuro recibo humano fica fora deste digest. Qualquer mudança de payload exige regenerar manifesto e novo aceite.
+
+## Dados e inspeção
+
+1088 candidatos pendentes, zero transferências, approved_for_dataset=0, usable=0. Bytes e mtimes de P06/P07/P08 e backup conferem com o início da rodada (29/13/139/138 arquivos, incluindo locks). iNaturalist real continua sem crosswalk humano. Treinamento não autorizado; P09 não iniciado. Nenhuma migração da configuração, code fingerprint ou journal externo.
+
+Inspeção abrange arquivos novos, modificados e os 33 paths da implementação original para distinguir história de inclusão nova. Fixtures/URLs/EXIF/revisores sintéticos em testes e pacotes de revisão são exemplos de contrato; logs guard contêm metadados operacionais históricos, não respostas reais de candidatos. Nenhuma imagem, base64 de imagem, credencial, .env, chave privada, autor/revisor real ou resposta bruta privada nova identificada. O inventário granular do dataset externo e os backups/lock operacionais do guard ficam preservados fora do commit proposto. Não é aprovação botânica ou de privacidade dos candidatos.
+
+## Sequência posterior condicionada
+
+1. Aceite explícito do novo digest; registrar recibo separado sem reusar o aceite original. Aceitar bytes não implica permissão de staging/commit/push; obter autorização Git expressa no escopo necessário.
+2. Revalidar HEAD, branch, workspace, índice e cada hash/inventário; realizar staging apenas dos paths listados e criar commit próprio (sugestão: fix(p08): preserve transient iNaturalist failures on resume). Não amendar/regravar original. Nada de push inferido.
+3. No novo SHA, emitir proof GREEN para B1 com argv e cwd idênticos ao RED, como exige o guard. Atenção: o wrapper histórico grava dois logs em closure/ por path absoluto. Preservar previamente esses bytes/mtimes, arquivar separadamente a saída GREEN e restabelecer/verificar os logs históricos; nunca apresentá-los sobrescritos como nova evidência. Registrar stdout/stderr/hash do proof novo. Não modificar o comando para simular equivalência.
+4. submit-delta --kind fix com base igual ao last_review_head original e head igual ao novo SHA; somente então review-package oficial do delta e review em awaiting_review. Finding B1 source=frozen/resolution=resolved deve referenciar o novo proof GREEN, conservando contrato/prova RED. Não repetir fix nem incrementar rodada por troca de sessão.
+5. Emitir proofs no novo SHA e registrar todos os gates obrigatórios, inclusive suíte/mutação seletiva do plano no SHA final, integridade read-only, aceite novo e inspeção. Reutilizar evidência histórica apenas como contexto; ela não satisfaz gates do novo SHA. Não executar aquisição/finalização/migração real para satisfazer gate. Se a checagem de integridade exigir o runtime antigo, preservar sua identidade e provar separadamente os bytes externos sem forçar atualização do dataset.
+6. Fechar guard somente com B1 formalmente resolvido, HEAD revisado e gates obrigatórios passed no novo SHA; depois atualizar fechamento P08 pelo método. Confirmar pendências legítimas dos candidatos e zero aprovados sem inventar parecer pericial. Não avançar release, treino, P09 ou push por inferência. Artefatos posteriores ao commit formam registro de fechamento separado, sem amend do commit da correção.
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json
new file mode 100644
index 0000000..1cd7ee9
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json
@@ -0,0 +1,27 @@
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_*.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:55.924807+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
+  "stderr_sha256": "de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt
new file mode 100644
index 0000000..29773ff
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt
@@ -0,0 +1,5 @@
+............................................................................................................................................................................................................................................
+----------------------------------------------------------------------
+Ran 236 tests in 10.852s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt
new file mode 100644
index 0000000..7a5fadf
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt
@@ -0,0 +1,5 @@
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "advance_cursor_before_commit", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "selective_mutation": "advance_cursor_before_commit"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 3, "mode": "mutant", "network_calls": 0, "seam": "allow_private_export", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "selective_mutation": "allow_private_export"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 1, "mode": "mutant", "network_calls": 0, "seam": "bypass_expert", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "selective_mutation": "bypass_expert"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "bypass_license", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "mutant": {"errors": 0, "failures": 8, "material_changes_reached": 8, "mock_calls": 9, "mode": "mutant", "network_calls": 0, "seam": "bypass_license", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "selective_mutation": "bypass_license"}
+{"baseline": {"errors": 0, "failures": 0, "material_changes_reached": 0, "mock_calls": 0, "mode": "baseline", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "mutant": {"errors": 0, "failures": 1, "material_changes_reached": 1, "mock_calls": 2, "mode": "mutant", "network_calls": 0, "seam": "ignore_hash_mismatch", "source_sha256": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7", "tests_run": 1, "tests_sha256": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"}, "selective_mutation": "ignore_hash_mismatch"}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json b/artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json
new file mode 100644
index 0000000..432c84d
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json
@@ -0,0 +1,9 @@
+{
+  "action": "decide_reversibly_record_if_material_and_continue",
+  "classification": "implementation_detail",
+  "extra_review_required": false,
+  "plan_files_mutable": false,
+  "plan_invalidating": false,
+  "reapproval_required": false,
+  "redesign_allowed": false
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json b/artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json
new file mode 100644
index 0000000..c415d6e
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json
@@ -0,0 +1,116 @@
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
+      "status": "completed",
+      "ledger": "artifacts/bianchini/v2/ledgers/P07.md"
+    },
+    {
+      "id": "P08",
+      "status": "blocked",
+      "ledger": "artifacts/bianchini/v2/ledgers/P08.md"
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
+  "next_action": "P08 closure blocked by synthetic iNaturalist timeout resumption proof-6928ea925e6f438e3873543389326106. Await separate instruction for any code/test change. No second commit or push. 1088 candidates pending; zero transfers, approved_for_dataset=0, usable=0; real iNaturalist no_crosswalk. Training unauthorized; release pending; P09 not started.",
+  "workspace": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+  "git": {
+    "branch": "bm/v2-p08",
+    "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "dirty": true
+  },
+  "ledger_tail": [
+    "# P08 execution ledger",
+    "",
+    "- Approved package: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`.",
+    "- Base revision: `24de252d27a137281c02cad50533280bb82dd80d`; P07 base `b6844f9129d9edf862ae7958d8f043d9bdd5bd84`.",
+    "- Workspace: `/tmp/scanplant-p08-execution`; branch `bm/v2-p08`.",
+    "- Method installation: active .agents, version 3.2.0, v2-standalone.",
+    "- Profile standard; technical mode strict/per_task, data-transform, one unit `1`; authorized grouped operational round.",
+    "- Explicit current user authorization supersedes historical planning-only scope, grants implementation and bounded collection, prohibits staging/commit/push/release.",
+    "- Preflight: root/branch/HEAD/upstream/remote, clean index/tree, only three known starting worktrees, snapshot and manifest, strict planning audit and hygiene passed. P07/guard completed, usable=0; P08 approved/unstarted, release pending, P09 absent. Python 3.14.4/Pillow 12.3.0 available.",
+    "- P06: 29 files, SHA256SUMS passed; 17/17 image hashes match P07 closure. All seven final external P07 hashes match. No historical mutation.",
+    "- `bm change-policy --file-location`: bounded_amendment; evidence artifacts and temporary execution workspace location recorded, approved plan immutable.",
+    "- RED: recovery-red.txt and inat-red.txt record missing-module failures before implementation. GREEN initial focal runs passed.",
+    "- Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.",
+    "- Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.",
+    "- Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint.",
+    "",
+    "- Continuation recovered the exact checkpoint digest and eleven untracked files; existing workspace reused, baseline HEAD unchanged, no upstream.",
+    "- Final continuation evidence: artifacts/bianchini/v2/codex/P08/continuation-report.md and verification-final.json. 51 recovery + 15 adapter focal tests; 233 full historical/affected tests; five selective mutations killed, zero survivors.",
+    "- Real Commons round: 120 successful metadata requests, 1090 class associations/1088 unique candidates, all pending, no media transfer. iNaturalist no_crosswalk, zero requests. P07 17/17 bytes and mtimes preserved.",
+    "- Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.",
+    "- External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.",
+    "- Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending.",
+    "",
+    "## Closure recovery — 2026-10-07",
+    "",
+    "- Same branch recovered through Git prune (only obsolete registration) and Method workspace create/resume into persistent `.worktrees/ScanPlant/p08`; HEAD `7981377a433270c9e2072fcafdf89b690988fa08`, parent `24de252d27a137281c02cad50533280bb82dd80d`; one own commit.",
+    "- No prior P08 sidecar/proof store recovered from surviving official worktrees/Git; common proof signing key exists, contents not exposed. Uncommitted evidence formerly in lost checkout is unavailable; committed historical logs are preserved but are not current guard proofs.",
+    "- All approved implementation bytes/receipt and both external manifests verified. Historical checkpoint digests remain immutable; new recovery records are separate.",
+    "- 51 recovery, 15 adapter, 233 affected/history tests passed; five selective mutants killed. External 138-file datasets, 29 historical source files, 17 images and seven P07 receipts match; read-only replay preserves bytes/mtimes.",
+    "- Independent review reproduced B1 using `proof-6928ea925e6f438e3873543389326106`: transient iNaturalist timeout loses retry classification. Guard sidecar: `artifacts/bianchini/v2/codex/convergence/P08/1.json`; see closure/guard-status.json and independent-review.json.",
+    "- Owner mandates halt on failure: no fixes, no second commit, no staging/push. Remaining final Git private-data inspection and candidate human review are not claimed passed. Evidence/state changes remain uncommitted for inspection.",
+    "- 1088 candidates pending; zero transfer/approved/usable. Real iNaturalist no_crosswalk; rights/botanical/privacy authority remains pending. Training unauthorized, release pending, P09 not started.",
+    "",
+    "",
+    "## B1 round 1 resumed — technical review and acceptance package",
+    "",
+    "- Current owner instruction supersedes the earlier closure-only prohibition for B1 work only; staging, commit and push remain prohibited. This entry is the current continuation authority; earlier state/checkpoint next_action prose describes the historical halt.",
+    "- Method 3.2.0 / v2-standalone / strict: workspace resume/check, route, state, approved snapshot, strict planning audit and hygiene passed. Original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 and branch bm/v2-p08 preserved; index empty.",
+    "- Existing two-line production delta preserves only existing transient RecoveryError codes in acquire_inat. RETRYABLE unchanged. Three existing synthetic restart tests preserved unchanged. All prior recovery documents preserved; this ledger is append-only.",
+    "- Historical RED proof-6928ea925e6f438e3873543389326106 is defect evidence on the original SHA only. Additional RED and GREEN fingerprints reconciled; reused 3 new / 54 P08 / 15 adapter / 236 affected tests and five killed selective mutations. No suite rerun during resumption.",
+    "- Independent reviewer p08_b1_independent_review returned no findings on the current technical delta. Full evidence and review: artifacts/bianchini/v2/codex/P08/fix-B1/. This is not a formal guard review or a proof on a future commit.",
+    "- Sidecar reference: artifacts/bianchini/v2/codex/convergence/P08/1.json. No second fix transition, submit-delta, review, gate, complete or stopped transition performed during resumption; no new round, redesign or P09.",
+    "- Read-only hashes and mtimes of all 319 external files (including operational locks) remain identical. Dataset/backup intact; 1088 pending, zero transfer/approved_for_dataset/usable; real iNaturalist no_crosswalk; training unauthorized; release pending.",
+    "- Git inspection distinguishes synthetic fixtures and preserved historical records from real private data. Full private external filename/mtime baseline and guard operational backups/lock remain local-only, preserved. Proposed exact paths: fix-B1/commit-inventory.txt; payload manifest: fix-B1/acceptance-manifest.sha256; digest: fix-B1/acceptance-digest.txt. Neither manifest nor digest includes itself in the payload hash set.",
+    "- Next authorized boundary: one human decision on the new bytes. Subsequent own commit, exact-SHA proofs, submit-delta and guard review/gates/closure require that decision and appropriate separate Git authorization. P08 is not completed; original human receipt is immutable and does not accept this fix."
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json b/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json
new file mode 100644
index 0000000..6e710f7
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json
@@ -0,0 +1,393 @@
+{
+  "base_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "proposed_count": 76,
+  "paths": [
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/guard-status.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/independent-review.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/proof-results.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/recovery-report.md",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/review-package.md",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-digest.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json",
+      "category": "B1 evidence and acceptance",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/codex/convergence/P08/1.json",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "new"
+    },
+    {
+      "path": "artifacts/bianchini/v2/ledgers/P08.md",
+      "category": "preexisting documentary recovery plus appended B1 continuation",
+      "git_status": "modified"
+    },
+    {
+      "path": "docs/living/PROJECT_STATE.md",
+      "category": "preexisting documentary recovery and guard history",
+      "git_status": "modified"
+    },
+    {
+      "path": "scripts/phase1/recover_p08.py",
+      "category": "B1 correction",
+      "git_status": "modified"
+    },
+    {
+      "path": "scripts/phase1/test_recover_p08.py",
+      "category": "B1 correction",
+      "git_status": "modified"
+    }
+  ],
+  "preserved_local_exclusions": {
+    "artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json": "Preserved local-only granular external dataset filename/hash/mtime inventory; aggregate integrity result is proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak": "Preserved operational sidecar backup; canonical sidecar proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.bak": "Preserved operational proof backup; canonical signed store proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.lock": "Preserved empty operational lock; not a deliverable."
+  },
+  "manifest_rule": "All exact proposed files except acceptance-manifest.sha256 and acceptance-digest.txt are hashed. SHA-256 of manifest is acceptance digest. Derived files are listed in inventory but not their own hash set."
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt
new file mode 100644
index 0000000..338f06a
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt
@@ -0,0 +1,76 @@
+artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/guard-status.json
+artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json
+artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/independent-review.json
+artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/proof-results.json
+artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json
+artifacts/bianchini/v2/codex/P08/closure/recovery-report.md
+artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt
+artifacts/bianchini/v2/codex/P08/closure/review-package.md
+artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt
+artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-digest.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-manifest.sha256
+artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md
+artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json
+artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json
+artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json
+artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json
+artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json
+artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json
+artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json
+artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json
+artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md
+artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json
+artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json
+artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json
+artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch
+artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt
+artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json
+artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md
+artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json
+artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json
+artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json
+artifacts/bianchini/v2/codex/convergence/P08/1.json
+artifacts/bianchini/v2/ledgers/P08.md
+docs/living/PROJECT_STATE.md
+scripts/phase1/recover_p08.py
+scripts/phase1/test_recover_p08.py
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json b/artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json
new file mode 100644
index 0000000..2277d2d
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json
@@ -0,0 +1,105 @@
+{
+  "kind": "working_bytes_evidence_reconciliation_not_guard_proof",
+  "checked_at": "2026-10-07T23:08:02.977490+00:00",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "records": {
+    "regression-red": {
+      "record_sha256": "2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74",
+      "source_and_output_hashes_match": true,
+      "exit_code": 1,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 3 tests in 0.125s",
+        "",
+        "FAILED (failures=12)"
+      ]
+    },
+    "regression-green": {
+      "record_sha256": "25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 3 tests in 0.205s",
+        "",
+        "OK"
+      ]
+    },
+    "focal-recovery": {
+      "record_sha256": "f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 54 tests in 3.052s",
+        "",
+        "OK"
+      ]
+    },
+    "focal-adapter": {
+      "record_sha256": "e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 15 tests in 0.007s",
+        "",
+        "OK"
+      ]
+    },
+    "affected-history": {
+      "record_sha256": "e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 236 tests in 10.852s",
+        "",
+        "OK"
+      ]
+    }
+  },
+  "historical_red_proof_id": "proof-6928ea925e6f438e3873543389326106",
+  "historical_red_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "mutations_reused": [
+    "advance_cursor_before_commit",
+    "allow_private_export",
+    "bypass_expert",
+    "bypass_license",
+    "ignore_hash_mismatch"
+  ],
+  "preexisting_documents_unchanged": true,
+  "preexisting_changed_only_by_authorized_fix_transition": [
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak"
+  ],
+  "external_bytes_and_mtimes_unchanged": true,
+  "external_counts": {
+    "p06-recovery-20260928": 29,
+    "p07-curation-20260928": 13,
+    "p08-recovery-20261005": 139,
+    "p08-recovery-20261005-backup": 138
+  },
+  "external_inventory_sha256": "6f35f2692d2901aa6bffbdea44912940267bbddf069452f2b0a3650374d9a30f",
+  "dependency_hashes": {
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS": "9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json": "f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee",
+    "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+    "scripts/phase1/acquire_commons.py": "ddd2bf5d5f6c7e75fe090af8fd0313a9785fefccb30ee3a62b070a48f0ba6046",
+    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/requirements-p06.txt": "41b54a6fb2918667ca47a61d73b522629d84490f3d78f0f20b21135faba10d35",
+    "scripts/phase1/test_acquire_commons.py": "3d7781ef2e70f9ee57331cff72848ac3b61be3c9ec33f627ae8c8b4fb01d622e",
+    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed"
+  },
+  "new_test_executions": 0,
+  "guard_proofs_for_fixed_bytes": false
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json b/artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json
new file mode 100644
index 0000000..fb2979c
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json
@@ -0,0 +1,11 @@
+{
+  "all_files_bytes_and_mtimes_unchanged": true,
+  "counts": {
+    "p06-recovery-20260928": 29,
+    "p07-curation-20260928": 13,
+    "p08-recovery-20261005": 139,
+    "p08-recovery-20261005-backup": 138
+  },
+  "network_collection": false,
+  "downloads": 0
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json
new file mode 100644
index 0000000..60df0d6
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json
@@ -0,0 +1,27 @@
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_inaturalist_source.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:55.827623+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt
new file mode 100644
index 0000000..070e7a6
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt
@@ -0,0 +1,5 @@
+...............
+----------------------------------------------------------------------
+Ran 15 tests in 0.007s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json
new file mode 100644
index 0000000..410d725
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json
@@ -0,0 +1,27 @@
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:52.443028+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt
new file mode 100644
index 0000000..fb138f7
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt
@@ -0,0 +1,5 @@
+......................................................
+----------------------------------------------------------------------
+Ran 54 tests in 3.052s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json
new file mode 100644
index 0000000..bbf6dec
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json
@@ -0,0 +1,316 @@
+{
+  "migrated": false,
+  "next_action": "fix_required",
+  "phase": "review_frozen",
+  "recovered": false,
+  "state": {
+    "blockers": {
+      "B1": {
+        "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+        "disposition": "blocker",
+        "id": "B1",
+        "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+        "review_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "risk_seam": "p08-source-contract",
+        "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+        "severity": "important",
+        "source": "initial",
+        "status": "open",
+        "structural": false,
+        "structural_class": null,
+        "structural_evidence": null,
+        "title": "Timeout de iNaturalist impede a retomada contratada"
+      }
+    },
+    "created_at": "2026-10-07T22:50:20.012004Z",
+    "decisions": [
+      {
+        "at": "2026-10-07T22:50:39.350539Z",
+        "kind": "local_block",
+        "result": "independent_work_continues",
+        "summary": "User explicitly requires ending closure on gate failure without code/test changes, a second commit or push. B1 remains open; no fix round or terminal transition requested. Only P08 closure is authorized."
+      }
+    ],
+    "deferred_hardening": [],
+    "delta_submissions": 0,
+    "events": [
+      {
+        "action": "review_frozen",
+        "at": "2026-10-07T22:50:20.012073Z",
+        "blockers": [
+          "B1"
+        ],
+        "hardening": 0
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.328167Z",
+        "gate": "synthetic-source-contract",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "status": "failed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.716608Z",
+        "gate": "focal-recovery",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.196782Z",
+        "gate": "focal-adapter",
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.767313Z",
+        "gate": "canonical-taxonomy",
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:22.422632Z",
+        "gate": "append-only-integrity-idempotence",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:23.182013Z",
+        "gate": "selective-mutation",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:24.137196Z",
+        "gate": "affected-history",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:25.130279Z",
+        "gate": "p07-17-preserved",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:26.221197Z",
+        "gate": "external-data-integrity",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:27.416911Z",
+        "gate": "final-human-bytes-acceptance",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:28.713376Z",
+        "gate": "approved-bytes",
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:30.017383Z",
+        "gate": "historical-checksums",
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:31.398464Z",
+        "gate": "state",
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:32.841139Z",
+        "gate": "planning-snapshot",
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:34.391837Z",
+        "gate": "planning-audit",
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:35.994322Z",
+        "gate": "repo-hygiene",
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:37.662898Z",
+        "gate": "diff-check",
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "status": "passed"
+      },
+      {
+        "action": "decision",
+        "at": "2026-10-07T22:50:39.350613Z",
+        "kind": "local_block",
+        "result": "independent_work_continues"
+      }
+    ],
+    "fix_rounds": 0,
+    "gates": {
+      "affected-history": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:24.137120Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "append-only-integrity-idempotence": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:22.422590Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "approved-bytes": {
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "recorded_at": "2026-10-07T22:50:28.713298Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "canonical-taxonomy": {
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "recorded_at": "2026-10-07T22:50:21.767168Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "diff-check": {
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "recorded_at": "2026-10-07T22:50:37.662852Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "external-data-integrity": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:26.221150Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "final-human-bytes-acceptance": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:27.416857Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-adapter": {
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "recorded_at": "2026-10-07T22:50:21.196738Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-recovery": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:20.716570Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "historical-checksums": {
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "recorded_at": "2026-10-07T22:50:30.017327Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "p07-17-preserved": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:25.130229Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-audit": {
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "recorded_at": "2026-10-07T22:50:34.391804Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-snapshot": {
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "recorded_at": "2026-10-07T22:50:32.841102Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "repo-hygiene": {
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "recorded_at": "2026-10-07T22:50:35.994266Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "selective-mutation": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:23.181982Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "state": {
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "recorded_at": "2026-10-07T22:50:31.398405Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "synthetic-source-contract": {
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "recorded_at": "2026-10-07T22:50:20.328100Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "failed"
+      }
+    },
+    "last_review_head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "pending_delta": null,
+    "phase": "review_frozen",
+    "plan_id": "P08",
+    "planning_version": "v2",
+    "redesign_count": 0,
+    "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+    "required_gates": [
+      "synthetic-source-contract",
+      "focal-recovery",
+      "focal-adapter",
+      "canonical-taxonomy",
+      "append-only-integrity-idempotence",
+      "selective-mutation",
+      "affected-history",
+      "p07-17-preserved",
+      "external-data-integrity",
+      "final-human-bytes-acceptance",
+      "approved-bytes",
+      "historical-checksums",
+      "state",
+      "planning-snapshot",
+      "planning-audit",
+      "repo-hygiene",
+      "diff-check",
+      "human-botanical-privacy-review",
+      "git-secrets-private-data-images-inspection"
+    ],
+    "schema_version": 2,
+    "seam": "p08-source-contract",
+    "task_brief": "artifacts/bianchini/v2/codex/P08/task-brief.md",
+    "task_brief_digest": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "unit_digest": "33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af",
+    "unit_id": "1",
+    "unit_identity": "2638b0c17436a9e732e54818b20e092e594ffa983a29df86b7c6b355a593404a",
+    "unit_identity_source": "task_brief",
+    "updated_at": "2026-10-07T22:50:39.350618Z"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json
new file mode 100644
index 0000000..5c3c987
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json
@@ -0,0 +1,331 @@
+{
+  "migrated": false,
+  "phase": "fixing",
+  "recovered": false,
+  "state": {
+    "blockers": {
+      "B1": {
+        "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+        "disposition": "blocker",
+        "id": "B1",
+        "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+        "review_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "risk_seam": "p08-source-contract",
+        "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+        "severity": "important",
+        "source": "initial",
+        "status": "open",
+        "structural": false,
+        "structural_class": null,
+        "structural_evidence": null,
+        "title": "Timeout de iNaturalist impede a retomada contratada"
+      }
+    },
+    "created_at": "2026-10-07T22:50:20.012004Z",
+    "decisions": [
+      {
+        "at": "2026-10-07T22:50:39.350539Z",
+        "kind": "local_block",
+        "result": "independent_work_continues",
+        "summary": "User explicitly requires ending closure on gate failure without code/test changes, a second commit or push. B1 remains open; no fix round or terminal transition requested. Only P08 closure is authorized."
+      }
+    ],
+    "deferred_hardening": [],
+    "delta_submissions": 0,
+    "events": [
+      {
+        "action": "review_frozen",
+        "at": "2026-10-07T22:50:20.012073Z",
+        "blockers": [
+          "B1"
+        ],
+        "hardening": 0
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.328167Z",
+        "gate": "synthetic-source-contract",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "status": "failed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.716608Z",
+        "gate": "focal-recovery",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.196782Z",
+        "gate": "focal-adapter",
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.767313Z",
+        "gate": "canonical-taxonomy",
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:22.422632Z",
+        "gate": "append-only-integrity-idempotence",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:23.182013Z",
+        "gate": "selective-mutation",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:24.137196Z",
+        "gate": "affected-history",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:25.130279Z",
+        "gate": "p07-17-preserved",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:26.221197Z",
+        "gate": "external-data-integrity",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:27.416911Z",
+        "gate": "final-human-bytes-acceptance",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:28.713376Z",
+        "gate": "approved-bytes",
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:30.017383Z",
+        "gate": "historical-checksums",
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:31.398464Z",
+        "gate": "state",
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:32.841139Z",
+        "gate": "planning-snapshot",
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:34.391837Z",
+        "gate": "planning-audit",
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:35.994322Z",
+        "gate": "repo-hygiene",
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:37.662898Z",
+        "gate": "diff-check",
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "status": "passed"
+      },
+      {
+        "action": "decision",
+        "at": "2026-10-07T22:50:39.350613Z",
+        "kind": "local_block",
+        "result": "independent_work_continues"
+      },
+      {
+        "action": "phase_transition",
+        "at": "2026-10-07T22:56:27.280222Z",
+        "command": "fix",
+        "source": "review_frozen",
+        "target": "fixing"
+      },
+      {
+        "action": "fix_started",
+        "at": "2026-10-07T22:56:27.280392Z",
+        "blockers": [
+          "B1"
+        ],
+        "round": 1,
+        "summary": "Authorized first B1 fix: preserve existing transient RecoveryError codes in acquire_inat; add synthetic restart regression; stop before staging/commit/push for grouped acceptance of new bytes."
+      }
+    ],
+    "fix_rounds": 1,
+    "gates": {
+      "affected-history": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:24.137120Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "append-only-integrity-idempotence": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:22.422590Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "approved-bytes": {
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "recorded_at": "2026-10-07T22:50:28.713298Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "canonical-taxonomy": {
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "recorded_at": "2026-10-07T22:50:21.767168Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "diff-check": {
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "recorded_at": "2026-10-07T22:50:37.662852Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "external-data-integrity": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:26.221150Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "final-human-bytes-acceptance": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:27.416857Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-adapter": {
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "recorded_at": "2026-10-07T22:50:21.196738Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-recovery": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:20.716570Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "historical-checksums": {
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "recorded_at": "2026-10-07T22:50:30.017327Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "p07-17-preserved": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:25.130229Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-audit": {
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "recorded_at": "2026-10-07T22:50:34.391804Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-snapshot": {
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "recorded_at": "2026-10-07T22:50:32.841102Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "repo-hygiene": {
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "recorded_at": "2026-10-07T22:50:35.994266Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "selective-mutation": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:23.181982Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "state": {
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "recorded_at": "2026-10-07T22:50:31.398405Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "synthetic-source-contract": {
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "recorded_at": "2026-10-07T22:50:20.328100Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "failed"
+      }
+    },
+    "last_review_head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "pending_delta": null,
+    "phase": "fixing",
+    "plan_id": "P08",
+    "planning_version": "v2",
+    "redesign_count": 0,
+    "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+    "required_gates": [
+      "synthetic-source-contract",
+      "focal-recovery",
+      "focal-adapter",
+      "canonical-taxonomy",
+      "append-only-integrity-idempotence",
+      "selective-mutation",
+      "affected-history",
+      "p07-17-preserved",
+      "external-data-integrity",
+      "final-human-bytes-acceptance",
+      "approved-bytes",
+      "historical-checksums",
+      "state",
+      "planning-snapshot",
+      "planning-audit",
+      "repo-hygiene",
+      "diff-check",
+      "human-botanical-privacy-review",
+      "git-secrets-private-data-images-inspection"
+    ],
+    "schema_version": 2,
+    "seam": "p08-source-contract",
+    "task_brief": "artifacts/bianchini/v2/codex/P08/task-brief.md",
+    "task_brief_digest": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "unit_digest": "33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af",
+    "unit_id": "1",
+    "unit_identity": "2638b0c17436a9e732e54818b20e092e594ffa983a29df86b7c6b355a593404a",
+    "unit_identity_source": "task_brief",
+    "updated_at": "2026-10-07T22:56:27.280394Z"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json
new file mode 100644
index 0000000..5c3c987
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json
@@ -0,0 +1,331 @@
+{
+  "migrated": false,
+  "phase": "fixing",
+  "recovered": false,
+  "state": {
+    "blockers": {
+      "B1": {
+        "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+        "disposition": "blocker",
+        "id": "B1",
+        "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+        "review_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "risk_seam": "p08-source-contract",
+        "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+        "severity": "important",
+        "source": "initial",
+        "status": "open",
+        "structural": false,
+        "structural_class": null,
+        "structural_evidence": null,
+        "title": "Timeout de iNaturalist impede a retomada contratada"
+      }
+    },
+    "created_at": "2026-10-07T22:50:20.012004Z",
+    "decisions": [
+      {
+        "at": "2026-10-07T22:50:39.350539Z",
+        "kind": "local_block",
+        "result": "independent_work_continues",
+        "summary": "User explicitly requires ending closure on gate failure without code/test changes, a second commit or push. B1 remains open; no fix round or terminal transition requested. Only P08 closure is authorized."
+      }
+    ],
+    "deferred_hardening": [],
+    "delta_submissions": 0,
+    "events": [
+      {
+        "action": "review_frozen",
+        "at": "2026-10-07T22:50:20.012073Z",
+        "blockers": [
+          "B1"
+        ],
+        "hardening": 0
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.328167Z",
+        "gate": "synthetic-source-contract",
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "status": "failed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:20.716608Z",
+        "gate": "focal-recovery",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.196782Z",
+        "gate": "focal-adapter",
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:21.767313Z",
+        "gate": "canonical-taxonomy",
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:22.422632Z",
+        "gate": "append-only-integrity-idempotence",
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:23.182013Z",
+        "gate": "selective-mutation",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:24.137196Z",
+        "gate": "affected-history",
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:25.130279Z",
+        "gate": "p07-17-preserved",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:26.221197Z",
+        "gate": "external-data-integrity",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:27.416911Z",
+        "gate": "final-human-bytes-acceptance",
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:28.713376Z",
+        "gate": "approved-bytes",
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:30.017383Z",
+        "gate": "historical-checksums",
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:31.398464Z",
+        "gate": "state",
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:32.841139Z",
+        "gate": "planning-snapshot",
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:34.391837Z",
+        "gate": "planning-audit",
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:35.994322Z",
+        "gate": "repo-hygiene",
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "status": "passed"
+      },
+      {
+        "action": "gate_recorded",
+        "at": "2026-10-07T22:50:37.662898Z",
+        "gate": "diff-check",
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "status": "passed"
+      },
+      {
+        "action": "decision",
+        "at": "2026-10-07T22:50:39.350613Z",
+        "kind": "local_block",
+        "result": "independent_work_continues"
+      },
+      {
+        "action": "phase_transition",
+        "at": "2026-10-07T22:56:27.280222Z",
+        "command": "fix",
+        "source": "review_frozen",
+        "target": "fixing"
+      },
+      {
+        "action": "fix_started",
+        "at": "2026-10-07T22:56:27.280392Z",
+        "blockers": [
+          "B1"
+        ],
+        "round": 1,
+        "summary": "Authorized first B1 fix: preserve existing transient RecoveryError codes in acquire_inat; add synthetic restart regression; stop before staging/commit/push for grouped acceptance of new bytes."
+      }
+    ],
+    "fix_rounds": 1,
+    "gates": {
+      "affected-history": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:24.137120Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "append-only-integrity-idempotence": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:22.422590Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "approved-bytes": {
+        "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+        "recorded_at": "2026-10-07T22:50:28.713298Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "canonical-taxonomy": {
+        "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+        "recorded_at": "2026-10-07T22:50:21.767168Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "diff-check": {
+        "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+        "recorded_at": "2026-10-07T22:50:37.662852Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "external-data-integrity": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:26.221150Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "final-human-bytes-acceptance": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:27.416857Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-adapter": {
+        "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+        "recorded_at": "2026-10-07T22:50:21.196738Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "focal-recovery": {
+        "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+        "recorded_at": "2026-10-07T22:50:20.716570Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "historical-checksums": {
+        "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+        "recorded_at": "2026-10-07T22:50:30.017327Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "p07-17-preserved": {
+        "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+        "recorded_at": "2026-10-07T22:50:25.130229Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-audit": {
+        "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+        "recorded_at": "2026-10-07T22:50:34.391804Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "planning-snapshot": {
+        "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+        "recorded_at": "2026-10-07T22:50:32.841102Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "repo-hygiene": {
+        "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+        "recorded_at": "2026-10-07T22:50:35.994266Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "selective-mutation": {
+        "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+        "recorded_at": "2026-10-07T22:50:23.181982Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "state": {
+        "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+        "recorded_at": "2026-10-07T22:50:31.398405Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "passed"
+      },
+      "synthetic-source-contract": {
+        "proof_id": "proof-6928ea925e6f438e3873543389326106",
+        "recorded_at": "2026-10-07T22:50:20.328100Z",
+        "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+        "status": "failed"
+      }
+    },
+    "last_review_head": "7981377a433270c9e2072fcafdf89b690988fa08",
+    "pending_delta": null,
+    "phase": "fixing",
+    "plan_id": "P08",
+    "planning_version": "v2",
+    "redesign_count": 0,
+    "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+    "required_gates": [
+      "synthetic-source-contract",
+      "focal-recovery",
+      "focal-adapter",
+      "canonical-taxonomy",
+      "append-only-integrity-idempotence",
+      "selective-mutation",
+      "affected-history",
+      "p07-17-preserved",
+      "external-data-integrity",
+      "final-human-bytes-acceptance",
+      "approved-bytes",
+      "historical-checksums",
+      "state",
+      "planning-snapshot",
+      "planning-audit",
+      "repo-hygiene",
+      "diff-check",
+      "human-botanical-privacy-review",
+      "git-secrets-private-data-images-inspection"
+    ],
+    "schema_version": 2,
+    "seam": "p08-source-contract",
+    "task_brief": "artifacts/bianchini/v2/codex/P08/task-brief.md",
+    "task_brief_digest": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "unit_digest": "33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af",
+    "unit_id": "1",
+    "unit_identity": "2638b0c17436a9e732e54818b20e092e594ffa983a29df86b7c6b355a593404a",
+    "unit_identity_source": "task_brief",
+    "updated_at": "2026-10-07T22:56:27.280394Z"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md b/artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md
new file mode 100644
index 0000000..852fdbe
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md
@@ -0,0 +1,22 @@
+# Implementer Report — P08 B1, round 1
+
+- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md`
+- Status: TECHNICAL_FIX_READY_FOR_REVIEW; acceptance and commit pending.
+
+## Changes
+
+The preexisting fix in acquire_inat preserves str(error) only when error is RecoveryError and its code already belongs to RETRYABLE. All other caught errors retain inaturalist_contract_or_evidence. RETRYABLE itself is unchanged. The previous unconditional classification made a transient metadata timeout permanently skipped on restart by acquire.
+Three existing synthetic tests cover timeout/restart/success, preserved journal prefix and config, cumulative request quotas, no premature page/cursor or candidate, one candidate exactly once, stable subsequent invocation, and fail-closed classification of contract/integrity/budget failures.
+
+## Verification
+
+Reused signed RED proof-6928ea925e6f438e3873543389326106 on original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 only as historical defect evidence. Additional RED ran the three new tests against original production bytes (12 failed assertions). Reconciled current source/output fingerprints for GREEN: 3 new tests, 54 recovery, 15 adapter, 236 affected/history tests with five materially reached/killed selective mutants. These are working-byte records, not proofs for a future SHA. No test suite rerun during this resumption.
+Fresh read-only Method preflight, diff check, complete evidence hash reconciliation and external bytes/mtime comparison passed. All unchanged suite dependencies match original HEAD; both modified files match the previous GREEN records. No network acquisition or downloads. See evidence-reconciliation.json.
+
+## Decisions
+
+Reuse round 1, existing correction, original commit and all documentary recovery. implementation_detail decision already recorded by bm change-policy. No start/red/fix command repeated. No staging, commit or push. The official review-package for base=head is an empty committed delta; its explicitly labeled working-tree annex enables technical review only. Formal submit-delta/review and fresh gates must wait for a separately authorized own commit.
+
+## Concerns
+
+Guard stays fixing, B1 open, round 1, redesign 0. P08 remains blocked, release pending. Historical human acceptance does not accept new bytes. External config/code fingerprint and old receipts remain intact and must not be silently migrated; new code is not authorized against the real dataset. 1088 pending candidates, zero transfers/approved_for_dataset/usable, no real iNaturalist crosswalk, no training, no P09.
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json b/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json
new file mode 100644
index 0000000..c5a868a
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json
@@ -0,0 +1,24 @@
+{
+  "kind": "independent_technical_review_of_uncommitted_bytes_not_guard_review",
+  "reviewer": "p08_b1_independent_review",
+  "result": "passed",
+  "findings_file": "artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json",
+  "reviewed_package_sha256": "5cc45350b4f82e7ff6ed487868928e1da7fbffae1da4f68bae170649eb059144",
+  "persisted_package_sha256": "8583b460784bb4749c73c8616a7c3ad73fa0ac36be89faddd865090cd27fc5d7",
+  "package_difference": "Only official generated header report/output paths changed from temporary to persistent relative artifact paths; reviewed annex identical.",
+  "reviewed_annex_sha256": "82bbc8ce1e175c481fece8f1085a78c46a4db53b66faaca88ef9d28683cf5b6b",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  },
+  "assessment": "B1 corrected in working bytes; no material delta regression found. Only existing RETRYABLE RecoveryError codes preserved. Tests reconcile timeout/restart/success, cumulative quota, unchanged journal/config, no premature page/cursor, exactly one pending candidate, stable repetition.",
+  "formal_guard_resolution": false,
+  "tests_rerun_by_reviewer": false,
+  "limitations": [
+    "No new SHA or signed GREEN proof yet.",
+    "No real dataset execution, migration or renewed human acceptance."
+  ]
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json b/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json
new file mode 100644
index 0000000..2ef5648
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json
@@ -0,0 +1,3 @@
+{
+  "findings": []
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json b/artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json
new file mode 100644
index 0000000..50973d5
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json
@@ -0,0 +1,45 @@
+{
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "files": {
+    "artifacts/bianchini/v2/ledgers/P08.md": "9bb91c9f54ab4cc389ed0608b667477c653383236b293672d73f9c75ab446f49",
+    "docs/living/PROJECT_STATE.md": "3639b3bd12e288b79488df30e0ef29144659019b50d61f4c2d289656aff42100",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt": "4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt": "7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt": "ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt": "029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/guard-status.json": "956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+    "artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json": "7d5a07f194b89238e3508418f8a01c23d9fa9c48b07851633923bfa1d4bb59f4",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt": "ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt": "ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539",
+    "artifacts/bianchini/v2/codex/P08/closure/independent-review.json": "c7dd7ddc83182ef6814666a33815aa8eb9703d06575b4b6a1c988945b625c308",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt": "f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e",
+    "artifacts/bianchini/v2/codex/P08/closure/proof-results.json": "89d3ddb5e3202f9e5302f6b16594034261822f1ec010cd4b82c2125d046f713f",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json": "ce0639a118bc8199074287dcd4eb1241dcf9065252dbe27c2a0c8b86b417a4a1",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-report.md": "5b846275cb8106379130786aee919ba7e5660c876f2b8bd51cb8e3e930f0e54a",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+    "artifacts/bianchini/v2/codex/P08/closure/review-package.md": "279a71c6f422ec2cd4ea96e186c4cc9b0d1c2d25ec64096e94ee58bdd5228948",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json": "4124764ea9235d0dca6c5b6042890a9d10c60f2ef06595309e0f5b6a9e8fdcf6",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.bak": "2d444b7debf303cfb06079e4d2bccdb272c80b28d28735bdfd67575f13724835",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.lock": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json": "3ae61e20fa92ee2cfe2fd21a7922d5c7f607ee0a991087d8c7e3c05818827d0d",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak": "d49efedf2490b83e696395ec93deb7b6f0543baa39835ada641c62abcaaf2562"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch b/artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch
new file mode 100644
index 0000000..ce21411
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch
@@ -0,0 +1,69 @@
+diff --git a/artifacts/bianchini/v2/ledgers/P08.md b/artifacts/bianchini/v2/ledgers/P08.md
+index cd17c62..cfc6316 100644
+--- a/artifacts/bianchini/v2/ledgers/P08.md
++++ b/artifacts/bianchini/v2/ledgers/P08.md
+@@ -20,3 +20,13 @@
+ - Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.
+ - External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.
+ - Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending.
++
++## Closure recovery — 2026-10-07
++
++- Same branch recovered through Git prune (only obsolete registration) and Method workspace create/resume into persistent `.worktrees/ScanPlant/p08`; HEAD `7981377a433270c9e2072fcafdf89b690988fa08`, parent `24de252d27a137281c02cad50533280bb82dd80d`; one own commit.
++- No prior P08 sidecar/proof store recovered from surviving official worktrees/Git; common proof signing key exists, contents not exposed. Uncommitted evidence formerly in lost checkout is unavailable; committed historical logs are preserved but are not current guard proofs.
++- All approved implementation bytes/receipt and both external manifests verified. Historical checkpoint digests remain immutable; new recovery records are separate.
++- 51 recovery, 15 adapter, 233 affected/history tests passed; five selective mutants killed. External 138-file datasets, 29 historical source files, 17 images and seven P07 receipts match; read-only replay preserves bytes/mtimes.
++- Independent review reproduced B1 using `proof-6928ea925e6f438e3873543389326106`: transient iNaturalist timeout loses retry classification. Guard sidecar: `artifacts/bianchini/v2/codex/convergence/P08/1.json`; see closure/guard-status.json and independent-review.json.
++- Owner mandates halt on failure: no fixes, no second commit, no staging/push. Remaining final Git private-data inspection and candidate human review are not claimed passed. Evidence/state changes remain uncommitted for inspection.
++- 1088 candidates pending; zero transfer/approved/usable. Real iNaturalist no_crosswalk; rights/botanical/privacy authority remains pending. Training unauthorized, release pending, P09 not started.
+diff --git a/docs/living/PROJECT_STATE.md b/docs/living/PROJECT_STATE.md
+index 2fd4686..87c5250 100644
+--- a/docs/living/PROJECT_STATE.md
++++ b/docs/living/PROJECT_STATE.md
+@@ -286,7 +286,7 @@
+     {
+       "id": "P08",
+       "path": "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md",
+-      "status": "approved",
++      "status": "blocked",
+       "risk": "high",
+       "execution": "strict",
+       "review": "per_task",
+@@ -318,8 +318,8 @@
+         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_recover_p08.py'",
+         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_inaturalist_source.py'"
+       ],
+-      "status": "pending",
+-      "scope": "P08 futuro; arquivos entregáveis, não implementados neste planejamento."
++      "status": "passed",
++      "scope": "P08 implementation 7981377: 51 recovery and 15 adapter tests passed; proofs in artifacts/bianchini/v2/codex/P08/closure/proof-results.json."
+     },
+     "plan": {
+       "commands": [
+@@ -328,8 +328,8 @@
+         "sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
+         "git diff --check"
+       ],
+-      "status": "pending",
+-      "scope": "P08 futuro; suite inclui cinco mutações stdlib aprovadas no planejamento; requer gates de dados/revisão/recibo externo. Não autoriza treino/release."
++      "status": "failed",
++      "scope": "P08: 233 historical/affected tests and five selective mutations passed, but independent review reproduced non-retryable iNaturalist timeout. Proof proof-6928ea925e6f438e3873543389326106 failed; closure and publication blocked. No code/test change authorized."
+     },
+     "release": {
+       "commands": [
+@@ -394,9 +394,14 @@
+       "id": "B-P03-R6-U009-TERMINAL-VSTEST-CONNECTION",
+       "summary": "P03-R6/U-009 foi invocada uma única vez via Bash: campaign_count=2, campaign_executed=true, U-008=consumed_non_reusable, U-009=consumed, exit_code=134 e failure_stage=campaign. Stryker 4.16.0 iniciou, mas falhou ao conectar a vstest.console após 90 segundos antes de produzir mutantes, mutation-report ou mutation score. Falha posterior ao marcador é terminal e não admite retry R6.",
+       "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909"
++    },
++    {
++      "id": "B-P08-INAT-TIMEOUT-RESUMPTION",
++      "summary": "Synthetic iNaturalist timeout is persisted as inaturalist_contract_or_evidence and cannot resume. Closure halted on gate failure as explicitly instructed; implementation and human receipt preserved.",
++      "evidence": "artifacts/bianchini/v2/codex/P08/closure/independent-review.json"
+     }
+   ],
+-  "next_action": "Aguardar autorização posterior de execução P08 sobre o plano publicado. Pacote/digest P08 integralmente aprovado; esta rodada autoriza somente registro, staging, commit e push do planejamento. P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed; guard completed sem blockers; usable=0 até decisões humanas válidas; P06/P07 fechados e imutáveis; release pending; active_execution null; treinamento não autorizado; P09 não iniciado.",
++  "next_action": "P08 closure blocked by synthetic iNaturalist timeout resumption proof-6928ea925e6f438e3873543389326106. Await separate instruction for any code/test change. No second commit or push. 1088 candidates pending; zero transfers, approved_for_dataset=0, usable=0; real iNaturalist no_crosswalk. Training unauthorized; release pending; P09 not started.",
+   "continuity_decision": {
+     "recommended_alternative": "A",
+     "status": "approved",
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json b/artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json
new file mode 100644
index 0000000..5587b27
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json
@@ -0,0 +1,7 @@
+{
+  "proof_id": "proof-6928ea925e6f438e3873543389326106",
+  "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "exit_code": 1,
+  "signature_validated_by_guard_status": true,
+  "saved_output_hashes_match": true
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json
new file mode 100644
index 0000000..197dd1c
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json
@@ -0,0 +1,30 @@
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py",
+    "-k",
+    "InaturalistResumeTests",
+    "-v"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:42.229752+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt
new file mode 100644
index 0000000..f0e9cca
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt
@@ -0,0 +1,8 @@
+test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... ok
+test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... ok
+test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... ok
+
+----------------------------------------------------------------------
+Ran 3 tests in 0.205s
+
+OK
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json
new file mode 100644
index 0000000..3003212
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json
@@ -0,0 +1,30 @@
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py",
+    "-k",
+    "InaturalistResumeTests",
+    "-v"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:35.344637+00:00",
+  "exit_code": 1,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt
new file mode 100644
index 0000000..6582c73
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt
@@ -0,0 +1,162 @@
+test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... 
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout') ... FAIL
+test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... FAIL
+test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... FAIL
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_429'
+- inaturalist_contract_or_evidence
++ http_429
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_500'
+- inaturalist_contract_or_evidence
++ http_500
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_502'
+- inaturalist_contract_or_evidence
++ http_502
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_503'
+- inaturalist_contract_or_evidence
++ http_503
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_504'
+- inaturalist_contract_or_evidence
++ http_504
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'maxlag'
+- inaturalist_contract_or_evidence
++ maxlag
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'network_error'
+- inaturalist_contract_or_evidence
++ network_error
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'response_timeout'
+- inaturalist_contract_or_evidence
++ response_timeout
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'resume_after'
+- inaturalist_contract_or_evidence
++ resume_after
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+======================================================================
+FAIL: test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget)
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 594, in test_timeout_restart_does_not_reset_request_budget
+    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+======================================================================
+FAIL: test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates)
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 534, in test_timeout_then_restart_preserves_journal_limits_and_candidates
+    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+----------------------------------------------------------------------
+Ran 3 tests in 0.125s
+
+FAILED (failures=12)
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt b/artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt
new file mode 100644
index 0000000..e69de29
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json b/artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json
new file mode 100644
index 0000000..b074bac
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json
@@ -0,0 +1,116 @@
+{
+  "workspace-resume": {
+    "branch": "bm/v2-p08",
+    "common_dir": "/home/administradorarthur/code/scanplant-current/ScanPlant/.git",
+    "git_dir": "/home/administradorarthur/code/scanplant-current/ScanPlant/.git/worktrees/p08",
+    "identity": "v2-p08",
+    "plan": "P08",
+    "planning_version": "v2",
+    "reused": true,
+    "safe": true,
+    "source": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+    "workspace": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08"
+  },
+  "workspace-check": {
+    "branch": "bm/v2-p08",
+    "common_dir": "/home/administradorarthur/code/scanplant-current/ScanPlant/.git",
+    "git_dir": "/home/administradorarthur/code/scanplant-current/ScanPlant/.git/worktrees/p08",
+    "safe": true
+  },
+  "route": {
+    "route": "v2-standalone",
+    "superpowers_required": false
+  },
+  "state": {
+    "method_version": 2,
+    "valid": true
+  },
+  "snapshot": {
+    "algorithm": "sha256-manifest-v1",
+    "digest": "6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a",
+    "manifest": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/approval/manifest-p08.sha256"
+  },
+  "planning-audit": {
+    "budget_exceeded": [],
+    "limits": {
+      "execution_units": 40,
+      "max_execution_unit_words": 8000,
+      "max_plan_words": 16000,
+      "plans": 16,
+      "platforms": 6,
+      "shared_context_words": 24000
+    },
+    "metrics": {
+      "execution_units": 9,
+      "max_execution_unit_words": 859,
+      "max_plan_words": 926,
+      "package_words": 58443,
+      "plans": 8,
+      "platforms": 2,
+      "shared_context_words": 3052
+    },
+    "profile": "standard",
+    "quality_contract": "planning-quality-v2",
+    "readiness": {
+      "counts": {
+        "assumptions": 11,
+        "decisions": 24,
+        "design_surfaces": 0,
+        "pitfalls": 20,
+        "spec_deltas": 6,
+        "spikes": 5,
+        "user_actions": 11
+      },
+      "coverage_gaps": [],
+      "design": null,
+      "design_required": false,
+      "scope_digest": "1ad0136669f82fcf9307b7dce287f544ed256c1205a70e2a717a041867167197",
+      "spec_deltas": [
+        {
+          "id": "SD-001",
+          "source": "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
+          "target": "docs/bianchini/current/specs/replan-v2.md"
+        },
+        {
+          "id": "SD-006",
+          "source": "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
+          "target": "docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md"
+        },
+        {
+          "id": "SD-101",
+          "source": "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
+          "target": "docs/bianchini/current/specs/provider-benchmark-decision.md"
+        },
+        {
+          "id": "SD-201",
+          "source": "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
+          "target": "docs/bianchini/current/specs/offline-class-manifest.md"
+        },
+        {
+          "id": "SD-701",
+          "source": "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md",
+          "target": "docs/bianchini/current/specs/traceable-dataset-curation.md"
+        },
+        {
+          "id": "SD-801",
+          "source": "docs/bianchini/changes/v2/spec-deltas/dataset-recovery.md",
+          "target": "docs/bianchini/current/specs/dataset-recovery.md"
+        }
+      ],
+      "status": "ready"
+    },
+    "recommended_profile": "standard",
+    "research_mode": "targeted_web",
+    "valid": true,
+    "warnings": []
+  },
+  "hygiene": {
+    "ignore_rule": "/.superpowers/",
+    "tracked_root_artifacts": [],
+    "valid": true
+  },
+  "diff-check": {
+    "exit_code": 0,
+    "output": ""
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md b/artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md
new file mode 100644
index 0000000..c1100e8
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md
@@ -0,0 +1,2539 @@
+# Review Package
+
+- Base: `7981377a433270c9e2072fcafdf89b690988fa08`
+- Head: `HEAD`
+- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md` (a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36)
+- Report: `artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md` (29f0379d43191f8030a94edf9496e43a15bbe2a3e636e660ef2ab6392ed28498)
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
+## Uncommitted technical annex — not a submitted guard delta
+
+The user prohibits commit/staging/push; this is independent technical review of round 1, not guard review. Review only B1 and actual delta regressions; return JSON findings. Reconstruct interrupted review from this package. No test rerun or mutations needed.
+
+# Implementer Report — P08 B1, round 1
+
+- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md`
+- Status: TECHNICAL_FIX_READY_FOR_REVIEW; acceptance and commit pending.
+
+## Changes
+
+The preexisting fix in acquire_inat preserves str(error) only when error is RecoveryError and its code already belongs to RETRYABLE. All other caught errors retain inaturalist_contract_or_evidence. RETRYABLE itself is unchanged. The previous unconditional classification made a transient metadata timeout permanently skipped on restart by acquire.
+Three existing synthetic tests cover timeout/restart/success, preserved journal prefix and config, cumulative request quotas, no premature page/cursor or candidate, one candidate exactly once, stable subsequent invocation, and fail-closed classification of contract/integrity/budget failures.
+
+## Verification
+
+Reused signed RED proof-6928ea925e6f438e3873543389326106 on original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 only as historical defect evidence. Additional RED ran the three new tests against original production bytes (12 failed assertions). Reconciled current source/output fingerprints for GREEN: 3 new tests, 54 recovery, 15 adapter, 236 affected/history tests with five materially reached/killed selective mutants. These are working-byte records, not proofs for a future SHA. No test suite rerun during this resumption.
+Fresh read-only Method preflight, diff check, complete evidence hash reconciliation and external bytes/mtime comparison passed. All unchanged suite dependencies match original HEAD; both modified files match the previous GREEN records. No network acquisition or downloads. See evidence-reconciliation.json.
+
+## Decisions
+
+Reuse round 1, existing correction, original commit and all documentary recovery. implementation_detail decision already recorded by bm change-policy. No start/red/fix command repeated. No staging, commit or push. The official review-package for base=head is an empty committed delta; its explicitly labeled working-tree annex enables technical review only. Formal submit-delta/review and fresh gates must wait for a separately authorized own commit.
+
+## Concerns
+
+Guard stays fixing, B1 open, round 1, redesign 0. P08 remains blocked, release pending. Historical human acceptance does not accept new bytes. External config/code fingerprint and old receipts remain intact and must not be silently migrated; new code is not authorized against the real dataset. 1088 pending candidates, zero transfers/approved_for_dataset/usable, no real iNaturalist crosswalk, no training, no P09.
+
+```diff
+diff --git a/scripts/phase1/recover_p08.py b/scripts/phase1/recover_p08.py
+index 3def6c1..3e74f9b 100644
+--- a/scripts/phase1/recover_p08.py
++++ b/scripts/phase1/recover_p08.py
+@@ -549,21 +549,22 @@ def acquire_inat(ds,cls,transport,fixture):
+                             taxonomic_confidence=initial['taxonomic_confidence'])
+                 records.append(item)
+             page=ds.save_page('inaturalist',cid,0,records,None)
+             ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
+                                       'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
+         for c in page['candidates']:
+             ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
+         ds.advance(page)
+         return 'budget_reached'
+     except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
+-        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':'inaturalist_contract_or_evidence'})
++        code=str(error) if isinstance(error,RecoveryError) and str(error) in RETRYABLE else 'inaturalist_contract_or_evidence'
++        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':code})
+         return 'source_blocked'
+ 
+ 
+ def acquire(ds,fixture=None):
+     transport=Transport(ds)
+     if fixture is not None:require(ds.offline,'fixture_mode')
+     elif ds.offline:raise RecoveryError('fixture_required')
+     for cls in canonical():
+         for source in SOURCES:
+             cid=cls['class_id']
+diff --git a/scripts/phase1/test_recover_p08.py b/scripts/phase1/test_recover_p08.py
+index aeb8b53..383cb8a 100644
+--- a/scripts/phase1/test_recover_p08.py
++++ b/scripts/phase1/test_recover_p08.py
+@@ -499,20 +499,124 @@ class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
+             kinds = [event['type'] for event in ds.events]
+             self.assertLess(kinds.index('page'), kinds.index('intention'))
+             self.assertLess(kinds.index('committed'), kinds.index('cursor'))
+         before = r.tree_fingerprint(self.root)
+         (media/'123').unlink()  # A repeated execution must use the durable objects.
+         process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
+         self.assertEqual(process.returncode, 0, process.stderr)
+         self.assertEqual(before, r.tree_fingerprint(self.root))
+ 
+ 
++class InaturalistResumeTests(DatasetCase, unittest.TestCase):
++    def prepare_round(self, request_cap=4):
++        from test_inaturalist_source import crosswalk, observation, page
++        cls = r.canonical()[0]
++        entry = crosswalk()
++        evidence = b'synthetic reviewed crosswalk evidence\n'
++        entry['taxonomy_ref_ids'] = cls['taxonomy_ref_ids']
++        entry['evidence'].update(path='evidence/crosswalk.json', sha256=r.sha(evidence))
++        self.config['crosswalk'][cls['class_id']] = entry
++        self.config['limits']['requests'] = request_cap
++        with self.open() as ds:
++            r.persist(ds.path(entry['evidence']['path']), evidence, immutable=True)
++            # Commons is already accounted for; exercise only the iNaturalist seam.
++            for item in r.canonical():
++                ds.append('source_status', {'source': 'commons', 'class_id': item['class_id'],
++                          'status': 'exhausted_within_query' if item['kind'] == 'species' else 'protection_not_queried'})
++        return cls, r.encode(page(observation()))
++
++    def test_timeout_then_restart_preserves_journal_limits_and_candidates(self):
++        cls, response = self.prepare_round()
++        config_bytes = (self.root/'config.json').read_bytes()
++        with self.open() as ds:
++            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
++            self.assertEqual(r.acquire(ds), 1)
++            self.assertEqual(factory.call_count, 3)
++            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
++            self.assertEqual(len(ds.select('request')), 3)
++            self.assertEqual([x['code'] for x in ds.select('response')], ['timeout'] * 3)
++            self.assertEqual(ds.select('page'), [])
++            self.assertEqual(ds.select('cursor'), [])
++            self.assertEqual(ds.records(), [])
++        prefix = (self.root/'journal.jsonl').read_bytes()
++        with self.open() as ds:
++            _, factory, _, _ = TransportTests.transport(self, ds, [FakeResponse(body=response)])
++            self.assertEqual(r.acquire(ds), 0)
++            self.assertEqual(factory.call_count, 1)
++            self.assertEqual(len(ds.select('request')), self.config['limits']['requests'])
++            self.assertEqual(len(ds.select('response')), 4)
++            self.assertEqual(len({x['request_id'] for x in ds.select('request')}), 4)
++            self.assertEqual(len(ds.select('page')), 1)
++            self.assertEqual(len(ds.select('cursor')), 1)
++            self.assertEqual(len(ds.records()), 1)
++            self.assertEqual(ds.records()[0]['state'], 'needs_license_review')
++            self.assertEqual(ds.records()[0]['class_ids'], [cls['class_id']])
++            self.assertEqual(ds.select('intention'), [])
++            self.assertEqual(ds.select('committed'), [])
++            kinds = [e['type'] for e in ds.events]
++            self.assertLess(kinds.index('evidence'), kinds.index('page'))
++            self.assertLess(kinds.index('page'), kinds.index('classified'))
++            self.assertLess(kinds.index('classified'), kinds.index('cursor'))
++            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
++            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
++            self.assertEqual(ds.config['limits'], self.config['limits'])
++            self.assertEqual(ds.summary()['usable'], 0)
++        stable = r.tree_fingerprint(self.root)
++        with self.open() as ds:
++            _, factory, _, _ = TransportTests.transport(self, ds, [])
++            self.assertEqual(r.acquire(ds), 0)
++            self.assertEqual(factory.call_count, 0)
++            self.assertEqual(r.tree_fingerprint(self.root), stable)
++
++    def test_only_existing_transient_recovery_codes_allow_restart(self):
++        cls, _ = self.prepare_round()
++        errors = [(r.RecoveryError(code), code) for code in sorted(r.RETRYABLE)]
++        errors += [(r.RecoveryError(code), 'inaturalist_contract_or_evidence') for code in
++                   ['http_403', 'http_404', 'request_budget', 'crosswalk_evidence_hash', 'invalid_json', 'unsafe_url']]
++        errors += [(r.inat.ContractError('timeout'), 'inaturalist_contract_or_evidence'),
++                   (OSError('timeout'), 'inaturalist_contract_or_evidence'),
++                   (KeyError('timeout'), 'inaturalist_contract_or_evidence')]
++        with self.open() as ds:
++            for error, expected in errors:
++                with self.subTest(error=type(error).__name__, code=str(error)):
++                    with patch.object(r.Transport, 'get', side_effect=error) as get:
++                        self.assertEqual(r.acquire_inat(ds, cls, r.Transport(ds), None), 'source_blocked')
++                    self.assertEqual(get.call_count, 1)
++                    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
++            self.assertEqual(ds.select('page'), [])
++            self.assertEqual(ds.select('cursor'), [])
++
++    def test_timeout_restart_does_not_reset_request_budget(self):
++        self.prepare_round(request_cap=3)
++        with self.open() as ds:
++            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
++            self.assertEqual(r.acquire(ds), 1)
++            self.assertEqual(factory.call_count, 3)
++            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
++        prefix = (self.root/'journal.jsonl').read_bytes()
++        config_bytes = (self.root/'config.json').read_bytes()
++        with self.open() as ds:
++            _, factory, _, _ = TransportTests.transport(self, ds, [])
++            self.assertEqual(r.acquire(ds), 1)
++            self.assertEqual(factory.call_count, 0)
++            self.assertEqual(len(ds.select('request')), 3)
++            self.assertNotIn(ds.select('source_failure')[-1]['code'], r.RETRYABLE)
++            self.assertEqual(ds.records(), [])
++            self.assertEqual(ds.select('page'), [])
++            self.assertEqual(ds.select('cursor'), [])
++            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
++            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
++            stable = r.tree_fingerprint(self.root)
++            self.assertEqual(r.acquire(ds), 1)
++            self.assertEqual(r.tree_fingerprint(self.root), stable)
++
++
+ class ContinuationProofs(DatasetCase, unittest.TestCase):
+     def test_inspect_html_identical_after_journal_reload(self):
+         with self.open() as ds:
+             ds.ingest(candidate(),lambda _:image_bytes())
+             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
+         before=r.tree_fingerprint(self.root)
+         with self.open() as ds:
+             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
+         self.assertEqual(before,r.tree_fingerprint(self.root))
+ 
+
+```
+
+### artifacts/bianchini/v2/codex/P08/task-brief.md
+
+```text
+# Task Brief 1
+
+- Plan: `docs/bianchini/changes/v2/plans/P08-dataset-recovery.md`
+- Plan SHA-256: `1d7e4dd67033c9ff28ebf5a2463c12b5ff7b9795b2701b899addafc12ba1acfe`
+- Kind: `task`
+- Group ID: `n/a`
+- Group SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`
+- Unit `1` SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`
+
+### Tarefa 1 — obter e preservar candidatos com decisões rastreáveis e aceite final
+
+**Execution:** strict
+**Review:** per_task
+**Change:** data-transform
+**Readiness refs:** D-801, D-802, D-803, D-804, D-805, A-801, A-802, P-801, P-802, U-801, U-802, U-803, U-804, S-801, SD-801
+**Test seams:** p08-source-contract, p08-taxonomic-map, p08-journal-integrity, p08-sanitization, p08-human-approval.
+**Spec refs:** docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md §1 autoridade; §2 arquitetura/CLI; §3 fontes/limites; §4 taxonomia/consultas; §5 direitos/storage; §6 journal; §7 triagem/estados; §8 resultado; §9 testes/aceite.
+**Files:** criar scripts/phase1/recover_p08.py, scripts/phase1/inaturalist_source.py, scripts/phase1/test_recover_p08.py, scripts/phase1/test_inaturalist_source.py, scripts/phase1/test_p08_mutation.py, docs/phase1/P08-recovery.md, artifacts/phase1/p08/summary.json e artifacts/bianchini/v2/ledgers/P08.md; atualizar somente campos P08 de docs/living/PROJECT_STATE.md no fechamento futuro. Ler funções puras acquire_commons.py/curate_p07.py, requirements-p06.txt, manifesto canônico/roster e evidências P07; esses arquivos históricos permanecem inalterados. Config, crosswalk, imagens, journal, decisões e atribuição somente no diretório externo autorizado por U-802.
+**Contract:** cumprir integralmente §§1–9 da spec. Após U-801 e autorização separada de implementação, construir extensão delimitada com stdlib/Pillow existente. RED deve comprovar que cada fronteira nova falha antes da implementação; GREEN cobre fixtures e replay. Não promover confiança comunitária a perícia, licença abreviada a autorização, título a taxon ID ou sanitização a privacidade. Commons+iNaturalist condicionais; demais fontes blocked, tetos 100 candidatos/20 transferências por fonte/classe, limites cumulativos de bytes/páginas/requisições. Preservar original servido e sanitizado por SHA, sem alegar original de câmera iNaturalist. Journal precede side effects e não reescreve eventos. A mesma entrega incorpora correção mínima do estado P07 publicado, já materializada documentalmente neste pacote.
+**Verification:** no cwd da worktree P08, usar Python persistente P07 3.14.4/Pillow12.3.0. Fast: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_recover_p08.py'` e o mesmo comando com `test_inaturalist_source.py`; esses dois arquivos são entregáveis futuros, não testes alegadamente existentes. Plan: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'`, incluindo harness seletivo test_p08_mutation.py criado na entrega; `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`; `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS`; `git diff --check`. Gate espera saída 0, todos contratos executados, zero sobrevivente material dos cinco desvios §9, não número arbitrário de testes. Ambiente ausente bloqueia, não instalar automaticamente. Rede real só após U-802/U-803 e contratos offline passed; verify futuro prova journal, hashes/P07 17/17, aceites e allowlist. Gate release histórico continua blocked e não será executado ou substituído por unittest.
+**Done when:** uma rodada autorizada contábil para as 14 classes, com esgotamento/limite/bloqueio por fonte explícito, originais/sanitizados/backup íntegros, P07 17/17 preservados, testes e revisão independente passed, parecer humano final por item incluindo pendências legítimas, atribuição completa e recibo U-804 do digest final. Falta de perito mantém pendências, podendo aceitar resultado zero; falta de autorização de execução/aceite ou falha de integridade impede completed. Zero aprovado e treinamento bloqueado são resultados válidos; nenhum mínimo de piloto, suficiência, split ou treino será criado.
+
+Sequência dentro da unidade: confirmar autorização/workspace/baseline; validar manifesto/crosswalk/config; produzir RED/GREEN do percurso completo fake; implementar transporte/journal/curadoria/exportação limitados; executar regressão/mutação seletiva/revisão; somente com U-802, autorizar efeitos externos em rodada limitada; inspecionar/reconciliar com P07; obter U-803 por item e preservar inconclusões; gerar relatórios/backup/manifesto de bytes; obter U-804 e encerrar documentalmente. Revisão humana de fonte/ID/licença é requisito antes do download quando necessário. Não inventar prova para ultrapassar essas pausas.
+
+A-801/A-802 limitam incerteza: fontes podem não fornecer candidatos elegíveis nem IDs/licenças suficientemente documentados. Fallback é fonte/item bloqueado e resultado vazio, sem expandir API/host/licença. P-801 impede aceite indevido; P-802 exige lock/durabilidade/hash/allowlist. U-801 autoriza somente pacote; U-802 ambiente e rede, U-803 qualificação/crosswalk/parecer, U-804 bytes finais. Sem staging, commit, push, merge/tag ou execução nesta sessão de planejamento. Sem autorização futura explícita dessas operações.
+
+```
+
+### docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md
+
+```text
+# P08 — recuperação limitada e rastreável do dataset
+
+## 1. Objetivo e autoridade
+
+D-801, D-805, A-801, U-801: enfrentar a insuficiência P07 mediante candidatos novos, verificáveis e preservados. Baseline b6844f9129d9edf862ae7958d8f043d9bdd5bd84, P07 completed/publicado, guard completed sem blockers, U-701/U-702 aceitas, 17 imagens: 2 rejected_quality, 8 needs_botanical_review, 7 needs_human_review, 0 approved_for_dataset/usable. As 14 classes estão sem aprovação; species_04 e species_08 e as duas proteções sem candidatos. Aceite anterior aceitou pareceres, não qualidade/identidade botânica das imagens. P06/P07 fechados não são reabertos. Preservar bloqueios históricos P01/P03 e release pending.
+
+Só planejamento autorizado agora, sem código, rede de aquisição, download, staging, commit ou push. Aprovar este pacote não executa a coleta nem autoriza publicação. Excluídos do P08 treinamento, comparação de modelos, augmentation, partições train/validation/test, exportação TFLite, integração mobile/API, fluxo do produto, homologação, release, P09, merge/tag. Sem interface: design_required=false. Sem benchmark de modelo ou meta de suficiência.
+
+## 2. Arquitetura delimitada
+
+S-801, P-802: Python/Pillow 12.3.0/stdlib em Linux/WSL. Criar scripts/phase1/recover_p08.py como CLI/orquestração limitada e scripts/phase1/inaturalist_source.py como adapter; reutilizar funções puras de acquire_commons.py e curate_p07.py sem alterar contratos ou outputs P06/P07. CommonsClient existente pode servir consulta, mas transporte P08 deve impor Retry-After/orçamento de rede; nunca herdar sua pausa 0.25s como suficiente. Não chamar collect/_collect_locked P06 nem reconcile/run/validate_decisions P07 para dados novos: schemas fixos e journal inadequado. Métricas JPEG reutilizadas; para PNG usar mesmas funções de pixels sem transcodificar a imagem de dataset só para satisfazer P07. Nenhuma nova dependência pesada ou atualização de Pillow.
+
+Seams públicos: p08-source-contract, p08-taxonomic-map, p08-journal-integrity, p08-sanitization, p08-human-approval. Externos: APIs públicas de metadados e hosts de mídia explicitamente permitidos; armazenamento local privado; revisor humano. Não há integração no app/API do ScanPlant. Configuração versionada de execução declara versão de schema, digest do manifesto, políticas/consultas/limites, fingerprints de código/ambiente e fontes; mudança material invalida retomada, não migra silenciosamente.
+
+CLI futura (contrato a implementar, não comandos existentes): recover_p08.py com subcomandos acquire, inspect, finalize e verify. acquire exige --config e --output; inspect exige --output e --p07-source; finalize exige --output e --decisions; verify exige --output, --p07-source e, no fechamento, --acceptance. Um --offline-fixture para testes deve impedir toda rede e usar fixtures geradas fora do Git. Sucesso limitado/zero retorna 0; fonte/gate indisponível retorna 1; configuração/schema/hash/IO inválido retorna 2. Saída textual contém códigos seguros, não corpos HTTP/proveniência. Nenhum comando implementado ou executado neste planejamento.
+
+## 3. Fontes e limites
+
+D-802/D-803, A-802, U-802: após autorização separada de execução, Commons e iNaturalist são fontes elegíveis somente pelos contratos abaixo. GBIF, cache GBIF, publishers genéricos, PlantCLEF, Pl@ntNet-300K e qualquer fonte não listada têm acquisition_enabled=false, teto 0. Sem fallback silencioso de fonte/licença. Fonte elegível que não comprove schema/termos necessários termina blocked_source; não força atividade em outra fonte.
+
+Commons: GET https://commons.wikimedia.org/w/api.php, generator=search, namespace 6, nome científico canônico entre aspas, imageinfo url/mime/size/timestamp/sha1/extmetadata. Usar continue/gsroffset validados, guardar página pendente/índice antes de avançar. Mídia apenas HTTPS upload.wikimedia.org, URL original retornada, sem thumbnails. ID de arquivo pageid/revisão é identidade da mídia; não é ID taxonômico. Sem inferência de espécie por categoria/título isolado.
+
+iNaturalist: GET público https://api.inaturalist.org/v1/observations, taxon_id do crosswalk aprovado, photos=true, quality_grade=research, order_by=id, order=asc, per_page=100; confirmar filtros/shape no schema oficial durante implementação autorizada e fixture de contrato. Taxon ID identifica espécie aceita, não aceitar descendente/híbrido automaticamente. Página/índice de foto e id_above após página consumida, checkpoint de cutoff temporal da rodada para não incorporar observações posteriores. Research grade filtra candidatos, nunca aprova. Dados/metadados da observação têm exame de licença independente. Fotos via HTTPS inaturalist-open-data.s3.amazonaws.com/photos/{photo_id}/original.{ext}, somente quando relação ID/extensão/URL estiver provada no contrato oficial/resposta. Não trocar string de thumbnail arbitrariamente. Páginas www.inaturalist.org/observations/{id} e /photos/{id} servem evidência; não scraper genérico. Link legal por foto deve comprovar versão. Se API trouxer apenas código abreviado, evidência legal humana complementar vinculada ao ID é obrigatória antes do download; falta implica needs_license_review sem baixar. Original aqui é o maior arquivo disponibilizado pelo serviço, que pode ser redimensionado; origin_fidelity=provider_original, camera_original_verified=false. Não inventar acesso à câmera nem baixar dumps do Open Data.
+
+Tetos cumulativos da rodada, persistidos inclusive entre invocações: por fonte/classe até 100 candidatos distintos examinados e 20 IDs reservados para transferência, mesmo que depois falhem/rejeitem. Commons até 10 páginas de 10; iNaturalist até 1 página de 100 observações, examinando no máximo 100 fotos, resto conhecido deferred_budget. Até 240 transferências distintas/fonte, 480 totais, não promessa de arquivos/aprovações. Repetir item para recuperação consome requisições/bytes, não cria vaga ou reseta teto. Proteções: zero consultas/transferências. Até 1000 requisições por fonte/rodada, 1 GiB de mídia total/rodada, 256 MiB/h; cada arquivo até 20 MiB, total recebido contabilizado mesmo em falha. Teto mais restritivo vence. Originais + sanitizados até 2 GiB para rodada; exigir ao menos 3 GiB livres no destino e parada segura antes de esgotar disco. São limites pequenos para revisar manualmente e conter custo, não número necessário para treino. Nenhum aumento automático se poucas aprovações.
+
+Transporte: uma conexão global, ≥1s entre requisições, User-Agent identificável com URL pública do projeto. timeout 20s; até duas novas tentativas por requisição e orçamento global; 403/404 sem retry. 429/503/maxlag: respeitar Retry-After (segundos/data), maxlag=5 Commons, backoff 2/4s quando sem instrução; espera exigida maior que orçamento encerra com resume_after, nunca encurta espera. 500/502/504/timeout retomáveis no mesmo teto. Sem proxies/IPs/chaves para contornar quotas. Validar HTTPS, host/porta, redirects em cada salto e IP público; negar loopback/rede privada, userinfo, portas não padrão, traversal e URLs externas ao contrato. Mudança de host/termos exige nova autorização/avaliação, não expansão dinâmica de allowlist.
+
+## 4. Taxonomia e consultas por classe
+
+D-804, U-803, P-801: única verdade de IDs/ordem/nomes/normalização é docs/phase1/offline-class-manifest.v1.json 1.1.0, validado contra artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json. Os quatro aliases quarantined ficam excluídos; não expandir sinônimos nesta rodada. Nome comum não participa de busca/mapeamento. Não alterar manifesto/resolver. A tabela deriva do manifesto; divergência bloqueia.
+
+| Índice | Classe | Nome científico e consulta Commons | iNaturalist |
+| --- | --- | --- | --- |
+| 0 | species_01 | "Epipremnum aureum" | taxon_id do crosswalk desta espécie |
+| 1 | species_02 | "Monstera deliciosa" | taxon_id do crosswalk desta espécie |
+| 2 | species_03 | "Zamioculcas zamiifolia" | taxon_id do crosswalk desta espécie |
+| 3 | species_04 | "Spathiphyllum wallisii" | taxon_id do crosswalk desta espécie |
+| 4 | species_05 | "Dracaena trifasciata" | taxon_id do crosswalk desta espécie |
+| 5 | species_06 | "Aloe vera" | taxon_id do crosswalk desta espécie |
+| 6 | species_07 | "Chlorophytum comosum" | taxon_id do crosswalk desta espécie |
+| 7 | species_08 | "Codiaeum variegatum" | taxon_id do crosswalk desta espécie |
+| 8 | species_09 | "Ficus elastica" | taxon_id do crosswalk desta espécie |
+| 9 | species_10 | "Kalanchoe blossfeldiana" | taxon_id do crosswalk desta espécie |
+| 10 | species_11 | "Nephrolepis exaltata" | taxon_id do crosswalk desta espécie |
+| 11 | species_12 | "Tradescantia zebrina" | taxon_id do crosswalk desta espécie |
+| 12 | outra_planta | sem consulta automática | not_applicable_automatic_query |
+| 13 | imagem_invalida | sem consulta automática | not_applicable_automatic_query |
+
+Não preencher IDs numéricos por memória: esta sessão não coletou taxa. Antes de consulta de imagens, um crosswalk externo revisado liga classe, fonte, source_taxon_id com namespace, scientific_name recebido, authorship quando disponível (null com razão quando ausente), rank/status/synonym_of, fonte/URL/versão/data da evidência e revisor. Usar referências taxonômicas já aprovadas no manifesto para reconciliação; ID da comunidade/Wikidata isolado não basta. Fonte sem ID confiável pode gerar candidatos Commons por nome canônico, mas nunca aprovação; iNaturalist sem crosswalk não é consultado. Conflito de autoria/homônimo => needs_botanical_review, sem reintrodução dos quatro aliases.
+
+Cada item registra esse mapeamento e taxonomic_confidence=unmapped|proposed|source_supported|human_validated|conflict; human_validated exige perito identificado, qualificação e evidência visual diagnóstica do item final. IA/Plant.id/dHash/research_grade e sugestão do agente nunca satisfazem confirmação. Botânico pode rejeitar identidade ou declarar inconclusivo. Proteções mantêm definições P05; rejeição técnica não vira imagem_invalida, espécie desconhecida não vira outra_planta. Permanecem vazias, sem geração de exemplos negativos.
+
+## 5. Direitos, entidades e armazenamento
+
+D-803/D-805, P-801/P-802: preservar dados completos somente em diretório P08 externo novo autorizado, nunca P06/P07, Git, /tmp ou pasta compartilhada pública. Permissões diretório 0700/arquivos 0600; responsável mantém backup verificado por hash antes do fechamento. Não incluir originals em páginas de revisão abertas. Original baixado é immutable por SHA256 em originals; derivado sanitizado em quarantine; aprovação cria referência no catálogo, não altera bytes.
+
+Registro privado por item: schema/run/config/manifest/code digests, candidate_id estável derivado de fonte+media_id, todas class associations, source/observation/photo/page/revision IDs, scientific_name recebido, source_taxon_id/namespace, authorship, mapping evidence/confidence/reviewer, query/cursor/timestamps, autor/licensor/credit, license code/version/legal URL/evidence hash, restrições e notices, source_page_url/file_url/resolved_url, MIME/dimensões declaradas/reais, source SHA declarado, original_sha256/sanitized_sha256, sanitization version, origin_fidelity, métricas/estados/razões, duplicate group e decisões humanas por hashes. Campos não disponíveis ficam null com reason, nunca valores inventados. HTML de origem é dado inerte, não renderizar como confiável. Não guardar coordenadas em projeções; snapshots probatórios integrais privados só quando indispensáveis para autoria/licença.
+
+Exigir CC0 1.0 ou CC BY 4.0 com URL legal canônica e evidência por arquivo de titular/autoria/proveniência consistente. Divergência dos campos, multi-licença ambígua, restrição extra, domínio público genérico, NC/ND/SA ou licença ausente/outra versão => needs_license_review ou rejected_license; nunca baixar com base só no rótulo. Obter prova antes dos bytes. Autoria desconhecida bloqueia mesmo CC0 por política de rastreabilidade. Fonte pode ter direitos de banco/observação adicionais: examinar separadamente, bloquear incompatibilidade. Manter evidência temporal; alteração posterior de termos/metadados não apaga histórico nem revoga automaticamente licença anterior, mas suspende promoção até revisão de titularidade.
+
+Attributions.jsonl/NOTICE.md privados ligam cada hash a autor/credit/licensor, título se necessário, página de origem, URL legal, avisos/disclaimer e indicação de alterações (orientação EXIF, RGB, recodificação, remoção de metadados). Gerar bundle de atribuição com cada redistribuição futura, inclusive CC0 por política. Redistribuição não está autorizada agora. BY/CC0 não exigem SA por si; não estender essa conclusão a contratos/terceiros nem declarar licença do futuro modelo/app. SA/NC/ND ficam bloqueadas nesta política. Treinamento requer decisão futura sobre dados efetivos, direitos e protocolo, mesmo com itens aprovados.
+
+## 6. Journal, integridade e retomada
+
+P-802: journal JSONL realmente append-only é autoridade; state/index/report são projeções reconstruíveis. Eventos com seq, timestamp UTC, event_id, prev_event_hash e event_hash (SHA256 de JSON canônico sem event_hash), config digest e tipo; JSON UTF-8/chaves ordenadas/LF final. Lock fcntl exclusivo por dataset; segundo escritor falha antes de rede. Validar prefixo/ordem/hash e hashes de objetos antes de continuar. Snapshot de página + candidatos e reservas durável antes de transferências; cursor só avança após todos os itens consumidos ou explicitamente deferred no checkpoint.
+
+Sequência: reservar orçamento e registrar intenção/fsync; receber bytes limitados em .part externo; hash/verificação; persistir original por rename sem overwrite + fsync diretório; sanitizar/reabrir/verificar metadados e persistir sanitizado igualmente; append evento committed com ambos hashes/fsync; atualizar projeções atomicamente. Original de formato inválido recebido dentro do teto fica preservado em área restrita rejeitada, nunca decodificado em viewer; excesso interrompido não é original completo nem conta como íntegro. Nenhuma falha altera arquivos históricos.
+
+Crash antes/depois de cada fronteira: replay reconcilia apenas objetos já vinculados a intenção e hashes; órfão não é aprovação. Arquivo existente íntegro não é baixado/recodificado; mesmo input/decisão repetido não adiciona evento nem muda bytes/mtime de projeções. Retry de tentativa fracassada adiciona evento e consome orçamento; idempotência não promete congelar API viva. Se original remoto muda, registrar nova revisão pendente, nunca substituir anterior. Journal com linha final parcial/corrupção bloqueia; não truncar/reparar automaticamente. Recuperação humana preserva arquivo original e prefixo validado em segmento novo ligado por digest, ou encerra blocked_integrity. Config/canonical digest incompatível, symlink/path escape, arquivo faltante ou hash divergente bloqueiam aprovação até reconciliação explícita; não reparar P06/P07.
+
+## 7. Triagem e estados
+
+D-804/D-805: aceitar JPEG/PNG, MIME/extensão/formato decodificado coerentes, um frame, até 20 MiB entrada/saída e 25 milhões pixels; verificar corrupção/truncamento/bombas. Aplicar orientação EXIF e reconstruir pixels RGB com função P06 (JPEG qualidade 95); remover EXIF/GPS/XMP/comentários/ICC/text chunks. Não cortar, borrar, melhorar exposição ou fazer augmentation; original intacto. Metadata retirada do arquivo não apaga avisos de atribuição externos. Reabrir arquivo final e confirmar ausência de metadados proibidos.
+
+Métricas P07: menor dimensão <224, aspecto >3, média luminância <40 ou >215, frações pixels <=15 ou >=240 ≥25%, variância Laplaciana <100 geram sinais de revisão, não aceite/rejeição automática de conteúdo. Documentar transformação cinza 256x256 apenas analítica. Inspeção humana da imagem final em resolução disponível registra fotografia/ilustração, derivada, montagem, texto/marca d'água, órgão/espécime vivo ou seco/herbário, alvo único/delimitado, nitidez e exposição. Ilustração/montagem, texto que domina alvo, herbário inadequado ou alvo não identificável são rejected_quality com razão; dúvida => needs_human_review. Não remover marca d'água para tornar utilizável.
+
+Privacidade visual: pessoas/rostos/corpos identificáveis, placas, números/endereço de residências, telas/documentos, localização e sinais sensíveis. Presença/risco não resolvido => rejected_privacy ou needs_privacy_review; ausência de EXIF não basta. Originais mantidos com acesso restrito para auditoria; não publicados. Botânico inspeciona imagem final, fonte e crosswalk; insuficiência => needs_botanical_review; incompatibilidade => rejected_label. Aprovação requer confirmação pericial explícita, não simples aceite de parecer do agente.
+
+Dedup global: media ID, original SHA256, sanitizado SHA256, aliases de proveniência e dHash64 P07. Comparar novos entre si e contra os 17 SHA/dHash P07, inclusive rejeitados/pendentes, sem promovê-los/rejeitá-los novamente. Hash original P07 só se evidência histórica o possuir; não inventar original perdido. Recalcular dHash das cópias sanitizadas preservadas em leitura. Distância <=6 sinal near_duplicate; 7..10 borderline; >10 não prova diferença (pares P07 a distância35 reforçam revisão). Pares sinalizados e mesma observação/série exigem decisão humana distinct/duplicate/pending; conflito de classe no mesmo objeto bloqueia todas associações. Rejeição exata por hash não apaga arquivo; ponteiro duplicate_of mantém referência. Grupo perceptual decidido por humano, nunca limiar como verdade.
+
+Estados derivados de gates independentes: discovered, needs_license_review, needs_taxonomic_mapping, deferred_budget, transfer_failed, quarantined, needs_human_review, needs_privacy_review, needs_botanical_review, needs_duplicate_review, rejected_license, rejected_format, rejected_quality, rejected_privacy, rejected_label, rejected_duplicate, approved_for_dataset. Razões múltiplas preservadas; estado principal prioriza rejeição definitiva, depois pendências licença/taxonomia/transferência/técnica/privacidade/botânica/duplicidade e finalmente aprovado. approved_for_dataset exige todos gates passed, hashes íntegros, original preservado, atribuição pronta, revisão humana final+botânica pericial e pares resolvidos. Nenhuma flag computada promove automaticamente. Qualquer mudança de bytes/decisão/mapeamento invalida aceites dependentes.
+
+## 8. Resultado, suficiência e conclusão
+
+A-801, U-804: por classe/fonte informar teto operacional, encontrados (IDs examinados, não estimativa total da API), transferidos, tecnicamente íntegros, licença válida, rótulo pericial validado, aprovados, rejeitados e pendentes. Os gates são conjuntos independentes; aprovados pertencem à interseção, não somar contagens como funil automático. Contar global por objeto e por classe explicitamente, sem duplicação inflar approved. Todas 14 classes aparecem na ordem original.
+
+Classe vazia distingue not_attempted/authorization_missing, no_crosswalk, source_blocked, exhausted_within_query, budget_reached, all_rejected, review_pending e protection_not_queried. Esgotar consulta não prova ausência universal da espécie. Minimum_experimental_pilot=null (não estabelecido neste escopo); scientific_sufficiency=not_demonstrated, production_sufficiency=not_demonstrated, training_authorized=false, partition_authorized=false, training_status=blocked. Usable representa aprovados para catálogo após aceite final, nunca autorização/suficiência de treinamento.
+
+No Git só código/testes sintéticos futuros, manual P08 e resumo de enums/contagens/IDs internos opacos/classes/hash dos recibos e objetos aceitos. Nunca imagens/base64, paths privados, autores/revisores identificáveis, URLs de itens, GPS/EXIF, respostas brutas, HTML ou texto livre de pareceres. Relatórios externos incluem proveniência completa; exportação pública allowlist rejeita campo extra e é inspecionada por humano. Estado vivo recebe apenas referência sanitizada de resultado e conserva release pending/active_execution null ao terminar.
+
+Conclusão do mecanismo+rodada exige todas classes contabilizadas, reservas/cursos/respostas reconciliados, journal válido, dados preservados/backup, comparação P07 17/17, testes/gates passed, revisão dos candidatos com estados explícitos (pendências legítimas), bundle de atribuição, relatório fiel, revisão independente e recibo U-804 dos hashes finais. Zero aprovadas, fontes bloqueadas e treino bloqueado podem ser conclusão aceita; falha não resolvida de integridade, licença indevidamente promovida, vazamento, acesso P07 ausente, gate indispensável indisponível ou ausência de aceite impedem conclusão. Interromper uma fonte por termos/limite não significa execução técnica total passed; relatar source_blocked e submeter resultado limitado ao humano. Não requer forçar candidato por classe nem resolver botânica inconclusiva.
+
+## 9. Verificação futura e aceite
+
+Uma unidade strict, risco high localizado de persistência/autoridade; perfil standard; revisão independente e RED/GREEN nos seams modificados. Testes sintéticos com transport fake e rede proibida: licenças/names/version/URL contraditórios, licença foto diferente observação, direitos de banco, falta autor, espécie homônima/alias quarantined/nome comum/source ID ausente, rótulo pericial false; todos gates booleanos e desconhecidos; JPEG/PNG válidos/truncados/limites 20MiB/25M/1 frame; EXIF/GPS/XMP e orientação; métricas abaixo/igual/acima dos limites; dHash 6/7/10/11 e duplicata exata cruzando fonte/P07/classe; imagens sintéticas de texto/montagem apenas exercitam sinais e estados, não alegam detector universal.
+
+Fronteiras de IO: crash em cada etapa de §6, disco cheio/fsync/rename/linha parcial, arquivo órfão/faltante/corrompido, alteração config/manifesto, lock concorrente, malicious redirects/SSRF/symlink/traversal, esquema API incompleto, paginação repetida/regressiva, cursor no meio, teto atingido com zero aprovados, orçamento cumulativo após restart, Retry-After e cancelamento. Testar CLI success/zero/error/exit codes, replay byte+mtime estável e projeção allowlist. Contadores/report de 14 classes sem coerção para treino. P06/P07 regressão sem alteração de bytes.
+
+Mutação seletiva requerida por policy: aprovar previamente harness stdlib unittest.mock em scripts/phase1/test_p08_mutation.py, sem instalação. Injetar, um por vez, bypass licença, bypass perito, ignore_hash_mismatch, advance_cursor_before_commit e allow_private_export; executar contratos focais em subprocesso e exigir falha do teste para cada desvio material. Harness prova alteração do ramo (não stub irrelevante), descarta cópia temporária externa após ensaio; gate falha se mutante sobreviver/nenhum teste rodar. Sem score global, sem reativar campanha .NET histórica. Evidência por fingerprint do código/testes e comandos; não executar mutação na fase fast nem agora.
+
+U-804: manifesto final privado inclui journal/objetos/decisões/attribution/relatórios e resumo sanitizado; recibo separado aponta digest, revisor/data/escopo e decisão. Recibo não entra em seu próprio digest. Aceite verifica bytes finais e possibilidade legítima de zero/pendências; não equivale a treino. Alteração posterior exige novo recibo. Staging/commit/push futuros só após esse aceite e autorização explícita separada, nunca nesta sessão.
+
+SD-801: contrato completo esperado em spec-deltas/dataset-recovery.md; current/specs congelado/ausente, sem sincronização neste planejamento.
+
+```
+
+### scripts/phase1/recover_p08.py
+
+```text
+"""P08 bounded recovery. Private datasets, append-only journal, explicit human gates.
+
+No training or automatic botanical/privacy approval. P06/P07 are read-only inputs.
+"""
+import argparse
+from collections import Counter
+from datetime import datetime, timezone
+from email.utils import parsedate_to_datetime
+import fcntl
+import hashlib
+from html import escape
+import http.client
+from io import BytesIO
+import ipaddress
+import json
+import os
+from pathlib import Path
+import re
+import shutil
+import socket
+import ssl
+import stat
+import sys
+import time
+from urllib.parse import urlencode, urlsplit, unquote, urljoin
+import PIL
+from PIL import Image
+import acquire_commons as commons
+import inaturalist_source as inat
+from curate_p07 import dhash, flags_for, laplacian_variance
+from validate_offline_manifest import validate_manifest
+
+ROOT = Path(__file__).resolve().parents[2]
+MANIFEST = ROOT/'docs/phase1/offline-class-manifest.v1.json'
+ROSTER = ROOT/'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'
+MAX_BYTES = 20*1024*1024
+SOURCES = ('commons','inaturalist')
+RETRYABLE={'timeout','network_error','response_timeout','http_429','http_500','http_502','http_503','http_504','maxlag','resume_after'}
+STATES = {'discovered','needs_license_review','needs_taxonomic_mapping','deferred_budget','transfer_failed',
+          'quarantined','needs_human_review','needs_privacy_review','needs_botanical_review','needs_duplicate_review',
+          'rejected_license','rejected_format','rejected_quality','rejected_privacy','rejected_label',
+          'rejected_duplicate','approved_for_dataset'}
+LIMITS = {'candidates':100,'transfers':20,'pages':10,'requests':1000,'media_bytes':1024**3,
+          'hour_bytes':256*1024**2,'storage_bytes':2*1024**3,'file_bytes':MAX_BYTES,'wait_seconds':60}
+SHA = re.compile(r'[a-f0-9]{64}')
+# Exact predecessor from the verified real round. The only behavior change is
+# deterministic key ordering in review HTML; config and acquisition stay frozen.
+HTML_ORDER_PREDECESSOR = '14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57'
+
+class RecoveryError(ValueError): pass
+
+def require(condition,code):
+    if not condition: raise RecoveryError(code)
+
+def sha(raw): return hashlib.sha256(raw).hexdigest()
+def encode(value): return (json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
+def now(): return datetime.now(timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
+def load(raw):
+    def pairs(items):
+        d={}
+        for k,v in items:
+            require(k not in d,'duplicate_json_key');d[k]=v
+        return d
+    try: return json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(RecoveryError('nonfinite_json')))
+    except (UnicodeError,ValueError,TypeError): raise RecoveryError('invalid_json') from None
+
+def safe_path(path):
+    p=Path(os.path.abspath(path))
+    require(not any(q.is_symlink() for q in (p,*p.parents)),'symlink')
+    return p
+
+def read(path):
+    p=safe_path(path)
+    with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
+        require(stat.S_ISREG(os.fstat(f.fileno()).st_mode),'not_regular')
+        return f.read()
+
+def fsync_dir(path):
+    fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
+    try: os.fsync(fd)
+    finally: os.close(fd)
+
+def persist(path,raw,immutable=False):
+    path=safe_path(path)
+    if path.exists():
+        old=read(path)
+        if old==raw:return
+        require(not immutable,'immutable_hash_mismatch')
+    part=path.with_name('.'+path.name+'.'+os.urandom(8).hex()+'.part')
+    fd=os.open(part,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
+    with os.fdopen(fd,'wb') as f: f.write(raw);f.flush();os.fsync(f.fileno())
+    if immutable:
+        try: os.link(part,path,follow_symlinks=False)
+        except FileExistsError: require(read(path)==raw,'immutable_hash_mismatch')
+        part.unlink()
+    else: os.replace(part,path)
+    fsync_dir(path.parent)
+
+def tree_fingerprint(root):
+    return {str(p.relative_to(root)):{'sha256':sha(read(p)),'mtime_ns':p.stat().st_mtime_ns}
+            for p in sorted(Path(root).rglob('*')) if p.is_file()}
+
+def fingerprint():
+    return {p.name:sha(read(p)) for p in [Path(__file__),ROOT/'scripts/phase1/inaturalist_source.py',
+                                        ROOT/'scripts/phase1/acquire_commons.py',ROOT/'scripts/phase1/curate_p07.py'] if p.exists()}
+
+def canonical():
+    m=load(read(MANIFEST)); validate_manifest(m,read(ROSTER))
+    # The historic validator raises on contract violations and returns diagnostics.
+    require(m['manifest_version']=='1.1.0' and len(m['classes'])==14,'canonical_manifest')
+    return m['classes']
+
+def default_config(offline=False):
+    return {'schema_version':1,'run_id':'p08-recovery','manifest_sha256':sha(read(MANIFEST)),
+            'code_sha256':fingerprint(),'python':'.'.join(map(str,sys.version_info[:3])),
+            'pillow':PIL.__version__,'offline':offline,'cutoff':now(),'limits':dict(LIMITS),
+            'sources':list(SOURCES),'crosswalk':{},'legal_evidence':{},'source_contracts':{},
+            'user_agent':'ScanPlant-P08/1.0 (https://github.com/Parys-boop/ScanPlant; dataset-recovery)'}
+
+def validate_config(c,offline):
+    require(set(c)==set(default_config(offline)),'config_fields')
+    require(c['schema_version']==1 and c['offline'] is offline,'config_mode')
+    current=fingerprint();previous={**current,'recover_p08.py':HTML_ORDER_PREDECESSOR}
+    require(c['manifest_sha256']==sha(read(MANIFEST)) and c['code_sha256'] in (current,previous),'config_fingerprint')
+    require(c['python']=='.'.join(map(str,sys.version_info[:3])) and c['pillow']==PIL.__version__=='12.3.0','environment')
+    require(c['sources']==list(SOURCES) and set(c['limits'])==set(LIMITS),'sources_limits')
+    for k,v in c['limits'].items():require(type(v)is int and 0<v<=LIMITS[k],'limit')
+    require(isinstance(c['crosswalk'],dict) and isinstance(c['source_contracts'],dict),'config_schema')
+    require(c['user_agent'].startswith('ScanPlant-P08/') and 'https://github.com/Parys-boop/ScanPlant' in c['user_agent'],'user_agent')
+    require(datetime.fromisoformat(c['cutoff'].replace('Z','+00:00')).tzinfo is not None,'cutoff')
+    canonical()
+
+def safe_url(url,source,media=False):
+    require(isinstance(url,str) and not any(ord(c)<33 for c in url),'unsafe_url')
+    p=urlsplit(url); host=({'commons':'upload.wikimedia.org','inaturalist':'inaturalist-open-data.s3.amazonaws.com'} if media else
+                         {'commons':'commons.wikimedia.org','inaturalist':'api.inaturalist.org'})[source]
+    require(p.scheme=='https' and p.netloc==host and not p.fragment and not p.username and not p.password,'unsafe_url')
+    path=unquote(unquote(p.path));require('\\' not in path and '..' not in path.split('/') and path.startswith('/'),'unsafe_path')
+    if not media:require(p.path==('/w/api.php' if source=='commons' else '/v1/observations'),'unsafe_endpoint')
+    else:
+        require(not p.query and Path(path).suffix.lower() in {'.jpg','.jpeg','.png'},'unsafe_media')
+        if source=='inaturalist':require(re.fullmatch(r'/photos/[1-9][0-9]*/original\.(jpg|jpeg|png)',path),'unsafe_media')
+    return url
+
+def public_addresses(host):
+    addresses=list(dict.fromkeys(row[4][0] for row in socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)))
+    require(bool(addresses) and all(ipaddress.ip_address(a).is_global for a in addresses),'nonpublic_address')
+    return addresses
+
+def candidate_id(c): return 'C'+sha((c['source']+':'+str(c['media_id'])).encode())[:24]
+
+def rights(c):
+    allowed={'cc-by-4.0':({'CC BY 4.0'},'https://creativecommons.org/licenses/by/4.0/'),
+             'cc0':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/'),
+             'cc-zero':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/')}
+    rule=allowed.get(c.get('license_id'))
+    if not rule or c.get('license_name') not in rule[0] or c.get('license_url')!=rule[1]:return 'needs_license_review'
+    if not c.get('author') or re.search(r'\b(unknown|anonymous|desconhecid[oa])\b',c['author'],re.I):return 'needs_license_review'
+    if c.get('restrictions') or c.get('rights_consistent') is not True or c.get('database_rights')!='passed':return 'needs_license_review'
+    if not isinstance(c.get('evidence_sha256'),str) or not SHA.fullmatch(c['evidence_sha256']):return 'needs_license_review'
+    return 'passed'
+
+def sanitize(raw,url,mime):
+    try:
+        clean,suffix=commons.sanitize_image(raw,url,mime)
+        with Image.open(BytesIO(clean)) as im:
+            im.load();require(not im.getexif() and not(set(im.info)&{'exif','xmp','XML:com.adobe.xmp','comment','icc_profile','text'}),'sanitization_metadata')
+        return clean,suffix
+    except commons.AcquisitionError:raise RecoveryError('invalid_image') from None
+
+def technical(raw):
+    with Image.open(BytesIO(raw)) as im:
+        im.load();w,h=im.size;px=list(im.convert('L').resize((256,256),Image.Resampling.LANCZOS).get_flattened_data())
+        mean=sum(px)/len(px);dark=sum(x<=15 for x in px)/len(px);bright=sum(x>=240 for x in px)/len(px)
+        var=laplacian_variance(px,256,256)
+        return {'decode':'ok','width':w,'height':h,'format':im.format,'dhash64':dhash(im),'mean_luminance':mean,
+                'dark_fraction':dark,'bright_fraction':bright,'laplacian_variance':var,'flags':flags_for(w,h,mean,dark,bright,var)}
+
+def review_digest(c):return sha(encode({k:v for k,v in c.items() if k not in {'state','decision'}}))
+
+def decide(c,d):
+    require(d.get('authority')=='human' and d.get('reviewer') and d.get('reviewed_at') and d.get('rationale'),'human_authority')
+    require(all(d.get(k)==c.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256']),'decision_hash')
+    require(d.get('evidence_digest')==review_digest(c),'stale_decision')
+    if rights(c)!='passed':return 'needs_license_review'
+    if not c.get('original_sha256') or not c.get('sanitized_sha256') or c.get('technical',{}).get('decode')!='ok':return 'rejected_format'
+    for key,state in [('quality','rejected_quality'),('privacy','rejected_privacy'),('botanical','rejected_label'),('duplicates','rejected_duplicate')]:
+        if d.get(key)=='rejected':return state
+    for key,state in [('quality','needs_human_review'),('privacy','needs_privacy_review'),('botanical','needs_botanical_review'),('duplicates','needs_duplicate_review')]:
+        if d.get(key)!='passed':return state
+    if not (d.get('expert_confirmation') is True and d.get('qualification') and d.get('botanical_evidence') and
+            isinstance(d.get('mapping'),dict) and d['mapping'].get('confidence')=='human_validated' and
+            d['mapping'].get('source_taxon_id') and d['mapping'].get('evidence_sha256')):return 'needs_botanical_review'
+    if len(c['class_ids'])!=1:return 'needs_botanical_review'
+    cls=next(x for x in canonical() if x['class_id']==c['class_ids'][0]);mapping=d['mapping']
+    if any(mapping.get(k)!=v for k,v in {'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],
+                                        'rank':'species','status':'accepted','taxonomy_ref_ids':cls['taxonomy_ref_ids']}.items()):return 'needs_botanical_review'
+    if not mapping.get('namespace') or not SHA.fullmatch(str(mapping.get('evidence_sha256',''))):return 'needs_botanical_review'
+    visual=d.get('visual',{});privacy=d.get('privacy_checks',{})
+    if set(visual)!={'photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'} or not all(v is True for v in visual.values()):return 'needs_human_review'
+    if set(privacy)!={'people','faces','plates','residences','screens_documents','sensitive_location'} or not all(v=='absent' for v in privacy.values()):return 'needs_privacy_review'
+    pairs=c.get('pairs',[])
+    if any(p.get('signal')=='exact_duplicate' for p in pairs):return 'rejected_duplicate'
+    if any(d.get('pair_decisions',{}).get(p['pair_id'])!='distinct' for p in pairs):return 'needs_duplicate_review'
+    return 'approved_for_dataset'
+
+class Dataset:
+    def __init__(self,root,config,offline=False):
+        self.root=safe_path(root);self.config=config;self.offline=offline;self.events=[];self.fd=None
+        validate_config(config,offline);self.config_hash=sha(encode(config))
+        require(ROOT not in self.root.parents and self.root!=ROOT,'dataset_in_git')
+        if not offline:
+            require(Path('/tmp') not in self.root.parents and self.root.name.startswith('p08-'),'private_p08_root')
+            require(shutil.disk_usage(self.root.parent).free>=3*1024**3,'insufficient_disk')
+    def path(self,name):
+        require(isinstance(name,str) and not Path(name).is_absolute() and '..' not in Path(name).parts,'path_escape')
+        return safe_path(self.root/name)
+    def __enter__(self):
+        self.root.mkdir(mode=0o700,parents=False,exist_ok=True)
+        require(stat.S_IMODE(self.root.stat().st_mode)==0o700,'private_permissions')
+        self.fd=os.open(self.path('.lock'),os.O_RDWR|os.O_CREAT|os.O_NOFOLLOW,0o600)
+        try:
+            try:fcntl.flock(self.fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
+            except BlockingIOError:raise RecoveryError('writer_locked') from None
+            for name in ['originals','quarantine','parts','evidence']:
+                self.path(name).mkdir(mode=0o700,exist_ok=True)
+            self.replay()
+            if not self.events:
+                self.append('config',self.config)
+                persist(self.path('config.json'),encode(self.config),True)
+            else:require(self.events[0]['data']==self.config,'config_changed')
+            self.verify_objects()
+            if self.config['code_sha256']!=fingerprint():
+                transition={'from':self.config['code_sha256'],'to':fingerprint(),'reason':'deterministic_review_html_key_order'}
+                if transition not in self.select('code_compatibility'):self.append('code_compatibility',transition)
+            return self
+        except BaseException:
+            os.close(self.fd);self.fd=None;raise
+    def __exit__(self,*args):
+        if self.fd is not None:os.close(self.fd);self.fd=None
+    def replay(self):
+        p=self.path('journal.jsonl')
+        if not p.exists():return
+        raw=read(p);require(not raw or raw.endswith(b'\n'),'journal_partial')
+        prev='0'*64
+        for seq,line in enumerate(raw.splitlines(keepends=True),1):
+            e=load(line);require(set(e)=={'seq','timestamp','event_id','prev_event_hash','event_hash','config_sha256','type','data'},'event_schema')
+            hashed={k:v for k,v in e.items() if k!='event_hash'}
+            require(encode(e)==line and e['seq']==seq and e['prev_event_hash']==prev and sha(encode(hashed))==e['event_hash'],'journal_hash')
+            require(e['config_sha256']==self.config_hash,'config_changed')
+            self.events.append(e);prev=e['event_hash']
+    def append(self,kind,data):
+        require(self.fd is not None,'lock_required')
+        e={'seq':len(self.events)+1,'timestamp':now(),'event_id':os.urandom(16).hex(),
+           'prev_event_hash':self.events[-1]['event_hash'] if self.events else '0'*64,
+           'config_sha256':self.config_hash,'type':kind,'data':data}
+        e['event_hash']=sha(encode(e))
+        fd=os.open(self.path('journal.jsonl'),os.O_WRONLY|os.O_APPEND|os.O_CREAT|os.O_NOFOLLOW,0o600)
+        with os.fdopen(fd,'ab') as f:f.write(encode(e));f.flush();os.fsync(f.fileno())
+        fsync_dir(self.root);self.events.append(e);return e
+    def select(self,kind):return [e['data'] for e in self.events if e['type']==kind]
+    def verify_objects(self):
+        for e in self.events:
+            d=e['data']
+            if e['type'] in {'received','committed'}:
+                for pathkey,hashkey in [('original_path','original_sha256'),('sanitized_path','sanitized_sha256'),('part_path','original_sha256')]:
+                    if d.get(pathkey):require(sha(read(self.path(d[pathkey])))==d[hashkey],'object_hash_mismatch')
+            if e['type']=='evidence':require(sha(read(self.path(d['path'])))==d['sha256'],'evidence_hash_mismatch')
+    def records(self):
+        result={}
+        for e in self.events:
+            if e['type'] in {'committed','classified'}:result[e['data']['candidate_id']]=dict(e['data'])
+        return list(result.values())
+    def record(self,c):return next((x for x in self.records() if x['candidate_id']==candidate_id(c)),None)
+    def classify(self,c,state,reason):
+        r={**c,'candidate_id':candidate_id(c),'state':state,'reasons':[reason]}
+        self.append('classified',r);return r
+    def save_page(self,source,class_id,cursor,candidates,next_cursor):
+        require(source in SOURCES and class_id.startswith('species_'),'page_class')
+        key=sha(encode([source,class_id,cursor]))
+        old=next((p for p in self.select('page') if p['page_id']==key),None)
+        if old:return old
+        ids=[candidate_id(c) for c in candidates];require(len(ids)==len(set(ids)),'duplicate_page_ids')
+        require(len(ids)<= (10 if source=='commons' else 100),'page_size')
+        pages=[p for p in self.select('page') if p['source']==source and p['class_id']==class_id]
+        require(len(pages)<(self.config['limits']['pages'] if source=='commons' else 1),'page_budget')
+        if next_cursor is not None:require(type(next_cursor)is int and next_cursor>cursor,'cursor_regression')
+        page={'page_id':key,'source':source,'class_id':class_id,'cursor':cursor,'next_cursor':next_cursor,'candidates':candidates}
+        self.append('page',page);return page
+    def advance(self,page):
+        if page['page_id'] in [a['page_id'] for a in self.select('cursor')]:return
+        done={x['candidate_id'] for x in self.records()}
+        require(all(candidate_id(c) in done for c in page['candidates']),'cursor_before_commit')
+        self.append('cursor',{'page_id':page['page_id'],'next_cursor':page['next_cursor']})
+    def ingest(self,c,download,crash=lambda _:None):
+        cid=candidate_id(c);old=self.record(c)
+        if old and not (old['state']=='transfer_failed' and set(old.get('reasons',[])) & RETRYABLE):
+            require(old['source']==c['source'] and old['file_url']==c['file_url'],'remote_revision_changed')
+            if not set(c['class_ids']) <= set(old['class_ids']):
+                old['class_ids']=sorted(set(old['class_ids']) | set(c['class_ids']))
+                old.update(state='needs_botanical_review', reasons=['conflicting_class_associations'])
+                old.pop('decision',None)
+                self.append('classified',old);self.project()
+            for field in ['revision_id','source_timestamp','source_sha1']:
+                if c.get(field)!=old.get(field):
+                    raise RecoveryError('remote_revision_changed')
+            self.project()
+            return old
+        require(c['source'] in SOURCES and c['class_ids'] and set(c['class_ids'])<= {x['class_id'] for x in canonical()[:12]},'candidate_class')
+        if rights(c)!='passed':return self.classify(c,'needs_license_review','individual_rights_unproven')
+        try:safe_url(c['file_url'],c['source'],True)
+        except RecoveryError as error:return self.classify(c,'rejected_format',str(error))
+        if c.get('mime') not in {'image/jpeg','image/png'} or (c.get('declared_size') is not None and
+                (type(c['declared_size'])is not int or not 0<c['declared_size']<=self.config['limits']['file_bytes'])):
+            return self.classify(c,'rejected_format','declared_format_or_size')
+        recv=next((x for x in self.select('received') if x['candidate_id']==cid),None)
+        intents=[x for x in self.select('intention') if x['candidate_id']==cid]
+        if not recv:
+            counts={cls:len({x['candidate_id'] for x in self.select('intention') if x['source']==c['source'] and cls in x['class_ids']}) for cls in c['class_ids']}
+            if not intents and any(n>=self.config['limits']['transfers'] for n in counts.values()):return self.classify(c,'deferred_budget','transfer_budget')
+            intent={'candidate_id':cid,'source':c['source'],'class_ids':c['class_ids'],'attempt':len(intents)+1}
+            self.append('intention',intent);crash('intention')
+            try:raw=download(c)
+            except RecoveryError as error:return self.classify(c,'transfer_failed',str(error))
+            require(isinstance(raw,bytes) and 0<len(raw)<=self.config['limits']['file_bytes'],'file_size')
+            part='parts/'+cid+'-'+str(len(intents)+1)+'.part'
+            persist(self.path(part),raw,True)
+            recv={'candidate_id':cid,'part_path':part,'original_sha256':sha(raw)}
+            self.append('received',recv);crash('received')
+        raw=read(self.path(recv['part_path']))
+        require(sha(raw)==recv['original_sha256'],'object_hash_mismatch')
+        original='originals/'+sha(raw)
+        used=sum(p.stat().st_size for base in ['originals','quarantine'] for p in self.path(base).iterdir() if p.is_file())
+        require(used+(0 if self.path(original).exists() else len(raw))+MAX_BYTES<=self.config['limits']['storage_bytes'],'storage_budget')
+        persist(self.path(original),raw,True);crash('original')
+        rec={**c,'candidate_id':cid,'original_sha256':sha(raw),'original_path':original,'state':'needs_human_review',
+             'sanitized_sha256':None,'sanitized_path':None,'technical':{},'reasons':['human_review_required'], 'pairs':[],'resolved_url':c['file_url'],'config_sha256':self.config_hash,'manifest_sha256':self.config['manifest_sha256'],'code_sha256':self.config['code_sha256']}
+        try:
+            if c.get('source_sha1'):require(hashlib.sha1(raw).hexdigest()==c['source_sha1'],'declared_hash_mismatch')
+            require(c.get('declared_size') in (None,len(raw)),'declared_size_mismatch')
+            clean,suffix=sanitize(raw,c['file_url'],c['mime']);rec['technical']=technical(clean)
+            rec['sanitized_sha256']=sha(clean);rec['sanitized_path']='quarantine/'+sha(clean)+suffix
+            persist(self.path(rec['sanitized_path']),clean,True);crash('sanitized')
+        except RecoveryError as error:rec.update(state='rejected_format',reasons=[str(error)])
+        self.append('committed',rec);crash('committed')
+        self.project();return rec
+    def project(self):
+        persist(self.path('records.json'),encode(self.records()))
+        persist(self.path('summary.json'),encode(self.summary()))
+    def summary(self):
+        recs=self.records();coverage=[]
+        for cls in canonical():
+            for source in SOURCES:
+                subset=[r for r in recs if r['source']==source and cls['class_id'] in r['class_ids']]
+                stopped=[x for x in self.select('source_status') if x['source']==source and x['class_id']==cls['class_id']]
+                status=stopped[-1]['status'] if stopped else ('protection_not_queried' if cls['kind']=='protection' else 'not_attempted')
+                coverage.append({'class_id':cls['class_id'],'source':source,'status':status,'candidate_cap':0 if cls['kind']=='protection' else self.config['limits']['candidates'],
+                                 'transfer_cap':0 if cls['kind']=='protection' else self.config['limits']['transfers'], 'found':len(subset),
+                                 'transferred':sum(bool(r.get('original_sha256')) for r in subset),
+                                 'technical_integrity':sum(bool(r.get('sanitized_sha256')) for r in subset),
+                                 'license_valid':sum(rights(r)=='passed' for r in subset),
+                                 'expert_validated':sum(r['state']=='approved_for_dataset' for r in subset),
+                                 'approved':sum(r['state']=='approved_for_dataset' for r in subset),
+                                 'rejected':sum(r['state'].startswith('rejected_') for r in subset),
+                                 'pending':sum(not r['state'].startswith(('approved_','rejected_')) for r in subset)})
+        result={'schema_version':1,'stage':'pending_human_acceptance','coverage':coverage,'counts':dict(sorted(Counter(r['state'] for r in recs).items())),
+                'unique_objects':len(recs),'usable':0,'minimum_experimental_pilot':None,'scientific_sufficiency':'not_demonstrated',
+                'production_sufficiency':'not_demonstrated','training_authorized':False,'partition_authorized':False,'training_status':'blocked'}
+        validate_public(result);return result
+
+PUBLIC_KEYS={'schema_version','stage','coverage','counts','unique_objects','usable','minimum_experimental_pilot','scientific_sufficiency','production_sufficiency','training_authorized','partition_authorized','training_status'}
+COVERAGE_KEYS={'class_id','source','status','candidate_cap','transfer_cap','found','transferred','technical_integrity','license_valid','expert_validated','approved','rejected','pending'}
+STATUSES={'not_attempted','no_crosswalk','source_blocked','exhausted_within_query','budget_reached','all_rejected','review_pending','protection_not_queried'}
+def validate_public(value):
+    require(set(value)==PUBLIC_KEYS,'private_export')
+    require(value['stage']=='pending_human_acceptance' and value['usable']==0 and value['minimum_experimental_pilot'] is None,'public_authority')
+    require(value['training_authorized'] is False and value['partition_authorized'] is False and value['training_status']=='blocked','public_training')
+    require(value['scientific_sufficiency']==value['production_sufficiency']=='not_demonstrated','public_sufficiency')
+    require(set(value['counts'])<=STATES and all(type(v)is int and v>=0 for v in value['counts'].values()),'public_counts')
+    expected=[(c['class_id'],s) for c in canonical() for s in SOURCES]
+    require([(c['class_id'],c['source']) for c in value['coverage']]==expected,'public_classes')
+    for c in value['coverage']:
+        require(set(c)==COVERAGE_KEYS and c['status'] in STATUSES,'private_export')
+        require(all(type(v)is int and v>=0 for k,v in c.items() if k not in {'class_id','source','status'}),'public_types')
+    require(type(value['schema_version'])is int and value['schema_version']==1 and type(value['unique_objects'])is int,'public_schema')
+
+class PinnedHTTPS(http.client.HTTPSConnection):
+    """Pin a validated public address; TLS still verifies the original hostname."""
+    def connect(self):
+        address=public_addresses(self.host)[0]
+        sock=socket.create_connection((address,443),self.timeout)
+        try:self.sock=self._context.wrap_socket(sock,server_hostname=self.host)
+        except BaseException:sock.close();raise
+
+def retry_delay(value,attempt,clock=None):
+    clock=clock or time.time
+    if value:
+        try:
+            delay=int(value) if value.isdecimal() else parsedate_to_datetime(value).timestamp()-clock()
+            return max(0,delay)
+        except (ValueError,TypeError,OverflowError):raise RecoveryError('invalid_retry_after') from None
+    return 2**(attempt+1)
+
+class Transport:
+    def __init__(self,ds):self.ds=ds;self.last=0
+    def get(self,url,source,media=False):
+        require(not self.ds.offline,'offline_network_forbidden')
+        limit=self.ds.config['limits']['file_bytes'] if media else 2*1024**2
+        safe_url(url,source,media)
+        for attempt in range(3):
+            reservations=self.ds.select('request');finished={x['request_id']:x for x in self.ds.select('response')}
+            require(sum(x['source']==source for x in reservations)<self.ds.config['limits']['requests'],'request_budget')
+            media_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'])
+            hour_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations
+                           if x['media'] and x['epoch']>time.time()-3600)
+            if media:
+                require(media_total+limit<=self.ds.config['limits']['media_bytes'],'media_budget')
+                require(hour_total+limit<=self.ds.config['limits']['hour_bytes'],'hour_budget')
+            requests_after=[x for x in self.ds.select('resume_after') if x['source']==source]
+            if requests_after:require(time.time()>=requests_after[-1]['epoch'],'resume_after')
+            delay=max(0,1-(time.time()-reservations[-1]['epoch'])) if reservations else 0
+            if delay:time.sleep(delay)
+            rid=os.urandom(16).hex()
+            self.ds.append('request',{'request_id':rid,'source':source,'media':media,'reserved':limit,'epoch':time.time(),'url':url})
+            received=0;conn=None;status=None;retry=None;code='network_error';spool=None
+            try:
+                p=urlsplit(url);conn=PinnedHTTPS(p.hostname,timeout=20,context=ssl.create_default_context())
+                conn.request('GET',p.path+('?' + p.query if p.query else ''),headers={'User-Agent':self.ds.config['user_agent'],'Accept':'application/json,image/jpeg,image/png','Accept-Encoding':'identity'})
+                response=conn.getresponse();status=response.status
+                if status in {301,302,303,307,308}:
+                    # Validated redirect is reported for explicit source reconciliation; never silently switches objects.
+                    safe_url(urljoin(url,response.getheader('Location','')),source,media)
+                    raise RecoveryError('redirect_requires_reconciliation')
+                if status!=200:
+                    retry=response.getheader('Retry-After');code='http_'+str(status)
+                    raise RecoveryError(code)
+                length=response.getheader('Content-Length')
+                require(not length or length.isdecimal() and int(length)<=limit,'response_size')
+                require(response.getheader('Content-Encoding','identity')=='identity','content_encoding')
+                chunks=[];started=time.monotonic()
+                if media:
+                    require(shutil.disk_usage(self.ds.root).free>=3*1024**3,'insufficient_disk')
+                    spool=os.fdopen(os.open(self.ds.path('parts/request-'+rid+'.part'),os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600),'wb')
+                while True:
+                    require(time.monotonic()-started<=20,'response_timeout')
+                    chunk=response.read(min(65536,limit+1-received))
+                    if not chunk:break
+                    received+=len(chunk);chunks.append(chunk)
+                    if spool:spool.write(chunk);spool.flush();os.fsync(spool.fileno())
+                    require(received<=limit,'response_size')
+                raw=b''.join(chunks)
+                if not media:
+                    data=load(raw)
+                    if isinstance(data,dict) and data.get('error',{}).get('code')=='maxlag':
+                        status=503;retry=response.getheader('Retry-After');raise RecoveryError('maxlag')
+                require(not length or received==int(length),'response_length_mismatch')
+                code='ok'
+                return raw
+            except (OSError,http.client.HTTPException) as error:
+                code='timeout' if isinstance(error,TimeoutError) else 'network_error'
+            except RecoveryError as error:
+                code=str(error)
+                if code not in RETRYABLE:raise
+            finally:
+                if spool:spool.close();fsync_dir(self.ds.path('parts'))
+                if conn:conn.close()
+                self.ds.append('response',{'request_id':rid,'received':received,'status':status,'code':code})
+            if attempt==2:raise RecoveryError(code)
+            delay=retry_delay(retry,attempt)
+            if delay>self.ds.config['limits']['wait_seconds']:
+                self.ds.append('resume_after',{'source':source,'epoch':time.time()+delay})
+                raise RecoveryError('resume_after')
+            time.sleep(delay)
+        raise RecoveryError('transfer_failed')
+
+
+def commons_query(cls,cursor):
+    require(cls['kind']=='species','protection_query')
+    return {'action':'query','format':'json','formatversion':2,'generator':'search','gsrsearch':'"'+cls['scientific_name']+'"',
+            'gsrnamespace':6,'gsrlimit':10,'gsroffset':cursor,'gsrsort':'relevance','prop':'imageinfo|revisions',
+            'rvprop':'ids','iiprop':'url|mime|size|timestamp|sha1|extmetadata','iilimit':1,'iiextmetadatalanguage':'en','iiextmetadatafilter':'Artist|Credit|Attribution|Restrictions|Copyrighted|AttributionRequired|License|LicenseShortName|LicenseUrl|Permission','maxlag':5}
+
+def commons_page(data,cls,evidence,config):
+    require(isinstance(data,dict) and not ('error' in data or 'warnings' in data),'commons_schema')
+    require('query' in data or data.get('batchcomplete') is True,'commons_schema')
+    pages=data.get('query',{}).get('pages',[])
+    require(isinstance(pages,list) and len(pages)<=10,'commons_pages')
+    result=[]
+    for page in pages:
+        try:
+            old=commons.inspect_page(page,cls,'"'+cls['scientific_name']+'"',config['cutoff'])
+            info=page['imageinfo'][0];meta=info.get('extmetadata',{})
+            record={'source':'commons','media_id':str(old['page_id']),'class_ids':[cls['class_id']],
+                    'page_id':old['page_id'],'revision_id':(page.get('revisions') or [{}])[0].get('revid'),
+                    'file_url':old['file_url'],'source_page_url':old['page_url'],'mime':old['declared_mime'],
+                    'declared_size':old['declared_size'],'declared_width':info.get('width'),'declared_height':info.get('height'),
+                    'source_sha1':old['source_sha1'],'source_timestamp':old['source_timestamp'],
+                    'author':old['author'],'license_id':old['license_id'],'license_name':old['license'],
+                    'license_url':old['license_url'],'restrictions':old['restrictions'],
+                    'credit':commons.plain(old['credit_html']),'attribution':commons.plain(old['attribution_html']),
+                    'title':old['title'],'evidence_sha256':evidence,'rights_consistent':False,
+                    'database_rights':'passed' if config['source_contracts'].get('commons',{}).get('database_rights')=='passed' else 'pending',
+                    'mapping':None,'mapping_reason':'source_taxon_id_unproven','scientific_name_received':None,
+                    'taxonomic_confidence':'unmapped','observation_id':None,'origin_fidelity':'provider_original',
+                    'camera_original_verified':False}
+            # Require the actual individual grant, known photographer and coherent authorship/source.
+            record['rights_consistent']=bool(record['revision_id'] and meta.get('LicenseUrl') and meta.get('Artist') and
+                                              not meta.get('Permission',{}).get('value') and 'own work' in record['credit'].lower() and record['source_page_url'].startswith('https://commons.wikimedia.org/wiki/'))
+            result.append(record)
+        except (KeyError,TypeError,ValueError,commons.AcquisitionError):raise RecoveryError('commons_item_schema') from None
+    continuation=data.get('continue');next_cursor=None
+    if continuation is not None:
+        require(isinstance(continuation,dict) and set(continuation)<={'continue','gsroffset'} and type(continuation.get('gsroffset'))is int,'commons_cursor')
+        next_cursor=continuation['gsroffset']
+    return result,next_cursor
+
+
+def acquire_inat(ds,cls,transport,fixture):
+    cid=cls['class_id'];crosswalk=ds.config['crosswalk'][cid]
+    try:
+        query=inat.build_query(crosswalk,cls,ds.config['cutoff'])
+        # A reviewed evidence document must actually be present and match its digest.
+        ev=crosswalk['evidence'];require(sha(read(ds.path(ev['path'])))==ev['sha256'],'crosswalk_evidence_hash')
+        saved=next((p for p in ds.select('page') if p['source']=='inaturalist' and p['class_id']==cid),None)
+        if saved:page=saved
+        else:
+            raw=encode(fixture['inaturalist'][cid]) if fixture is not None else transport.get(inat.API_URL+'?'+urlencode(query),'inaturalist')
+            digest=sha(raw);path='evidence/'+digest+'.json';persist(ds.path(path),raw,True)
+            if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
+            data=load(raw);parsed=inat.parse_page(data,crosswalk,cls,ds.config['cutoff'])
+            by_photo={}
+            for observation in data['results']:
+                for photo in observation['photos']:
+                    by_photo.setdefault(str(photo['id']),(photo,observation))
+            records=[]
+            for initial in parsed['candidates']:
+                media_id=initial['media_id'];photo,observation=by_photo[media_id]
+                proof=ds.config['legal_evidence'].get(media_id)
+                if proof:
+                    for key in ['photo','observation']:
+                        require(sha(read(ds.path(proof[key]['path'])))==proof[key]['evidence_sha256'],'rights_evidence_hash')
+                item=inat.photo_record(photo,observation,proof)
+                eligible=item['download_allowed'] and initial['taxonomic_confidence']=='source_supported'
+                item.update(class_ids=[cid],license_id='cc-by-4.0' if item['license_code']=='cc-by' else item['license_code'],
+                            license_name='CC BY 4.0' if item['license_code']=='cc-by' else 'CC0 1.0',license_url=item['legal_url'],
+                            restrictions='',rights_consistent=eligible,database_rights='passed' if item['database_rights_passed'] else 'pending',
+                            evidence_sha256=item['license_evidence_sha256'],mapping=crosswalk,declared_size=None,
+                            mime='image/png' if (item['file_url'] or '').endswith('.png') else 'image/jpeg',
+                            taxonomic_confidence=initial['taxonomic_confidence'])
+                records.append(item)
+            page=ds.save_page('inaturalist',cid,0,records,None)
+            ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
+                                      'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
+        for c in page['candidates']:
+            ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
+        ds.advance(page)
+        return 'budget_reached'
+    except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
+        code=str(error) if isinstance(error,RecoveryError) and str(error) in RETRYABLE else 'inaturalist_contract_or_evidence'
+        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':code})
+        return 'source_blocked'
+
+
+def acquire(ds,fixture=None):
+    transport=Transport(ds)
+    if fixture is not None:require(ds.offline,'fixture_mode')
+    elif ds.offline:raise RecoveryError('fixture_required')
+    for cls in canonical():
+        for source in SOURCES:
+            cid=cls['class_id']
+            statuses=[s for s in ds.select('source_status') if s['source']==source and s['class_id']==cid]
+            if statuses:
+                failed=[e for e in ds.select('source_failure') if e['source']==source and e['class_id']==cid]
+                if statuses[-1]['status']!='source_blocked' or not failed or failed[-1]['code'] not in RETRYABLE:continue
+            status='protection_not_queried'
+            if cls['kind']=='species':
+                if source=='inaturalist' and cid not in ds.config['crosswalk']:
+                    status='no_crosswalk'
+                elif source=='inaturalist':
+                    status=acquire_inat(ds,cls,transport,fixture)
+                else:
+                    cursor=0;status='budget_reached'
+                    for page_index in range(ds.config['limits']['pages']):
+                        saved=next((p for p in ds.select('page') if p['source']==source and p['class_id']==cid and p['cursor']==cursor),None)
+                        try:
+                            if saved:page=saved
+                            else:
+                                if fixture is not None:
+                                    raw=encode(fixture.get(cid,{}).get(str(cursor),{'batchcomplete':True}))
+                                else:raw=transport.get('https://commons.wikimedia.org/w/api.php?'+urlencode(commons_query(cls,cursor)),source)
+                                digest=sha(raw);path='evidence/'+digest+'.json'
+                                persist(ds.path(path),raw,True)
+                                if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
+                                candidates,next_cursor=commons_page(load(raw),cls,digest,ds.config)
+                                page=ds.save_page(source,cid,cursor,candidates,next_cursor)
+                            examined={candidate_id(c) for p in ds.select('page') if p['source']==source and p['class_id']==cid for c in p['candidates']}
+                            require(len(examined)<=ds.config['limits']['candidates'],'candidate_budget')
+                            for c in page['candidates']:
+                                def download(record):
+                                    if fixture is not None:
+                                        require('synthetic_media' in fixture,'fixture_media_missing')
+                                        return read(Path(fixture['synthetic_media'])/str(record['media_id']))
+                                    return transport.get(record['file_url'],source,True)
+                                ds.ingest(c,download)
+                            ds.advance(page)
+                            retryable=[ds.record(c) for c in page['candidates'] if ds.record(c)['state']=='transfer_failed'
+                                       and set(ds.record(c).get('reasons',[])) & RETRYABLE]
+                            if retryable:
+                                raise RecoveryError(retryable[0]['reasons'][0])
+                            if page['next_cursor'] is None:
+                                status='exhausted_within_query';break
+                            cursor=page['next_cursor']
+                        except RecoveryError as error:
+                            ds.append('source_failure',{'source':source,'class_id':cid,'code':str(error)})
+                            status='source_blocked';break
+            ds.append('source_status',{'source':source,'class_id':cid,'status':status})
+    ds.project()
+    return 1 if any(c['status']=='source_blocked' for c in ds.summary()['coverage']) else 0
+
+
+def historical(source):
+    """Read-only verification against the frozen P07 closure (never P07 finalizers)."""
+    source=safe_path(source);closure=load(read(ROOT/'artifacts/bianchini/v2/codex/P07/closure-evidence.json'))
+    p07=source.parent/'p07-curation-20260928'
+    for n,h in closure['external_final_sha256'].items():require(sha(read(p07/n))==h,'p07_reference_hash')
+    before=load(read(p07/'source-before.json'))
+    actual={str(p.relative_to(source)):sha(read(p)) for p in source.rglob('*') if p.is_file()}
+    require(before==actual and len(actual)==29,'p06_source_hashes')
+    records=[]
+    for item in closure['images_before_after']:
+        h=item['sha256_after'];path=source/'quarantine'/f'{h}.jpg';raw=read(path)
+        require(sha(raw)==h,'p07_image_hash')
+        records.append({'candidate_id':item['id'],'sanitized_sha256':h,'technical':technical(raw),'class_ids':[],
+                        'original_sha256':None,'observation_id':None})
+    return actual,records
+
+
+def inspect(ds,source):
+    hashes,prior=historical(source);recs=ds.records();pairs=[]
+    combined=[*prior,*[r for r in recs if r.get('sanitized_sha256')]]
+    for i,a in enumerate(combined):
+        for b in combined[i+1:]:
+            if a['candidate_id'].startswith('Q') and b['candidate_id'].startswith('Q'):continue
+            dist=(int(a['technical']['dhash64'],16)^int(b['technical']['dhash64'],16)).bit_count()
+            exact=bool(a.get('sanitized_sha256')==b.get('sanitized_sha256') or a.get('original_sha256') and a.get('original_sha256')==b.get('original_sha256'))
+            same=bool(a.get('observation_id') and a.get('observation_id')==b.get('observation_id'))
+            signal='exact_duplicate' if exact else 'near_duplicate' if dist<=6 else 'borderline' if dist<=10 else 'same_series' if same else 'no_algorithmic_signal'
+            pairs.append({'pair_id':a['candidate_id']+'-'+b['candidate_id'],'left':a['candidate_id'],'right':b['candidate_id'],'distance':dist,'signal':signal})
+    for rec in recs:
+        related=[p for p in pairs if rec['candidate_id'] in {p['left'],p['right']} and p['signal']!='no_algorithmic_signal']
+        if rec.get('pairs')!=related:
+            rec['pairs']=related;rec.pop('decision',None)
+            if rec.get('sanitized_sha256'):
+                rec['state']='rejected_duplicate' if any(p['signal']=='exact_duplicate' for p in related) else 'needs_duplicate_review' if related else 'needs_human_review'
+            ds.append('classified',rec)
+    ds.project()
+    report={'p07_images':len(prior),'p06_hashes':hashes,'pairs':pairs,'records':recs,'summary':ds.summary()}
+    persist(ds.path('inspection.json'),encode(report))
+    rows=[];attrs=[]
+    for r in recs:
+        image=f'<img loading="lazy" width="240" src="{escape(r["sanitized_path"])}">' if r.get('sanitized_path') else ''
+        detail=escape(json.dumps(r,ensure_ascii=False,indent=2,sort_keys=True))
+        rows.append(f'<article><h2>{r["candidate_id"]}</h2>{image}<pre>{detail}</pre></article>')
+        if r.get('original_sha256'):
+            attrs.append({k:r.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256','author','credit','attribution','title','source_page_url','license_url','restrictions']})
+            attrs[-1]['changes']='EXIF orientation; RGB pixel reconstruction; metadata removal; JPEG quality 95 or PNG; no crop or enhancement'
+    html='<!doctype html><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; img-src \'self\'; style-src \'unsafe-inline\'"><title>P08 private review</title><h1>P08 — pending human review</h1>'+''.join(rows)
+    persist(ds.path('review.html'),html.encode())
+    persist(ds.path('Attributions.jsonl'),b''.join(encode(a) for a in attrs))
+    persist(ds.path('NOTICE.md'),('P08 private attribution bundle; no redistribution authorized.\n\n'+''.join(json.dumps(a,ensure_ascii=False)+'\n\n' for a in attrs)).encode())
+    persist(ds.path('decisions.template.json'),encode({'authority':'human','decisions':[
+        {'candidate_id':r['candidate_id'],'original_sha256':r.get('original_sha256'),'sanitized_sha256':r.get('sanitized_sha256'),
+         'evidence_digest':review_digest(r),'reviewer':None,'reviewed_at':None,'authority':'human','quality':'pending',
+         'privacy':'pending','botanical':'pending','duplicates':'pending','expert_confirmation':False,
+         'qualification':None,'botanical_evidence':None,'mapping':None,'rationale':None} for r in recs]}))
+    return report
+
+
+def finalize(ds,decisions):
+    data=load(read(decisions));require(data.get('authority')=='human' and isinstance(data.get('decisions'),list),'human_authority')
+    ids=[d.get('candidate_id') for d in data['decisions']];require(len(ids)==len(set(ids)),'duplicate_decisions')
+    recs={r['candidate_id']:r for r in ds.records()};require(set(ids)==set(recs),'decision_coverage')
+    for d in data['decisions']:
+        rec=recs[d['candidate_id']]
+        if rec.get('decision')==d:continue
+        state=decide(rec,d)
+        if state=='approved_for_dataset':
+            inspection=load(read(ds.path('inspection.json')))
+            require(inspection.get('p07_images')==17 and any(review_digest(item)==review_digest(rec)
+                    for item in inspection['records']),'inspection_binding')
+            attrs=[load(line) for line in read(ds.path('Attributions.jsonl')).splitlines()]
+            require(any(all(item.get(k)==rec.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256',
+                         'author','license_url','source_page_url']) for item in attrs),'attribution_binding')
+            require(sha(read(ds.path(d['mapping']['evidence_path'])))==d['mapping']['evidence_sha256'],'mapping_evidence_hash')
+            require(sha(read(ds.path(d['botanical_evidence_path'])))==d['botanical_evidence'],'botanical_evidence_hash')
+        rec.update(state=state,decision=d);ds.append('classified',rec)
+    ds.project()
+
+
+def verify(ds,source,acceptance=None):
+    ds.verify_objects();historical(source);validate_public(ds.summary())
+    require(len({(s['source'],s['class_id']) for s in ds.select('source_status')})==28,'incomplete_round')
+    require({p['page_id'] for p in ds.select('page')}=={p['page_id'] for p in ds.select('cursor')},'pending_pages')
+    if acceptance:
+        a=load(read(acceptance));manifest=read(ds.path('final-manifest.json'))
+        require(a.get('decision')=='accepted' and a.get('authority')=='human' and a.get('reviewer') and a.get('reviewed_at') and a.get('manifest_sha256')==sha(manifest),'human_acceptance')
+        files=load(manifest)['files']
+        actual={str(p.relative_to(ds.root)):sha(read(p)) for p in ds.root.rglob('*') if p.is_file() and str(p.relative_to(ds.root)) not in {'.lock','final-manifest.json','acceptance.json'}}
+        require(files==actual,'acceptance_coverage_or_bytes')
+        require({'journal.jsonl','config.json','records.json','summary.json','inspection.json','Attributions.jsonl','NOTICE.md','review.html'} <= set(files),'acceptance_required_files')
+        require(a.get('training_authorized') is False,'acceptance_not_training')
+    return 0
+
+
+def main(argv=None):
+    parser=argparse.ArgumentParser(description=__doc__)
+    sub=parser.add_subparsers(dest='command',required=True)
+    for name in ['acquire','inspect','finalize','verify']:
+        p=sub.add_parser(name);p.add_argument('--output',required=True);p.add_argument('--offline-fixture')
+        if name=='acquire':p.add_argument('--config',required=True)
+        if name in {'inspect','verify'}:p.add_argument('--p07-source',required=True)
+        if name=='finalize':p.add_argument('--decisions',required=True)
+        if name=='verify':p.add_argument('--acceptance')
+    args=parser.parse_args(argv)
+    try:
+        config=load(read(args.config if args.command=='acquire' else Path(args.output)/'config.json'))
+        with Dataset(args.output,config,offline=bool(args.offline_fixture)) as ds:
+            if args.command=='acquire':code=acquire(ds,load(read(args.offline_fixture)) if args.offline_fixture else None)
+            elif args.command=='inspect':inspect(ds,args.p07_source);code=0
+            elif args.command=='finalize':finalize(ds,args.decisions);code=0
+            else:code=verify(ds,args.p07_source,args.acceptance)
+        print(json.dumps({'command':args.command,'status':'passed' if code==0 else 'source_blocked'}));return code
+    except (OSError,ValueError,KeyError,TypeError):
+        print('p08_invalid_config_schema_hash_or_io',file=sys.stderr);return 2
+    except KeyboardInterrupt:
+        print('p08_cancelled_replay_required',file=sys.stderr);return 1
+
+if __name__=='__main__':raise SystemExit(main())
+
+```
+
+### scripts/phase1/test_recover_p08.py
+
+```text
+"""Public P08 boundaries, synthetic data only; no network in these tests."""
+import copy
+from contextlib import ExitStack
+import io
+import json
+import os
+from pathlib import Path
+import subprocess
+import sys
+import tempfile
+import unittest
+from unittest.mock import patch
+from PIL import Image
+import recover_p08 as r
+
+
+def image_bytes(fmt='JPEG'):
+    out = io.BytesIO()
+    im = Image.new('RGB', (240, 240), (100, 160, 40))
+    exif = Image.Exif(); exif[270] = 'synthetic-private-metadata'; exif[274] = 6
+    im.save(out, format=fmt, exif=exif)
+    return out.getvalue()
+
+
+def candidate(raw=None):
+    raw = raw or image_bytes()
+    return {'source': 'commons', 'media_id': '123', 'class_ids': ['species_01'],
+            'file_url': 'https://upload.wikimedia.org/a/test.jpg',
+            'source_page_url': 'https://commons.wikimedia.org/wiki/File:Test.jpg',
+            'mime': 'image/jpeg', 'declared_size': len(raw), 'source_sha1': __import__('hashlib').sha1(raw).hexdigest(),
+            'author': 'Synthetic fixture', 'license_id': 'cc-by-4.0', 'license_name': 'CC BY 4.0',
+            'license_url': 'https://creativecommons.org/licenses/by/4.0/', 'restrictions': '',
+            'credit': 'Synthetic fixture', 'attribution': 'Synthetic fixture', 'evidence_sha256': 'a'*64,
+            'rights_consistent': True, 'database_rights': 'passed', 'mapping': None,
+            'observation_id': None, 'origin_fidelity': 'provider_original', 'camera_original_verified': False}
+
+
+class DatasetCase:
+    def setUp(self):
+        self.tmp = tempfile.TemporaryDirectory()
+        self.addCleanup(self.tmp.cleanup)
+        self.root = Path(self.tmp.name)/'synthetic'
+        self.config = r.default_config(offline=True)
+
+    def open(self):
+        return r.Dataset(self.root, self.config, offline=True)
+
+
+class RecoveryTests(DatasetCase, unittest.TestCase):
+
+    def test_rights_gate(self):
+        c = candidate()
+        self.assertEqual(r.rights(c), 'passed')
+        for key, val in [('license_url', 'https://creativecommons.org/licenses/by/3.0/'),
+                         ('license_name','CC BY-SA 4.0'),('license_id','cc-by'),
+                         ('author','unknown'),('restrictions','extra'),('rights_consistent',False),
+                         ('evidence_sha256',None),('database_rights','pending')]:
+            with self.subTest(key=key):
+                bad=copy.deepcopy(c); bad[key]=val
+                self.assertNotEqual(r.rights(bad),'passed')
+
+    def test_expert_gate(self):
+        c = candidate(); c.update(candidate_id=r.candidate_id(c),original_sha256='b'*64,sanitized_sha256='c'*64,
+                                technical={'decode':'ok'},pairs=[],state='quarantined')
+        d = {'candidate_id':c['candidate_id'], 'original_sha256':'b'*64,'sanitized_sha256':'c'*64,
+             'evidence_digest':r.review_digest(c),'reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z',
+             'authority':'human','quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
+             'expert_confirmation':False,'qualification':'','botanical_evidence':'','mapping':None,
+             'rationale':'Synthetic decision'}
+        self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
+        for flag in [None, 'true',1]:
+            d['expert_confirmation']=flag
+            self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
+        d['authority']='agent_proposal'
+        with self.assertRaises(r.RecoveryError): r.decide(c,d)
+
+    def test_original_sanitization_resume(self):
+        raw=image_bytes(); c=candidate(raw)
+        with self.open() as ds:
+            rec=ds.ingest(c,lambda _:raw)
+            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)
+            self.assertNotEqual(rec['original_sha256'],rec['sanitized_sha256'])
+            with Image.open(self.root/rec['sanitized_path']) as im:
+                self.assertFalse(im.getexif()); self.assertNotIn('xmp',im.info)
+            before=r.tree_fingerprint(self.root)
+            ds.ingest(c,lambda _:self.fail('repeat download'))
+            self.assertEqual(before,r.tree_fingerprint(self.root))
+        with self.open() as ds:
+            self.assertEqual(len(ds.records()),1)
+            before=r.tree_fingerprint(self.root)
+            ds.ingest(c,lambda _:self.fail('restart download'))
+            self.assertEqual(before,r.tree_fingerprint(self.root))
+            self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')
+
+    def test_hash_mismatch(self):
+        with self.open() as ds:
+            rec=ds.ingest(candidate(),lambda _:image_bytes())
+        (self.root/rec['original_path']).write_bytes(b'corrupt')
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+
+    def test_journal_partial(self):
+        with self.open(): pass
+        with (self.root/'journal.jsonl').open('ab') as f: f.write(b'{')
+        before=(self.root/'journal.jsonl').read_bytes()
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+        self.assertEqual(before,(self.root/'journal.jsonl').read_bytes())
+
+    def test_journal_chain(self):
+        with self.open() as ds: ds.append('test',{'x':1})
+        p=self.root/'journal.jsonl'; raw=p.read_bytes().replace(b'"x":1',b'"x":2');p.write_bytes(raw)
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+
+    def test_lock(self):
+        with self.open():
+            with self.assertRaises(r.RecoveryError):
+                with self.open(): pass
+
+    def test_changed_config(self):
+        with self.open(): pass
+        self.config['limits']['pages']=1
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+
+    def test_symlink(self):
+        self.root.symlink_to(Path(self.tmp.name),target_is_directory=True)
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+
+    def test_cursor_gate(self):
+        with self.open() as ds:
+            page=ds.save_page('commons','species_01',0,[candidate()],None)
+            with self.assertRaises(r.RecoveryError): ds.advance(page)
+            ds.ingest(candidate(),lambda _:image_bytes())
+            ds.advance(page)
+            before=r.tree_fingerprint(self.root);ds.advance(page)
+            self.assertEqual(before,r.tree_fingerprint(self.root))
+
+    def test_private_export(self):
+        with self.open() as ds: value=ds.summary()
+        self.assertEqual(len(value['coverage']),28)
+        self.assertFalse(value['training_authorized'])
+        self.assertEqual(value['usable'],0)
+        r.validate_public(value)
+        for key in ['author','url','gps','free_text']:
+            bad=copy.deepcopy(value);bad[key]='PRIVATE'
+            with self.assertRaises(r.RecoveryError):r.validate_public(bad)
+        bad=copy.deepcopy(value);bad['coverage'][0]['author']='PRIVATE'
+        with self.assertRaises(r.RecoveryError):r.validate_public(bad)
+
+    def test_download_budget_restart(self):
+        self.config['limits']['transfers']=1
+        with self.open() as ds:
+            ds.ingest(candidate(),lambda _:image_bytes())
+        with self.open() as ds:
+            c=candidate();c['media_id']='124'
+            rec=ds.ingest(c,lambda _:self.fail('budget exceeded'))
+            self.assertEqual(rec['state'],'deferred_budget')
+
+    def test_crash_boundaries(self):
+        for stage in ['intention','received','original','sanitized','committed']:
+            with self.subTest(stage=stage),tempfile.TemporaryDirectory() as td:
+                root=Path(td)/'synthetic'
+                with r.Dataset(root,self.config,offline=True) as ds:
+                    def crash(point):
+                        if point==stage: raise RuntimeError('crash')
+                    with self.assertRaises(RuntimeError):ds.ingest(candidate(),lambda _:image_bytes(),crash=crash)
+                with r.Dataset(root,self.config,offline=True) as ds:
+                    rec=ds.ingest(candidate(),lambda _:image_bytes())
+                    self.assertTrue((root/rec['original_path']).exists())
+                    self.assertEqual(len(ds.records()),1)
+                    self.assertEqual(rec['state'],'needs_human_review')
+
+    def test_format_invalid_preserved(self):
+        raw=b'not image';c=candidate(raw)
+        with self.open() as ds:
+            rec=ds.ingest(c,lambda _:raw)
+            self.assertEqual(rec['state'],'rejected_format')
+            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)
+
+    def test_symlink_object(self):
+        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
+        p=self.root/rec['original_path'];raw=p.read_bytes();p.unlink()
+        q=Path(self.tmp.name)/'fixture';q.write_bytes(raw);p.symlink_to(q)
+        with self.assertRaises(r.RecoveryError):
+            with self.open(): pass
+
+    def test_url_boundaries(self):
+        good='https://upload.wikimedia.org/a/a.jpg'
+        self.assertEqual(r.safe_url(good,'commons',True),good)
+        for u in ['http://upload.wikimedia.org/a.jpg','https://upload.wikimedia.org:444/a.jpg',
+                  'https://[REDACTED EMAIL]/a.jpg','https://evil.invalid/a.jpg',
+                  'https://upload.wikimedia.org/%2e%2e/a.jpg','https://upload.wikimedia.org/a.jpg#x']:
+            with self.subTest(u=u),self.assertRaises(r.RecoveryError):r.safe_url(u,'commons',True)
+        with patch('socket.getaddrinfo',return_value=[(2,1,6,'',('127.0.0.1',443))]):
+            with self.assertRaises(r.RecoveryError):r.public_addresses('upload.wikimedia.org')
+
+    def test_metadata_and_dimensions(self):
+        for fmt in ['JPEG','PNG']:
+            raw=image_bytes(fmt);suffix='jpg' if fmt=='JPEG' else 'png'
+            clean,ext=r.sanitize(raw,'https://upload.wikimedia.org/a.'+suffix,'image/'+('jpeg' if fmt=='JPEG' else 'png'))
+            with Image.open(io.BytesIO(clean)) as im:
+                self.assertFalse(im.getexif());self.assertEqual(im.mode,'RGB')
+        with self.assertRaises(r.RecoveryError):r.sanitize(b'', 'https://upload.wikimedia.org/a.jpg','image/jpeg')
+        with self.assertRaises(r.RecoveryError):r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.jpg','image/jpeg')
+
+    def test_cli_invalid_safe(self):
+        p=subprocess.run([sys.executable,'-B',str(r.Path(r.__file__)),'verify','--output',str(self.root),'--p07-source',str(self.root)],capture_output=True,text=True)
+        self.assertEqual(p.returncode,2)
+        self.assertNotIn(str(self.root),p.stderr)
+
+class ExtendedTests(DatasetCase, unittest.TestCase):
+    """Risk neighbors through durable acquisition and transport boundaries."""
+    def test_retry_transfer(self):
+        with self.open() as ds:
+            def fail(_):raise r.RecoveryError('timeout')
+            self.assertEqual(ds.ingest(candidate(),fail)['state'],'transfer_failed')
+        with self.open() as ds:
+            self.assertEqual(ds.ingest(candidate(),lambda _:image_bytes())['state'],'needs_human_review')
+            self.assertEqual(len(ds.select('intention')),2)
+
+    def test_zero_round_replay(self):
+        with self.open() as ds:
+            self.assertEqual(r.acquire(ds,{}),0)
+            ds.project();before=r.tree_fingerprint(self.root)
+            self.assertEqual(r.acquire(ds,{}),0)
+            self.assertEqual(before,r.tree_fingerprint(self.root))
+            coverage=ds.summary()['coverage']
+            self.assertEqual(sum(x['status']=='no_crosswalk' for x in coverage),12)
+            self.assertEqual(sum(x['status']=='protection_not_queried' for x in coverage),4)
+
+    def test_same_object_class_conflict(self):
+        with self.open() as ds:
+            ds.ingest(candidate(),lambda _:image_bytes())
+            c=candidate();c['class_ids']=['species_02']
+            rec=ds.ingest(c,lambda _:self.fail('duplicate download'))
+            self.assertEqual(rec['class_ids'],['species_01','species_02'])
+            self.assertEqual(rec['state'],'needs_botanical_review')
+            self.assertEqual(len(ds.records()),1)
+
+    def test_fsync_failure_preserves_source(self):
+        with self.open() as ds:
+            with patch.object(r.os,'fsync',side_effect=OSError('synthetic full disk')):
+                with self.assertRaises(OSError):ds.ingest(candidate(),lambda _:self.fail('before durable intent'))
+
+    def test_missing_object(self):
+        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
+        (self.root/rec['sanitized_path']).unlink()
+        with self.assertRaises(OSError):
+            with self.open():pass
+
+    def test_png_pixels_and_metrics(self):
+        clean,_=r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.png','image/png')
+        tech=r.technical(clean)
+        self.assertEqual(tech['format'],'PNG')
+        self.assertEqual(len(tech['dhash64']),16)
+        for mean,expected in [(39,True),(40,False),(215,False),(216,True)]:
+            flags=r.flags_for(224,224,mean,0,0,100)
+            self.assertEqual('dark_mean' in flags or 'bright_mean' in flags,expected)
+        self.assertIn('dark_fraction',r.flags_for(224,224,100,.25,0,100))
+        self.assertNotIn('small_dimension',r.flags_for(224,224,100,0,0,100))
+        self.assertIn('small_dimension',r.flags_for(223,224,100,0,0,100))
+        self.assertNotIn('extreme_aspect',r.flags_for(224,672,100,0,0,100))
+        self.assertIn('extreme_aspect',r.flags_for(224,673,100,0,0,100))
+        self.assertIn('low_laplacian_variance',r.flags_for(224,224,100,0,0,99))
+
+    def test_retry_after(self):
+        self.assertEqual(r.retry_delay('120',0),120)
+        self.assertEqual(r.retry_delay(None,0),2)
+        self.assertEqual(r.retry_delay(None,1),4)
+        self.assertEqual(r.retry_delay('Thu, 01 Jan 1970 00:02:00 GMT',0,clock=lambda:0),120)
+        with self.assertRaises(r.RecoveryError):r.retry_delay('invalid',0)
+
+    def test_offline_transport_never_network(self):
+        with self.open() as ds,patch.object(r.socket,'create_connection',side_effect=AssertionError('network')):
+            with self.assertRaises(r.RecoveryError):r.Transport(ds).get('https://commons.wikimedia.org/w/api.php','commons')
+
+    def test_final_positive_authority_and_mapping(self):
+        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
+        cls=r.canonical()[0]
+        d={'authority':'human','reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
+           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
+           'evidence_digest':r.review_digest(c),'expert_confirmation':True,'qualification':'synthetic botanist',
+           'botanical_evidence':'a'*64,'quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
+           'mapping':{'confidence':'human_validated','source_taxon_id':'fixture','namespace':'fixture','evidence_sha256':'a'*64,
+                      'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],'rank':'species','status':'accepted',
+                      'taxonomy_ref_ids':cls['taxonomy_ref_ids']},
+           'visual':dict.fromkeys(['photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'],True),
+           'privacy_checks':dict.fromkeys(['people','faces','plates','residences','screens_documents','sensitive_location'],'absent')}
+        self.assertEqual(r.decide(c,d),'approved_for_dataset')
+        for key in ['scientific_name','class_id','taxonomy_ref_ids','namespace']:
+            bad=copy.deepcopy(d);bad['mapping'][key]=None
+            self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')
+        for gate in ['quality','privacy','botanical','duplicates']:
+            for value in [None,True,'unknown','pending']:
+                bad=copy.deepcopy(d);bad[gate]=value
+                self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')
+
+
+class FakeResponse:
+    def __init__(self, status=200, body=b'{}', headers=None, read_error=None):
+        self.status = status
+        self.body = io.BytesIO(body)
+        self.headers = headers or {}
+        self.read_error = read_error
+        self.read_calls = 0
+
+    def getheader(self, name, default=None):
+        return self.headers.get(name, default)
+
+    def read(self, count):
+        self.read_calls += 1
+        if self.read_error and self.read_calls > 1:
+            raise self.read_error
+        return self.body.read(count)
+
+
+class FakeConnection:
+    def __init__(self, result):
+        self.result = result
+        self.requests = []
+        self.closed = False
+
+    def request(self, *args, **kwargs):
+        self.requests.append((args, kwargs))
+
+    def getresponse(self):
+        if isinstance(self.result, BaseException):
+            raise self.result
+        return self.result
+
+    def close(self):
+        self.closed = True
+
+
+class TransportTests(DatasetCase, unittest.TestCase):
+    api = 'https://commons.wikimedia.org/w/api.php'
+    media = 'https://upload.wikimedia.org/a/synthetic.jpg'
+
+    def transport(self, ds, responses):
+        stack = ExitStack()
+        self.addCleanup(stack.close)
+        connections = [FakeConnection(response) for response in responses]
+        factory = stack.enter_context(patch.object(r, 'PinnedHTTPS', side_effect=connections))
+        stack.enter_context(patch.object(ds, 'offline', False))
+        stack.enter_context(patch.object(r.socket, 'create_connection', side_effect=AssertionError('network_forbidden')))
+        stack.enter_context(patch.object(r.socket, 'getaddrinfo', side_effect=AssertionError('network_forbidden')))
+        clock = [1000.0]
+        stack.enter_context(patch.object(r.time, 'time', side_effect=lambda: clock[0]))
+        stack.enter_context(patch.object(r.time, 'monotonic', side_effect=lambda: clock[0]))
+        sleeps = stack.enter_context(patch.object(r.time, 'sleep', side_effect=lambda value: clock.__setitem__(0, clock[0]+value)))
+        stack.enter_context(patch.object(r.shutil, 'disk_usage', return_value=type('Disk', (), {'free': 4*1024**3})()))
+        return r.Transport(ds), factory, connections, sleeps
+
+    def test_403_never_retries(self):
+        with self.open() as ds:
+            transport, factory, connections, sleeps = self.transport(ds, [FakeResponse(403)])
+            with self.assertRaisesRegex(r.RecoveryError, 'http_403'):
+                transport.get(self.api, 'commons')
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(len(ds.select('request')), 1)
+            self.assertEqual(ds.select('response')[0]['status'], 403)
+            self.assertTrue(connections[0].closed)
+            sleeps.assert_not_called()
+
+    def test_429_wait_above_budget_persists_resume_after(self):
+        with self.open() as ds:
+            transport, factory, _, sleeps = self.transport(ds, [FakeResponse(429, headers={'Retry-After': '120'})])
+            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
+                transport.get(self.api, 'commons')
+            self.assertEqual(ds.select('resume_after')[0]['epoch'], 1120)
+            self.assertEqual(factory.call_count, 1)
+            sleeps.assert_not_called()
+            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
+                transport.get(self.api, 'commons')
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(len(ds.select('request')), 1)
+
+    def test_timeout_three_attempts_and_cumulative_quota(self):
+        self.config['limits']['requests'] = 3
+        with self.open() as ds:
+            transport, factory, connections, sleeps = self.transport(ds, [TimeoutError('synthetic') for _ in range(3)])
+            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
+                transport.get(self.api, 'commons')
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
+            self.assertEqual([call.args[0] for call in sleeps.call_args_list], [2, 4])
+            self.assertTrue(all(connection.closed for connection in connections))
+        with self.open() as ds:
+            transport, factory, _, _ = self.transport(ds, [])
+            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
+                transport.get(self.api, 'commons')
+            factory.assert_not_called()
+
+    def test_request_reservation_survives_crash_without_response(self):
+        self.config['limits']['requests'] = 1
+        with self.open() as ds:
+            ds.append('request', {'request_id': 'synthetic-interrupted', 'source': 'commons', 'media': True,
+                                  'reserved': 16, 'epoch': 1000, 'url': self.media})
+        with self.open() as ds:
+            transport, factory, _, _ = self.transport(ds, [])
+            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
+                transport.get(self.media, 'commons', True)
+            factory.assert_not_called()
+
+    def test_malicious_redirect_does_not_connect_to_destination(self):
+        with self.open() as ds:
+            transport, factory, _, _ = self.transport(ds, [FakeResponse(302, headers={'Location': 'https://127.0.0.1/a'})])
+            with self.assertRaisesRegex(r.RecoveryError, 'unsafe_url'):
+                transport.get(self.api, 'commons')
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(ds.select('response')[0]['status'], 302)
+
+    def test_public_hostname_resolving_private_ip_is_rejected_before_connect(self):
+        for ip in ['127.0.0.1', '10.0.0.1', '169.254.169.254', '::1', 'fc00::1']:
+            with self.subTest(ip=ip), patch.object(r.socket, 'getaddrinfo', return_value=[(2, 1, 6, '', (ip, 443))]), patch.object(r.socket, 'create_connection', side_effect=AssertionError('must_not_connect')) as connect:
+                with self.assertRaisesRegex(r.RecoveryError, 'nonpublic_address'):
+                    r.PinnedHTTPS('upload.wikimedia.org', timeout=20).connect()
+                connect.assert_not_called()
+
+    def test_oversized_response_counts_received_bytes_and_failure(self):
+        self.config['limits']['file_bytes'] = 8
+        self.config['limits']['media_bytes'] = 16
+        with self.open() as ds:
+            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'123456789')])
+            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
+                transport.get(self.media, 'commons', True)
+            self.assertEqual(ds.select('response')[0]['received'], 9)
+            self.assertEqual(ds.select('response')[0]['code'], 'response_size')
+            with self.assertRaisesRegex(r.RecoveryError, 'media_budget'):
+                transport.get(self.media, 'commons', True)
+            self.assertEqual(factory.call_count, 1)
+
+    def test_partial_timeout_counts_bytes_on_every_retry(self):
+        self.config['limits']['file_bytes'] = 16
+        with self.open() as ds:
+            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'1234', read_error=TimeoutError('synthetic')) for _ in range(3)])
+            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
+                transport.get(self.media, 'commons', True)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual([e['received'] for e in ds.select('response')], [4, 4, 4])
+            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
+
+    def test_declared_oversize_rejected_before_body(self):
+        self.config['limits']['file_bytes'] = 8
+        response = FakeResponse(body=b'123456789', headers={'Content-Length': '9'})
+        with self.open() as ds:
+            transport, _, _, _ = self.transport(ds, [response])
+            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
+                transport.get(self.media, 'commons', True)
+            self.assertEqual(response.read_calls, 0)
+            self.assertEqual(ds.select('response')[0]['received'], 0)
+
+
+class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
+    def test_fake_commons_cli_snapshot_ingest_and_restart(self):
+        raw = image_bytes()
+        c = candidate(raw)
+        media = Path(self.tmp.name)/'media'
+        media.mkdir()
+        (media/'123').write_bytes(raw)
+        fields = {'Artist': 'Synthetic fixture', 'License': 'cc-by-4.0', 'LicenseShortName': 'CC BY 4.0',
+                  'LicenseUrl': c['license_url'], 'Credit': 'Own work', 'Attribution': 'Synthetic fixture'}
+        page = {'pageid': 123, 'ns': 6, 'title': 'File:Synthetic.jpg', 'revisions': [{'revid': 456}],
+                'imageinfo': [{'url': c['file_url'], 'descriptionurl': c['source_page_url'],
+                               'mime': c['mime'], 'size': len(raw), 'width': 240, 'height': 240,
+                               'sha1': c['source_sha1'], 'timestamp': '2026-10-04T00:00:00Z',
+                               'extmetadata': {key: {'value': value} for key, value in fields.items()}}]}
+        fixture = {'species_01': {'0': {'query': {'pages': [page]}, 'continue': {'continue': 'gsroffset||', 'gsroffset': 10}},
+                                  '10': {'batchcomplete': True}}, 'synthetic_media': str(media)}
+        fixture_path = Path(self.tmp.name)/'fixture.json'
+        fixture_path.write_bytes(r.encode(fixture))
+        self.config['source_contracts']['commons'] = {'database_rights': 'passed'}
+        config_path = Path(self.tmp.name)/'run.json'
+        config_path.write_bytes(r.encode(self.config))
+        script = ('import sys\nfrom unittest.mock import patch\n'
+                  'sys.path.insert(0, sys.argv.pop(1))\nimport recover_p08\n'
+                  'with patch("socket.create_connection", side_effect=AssertionError("network_forbidden")), patch("socket.getaddrinfo", side_effect=AssertionError("network_forbidden")):\n'
+                  ' raise SystemExit(recover_p08.main(sys.argv[1:]))\n')
+        argv = [sys.executable, '-B', '-c', script, str(Path(r.__file__).parent), 'acquire', '--config', str(config_path),
+                '--output', str(self.root), '--offline-fixture', str(fixture_path)]
+        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
+        self.assertEqual(process.returncode, 0, process.stderr)
+        self.assertEqual(json.loads(process.stdout)['status'], 'passed')
+        with self.open() as ds:
+            record = ds.records()[0]
+            self.assertEqual(len(ds.records()), 1)
+            self.assertEqual((self.root/record['original_path']).read_bytes(), raw)
+            self.assertEqual(record['state'], 'needs_human_review')
+            self.assertEqual(len(ds.select('intention')), 1)
+            self.assertEqual(len(ds.select('source_status')), 28)
+            for event in ds.select('evidence'):
+                self.assertEqual(r.sha((self.root/event['path']).read_bytes()), event['sha256'])
+            pages = [p for p in ds.select('page') if p['class_id'] == 'species_01']
+            self.assertEqual([p['cursor'] for p in pages], [0, 10])
+            kinds = [event['type'] for event in ds.events]
+            self.assertLess(kinds.index('page'), kinds.index('intention'))
+            self.assertLess(kinds.index('committed'), kinds.index('cursor'))
+        before = r.tree_fingerprint(self.root)
+        (media/'123').unlink()  # A repeated execution must use the durable objects.
+        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
+        self.assertEqual(process.returncode, 0, process.stderr)
+        self.assertEqual(before, r.tree_fingerprint(self.root))
+
+
+class InaturalistResumeTests(DatasetCase, unittest.TestCase):
+    def prepare_round(self, request_cap=4):
+        from test_inaturalist_source import crosswalk, observation, page
+        cls = r.canonical()[0]
+        entry = crosswalk()
+        evidence = b'synthetic reviewed crosswalk evidence\n'
+        entry['taxonomy_ref_ids'] = cls['taxonomy_ref_ids']
+        entry['evidence'].update(path='evidence/crosswalk.json', sha256=r.sha(evidence))
+        self.config['crosswalk'][cls['class_id']] = entry
+        self.config['limits']['requests'] = request_cap
+        with self.open() as ds:
+            r.persist(ds.path(entry['evidence']['path']), evidence, immutable=True)
+            # Commons is already accounted for; exercise only the iNaturalist seam.
+            for item in r.canonical():
+                ds.append('source_status', {'source': 'commons', 'class_id': item['class_id'],
+                          'status': 'exhausted_within_query' if item['kind'] == 'species' else 'protection_not_queried'})
+        return cls, r.encode(page(observation()))
+
+    def test_timeout_then_restart_preserves_journal_limits_and_candidates(self):
+        cls, response = self.prepare_round()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertEqual([x['code'] for x in ds.select('response')], ['timeout'] * 3)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertEqual(ds.records(), [])
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [FakeResponse(body=response)])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(len(ds.select('request')), self.config['limits']['requests'])
+            self.assertEqual(len(ds.select('response')), 4)
+            self.assertEqual(len({x['request_id'] for x in ds.select('request')}), 4)
+            self.assertEqual(len(ds.select('page')), 1)
+            self.assertEqual(len(ds.select('cursor')), 1)
+            self.assertEqual(len(ds.records()), 1)
+            self.assertEqual(ds.records()[0]['state'], 'needs_license_review')
+            self.assertEqual(ds.records()[0]['class_ids'], [cls['class_id']])
+            self.assertEqual(ds.select('intention'), [])
+            self.assertEqual(ds.select('committed'), [])
+            kinds = [e['type'] for e in ds.events]
+            self.assertLess(kinds.index('evidence'), kinds.index('page'))
+            self.assertLess(kinds.index('page'), kinds.index('classified'))
+            self.assertLess(kinds.index('classified'), kinds.index('cursor'))
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            self.assertEqual(ds.config['limits'], self.config['limits'])
+            self.assertEqual(ds.summary()['usable'], 0)
+        stable = r.tree_fingerprint(self.root)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+    def test_only_existing_transient_recovery_codes_allow_restart(self):
+        cls, _ = self.prepare_round()
+        errors = [(r.RecoveryError(code), code) for code in sorted(r.RETRYABLE)]
+        errors += [(r.RecoveryError(code), 'inaturalist_contract_or_evidence') for code in
+                   ['http_403', 'http_404', 'request_budget', 'crosswalk_evidence_hash', 'invalid_json', 'unsafe_url']]
+        errors += [(r.inat.ContractError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (OSError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (KeyError('timeout'), 'inaturalist_contract_or_evidence')]
+        with self.open() as ds:
+            for error, expected in errors:
+                with self.subTest(error=type(error).__name__, code=str(error)):
+                    with patch.object(r.Transport, 'get', side_effect=error) as get:
+                        self.assertEqual(r.acquire_inat(ds, cls, r.Transport(ds), None), 'source_blocked')
+                    self.assertEqual(get.call_count, 1)
+                    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+
+    def test_timeout_restart_does_not_reset_request_budget(self):
+        self.prepare_round(request_cap=3)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertNotIn(ds.select('source_failure')[-1]['code'], r.RETRYABLE)
+            self.assertEqual(ds.records(), [])
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            stable = r.tree_fingerprint(self.root)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+
+class ContinuationProofs(DatasetCase, unittest.TestCase):
+    def test_inspect_html_identical_after_journal_reload(self):
+        with self.open() as ds:
+            ds.ingest(candidate(),lambda _:image_bytes())
+            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
+        before=r.tree_fingerprint(self.root)
+        with self.open() as ds:
+            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
+        self.assertEqual(before,r.tree_fingerprint(self.root))
+
+    def test_exact_projection_predecessor_is_journaled_without_changing_config(self):
+        self.config['code_sha256']['recover_p08.py']=r.HTML_ORDER_PREDECESSOR
+        with self.open() as ds:
+            self.assertEqual(len(ds.select('code_compatibility')),1)
+            self.assertEqual(ds.select('code_compatibility')[0]['to'],r.fingerprint())
+        before=r.tree_fingerprint(self.root)
+        with self.open() as ds:self.assertEqual(len(ds.select('code_compatibility')),1)
+        self.assertEqual(before,r.tree_fingerprint(self.root))
+        self.config['code_sha256']['inaturalist_source.py']='0'*64
+        with self.assertRaisesRegex(r.RecoveryError,'config_fingerprint'):
+            with self.open():pass
+
+    def test_full_round_retries_transient_media_without_requery(self):
+        c=candidate()
+        with self.open() as ds:
+            ds.save_page('commons','species_01',0,[c],None)
+            def fail(_):raise r.RecoveryError('timeout')
+            ds.ingest(c,fail);ds.advance(ds.select('page')[0])
+            ds.append('source_failure',{'source':'commons','class_id':'species_01','code':'timeout'})
+            ds.append('source_status',{'source':'commons','class_id':'species_01','status':'source_blocked'})
+        media=Path(self.tmp.name)/'media';media.mkdir();(media/'123').write_bytes(image_bytes())
+        with self.open() as ds:
+            self.assertEqual(r.acquire(ds,{'synthetic_media':str(media)}),0)
+            self.assertEqual(ds.records()[0]['state'],'needs_human_review')
+            self.assertEqual(len(ds.select('intention')),2)
+            before=r.tree_fingerprint(self.root)
+            self.assertEqual(r.acquire(ds,{}),0)
+            self.assertEqual(before,r.tree_fingerprint(self.root))
+
+    def test_round_marks_failed_media_retryable_instead_of_exhausted(self):
+        with self.open() as ds:
+            ds.save_page('commons','species_01',0,[candidate()],None)
+            with patch.object(r,'read',side_effect=r.RecoveryError('timeout')):
+                # Only the media loader uses read during this cached synthetic page.
+                with patch.object(r,'canonical',return_value=[{'class_id':'species_01','kind':'species'}]), patch.object(r,'validate_public'):
+                    self.assertEqual(r.acquire(ds,{'synthetic_media':self.tmp.name}),1)
+            self.assertEqual(ds.select('source_status')[0]['status'],'source_blocked')
+            self.assertEqual(ds.select('source_failure')[0]['code'],'timeout')
+
+    def test_lock_in_other_process_precedes_network(self):
+        script='''import sys
+from unittest.mock import patch
+sys.path.insert(0,sys.argv[1])
+import recover_p08 as r
+c=r.load(r.read(r.Path(sys.argv[2])/'config.json'))
+with patch('socket.create_connection',side_effect=AssertionError('network')):
+ try:
+  with r.Dataset(sys.argv[2],c,offline=True):raise AssertionError('concurrent writer')
+ except r.RecoveryError as e:
+  assert str(e)=='writer_locked'
+'''
+        with self.open():
+            p=subprocess.run([sys.executable,'-B','-c',script,str(Path(r.__file__).parent),str(self.root)],capture_output=True,text=True)
+            self.assertEqual(p.returncode,0,p.stderr)
+
+    def test_missing_and_changed_taxonomic_evidence_blocks_finalization(self):
+        with self.open() as ds:
+            c=ds.ingest(candidate(),lambda _:image_bytes())
+            # Mock only the pure decision to isolate the durable evidence gate.
+            inspection={'p07_images':17,'records':[c]}
+            r.persist(ds.path('inspection.json'),r.encode(inspection))
+            r.persist(ds.path('Attributions.jsonl'),r.encode(c))
+            r.persist(ds.path('evidence/map'),b'map')
+            r.persist(ds.path('evidence/botanical'),b'botanical')
+            d={'candidate_id':c['candidate_id'],'mapping':{'evidence_path':'evidence/map','evidence_sha256':r.sha(b'map')},
+               'botanical_evidence_path':'evidence/botanical','botanical_evidence':r.sha(b'botanical')}
+            file=Path(self.tmp.name)/'decision.json'
+            file.write_bytes(r.encode({'authority':'human','decisions':[d]}))
+            with patch.object(r,'decide',return_value='approved_for_dataset'):
+                r.persist(ds.path('evidence/map'),b'changed')
+                with self.assertRaisesRegex(r.RecoveryError,'mapping_evidence_hash'):r.finalize(ds,file)
+                self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')
+                r.persist(ds.path('evidence/map'),b'map')
+                r.persist(ds.path('evidence/botanical'),b'changed')
+                with self.assertRaisesRegex(r.RecoveryError,'botanical_evidence_hash'):r.finalize(ds,file)
+                r.persist(ds.path('evidence/botanical'),b'botanical')
+                r.finalize(ds,file)
+                before=r.tree_fingerprint(self.root);r.finalize(ds,file)
+                self.assertEqual(before,r.tree_fingerprint(self.root))
+
+    def test_decision_stale_after_taxonomy_or_class_change(self):
+        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
+        d={'authority':'human','reviewer':'Synthetic','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
+           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
+           'evidence_digest':r.review_digest(c)}
+        for key,value in [('mapping',{'source_taxon_id':123}),('class_ids',['species_02']),('author','Changed')]:
+            changed=copy.deepcopy(c);changed[key]=value
+            with self.assertRaisesRegex(r.RecoveryError,'stale_decision'):r.decide(changed,d)
+
+    def test_acceptance_binds_all_final_files(self):
+        with self.open() as ds:
+            r.acquire(ds,{})
+            for name in ['inspection.json','Attributions.jsonl','NOTICE.md','review.html']:
+                r.persist(ds.path(name),b'{}\n')
+            files={str(p.relative_to(self.root)):r.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file() and p.name!='.lock'}
+            manifest=r.encode({'files':files});r.persist(ds.path('final-manifest.json'),manifest)
+            acceptance=Path(self.tmp.name)/'acceptance.json'
+            acceptance.write_bytes(r.encode({'decision':'accepted','authority':'human','reviewer':'Synthetic',
+                  'reviewed_at':'2026-10-05T00:00:00Z','manifest_sha256':r.sha(manifest),'training_authorized':False}))
+            with patch.object(r,'historical',return_value=({},[])):
+                self.assertEqual(r.verify(ds,self.root,acceptance),0)
+                r.persist(ds.path('new-unbound-file'),b'x')
+                with self.assertRaisesRegex(r.RecoveryError,'acceptance_coverage_or_bytes'):r.verify(ds,self.root,acceptance)
+
+    def test_duplicate_comparison_against_17_with_boundary_distances(self):
+        with self.open() as ds:
+            rec=ds.ingest(candidate(),lambda _:image_bytes())
+            h=int(rec['technical']['dhash64'],16)
+            prior=[{'candidate_id':'Q'+str(i),'sanitized_sha256':'f'*64,'original_sha256':None,'observation_id':None,
+                    'technical':{'dhash64':format(h^((1<<n)-1),'016x')}} for i,n in enumerate([6,7,10,11]+[20]*13)]
+            with patch.object(r,'historical',return_value=({},prior)):
+                report=r.inspect(ds,self.root)
+                self.assertEqual(len(report['pairs']),17)
+                self.assertEqual([p['signal'] for p in report['pairs'][:4]],['near_duplicate','borderline','borderline','no_algorithmic_signal'])
+                before=r.tree_fingerprint(self.root);r.inspect(ds,self.root)
+                self.assertEqual(before,r.tree_fingerprint(self.root))
+                prior[0]['sanitized_sha256']=rec['sanitized_sha256']
+                r.inspect(ds,self.root)
+                self.assertEqual(ds.records()[0]['state'],'rejected_duplicate')
+                self.assertTrue(ds.path(rec['original_path']).exists())
+
+    def test_bad_schema_and_regressive_page(self):
+        with self.assertRaises(r.RecoveryError):r.commons_page({},r.canonical()[0],'a'*64,self.config)
+        with self.open() as ds:
+            with self.assertRaisesRegex(r.RecoveryError,'cursor_regression'):ds.save_page('commons','species_01',10,[],10)
+            for i in range(10):ds.save_page('commons','species_01',i*10,[],None)
+            with self.assertRaisesRegex(r.RecoveryError,'page_budget'):ds.save_page('commons','species_01',100,[],None)
+
+    def test_unsupported_media_classified_without_transfer(self):
+        with self.open() as ds:
+            c=candidate();c['file_url']='https://upload.wikimedia.org/a/a.svg'
+            self.assertEqual(ds.ingest(c,lambda _:self.fail('unsupported media downloaded'))['state'],'rejected_format')
+            self.assertEqual(ds.select('intention'),[])
+
+
+class ExtraTransportProofs(DatasetCase, unittest.TestCase):
+    transport=TransportTests.transport
+    api=TransportTests.api
+    media=TransportTests.media
+    def test_retryable_http_and_maxlag(self):
+        for status,body in [(429,b''),(500,b''),(502,b''),(503,b''),(504,b''),(200,b'{"error":{"code":"maxlag"}}')]:
+            with self.subTest(status=status),tempfile.TemporaryDirectory() as td:
+                with r.Dataset(Path(td)/'synthetic',self.config,offline=True) as ds:
+                    transport,factory,_,sleeps=self.transport(ds,[FakeResponse(status,body,{'Retry-After':'2'}),FakeResponse()])
+                    self.assertEqual(transport.get(self.api,'commons'),b'{}')
+                    self.assertEqual(factory.call_count,2)
+                    self.assertEqual(ds.select('response')[-1]['code'],'ok')
+                    self.assertEqual(sleeps.call_args_list[0].args,(2,))
+
+    def test_hour_and_media_reservations_survive_restart(self):
+        for limit,reason in [('hour_bytes','hour_budget'),('media_bytes','media_budget')]:
+            with self.subTest(limit=limit),tempfile.TemporaryDirectory() as td:
+                config=copy.deepcopy(self.config);config['limits']['file_bytes']=8;config['limits'][limit]=12
+                root=Path(td)/'synthetic'
+                with r.Dataset(root,config,offline=True) as ds:
+                    ds.append('request',{'request_id':'interrupted','source':'commons','media':True,'reserved':8,'epoch':1000})
+                with r.Dataset(root,config,offline=True) as ds:
+                    transport,factory,_,_=self.transport(ds,[])
+                    with self.assertRaisesRegex(r.RecoveryError,reason):transport.get(self.media,'commons',True)
+                    factory.assert_not_called()
+
+    def test_retry_after_http_date_and_cancelled_request_accounting(self):
+        with self.open() as ds:
+            transport,factory,_,_=self.transport(ds,[FakeResponse(503,headers={'Retry-After':'Thu, 01 Jan 1970 00:20:00 GMT'})])
+            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
+            self.assertEqual(ds.select('resume_after')[0]['epoch'],1200)
+        with self.open() as ds:
+            transport,factory,_,_=self.transport(ds,[])
+            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
+            factory.assert_not_called()
+
+
+if __name__ == '__main__':
+    unittest.main()
+
+```
+
+### scripts/phase1/test_inaturalist_source.py
+
+```text
+"""Synthetic iNaturalist adapter contracts; no network or real identifiers."""
+import copy
+import unittest
+from inaturalist_source import ContractError, build_query, parse_page, photo_record
+
+
+CUTOFF = "2026-10-05T00:00:00Z"
+CLASS = {"class_id": "species_01", "kind": "species", "scientific_name": "Epipremnum aureum", "taxonomy_ref_ids": ["kew_species_01"]}
+
+
+def crosswalk():
+    return {"class_id": "species_01", "source": "inaturalist", "namespace": "inaturalist", "source_taxon_id": 999999001,
+            "scientific_name": CLASS["scientific_name"], "rank": "species", "status": "active", "synonym_of": None,
+            "authorship": None, "authorship_missing_reason": "Not supplied by synthetic source", "taxonomy_ref_ids": ["kew_species_01"],
+            "evidence": {"url": "https://www.inaturalist.org/taxa/999999001", "version": "fixture-v1", "date": "2026-10-04", "sha256": "a" * 64},
+            "reviewer": {"id": "synthetic-reviewer", "qualification": "synthetic botanist", "decision": "approved"}}
+
+
+def observation(identifier=999999002):
+    return {"id": identifier, "created_at": "2026-10-04T00:00:00Z", "quality_grade": "research", "license_code": "cc0",
+            "taxon": {"id": 999999001, "name": CLASS["scientific_name"], "rank": "species", "is_active": True},
+            "photos": [{"id": 999999003, "license_code": "cc-by", "attribution": "Synthetic author, CC BY", "url": "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg"}]}
+
+
+def legal():
+    return {"photo_id": 999999003, "observation_id": 999999002, "reviewer": "synthetic-reviewer", "reviewed_at": CUTOFF,
+            "author": "Synthetic author", "licensor": "Synthetic author", "credit": "Synthetic credit", "decision": "approved",
+            "photo": {"license_code": "cc-by", "version": "4.0", "legal_url": "https://creativecommons.org/licenses/by/4.0/", "evidence_sha256": "b" * 64, "source_url": "https://www.inaturalist.org/photos/999999003", "restrictions": []},
+            "observation": {"license_code": "cc0", "version": "1.0", "legal_url": "https://creativecommons.org/publicdomain/zero/1.0/", "evidence_sha256": "c" * 64, "source_url": "https://www.inaturalist.org/observations/999999002", "restrictions": []},
+            "database_rights": "compatible"}
+
+
+def page(*observations):
+    return {"total_results": len(observations), "page": 1, "per_page": 100, "results": list(observations)}
+
+
+class AdapterTests(unittest.TestCase):
+    def test_query_exact_contract(self):
+        query = build_query(crosswalk(), CLASS, CUTOFF)
+        self.assertEqual(query["taxon_id"], 999999001)
+        self.assertEqual(query["created_d2"], "2026-10-05")
+        self.assertEqual((query["order_by"], query["order"], query["per_page"]), ("id", "asc", 100))
+        self.assertEqual(query["quality_grade"], "research")
+        self.assertEqual(query["photos"], "true")
+
+    def test_crosswalk_required_fields_and_identity(self):
+        for key in crosswalk():
+            entry = crosswalk()
+            del entry[key]
+            if key == "authorship_missing_reason":
+                pass
+            with self.subTest(key=key), self.assertRaises(ContractError):
+                build_query(entry, CLASS, CUTOFF)
+        for key, value in [("scientific_name", "Pothos aureus"), ("namespace", "wikidata"), ("source_taxon_id", True), ("rank", "subspecies"), ("status", "inactive"), ("synonym_of", 9), ("taxonomy_ref_ids", [])]:
+            entry = crosswalk()
+            entry[key] = value
+            with self.subTest(key=key), self.assertRaises(ContractError):
+                build_query(entry, CLASS, CUTOFF)
+
+    def test_protection_never_queries(self):
+        for class_id in ("outra_planta", "imagem_invalida"):
+            with self.assertRaises(ContractError):
+                build_query(crosswalk(), {"class_id": class_id, "kind": "protection"}, CUTOFF)
+
+    def test_cutoff_must_have_timezone(self):
+        with self.assertRaises(ContractError):
+            build_query(crosswalk(), CLASS, "2026-10-05")
+
+    def test_photo_code_alone_never_authorizes(self):
+        obs = observation()
+        result = photo_record(obs["photos"][0], obs)
+        self.assertFalse(result["download_allowed"])
+        self.assertIsNone(result["file_url"])
+        self.assertIn("needs_license_review", result["reasons"])
+        obs["photos"][0]["license_code"] = ["cc-by"]
+        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
+
+    def test_documented_size_mapping_and_individual_evidence(self):
+        obs = observation()
+        result = photo_record(obs["photos"][0], obs, legal())
+        self.assertTrue(result["download_allowed"])
+        self.assertTrue(result["file_url"].endswith("/999999003/original.jpg"))
+        self.assertEqual(result["origin_fidelity"], "provider_original")
+        self.assertFalse(result["camera_original_verified"])
+
+    def test_observation_rights_do_not_inherit_photo_rights(self):
+        obs = observation()
+        obs["license_code"] = "cc-by-nc"
+        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
+
+    def test_legal_proof_must_bind_ids_and_version_author_and_database(self):
+        for field, value in [("photo_id", 9), ("observation_id", 9), ("author", ""), ("licensor", ""), ("credit", ""), ("reviewer", ""), ("database_rights", "unknown")]:
+            proof = legal()
+            proof[field] = value
+            obs = observation()
+            with self.subTest(field=field):
+                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])
+        for field, value in [("version", "3.0"), ("legal_url", "https://creativecommons.org/licenses/by/3.0/"), ("restrictions", ["extra"]), ("evidence_sha256", None), ("source_url", "https://www.inaturalist.org/photos/9")]:
+            proof = legal()
+            proof["photo"][field] = value
+            obs = observation()
+            with self.subTest(field=field):
+                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])
+
+    def test_url_confusion_does_not_generate_original(self):
+        urls = ["http://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com.evil.invalid/photos/999999003/square.jpg", "https://[REDACTED EMAIL]/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com:444/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/9/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/../square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.gif", "https://static.inaturalist.org/photos/999999003/square.jpg"]
+        for url in urls:
+            obs = observation()
+            obs["photos"][0]["url"] = url
+            with self.subTest(url=url):
+                self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])
+
+    def test_page_preserves_pending_without_location(self):
+        obs = observation()
+        obs["location"] = "0,0"
+        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
+        self.assertEqual(len(result["candidates"]), 1)
+        self.assertFalse(result["candidates"][0]["download_allowed"])
+        self.assertNotIn("location", result["candidates"][0])
+        self.assertEqual(result["next_id_above"], obs["id"])
+
+    def test_exact_species_and_active_required(self):
+        for key, value in [("id", 999999004), ("name", "Pothos aureus"), ("rank", "subspecies"), ("is_active", False)]:
+            obs = observation()
+            obs["taxon"][key] = value
+            result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
+            self.assertEqual(result["candidates"][0]["taxonomic_confidence"], "conflict")
+            self.assertIn("needs_taxonomic_mapping", result["candidates"][0]["reasons"])
+
+    def test_regressive_duplicate_or_after_cutoff_page_fails(self):
+        for observations in [(observation(), observation()), (observation(999999004), observation()), (dict(observation(), created_at="2026-10-06T00:00:00Z"),)]:
+            with self.assertRaises(ContractError):
+                parse_page(page(*observations), crosswalk(), CLASS, CUTOFF)
+        with self.assertRaises(ContractError):
+            parse_page(page(observation()), crosswalk(), CLASS, CUTOFF, id_above=999999002)
+
+    def test_schema_failures(self):
+        for response in [{}, {"results": []}, dict(page(), per_page=101), dict(page(), page=2), dict(page(), total_results=True), page(dict(observation(), photos=None)), page(dict(observation(), quality_grade="casual"))]:
+            with self.subTest(response=response), self.assertRaises(ContractError):
+                parse_page(response, crosswalk(), CLASS, CUTOFF)
+
+    def test_100_photo_ceiling_with_deferred_accounting(self):
+        obs = observation()
+        obs["photos"] = [dict(obs["photos"][0], id=999999100+i) for i in range(105)]
+        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
+        self.assertEqual(len(result["candidates"]), 100)
+        self.assertEqual(result["deferred_photo_count"], 5)
+
+    def test_duplicate_media_not_inflated(self):
+        obs = observation()
+        obs["photos"].append(copy.deepcopy(obs["photos"][0]))
+        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
+        self.assertEqual(len(result["candidates"]), 1)
+        self.assertEqual(result["duplicate_photo_count"], 1)
+
+
+if __name__ == "__main__":
+    unittest.main()
+
+```
+
+### Reconciled evidence
+```json
+{
+  "kind": "working_bytes_evidence_reconciliation_not_guard_proof",
+  "checked_at": "2026-10-07T23:08:02.977490+00:00",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "records": {
+    "regression-red": {
+      "record_sha256": "2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74",
+      "source_and_output_hashes_match": true,
+      "exit_code": 1,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 3 tests in 0.125s",
+        "",
+        "FAILED (failures=12)"
+      ]
+    },
+    "regression-green": {
+      "record_sha256": "25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 3 tests in 0.205s",
+        "",
+        "OK"
+      ]
+    },
+    "focal-recovery": {
+      "record_sha256": "f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 54 tests in 3.052s",
+        "",
+        "OK"
+      ]
+    },
+    "focal-adapter": {
+      "record_sha256": "e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 15 tests in 0.007s",
+        "",
+        "OK"
+      ]
+    },
+    "affected-history": {
+      "record_sha256": "e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f",
+      "source_and_output_hashes_match": true,
+      "exit_code": 0,
+      "stderr_summary": [
+        "----------------------------------------------------------------------",
+        "Ran 236 tests in 10.852s",
+        "",
+        "OK"
+      ]
+    }
+  },
+  "historical_red_proof_id": "proof-6928ea925e6f438e3873543389326106",
+  "historical_red_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "mutations_reused": [
+    "advance_cursor_before_commit",
+    "allow_private_export",
+    "bypass_expert",
+    "bypass_license",
+    "ignore_hash_mismatch"
+  ],
+  "preexisting_documents_unchanged": true,
+  "preexisting_changed_only_by_authorized_fix_transition": [
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak"
+  ],
+  "external_bytes_and_mtimes_unchanged": true,
+  "external_counts": {
+    "p06-recovery-20260928": 29,
+    "p07-curation-20260928": 13,
+    "p08-recovery-20261005": 139,
+    "p08-recovery-20261005-backup": 138
+  },
+  "external_inventory_sha256": "6f35f2692d2901aa6bffbdea44912940267bbddf069452f2b0a3650374d9a30f",
+  "dependency_hashes": {
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS": "9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23",
+    "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json": "f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee",
+    "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
+    "scripts/phase1/acquire_commons.py": "ddd2bf5d5f6c7e75fe090af8fd0313a9785fefccb30ee3a62b070a48f0ba6046",
+    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/requirements-p06.txt": "41b54a6fb2918667ca47a61d73b522629d84490f3d78f0f20b21135faba10d35",
+    "scripts/phase1/test_acquire_commons.py": "3d7781ef2e70f9ee57331cff72848ac3b61be3c9ec33f627ae8c8b4fb01d622e",
+    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed"
+  },
+  "new_test_executions": 0,
+  "guard_proofs_for_fixed_bytes": false
+}
+```
+
+### regression-red
+```json
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py",
+    "-k",
+    "InaturalistResumeTests",
+    "-v"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:35.344637+00:00",
+  "exit_code": 1,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
+
+```
+```text
+test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... 
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after') ... FAIL
+  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout') ... FAIL
+test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... FAIL
+test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... FAIL
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_429'
+- inaturalist_contract_or_evidence
++ http_429
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_500'
+- inaturalist_contract_or_evidence
++ http_500
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_502'
+- inaturalist_contract_or_evidence
++ http_502
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_503'
+- inaturalist_contract_or_evidence
++ http_503
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'http_504'
+- inaturalist_contract_or_evidence
++ http_504
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'maxlag'
+- inaturalist_contract_or_evidence
++ maxlag
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'network_error'
+- inaturalist_contract_or_evidence
++ network_error
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'response_timeout'
+- inaturalist_contract_or_evidence
++ response_timeout
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'resume_after'
+- inaturalist_contract_or_evidence
++ resume_after
+
+
+======================================================================
+FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout')
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
+    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+======================================================================
+FAIL: test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget)
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 594, in test_timeout_restart_does_not_reset_request_budget
+    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+======================================================================
+FAIL: test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates)
+----------------------------------------------------------------------
+Traceback (most recent call last):
+  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 534, in test_timeout_then_restart_preserves_journal_limits_and_candidates
+    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
+AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
+- inaturalist_contract_or_evidence
++ timeout
+
+
+----------------------------------------------------------------------
+Ran 3 tests in 0.125s
+
+FAILED (failures=12)
+
+```
+
+### regression-green
+```json
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py",
+    "-k",
+    "InaturalistResumeTests",
+    "-v"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:42.229752+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
+
+```
+```text
+test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... ok
+test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... ok
+test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... ok
+
+----------------------------------------------------------------------
+Ran 3 tests in 0.205s
+
+OK
+
+```
+
+### focal-recovery
+```json
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_recover_p08.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:52.443028+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
+
+```
+```text
+......................................................
+----------------------------------------------------------------------
+Ran 54 tests in 3.052s
+
+OK
+
+```
+
+### focal-adapter
+```json
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_inaturalist_source.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:55.827623+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+  "stderr_sha256": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
+
+```
+```text
+...............
+----------------------------------------------------------------------
+Ran 15 tests in 0.007s
+
+OK
+
+```
+
+### affected-history
+```json
+{
+  "kind": "working_bytes_not_guard_proof",
+  "argv": [
+    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
+    "-B",
+    "-m",
+    "unittest",
+    "discover",
+    "-s",
+    "scripts/phase1",
+    "-p",
+    "test_*.py"
+  ],
+  "cwd": ".",
+  "started_at": "2026-10-07T22:56:55.924807+00:00",
+  "exit_code": 0,
+  "stdout_sha256": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
+  "stderr_sha256": "de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac",
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "source_sha256": {
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
+  }
+}
+
+```
+```text
+............................................................................................................................................................................................................................................
+----------------------------------------------------------------------
+Ran 236 tests in 10.852s
+
+OK
+
+```
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json b/artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json
new file mode 100644
index 0000000..c815362
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/security-inspection.json
@@ -0,0 +1,127 @@
+{
+  "kind": "working_tree_commit_set_inspection_not_guard_proof",
+  "result": "passed",
+  "scanned_files_sha256": {
+    "artifacts/bianchini/v2/codex/P08/audit-final.json": "4431ab3f00cdeec62fecbb2058f18dcfb63c4d33b223bd5f972726493cb97c80",
+    "artifacts/bianchini/v2/codex/P08/checkpoint.json": "9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt": "4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt": "7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt": "ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt": "029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/guard-status.json": "956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+    "artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json": "7d5a07f194b89238e3508418f8a01c23d9fa9c48b07851633923bfa1d4bb59f4",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt": "ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt": "ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539",
+    "artifacts/bianchini/v2/codex/P08/closure/independent-review.json": "c7dd7ddc83182ef6814666a33815aa8eb9703d06575b4b6a1c988945b625c308",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt": "f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e",
+    "artifacts/bianchini/v2/codex/P08/closure/proof-results.json": "89d3ddb5e3202f9e5302f6b16594034261822f1ec010cd4b82c2125d046f713f",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json": "ce0639a118bc8199074287dcd4eb1241dcf9065252dbe27c2a0c8b86b417a4a1",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-report.md": "5b846275cb8106379130786aee919ba7e5660c876f2b8bd51cb8e3e930f0e54a",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+    "artifacts/bianchini/v2/codex/P08/closure/review-package.md": "279a71c6f422ec2cd4ea96e186c4cc9b0d1c2d25ec64096e94ee58bdd5228948",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+    "artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json": "edce9f48d1a230bfb2aa98072b99f2d8ef28ec30bcc92c87206667a7cae80296",
+    "artifacts/bianchini/v2/codex/P08/continuation-report.md": "fc42eb7ba4a348d0edb206dcf69867ef1bbea45b73a6a4b4a44443b303f5635d",
+    "artifacts/bianchini/v2/codex/P08/final-files.sha256": "5c5c61406db304c42671a727a2016b566b2e5d5fca2c487466f3adebb09055b2",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/acceptance-package.md": "7039b2669e97b9545d424451cfe745d3f182201c88b80fdd858be7cc7de77a45",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json": "e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt": "de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json": "84998da46e2782c76a75b7310063d3926b7b2a71ffb2e3d176b0c1244cef0b54",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/checkpoint.json": "3dab65e6e07bf0ad2bfc426e7afc919bfc10192618e12ea4ccc47cfa9fae76fe",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.json": "32fcf753a20c68b5ccddfad07b283a11264cfbc9099ea5866db609e233453f5f",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/commit-inventory.txt": "3f7899f68082e8f8bce1e3d0cacd4d8ff811e0e829e0a236fd2c1bebdc4668c8",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/evidence-reconciliation.json": "782ee5d0b1d150b10839425a5930ec6174e531ac23c5cfcb329f40b4a3505e61",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json": "6f6f9a97d3da3a0a1682101b039ae29328515a91d544776c5e8a63d1d3ab1517",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json": "e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json": "f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt": "d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json": "956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json": "c84acef69292ab80a7276292012167b52bc7c04cc9689a759318dacc71bc1d17",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/guard-resumed.json": "c84acef69292ab80a7276292012167b52bc7c04cc9689a759318dacc71bc1d17",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md": "29f0379d43191f8030a94edf9496e43a15bbe2a3e636e660ef2ab6392ed28498",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/independent-review-assessment.json": "76d03c0a41bdffd56bd8aa25af3bac683dd6702b720c3a355493301b893d59c1",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/independent-review.json": "8aa973100a15bf817985395637131e838cf84e427be4792583def923f020f5fa",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json": "78e3d2077b31f1610af2b8e4710f29e0fc27180b9835677eb989cfd159ae2a0b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch": "659d8c1defba1ff49236bc25965b2a90a66fb2b5228dc4e3ed4fd8d40f6ad24b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json": "ccf06e3f5681ebb3c34cd83900d1e19cdef5adc3adcb3df1edff9ed7afbc2316",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json": "25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt": "6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json": "2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt": "075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/resume-preflight.json": "a8bf22d06b660c169a59aedbe86c4d64199ffc5e0b4067fda8b4a9c1b5c551b1",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/review-package.md": "8583b460784bb4749c73c8616a7c3ad73fa0ac36be89faddd865090cd27fc5d7",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json": "e106ffc8c99a844a5c7483c511a87c7c741f14a507e1b2c227f1bd80d7ed30b7",
+    "artifacts/bianchini/v2/codex/P08/focal-inat-final.txt": "2fdf7a432a53fceb691486981be60fcb65192fbaa6b7627e6b3fe3a0c95917bf",
+    "artifacts/bianchini/v2/codex/P08/focal-inat.txt": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+    "artifacts/bianchini/v2/codex/P08/focal-recovery-final.txt": "2685ccaab15660c44c951beb8fe9c19d6d9e9e347b91699628320b87c86b058f",
+    "artifacts/bianchini/v2/codex/P08/full-suite-final.txt": "ed24024f0c3d1b17f96cc32552dd6391462ca11089c74f599305c51d7ec0a660",
+    "artifacts/bianchini/v2/codex/P08/full-suite.txt": "3d6689642da34d73791790f53db3d6b989e16eabbd850972ccfaa176e92b2db0",
+    "artifacts/bianchini/v2/codex/P08/human-acceptance.json": "3650e20c20ceb6ec2b76d55636202a86159ed7fc6ba108239f43edad12ea0d3d",
+    "artifacts/bianchini/v2/codex/P08/implementer-report.md": "b3cb7bb752829b2c95971653c14d460b7e26f2ef095b895f2b33921fe94c1a5b",
+    "artifacts/bianchini/v2/codex/P08/inat-red.txt": "5588c065e674a94b4cfc0f14748eac93d6f2fb0101e5f32a5e992420840eb645",
+    "artifacts/bianchini/v2/codex/P08/manifest.txt": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+    "artifacts/bianchini/v2/codex/P08/mutation-evidence-final.json": "23527bd62c51bdc91b6bf9193ed60bf68a267c0dbd432ac4be88a05fc6f1c315",
+    "artifacts/bianchini/v2/codex/P08/mutation-evidence.json": "55ef68eefb2e85931f2c4a303d161b326bccea87468311ec22db47ee62996ba5",
+    "artifacts/bianchini/v2/codex/P08/real-round.json": "d090bc5706aeff5ae351260208365c2e37a83eec2570b8085a5dbbfd9e78b0af",
+    "artifacts/bianchini/v2/codex/P08/recovery-red.txt": "9d56b591390394d0f50ce1532442a2bc571c26c93329b08a92e518521092fc34",
+    "artifacts/bianchini/v2/codex/P08/resume-inventory.json": "61c61bfa952bc0d2958c9eb1dc4fb053bf30700e9cd67da051679cb9b4f6a19f",
+    "artifacts/bianchini/v2/codex/P08/resumed-test_inaturalist_source.py.txt": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+    "artifacts/bianchini/v2/codex/P08/resumed-test_recover_p08.py.txt": "e885f40ddecec4eef4b0585e1f71e621c9f3188e3aaf84bda2ec2856e74763a2",
+    "artifacts/bianchini/v2/codex/P08/roster-hashes.txt": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+    "artifacts/bianchini/v2/codex/P08/task-brief.md": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+    "artifacts/bianchini/v2/codex/P08/verification-final.json": "8893c65c032fbb63e54671ad422e661421c5d1ee354ecf2716cb103f1e5ccd3b",
+    "artifacts/bianchini/v2/codex/P08/verification.json": "7de6424ec7e3e7d6cbec51fa4402a5c3d1d5780a8431808891d81be913635296",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json": "4124764ea9235d0dca6c5b6042890a9d10c60f2ef06595309e0f5b6a9e8fdcf6",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json": "c1bf12a234012329aa6c5ffc0347e97cc29438b2fc8e2c295e7bc20766adf0f1",
+    "artifacts/bianchini/v2/ledgers/P08.md": "b05ec6a4c44731c1973f905bc71b96952b270706e4602c78b90f1aa940865547",
+    "artifacts/phase1/p08/summary.json": "d1130531abea27c2d6bb157fda7be376b3cefec514b49fb5374c82fcd8cb2c4f",
+    "docs/living/PROJECT_STATE.md": "3639b3bd12e288b79488df30e0ef29144659019b50d61f4c2d289656aff42100",
+    "docs/phase1/P08-recovery.md": "10c454fcc82cf17a8051f37e8ca81defcd3a78ae6f180c8008e4bfb89b0d218b",
+    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
+    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239"
+  },
+  "automated_findings": [],
+  "manual_classification": [
+    "No binary/image files or image base64, live credentials, private keys, .env, real candidate payloads or actual private reviewer identities found in proposed set.",
+    "Email-like matches in original tests are userinfo rejection fixtures; new review annex quotes the same synthetic fixtures.",
+    "API/legal/project URLs and generated item URL templates are code/contracts; example media IDs and candidate URLs are synthetic tests. No newly exported real candidate URL.",
+    "Private field names occur in schemas, test assertions and historical proof argv. No real private field values newly included.",
+    "Historical worktree/tool paths and code that references external roots are preserved operational provenance, not embedded external dataset contents.",
+    "Granular external inventory retained local-only; no deletion. Guard backups/lock likewise retained local-only.",
+    "Original 33-path implementation inventory inspected to distinguish historical synthetic fixtures and artifacts; original commit and original acceptance unchanged.",
+    "This inspection does not provide botanical, licensing or visual privacy approval of dataset candidates."
+  ],
+  "local_exclusions": {
+    "artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json": "Preserved local-only granular external dataset filename/hash/mtime inventory; aggregate integrity result is proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak": "Preserved operational sidecar backup; canonical sidecar proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.bak": "Preserved operational proof backup; canonical signed store proposed.",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.lock": "Preserved empty operational lock; not a deliverable."
+  },
+  "scan_limitations": "Heuristic scan plus manual classification; not a claim of universal secret detection. This report and derived manifest/digest are separately reviewed metadata, excluded from their own hash sets."
+}
diff --git a/artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json b/artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json
new file mode 100644
index 0000000..8e6c776
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/P08/fix-B1/session-start-inventory.json
@@ -0,0 +1,71 @@
+{
+  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "files": {
+    "artifacts/bianchini/v2/ledgers/P08.md": "9bb91c9f54ab4cc389ed0608b667477c653383236b293672d73f9c75ab446f49",
+    "docs/living/PROJECT_STATE.md": "3639b3bd12e288b79488df30e0ef29144659019b50d61f4c2d289656aff42100",
+    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
+    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt": "4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2",
+    "artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt": "7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt": "ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt": "029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b",
+    "artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/guard-status.json": "956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+    "artifacts/bianchini/v2/codex/P08/closure/implementation-inventory.json": "7d5a07f194b89238e3508418f8a01c23d9fa9c48b07851633923bfa1d4bb59f4",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt": "ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d",
+    "artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt": "ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539",
+    "artifacts/bianchini/v2/codex/P08/closure/independent-review.json": "c7dd7ddc83182ef6814666a33815aa8eb9703d06575b4b6a1c988945b625c308",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt": "f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e",
+    "artifacts/bianchini/v2/codex/P08/closure/proof-results.json": "89d3ddb5e3202f9e5302f6b16594034261822f1ec010cd4b82c2125d046f713f",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-checkpoint.json": "ce0639a118bc8199074287dcd4eb1241dcf9065252dbe27c2a0c8b86b417a4a1",
+    "artifacts/bianchini/v2/codex/P08/closure/recovery-report.md": "5b846275cb8106379130786aee919ba7e5660c876f2b8bd51cb8e3e930f0e54a",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+    "artifacts/bianchini/v2/codex/P08/closure/review-package.md": "279a71c6f422ec2cd4ea96e186c4cc9b0d1c2d25ec64096e94ee58bdd5228948",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.json": "e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stderr.txt": "de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/affected-history.stdout.txt": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/change-policy.json": "84998da46e2782c76a75b7310063d3926b7b2a71ffb2e3d176b0c1244cef0b54",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json": "6f35f2692d2901aa6bffbdea44912940267bbddf069452f2b0a3650374d9a30f",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/external-preserved.json": "6f6f9a97d3da3a0a1682101b039ae29328515a91d544776c5e8a63d1d3ab1517",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.json": "e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stderr.txt": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-adapter.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.json": "f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stderr.txt": "d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/focal-recovery.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/guard-before.json": "956418120bc4f15a188aa9c14dcb4ab02d656d58c62a9ecf59059fb2f8acf7a0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/guard-fix-started.json": "c84acef69292ab80a7276292012167b52bc7c04cc9689a759318dacc71bc1d17",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md": "3e3d88e1c7afca1e297118a81566cb99d4ca4db0dd699d27641f0582c1c097e1",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/preexisting-inventory.json": "78e3d2077b31f1610af2b8e4710f29e0fc27180b9835677eb989cfd159ae2a0b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/recovery-documentary-before.patch": "659d8c1defba1ff49236bc25965b2a90a66fb2b5228dc4e3ed4fd8d40f6ad24b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/red-reused.json": "ccf06e3f5681ebb3c34cd83900d1e19cdef5adc3adcb3df1edff9ed7afbc2316",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.json": "25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stderr.txt": "6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-green.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.json": "2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stderr.txt": "075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded",
+    "artifacts/bianchini/v2/codex/P08/fix-B1/regression-red.stdout.txt": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json": "4124764ea9235d0dca6c5b6042890a9d10c60f2ef06595309e0f5b6a9e8fdcf6",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.bak": "2d444b7debf303cfb06079e4d2bccdb272c80b28d28735bdfd67575f13724835",
+    "artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json.lock": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json": "c1bf12a234012329aa6c5ffc0347e97cc29438b2fc8e2c295e7bc20766adf0f1",
+    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak": "3ae61e20fa92ee2cfe2fd21a7922d5c7f607ee0a991087d8c7e3c05818827d0d"
+  }
+}
diff --git a/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json b/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json
new file mode 100644
index 0000000..7ca096f
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/convergence/P08/.proofs/1.json
@@ -0,0 +1,297 @@
+{
+  "created_at": "2026-10-07T22:34:34.444651Z",
+  "plan_id": "P08",
+  "planning_version": "v2",
+  "proofs": {
+    "proof-034132282be7abb6b24447b178256ca0": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/historical-checksums.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.900475Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+      "signature": "c4539628b78879335d57d375116a9bf931c3571610dbe4106adfcb1d69cd76a5",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-103d80e98b7ad5ab26a325e7645dc5e9": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport sys,json,hashlib,stat,fcntl,subprocess,re\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nroot=Path.cwd();base=Path('/home/administradorarthur/datasets/scanplant');data=base/'p08-recovery-20261005';backup=base/'p08-recovery-20261005-backup';source=base/'p06-recovery-20260928'\\nreceipt=json.loads((root/'artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_bytes())\\nassert receipt['decision']=='accepted' and receipt['authority']=='human' and receipt['scope']=='technical_and_documentary_bytes_only'\\nassert receipt['approved_git_delivery_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/final-files.sha256')\\nassert receipt['approved_checkpoint_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json')\\nassert receipt['baseline']==subprocess.check_output(['git','rev-parse','HEAD^'],text=True).strip()\\nassert receipt['counts']==dict(candidates_pending=1088,transferred=0,p08_images=0,approved_for_dataset=0,usable=0)\\nassert receipt['zero_transfer_result_accepted'] is True and receipt['U-803']=='candidate_opinions_pending'\\nfor k in ['candidate_approval','download_authorized','authorship_confirmation','rights_approval','botanical_confirmation','privacy_approval','duplicate_decisions_conclusive','training_authorized','partition_authorized','p09_started']:assert receipt[k] is False,k\\nassert receipt['release']=='pending'\\nbefore={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nmanifest=json.loads((data/'final-manifest.json').read_bytes())\\nfor folder in [data,backup]:\\n assert h(folder/'final-manifest.json')==receipt['approved_external_manifest_sha256']=='334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716'\\n actual={str(p.relative_to(folder)):h(p) for p in folder.rglob('*') if p.is_file() and p.name not in ['.lock','final-manifest.json']}\\n assert actual==manifest['files'] and len(actual)==137\\n assert stat.S_IMODE(folder.stat().st_mode)==0o700\\n for p in folder.rglob('*'):\\n  assert not p.is_symlink()\\n  assert stat.S_IMODE(p.stat().st_mode)==(0o700 if p.is_dir() else 0o600)\\n  assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif'}\\nassert (data/'.lock').read_bytes()==b''\\nconfig=r.load(r.read(data/'config.json'));assert r.sha(r.encode(config))==manifest['config_sha256']\\nassert manifest['runtime_code_sha256']==r.fingerprint()\\nassert manifest['code_sha256']==config['code_sha256']\\nassert config['code_sha256']['recover_p08.py']==r.HTML_ORDER_PREDECESSOR\\nwith (data/'.lock').open('rb') as lock,patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')),patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')):\\n fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)\\n ds=r.Dataset(data,config);ds.replay();ds.verify_objects()\\n assert ds.events[0]['data']==config\\n assert {'from':config['code_sha256'],'to':r.fingerprint(),'reason':'deterministic_review_html_key_order'} in ds.select('code_compatibility')\\n assert r.verify(ds,source)==0\\n hashes,images=r.historical(source);assert len(hashes)==29 and len(images)==17\\n records=ds.records();summary=ds.summary()\\n assert len(records)==1088 and summary==r.load(r.read(data/'summary.json'))==r.load(r.read(root/'artifacts/phase1/p08/summary.json'))\\n assert summary['usable']==0 and summary['training_authorized'] is False and summary['partition_authorized'] is False\\n assert all(x['state']!='approved_for_dataset' and not x.get('original_sha256') and not x.get('sanitized_sha256') for x in records)\\n assert len(ds.select('page'))==len(ds.select('cursor'))==120 and not ds.select('committed') and not ds.select('received') and not ds.select('source_failure')\\n assert all(x['status']=='no_crosswalk' for x in summary['coverage'] if x['source']=='inaturalist' and x['class_id'].startswith('species_'))\\n assert len(summary['coverage'])==28 and all(x['transferred']==x['approved']==0 for x in summary['coverage'])\\n review=r.load(r.read(data/'human-review.json'));objects=r.load(r.read(data/'object-hashes.json'));decisions=r.load(r.read(data/'decisions.template.json'))\\n assert len(review['candidates'])==len(objects)==len(decisions['decisions'])==1088\\n assert {x['candidate_id'] for x in review['candidates']}=={x['candidate_id'] for x in records}=={x['candidate_id'] for x in decisions['decisions']}\\n assert all(x['reviewer'] is None and x['expert_confirmation'] is False for x in decisions['decisions'])\\n assert r.read(data/'Attributions.jsonl')==b''\\n assert len(ds.select('request'))==120\\n for n in ['historical-before.json','historical-before-after.json']:\\n  historical=r.load(r.read(data/n));assert len(historical)==17\\n # Replay and verification are read-only: no acquisition/inspection/finalization invocation.\\n ds2=r.Dataset(data,config);ds2.replay();assert ds2.events==ds.events and ds2.summary()==summary\\nassert before=={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nprint(json.dumps({'result':'passed','external_files_each':138,'manifest_sha256':receipt['approved_external_manifest_sha256'],'historical_files':29,'historical_images':17,'p07_receipt_hashes':7,'candidates_pending':1088,'transferred':0,'approved_for_dataset':0,'usable':0,'read_only_replay_bytes_and_mtimes_unchanged':True,'acceptance':'technical_bytes_only','candidate_review':'pending','inat':'no_crosswalk','training_authorized':False,'release':'pending','p09_started':False},sort_keys=True))\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/external-integrity-and-human-acceptance.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:37:03.153530Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "signature": "4ae6d337898ce8a32f222812c01f26946f924718e986f00b0270d995a0c4d1d3",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-20c948a7c09b3cd0de5e999267bf1cd1": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_inaturalist_source.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-adapter.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:34.841212Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+      "signature": "b42a84d6e2cd5c0041db9b996e01533a295aced6438aca3cd2f2452ab555cc68",
+      "spawn_error": false,
+      "stderr_sha256": "c39c88100a3b6b5a07400fd4f9264af9dcb67d8bf0752a29fda6fee19edc8cbc",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-23228b63703e5fb20da4c1b69fa9c73b": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/affected-history-and-selective-mutation.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.263570Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "signature": "280df38f125407d5858b1d9c968a6a18de26fe3b3fddf687a4ca4dbd66b4dec7",
+      "spawn_error": false,
+      "stderr_sha256": "4c1941c18d3cb7befdb524c22a1e8710e2bb86b1e69ef1132a9b3be78a6662b2",
+      "stdout_sha256": "7c48c1ff3bf068b381d100c2643a24d831cb0fe353777569b4f8bc997c09a2c6",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-28272ad7fd0c858844fb8e2306c628e4": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'snapshot', 'verify', 'docs/living/PROJECT_STATE.md', '--root', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-snapshot.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:46.107195Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+      "signature": "b3104b168241884cf6566475d3efd78d7b5167aac29f5cbfc44cfa40b08de48a",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "f27fe920640e4be6f3023d3faa37d9db78fad3b5ef05977e000e402742cf8c5e",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-4745dbc8b82d4bebede04f82359eea9a": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'planning-audit', 'docs/living/PROJECT_STATE.md', '--root', '.', '--strict'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/planning-audit.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:46.591855Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+      "signature": "17e577bbc1b14304f173dc8f552214961c75fd6785919903f0bd57c0cfe89a67",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-6928ea925e6f438e3873543389326106": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"import sys,tempfile,json\\nfrom pathlib import Path\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nimport test_inaturalist_source as fixture\\n\\nclass TimeoutTransport:\\n    def __init__(self): self.calls=0\\n    def get(self,*args,**kwargs):\\n        self.calls+=1\\n        raise r.RecoveryError('timeout')\\n\\nwith tempfile.TemporaryDirectory(prefix='p08-synthetic-resume-') as tmp:\\n    dataset=Path(tmp)/'synthetic'\\n    config=r.default_config(offline=True)\\n    cls=r.canonical()[0]\\n    crosswalk=fixture.crosswalk()\\n    evidence=b'synthetic reviewed crosswalk evidence\\\\n'\\n    crosswalk['taxonomy_ref_ids']=cls['taxonomy_ref_ids']\\n    crosswalk['evidence'].update(path='evidence/crosswalk.json',sha256=r.sha(evidence))\\n    config['crosswalk'][cls['class_id']]=crosswalk\\n    transport=TimeoutTransport()\\n    with patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')),patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')):\\n        with r.Dataset(dataset,config,offline=True) as ds:\\n            r.persist(ds.path('evidence/crosswalk.json'),evidence,immutable=True)\\n            # Real conditional acquisition boundary; only the transport is fake.\\n            status=r.acquire_inat(ds,cls,transport,None)\\n            failure=ds.select('source_failure')[-1]\\n            assert transport.calls==1, 'crosswalk did not reach fake transport'\\n            assert status=='source_blocked'\\n            print(json.dumps({'scenario':'synthetic_inaturalist_timeout','fake_transport_calls':transport.calls,'actual_failure_code':failure['code'],'retryable':failure['code'] in r.RETRYABLE,'expected':'preserve retryable timeout for restart','real_network_calls':0}),flush=True)\\n            assert failure['code'] in r.RETRYABLE, 'approved timeout recovery contract violated: timeout became non-retryable '+failure['code']\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:47:42.806328Z",
+      "cwd": ".",
+      "exit_code": 1,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "signature": "a874b5d9a9ba6c5a874bf486f0cfb1de9e57d9f965c46158bc70932de7122f92",
+      "spawn_error": false,
+      "stderr_sha256": "ab10a09d3c610810df221d06c63fc34c1557a1a4ebec156b478028047f5db92d",
+      "stdout_sha256": "ae8ecbd530374ef2f3f826ae520e6c8f33050d5a0727123a0187ceaa87386539",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-968a10b02132245bb68c901f5153b7c0": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_recover_p08.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/focal-recovery.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:34.435704Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "signature": "ccbf3d7d9831f95fb105f1b8b9d4382a5bab457ad919cb8f98b434918233451c",
+      "spawn_error": false,
+      "stderr_sha256": "029c4ec1246fb13504e289b81b75bd349f1a6e8c05cc94ba472e96842eb2106b",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-96e30effbaad1033d32a3f2bff607ea7": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/codex/P08/final-files.sha256'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/approved-bytes.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:45.189731Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+      "signature": "83789522da0c5613b99e18365492df068d5982d32567e2a44073a318974b0a0c",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "ef02e32536c5020b07b50cc979fe3245ddcf9710b277318f27c10bd5de080af5",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-9e9f28ef0bd6bbb5c496decb3bce6b84": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['git', 'diff', '--check', '7981377a433270c9e2072fcafdf89b690988fa08^', '7981377a433270c9e2072fcafdf89b690988fa08'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/diff-check.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/diff-check.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:47.350328Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+      "signature": "394655e43777b80248adc3067337221413d6378cccccc69d7fd7c6923b57efaa",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-e09dcbc9831234d7c3bf5d1903eeac89": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'validate-state', 'docs/living/PROJECT_STATE.md'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/state.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/state.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:45.619629Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+      "signature": "fc41aa66e57b3d2d64474b889c055d7581a9c625026ac460cc5708396f54304a",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-eb43996df5d8cf4fe2371c278a38aa9d": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'repo-hygiene', 'check', '--repo', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/repo-hygiene.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:47.034159Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+      "signature": "46e89f991049e8ec6e4f9900816ae614bf9885e5f07b1aa064ae09f42af557d7",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    },
+    "proof-f51fb838123d5173f7c7da08d9c1d87f": {
+      "command": [
+        "python3",
+        "-B",
+        "-c",
+        "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', 'scripts/phase1/validate_offline_manifest.py', '--manifest', 'docs/phase1/offline-class-manifest.v1.json', '--roster', 'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/canonical-taxonomy.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
+      ],
+      "commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "created_at": "2026-10-07T22:34:44.600584Z",
+      "cwd": ".",
+      "exit_code": 0,
+      "plan_id": "P08",
+      "planning_version": "v2",
+      "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+      "signature": "c0be870c5d94d8a7264d5e42e1f140cdd4b1cba9ca136d8a5110f3ff1125aa46",
+      "spawn_error": false,
+      "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
+      "stdout_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
+      "timed_out": false,
+      "timeout_seconds": 180.0,
+      "unit_id": "1"
+    }
+  },
+  "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+  "store_version": 1,
+  "unit_id": "1",
+  "updated_at": "2026-10-07T22:47:42.895402Z"
+}
diff --git a/artifacts/bianchini/v2/codex/convergence/P08/1.json b/artifacts/bianchini/v2/codex/convergence/P08/1.json
new file mode 100644
index 0000000..b8c2b46
--- /dev/null
+++ b/artifacts/bianchini/v2/codex/convergence/P08/1.json
@@ -0,0 +1,326 @@
+{
+  "blockers": {
+    "B1": {
+      "approved_requirement": "cumprir integralmente §§1–9 da spec.",
+      "disposition": "blocker",
+      "id": "B1",
+      "material_impact": "Uma falha temporária torna a aquisição permanentemente bloqueada na mesma configuração, violando o contrato de retomada do mecanismo aprovado.",
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "reachable_scenario": "Dataset offline sintético com crosswalk e evidência válidos alcança o transporte fake, que lança timeout. O evento persistido perde a classificação retomável.",
+      "review_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "risk_seam": "p08-source-contract",
+      "root_cause": "acquire_inat substitui timeout por inaturalist_contract_or_evidence, fora de RETRYABLE; acquire ignora a fonte nas invocações seguintes.",
+      "severity": "important",
+      "source": "initial",
+      "status": "open",
+      "structural": false,
+      "structural_class": null,
+      "structural_evidence": null,
+      "title": "Timeout de iNaturalist impede a retomada contratada"
+    }
+  },
+  "created_at": "2026-10-07T22:50:20.012004Z",
+  "decisions": [
+    {
+      "at": "2026-10-07T22:50:39.350539Z",
+      "kind": "local_block",
+      "result": "independent_work_continues",
+      "summary": "User explicitly requires ending closure on gate failure without code/test changes, a second commit or push. B1 remains open; no fix round or terminal transition requested. Only P08 closure is authorized."
+    }
+  ],
+  "deferred_hardening": [],
+  "delta_submissions": 0,
+  "events": [
+    {
+      "action": "review_frozen",
+      "at": "2026-10-07T22:50:20.012073Z",
+      "blockers": [
+        "B1"
+      ],
+      "hardening": 0
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:20.328167Z",
+      "gate": "synthetic-source-contract",
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "status": "failed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:20.716608Z",
+      "gate": "focal-recovery",
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:21.196782Z",
+      "gate": "focal-adapter",
+      "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:21.767313Z",
+      "gate": "canonical-taxonomy",
+      "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:22.422632Z",
+      "gate": "append-only-integrity-idempotence",
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:23.182013Z",
+      "gate": "selective-mutation",
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:24.137196Z",
+      "gate": "affected-history",
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:25.130279Z",
+      "gate": "p07-17-preserved",
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:26.221197Z",
+      "gate": "external-data-integrity",
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:27.416911Z",
+      "gate": "final-human-bytes-acceptance",
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:28.713376Z",
+      "gate": "approved-bytes",
+      "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:30.017383Z",
+      "gate": "historical-checksums",
+      "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:31.398464Z",
+      "gate": "state",
+      "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:32.841139Z",
+      "gate": "planning-snapshot",
+      "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:34.391837Z",
+      "gate": "planning-audit",
+      "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:35.994322Z",
+      "gate": "repo-hygiene",
+      "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+      "status": "passed"
+    },
+    {
+      "action": "gate_recorded",
+      "at": "2026-10-07T22:50:37.662898Z",
+      "gate": "diff-check",
+      "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+      "status": "passed"
+    },
+    {
+      "action": "decision",
+      "at": "2026-10-07T22:50:39.350613Z",
+      "kind": "local_block",
+      "result": "independent_work_continues"
+    },
+    {
+      "action": "phase_transition",
+      "at": "2026-10-07T22:56:27.280222Z",
+      "command": "fix",
+      "source": "review_frozen",
+      "target": "fixing"
+    },
+    {
+      "action": "fix_started",
+      "at": "2026-10-07T22:56:27.280392Z",
+      "blockers": [
+        "B1"
+      ],
+      "round": 1,
+      "summary": "Authorized first B1 fix: preserve existing transient RecoveryError codes in acquire_inat; add synthetic restart regression; stop before staging/commit/push for grouped acceptance of new bytes."
+    }
+  ],
+  "fix_rounds": 1,
+  "gates": {
+    "affected-history": {
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "recorded_at": "2026-10-07T22:50:24.137120Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "append-only-integrity-idempotence": {
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "recorded_at": "2026-10-07T22:50:22.422590Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "approved-bytes": {
+      "proof_id": "proof-96e30effbaad1033d32a3f2bff607ea7",
+      "recorded_at": "2026-10-07T22:50:28.713298Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "canonical-taxonomy": {
+      "proof_id": "proof-f51fb838123d5173f7c7da08d9c1d87f",
+      "recorded_at": "2026-10-07T22:50:21.767168Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "diff-check": {
+      "proof_id": "proof-9e9f28ef0bd6bbb5c496decb3bce6b84",
+      "recorded_at": "2026-10-07T22:50:37.662852Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "external-data-integrity": {
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "recorded_at": "2026-10-07T22:50:26.221150Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "final-human-bytes-acceptance": {
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "recorded_at": "2026-10-07T22:50:27.416857Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "focal-adapter": {
+      "proof_id": "proof-20c948a7c09b3cd0de5e999267bf1cd1",
+      "recorded_at": "2026-10-07T22:50:21.196738Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "focal-recovery": {
+      "proof_id": "proof-968a10b02132245bb68c901f5153b7c0",
+      "recorded_at": "2026-10-07T22:50:20.716570Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "historical-checksums": {
+      "proof_id": "proof-034132282be7abb6b24447b178256ca0",
+      "recorded_at": "2026-10-07T22:50:30.017327Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "p07-17-preserved": {
+      "proof_id": "proof-103d80e98b7ad5ab26a325e7645dc5e9",
+      "recorded_at": "2026-10-07T22:50:25.130229Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "planning-audit": {
+      "proof_id": "proof-4745dbc8b82d4bebede04f82359eea9a",
+      "recorded_at": "2026-10-07T22:50:34.391804Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "planning-snapshot": {
+      "proof_id": "proof-28272ad7fd0c858844fb8e2306c628e4",
+      "recorded_at": "2026-10-07T22:50:32.841102Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "repo-hygiene": {
+      "proof_id": "proof-eb43996df5d8cf4fe2371c278a38aa9d",
+      "recorded_at": "2026-10-07T22:50:35.994266Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "selective-mutation": {
+      "proof_id": "proof-23228b63703e5fb20da4c1b69fa9c73b",
+      "recorded_at": "2026-10-07T22:50:23.181982Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "state": {
+      "proof_id": "proof-e09dcbc9831234d7c3bf5d1903eeac89",
+      "recorded_at": "2026-10-07T22:50:31.398405Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "passed"
+    },
+    "synthetic-source-contract": {
+      "proof_id": "proof-6928ea925e6f438e3873543389326106",
+      "recorded_at": "2026-10-07T22:50:20.328100Z",
+      "revision": "7981377a433270c9e2072fcafdf89b690988fa08",
+      "status": "failed"
+    }
+  },
+  "last_review_head": "7981377a433270c9e2072fcafdf89b690988fa08",
+  "pending_delta": null,
+  "phase": "fixing",
+  "plan_id": "P08",
+  "planning_version": "v2",
+  "redesign_count": 0,
+  "repository_root": "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08",
+  "required_gates": [
+    "synthetic-source-contract",
+    "focal-recovery",
+    "focal-adapter",
+    "canonical-taxonomy",
+    "append-only-integrity-idempotence",
+    "selective-mutation",
+    "affected-history",
+    "p07-17-preserved",
+    "external-data-integrity",
+    "final-human-bytes-acceptance",
+    "approved-bytes",
+    "historical-checksums",
+    "state",
+    "planning-snapshot",
+    "planning-audit",
+    "repo-hygiene",
+    "diff-check",
+    "human-botanical-privacy-review",
+    "git-secrets-private-data-images-inspection"
+  ],
+  "schema_version": 2,
+  "seam": "p08-source-contract",
+  "task_brief": "artifacts/bianchini/v2/codex/P08/task-brief.md",
+  "task_brief_digest": "a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36",
+  "unit_digest": "33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af",
+  "unit_id": "1",
+  "unit_identity": "2638b0c17436a9e732e54818b20e092e594ffa983a29df86b7c6b355a593404a",
+  "unit_identity_source": "task_brief",
+  "updated_at": "2026-10-07T22:56:27.280394Z"
+}
diff --git a/artifacts/bianchini/v2/ledgers/P08.md b/artifacts/bianchini/v2/ledgers/P08.md
index cd17c62..2e4e353 100644
--- a/artifacts/bianchini/v2/ledgers/P08.md
+++ b/artifacts/bianchini/v2/ledgers/P08.md
@@ -13,10 +13,33 @@
 - Owner prohibition on commits prevents commit-bound guard proofs from representing the new working bytes. Formal convergence review/gates are not claimed; do not freeze/complete a sidecar for baseline code as if it included this implementation. Working-byte review and evidence are separately fingerprinted. No fake proof_id.
 - Independent technical review is in progress on working bytes. No completed/stopped terminal state has been created. Method state stays unchanged pending final human acceptance.
 - Current step: strengthen transport/resumption/authority tests before bounded real collection. No external P08 directory or collection at this checkpoint.
 
 - Continuation recovered the exact checkpoint digest and eleven untracked files; existing workspace reused, baseline HEAD unchanged, no upstream.
 - Final continuation evidence: artifacts/bianchini/v2/codex/P08/continuation-report.md and verification-final.json. 51 recovery + 15 adapter focal tests; 233 full historical/affected tests; five selective mutations killed, zero survivors.
 - Real Commons round: 120 successful metadata requests, 1090 class associations/1088 unique candidates, all pending, no media transfer. iNaturalist no_crosswalk, zero requests. P07 17/17 bytes and mtimes preserved.
 - Bounded amendment: deterministic review HTML after journal reload; exact predecessor fingerprint transition journaled, original config and journal prefix unchanged. Real replay stable after correction.
 - External final-manifest SHA256 334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716; 138 files with verified private backup. Human decisions/U-804 acceptance pending; usable=0/training blocked.
 - Guard cannot prove new uncommitted bytes without a forbidden commit/new proof worktree. No fake sidecar/proofs/completion. No staging/commit/push. Single grouped final human decision requested by owner remains pending.
+
+## Closure recovery — 2026-10-07
+
+- Same branch recovered through Git prune (only obsolete registration) and Method workspace create/resume into persistent `.worktrees/ScanPlant/p08`; HEAD `7981377a433270c9e2072fcafdf89b690988fa08`, parent `24de252d27a137281c02cad50533280bb82dd80d`; one own commit.
+- No prior P08 sidecar/proof store recovered from surviving official worktrees/Git; common proof signing key exists, contents not exposed. Uncommitted evidence formerly in lost checkout is unavailable; committed historical logs are preserved but are not current guard proofs.
+- All approved implementation bytes/receipt and both external manifests verified. Historical checkpoint digests remain immutable; new recovery records are separate.
+- 51 recovery, 15 adapter, 233 affected/history tests passed; five selective mutants killed. External 138-file datasets, 29 historical source files, 17 images and seven P07 receipts match; read-only replay preserves bytes/mtimes.
+- Independent review reproduced B1 using `proof-6928ea925e6f438e3873543389326106`: transient iNaturalist timeout loses retry classification. Guard sidecar: `artifacts/bianchini/v2/codex/convergence/P08/1.json`; see closure/guard-status.json and independent-review.json.
+- Owner mandates halt on failure: no fixes, no second commit, no staging/push. Remaining final Git private-data inspection and candidate human review are not claimed passed. Evidence/state changes remain uncommitted for inspection.
+- 1088 candidates pending; zero transfer/approved/usable. Real iNaturalist no_crosswalk; rights/botanical/privacy authority remains pending. Training unauthorized, release pending, P09 not started.
+
+
+## B1 round 1 resumed — technical review and acceptance package
+
+- Current owner instruction supersedes the earlier closure-only prohibition for B1 work only; staging, commit and push remain prohibited. This entry is the current continuation authority; earlier state/checkpoint next_action prose describes the historical halt.
+- Method 3.2.0 / v2-standalone / strict: workspace resume/check, route, state, approved snapshot, strict planning audit and hygiene passed. Original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 and branch bm/v2-p08 preserved; index empty.
+- Existing two-line production delta preserves only existing transient RecoveryError codes in acquire_inat. RETRYABLE unchanged. Three existing synthetic restart tests preserved unchanged. All prior recovery documents preserved; this ledger is append-only.
+- Historical RED proof-6928ea925e6f438e3873543389326106 is defect evidence on the original SHA only. Additional RED and GREEN fingerprints reconciled; reused 3 new / 54 P08 / 15 adapter / 236 affected tests and five killed selective mutations. No suite rerun during resumption.
+- Independent reviewer p08_b1_independent_review returned no findings on the current technical delta. Full evidence and review: artifacts/bianchini/v2/codex/P08/fix-B1/. This is not a formal guard review or a proof on a future commit.
+- Sidecar reference: artifacts/bianchini/v2/codex/convergence/P08/1.json. No second fix transition, submit-delta, review, gate, complete or stopped transition performed during resumption; no new round, redesign or P09.
+- Read-only hashes and mtimes of all 319 external files (including operational locks) remain identical. Dataset/backup intact; 1088 pending, zero transfer/approved_for_dataset/usable; real iNaturalist no_crosswalk; training unauthorized; release pending.
+- Git inspection distinguishes synthetic fixtures and preserved historical records from real private data. Full private external filename/mtime baseline and guard operational backups/lock remain local-only, preserved. Proposed exact paths: fix-B1/commit-inventory.txt; payload manifest: fix-B1/acceptance-manifest.sha256; digest: fix-B1/acceptance-digest.txt. Neither manifest nor digest includes itself in the payload hash set.
+- Next authorized boundary: one human decision on the new bytes. Subsequent own commit, exact-SHA proofs, submit-delta and guard review/gates/closure require that decision and appropriate separate Git authorization. P08 is not completed; original human receipt is immutable and does not accept this fix.
diff --git a/docs/living/PROJECT_STATE.md b/docs/living/PROJECT_STATE.md
index 2fd4686..87c5250 100644
--- a/docs/living/PROJECT_STATE.md
+++ b/docs/living/PROJECT_STATE.md
@@ -279,21 +279,21 @@
         "source-hash-reconciliation",
         "synthetic-curation-tests",
         "human-17-decisions",
         "idempotence-and-sanitization",
         "final-human-acceptance"
       ]
     },
     {
       "id": "P08",
       "path": "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md",
-      "status": "approved",
+      "status": "blocked",
       "risk": "high",
       "execution": "strict",
       "review": "per_task",
       "test_seams": [
         "p08-source-contract",
         "p08-taxonomic-map",
         "p08-journal-integrity",
         "p08-sanitization",
         "p08-human-approval"
       ],
@@ -311,32 +311,32 @@
         "final-human-bytes-acceptance"
       ]
     }
   ],
   "verification": {
     "fast": {
       "commands": [
         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_recover_p08.py'",
         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_inaturalist_source.py'"
       ],
-      "status": "pending",
-      "scope": "P08 futuro; arquivos entregáveis, não implementados neste planejamento."
+      "status": "passed",
+      "scope": "P08 implementation 7981377: 51 recovery and 15 adapter tests passed; proofs in artifacts/bianchini/v2/codex/P08/closure/proof-results.json."
     },
     "plan": {
       "commands": [
         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'",
         "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
         "sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
         "git diff --check"
       ],
-      "status": "pending",
-      "scope": "P08 futuro; suite inclui cinco mutações stdlib aprovadas no planejamento; requer gates de dados/revisão/recibo externo. Não autoriza treino/release."
+      "status": "failed",
+      "scope": "P08: 233 historical/affected tests and five selective mutations passed, but independent review reproduced non-retryable iNaturalist timeout. Proof proof-6928ea925e6f438e3873543389326106 failed; closure and publication blocked. No code/test change authorized."
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
@@ -387,23 +387,28 @@
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
+    },
+    {
+      "id": "B-P08-INAT-TIMEOUT-RESUMPTION",
+      "summary": "Synthetic iNaturalist timeout is persisted as inaturalist_contract_or_evidence and cannot resume. Closure halted on gate failure as explicitly instructed; implementation and human receipt preserved.",
+      "evidence": "artifacts/bianchini/v2/codex/P08/closure/independent-review.json"
     }
   ],
-  "next_action": "Aguardar autorização posterior de execução P08 sobre o plano publicado. Pacote/digest P08 integralmente aprovado; esta rodada autoriza somente registro, staging, commit e push do planejamento. P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed; guard completed sem blockers; usable=0 até decisões humanas válidas; P06/P07 fechados e imutáveis; release pending; active_execution null; treinamento não autorizado; P09 não iniciado.",
+  "next_action": "P08 closure blocked by synthetic iNaturalist timeout resumption proof-6928ea925e6f438e3873543389326106. Await separate instruction for any code/test change. No second commit or push. 1088 candidates pending; zero transfers, approved_for_dataset=0, usable=0; real iNaturalist no_crosswalk. Training unauthorized; release pending; P09 not started.",
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
diff --git a/scripts/phase1/recover_p08.py b/scripts/phase1/recover_p08.py
index 3def6c1..3e74f9b 100644
--- a/scripts/phase1/recover_p08.py
+++ b/scripts/phase1/recover_p08.py
@@ -549,21 +549,22 @@ def acquire_inat(ds,cls,transport,fixture):
                             taxonomic_confidence=initial['taxonomic_confidence'])
                 records.append(item)
             page=ds.save_page('inaturalist',cid,0,records,None)
             ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
                                       'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
         for c in page['candidates']:
             ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
         ds.advance(page)
         return 'budget_reached'
     except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
-        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':'inaturalist_contract_or_evidence'})
+        code=str(error) if isinstance(error,RecoveryError) and str(error) in RETRYABLE else 'inaturalist_contract_or_evidence'
+        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':code})
         return 'source_blocked'
 
 
 def acquire(ds,fixture=None):
     transport=Transport(ds)
     if fixture is not None:require(ds.offline,'fixture_mode')
     elif ds.offline:raise RecoveryError('fixture_required')
     for cls in canonical():
         for source in SOURCES:
             cid=cls['class_id']
diff --git a/scripts/phase1/test_recover_p08.py b/scripts/phase1/test_recover_p08.py
index aeb8b53..383cb8a 100644
--- a/scripts/phase1/test_recover_p08.py
+++ b/scripts/phase1/test_recover_p08.py
@@ -499,20 +499,124 @@ class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
             kinds = [event['type'] for event in ds.events]
             self.assertLess(kinds.index('page'), kinds.index('intention'))
             self.assertLess(kinds.index('committed'), kinds.index('cursor'))
         before = r.tree_fingerprint(self.root)
         (media/'123').unlink()  # A repeated execution must use the durable objects.
         process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
         self.assertEqual(process.returncode, 0, process.stderr)
         self.assertEqual(before, r.tree_fingerprint(self.root))
 
 
+class InaturalistResumeTests(DatasetCase, unittest.TestCase):
+    def prepare_round(self, request_cap=4):
+        from test_inaturalist_source import crosswalk, observation, page
+        cls = r.canonical()[0]
+        entry = crosswalk()
+        evidence = b'synthetic reviewed crosswalk evidence\n'
+        entry['taxonomy_ref_ids'] = cls['taxonomy_ref_ids']
+        entry['evidence'].update(path='evidence/crosswalk.json', sha256=r.sha(evidence))
+        self.config['crosswalk'][cls['class_id']] = entry
+        self.config['limits']['requests'] = request_cap
+        with self.open() as ds:
+            r.persist(ds.path(entry['evidence']['path']), evidence, immutable=True)
+            # Commons is already accounted for; exercise only the iNaturalist seam.
+            for item in r.canonical():
+                ds.append('source_status', {'source': 'commons', 'class_id': item['class_id'],
+                          'status': 'exhausted_within_query' if item['kind'] == 'species' else 'protection_not_queried'})
+        return cls, r.encode(page(observation()))
+
+    def test_timeout_then_restart_preserves_journal_limits_and_candidates(self):
+        cls, response = self.prepare_round()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertEqual([x['code'] for x in ds.select('response')], ['timeout'] * 3)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertEqual(ds.records(), [])
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [FakeResponse(body=response)])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(len(ds.select('request')), self.config['limits']['requests'])
+            self.assertEqual(len(ds.select('response')), 4)
+            self.assertEqual(len({x['request_id'] for x in ds.select('request')}), 4)
+            self.assertEqual(len(ds.select('page')), 1)
+            self.assertEqual(len(ds.select('cursor')), 1)
+            self.assertEqual(len(ds.records()), 1)
+            self.assertEqual(ds.records()[0]['state'], 'needs_license_review')
+            self.assertEqual(ds.records()[0]['class_ids'], [cls['class_id']])
+            self.assertEqual(ds.select('intention'), [])
+            self.assertEqual(ds.select('committed'), [])
+            kinds = [e['type'] for e in ds.events]
+            self.assertLess(kinds.index('evidence'), kinds.index('page'))
+            self.assertLess(kinds.index('page'), kinds.index('classified'))
+            self.assertLess(kinds.index('classified'), kinds.index('cursor'))
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            self.assertEqual(ds.config['limits'], self.config['limits'])
+            self.assertEqual(ds.summary()['usable'], 0)
+        stable = r.tree_fingerprint(self.root)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+    def test_only_existing_transient_recovery_codes_allow_restart(self):
+        cls, _ = self.prepare_round()
+        errors = [(r.RecoveryError(code), code) for code in sorted(r.RETRYABLE)]
+        errors += [(r.RecoveryError(code), 'inaturalist_contract_or_evidence') for code in
+                   ['http_403', 'http_404', 'request_budget', 'crosswalk_evidence_hash', 'invalid_json', 'unsafe_url']]
+        errors += [(r.inat.ContractError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (OSError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (KeyError('timeout'), 'inaturalist_contract_or_evidence')]
+        with self.open() as ds:
+            for error, expected in errors:
+                with self.subTest(error=type(error).__name__, code=str(error)):
+                    with patch.object(r.Transport, 'get', side_effect=error) as get:
+                        self.assertEqual(r.acquire_inat(ds, cls, r.Transport(ds), None), 'source_blocked')
+                    self.assertEqual(get.call_count, 1)
+                    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+
+    def test_timeout_restart_does_not_reset_request_budget(self):
+        self.prepare_round(request_cap=3)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertNotIn(ds.select('source_failure')[-1]['code'], r.RETRYABLE)
+            self.assertEqual(ds.records(), [])
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            stable = r.tree_fingerprint(self.root)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+
 class ContinuationProofs(DatasetCase, unittest.TestCase):
     def test_inspect_html_identical_after_journal_reload(self):
         with self.open() as ds:
             ds.ingest(candidate(),lambda _:image_bytes())
             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
         before=r.tree_fingerprint(self.root)
         with self.open() as ds:
             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
         self.assertEqual(before,r.tree_fingerprint(self.root))
```

## Formal round 1 evidence

# P08 B1 formal implementer report

Correction committed exactly as accepted: dd595a6d652c27773849003b0fc2c0ec1d8d3ad4. Round 1 preserved. All gates executed on this SHA; human-botanical-privacy-review is blocked by absent per-item human opinions, independent from B1. Current acceptance explicitly does not supply candidate decisions. No dataset mutations or network. No completed claim.

Signed proof references:
- synthetic-source-contract: proof-3f1d97fec3f4815a6b61620c9825b2f8 (exit 0)
- focal-recovery: proof-1dec31cb030080a9e8fb9712ccf80e46 (exit 0)
- focal-adapter: proof-612ed1f00914339f42d7bb1ee8be302d (exit 0)
- affected-history: proof-8fe94629a707b3a3313a29d3a162c75b (exit 0)
- append-only-integrity-idempotence: proof-1dec31cb030080a9e8fb9712ccf80e46 (exit 0)
- selective-mutation: proof-8fe94629a707b3a3313a29d3a162c75b (exit 0)
- canonical-taxonomy: proof-77592a622d7c1eb8610c130bd75e1c5b (exit 0)
- historical-checksums: proof-008a3bebb227efe8c8ebb9b5d6e19384 (exit 0)
- state: proof-d0c5e8677b3368318cd81f7a0adfc823 (exit 0)
- planning-snapshot: proof-bdeebda09b843ecb5bcdf9b38a30cf24 (exit 0)
- planning-audit: proof-ce83c05119aad31f9d7f901241b2a02d (exit 0)
- repo-hygiene: proof-7c42672bfe3882f5fdbb23def69fd525 (exit 0)
- diff-check: proof-22d26238553be61b4d48850473e44231 (exit 0)
- external-data-integrity: proof-ed42297912a84f72c6e20df34f39d52c (exit 0)
- p07-17-preserved: proof-ed42297912a84f72c6e20df34f39d52c (exit 0)
- approved-bytes: proof-9990999bf24ec29f22691c07fb773ee4 (exit 0)
- final-human-bytes-acceptance: proof-5677a9d814e6faef015142a599db3307 (exit 0)
- human-botanical-privacy-review: proof-2f87449a54b378d54f97243c6d1e5470 (exit 1)
- git-secrets-private-data-images-inspection: proof-04b1a3f781cfb488ecd2e43cd1232664 (exit 0)

The reviewer must resolve only frozen B1 and check regressions of the submitted delta. For B1 use source=frozen, resolution=resolved, proof_id=proof-3f1d97fec3f4815a6b61620c9825b2f8. Keep the frozen approved_requirement; this proof ran the exact RED argv/cwd on the new SHA. Human review gate is independent and remains failed; do not invent candidate acceptance or mark plan completed.

```json
{
  "synthetic-source-contract": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"import sys,tempfile,json\\nfrom pathlib import Path\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nimport test_inaturalist_source as fixture\\n\\nclass TimeoutTransport:\\n    def __init__(self): self.calls=0\\n    def get(self,*args,**kwargs):\\n        self.calls+=1\\n        raise r.RecoveryError('timeout')\\n\\nwith tempfile.TemporaryDirectory(prefix='p08-synthetic-resume-') as tmp:\\n    dataset=Path(tmp)/'synthetic'\\n    config=r.default_config(offline=True)\\n    cls=r.canonical()[0]\\n    crosswalk=fixture.crosswalk()\\n    evidence=b'synthetic reviewed crosswalk evidence\\\\n'\\n    crosswalk['taxonomy_ref_ids']=cls['taxonomy_ref_ids']\\n    crosswalk['evidence'].update(path='evidence/crosswalk.json',sha256=r.sha(evidence))\\n    config['crosswalk'][cls['class_id']]=crosswalk\\n    transport=TimeoutTransport()\\n    with patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')),patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')):\\n        with r.Dataset(dataset,config,offline=True) as ds:\\n            r.persist(ds.path('evidence/crosswalk.json'),evidence,immutable=True)\\n            # Real conditional acquisition boundary; only the transport is fake.\\n            status=r.acquire_inat(ds,cls,transport,None)\\n            failure=ds.select('source_failure')[-1]\\n            assert transport.calls==1, 'crosswalk did not reach fake transport'\\n            assert status=='source_blocked'\\n            print(json.dumps({'scenario':'synthetic_inaturalist_timeout','fake_transport_calls':transport.calls,'actual_failure_code':failure['code'],'retryable':failure['code'] in r.RETRYABLE,'expected':'preserve retryable timeout for restart','real_network_calls':0}),flush=True)\\n            assert failure['code'] in r.RETRYABLE, 'approved timeout recovery contract violated: timeout became non-retryable '+failure['code']\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/closure/inaturalist-timeout-resumption.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:35.822861Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-3f1d97fec3f4815a6b61620c9825b2f8",
    "signature": "18d34d3607b3f050c0bd84ae7d099c2e81044d50bd1fa37094754113a702e92d",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "58231e42db05efe62bdf6e3950595693f437c06203c3d0ecfb911f736e8a827d",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "focal-recovery": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_recover_p08.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-recovery.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-recovery.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:38.129100Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-1dec31cb030080a9e8fb9712ccf80e46",
    "signature": "c9b09b7d9d3262efdff889f1da9a08a4f21c972d9552747950ffdc8d2e5606c1",
    "spawn_error": false,
    "stderr_sha256": "cc28c7cf8d28dcb6d526105a3a25017aed400dbf6c1c9b528305416d0cf7fcdc",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "focal-adapter": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_inaturalist_source.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-adapter.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-adapter.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:38.484247Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-612ed1f00914339f42d7bb1ee8be302d",
    "signature": "00b955d063559cf65d9bd7eab629ed24c1f4f09bf8663f245dfa3ef3bddead1d",
    "spawn_error": false,
    "stderr_sha256": "975e0425226508b074cb5b4fb8ecbac30d3972e91ff2267af8c7849169c920bb",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "affected-history": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/affected-history.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/affected-history.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:46.024977Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-8fe94629a707b3a3313a29d3a162c75b",
    "signature": "df1c31d36329dcf6703f92efb02830ff8671ffe48b3bba5e3c41847a644d2d3f",
    "spawn_error": false,
    "stderr_sha256": "e140136152fe9991cc71630abc6262790f4713cdada70ff2a700b8260677b017",
    "stdout_sha256": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "append-only-integrity-idempotence": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_recover_p08.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-recovery.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/focal-recovery.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:38.129100Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-1dec31cb030080a9e8fb9712ccf80e46",
    "signature": "c9b09b7d9d3262efdff889f1da9a08a4f21c972d9552747950ffdc8d2e5606c1",
    "spawn_error": false,
    "stderr_sha256": "cc28c7cf8d28dcb6d526105a3a25017aed400dbf6c1c9b528305416d0cf7fcdc",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "selective-mutation": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/affected-history.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/affected-history.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:46.024977Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-8fe94629a707b3a3313a29d3a162c75b",
    "signature": "df1c31d36329dcf6703f92efb02830ff8671ffe48b3bba5e3c41847a644d2d3f",
    "spawn_error": false,
    "stderr_sha256": "e140136152fe9991cc71630abc6262790f4713cdada70ff2a700b8260677b017",
    "stdout_sha256": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "canonical-taxonomy": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', 'scripts/phase1/validate_offline_manifest.py', '--manifest', 'docs/phase1/offline-class-manifest.v1.json', '--roster', 'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/canonical-taxonomy.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/canonical-taxonomy.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:46.369014Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-77592a622d7c1eb8610c130bd75e1c5b",
    "signature": "898b8291b607a6960ac1e6077e90fd53fc6f247116f3e6f3b75740974736dadb",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "0135f3b559acb1e6545a636f6f1586b860ac3286045bd0d4263bc07e1546effe",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "historical-checksums": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/historical-checksums.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/historical-checksums.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:46.666532Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-008a3bebb227efe8c8ebb9b5d6e19384",
    "signature": "75085c2896d758aa3ce4a6dc93f5ed07060c16b2b9bc095bae257d8d83a6fa99",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "850eb6347414314de985f34579f94e20801c463bda4e093fd30bee11ed38d7f3",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "state": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'validate-state', 'docs/living/PROJECT_STATE.md'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/state.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/state.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:47.082915Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-d0c5e8677b3368318cd81f7a0adfc823",
    "signature": "e94a3185a72cd827c7c64680c2bb7ab9141b90990eb932e53e1098e029c91f3a",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "83b81ece329d9fb0283ec9e89153c65da3f940e5322cfeaf65862371010ee4d4",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "planning-snapshot": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'snapshot', 'verify', 'docs/living/PROJECT_STATE.md', '--root', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/planning-snapshot.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/planning-snapshot.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:47.543307Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-bdeebda09b843ecb5bcdf9b38a30cf24",
    "signature": "c6a0b994c6ad93339ce08e97c21aa74cdc2ddc65b380aba94ecb08f1f01161f9",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "86f0a9af8d5ea02ee78762c4aae38a6b1612e2c54cfafa58f48ff3b8ad3d6b5a",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "planning-audit": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'planning-audit', 'docs/living/PROJECT_STATE.md', '--root', '.', '--strict'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/planning-audit.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/planning-audit.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:47.997751Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-ce83c05119aad31f9d7f901241b2a02d",
    "signature": "97167445f5c319c35ccd2b60c0df7d4f43864175c414ca00f6c01dd56bb48605",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "b9b6d24017c48572e03ae7057009cfbc2415dc7e93442c5f66a0848f1b22de2a",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "repo-hygiene": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['python3', '-B', '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py', 'repo-hygiene', 'check', '--repo', '.'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/repo-hygiene.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/repo-hygiene.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:48.418367Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-7c42672bfe3882f5fdbb23def69fd525",
    "signature": "5f7f3b274d2dff0e7db2e48eff7f050e6327c4003501231117ba6212a69c7396",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "d6509374bd6914de255bb69aca7af20829fdaef483def9f33bbf7d1dd475ad2e",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "diff-check": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['git', 'diff', '--check'],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/diff-check.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/diff-check.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:48.802753Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-22d26238553be61b4d48850473e44231",
    "signature": "750edc3657d6fff05e18866029e7fa31386420728f3f2e85c0b28836a09078f5",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "external-data-integrity": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport sys,json,hashlib,stat,fcntl,subprocess,re\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nroot=Path.cwd();base=Path('/home/administradorarthur/datasets/scanplant');data=base/'p08-recovery-20261005';backup=base/'p08-recovery-20261005-backup';source=base/'p06-recovery-20260928'\\nreceipt=json.loads((root/'artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_bytes())\\nassert receipt['decision']=='accepted' and receipt['authority']=='human' and receipt['scope']=='technical_and_documentary_bytes_only'\\nassert receipt['approved_git_delivery_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/final-files.sha256')\\nassert receipt['approved_checkpoint_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json')\\nassert receipt['baseline']=='24de252d27a137281c02cad50533280bb82dd80d'\\nassert receipt['counts']==dict(candidates_pending=1088,transferred=0,p08_images=0,approved_for_dataset=0,usable=0)\\nassert receipt['zero_transfer_result_accepted'] is True and receipt['U-803']=='candidate_opinions_pending'\\nfor k in ['candidate_approval','download_authorized','authorship_confirmation','rights_approval','botanical_confirmation','privacy_approval','duplicate_decisions_conclusive','training_authorized','partition_authorized','p09_started']:assert receipt[k] is False,k\\nassert receipt['release']=='pending'\\nbefore={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nmanifest=json.loads((data/'final-manifest.json').read_bytes())\\nfor folder in [data,backup]:\\n assert h(folder/'final-manifest.json')==receipt['approved_external_manifest_sha256']=='334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716'\\n actual={str(p.relative_to(folder)):h(p) for p in folder.rglob('*') if p.is_file() and p.name not in ['.lock','final-manifest.json']}\\n assert actual==manifest['files'] and len(actual)==137\\n assert stat.S_IMODE(folder.stat().st_mode)==0o700\\n for p in folder.rglob('*'):\\n  assert not p.is_symlink()\\n  assert stat.S_IMODE(p.stat().st_mode)==(0o700 if p.is_dir() else 0o600)\\n  assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif'}\\nassert (data/'.lock').read_bytes()==b''\\nconfig=r.load(r.read(data/'config.json'));assert r.sha(r.encode(config))==manifest['config_sha256']\\noriginal_runtime={name:hashlib.sha256(subprocess.check_output(['git','show','7981377a433270c9e2072fcafdf89b690988fa08'+':scripts/phase1/'+name])).hexdigest() for name in r.fingerprint()}\\nassert manifest['runtime_code_sha256']==original_runtime\\nassert {k for k,v in r.fingerprint().items() if v!=original_runtime[k]}=={'recover_p08.py'}\\nassert manifest['code_sha256']==config['code_sha256']\\nassert config['code_sha256']['recover_p08.py']==r.HTML_ORDER_PREDECESSOR\\nwith (data/'.lock').open('rb') as lock,patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')),patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')):\\n fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)\\n ds=r.Dataset(data,config);ds.replay();ds.verify_objects()\\n assert ds.events[0]['data']==config\\n assert {'from':config['code_sha256'],'to':original_runtime,'reason':'deterministic_review_html_key_order'} in ds.select('code_compatibility')\\n assert r.verify(ds,source)==0\\n hashes,images=r.historical(source);assert len(hashes)==29 and len(images)==17\\n records=ds.records();summary=ds.summary()\\n assert len(records)==1088 and summary==r.load(r.read(data/'summary.json'))==r.load(r.read(root/'artifacts/phase1/p08/summary.json'))\\n assert summary['usable']==0 and summary['training_authorized'] is False and summary['partition_authorized'] is False\\n assert all(x['state']!='approved_for_dataset' and not x.get('original_sha256') and not x.get('sanitized_sha256') for x in records)\\n assert len(ds.select('page'))==len(ds.select('cursor'))==120 and not ds.select('committed') and not ds.select('received') and not ds.select('source_failure')\\n assert all(x['status']=='no_crosswalk' for x in summary['coverage'] if x['source']=='inaturalist' and x['class_id'].startswith('species_'))\\n assert len(summary['coverage'])==28 and all(x['transferred']==x['approved']==0 for x in summary['coverage'])\\n review=r.load(r.read(data/'human-review.json'));objects=r.load(r.read(data/'object-hashes.json'));decisions=r.load(r.read(data/'decisions.template.json'))\\n assert len(review['candidates'])==len(objects)==len(decisions['decisions'])==1088\\n assert {x['candidate_id'] for x in review['candidates']}=={x['candidate_id'] for x in records}=={x['candidate_id'] for x in decisions['decisions']}\\n assert all(x['reviewer'] is None and x['expert_confirmation'] is False for x in decisions['decisions'])\\n assert r.read(data/'Attributions.jsonl')==b''\\n assert len(ds.select('request'))==120\\n for n in ['historical-before.json','historical-before-after.json']:\\n  historical=r.load(r.read(data/n));assert len(historical)==17\\n # Replay and verification are read-only: no acquisition/inspection/finalization invocation.\\n ds2=r.Dataset(data,config);ds2.replay();assert ds2.events==ds.events and ds2.summary()==summary\\nassert before=={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nprint(json.dumps({'result':'passed','external_files_each':138,'manifest_sha256':receipt['approved_external_manifest_sha256'],'historical_files':29,'historical_images':17,'p07_receipt_hashes':7,'candidates_pending':1088,'transferred':0,'approved_for_dataset':0,'usable':0,'read_only_replay_bytes_and_mtimes_unchanged':True,'acceptance':'technical_bytes_only','candidate_review':'pending','inat':'no_crosswalk','training_authorized':False,'release':'pending','p09_started':False},sort_keys=True))\\n\\noriginal_before=json.loads(Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json').read_text())\\nassert {p.name:r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}==original_before\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/external-data-integrity.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/external-data-integrity.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:53.522403Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-ed42297912a84f72c6e20df34f39d52c",
    "signature": "8e6c6632019402fe47a31926a449cbff57acb0072757dc01fb81cd44dd4ad9d0",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "p07-17-preserved": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport sys,json,hashlib,stat,fcntl,subprocess,re\\nfrom unittest.mock import patch\\nsys.path.insert(0,str(Path.cwd()/'scripts/phase1'))\\nimport recover_p08 as r\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nroot=Path.cwd();base=Path('/home/administradorarthur/datasets/scanplant');data=base/'p08-recovery-20261005';backup=base/'p08-recovery-20261005-backup';source=base/'p06-recovery-20260928'\\nreceipt=json.loads((root/'artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_bytes())\\nassert receipt['decision']=='accepted' and receipt['authority']=='human' and receipt['scope']=='technical_and_documentary_bytes_only'\\nassert receipt['approved_git_delivery_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/final-files.sha256')\\nassert receipt['approved_checkpoint_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json')\\nassert receipt['baseline']=='24de252d27a137281c02cad50533280bb82dd80d'\\nassert receipt['counts']==dict(candidates_pending=1088,transferred=0,p08_images=0,approved_for_dataset=0,usable=0)\\nassert receipt['zero_transfer_result_accepted'] is True and receipt['U-803']=='candidate_opinions_pending'\\nfor k in ['candidate_approval','download_authorized','authorship_confirmation','rights_approval','botanical_confirmation','privacy_approval','duplicate_decisions_conclusive','training_authorized','partition_authorized','p09_started']:assert receipt[k] is False,k\\nassert receipt['release']=='pending'\\nbefore={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nmanifest=json.loads((data/'final-manifest.json').read_bytes())\\nfor folder in [data,backup]:\\n assert h(folder/'final-manifest.json')==receipt['approved_external_manifest_sha256']=='334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716'\\n actual={str(p.relative_to(folder)):h(p) for p in folder.rglob('*') if p.is_file() and p.name not in ['.lock','final-manifest.json']}\\n assert actual==manifest['files'] and len(actual)==137\\n assert stat.S_IMODE(folder.stat().st_mode)==0o700\\n for p in folder.rglob('*'):\\n  assert not p.is_symlink()\\n  assert stat.S_IMODE(p.stat().st_mode)==(0o700 if p.is_dir() else 0o600)\\n  assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif'}\\nassert (data/'.lock').read_bytes()==b''\\nconfig=r.load(r.read(data/'config.json'));assert r.sha(r.encode(config))==manifest['config_sha256']\\noriginal_runtime={name:hashlib.sha256(subprocess.check_output(['git','show','7981377a433270c9e2072fcafdf89b690988fa08'+':scripts/phase1/'+name])).hexdigest() for name in r.fingerprint()}\\nassert manifest['runtime_code_sha256']==original_runtime\\nassert {k for k,v in r.fingerprint().items() if v!=original_runtime[k]}=={'recover_p08.py'}\\nassert manifest['code_sha256']==config['code_sha256']\\nassert config['code_sha256']['recover_p08.py']==r.HTML_ORDER_PREDECESSOR\\nwith (data/'.lock').open('rb') as lock,patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')),patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')):\\n fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)\\n ds=r.Dataset(data,config);ds.replay();ds.verify_objects()\\n assert ds.events[0]['data']==config\\n assert {'from':config['code_sha256'],'to':original_runtime,'reason':'deterministic_review_html_key_order'} in ds.select('code_compatibility')\\n assert r.verify(ds,source)==0\\n hashes,images=r.historical(source);assert len(hashes)==29 and len(images)==17\\n records=ds.records();summary=ds.summary()\\n assert len(records)==1088 and summary==r.load(r.read(data/'summary.json'))==r.load(r.read(root/'artifacts/phase1/p08/summary.json'))\\n assert summary['usable']==0 and summary['training_authorized'] is False and summary['partition_authorized'] is False\\n assert all(x['state']!='approved_for_dataset' and not x.get('original_sha256') and not x.get('sanitized_sha256') for x in records)\\n assert len(ds.select('page'))==len(ds.select('cursor'))==120 and not ds.select('committed') and not ds.select('received') and not ds.select('source_failure')\\n assert all(x['status']=='no_crosswalk' for x in summary['coverage'] if x['source']=='inaturalist' and x['class_id'].startswith('species_'))\\n assert len(summary['coverage'])==28 and all(x['transferred']==x['approved']==0 for x in summary['coverage'])\\n review=r.load(r.read(data/'human-review.json'));objects=r.load(r.read(data/'object-hashes.json'));decisions=r.load(r.read(data/'decisions.template.json'))\\n assert len(review['candidates'])==len(objects)==len(decisions['decisions'])==1088\\n assert {x['candidate_id'] for x in review['candidates']}=={x['candidate_id'] for x in records}=={x['candidate_id'] for x in decisions['decisions']}\\n assert all(x['reviewer'] is None and x['expert_confirmation'] is False for x in decisions['decisions'])\\n assert r.read(data/'Attributions.jsonl')==b''\\n assert len(ds.select('request'))==120\\n for n in ['historical-before.json','historical-before-after.json']:\\n  historical=r.load(r.read(data/n));assert len(historical)==17\\n # Replay and verification are read-only: no acquisition/inspection/finalization invocation.\\n ds2=r.Dataset(data,config);ds2.replay();assert ds2.events==ds.events and ds2.summary()==summary\\nassert before=={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}\\nprint(json.dumps({'result':'passed','external_files_each':138,'manifest_sha256':receipt['approved_external_manifest_sha256'],'historical_files':29,'historical_images':17,'p07_receipt_hashes':7,'candidates_pending':1088,'transferred':0,'approved_for_dataset':0,'usable':0,'read_only_replay_bytes_and_mtimes_unchanged':True,'acceptance':'technical_bytes_only','candidate_review':'pending','inat':'no_crosswalk','training_authorized':False,'release':'pending','p09_started':False},sort_keys=True))\\n\\noriginal_before=json.loads(Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json').read_text())\\nassert {p.name:r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}==original_before\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/external-data-integrity.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/external-data-integrity.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:53.522403Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-ed42297912a84f72c6e20df34f39d52c",
    "signature": "8e6c6632019402fe47a31926a449cbff57acb0072757dc01fb81cd44dd4ad9d0",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "15026efdded74f457940ef09f7387c56af3d92ec1bd7273ed8ec9a025042cff5",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "approved-bytes": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport hashlib,json,subprocess\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nf=Path('artifacts/bianchini/v2/codex/P08/fix-B1')\\nassert h(f/'acceptance-manifest.sha256')=='d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d'\\nfiles=(f/'commit-inventory.txt').read_text().splitlines();assert len(files)==76\\nfor line in (f/'acceptance-manifest.sha256').read_text().splitlines():\\n expected,p=line.split('  ',1);assert h(Path(p))==expected\\nassert (f/'acceptance-digest.txt').read_text().split()[0]=='d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d'\\nassert set(files)=={l.split('  ',1)[1] for l in (f/'acceptance-manifest.sha256').read_text().splitlines()}|{str(f/'acceptance-manifest.sha256'),str(f/'acceptance-digest.txt')}\\nassert subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r','HEAD'],text=True).splitlines()==files\\nprint(json.dumps({'accepted_manifest_sha256':'d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d','accepted_paths':76,'covered_hashes':74,'result':'passed'}))\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/approved-bytes.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/approved-bytes.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:53.891693Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-9990999bf24ec29f22691c07fb773ee4",
    "signature": "8f9b868573915b1de58717efa386cf545147b17d47301c5c6adaa81313c2abe5",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "6f78ba258eeba25edb05f214f08ca9997d12dd84eccbec1b34b73c05eede5c24",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "final-human-bytes-acceptance": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport hashlib,json,subprocess\\nh=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()\\nf=Path('artifacts/bianchini/v2/codex/P08/fix-B1')\\nassert h(f/'acceptance-manifest.sha256')=='d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d'\\nfiles=(f/'commit-inventory.txt').read_text().splitlines();assert len(files)==76\\nfor line in (f/'acceptance-manifest.sha256').read_text().splitlines():\\n expected,p=line.split('  ',1);assert h(Path(p))==expected\\nassert (f/'acceptance-digest.txt').read_text().split()[0]=='d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d'\\nassert set(files)=={l.split('  ',1)[1] for l in (f/'acceptance-manifest.sha256').read_text().splitlines()}|{str(f/'acceptance-manifest.sha256'),str(f/'acceptance-digest.txt')}\\nassert subprocess.check_output(['git','diff-tree','--no-commit-id','--name-only','-r','HEAD'],text=True).splitlines()==files\\nprint(json.dumps({'accepted_manifest_sha256':'d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d','accepted_paths':76,'covered_hashes':74,'result':'passed'}))\\n\\na=json.loads(Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/human-acceptance.json').read_text())\\nassert a['accepted_manifest_sha256']=='d3440e45322d18e352a0d800e89d4054e89fc0f112520b777f871281080abd2d' and a['decision']=='accepted' and a['authority']=='human'\\nassert a['candidate_approval'] is False and a['authorization']['dataset_changes'] is False\\nprint(json.dumps({'correction_bytes_accepted':True,'candidate_decisions_not_substituted':True,'receipt_sha256':h(Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/human-acceptance.json'))}))\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/final-human-bytes-acceptance.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/final-human-bytes-acceptance.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:54.272526Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-5677a9d814e6faef015142a599db3307",
    "signature": "768fa619a29d57dd1c5fd258ff76434a2b5750ee7c2a8bf817ea47cbea423798",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "2da400cb2b1c6791f2f441aceedd45e5989f5b4c75c052f0d620cb4228f4ed9f",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "human-botanical-privacy-review": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport json,hashlib,sys\\nbase=Path('/home/administradorarthur/datasets/scanplant/p08-recovery-20261005')\\nevents=[json.loads(l) for l in (base/'journal.jsonl').read_text().splitlines()]\\nrecords=json.loads((base/'records.json').read_text())\\nif isinstance(records,dict): records=list(records.values())\\ntemplate=json.loads((base/'decisions.template.json').read_text())['decisions']\\nreceipt=json.loads(Path('artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_text())\\nreal=[]\\nfor item in records:\\n d=item.get('decision') or {}\\n if d.get('authority')=='human' and d.get('reviewer') and d.get('reviewed_at') and d.get('rationale'): real.append(item)\\nresult={'required_candidate_opinions':1088,'records':len(records),'human_candidate_opinions':len(real),'blank_template_entries':sum(not x.get('reviewer') for x in template),'historical_U803':receipt['U-803'],'technical_zero_transfer_accepted':receipt['zero_transfer_result_accepted'],'candidate_approval':receipt['candidate_approval'],'result':'passed' if len(real)==1088 else 'blocked_missing_human_candidate_opinions'}\\nprint(json.dumps(result,sort_keys=True),flush=True)\\nsys.exit(0 if len(real)==1088 else 1)\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/human-botanical-privacy-review.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/human-botanical-privacy-review.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:54.713258Z",
    "cwd": ".",
    "exit_code": 1,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-2f87449a54b378d54f97243c6d1e5470",
    "signature": "88521fb4aff4f58ea6d2a924159db5301cc5133884e4c87e7ae2d3bc63c61908",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "f83126da14025843546ab681e717a790a8f4bd2b43a705791df0a6993a3d9ae0",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  },
  "git-secrets-private-data-images-inspection": {
    "command": [
      "python3",
      "-B",
      "-c",
      "import subprocess,sys,pathlib; p=subprocess.run(['/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python', '-B', '-c', \"from pathlib import Path\\nimport json,hashlib,re,subprocess\\nroot=Path.cwd();f=root/'artifacts/bianchini/v2/codex/P08/fix-B1'\\nfiles=(f/'commit-inventory.txt').read_text().splitlines()\\nreport=json.loads((f/'security-inspection.json').read_text())\\nassert report['result']=='passed' and not report['automated_findings']\\nfor p,h in report['scanned_files_sha256'].items():assert hashlib.sha256((root/p).read_bytes()).hexdigest()==h,p\\nbad=[]\\nfor p in files:\\n b=(root/p).read_bytes();t=b.decode('utf-8')\\n if (root/p).suffix.lower() in {'.jpg','.jpeg','.png','.gif','.webp','.env','.pem','.p12'} or (root/p).is_symlink():bad.append(p)\\n if re.search(r'-----BEGIN (?:[A-Z ]+)?PRIVATE KEY-----|data:image/[^;]+;base64,|\\\\b(?:AKIA|ASIA)[A-Z0-9]{16}\\\\b|\\\\bgh[pousr]_[A-Za-z0-9]{30,}\\\\b',t):bad.append(p)\\nassert not bad\\nprint(json.dumps({'paths_scanned':len(files),'accepted_manual_classification_bound_by_hash':True,'binary_or_secret_findings':0,'synthetic_fixtures_and_historical_logs_preserved':True,'result':'passed'}))\\n\"],capture_output=True); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/git-secrets-private-data-images-inspection.stdout.txt').write_bytes(p.stdout); pathlib.Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/formal/git-secrets-private-data-images-inspection.stderr.txt').write_bytes(p.stderr); sys.stdout.buffer.write(p.stdout); sys.stderr.buffer.write(p.stderr); sys.exit(p.returncode)"
    ],
    "commit": "dd595a6d652c27773849003b0fc2c0ec1d8d3ad4",
    "created_at": "2026-10-07T23:24:55.104252Z",
    "cwd": ".",
    "exit_code": 0,
    "plan_id": "P08",
    "planning_version": "v2",
    "proof_id": "proof-04b1a3f781cfb488ecd2e43cd1232664",
    "signature": "4994e36d3d13a3acb3545139224420d6a664926ed58a4ae363dba6d54d879dbc",
    "spawn_error": false,
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "538facd3781ce2c1c8566817c3d8853737fe5d8cfb4698d97315edc6b7ad03a7",
    "timed_out": false,
    "timeout_seconds": 180.0,
    "unit_id": "1"
  }
}
```
