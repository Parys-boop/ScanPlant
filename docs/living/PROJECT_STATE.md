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
    "source": "docs/bianchini/changes/v2/inputs/POST-U009-CONTINUITY-SCOPE.md",
    "approved_at": null,
    "authorization_scope": "Plano P04/F1-API01 aprovado; U-101 resolvida em 2026-09-10 para exatamente 14 identificações dos sete bytes congelados, sete por provider, zero retry e zero chamadas textuais."
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "repo_only",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p04-f1-api01.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p04-f1-api01.md",
    "spec": "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p04-f1-api01.md",
    "checker": {
      "status": "passed",
      "rounds": 2,
      "history_path": "artifacts/bianchini/v2/planning/checker-p04-f1-api01.jsonl",
      "package_digest": "eb53eeedc7cd134bbd9abdca2e2db383e87a0e2bda9e9ae4e7c0fdad2a4dd392",
      "report_digest": "0e3ef022fdd4f6c3d14cb926857f38ddc0eb1a5e4e9266d51ad8d01e78b5081a"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Uma única entrega documental P04/F1-API01, sem produto ou campanha. P01/P02/P03 permanecem no estado e pacote como contratos históricos imutáveis, sem reabertura e sem fechamento do ciclo.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-09T22:22:31Z",
    "approved_by": "responsável humano",
    "approved_plans": [
      "P01",
      "P02",
      "P03",
      "P04"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p04-f1-api01.sha256",
      "manifest_digest": "9657abcbb1520701a59bbd8fcecf34ff5d7a34fb901ad5d84defd6df34a31d23",
      "files": [
        "docs/bianchini/changes/v2/inputs/P03-R6-TEST-PROJECT-ISOLATION-REPLAN.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r6.md",
        "docs/bianchini/changes/v2/READINESS-p03-r6.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r6.md",
        "artifacts/bianchini/v2/checkpoints/P03-R5-U008-terminal-attempt-716ef26.json",
        "artifacts/bianchini/v2/ledgers/P01.md",
        "docs/PLANO_CANONICO_IA_HIBRIDA.md",
        "docs/bianchini/changes/v2/inputs/POST-U009-CONTINUITY-SCOPE.md",
        "docs/bianchini/changes/v2/POST-U009-DELIBERATION.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md",
        "docs/bianchini/changes/v2/READINESS-p04-f1-api01.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p04-f1-api01.md",
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p04-f1-api01.md",
        "artifacts/bianchini/v2/ledgers/P04.md",
        "artifacts/bianchini/v2/approval/manifest-p03-r6.sha256",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/README.md",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/campaign-summary.txt",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/campaign-count",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/progress.log",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/stryker.log",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/namespace-loopback-diagnosis.txt",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/preserved-files-inventory.txt",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/sanitization-report.txt",
        "artifacts/bianchini/v2/evidence/P03-p01-mutation-r6/u009-terminal-execution-20260909/SHA256SUMS"
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
      "status": "in_progress",
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
    }
  ],
  "verification": {
    "fast": {
      "commands": [
        "git diff --check"
      ],
      "status": "passed"
    },
    "plan": {
      "commands": [
        "python3 -m json.tool artifacts/bianchini/v2/evidence/P04-f1-api01/corpus-manifest.json",
        "python3 -m json.tool artifacts/bianchini/v2/evidence/P04-f1-api01/observations.json",
        "git diff --check"
      ],
      "status": "passed",
      "scope": "U-101 aprovada e preflight sem transmissão validado: sete bytes congelados, 14 pares not_run, hashes/metadados/JSON/checksums, segredos presentes sem leitura, DNS/HTTPS, isolamento e persistência conferidos. Coleta e revisão final ainda não executadas."
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
  "next_action": "Após preservar e sincronizar o checkpoint do corpus, executar uma única coleta P04 na ordem congelada: Pl@ntNet e Plant.id por caso, sete chamadas por provider, concorrência 1, timeout 20 segundos, zero retry e persistência antes do próximo slot; então parar para revisão humana antes do commit final. P01/P03-R6 permanecem blocked-terminal, P02 completed e release pending.",
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
  }
}
