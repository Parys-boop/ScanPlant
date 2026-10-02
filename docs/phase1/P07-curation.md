# P07 — curadoria rastreável concluída localmente

Implementação: `a2dfd8805527e6323334fcc0a7b7f45c63c7d3c9`, na branch `bm/v2-p07`. Worktree persistente: `/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p07`.

U-701 e U-702 foram aceitas explicitamente no digest `b93852dfb4feef58050ed85fa4205838830a9cd9f660661e8857be80f4427c9e`. O manifesto desse digest permanece como snapshot dos bytes aceitos em a2dfd88; os registros antigos de pendência são históricos. O recibo vigente está em `artifacts/bianchini/v2/codex/P07/human-acceptance.json`.

| Estado humano aceito | Quantidade |
| --- | ---: |
| approved_for_dataset | 0 |
| rejected_quality | 2 |
| rejected_duplicate | 0 |
| rejected_privacy | 0 |
| rejected_label | 0 |
| needs_botanical_review | 8 |
| needs_human_review | 7 |

`usable=0`; treinamento não autorizado; suficiência não demonstrada. Aceitar os pareceres não constitui perícia botânica nem aprovação de imagens. As 14 classes continuam sem candidato aprovado. `species_04`, `species_08`, `outra_planta` e `imagem_invalida` não têm candidato adquirido.

136 pares SHA/dHash horizontal de 64 bits, menor distância 21 e zero sinais automáticos de duplicidade. Q01–Q02 e Q14–Q15 continuam como possíveis redundâncias visuais pendentes, ambos com distância 35. Nenhuma rejeição automática.

## Resultados e reprodução

Fonte preservada: `/home/administradorarthur/datasets/scanplant/p06-recovery-20260928`, 29 arquivos, incluindo as 17 imagens em quarentena; hashes antes/depois idênticos.

Resultados integrais: `/home/administradorarthur/datasets/scanplant/p07-curation-20260928`. `human-decisions.json` e arquivos `.draft` preservam propostas históricas do agente. `accepted-human-decisions.json` e `human-acceptance.json` externos registram a decisão humana. `curation.json`, `report.md` e `summary.json` são derivados pelo código aprovado, sem alteração dos pareceres. O campo padrão `final_bytes_human_acceptance=pending` do JSON gerado permanece intacto; o recibo humano separado é a fonte do aceite U-702, vinculado no registro sanitizado. Não copiar imagens ou relatórios integrais para o Git.

Ambiente: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python`, Python 3.14.4 e Pillow 12.3.0 instalado do cache local. O ambiente temporário anterior foi removido; o helper `verify_working_tree.py` preserva a evidência histórica anterior ao aceite e não é o verificador do fechamento atual.

```bash
/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_curate_p07.py'
/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/curate_p07.py --source /home/administradorarthur/datasets/scanplant/p06-recovery-20260928 --output /home/administradorarthur/datasets/scanplant/p07-curation-20260928 --finalize --decisions /home/administradorarthur/datasets/scanplant/p07-curation-20260928/accepted-human-decisions.json
```

38 testes P07 e 162 testes afetados/históricos passaram em checkout isolado. Finalização real repetida com bytes e mtimes idênticos. O guard concluiu a unidade do commit de implementação com 12 gates passed, sem blockers, fixes ou redesign. Sidecar: `artifacts/bianchini/v2/codex/convergence/P07/1.json`; provas e hashes em `artifacts/bianchini/v2/codex/P07/closure-evidence.json`.

P01–P06/P05-R1 e current_specs preservados; release pending; P08 não iniciado. A branch está preparada para publicação após autorização humana de push. O commit documental posterior registra esse fechamento e não altera código, testes ou decisões.
