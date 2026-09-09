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
    "source": "docs/bianchini/changes/v2/inputs/P03-R6-TEST-PROJECT-ISOLATION-REPLAN.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "repo_only",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r6.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p03-r6.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r6.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r6.jsonl",
      "package_digest": "03074f5578e7270b720e06f5ecee8a1af75d81558968771aea6bdc1b970c5ce8",
      "report_digest": "eeb64bfb6cc5a36152c8abab7cb189ec9153f48bcc4bdb7d29551b5b953d2d3c"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Replanejamento documental mínimo do contrato de seleção de projeto de testes e solução temporária net8; preserva a tentativa U-008 terminal e não contém patch de produto.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-09T01:38:16Z",
    "approved_by": "supervisor",
    "approved_plans": [
      "P01",
      "P02",
      "P03"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r6.sha256",
      "manifest_digest": "18cef0bf86bc6eecfaa10a8ee241e0c4fa3d543fbcdcd90cca75d6b661c032e1",
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
        "artifacts/bianchini/v2/ledgers/P01.md"
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
      "status": "approved",
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
    }
  ],
  "verification": {
    "fast": {
      "commands": [
        "git diff --check"
      ],
      "status": "pending"
    },
    "plan": {
      "commands": [
        "dotnet build /tmp/p03-r6-net8-context/P03-R6-net8.sln --no-restore",
        "dotnet test ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore"
      ],
      "status": "blocked"
    },
    "release": {
      "commands": [
        "git diff --check"
      ],
      "status": "pending"
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
    }
  ],
  "next_action": "Commitar e sincronizar somente o pacote documental aprovado P03-R6. Após o HEAD documental final estar em origin/bm/v2-p03, limpo e em 0/0, executar apenas o preflight corretivo R6 no WSL normal. U-008 está consumida; campaign_count acumulado=1; somente U-009 posterior poderá autorizar uma nova transição 1->2."
}
