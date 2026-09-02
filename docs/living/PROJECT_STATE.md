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
    "source": "docs/bianchini/changes/v2/inputs/P03-R2-LAUNCHER-REPLAN.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "targeted_web",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH.md",
    "readiness": "docs/bianchini/changes/v2/READINESS.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r2.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r2.jsonl",
      "package_digest": "8780ba276727c55fc11e7180e8c201df1da3f1e4679565b1f8b762dc88d6d3ed",
      "report_digest": "1b803e0d6648ec2a4500c26675a6a0a09c21ed9ba5c5e5ecb032781256d48870"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Revisão estritamente limitada à falha ambiental do launcher P03-R1, a dois preflights não consumidores e a no máximo uma campanha humana futura; sem alteração de produto.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-02T13:07:10Z",
    "approved_by": "supervisor",
    "approved_plans": ["P01", "P02", "P03"],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r2.sha256",
      "manifest_digest": "089b27ab52ec8351ed9d8abda6a8f1dcb9603a6681ec8ad14b54bba2d410ad6b",
      "files": [
        "docs/bianchini/changes/v2/inputs/P03-R2-LAUNCHER-REPLAN.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH.md",
        "docs/bianchini/changes/v2/READINESS.md",
        "docs/bianchini/changes/v2/USER_ACTIONS.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r2.md"
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
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md",
      "status": "blocked",
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
        "launcher-resolution",
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
        "python3 /home/arthur/.agents/skills/_shared/scripts/bm.py mutation-evidence verify --state docs/living/PROJECT_STATE.md --root . --plan P03 --risk-seam external-fallback --tool stryker --command \"$(tr '\\n' ' ' < artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/campaign/command.txt)\" --report artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/results/reports/mutation-report.json --classifications artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/mutation-classifications.json --revision \"$(git rev-parse HEAD)\" --output artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/mutation-evidence.json"
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
      "summary": "P03-R1 consumiu 1/1 campanha e falhou no resolver do local tool antes de mutação; o planejamento P03-R2 está aprovado. Somente preflights não consumidores poderão ocorrer no próximo marco; uma nova campanha requer autorização humana explícita, separada e posterior aos preflights aprovados.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json"
    },
    {
      "id": "B-P03-R2-LAUNCHER-BANNER",
      "summary": "P03-R2 Tarefa 1 materializou o resolver local 4.16.0 e executou uma única prova --help no ambiente sanitizado, mas o stdout não emitiu o banner obrigatório Version: 4.16.0. A tarefa está bloqueada; MutationHarness, Tarefa 2 e campanha não foram executados, e campaign_count permanece 0.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/preflight-run-ZBwbUU/task-1-blocked.json"
    }
  ],
  "next_action": "P03-R2 Tarefa 1 está bloqueada pela ausência do banner obrigatório Version: 4.16.0 no único launcher preflight permitido. Não executar MutationHarness, Tarefa 2 ou campanha; campaign_count permanece 0. Exige decisão humana explícita antes de qualquer nova tentativa."
}
