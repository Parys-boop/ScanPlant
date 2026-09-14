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
    "source": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md",
    "approved_at": "2026-09-14T22:30:45.431487+00:00",
    "authorization_scope": "Aprovação humana explícita nesta sessão do digest P05-R1 6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f, quarentena de quatro homônimos, versão 1.1.0, 79 aliases e 91 chaves. Autorizados commit local único de planejamento e execução completa da unidade. Implementação permanece unstaged, sem commit ou push até aceite humano final dos bytes. Aceite humano posterior dos oito hashes e autorização explícita dos dois commits de encerramento e push único reafirmados na retomada; registro artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json."
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
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p05-r1.jsonl",
      "package_digest": "adbb5266ffe846f03a02aa8c3bb03a390429aae216043cc58966f95094d0c0d0",
      "report_digest": "56f0776fa02ed7dfd22061b0e77cdd265737d4b5955105b47c9cf6b7cb903e73"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "P05-R1: uma unidade localizada à elegibilidade/quarentena authorless; P01 a P05 históricos preservados. Perfil standard e ciclo v2 mantidos; nenhum requisito adiado.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-14T22:30:45.431487+00:00",
    "approved_by": "responsável humano",
    "approved_plans": [
      "P01",
      "P02",
      "P03",
      "P04",
      "P05",
      "P05-R1"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p05-r1.sha256",
      "manifest_digest": "6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f",
      "files": [
        "CHECKPOINT_FASE0_OFFLINE.md",
        "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
        "artifacts/bianchini/v2/approval/manifest-p05-f1-man01.sha256",
        "artifacts/bianchini/v2/planning/p05-r1-policy.json",
        "artifacts/bianchini/v2/planning/p05-r1-preflight.json",
        "docs/PLANO_CANONICO_IA_HIBRIDA.md",
        "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-f1-man01.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md",
        "docs/bianchini/changes/v2/READINESS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/READINESS-p05-r1.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md",
        "docs/bianchini/changes/v2/inputs/p05-f1-man01/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/phase1/F1-G01-matriz-modelos-botanicos.md"
      ]
    }
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
      "status": "blocked",
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
      "status": "in_progress",
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
    }
  ],
  "verification": {
    "fast": {
      "commands": [
        "python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'",
        "python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
      ],
      "status": "passed",
      "scope": "P05-R1 working tree Python 3.14.4 -B: 94/94 testes documentais (81 anteriores + 13 novos), CLI 1.1.0, 79 aliases, 12 canônicos, 91 chaves; hashes em validation-report.json. Não é prova de commit da implementação."
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
      "scope": "Aceite humano dos oito hashes recebido; gates finais e provas vinculadas ao commit da implementação pendentes. Evidências posteriores em artifacts/bianchini/v2/codex/P05-R1/closure-verification.json."
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
  "active_execution": {
    "plan_id": "P05-R1",
    "unit": "1",
    "workspace": "/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a",
    "gate": "commit-bound-final-verification"
  },
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
  "next_action": "Concluir validações finais, commit autorizado da implementação, provas/revisão do guard nesse SHA e encerramento documental P05/P05-R1; publicar bm/v2-p05-r1 em push único sem força. Aceite U-201 registrado; release pending.",
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
    "plan": "P05",
    "functional_id": "F1-MAN01",
    "title": "Manifesto canônico das 12 espécies offline, sinônimos e duas classes de proteção",
    "status": "blocked",
    "roster_boundary": "U-201",
    "u201_status": "resolved_consumed",
    "execution_authorized": true,
    "release_authorized": false,
    "new_mutation_campaign_authorized": false,
    "replan": "P05-R1",
    "human_acceptance": "artifacts/bianchini/v2/codex/P05-R1/human-acceptance.json"
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
  }
}
