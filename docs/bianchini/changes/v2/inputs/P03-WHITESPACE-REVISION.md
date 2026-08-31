# Revisão formal P03-R1 — correção documental pré-publicação

## Fato verificado

O pacote P03 anteriormente aprovado foi invalidado antes de publicação porque `git diff --cached --check` encontrou cinco trailing whitespaces nas linhas 9–13 de `docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence.md`. A correção removeu exclusivamente esses cinco sufixos de whitespace; a comparação pré/pós não contém mudança de texto, escopo, contrato, policy, seam, mutate paths, versões, concorrência ou regra de parada.

## Rastreabilidade

- pacote/aprovação invalidado: `84d1178b1ea1ac72c93e9770bba5a56cce74499f1994685278714cc7cf4d3d07`;
- checker original preservado: `artifacts/bianchini/v2/planning/checker.jsonl`, duas passagens `passed`, digest de entrada `e7e1e4706efaecff92b2ee76cddfa4a771c99a69cbe3332857908576784b712d`;
- plano de origem: `docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence.md`;
- plano revisado: `docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r1.md`.

## Limite da revisão

P03-R1 substitui somente o artefato documental de P03 no pacote de planejamento. Continua exigindo Stryker `4.16.0`, `net8.0`, concorrência `1`, policy `required_selective`, seam `external-fallback`, exatamente os dois mutate paths existentes e uma única campanha seletiva quando houver autorização própria. Esta revisão não autoriza execução, Stryker, alteração de código, testes, MutationHarness, filtros, thresholds, runtime, RC, fingerprint, proof-map ou carry-forward.

## Aprovação necessária

O snapshot de P03-R1 requer uma nova aprovação humana única antes de qualquer execução. Esta revisão não registra essa aprovação.
