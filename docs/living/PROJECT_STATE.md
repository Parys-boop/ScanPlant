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
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker.jsonl",
      "package_digest": "3cf4e90115ddbdadd7f33b6fbf07614e3320f41d5c1d3b211b0d0a67c441770d",
      "report_digest": "83b873f2f68edfdb569cca89ce2bfddafe8b61a44488b4d90459aec2a370e1c3"
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
    "approved_at": "2026-08-29T19:35:00-03:00",
    "approved_by": "supervisor",
    "approved_plans": ["P01", "P02"],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest.sha256",
      "manifest_digest": "5cb628ea54d8e34b5b59531a8cec60784ee1a0312bb1d05ef5e54c69e6ccb36c",
      "files": [
        "docs/bianchini/changes/v2/inputs/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH.md",
        "docs/bianchini/changes/v2/READINESS.md",
        "docs/bianchini/changes/v2/USER_ACTIONS.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW.md"
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
      "status": "approved",
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
        "git diff --check"
      ],
      "status": "pending"
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
      "summary": "P01 bloqueado-terminal por lifecycle/observabilidade recorrente do executor Stryker; nenhuma nova campanha autorizada.",
      "evidence": "artifacts/bianchini/v1/evidence/P01-R1-final-foreground-inconclusive.json"
    }
  ],
  "next_action": "Aprovar uma única vez o pacote v2 e os planos P01/P02; executar P02 somente após validar suas pré-condições técnicas."
}
