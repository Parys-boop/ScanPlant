# P07 — mudança: curadoria rastreável das 17 imagens adquiridas

## Objetivo e fronteira

P07 cria um processo reproduzível de **análise técnica seguida de decisão humana** para as 17 imagens externas da recuperação P06. A entrada é o diretório externo `p06-recovery-20260928`; a saída integral fica em diretório externo novo e separado, e somente um resumo sem dados pessoais entra no Git. A unidade inclui a reconciliação mínima de `PROJECT_STATE.md` e da cronologia do plano canônico. D-701, D-704, SD-701. Não executa aquisição, treinamento, partições, modelo, produto, homologação ou release. P01/P03-R6 permanecem blocked-terminal; P02/P04/P05/P05-R1 completed; P06 continua encerrado como mecanismo; `usable=0` é o ponto de partida, não a meta de saída.

## Entradas, identidade e integridade

Entrada única: `state.json`, `manifest.jsonl`, `coverage.json`, `inventory.json`, `SHA256SUMS`, `review-2026-09-28/human-decisions.json` e exatamente 17 arquivos em `quarantine/`. Reconciliar registros `result=accepted`, decisões Q01–Q17 ↔ R01–R17, `class_id` com o manifesto P05 1.1.0 e SHA-256 esperado de cada arquivo. Conjunto duplicado, ausente, extra, hash divergente, manifesto/decisão incoerente ou symlink bloqueia resultado; não recuperar, recodificar, mover nem deletar. Guardar hashes de todos os arquivos P06 lidos antes/depois. A-701, P-701, U-703.

O ID estável P07 é `Q01`…`Q17` junto de `R01`…`R17`, run_id P06 e SHA-256, sem renumeração. A decisão P06 é campo `prior_p06_decision` imutável; suas três `aprovar_para_curadoria_futura` jamais são promoção. As três `rejeitar` permanecem ineligíveis até parecer P07 explícito e fundamentado; nenhum parecer P07 altera o registro P06. Autoria, licença, licença URL, página de origem e atribuição são referenciadas integralmente apenas no artefato externo; devem coincidir com os metadados P06, nunca ser inferidas de pixels.

## Análise técnica determinística

D-703 e S-701: usar Pillow 12.3.0 para decodificação completa e conversão temporária a luminância. Registrar erro de decodificação, formato, largura, altura, razão maior/menor lado, média e frações de luminância extrema. Em imagem `L` redimensionada 256×256 por LANCZOS, calcular variância populacional do Laplaciano assinado `4c−esquerda−direita−acima−abaixo` nos pixels interiores. Sinais de triagem: menor lado `<224`, razão `>3,0`, média `<40` ou `>215`, fração de pixels `≤15` ou `≥240` `≥0,25`, Laplaciano `var<100`. Igualdade ao limite segue exatamente o operador indicado. Registrar medidas, flags, método, versão e interpretador; **nenhuma flag rejeita**. P-702.

Calcular SHA-256 para igualdade de bytes e dHash horizontal v1: imagem `L` 9×8 LANCZOS, bit 1 quando luminância da coluna direita é estritamente maior que a esquerda, ordem de linhas, 64 bits; distância Hamming de XOR. Avaliar 136 pares em ordem estável: SHA igual = `exact_duplicate`; SHA diferente e Hamming `0–6` = `near_duplicate_candidate`; `7–10` = `borderline_visual_pair`; `11–64` = `no_algorithmic_signal`. Registrar 64 bits hex, distância, limiares, pares e versão. Colisão dHash, enquadramento distinto, crop, rotação e cor exigem revisão humana; nem mesmo distância 0 é rejeição automática. A-702, P-702.

Enquadramento, oclusão, múltiplas espécies, representatividade de classe, pessoas/rostos, placas, veículos, residências, documentos e outros identificáveis são campos de revisão visual humana em resolução original. Ausência de achado automatizado não prova privacidade. A validação botânica exige evidência concreta de identificação compatível com `class_id`; metadado Commons e decisão visual P06 isolados não bastam. Sem evidência suficiente usar `needs_botanical_review`. A revisão humana pode concluir que qualidade/privacidade exige pendência sem forçar rejeição. D-702, P-703, U-701.

