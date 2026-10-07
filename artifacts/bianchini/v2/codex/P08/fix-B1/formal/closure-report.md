# P08 — B1 formally resolved; plan closure pending

Accepted correction commit: dd595a6d652c27773849003b0fc2c0ec1d8d3ad4. Original commit 7981377a433270c9e2072fcafdf89b690988fa08 is unchanged. Exactly the accepted 76 paths were committed. Receipt is post-acceptance and outside the accepted manifest. The accepted manifest describes correction-commit bytes; later authorized state/ledger/guard updates do not rewrite that historical manifest.

B1 resolution proof proof-3f1d97fec3f4815a6b61620c9825b2f8 ran exactly the historical RED argv/cwd and passed on dd595a6d652c27773849003b0fc2c0ec1d8d3ad4. Independent formal review resolved B1 after submit-delta --kind fix. Round 1, no redesign or extra fix. Guard is review_frozen, next_action approve, with zero open code blockers. approve is not completed: one mandatory gate failed.

All 19 gates are bound to dd595a6d652c27773849003b0fc2c0ec1d8d3ad4: 18 passed and human-botanical-privacy-review failed (proof proof-2f87449a54b378d54f97243c6d1e5470). 54 recovery, 15 adapter, 236 affected tests passed, including five killed selective mutations. Tests were run once on the correction SHA; documentation does not claim proofs on its own later commit SHA. Full command/cwd/time/result/stdout/stderr hashes and IDs are in proof-results.json and plan-proof-map.json.

Closure is unavailable because the approved brief requires final human opinions per candidate, including legitimate pending outcomes. The gate found 0 such opinions and 1088 blank template entries. The old receipt explicitly records U-803 candidate_opinions_pending; the new receipt accepts B1 bytes only and does not replace missing data decisions. Zero approvals are allowed; absent required opinions are not represented as completed review. P08 remains blocked. No fake botanical, licensing, privacy or dataset approval.

Dataset and backup preserved byte-for-byte and mtime-for-mtime; 1088 pending, zero transfers, approved_for_dataset=0, usable=0. iNaturalist no_crosswalk; training unauthorized; release pending; P09 not started. New code verified the external journal read-only and explicitly distinguished the recorded historical runtime fingerprint from the correction fingerprint; no config/journal migration or acquisition was performed.

The Method 3.2.0 release proof-map command requires release.candidate. Its refusal is recorded in proof-map-command.json. plan-proof-map.json is only a signed-proof projection for this plan; no release candidate was invented. No complete/stop transition or second fix round was invoked.

Original RED logs and all accepted historical artifacts are preserved. Guard canonical files were changed only through guard commands. Active .bak files reflect that official lifecycle; pre-acceptance backups and original RED outputs are also archived in local-preserved/, untracked. external-before.json and the proof lock remain untracked. No local archive is proposed for publication.

Publication is not authorized and this branch is not ready to be represented as a completed P08. publication-inventory.txt lists the exact proposed Git paths since the P08 base (including the original implementation); documentation-commit-inventory.txt lists this documentary commit only. There is no upstream set or cached origin/bm/v2-p08 ref; remote state was not queried. No push, merge, PR or tag.

Future completion requires the missing human opinions and a renewed check of all applicable gates/acceptances on the actual closure revision. This turn authorizes no real dataset edits to obtain those opinions. Do not re-use correction proofs as if their commit were a future closure SHA.
