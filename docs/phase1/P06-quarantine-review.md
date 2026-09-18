# P06 — revisão assistida dos 11 candidatos em quarentena

Rodada única de 2026-09-18, a partir do P06 publicado em
`997ed3aa038ab0a667061c47cfdb8a2d701da0fe`, branch `bm/v2-p06-direct`.
Este relatório registra observações e decisões propostas, sem aplicar decisões
ao dataset. Nenhuma revisão visual humana ou validação botânica definitiva foi
concluída. Os 11 arquivos permanecem em quarentena; zero liberados para treino.

## Precheck e preservação

- `git ls-remote --exit-code origin refs/heads/bm/v2-p06-direct` confirmou o SHA
  acima diretamente no remoto `Parys-boop/ScanPlant`; HEAD e upstream iguais,
  divergência `0/0`, árvore e índice limpos antes desta rodada.
- Commit `feat(p06): add licensed Commons acquisition pipeline`, com somente
  `.gitignore`, `artifacts/phase1/p06/coverage.json`, `docs/phase1/P06-acquisition.md`,
  `scripts/phase1/acquire_commons.py`, `scripts/phase1/requirements-p06.txt` e
  `scripts/phase1/test_acquire_commons.py`.
- Base `2a8a6902fd6e33b794628235757b0279f580b02a` confirmada como ancestral.
- Dataset externo existente em `$HOME/datasets/scanplant/p06`.
- Ausência de `AGENTS.md` explicitamente dispensada pelo responsável nesta sessão;
  nenhum arquivo substituto foi criado.
- P05/P05-R1 completed, U-201 resolved/consumed, P01/P03-R6 blocked-terminal,
  P02/P04 completed e release pending preservados, sem alterar PROJECT_STATE.

O resultado histórico permanece: 109 consultados, 11 aceitos tecnicamente,
94 rejeitados por licença, 4 pendentes pelo teto, zero falhas de aquisição,
7 CC BY 4.0 e 4 CC0 1.0. Nenhum coletor foi executado, nem mesmo `--resume-only`.
Os 123 testes publicados pertencem à entrega anterior; as verificações finais
desta revisão são registradas separadamente no RESULT operacional local.

## Evidência externa e método

O pacote revisável está em `$HOME/datasets/scanplant/p06/review-2026-09-18/`:

- `report.md`: uma entrada por candidato com arquivo, SHA-256 completo, classe,
  página Commons, autoria, licença, observações, proposta e decisão humana necessária.
- `index.html`: galeria local com os mesmos 11 candidatos e links aos arquivos em
  resolução integral. Usa diretamente os JPEGs existentes, sem recursos remotos
  automáticos, recortes, miniaturas ou derivados raster.
- `review.json`: inventário, metadados de origem, verificações e propostas, com
  hashes dos arquivos originais para conferir preservação.
- `p06-review-audit.py`: verificador de leitura; imprime JSON em stdout, sem
  adquirir, recodificar, mover ou alterar arquivos.

Autoria/licença/URLs vêm do snapshot local do manifesto, cujo SHA-256 é
`98bf4332edd7b97b99ee9229a84fed6afaa59b03817a568699ee716754ca7198`.
Não houve reconsulta ao Commons nem verificação independente da titularidade.
Conforme a política de P06, atribuições e imagens ficam fora do Git.

Os 11 SHA-256 coincidem com os registros aceitos mais recentes. Manifesto JSONL
e registros do estado coincidem; existem exatamente os 11 arquivos esperados na
quarentena. Todos passaram por `Pillow.verify()` e decodificação completa com
`LOAD_TRUNCATED_IMAGES=False`: JPEG/RGB, dentro dos limites existentes, total de
22.460.748 bytes. EXIF e IFD GPS vazios; apenas APP0 JFIF, sem APP1/APP2/COM ou
campos de XMP, ICC e comentários. Isso não é análise forense de esteganografia.

O assistente inspecionou os 11 arquivos via `view_image`, na renderização padrão;
Q10 também foi aberto com `detail=original`. Não foi feita revisão humana nem
varredura exaustiva de cada pixel. “Não aparente” abaixo significa não observado,
sem garantir ausência ou consentimento. A identidade de **todos** permanece
incerta até validação botânica humana. Os flags históricos da coleta permanecem
inalterados; a inspeção assistida é registrada separadamente em `review.json`.

## Inventário por SHA-256 registrado

Os arquivos externos são `quarantine/<SHA-256>.jpg`. IDs Q01–Q11 ordenam os
candidatos por classe e sequência do registro aceito; não são novos IDs de coleta.
Todos têm integridade, abertura e ausência de EXIF/GPS aprovadas nesta rodada.

