# Implementer Report — P05-R1 / T1

- Brief: `artifacts/bianchini/v2/codex/P05-R1/task-brief.md`
- Status: IMPLEMENTED_WORKING_TREE; pending final human bytes acceptance.
- Approval commit: `c7012b942c36fe93fb136a376a1a73093f1e5aaa` (planning/approval only).

## Changes

Removed exactly four authorless homonyms from synonyms; manifest_version 1.1.0.
The scientific map rejects normalized quarantined names with E_NAME_QUARANTINED.
A valid manifest resolves the four to None. Schema/normalization/roster, all class
identities, IDs/order/common names/protections and other aliases remain unchanged.
Updated taxonomy evidence, F1-MAN01 docs, report and seven-file checksum seal.
Frozen applicable spec/delta already define the rule and remain byte-identical.
The current-spec target is reserved for cycle close as explicitly planned, not this gate.

## Verification

Python 3.14.4 -B, stdlib only; historical evidence used 3.12.3. RED baseline proof:
proof-93c13d6b0c1affb7122f227180990597, exit 1 at approval commit. Expanded pre-fix suite
ran 92 tests with 91 failing assertions/subtests; no production integration exercised.
Final GREEN: 94 tests, zero failures/errors/skips; 81 prior tests plus 13 new tests.
Exact baseline set/mapping equality: 83 minus the four quarantined = 79 aliases;
12 canonicals remain, 91 unique scientific keys. Reintroduction tested in all 12
species and through normalized alias/canonical paths. Authorship is never stripped.
CLI, strict JSON/JSONL, snapshots, state, audit and checksums passed.
Read validation-report.json and FINAL_REVIEW.md for actual commands, hashes and limits.

## Decisions

One fix round in the same T1 sidecar, zero redesigns and no deferred hardening.
Known-homonym exclusion is a small normalized set in the existing validator; evidence
retains authorship and conflicts separately without changing manifest schema.
bm change-policy with no flags: implementation_detail; with --plan-command for
postponing commit-bound proof: bounded_amendment, no invalidation/reapproval.
User instruction forbids implementation staging/commit before the final gate.
Therefore guard remains fixing with B1 formally open against baseline; B1 is corrected
and verified in the hashed working tree. Do not fake submit-delta, green commit proofs,
review or complete. After authorization, submit the actual commit and recheck its proofs
in this same sidecar; this is not a new plan or another implementation round.
The one-task grouped brief is emitted by bm as kind task (one unit digest), not group;
preserve the official digest without inventing another task/group.

## Concerns and final boundary

No unresolved implementation defect found in final local review. Human acceptance
of final bytes and permission for commit/push are pending. P05 blocked, P05-R1 in_progress,
U-201 open only for final bytes acceptance; prior plans and release preserved.
No push, merge, product integration, provider, credential use, taxonomy network,
installation, runtime stack, mutation campaign, old-worktree or external-backup edit.
