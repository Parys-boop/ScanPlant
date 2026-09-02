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
    "source": "docs/bianchini/changes/v2/inputs/P03-R4-HOST-PORTABILITY-REPLAN.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "repo_only",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r4.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p03-r4.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p03-r4.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r4.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r4.jsonl",
      "package_digest": "c528fe22d9036ea8dd9b43e7c5c0784a989e11ed58a2476ca172d44161966c27",
      "report_digest": "1f0d498f81aa4991e39cdae318d097a663004bbc228436b923fda0203de37a74"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Revisão mínima limitada à portabilidade de paths externos P03 entre hosts equivalentes; preserva todos os contratos funcionais, parâmetros de campanha e histórico.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-02T23:02:29Z",
    "approved_by": "supervisor",
    "approved_plans": ["P01", "P02", "P03"],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r4.sha256",
      "manifest_digest": "1843cf70ea778d9ef884305361a42c5e97b45c9c91aa8b8815b6eba912dca1be",
      "files": [
        "docs/bianchini/changes/v2/inputs/P03-R4-HOST-PORTABILITY-REPLAN.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r4.md",
        "docs/bianchini/changes/v2/READINESS-p03-r4.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r4.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r4.md"
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
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md",
      "status": "approved",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "mutation-observability",
        "external-fallback"
      ],
      "depends_on": [
        "P01"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P01.md",
      "gates": [
        "host-portability-resolution",
        "composite-launcher-identity-resolution",
        "mutation-harness-preflight",
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
      "status": "pending"
    },
    "plan": {
      "commands": [
        "P03-R4: preflights and mutation-evidence verify are not authorized in this planning round; execute only after the separate approvals stated in USER_ACTIONS-p03-r4.md."
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
      "summary": "P03-R1 consumiu 1/1 campanha e falhou no resolver do local tool antes de mutação. P01 permanece blocked-terminal; P03-R3 pode somente ser executado após aprovação humana do novo pacote.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json"
    },
    {
      "id": "B-P03-R2-LAUNCHER-BANNER",
      "summary": "Histórico imutável: P03-R2 Tarefa 1 materializou o resolver local 4.16.0 e executou uma única prova --help no ambiente sanitizado, mas o stdout não emitiu o banner então obrigatório Version: 4.16.0. A tarefa bloqueou sob seu contrato; MutationHarness, Tarefa 2 e campanha não foram executados, e campaign_count permaneceu 0.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/preflight-run-ZBwbUU/task-1-blocked.json"
    },
    {
      "id": "B-P03-R3-HOST-PORTABILITY-MATERIAL-CHANGE",
      "summary": "P03-R3 permanece historicamente aprovado, mas seus paths externos literais pertencem ao host anterior e não são executáveis neste host sob o contrato rígido. É bloqueio de portabilidade contratual/ambiental, não falha de produto; P03-R4 está aprovado e preserva autorização de campanha separada.",
      "evidence": "docs/bianchini/changes/v2/inputs/P03-R4-HOST-PORTABILITY-REPLAN.md"
    }
  ],
  "next_action": "Commitar e sincronizar o pacote P03-R4 aprovado; somente depois, e quando explicitamente solicitado, executar os preflights não consumidores no linked worktree canônico. Campanha continua não autorizada e exige autorização humana separada, posterior e vinculada ao HEAD executável."
}
