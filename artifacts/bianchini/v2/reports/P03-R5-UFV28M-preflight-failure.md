# P03-R5 — checkpoint factual do preflight UFV28M

## Resultado

O preflight manual não mutacional executado no WSL normal falhou somente na validação posterior ao teste do MutationHarness. O run-dir factual é `artifacts/bianchini/v2/evidence/P03-p01-mutation-r5/preflight-run-UFV28M/`; ele é preservado sem qualquer alteração.

## Binding e preflights aprovados

- `expected_revision`, `revision`, `HEAD` e `upstream_revision`: `cfbfb6f67b0f45f11b06aab55716139f3cc89dfe`; branch `bm/v2-p03`; behind/ahead `0/0`; árvore inicial vazia.
- Loopback IPv4: `127.0.0.1/8`; IPv6: `::1/128`.
- `/usr/bin/rg` no PATH sanitizado: `ripgrep 15.1.0`; SDK `8.0.424`; ambos os runtimes exigidos `8.0.30`.
- `tool restore` e `tool list` passaram; `dotnet-stryker 4.16.0` foi resolvido. A única invocação relativa ao Stryker foi `dotnet tool run dotnet-stryker -- --help`, exit `0`, sem campanha.
- Restore offline, build `net8.0 --no-restore` e teste final `--no-build --no-restore` do MutationHarness passaram. O gate final registrou Failed `0`, Passed `23`, Skipped `0`, Total `23`.

## Falha e limites

Depois do teste, o launcher original executou `/usr/bin/rg -Eq` para validar literalmente o resumo. Em ripgrep `15.1.0`, `-E` é `--encoding`; portanto `q` foi tratado como encoding e gerou `unknown encoding: q`. A fase final é `failed` e o exit final é `95`; isto não invalida o resultado 23/23 do harness.

`campaign_count` ficou em `0`; `campaign_authorized=false` e `campaign_executed=false`. Não há `mutation-report.json`, diretório `results/`, `reports/` ou resultado de campanha. U-008 não foi concedida nem consumida. Nenhuma campanha, retry, Stryker mutacional, alteração funcional ou alteração do MutationHarness ocorreu.

O manifesto de checksums do run-dir foi verificado com 232 entradas `OK`. A allowlist correspondente exclui caches, binários, pipes, certificado transitório e demais conteúdo de `home/`, `cli-home/` e `tmp/` do índice Git.
