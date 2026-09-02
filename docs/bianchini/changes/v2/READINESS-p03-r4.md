# Readiness — P03-R4 portabilidade ambiental

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "5e7f13cced308ac5112b1e03992d507521eb4fec34528c67532949871045e947",
  "repository_revision": "48a8da64926063048c9e736795298589e0b2625b",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlantAPI"],
    "modules": ["P03 launcher contract", "sanitized environment manifest", "MutationHarness preflight", "external-fallback evidence"],
    "contracts": ["host-home resource resolution", "frozen material environment equality", "P03 revision binding"],
    "data": ["ephemeral run-dir manifest and future evidence only"],
    "platforms": ["ASP.NET Core .NET 8", "equivalent Linux/WSL hosts"]
  },
  "decisions": [
    {"id":"D-001","statement":"P01 permanece blocked-terminal; P03-R4 não reabre produto nem o contrato histórico de observabilidade.","evidence":"artifacts/bianchini/v2/ledgers/P01.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"D-002","statement":"P02 permanece completed e separado deste replanejamento ambiental.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"D-006","statement":"P03-R4 is a minimum versioned replan after material external impossibility; v2 remains the planning version and P03-R3 is preserved immutable.","evidence":"bm.py change-policy --external-impossibility --critical-invariant; P03-R3 approved package digest 3913a...","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]},
    {"id":"D-007","statement":"host_home is captured before sanitization; resolved external paths derive only from host_home and are frozen per run-dir.","evidence":"confirmed host facts in P03-R4 approved scope; P03-R3 rigid literals","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]},
    {"id":"D-008","statement":"HOME sanitizado, DOTNET_CLI_HOME and TMPDIR remain run-dir-local and are never inputs to resolve external toolchain/cache resources.","evidence":"P03-R3 sanitized-environment contract","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]}
  ],
  "assumptions": [
    {"id":"A-001","impact":"high","status":"confirmed","statement":"Os contratos funcionais P01/P02 não mudam com a portabilidade ambiental P03-R4.","evidence":"ledgers P01/P02 e escopo aprovado P03-R4","fallback":"manter P01 blocked-terminal e P02 completed","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"A-005","impact":"critical","status":"confirmed","statement":"Equivalent hosts expose the required SDK/runtime/tool package under the declared host-home-derived locations before execution.","evidence":"current host diagnosis: SDK 8.0.424, runtimes 8.0.30 and dotnet-stryker 4.16.0 local under /home/administradorarthur; no download used","fallback":"stop before preflight with campaign_count=0; do not download, install, copy, symlink or select another toolchain","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]}
  ],
  "pitfalls": [
    {"id":"P-001","impact":"critical","statement":"P02 não pode inferir aprovação de P01 nem ser reaberto por P03-R4.","prevention":"preservar P02 completed e limitar P03-R4 ao contrato ambiental","recovery":"manter P01 blocked e P02 completed","verification":"planning audit e ledger P02","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"P-002","impact":"high","statement":"A pendência de observabilidade não recebe waiver ou carry-forward.","prevention":"preservar P01 blocked-terminal até evidence verificável","recovery":"bloquear P01","verification":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"P-008","impact":"critical","statement":"Resolving from sanitized HOME would target run-dir/home rather than the host resources and invalidates portability.","prevention":"capture and validate host_home before assigning HOME=<run-dir>/home; record both separately","recovery":"stop before restore/launcher/harness/campaign with campaign_count=0","verification":"frozen environment manifest proves source and final values","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]},
    {"id":"P-009","impact":"critical","statement":"Allowing a value resolved in one phase to differ in another weakens the environmental proof.","prevention":"compare frozen values and run-dir byte-for-byte across restore, launcher, harness and campaign","recovery":"stop before campaign with campaign_count=0","verification":"per-phase manifest comparison","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]},
    {"id":"P-010","impact":"critical","statement":"A workaround by symlink, copy, download, automatic installation, or fallback dotnet would mask missing prerequisites.","prevention":"reject these operations and validate local paths/version identity before execution","recovery":"stop before any preflight with campaign_count=0","verification":"preflight evidence and command/source audit","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]}
  ],
  "user_actions": [
    {"id":"U-001","needed_by":"P02","statement":"A aprovação histórica P02 é preservada e não cria autorização nova.","fallback":"manter P02 completed e não reabrir escopo","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r4.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"can_continue_without":false,"evidence_required":"registro histórico de aprovação P02"},
    {"id":"U-006","needed_by":"P03","statement":"Approve P03-R4 only for preflights, then separately authorize one campaign against the executable HEAD.","fallback":"do not execute preflight or campaign; retain P01 blocked-terminal, P03-R4 pending/blocked and release pending","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r4.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"],"can_continue_without":false,"evidence_required":"P03-R4 digest approval, then separate campaign authorization bound to executable HEAD"}
  ],
  "spikes": [
    {"id":"S-001","status":"passed","statement":"P02 é tecnicamente independente do encerramento de observabilidade P01.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"decision":"Preservar P02 completed."},
    {"id":"S-004","status":"passed","statement":"The issue is contract portability rather than component absence: required versions exist under this host's natural home.","evidence":"confirmed current-host diagnostic supplied in approved scope; no download was required","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"],"decision":"Resolve from host_home and freeze values per execution, rather than changing a username literal."}
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {"id":"SD-001","statement":"P01/P02 preservam seus estados e contratos separados.","source":"docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md","target":"docs/bianchini/current/specs/replan-v2.md","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"SD-004","statement":"The next launcher-gate contract resolves host resources portably while retaining frozen environmental equality.","source":"docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","target":"docs/bianchini/current/specs/mutation-launcher-gate.md","destinations":["docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r4.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r4.md"]}
  ]
}
```
