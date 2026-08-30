# P01 manual final Stryker evidence (v3)

This directory preserves the manually produced, foreground Stryker lifecycle
evidence that closed the former observability gap. It was copied from
`/tmp/scanplant-p01-manual-final-v3-MJ0S6RnY` after its original `SHA256SUMS`
validated with exit code 0. `SHA256SUMS` is the original complete manifest,
including the transient `tmp/` tool cache that is deliberately not retained.
`SHA256SUMS.preserved` covers every retained file in this directory except
itself.

- Script: `scanplant-p01-manual-final-v3.sh`, SHA-256
  `9474144e5f41fc072e8a9abbdc677af36bb29ff6c24d0ab4f48b1cc238946cad`.
- Raw report: `results/reports/mutation-report.json`, SHA-256
  `a3bdaf66a15dcf455e2eeaff95fc9da0c5dd9b354e01fb2d33000cd59059351b`.
- Execution: 2026-08-30T16:59:52Z through 2026-08-30T17:02:15Z (143 seconds),
  with preflight, Stryker, and wrapper exit codes all 0; final phase
  `stryker_finished`.
- The command has exactly the two authorized `--mutate` paths. Preflight ran
  the isolated MutationHarness (23/23). The raw report records 66 killed,
  12 survived, 2 timeouts, 0 runtime errors, and an 80.00% mutation score.

`mutation-report.normalized.json` is the canonical projection used by the
official verifier: it retains the 85 selected material mutants and excludes
the 18 compile-error and 187 ignored entries, exactly as the preceding
canonical P01 evidence did. A direct ID/status/mutator/location comparison
with the historical raw report is identical; only lifecycle metadata and the
raw-report hash differ.
