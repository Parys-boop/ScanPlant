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
      "history_path": "artifacts/bianchini/v1/planning/checker-p01-r1.jsonl",
      "package_digest": "05f6c60ca50b96a3d19d9fca72eae878bfc00e06a01045a62e19a3e46f794ddb",
      "report_digest": "2efb48dccece182d0ae709517b44fad1988f9252cba2355a2c6ebeb7fcfc7f8d"
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
    "approved_at": "2026-08-28T10:08:50-03:00",
    "approved_by": "supervisor",
    "approved_plans": [
      "P01",
      "P02"
    ],
    "package": {
      "algorithm": "sha256-manifest-v1",
      "manifest_path": "artifacts/bianchini/v1/approval/manifest.sha256",
      "manifest_digest": "187caa159699699e93373638dd07718630d8f1616dca6bbe29394eb4bfda976a",
      "files": [
        "docs/bianchini/changes/v1/inputs/APPROVED_SCOPE.md",
        "docs/bianchini/changes/v1/inputs/P01-MUTATION-GATE-AMENDMENT.md",
        "docs/bianchini/changes/v1/STACK_RESEARCH.md",
        "docs/bianchini/changes/v1/READINESS.md",
        "docs/bianchini/changes/v1/USER_ACTIONS.md",
        "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md",
        "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md",
        "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
        "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback-r1.md",
        "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md",
        "docs/bianchini/changes/v1/PLANNING_REVIEW.md"
      ]
    }
  },
  "plans": [
    {
      "id": "P01",
      "path": "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback-r1.md",
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
      "status": "blocked",
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
        "env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet test ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj --framework net8.0 --configuration Release",
        "env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet test ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj --framework net8.0 --configuration Release --filter FullyQualifiedName~ExternalFallback",
        "git diff --check"
      ],
      "status": "pending"
    },
    "plan": {
      "commands": [
        "env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet build ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj --framework net8.0 --configuration Release",
        "cd ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness && env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet tool run dotnet-stryker --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --mutate Services/ExternalProviders/ExternalFallbackUploadValidator.cs --mutate Services/ExternalProviders/ExternalFallbackService.cs --output /tmp/scanplant-p01r1-mutation",
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
  "blockers": [
    {
      "id": "B-P02-001",
      "summary": "P02 permanece bloqueado por depender da execução e do gate final do P01-R1 aprovado.",
      "evidence": "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"
    }
  ],
  "next_action": "Retomar exclusivamente P01-R1 no workspace existente, pela Tarefa 1 e sem iniciar P02."
}
