# Readiness — P03-R5 contrato do MutationHarness

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "0e8e0c1402639df2535aadda658160887075e305c84bb5fc50bc5c6b9ddeec0f",
  "repository_revision": "144670031c7786829bf7e067c36df7332ddafc5f",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlantAPI"],
    "modules": ["P03-R5 MutationHarness preparation", "P03 frozen environment", "external-fallback evidence"],
    "contracts": ["harness project resolution", "offline artifact preparation", "phase-specific cwd equality", "revision binding"],
    "data": ["new sanitized R5 run-dir evidence only"],
    "platforms": ["ASP.NET Core .NET 8", "equivalent Linux/WSL hosts"]
  },
  "decisions": [
    {"id":"D-001","statement":"P01 permanece blocked-terminal.","evidence":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"D-002","statement":"P02 permanece completed.","evidence":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"D-009","statement":"P03-R5 is the minimal invalidating replan; P03-R4 remains blocked historical evidence.","evidence":"B-P03-R4-MUTATIONHARNESS-CWD-ARTIFACTS; change-policy result","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]},
    {"id":"D-010","statement":"The harness cwd is ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness and the final command names its local csproj.","evidence":"real csproj layout; P01 v3/v5 historical preflight contract","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]},
    {"id":"D-011","statement":"Restore offline and build are explicit preparation phases; final test remains no-build/no-restore.","evidence":"R4 blocker records missing assets; historical proof checks assets before final command","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]},
    {"id":"D-012","statement":"Common frozen environment is equal across phases; declared phase cwd values are compared by phase rather than forced equal.","evidence":"R4 environment equality and its cwd conflict; distinct real launcher/harness layouts","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]}
  ],
  "assumptions": [
    {"id":"A-001","impact":"high","status":"confirmed","statement":"P02 não depende da conclusão de P01.","evidence":"ledger P02","fallback":"preservar P02 completed","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"A-006","impact":"critical","status":"confirmed","statement":"A local package cache can satisfy the harness restore when all package sources are cleared.","evidence":"R4 NuGet.Config clears sources; NUGET_PACKAGES is frozen under host_home","fallback":"stop before preparation final gate and campaign; do not download","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]}
  ],
  "pitfalls": [
    {"id":"P-001","impact":"critical","statement":"P02 não pode ser reaberto por P03.","prevention":"preservar status P02","recovery":"manter P02 completed","verification":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"P-002","impact":"high","statement":"P01 não recebe waiver.","prevention":"preservar bloqueio","recovery":"manter P01 blocked-terminal","verification":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"P-011","impact":"critical","statement":"A harness final gate can be falsely weakened by implicit restore/build or an incorrect cwd.","prevention":"record preparation separately; use the real harness cwd and final no-build/no-restore command","recovery":"stop before campaign with campaign_count=0","verification":"per-phase lifecycle, artifact inventory and final 23/23 transcript","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]},
    {"id":"P-012","impact":"critical","statement":"Treating an expected phase-specific cwd as common-environment drift either rejects the valid graph or weakens equality.","prevention":"freeze common values once and freeze named cwd values before execution","recovery":"stop on unexpected cwd or common-value mismatch","verification":"environment-equality JSON distinguishes common and per-phase fields","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]},
    {"id":"P-013","impact":"critical","statement":"A new run may silently reuse R4 execution evidence or consume campaign authorization.","prevention":"require new R5 run-dir and explicit campaign prohibition","recovery":"stop with campaign_count=0","verification":"new evidence path, counter and user-action binding","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md","docs/bianchini/changes/v2/USER_ACTIONS-p03-r5.md"]}
  ],
  "user_actions": [
    {"id":"U-001","needed_by":"P02","statement":"A aprovação histórica de P02 é preservada.","fallback":"não reabrir P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"can_continue_without":false,"evidence_required":"ledger P02"},
    {"id":"U-007","needed_by":"P03","statement":"A human must approve the complete P03-R5 package before any non-consumer preflight, preparation, launcher or harness command.","fallback":"no execution; retain P01 blocked-terminal, P03-R4 historical blocked, P03-R5 planned and campaign_count=0","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r5.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"],"can_continue_without":false,"evidence_required":"human approval of the R5 package digest"},
    {"id":"U-008","needed_by":"P03","statement":"A separate later human authorization bound to the executable approved, committed, synchronized and clean HEAD is required for one campaign.","fallback":"do not start campaign after a passing harness","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r5.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"],"can_continue_without":true,"evidence_required":"explicit campaign authorization after all R5 non-consumer gates pass"}
  ],
  "spikes": [
    {"id":"S-001","status":"passed","statement":"P02 é independente do bloqueio de P01.","evidence":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"decision":"Preservar P02 completed."},
    {"id":"S-005","status":"passed","statement":"Repository and versioned evidence identify a resolvable isolated harness cwd and the required artifacts.","evidence":"ScanPlantAPI.MutationHarness.csproj; P01 v3/v5 preflight contracts; R4 blocker","destinations":["docs/bianchini/changes/v2/STACK_RESEARCH-p03-r5.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"],"decision":"Prepare and gate the harness in its own cwd."}
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {"id":"SD-001","statement":"P01/P02 mantêm contratos e estados históricos.","source":"docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md","target":"docs/bianchini/current/specs/replan-v2.md","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"SD-005","statement":"The accepted future gate separates offline preparation from final no-build/no-restore verification and freezes cwd by phase.","source":"docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","target":"docs/bianchini/current/specs/mutation-harness-gate.md","destinations":["docs/bianchini/changes/v2/spec-deltas/mutation-harness-gate-r5.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r5.md"]}
  ]
}
```
