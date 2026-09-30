# Task Brief 1

- Plan: `docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md`
- Plan SHA-256: `8aee1fb59866c780b45f955b7123ed124e02274b9ac9c620068fffe61554594f`
- Kind: `task`
- Group ID: `n/a`
- Group SHA-256: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`
- Unit `1` SHA-256: `86cac93eb8421c461b9a74c4086f067090a86900eb427a86fc3480d63a8fdf04`

### Tarefa 1 — 17 análises reconciliadas, pareceres humanos e relatório rastreável

**Execution:** slice

**Review:** per_slice

**Change:** workflow

**Readiness refs:** D-701, D-702, D-703, D-704, A-701, A-702, P-701, P-702, P-703, U-701, U-702, U-703, S-701, SD-701

**Test seams:** `curate_p07` CLI de leitura/análise/finalização; parser estrito de `state.json`/manifesto/decisões; reconciliação Q/R/SHA/class_id; métricas de luminância/nitidez; dHash/Hamming 136 pares; transição análise→parecer→estado; projeção sanitizada e reexecução idempotente.

**Spec refs:** `docs/bianchini/changes/v2/specs/p07-curation-change.md#entradas-identidade-e-integridade`, `#análise-técnica-determinística`, `#estados-e-autoridade`, `#saídas-concorrência-e-idempotência`, `#gate-e-aceite`; `docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md#análise-e-duplicidade`, `#revisão-estados-e-prova`, `#persistência-e-visibilidade`. D-702, D-703, SD-701.

**Files:** criar futuramente `scripts/phase1/curate_p07.py`, `scripts/phase1/test_curate_p07.py`, `artifacts/phase1/p07/summary.json`, `docs/phase1/P07-curation.md`, `artifacts/bianchini/v2/ledgers/P07.md` (append-only após criação). Atualizar minimamente `docs/living/PROJECT_STATE.md` no gate, mantendo todos os estados anteriores, e a cronologia de `docs/PLANO_CANONICO_IA_HIBRIDA.md` já incluída no pacote de planejamento. Resultados integrais futuros ficam **fora do Git** em diretório novo separado do P06: `analysis.json`, `human-decisions.json`, `curation.json`, `report.md`. Não alterar `scripts/phase1/acquire_commons.py`, manifesto P05, P06, planos/ledgers/evidências antigos, imagens, `current_specs` ou aplicações. D-704, P-701, P-703.

**Contract:** com acesso U-703, verificar fontes externas em leitura, conjunto exato de 17 aceitos e decisões Q01–Q17/R01–R17, SHA-256 e versões. Falha bloqueia sem saída final nem substituição. Gerar análise determinística para todos: decodificação, dimensões, razão, luminância/exposição, variância Laplaciana e flags nos limiares congelados; comparar 136 pares por SHA/dHash 64/Hamming. Testes sintéticos fixam cálculo e fronteiras; flags apenas sinalizam. Revisar em resolução original os critérios humanos de enquadramento, oclusão, múltiplas espécies, representatividade, privacidade e rótulo botânico. U-701 produz 17 pareceres, inclusive pendências legítimas, com responsável/timestamp/justificativa/evidência. Finalizar somente após validar que nenhum `approved_for_dataset` veio de algoritmo ou de decisão P06, que toda rejeição humana tem motivo e que todos os pares sinalizados foram resolvidos ou explicitamente mantidos pendentes. Preservar bytes P06 e atribuição/licença/origem; saída externa atômica e idempotente. Resumo Git usa allowlist de campos sem PII; relatório expõe zero aprovação e classes vazias como resultados válidos, nunca suficiência de treino. U-702 aceita hashes finais antes de commit/push. P-701, P-702, P-703, A-701, A-702.

**Verification:** no cwd raiz do workspace aprovado, com Python do ambiente isolado Pillow 12.3.0 disponível na execução: `python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'` e `python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'`, exit 0; `python -B scripts/phase1/curate_p07.py --source /home/administradorarthur/datasets/scanplant/p06-recovery-20260928 --output /home/administradorarthur/datasets/scanplant/p07-curation-20260928 --analyze-only`, exit 0 após U-703; depois de U-701, mesma CLI com `--finalize --decisions /home/administradorarthur/datasets/scanplant/p07-curation-20260928/human-decisions.json`, exit 0 e reexecução byte-idêntica. Validar `python -B -m json.tool artifacts/phase1/p07/summary.json`, `python3 -B /home/administradorarthur/.agents/skills/_shared/scripts/bm.py validate-state docs/living/PROJECT_STATE.md`, `python3 -B /home/administradorarthur/.agents/skills/_shared/scripts/bm.py snapshot verify docs/living/PROJECT_STATE.md --root .`, `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS`, `git diff --check` e inspeção dos arquivos Git alterados contra segredos/PII/binários. `SHA256SUMS` externo P06 e os 17 hashes são conferidos antes/depois; comparar os bytes dos manifestos/snapshots históricos ao HEAD, sem exigir que um manifesto antigo recalcule arquivos vivos intencionalmente atualizados. Nenhum comando de produto, mutação, release ou rede de aquisição.

**Done when:** 17/17 fontes reconciliadas e byte-iguais antes/depois; 17/17 análises e pareceres humanos vinculados, 136 pares calculados, JSON estrito, relatório externo e resumo Git coerentes, estados válidos com justificativas, nenhum dado pessoal/imagem no Git, reexecução idempotente, testes/gates aprovados e U-702 registra aceite explícito dos bytes finais. Zero `approved_for_dataset`, pendências botânicas e classes vazias são permitidos. Ausência de U-701/U-702 ou integridade divergente mantém P07 não concluído; nenhuma promoção, commit, push ou reabertura histórica é inferida.
