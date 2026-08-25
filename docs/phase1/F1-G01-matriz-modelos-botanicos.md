# F1-G01 — Seleção e viabilidade do modelo botânico offline

**Status do gate:** concluído como auditoria documental; nenhum artefato foi baixado, convertido ou versionado.
**Data de consulta:** 24/08/2026 (BRT).
**Amostra pesquisada:** quatro candidatos; não é busca exaustiva de modelos botânicos.

## Escopo e regra de evidência

O F1-G01 avalia somente a viabilidade documental de um classificador offline, em CPU, para *Epipremnum aureum*, *Monstera deliciosa*, *Zamioculcas zamiifolia*, *Spathiphyllum wallisii* e *Dracaena trifasciata*. Um candidato exigiria, antes de ser aprovado, TFLite pronto ou conversão reproduzível, CPU sem custom ops/delegate obrigatório, modelo+labels até 25 MB, I/O publicado, cobertura comprovada por label map e licença explícita para pesos, labels e redistribuição.

Nesta matriz, licença de código, pesos, dataset, labels e permissão de redistribuição são campos independentes. Uma tag de licença de repositório ou model card não é tratada, por si só, como prova de licença dos outros artefatos. “Não verificável” significa que a fonte foi incompleta ou não foi consultável sem baixar artefatos; não significa ausência do item.

## Taxonomia do piloto

O nome aceito para o piloto é *Dracaena trifasciata*; Plants of the World Online (Royal Botanic Gardens, Kew) registra *Sansevieria trifasciata* como sinônimo. [POWO — *Dracaena trifasciata*](https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A77164235-1) (consultado em 24/08/2026). Esse sinônimo será aceito apenas quando o label map do candidato o contiver.

## Fontes consultadas

| ID | Fonte direta | Papel e data |
|---|---|---|
| S1 | https://docs.plantnet.org/en/tutorials/install-the-offline-embedded-mode/ | Documentação oficial do modo embedded do Pl@ntNet; 24/08/2026. |
| S2 | https://github.com/plantnet/PlantNet-300K | Repositório oficial do código/benchmark PlantNet-300K; 24/08/2026. |
| S3 | https://github.com/plantnet/PlantNet-300K/blob/main/LICENSE | Arquivo LICENSE do **código** PlantNet-300K; 24/08/2026. |
| S4 | https://huggingface.co/litert-community/PlantNet-300K-ResNet18-LiteRT | Model card da distribuição comunitária LiteRT; 24/08/2026. |
| S5 | https://huggingface.co/litert-community/PlantNet-300K-ResNet18-LiteRT/blob/main/plantnet.tflite | Página direta do artefato `plantnet.tflite`; tamanho e SHA declarados; 24/08/2026. |
| S6 | https://github.com/joergmlpts/nature-id | Repositório do integrador `nature-id`; 24/08/2026. |
| S7 | https://github.com/joergmlpts/nature-id/blob/master/LICENSE | Arquivo LICENSE do **código** `nature-id`; 24/08/2026. |
| S8 | https://www.kaggle.com/models/google/aiy/tensorFlow1/vision-classifier-plants-v1/1 | Página de distribuição apontada por `nature-id`; conteúdo não legível na consulta sem baixar/autenticar; 24/08/2026. |
| S9 | https://powo.science.kew.org/taxon/urn%3Alsid%3Aipni.org%3Anames%3A77164235-1 | Fonte taxonômica para *Dracaena trifasciata* e *Sansevieria trifasciata*; 24/08/2026. |
| S10 | `ScanPlant-Final/assets/offline-proof/manifest.json` e `ScanPlant-Final/assets/offline-proof/labels.txt` | Evidência local da PT-05: origem declarada, contrato e label map efetivamente inspecionado; 24/08/2026. |

## Cobertura por label map

Nenhuma cobertura é inferida da arquitetura, do nome do dataset ou de nomes de uso comum. A tabela registra o resultado da inspeção disponível para cada espécie.

| Candidato | *E. aureum* | *M. deliciosa* | *Z. zamiifolia* | *S. wallisii* | *D. trifasciata* / *S. trifasciata* | Evidência |
|---|---|---|---|---|---|---|
| MobileNet V1/ImageNet PT-05 | Ausência no label map local: string exata não encontrada | Ausência no label map local: string exata não encontrada | Ausência no label map local: string exata não encontrada | Ausência no label map local: string exata não encontrada | Ausência no label map local: nem nome aceito nem sinônimo encontrados | S10; busca literal nas 1.001 linhas locais em 24/08/2026. Não é busca exaustiva de sinônimos além dos dois registrados. |
| Pl@ntNet offline/embedded | Não verificável | Não verificável | Não verificável | Não verificável | Não verificável | S1 não publica label map exportável para integração. |
| PlantNet-300K ResNet18 LiteRT | Não verificável | Não verificável | Não verificável | Não verificável | Não verificável | S2 descreve os arquivos de mapeamento de classes, e S4 aponta para eles, mas o conteúdo oficial do label map não foi inspecionado nem baixado nesta auditoria. |
| Google AIY Plants via `nature-id` | Não verificável | Não verificável | Não verificável | Não verificável | Não verificável | S6 aponta para CSV em `gstatic` e modelo em S8; o CSV não foi consultável pelo leitor web e não foi baixado. |

## Matriz de decisão