## Estados e autoridade

Cada uma das 17 imagens recebe exatamente um estado P07:

| Estado | Semântica e autoridade |
|---|---|
| `approved_for_dataset` | Parecer humano explícito: integridade, licença/proveniência, qualidade, privacidade, unicidade e rótulo botânico suficientes para inclusão em conjunto curado. Não autoriza treino. |
| `rejected_quality` | Parecer humano considera qualidade/representatividade inadequada; preservar arquivo. |
| `rejected_duplicate` | Parecer humano identifica duplicata/cópia redundante e aponta ID do exemplar mantido; preservar arquivo. |
| `rejected_privacy` | Parecer humano considera identificáveis inadequados; detalhes ficam externos. |
| `rejected_label` | Parecer humano confirma rótulo inadequado à classe/finalidade; não atribuir classe nova automaticamente. |
| `needs_botanical_review` | Parecer humano registra evidência insuficiente de identidade; mantém quarentena. |
| `needs_human_review` | Parecer humano registra outra incerteza específica ainda não resolvida; mantém quarentena. |

Todos os sete estados exigem um registro humano por imagem, com `reviewer_id`/papel, timestamp ISO-8601 com fuso, justificativa, evidência ou razão de insuficiência, rubrica técnica e de privacidade e referência aos pares pertinentes. Um resultado automático só produz `analysis` e flags sem `decision`. Um revisor não pode marcar `approved_for_dataset` se qualquer gate obrigatório estiver não avaliado ou a evidência botânica faltar. `needs_*` é resultado válido para fechamento P07; `approved_for_dataset` não muda fisicamente `quarantine/` nem `coverage.json` do P06. D-702, U-701.

## Saídas, concorrência e idempotência

No diretório externo novo de P07: `analysis.json` determinístico, `human-decisions.json` de revisão, `curation.json` reconciliado e `report.md` legível. JSON UTF-8/LF, objetos fechados, sem chaves duplicadas, NaN/Infinity ou coerção; ordenar por Q e pares. `curation.json` inclui run_id, hashes das entradas, algoritmo/versões/limiares, 17 registros completos, contagens dos sete estados e cobertura por 14 classes, lacunas e classes sem candidato; sempre declara suficiência para treinamento **não demonstrada**. O relatório explicita zero aprovadas como resultado legítimo. No Git: `artifacts/phase1/p07/summary.json` e `docs/phase1/P07-curation.md` somente com IDs, hashes, classes, estados, contagens, lacunas e limitações; sem autoria, URL de arquivo, imagem, observação privada, descrição de pessoa ou documento. P-703, D-704, SD-701.

Uma execução usa trava exclusiva no destino externo e pré-condições de entrada congeladas. Escrever temporários no próprio destino e trocar atomicamente apenas arquivos P07 completos; falha conserva P06 e resultado anterior. Reexecução com mesmas entradas, configuração e decisões mantém bytes e timestamps de decisões; conteúdo divergente exige nova revisão/versão, nunca sobrescrita silenciosa. Validar os 17 hashes de entrada também após leitura e comparar árvores P06 antes/depois. Não gerar backups. P-701, U-703.

## Gate e aceite

Fixtures sintéticas cobrem decoder inválido, medidas e fronteiras, duplicata SHA, quase duplicata dHash, colisão e ausência de promoção automática, JSON estrito, 17 IDs, erro de integridade, saída sanitizada e idempotência. A execução real exige 17 análises e 17 pareceres U-701, ainda que alguns sejam `needs_*`; reconciliação integral e relatório. U-702 aceita os bytes finais e hashes antes de qualquer commit/push. `git diff --check`, checksums e snapshots históricos continuam íntegros. O plano P07 não resolve o bloqueio seletivo P01/P03 nem os gates de release.