| ID | Classe candidata | SHA-256 | Dimensões | Licença |
|---|---|---|---|---|
| Q01 | species_01 — Epipremnum aureum | `b6b853f31ecc3a3b7bf00faae149602278c166661f01a9dcbff9bbae61fd2b0a` | 3456 × 4608 | CC0 1.0 |
| Q02 | species_02 — Monstera deliciosa | `2e88ea17c9bb1b7fcca38adc5328191261da9a204fb824d5d0e1e9c37c499ae6` | 1001 × 987 | CC0 1.0 |
| Q03 | species_03 — Zamioculcas zamiifolia | `265d0550ce63292823fe0f185c984ab68654a88b006844aaed3e30dbdd0d50c2` | 3120 × 4160 | CC0 1.0 |
| Q04 | species_05 — Dracaena trifasciata | `3ced8f675ad228293f26d998d09e2b2ba5fbd5b8db7886c7f12bbedbc7213743` | 1536 × 2048 | CC BY 4.0 |
| Q05 | species_05 — Dracaena trifasciata | `e8bd82d505dd2210ec0aaa51fdf907b622166cce82ee4efbfe21c271688f5aec` | 1536 × 2048 | CC BY 4.0 |
| Q06 | species_07 — Chlorophytum comosum | `e168656879d2df43c1b2948c727f9728bd1111411bb61d98a8d2a8ebb3691048` | 3870 × 2580 | CC BY 4.0 |
| Q07 | species_07 — Chlorophytum comosum | `b88e23a8b46665fb27495c7baf4f8cc63d777497cc887a30eb08721ff94be578` | 3577 × 2385 | CC0 1.0 |
| Q08 | species_09 — Ficus elastica | `7fc30a7e965ae7ef60c17b70b253c13194b9fd04b99a9b2ae6bb2f9aa1cdcd4d` | 1536 × 2048 | CC BY 4.0 |
| Q09 | species_09 — Ficus elastica | `3c234066b31a71dde65722e2ca31a5c41c223ae69692b0d0d582ec5199917f08` | 1536 × 2048 | CC BY 4.0 |
| Q10 | species_12 — Tradescantia zebrina | `8967f71372a9892d914f3003913b6061f3b8a6874ef60d53f60b928a568dd29b` | 4032 × 3024 | CC BY 4.0 |
| Q11 | species_12 — Tradescantia zebrina | `8f9d7aab9e37dc29ec72baf1aca574c39c15dcccfb5bf3d71c5726e5c3401c15` | 4000 × 3000 | CC BY 4.0 |

## Propostas e justificativas

`manter_em_quarentena` destaca impedimentos específicos de adequação ou rótulo;
`aguardando_revisao_humana` encaminha os demais para a revisão pendente. Ambas
preservam fisicamente os arquivos e impedem uso em treino. Nenhuma proposta foi
aplicada ao estado da coleta. Não há rejeição técnica proposta: nenhum arquivo
corrompido/ilegível, e não se inventou critério para excluir fotos de órgãos ou
figuras anotadas. A adequação desses casos depende do responsável.

