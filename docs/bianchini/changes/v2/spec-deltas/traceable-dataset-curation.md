# Contrato completo esperado — curadoria rastreável P07

SD-701. Destino futuro: `docs/bianchini/current/specs/traceable-dataset-curation.md`, hoje inexistente. Este delta descreve o contrato após eventual entrega; **não** sincronizar current_specs durante planejamento ou execução, pois o ciclo v2/release segue pendente.

## Domínio e fonte

O conjunto fonte é a recuperação independente P06 de 2026-09-28: exatamente 17 arquivos em `quarantine/`, 17 decisões anteriores Q01–Q17 ↔ R01–R17, `state.json`, `manifest.jsonl`, `coverage.json`, `inventory.json` e `SHA256SUMS`. Os 11 arquivos de 18/09 estão perdidos e não integram P07. O manifesto de classes P05-R1 1.1.0 fixa 12 espécies e `outra_planta`/`imagem_invalida`; nenhuma classe, ID ou índice é alterado. P06 permanece byte-igual, incluindo suas decisões e `usable=0`. D-701, A-701, P-701.

## Análise e duplicidade

Pillow 12.3.0 decodifica cada arquivo em leitura; SHA-256 confronta bytes, paths e conjunto esperado antes/depois. Registrar dimensões, razão, luminância, exposição e variância do Laplaciano assinado sobre luminância 256×256 LANCZOS. Flags: lado menor `<224`, razão `>3,0`, média `<40` ou `>215`, extremos `≤15`/`≥240` com fração `≥0,25`, variância `<100`. dHash horizontal v1 usa luminância 9×8 LANCZOS, 64 bits; Hamming `0–6` sinaliza quase duplicata, `7–10` limítrofe, `11–64` sem sinal. SHA igual marca duplicata exata. Comparar os 136 pares, registrar hash, distância e versão. As medidas e flags são **triagem**, sem rejeição ou aprovação automática. D-703, P-702, S-701.

## Revisão, estados e prova

Todos os 17 IDs exigem parecer U-701 individual com SHA-256, classe candidata, critérios técnicos, pares de duplicidade, avaliação de enquadramento/oclusão/múltiplas espécies/representatividade, privacidade (pessoas, rostos, placas, veículos, residências, documentos, outros identificáveis), evidência botânica ou insuficiência, responsável, timestamp com fuso e justificativa. Autoria, licença, origem e atribuição P06 são preservadas no arquivo externo. Nenhuma decisão P06 se converte automaticamente em P07. D-702, P-703.

Estados exatos: `approved_for_dataset`, `rejected_quality`, `rejected_duplicate`, `rejected_privacy`, `rejected_label`, `needs_botanical_review`, `needs_human_review`. O primeiro requer todos os gates humanos suficientes e **não** autoriza treino. Todo `rejected_*` exige justificativa humana; `rejected_duplicate` aponta exemplar mantido. Os dois `needs_*` mantêm quarentena e podem permanecer após conclusão P07. Zero aprovadas e classes vazias são resultados válidos. Não há meta de imagens por classe nem alegação de suficiência para treinamento. D-702, U-701.

## Persistência e visibilidade

Saída integral apenas em diretório externo P07 novo: `analysis.json`, `human-decisions.json`, `curation.json`, `report.md`, sem alterar P06, imagens ou backups. JSON estrito UTF-8/LF, ordem de IDs/pares estável, 17 registros, contagens por estado e por 14 classes, lacunas, classes sem candidato e `training_sufficiency=not_demonstrated`. Timestamps humanos são entrada versionada, nunca relógio novo em reexecução igual. Trava exclusiva, escrita atômica de arquivos P07 e recusa de divergência silenciosa garantem idempotência. No Git, somente resumo JSON e relatório sem autoria, URLs de arquivo, detalhes privados, binários, segredo ou dado pessoal. D-704, P-701, P-703, U-703.

## Aceite e limites

Testes com imagens sintéticas cobrem métricas/limiares, SHA, dHash, colisões, parser estrito, 17 IDs, estados, ausência de promoção, bloqueio por hash, privacidade do resumo e idempotência. A execução real requer 17 análises e 17 pareceres, integridade P06 antes/depois e relatório legível. U-702 exige aceite humano dos hashes finais antes de commit/push. Nenhuma aquisição, treinamento, partição, modelo, integração de produto, homologação, release ou reparo P01/P03 pertence a este domínio.
