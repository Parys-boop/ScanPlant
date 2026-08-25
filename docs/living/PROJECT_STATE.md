{
  "method_version": 2,
  "method_mode": "standalone-adaptive",
  "planning_version": "v1",
  "planning_status": "approved",
  "execution_policy": "adaptive",
  "assurance_profile": "standard",
  "architecture_audit": "optional",
  "architecture_audit_status": "not_run",
  "manual_pdf": "scope",
  "scope": {
    "status": "approved",
    "source": "docs/bianchini/changes/v1/inputs/APPROVED_SCOPE.md",
    "approved_at": null
  },
  "planning": {
    "quality_version": 2,
    "research_mode": "targeted_web",
    "research": "docs/bianchini/changes/v1/STACK_RESEARCH.md",
    "readiness": "docs/bianchini/changes/v1/READINESS.md",
    "user_actions": "docs/bianchini/changes/v1/USER_ACTIONS.md",
    "spec": "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md",
    "review": "docs/bianchini/changes/v1/PLANNING_REVIEW.md",
    "checker": {
      "status": "passed",
      "rounds": 2,
      "history_path": "artifacts/bianchini/v1/planning/checker.jsonl",
      "package_digest": "ba1dfda1f0a8b93cdccb841fd6718845d54beed6ba1c2bd8942aa1058f2e5ad9",
      "report_digest": "5abcb6cafd96a9677cebb7796b05bf703603be84e65e97338364e62a0f5b83fb"
    },
    "design_manifest": null,
    "change_root": "docs/bianchini/changes/v1",
    "current_specs": "docs/bianchini/current/specs"
  },
  "complexity_review": {
    "decision": "within_budget",
    "justification": null,
    "deferred_scope": [],
    "scope_split_approved": false,
    "scope_split_approved_by": null,
    "scope_split_approved_at": null
  },
  "approval": {
    "status": "approved",
    "approved_at": "2026-08-25T19:34:17-03:00",
    "approved_by": "solicitante autorizado",
    "approved_plans": [
      "P01",
      "P02"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v1/approval/manifest.sha256",
      "manifest_digest": "3098cd22058f478ed5ed8530452c4258b60b879a78106900baacb5f30e8b161f",
      "files": [
        "docs/bianchini/changes/v1/inputs/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v1/STACK_RESEARCH.md",
        "docs/bianchini/changes/v1/READINESS.md",
        "docs/bianchini/changes/v1/USER_ACTIONS.md",
        "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md",
        "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md",
        "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
        "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md",
        "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v1/PLANNING_REVIEW.md"
      ]
    }
  },
  "plans": [
    {
      "id": "P01",
      "path": "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md",
      "status": "approved",
      "risk": "high",
      "execution": "strict",
      "review": "per_task",
      "test_seams": [
        "external-fallback",
        "upload-validator",
        "provider-error-mapping"
      ],
      "depends_on": [],
      "ledger": "artifacts/bianchini/v1/ledgers/P01.md",
      "gates": [
        "compile",
        "unit",
        "integration",
        "security",
        "mutation-selective"
      ]
    },
    {
      "id": "P02",
      "path": "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md",
      "status": "approved",
      "risk": "medium",
      "execution": "slice",
      "review": "per_slice",
      "test_seams": [
        "mobile-consent-gate",
        "scanplant-api-client"
      ],
      "depends_on": [
        "P01"
      ],
      "ledger": "artifacts/bianchini/v1/ledgers/P02.md",
      "gates": [
        "focused-regression",
        "mobile-build"
      ]
    }
  ],
  "verification": {
    "fast": {
      "commands": [
        "dotnet test ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release --filter FullyQualifiedName~ExternalFallback",
        "git diff --check"
      ],
      "status": "pending"
    },
    "plan": {
      "commands": [
        "dotnet test ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release",
        "dotnet stryker --solution ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --project ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj",
        "git diff --check"
      ],
      "status": "pending"
    },
    "release": {
      "commands": [
        "dotnet build ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release",
        "dotnet test ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release",
        "npx expo export --platform android --output-dir /tmp/scanplant-f1-be01-export"
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
    "path": "artifacts/bianchini/v1/telemetry.jsonl"
  },
  "blockers": [],
  "next_action": "Resolver U-001; em seguida, criar e validar o workspace Bianchini fora da branch principal antes da execução."
}
