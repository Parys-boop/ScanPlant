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
    "source": "docs/bianchini/changes/v2/inputs/P03-R5-MUTATIONHARNESS-CONTRACT-REPLAN.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "repo_only",
    "research": "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r5.md",
    "readiness": "docs/bianchini/changes/v2/READINESS-p03-r5.md",
    "user_actions": "docs/bianchini/changes/v2/USER_ACTIONS-p03-r5.md",
    "spec": "docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md",
    "review": "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r5.md",
    "checker": {
      "status": "passed",
      "rounds": 1,
      "history_path": "artifacts/bianchini/v2/planning/checker-p03-r5.jsonl",
      "package_digest": "73488f8ee85ca34455b1f63f6c687c936386ce788eb45f344950a2d89cdfb4c3",
      "report_digest": "9c1c39359bfa51a1329b9fecf5b3104c765b5cec918f4725b7236ab4b29f2667"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v2",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": "Replanejamento documental mínimo do único contrato factual inválido: cwd e artifacts do MutationHarness; não há patch, dependência, alvo ou campanha no escopo.",
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-09-02T23:43:12Z",
    "approved_by": "supervisor",
    "approved_plans": [
      "P01",
      "P02",
      "P03"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v2/approval/manifest-p03-r5.sha256",
      "manifest_digest": "6c93ec50d297b23864b8c808b10e789409de9a46f8ee8f3faf2c5c111f2e33eb",
      "files": [
        "docs/bianchini/changes/v2/inputs/P03-R5-MUTATIONHARNESS-CONTRACT-REPLAN.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r5.md",
        "docs/bianchini/changes/v2/READINESS-p03-r5.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r5.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md",
        "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md",
        "docs/bianchini/changes/v2/PLANNING_REVIEW-p03-r5.md"
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
      "path": "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md",
      "status": "blocked",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "mutation-observability",
        "external-fallback",
        "harness-project-resolution"
      ],
      "depends_on": [
        "P01"
      ],
      "ledger": "artifacts/bianchini/v2/ledgers/P01.md",
      "gates": [
        "host-portability-resolution",
        "composite-launcher-identity-resolution",
        "offline-harness-preparation",
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
        "dotnet test ScanPlantAPI.MutationHarness.csproj --framework net8.0 --no-build --no-restore"
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
    }
  ],
  "next_action": "O checkpoint de aquisição oficial foi promovido sem alteração para 71ef3afc489da146f839448b5366af4ab4dd2dce. A resolução factual em artifacts/bianchini/v2/checkpoints/P03-R5-c187-official-package-integrity-resolution.json confirma pelo catalogEntry NuGet V3 que dotnet-stryker 4.16.0, packageSize 46147078 e SHA-512 8d055c27ebd241a4a86fdcfe48505249b301c27b27080876ec93f65ef4c9d26b0a8f893af274c0f2d387f5757b4464f2d8e2135ef9483521c40b55a9d0263f82 correspondem ao pacote adquirido. O bloqueio de integridade está resolvido. P01 permanece blocked-terminal, P03 blocked, release pending, campaign_count=0, campaign_authorized=false e campaign_executed=false; U-008 não foi concedida nem consumida. Após o commit documental e a sincronização, qualquer novo preflight exige expected_revision == revision == HEAD == upstream no HEAD final, branch bm/v2-p03, árvore limpa e divergência 0/0. Só então uma decisão humana nova e explícita poderá avaliar U-008; nenhuma campanha é inferida."
}
