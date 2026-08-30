# P01 manual final Stryker evidence (v5)

This directory preserves the manually produced foreground v5 campaign copied
from `/tmp/scanplant-p01-manual-final-v5-LXMhgoKW`. `SHA256SUMS` is the
original complete manifest; it also names transient tool logs deliberately not
retained here. `SHA256SUMS.preserved` covers every retained file except itself.

- Script: `scanplant-p01-manual-final-v5.sh`, SHA-256
  `d0b685df7960db9dad0d8c661a834e686ebb8c09e42132731eaa840bfa4736e6`.
- Raw report: `results/reports/mutation-report.json`, SHA-256
  `f83599193c98fa8c588e07d8e6b73364eb04c43f6fcfcc36d8d9f562115463f8`.
- Execution: 2026-08-30T17:35:31Z through 2026-08-30T17:37:51Z (140 seconds),
  with preflight, Stryker, scope validation, and wrapper exit codes all 0;
  final phase `scope_validated`.
- The validated configuration contains exactly the two authorized mutate paths.
  The isolated MutationHarness preflight passed 23/23. The raw report records
  66 killed, 12 survived, 2 timeouts, 0 runtime errors, and an 80.00% score.
- `mutation-report.normalized.json` is the deterministic projection of the 85
  effective mutants. It omits only 18 CompileError and 187 Ignored entries;
  classifications are retained for the 17 survived/NoCoverage mutants. The
  two Timeout mutants are accepted as killed by the verifier's status mapping.

This is preservation only. It does not alter P01's blocked-terminal status;
v3 remains preserved as historical/superseded evidence.
