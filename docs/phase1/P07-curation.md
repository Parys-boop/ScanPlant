# P07 — curadoria rastreável, aguardando aceite humano

A execução existente foi retomada na worktree `/tmp/scanplant-p07-workspace`, branch `bm/v2-p07`, base `822954421019ad611d4d14dc5461cc7a495b7db4`. O planejamento continua congelado no digest `2968f4a7c7711d35c7396f0aa164fadda866aff01cb546ab9e40355f2471e2f3`.

As 17 fontes externas foram reconciliadas com P06, incluindo Q/R, classe candidata, SHA-256 e proveniência. Imagens e resultados integrais permanecem externos. Os 29 arquivos P06 continuam byte-iguais ao inventário inicial. Autoria, licença e origem permanecem nos resultados externos.

O resumo em `artifacts/phase1/p07/summary.json` é uma projeção de **propostas do agente**, sem decisão humana registrada. As três avaliações favoráveis antigas do P06 não foram promovidas. `usable=0`, `approved_for_dataset=0`, treinamento não autorizado e suficiência para treinamento não demonstrada.

| Estado proposto | Quantidade |
| --- | ---: |
| approved_for_dataset | 0 |
| rejected_quality | 2 |
| rejected_duplicate | 0 |
| rejected_privacy | 0 |
| rejected_label | 0 |
| needs_botanical_review | 8 |
| needs_human_review | 7 |

Há 136 comparações SHA/dHash horizontal 64 bits, sem sinal automático de duplicidade nos limiares aprovados. Distância mínima 21. Q01–Q02 e Q14–Q15 permanecem pares visuais pendentes, ambos com distância 35. Nenhum item foi rejeitado automaticamente.

As 14 classes seguem sem candidato aprovado. `species_04`, `species_08`, `outra_planta` e `imagem_invalida` não têm candidato adquirido. Ausência de aprovação ou classes vazias não invalida o processo de curadoria.

## Operação reproduzível

Dependência única: Pillow 12.3.0, com biblioteca padrão Python. Ambiente existente `/tmp/scanplant-p07-env`; nenhuma dependência adicional instalada na retomada.

```bash
/tmp/scanplant-p07-env/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'
/tmp/scanplant-p07-env/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
/tmp/scanplant-p07-env/bin/python -B artifacts/bianchini/v2/codex/P07/verify_working_tree.py --external
```

38 testes P07 e 162 testes afetados/históricos passaram. JSON estrito, métricas/fronteiras, SHA/dHash, colisões, pares manuais, barreira de aprovação humana, duplicatas, integridade, trava, escrita atômica e idempotência estão cobertos. A reexecução real de análise e rascunho preservou bytes e mtimes; a finalização humana foi testada somente com fixtures sintéticas.

O modo `--review-draft --decisions <arquivo>` permite preparar o resultado para aceite sem alegar decisão humana. `--finalize` recusa `authority=agent_proposal`. Os arquivos `.draft` são deliberados: U-701 ainda não foi consumida. As propostas persistidas e seus timestamps não foram reescritos.

Resultados integrais: `/home/administradorarthur/datasets/scanplant/p07-curation-20260928/`. Incluem `analysis.json`, `human-decisions.json` (conteúdo explicitamente marcado `agent_proposal`), `curation.draft.json`, `report.draft.md`, `summary.draft.json`, `source-before.json` e `verification.json`. Não copiar os relatórios integrais para o Git.

## Limites de fechamento

P07 permanece `in_progress`. U-701 requer confirmação dos 17 pareceres; U-702 requer aceite dos bytes finais. Avaliação do agente não constitui confirmação botânica pericial. Todos os arquivos físicos permanecem em quarentena.

A revisão formal do guard não foi executada: seu `proof` cria uma worktree a partir de um commit; a implementação permanece não commitada e a rodada proíbe nova worktree/staging/commit. As evidências registram hashes dos bytes de trabalho, não `proof_id` de um commit que não contém a implementação. Nenhum sidecar terminal foi fabricado. A revisão técnica local e os gates estão documentados em `artifacts/bianchini/v2/codex/P07/`.

P01–P06/P05-R1 e seus históricos foram preservados; `current_specs` não foi sincronizado. `release=pending`. P08 não iniciado. Não houve staging, commit, push, merge ou tag.
