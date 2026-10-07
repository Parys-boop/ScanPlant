# Implementer Report — P08 B1, round 1

- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md`
- Status: TECHNICAL_FIX_READY_FOR_REVIEW; acceptance and commit pending.

## Changes

The preexisting fix in acquire_inat preserves str(error) only when error is RecoveryError and its code already belongs to RETRYABLE. All other caught errors retain inaturalist_contract_or_evidence. RETRYABLE itself is unchanged. The previous unconditional classification made a transient metadata timeout permanently skipped on restart by acquire.
Three existing synthetic tests cover timeout/restart/success, preserved journal prefix and config, cumulative request quotas, no premature page/cursor or candidate, one candidate exactly once, stable subsequent invocation, and fail-closed classification of contract/integrity/budget failures.

## Verification

Reused signed RED proof-6928ea925e6f438e3873543389326106 on original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 only as historical defect evidence. Additional RED ran the three new tests against original production bytes (12 failed assertions). Reconciled current source/output fingerprints for GREEN: 3 new tests, 54 recovery, 15 adapter, 236 affected/history tests with five materially reached/killed selective mutants. These are working-byte records, not proofs for a future SHA. No test suite rerun during this resumption.
Fresh read-only Method preflight, diff check, complete evidence hash reconciliation and external bytes/mtime comparison passed. All unchanged suite dependencies match original HEAD; both modified files match the previous GREEN records. No network acquisition or downloads. See evidence-reconciliation.json.

## Decisions

Reuse round 1, existing correction, original commit and all documentary recovery. implementation_detail decision already recorded by bm change-policy. No start/red/fix command repeated. No staging, commit or push. The official review-package for base=head is an empty committed delta; its explicitly labeled working-tree annex enables technical review only. Formal submit-delta/review and fresh gates must wait for a separately authorized own commit.

## Concerns

Guard stays fixing, B1 open, round 1, redesign 0. P08 remains blocked, release pending. Historical human acceptance does not accept new bytes. External config/code fingerprint and old receipts remain intact and must not be silently migrated; new code is not authorized against the real dataset. 1088 pending candidates, zero transfers/approved_for_dataset/usable, no real iNaturalist crosswalk, no training, no P09.
