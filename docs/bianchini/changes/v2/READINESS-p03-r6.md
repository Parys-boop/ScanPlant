# Readiness — P03-R6 isolamento do projeto de testes

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "81ac538262610a14fe9fa0941ccbe45d96bf10362f598c82d8f0cd4e013e26db",
  "repository_revision": "716ef26c8621251a1851b4b44f08dbb60c66e45c",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlantAPI"],
    "modules": ["P03 campaign launcher", "temporary net8-only solution context", "MutationHarness"],
    "contracts": ["explicit test-project selection", "isolated solution membership", "U-009 single-use accounting", "future documentary-HEAD binding"],
    "data": ["new R6 temporary run-dir evidence only", "preserved R5 terminal attempt"],
    "platforms": ["WSL normal", "ASP.NET Core .NET 8"]
  },
  "decisions": [
    {"id":"D-001","statement":"P01 permanece blocked-terminal e não é reaberto por R6.","evidence":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"D-002","statement":"P02 permanece completed e independente de P03.","evidence":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"D-013","statement":"P03-R5/U-008 is immutable terminal evidence: campaign_count is 1, U-008 is consumed, and no mutant/report exists.","evidence":"/tmp/p03-r5-u007.h8rfIr/u008-campaign-started/campaign-count; u008-campaign-results/log","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md","artifacts/bianchini/v2/checkpoints/P03-R5-U008-terminal-attempt-716ef26.json"]},
    {"id":"D-014","statement":"The only future test project is ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj targeting net8.0.","evidence":"MutationHarness csproj and R5 host-completion 23/23","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]},
    {"id":"D-015","statement":"A generated run-dir-local solution with exactly API plus harness replaces automatic discovery of the versioned solution for R6 campaign context.","evidence":"R5 log proves ScanPlantAPI.sln selected ScanPlantAPI.Tests.csproj and NETSDK1045","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]},
    {"id":"D-016","statement":"R6 is a material-change replan of execution configuration only; source, csproj, TargetFrameworks, SDK, Stryker, targets, reporters and thresholds remain frozen.","evidence":"bm.py change-policy result; R5 terminal log","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]}
  ],
  "assumptions": [
    {"id":"A-001","impact":"high","status":"confirmed","statement":"P02 não depende da conclusão de P01/P03.","evidence":"ledger P02","fallback":"preservar P02 completed","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"A-007","impact":"critical","status":"confirmed","statement":"The approved isolated feed/cache, Stryker 4.16.0 and SDK 8.0.424 remain available without acquisition, integrity resolution or global-cache writes.","evidence":"R5 package inventory of 79 packages and official integrity checkpoint","fallback":"stop before corrective preflight; do not download, refresh inventory or substitute a toolchain","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]}
  ],
  "pitfalls": [
    {"id":"P-001","impact":"critical","statement":"P02 não pode ser reaberto pelo replanejamento P03.","prevention":"preservar status P02","recovery":"manter P02 completed","verification":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"P-002","impact":"high","statement":"P01 não recebe waiver por uma campanha R6.","prevention":"preservar bloqueio terminal","recovery":"manter P01 blocked-terminal","verification":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"P-014","impact":"critical","statement":"An empty TestProjects list can select the multi-target project and invalidate SDK 8 execution before mutation.","prevention":"require explicit harness path and reject any multi-target project before build","recovery":"stop preflight with campaign_count=1 and do not invoke Stryker","verification":"launcher/config parse and temporary-solution member audit","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]},
    {"id":"P-015","impact":"critical","statement":"A solution-context build can reintroduce ScanPlantAPI.sln even when a test project is explicit.","prevention":"pass only the generated two-member net8 solution and verify its exact members before build/campaign","recovery":"stop before U-009 with campaign_count=1","verification":"temporary solution text/hash plus build transcript showing no net10.0","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]},
    {"id":"P-016","impact":"critical","statement":"U-008 cannot be reused and a new campaign must not reset the accumulated count.","prevention":"U-009 is separately approved after preflight and launcher permits only atomic 1 -> 2","recovery":"existing or invalid marker stops without a new invocation","verification":"state transition evidence and launcher guard","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md","docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md"]},
    {"id":"P-017","impact":"high","statement":"The Codex sandbox blocks VSTest local sockets despite valid loopback.","prevention":"run targeted preflight only in WSL normal","recovery":"do not interpret sandbox SocketException as product/test failure or retry there","verification":"WSL transcript records executor and 23/23","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]}
  ],
  "user_actions": [
    {"id":"U-001","needed_by":"P02","statement":"A aprovação histórica de P02 é preservada.","fallback":"não reabrir P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"can_continue_without":false,"evidence_required":"ledger P02"},
    {"id":"U-009","needed_by":"P03","statement":"After the R6 corrective preflight passes against the final documentary commit, a human may authorize exactly one new campaign with the explicit harness and isolated net8 context.","fallback":"do not create the 1 -> 2 marker or invoke Stryker; retain campaign_count=1","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"],"can_continue_without":true,"evidence_required":"separate explicit authorization after passing R6 preflight and final documentary-HEAD binding"}
  ],
  "spikes": [
    {"id":"S-001","status":"passed","statement":"P02 é independente do bloqueio de P01/P03.","evidence":"ledger P02","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"decision":"Preservar P02 completed."},
    {"id":"S-006","status":"passed","statement":"The terminal R5 log identifies the exact failing graph and the harness graph is locally distinguishable without modifying projects.","evidence":"/tmp/p03-r5-u007.h8rfIr/u008-campaign-results/logs/log-20260908.txt; csproj and solution inspection","destinations":["docs/bianchini/changes/v2/STACK_RESEARCH-p03-r6.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"],"decision":"Use explicit harness selection plus a generated two-member solution."}
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {"id":"SD-001","statement":"P01/P02 mantêm contratos e estados históricos.","source":"docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md","target":"docs/bianchini/current/specs/replan-v2.md","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"SD-006","statement":"The accepted future campaign contract binds one net8 harness and one run-dir-local two-member solution, with U-009 and a monotonic 1 -> 2 counter.","source":"docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md","target":"docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md","destinations":["docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"]}
  ]
}
```
