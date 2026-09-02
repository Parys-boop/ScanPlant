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
    "source": "docs/bianchini/changes/v2/inputs/APPROVED_SCOPE.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "repo_only",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH.md",
    "readiness": "docs/bianchini/changes/v2/READINESS.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r1.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r1.jsonl",
      "package_digest": "e7f2192532ceabdae3ebc6aba9a140b3d512734e3ddb9e3e26944df7aec8f4ee",
      "report_digest": "1891cec2133ac11e01c44660d5b799cd7456fe355332aa0ed3819e05d5784df9"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Replanejamento limitado à dependência P01/P02 e observabilidade; sem código nesta rodada.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-08-31T19:51:42Z",
    "approved_by": "supervisor",
    "approved_plans": ["P01", "P02", "P03"],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest.sha256",
      "manifest_digest": "104c6d9af1ab2d2656e669ee85965048269bc9e36499d8ae280644e1863afe9b",
      "files": [
        "docs/bianchini/changes/v2/inputs/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/inputs/P03-WHITESPACE-REVISION.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH.md",
        "docs/bianchini/changes/v2/READINESS.md",
        "docs/bianchini/changes/v2/USER_ACTIONS.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r1.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r1.md"
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
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r1.md",
      "status": "blocked",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "mutation-observability"
      ],
      "depends_on": [
        "P01"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P01.md",
      "gates": [
        "mutation-evidence-verify",
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
        "git diff --check"
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
      "summary": "P01 bloqueado-terminal por lifecycle/observabilidade do executor Stryker; P03-R1 consumiu sua única campanha e falhou no resolver do local tool antes de produzir relatório. Nenhuma nova campanha é autorizada.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json"
    }
  ],
  "next_action": "Aguardar nova decisão formal sobre o bloqueio P03-R1; não executar P03-R1, Stryker ou P01 e não autorizar segunda campanha."
}
