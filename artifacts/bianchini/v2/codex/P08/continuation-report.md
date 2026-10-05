# P08 continuation report

## Recovery

Method 3.2.0; skill and three ordered overlay contracts read. Existing workspace resumed, technical mode strict/per_task, one operational grouped round. No new worktree, index update, commit, push or historical source edit.

Checkpoint SHA-256: `9b26eadbde08c95badf8d5028c8531a3209d41b8fb51d2682a8a4bba0a367230`, exact expected bytes, identity and ledger matched. Original checkpoint remains immutable. Planning snapshot verified: `6724418360384c6a63300cffd9e8772fee7727a14bc39dd59c168460fb6c164a`. Branch `bm/v2-p08`, HEAD/baseline `24de252d27a137281c02cad50533280bb82dd80d`, ancestry satisfied, no upstream. Remote origin is the existing project GitHub repository; local origin/bm/v2-p08-planning matches baseline.

Eleven untracked files existed at recovery; exact paths and SHA-256 are in `resume-inventory.json`. No external P08 dataset existed. No active collector found in host process inspection before the round; dataset exclusive lock enforced. No recoverable prior mutation output or detailed independent reviewer report was present; the implementer report was a skeleton. Historical RED logs and mutation harness preserved. The recovered checkpoint records process state, not implementation hashes or test results.

## Review and corrections

1. Recovered tests exposed two failed assertions: HTTP 200 response bodies failing size checks or timing out were journaled as `ok`. Response outcome now records the actual error; transient body timeouts retry within cumulative quotas.
2. A failed media transfer could leave its source marked exhausted. Acquisition now records a retryable source failure, reuses the durable page on restart and does not reset quotas.
3. Durable finalization now requires the inspected candidate and attribution bundle to match hashes/source/author/license before approval; taxonomic and botanical evidence files remain SHA-bound. Tests cover missing/changed evidence, stale mapping/class/author decisions, final-manifest coverage and replay.
4. Unsupported media are retained as rejected-format metadata without transfer; an empty malformed Commons schema is rejected.
5. The real first reopened inspection exposed HTML field-order instability. Read-only reconstruction identified `review.html` as the sole differing projection. Sorted key rendering fixes it. An exact predecessor code fingerprint is accepted only with all other code/config/manifest fingerprints unchanged; a durable `code_compatibility` event records predecessor/current hashes. Original config and journal prefix were preserved. `bm change-policy --internal-order` classified this as bounded_amendment; the approved plan is unchanged.

The symptoms of the two earlier findings supplied in the handoff (transient resumption and human/taxonomic/manifest binding) have explicit regression coverage. Their original reviewer IDs/report were not recovered, so no independent-review approval is invented. Review in this continuation was inline against the frozen plan/spec. Current authority remains pending human acceptance.

## Proofs

- Final focused recovery: 51 passed; adapter: 15 passed.
- Final full historical/affected suite: 233 passed. Full-suite output and command/fingerprint manifests retained.
- Five selective mutations killed, no material survivor, fresh subprocesses, zero network calls. Initial continuation campaign is preserved; final campaign was necessary after the proven production-code change invalidated its byte fingerprint.
- Manifest/approved roster validation and SHA256SUMS passed. No unrelated release/.NET mutation campaign was run.
- Tests cover transport/SSRF, 403, 429/5xx/maxlag, date/seconds Retry-After, request/hour/media/transfer/page quotas, partial body counts, fsync errors, corrupt/truncated journal, symlinks/missing objects, five ingest crash boundaries, process concurrency, EXIF sanitization, original preservation, rights, taxonomy/human binding and dHash boundary comparisons against 17 synthetic prior references.
- Real acquire and inspect replay are byte+mtime stable after the HTML correction. Real comparison loaded all 17 historical images; no new media existed for pixel pairs. All 17 SHA-256 and mtimes match before/after; exact values in `real-round.json` and the external report.

## Real round

120 Commons metadata requests, 120 pages, 2,127,950 response bytes, zero failed responses/source failures. 1,090 unique class associations, 1,088 distinct media IDs, zero transferred/rejected, 1,088 pending. No original/sanitized P08 image hash exists: no image was downloaded. No new media-to-P07 perceptual pairs exist; this is not a claim of visual distinctness.

Commons database/source-rights clearance remains pending; individual media metadata alone was not promoted to legal clearance. No human authorship, privacy, botanical or dataset release decision was fabricated. iNaturalist: no approved human crosswalk, zero requests/transfers. All twelve species show `no_crosswalk`; two protections are unqueried on both sources. Eleven Commons queries hit the page budget, species_04 exhausted within its query. Per-class results are in `artifacts/phase1/p08/summary.json`; totals are not training sufficiency.

The private human-review JSON/HTML contains every candidate with stable ID, source URLs, declared authorship/license/attribution, evidence hash, absent-media-hash reason, proposed classes, taxonomy, quality/privacy/duplicate status, technical recommendation and pending human decision. Object-hash inventory explicitly records null original/sanitized hashes. There are 138 external files plus the empty lock; the verified private backup contains the same 138 files. Directories 0700/files 0600. The final dataset manifest SHA-256 is `334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716`.

## Guard and authority

`review_guard status` reports no P08 sidecar. Proof execution requires a committed revision and creates a new isolated worktree, both forbidden in this round. No fake proof_id, freeze, completed/stopped state, sidecar edit or method-state change was made. Therefore local tests/byte proofs passed, but formal guard completion and independent commit-bound review remain unavailable. Fix rounds/redesign: none recorded by guard; no claim of terminal completion.

Release pending, active execution state unchanged, current specs/P06/P07/P09 unchanged. Pending: real human per-item decisions (legitimate pending outcomes allowed), rights/qualified botanical/privacy review as applicable, U-804 acceptance of final bytes, and explicit future staging/commit/push authorization. No automatic publication. Suggested commit after acceptance: `feat(p08): add bounded traceable dataset recovery`.

## Audit and inventories

`resume-inventory.json` identifies every preexisting file; `final-files.sha256` inventories exact final changed/untracked Git bytes, excluding itself. Its own SHA-256 is the Git-delivery digest. `audit-final.json` records hygiene, diff checks, guard status and index state. The original checkpoint is preserved; `continuation-checkpoint.json` is newly emitted by the CLI. External filenames and all hashes are in private `final-manifest.json`; no raw source responses, item URLs, authors, images or review HTML were copied into Git.
