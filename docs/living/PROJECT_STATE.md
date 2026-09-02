{
  "method_version": 2,
  "method_mode": "standalone-adaptive",
  "planning_version": "v2",
  "planning_status": "pending_approval",
  "execution_policy": "adaptive",
  "assurance_profile": "standard",
  "architecture_audit": "optional",
  "architecture_audit_status": "not_run",
  "manual_pdf": "scope",
  "scope": {
    "status": "approved",
    "source": "docs/bianchini/changes/v2/inputs/P03-R3-COMPOSITE-LAUNCHER-REPLAN.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "targeted_web",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r3.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p03-r3.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p03-r3.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r3.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r3.jsonl",
      "package_digest": "3913a9589cd18354f033ad84c4b92033f99f0ccd7a5e0e946c8fc3f08f9aadd7",
      "report_digest": "bb7d1a062dd036c061755cc07e4bfa3c483a827f2032eeba07d3d433dde1bd45"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Revisão estritamente limitada à impossibilidade comprovada do banner de help P03-R2, à prova composta não consumidora, ao harness e a no máximo uma campanha humana futura; sem alteração de produto.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "pending",
    "approved_at": null,
    "approved_by": null,
    "approved_plans": [],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r3.sha256",
      "manifest_digest": "a337c89a4ab678d3f6f59494f8888832e6d789e9b213f5b3f01c5b0e3379b741",
      "files": [
        "docs/bianchini/changes/v2/inputs/P03-R3-COMPOSITE-LAUNCHER-REPLAN.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r3.md",
        "docs/bianchini/changes/v2/READINESS-p03-r3.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r3.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r3.md"
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
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md",
      "status": "planned",
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
      "summary": "P03-R1 consumiu 1/1 campanha e falhou no resolver do local tool antes de mutação. P01 permanece blocked-terminal; P03-R3 pode somente ser executado após aprovação humana do novo pacote.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json"
    },
    {
      "id": "B-P03-R2-LAUNCHER-BANNER",
      "summary": "Histórico imutável: P03-R2 Tarefa 1 materializou o resolver local 4.16.0 e executou uma única prova --help no ambiente sanitizado, mas o stdout não emitiu o banner então obrigatório Version: 4.16.0. A tarefa bloqueou sob seu contrato; MutationHarness, Tarefa 2 e campanha não foram executados, e campaign_count permaneceu 0.",
      "evidence": "artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/preflight-run-ZBwbUU/task-1-blocked.json"
    },
    {
      "id": "B-P03-R3-PENDING-APPROVAL",
      "summary": "P03-R3 é planejamento pendente de aprovação humana. Nenhum preflight, launcher, MutationHarness ou campanha está autorizado nesta rodada; campaign_count permanece 0.",
      "evidence": "docs/bianchini/changes/v2/inputs/P03-R3-COMPOSITE-LAUNCHER-REPLAN.md"
    }
  ],
  "next_action": "Solicitar aprovação humana única do digest e de todos os planos P03-R3. Antes dela não executar launcher, tool restore, MutationHarness ou campanha; campaign_count permanece 0. Após preflights passarem, uma segunda autorização humana explícita e separada será necessária para a única campanha."
}