| Candidato | Modelo, formato, tamanho e contrato | Licenças e redistribuição — evidência separada | CPU / conversão | Riscos decisivos | Decisão |
|---|---|---|---|---|---|
| **MobileNet V1/ImageNet da PT-05** | Modelo TFLite local: `4.276.352` bytes; entrada RGB uint8 `[1,224,224,3]`, saída uint8 `[1,1001]`. Esses dados vêm do manifesto e do arquivo local, não de um release externo revalidado nesta auditoria (S10). | **Código/runtime:** fora da decisão de licença do modelo. **Pesos:** o manifesto local declara Apache-2.0 e aponta para `https://storage.googleapis.com/download.tensorflow.org/models/tflite/mobilenet_v1_1.0_224_quant_and_labels.zip`; a licença dos pesos não foi revalidada no release. **Labels:** origem declarada `https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt`; licença não verificada separadamente. **Dataset:** ImageNet, licença não verificada aqui. **Redistribuição:** não verificada separadamente. | CPU local já foi provada na PT-05; não é evidência de reconhecimento botânico. Não há conversão proposta. | O label map local não contém as cinco espécies nem o sinônimo registrado; usar ImageNet como catálogo botânico violaria o escopo. | **Rejeitado** para F1-G01 por incompatibilidade de cobertura, independentemente das lacunas de licença. |
| **Pl@ntNet offline/embedded** | S1 descreve um modelo comprimido para uso offline, mas não publica formato, tamanho, I/O ou label map para integração externa. Todos esses campos são não verificáveis. | **Código, pesos, dataset, labels e redistribuição:** não verificáveis pela página consultada. S1 informa que o modo/modelo é exclusivo do aplicativo móvel e exige conta para download; isso não é licença de redistribuição ao ScanPlant. | CPU, TFLite, custom ops e delegate: não verificáveis. Não há conversão reproduzível publicada em S1. | Não há artefato externo, contrato ou permissão de redistribuição comprovados. | **Evidência insuficiente** — não aprovado; não é rejeição técnica definitiva de um eventual acordo/licença futuro. |
| **PlantNet-300K ResNet18 LiteRT** | S5 declara o artefato `plantnet.tflite` com 46,9 MB e SHA-256 `6f59f046c6a86593713aca76a3ab7bb55b520265eb66f5a77a114e450b1ccbf5`; o tamanho excede objetivamente 25 MB. S4 declara entrada float32 NCHW `[1,3,224,224]`, RGB normalizado por ImageNet, e saída `[1,1081]` de logits. | **Código PlantNet-300K:** BSD-2-Clause em S3. **Pesos:** S4 declara Apache-2.0 para `cpoisson/plantnet300k-resnet18`, mas a licença do arquivo de pesos original não foi inspecionada diretamente nesta auditoria. **Dataset:** S2 diz que cada imagem possui licença em metadados; não há licença única do dataset demonstrada aqui. **Labels:** S2 descreve os arquivos de mapeamento; licença específica não verificada. **Redistribuição do TFLite:** S4/S5 exibem tag Apache-2.0, mas o texto LICENSE específico do artefato e a cadeia completa de direitos não foram inspecionados. | S4 declara uma conversão já publicada e fornece exemplo com `Interpreter`/CPU, porém a compatibilidade no Redmi A5, operações TFLite e ausência de custom ops não foram verificadas sem baixar o arquivo. Nenhuma conversão será feita no F1-G01. | Falha no teto de tamanho confirmada pelo artefato S5; cobertura das cinco espécies e cadeia de licença permanecem não verificadas. | **Rejeitado** sob F1-G01 pelo tamanho confirmado acima de 25 MB. |
| **Google AIY Plants referido por `nature-id`** | S6 informa TFLite e CSV; a própria fonte relata 2.102 labels no exemplo. O artefato exato, tamanho, I/O e versão não foram confirmados na página de distribuição S8. Portanto, o tamanho é não verificável; nenhuma estimativa é usada. | **Código `nature-id`:** MIT conforme S7. **Pesos, labels, dataset e redistribuição:** não verificáveis a partir de S6/S8; a licença do código não é aplicada aos modelos Google. | S6 afirma uso com TensorFlow Lite, mas custom ops, execução CPU sem delegate obrigatório e contrato do modelo não estão verificados. Não há conversão proposta. | Modelo/CSV são externos ao repositório do integrador; faltam artefato, licença e label map verificáveis. | **Evidência insuficiente** — não aprovado; não é rejeição técnica definitiva. |

## Limitações da pesquisa

- Foram avaliados quatro candidatos: o artefato local PT-05, Pl@ntNet embedded, a conversão comunitária PlantNet-300K LiteRT e o modelo Google AIY apontado por `nature-id`.
- Não foi realizada busca exaustiva de modelos, releases ou fornecedores.
- S8 não expôs conteúdo legível na consulta; o CSV de labels referido por S6 não foi inspecionado porque o leitor web não suportou o tipo CSV e a auditoria não baixou arquivos.
- Não houve download, hash local de artefato remoto, inspeção de flatbuffer, medição CPU, conversão ou verificação prática de custom ops.
- A confirmação de cobertura dos candidatos externos, a cadeia de licença de pesos/labels e a permissão de redistribuição dependerão de fontes diretas adicionais — e podem exigir download/conversão somente após nova autorização.

## Conclusão do gate

**Nenhum dos candidatos avaliados foi aprovado sob os critérios do F1-G01.**

O resultado não afirma que não exista outro modelo possível fora da amostra pesquisada. A próxima decisão, fora deste gate, é comparar um fine-tune de backbone mobile pequeno com a revisão das espécies-alvo. Qualquer download, treinamento, conversão, criação de corpus, alteração de aplicativo ou teste físico requer nova autorização.