| ID | Decisão proposta | Observação visual e justificativa | Privacidade e decisão humana necessária |
|---|---|---|---|
| Q01 | aguardando_revisao_humana | Trepadeira parcial, escura, com grande área de parede; folhas visíveis. | Parede, grade e corrimão sugerem área possivelmente residencial. Sem pessoas, rostos, documentos ou placas aparentes. Confirmar identidade, enquadramento e contexto. |
| Q02 | manter_em_quarentena | Figura didática com textos, moldura e linhas sobre estrutura reprodutiva e folhas. Adequação da apresentação anotada pendente. | Legendas sem dados pessoais aparentes; sem pessoas, rostos, placas veiculares ou residência aparente. Decidir admissibilidade e confirmar identidade. |
| Q03 | aguardando_revisao_humana | Folíolos/eixos em primeiro plano, brilho e detalhes visíveis; planta parcial. | Parede e solo sugerem jardim/quintal possivelmente residencial. Sem pessoas, rostos, documentos ou placas aparentes. Confirmar identidade, qualidade e contexto. |
| Q04 | aguardando_revisao_humana | Folhas eretas com faixas transversais, cortadas nas bordas e parcialmente ocultas por galhos. | Vegetação/solo, sem pessoas, rostos, documentos, placas ou residência aparentes. Confirmar identidade e aceitar ou recusar oclusão e enquadramento. |
| Q05 | aguardando_revisao_humana | Folhas com faixas, amarelecimento, perfurações e áreas secas; detalhes visíveis. Danos da planta não são corrupção do arquivo. | Possível superfície construída amarela ao fundo, uso residencial indeterminado; sem pessoas, rostos, documentos ou placas aparentes. Confirmar identidade e adequação de folhas danificadas, sem diagnosticar doença. |
| Q06 | manter_em_quarentena | Macro de flor branca e botões, sem hábito/folhagem; detalhe visível, identidade não determinável com segurança. | Sem pessoas, rostos, documentos, placas ou residência aparentes. Decidir representatividade de flor isolada e obter identificação humana. |
| Q07 | manter_em_quarentena | Semente e estrutura vegetal seca; parte desfocada, sem mostrar planta/folhagem. Identidade não determinável com segurança. | Suporte semelhante a papel quadriculado, sem escrita pessoal aparente; sem pessoas, rostos, placas ou residência aparentes. Decidir adequação do órgão isolado e desfoque. |
| Q08 | aguardando_revisao_humana | Árvore em plano aberto, ave no topo, folhas pequenas, muito céu e outras plantas. | Jardim, bordadura e cerca/estrutura linear; sem residência identificável, pessoas, rostos, documentos ou placas aparentes. Confirmar identidade e suficiência de detalhes. |
| Q09 | aguardando_revisao_humana | Folhas elípticas, ramo e broto visíveis; gotas e lesão foliar, sem falha categórica. | Escada e apoio vertical, uso do local indeterminado; sem pessoas, rostos, documentos ou placas aparentes. Confirmar identidade e revisar contexto construído. |
| Q10 | manter_em_quarentena | Folhas estreitas predominantemente roxas levantam suspeita de divergência do rótulo registrado. Não há identificação alternativa definitiva. | Dois veículos, mobiliário e placa/cartaz no banco; placas veiculares não discerníveis, ocupantes não excluídos. Sem pessoa/rosto claramente identificável ou residência aparente. Prioridade humana: rótulo e privacidade em resolução integral. |
| Q11 | aguardando_revisao_humana | Folhagem ocupa quase todo o quadro, faixas longitudinais claras e partes arroxeadas; pequenos danos. | Sem pessoas, rostos, documentos, placas ou residência aparentes. Confirmar identidade, nitidez e enquadramento. |

Resultado: **4 manter_em_quarentena**, **7 aguardando_revisao_humana**,
**0 rejeitar_tecnicamente**, **0 liberados**. A suspeita de rótulo em Q10 é uma
observação visual, não uma conclusão taxonômica. Nenhuma imagem foi declarada
inutilizável de forma definitiva.

## Verificações e limites da rodada

Verificações executadas após as alterações documentais, usando o ambiente P06
existente com Pillow 12.3.0: **123/123 testes aprovados**, manifesto 1.1.0 válido
(14 classes, 79 aliases e 91 chaves científicas), PROJECT_STATE v2 válido,
**7/7 checksums aprovados** e `git diff --check` sem erros. Nenhum teste novo,
dependência ou campanha de mutação foi criado:

```bash
/tmp/scanplant-p06-env.G7C2MM/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
/tmp/scanplant-p06-env.G7C2MM/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json
python3 /caminho/da/skill/_shared/scripts/bm.py validate-state docs/living/PROJECT_STATE.md
sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
git diff --check
```

Também conferidos: os hashes de `source_files_sha256` em `review.json` (15 arquivos
de origem preservados byte a byte, incluindo os 11 JPEGs), os 11 links locais da
galeria, o inventário de imagens rastreadas idêntico ao HEAD e o índice vazio.
Estrutura e links do HTML verificados por parser; sem teste de renderização em browser.
O verificador externo pode ser reexecutado com o mesmo Python e `-B`.
Logs/resultados operacionais ficam no scratch ignorado
`.superpowers/bianchini/direct/p06-quarantine-review/`, sem substituir os registros
da execução P06 publicada. Não houve treinamento, partições, TFLite, mobile,
release, homologação, exclusão, staging, commit ou push.

## Decisão humana agrupada

Confirmar ou corrigir as propostas Q01–Q11 em uma resposta, indicando ID,
decisão e justificativa nas exceções: identidade de todos; adequação de
Q02/Q06/Q07; rótulo e privacidade de Q10; contextos construídos de
Q01/Q03/Q05/Q08/Q09. O aceite deste relatório não equivale a revisão botânica,
consentimento, exclusão ou autorização para treinamento.
