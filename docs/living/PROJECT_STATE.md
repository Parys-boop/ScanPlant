{
  "method_version": 2,
  "method_mode": "standalone-adaptive",
  "planning_version": "v2",
  "planning_status": "approved",
  "execution_policy": "adaptive",
  "assurance_profile": "standard",
  "architecture_audit": "optional",
  "architecture_audit_status": "not_run",
  "manual_pdf": "scope",
  "scope": {
    "status": "approved",
    "source": "docs/bianchini/changes/v2/inputs/p08/APPROVED_SCOPE.md",
    "approved_at": null,
    "authorization_scope": "Escopo de planejamento aprovado; instrução posterior aprovou digest e autorizou somente registrar/stage/commit/push do planejamento P08 nos 13 caminhos. Execução depende de autorização posterior sobre o plano publicado."
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "targeted_web",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p08.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p08.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
    "spec": "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p08.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p08.jsonl",
      "package_digest": "93bac3f4cef107e95a563b04e8a0f3d70560a61dcd43ae9fecebd352ced8aa21",
      "report_digest": "3c308f43108595fac5ed86e407f0c99ab829b9de9042bac7d9da08a2b6c455ad"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Um novo plano P08/uma unidade strict de risco alto localizado, perfil standard; extensão Python e dois contratos de fonte. Sete planos anteriores são históricos preservados, sem execução. Nenhum requisito adiado por orçamento.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-10-02T03:08:06.008772+00:00",
    "approved_by": "responsável humano — aprovação explícita nesta sessão",
    "approved_plans": [
      "P01",
      "P02",
      "P03",
      "P04",
      "P05",
      "P05-R1",
      "P07",
      "P08"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p08.sha256",
      "manifest_digest": "6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a",
      "files": [
        "CHECKPOINT_FASE0_OFFLINE.md",
        "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
        "artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256",
        "artifacts/bianchini/v2/codex/P07/closure-evidence.json",
        "artifacts/bianchini/v2/codex/P07/human-acceptance.json",
        "artifacts/bianchini/v2/codex/convergence/P07/1.json",
        "artifacts/bianchini/v2/planning/p05-r1-policy.json",
        "artifacts/bianchini/v2/planning/p05-r1-preflight.json",
        "artifacts/bianchini/v2/planning/p07-policy.json",
        "artifacts/bianchini/v2/planning/p08-policy.json",
        "artifacts/phase1/p06/recovery-20260928.json",
        "artifacts/phase1/p07/summary.json",
        "docs/PLANO_CANONICO_IA_HIBRIDA.md",
        "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
        "docs/bianchini/changes/v2/P08-BASELINE.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-f1-man01.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p07.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p08.md",
        "docs/bianchini/changes/v2/READINESS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/READINESS-p05-r1.md",
        "docs/bianchini/changes/v2/READINESS-p07.md",
        "docs/bianchini/changes/v2/READINESS-p08.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p07.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p08.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
        "docs/bianchini/changes/v2/inputs/p05-f1-man01/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/inputs/p07/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/inputs/p08/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md",
        "docs/bianchini/changes/v2/spec-deltas/dataset-recovery.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md",
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/phase1/F1-API01-benchmark-decision.md",
        "docs/phase1/F1-G01-matriz-modelos-botanicos.md",
        "docs/phase1/F1-MAN01-offline-class-manifest.md",
        "docs/phase1/P06-acquisition.md",
        "docs/phase1/P06-quarantine-review.md",
        "docs/phase1/P06-recovery-20260928.md",
        "docs/phase1/P07-curation.md",
        "docs/phase1/offline-class-manifest.v1.json",
        "scripts/phase1/requirements-p06.txt"
      ]
    },
    "authorization_scope": "Aprovação integral somente do pacote P08 e de seu único plano/unidade, vinculada ao digest 6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a. Autorizados nesta rodada apenas registro da aprovação, staging dos 13 caminhos inventariados, um commit chore(p08): approve dataset recovery plan e push normal da branch bm/v2-p08-planning. IDs anteriores em approved_plans preservam compatibilidade do Method; não reabrem nem renovam autorização histórica. Implementação, APIs de aquisição, imagens/dataset P08, dependências, treinamento, partições, augmentation, integração, P09, merge/tag/homologação/release continuam não autorizados."
  },
  "plans": [
    {
      "id": "P01",
      "path": "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
      "status": "blocked",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "mutation-observability"
      ],
      "depends_on": [],
      "ledger": "artifacts/bianchini/v2/ledgers/P01.md",
      "gates": [
        "documentary-integrity"
      ]
    },
    {
      "id": "P02",
      "path": "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
      "status": "completed",
      "risk": "medium",
      "execution": "slice",
      "review": "per_slice",
      "test_seams": [
        "mobile-consent-gate",
        "scanplant-api-client"
      ],
      "depends_on": [],
      "ledger": "artifacts/bianchini/v2/ledgers/P02.md",
      "gates": [
        "focused-regression",
        "mobile-build"
      ]
    },
    {
      "id": "P03",
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
      "status": "blocked",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "mutation-observability",
        "external-fallback",
        "harness-project-resolution",
        "isolated-test-project-selection"
      ],
      "depends_on": [
        "P01"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P01.md",
      "gates": [
        "r6-context-selection",
        "r6-isolated-net8-build",
        "mutation-harness-preflight",
        "documentary-integrity"
      ]
    },
    {
      "id": "P04",
      "path": "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
      "status": "completed",
      "risk": "medium",
      "execution": "slice",
      "review": "per_slice",
      "test_seams": [
        "provider-benchmark-evidence",
        "corpus-to-observations"
      ],
      "depends_on": [
        "P02"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P04.md",
      "gates": [
        "benchmark-evidence-review",
        "external-authorization-and-zero-spend",
        "documentary-integrity"
      ]
    },
    {
      "id": "P05",
      "path": "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
      "status": "completed",
      "risk": "low",
      "execution": "grouped",
      "review": "plan_gate",
      "test_seams": [
        "offline-manifest-contract",
        "normalize_name",
        "resolve_scientific_name"
      ],
      "depends_on": [
        "P04"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P05.md",
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
      "status": "completed",
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
        "P04"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P05.md",
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
      "status": "completed",
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
      "depends_on": [
        "P05-R1"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P07.md",
      "gates": [
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
      "status": "approved",
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
      "depends_on": [
        "P07"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P08.md",
      "gates": [
        "synthetic-source-contract",
        "canonical-taxonomy",
        "append-only-integrity-idempotence",
        "selective-mutation",
        "p07-17-preserved",
        "human-botanical-privacy-review",
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
      "status": "pending",
      "scope": "P08 futuro; arquivos entregáveis, não implementados neste planejamento."
    },
    "plan": {
      "commands": [
        "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'",
        "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
        "sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS",
        "git diff --check"
      ],
      "status": "pending",
      "scope": "P08 futuro; suite inclui cinco mutações stdlib aprovadas no planejamento; requer gates de dados/revisão/recibo externo. Não autoriza treino/release."
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
    "status": "pending",
    "platforms": [
      "ASP.NET Core .NET 8",
      "Android Expo/React Native"
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
  "active_execution": null,
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
    {
      "id": "B-P03-R2-LAUNCHER-BANNER",
      "summary": "Histórico imutável: P03-R2 bloqueou na Tarefa 1; MutationHarness, Tarefa 2 e campanha não foram executados e campaign_count permaneceu 0.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/preflight-run-ZBwbUU/task-1-blocked.json"
    },
    {
      "id": "B-P03-R3-HOST-PORTABILITY-MATERIAL-CHANGE",
      "summary": "P03-R3 permanece histórico aprovado, incompatível com o host sob seu contrato anterior; R4 preservou a portabilidade ambiental.",
      "evidence": "docs/bianchini/changes/v2/inputs/P03-R4-HOST-PORTABILITY-REPLAN.md"
    },
    {
      "id": "B-P03-R4-MUTATIONHARNESS-CWD-ARTIFACTS",
      "summary": "P03-R4 bloqueou antes do MutationHarness: cwd literal não resolve o csproj real e os artifacts net8.0 para no-build/no-restore estavam ausentes; campaign_count permaneceu 0.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r4/preflight-run-9YWNE7/task-1-blocked.json"
    },
    {
      "id": "B-P03-R5-U008-PREFLIGHT-RG",
      "summary": "Checkpoint histórico: o preflight parcial U-008 interrompeu antes de restore, launcher, MutationHarness e Stryker porque rg não estava no PATH sanitizado; campaign_count permaneceu 0. A correção externa posterior confirmou /usr/bin/rg no mesmo PATH, sem retry.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r5/preflight-run-U008-Is31mo"
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
    }
  ],
  "next_action": "Aguardar autorização posterior de execução P08 sobre o plano publicado. Pacote/digest P08 integralmente aprovado; esta rodada autoriza somente registro, staging, commit e push do planejamento. P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed; guard completed sem blockers; usable=0 até decisões humanas válidas; P06/P07 fechados e imutáveis; release pending; active_execution null; treinamento não autorizado; P09 não iniciado.",
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
  "terminal_campaign": {
    "plan": "P03-R6",
    "status": "blocked-terminal",
    "campaign_count": 2,
    "campaign_executed": true,
    "U-008": "consumed_non_reusable",
    "U-009": "consumed",
    "exit_code": 134,
    "failure_stage": "campaign",
    "mutation_score": null,
    "mutant_counts": null,
    "retry_permitted": false,
    "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909"
  },
  "prior_approval": {
    "plan": "P03-R6",
    "status": "approved",
    "approved_at": "2026-09-09T01:38:16Z",
    "approved_by": "supervisor",
    "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r6.sha256",
    "manifest_digest": "18cef0bf86bc6eecfaa10a8ee241e0c4fa3d543fbcdcd90cca75d6b661c032e1",
    "execution_status": "blocked-terminal; authorization consumed; immutable history"
  },
  "prior_p04_approval": {
    "status": "approved",
    "approved_at": "2026-09-09T22:22:31Z",
    "approved_by": "responsável humano",
    "manifest_path": "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
    "manifest_digest": "9657abcbb1520701a59bbd8fcecf34ff5d7a34fb901ad5d84defd6df34a31d23",
    "execution_status": "completed",
    "state_at_revision": "a34da4dd34eea58921862f0d0fa2d0016be5ce31",
    "note": "Registro histórico, não revalidar manifesto antigo contra ledger/evidências vivos posteriores."
  },
  "next_milestone_proposal": {
    "plan": "P08",
    "functional_id": "P08",
    "title": "Recuperação limitada e rastreável da insuficiência do dataset",
    "status": "approved",
    "execution_authorized": false,
    "collection_authorized": false,
    "training_authorized": false,
    "release_authorized": false,
    "usable_baseline": 0,
    "source_commit": "b6844f9129d9edf862ae7958d8f043d9bdd5bd84"
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
      "P05"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256",
      "manifest_digest": "246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5",
      "files": [
        "CHECKPOINT_FASE0_OFFLINE.md",
        "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
        "docs/PLANO_CANONICO_IA_HIBRIDA.md",
        "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-f1-man01.md",
        "docs/bianchini/changes/v2/READINESS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/inputs/p05-f1-man01/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/phase1/F1-G01-matriz-modelos-botanicos.md"
      ]
    },
    "plan": "P05",
    "state_at_revision": "77e93a221dad3115c301b10317b626c236a3ba84",
    "execution_status": "blocked; historical package immutable; affected alias rule replanned by P05-R1",
    "historical_checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p05-f1-man01.jsonl",
      "package_digest": "2397bbf690f5cada9d0429b8a07c79bd32ee2dd162b2644ffeb7be81bd624493",
      "report_digest": "104a4d10e0328f32ec69ab90ded94100f265c411229119589d5eaf2175aef8ac"
    }
  },
  "prior_p05_r1_approval": {
    "status": "approved",
    "manifest_path": "artifacts/bianchini/v2/approval/manifest-p05-r1.sha256",
    "manifest_digest": "6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f",
    "execution_status": "P05 and P05-R1 completed at 2a8a6902fd6e33b794628235757b0279f580b02a; historical package immutable"
  },
  "p06_direct_closure": {
    "status": "completed_acquisition_mechanism_only",
    "commit": "3f0beaad06bfdd9b4f069a6f5f668ce9e9b93d97",
    "evidence": "docs/phase1/P06-recovery-20260928.md",
    "external_quarantined": 17,
    "usable": 0,
    "training_released": 0,
    "historical_images_lost": 11,
    "historical_images_reproduced": 0,
    "release": "pending",
    "reopened": false
  },
  "prior_next_milestone_proposal": {
    "plan": "P05",
    "functional_id": "F1-MAN01",
    "title": "Manifesto canônico das 12 espécies offline, sinônimos e duas classes de proteção",
    "status": "completed",
    "roster_boundary": "U-201",
    "u201_status": "resolved_consumed",
    "execution_authorized": true,
    "release_authorized": false,
    "new_mutation_campaign_authorized": false,
    "replan": "P05-R1",
    "human_acceptance": "artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json"
  },
  "prior_p07_approval": {
    "approval": {
      "status": "approved",
      "approved_at": "2026-09-30T20:44:44+00:00",
      "approved_by": "responsável humano",
      "approved_plans": [
        "P01",
        "P02",
        "P03",
        "P04",
        "P05",
        "P05-R1",
        "P07"
      ],
      "package": {
        "algorithm": "sha256-manifest-v1",
        "manifest_path": "artifacts/bianchini/v2/approval/manifest-p07.sha256",
        "manifest_digest": "2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3",
        "files": [
          "CHECKPOINT_FASE0_OFFLINE.md",
          "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
          "artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256",
          "artifacts/bianchini/v2/planning/p05-r1-policy.json",
          "artifacts/bianchini/v2/planning/p05-r1-preflight.json",
          "artifacts/bianchini/v2/planning/p07-policy.json",
          "artifacts/phase1/p06/recovery-20260928.json",
          "docs/PLANO_CANONICO_IA_HIBRIDA.md",
          "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
          "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-f1-man01.md",
          "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md",
          "docs/bianchini/changes/v2/PLANNING_REVIEW-p07.md",
          "docs/bianchini/changes/v2/READINESS-p05-f1-man01.md",
          "docs/bianchini/changes/v2/READINESS-p05-r1.md",
          "docs/bianchini/changes/v2/READINESS-p07.md",
          "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md",
          "docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md",
          "docs/bianchini/changes/v2/STACK_RESEARCH-p07.md",
          "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
          "docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md",
          "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
          "docs/bianchini/changes/v2/inputs/p05-f1-man01/APPROVED_SCOPE.md",
          "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md",
          "docs/bianchini/changes/v2/inputs/p07/APPROVED_SCOPE.md",
          "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
          "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
          "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
          "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
          "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
          "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
          "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md",
          "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
          "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
          "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
          "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
          "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
          "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md",
          "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
          "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
          "docs/bianchini/changes/v2/specs/p07-curation-change.md",
          "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
          "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
          "docs/bianchini/changes/v2/specs/replan-v2.md",
          "docs/phase1/F1-API01-benchmark-decision.md",
          "docs/phase1/F1-G01-matriz-modelos-botanicos.md",
          "docs/phase1/F1-MAN01-offline-class-manifest.md",
          "docs/phase1/P06-acquisition.md",
          "docs/phase1/P06-quarantine-review.md",
          "docs/phase1/P06-recovery-20260928.md",
          "docs/phase1/offline-class-manifest.v1.json",
          "scripts/phase1/requirements-p06.txt"
        ]
      },
      "authorization_scope": "Aprovação nova somente do pacote P07 e digest 2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3; autorização desta rodada limitada a registrar, commitar e publicar os 13 caminhos do planejamento. IDs históricos em approved_plans satisfazem o contrato do estado e não reabrem execução."
    },
    "planning": {
      "quality_version": 2,
      "research_mode": "targeted_web",
      "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p07.md",
      "readiness": "docs/bianchini/changes/v2/READINESS-p07.md",
      "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
      "spec": "docs/bianchini/changes/v2/specs/p07-curation-change.md",
      "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p07.md",
      "checker": {
        "status": "passed",
        "rounds": 1,
        "history_path": "artifacts/bianchini/v2/planning/checker-p07.jsonl",
        "package_digest": "ba7e75942b363d5090166dc0f15569c4a47b29b224b2ca9dc2f688354fb3e9ac",
        "report_digest": "8254439e3b7104256870255a16608bc5e9ec8111477d26a2ea3046c4d9b635fb"
      },
      "design_manifest": null,
      "change_root": "docs/bianchini/changes/v2",
      "current_specs": "docs/bianchini/current/specs"
    },
    "execution_status": "completed",
    "published_commit": "b6844f9129d9edf862ae7958d8f043d9bdd5bd84",
    "note": "Histórico imutável; não revalidar manifesto antigo contra fatos vivos posteriores."
  },
  "prior_p07_verification": {
    "fast": {
      "commands": [
        "python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'"
      ],
      "status": "passed",
      "scope": "P07: 38 testes; evidências vinculadas ao commit de implementação em artifacts/bianchini/v2/codex/P07/closure-evidence.json."
    },
    "plan": {
      "commands": [
        "python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'",
        "python -B -m json.tool artifacts/phase1/p07/summary.json",
        "git diff --check"
      ],
      "status": "passed",
      "scope": "P07: 162 testes afetados/históricos, 17 fontes preservadas, 136 pares, aceite humano, finalização idempotente e verificações documentais aprovados. Evidência em artifacts/bianchini/v2/codex/P07/closure-evidence.json. Não substitui verification.release."
    }
  },
  "p07_closure": {
    "status": "completed",
    "published_commit": "b6844f9129d9edf862ae7958d8f043d9bdd5bd84",
    "guard": "completed",
    "guard_blockers": [],
    "U-701": "accepted",
    "U-702": "accepted",
    "approved_for_dataset": 0,
    "usable": 0,
    "release": "pending",
    "training_authorized": false,
    "reopened": false
  },
  "prior_p07_milestone": {
    "plan": "P07",
    "functional_id": "P07",
    "title": "Curadoria rastreável das 17 imagens externas preservadas pelo P06",
    "status": "completed",
    "execution_authorized": true,
    "release_authorized": false,
    "usable_baseline": 0,
    "source_commit": "3f0beaad06bfdd9b4f069a6f5f668ce9e9b93d97"
  },
  "p08_planning_approval": {
    "digest": "6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a",
    "approved_at": "2026-10-02T03:08:06.008772+00:00",
    "approved_by": "responsável humano",
    "new_plans": [
      "P08"
    ],
    "execution_units": 1,
    "assurance_profile": "standard",
    "risk": "high",
    "execution": "strict",
    "review": "per_task",
    "publication_authorized": true,
    "execution_authorized": false,
    "usable": 0,
    "training_authorized": false,
    "p09_started": false,
    "human_decision_boundary": "Itens sem licença individual, autoria/proveniência, identidade taxonômica ou revisão de privacidade suficientes permanecem pendentes/rejeitados. Ausência de especialista não permite aprovação artificial nem invalida conclusão técnica do mecanismo; zero aprovadas e classes vazias são válidos. Aceite futuro dos bytes e demais gates permanecem obrigatórios."
  }
}
