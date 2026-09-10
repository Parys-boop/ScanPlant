# F1-API01 — protocolo de benchmark e decisão de providers

## Estado da decisão

**P04 completed em 2026-09-10.** U-101 foi autorizada e consumida exclusivamente pelas 14 transmissões previstas: sete casos para Pl@ntNet e os mesmos sete bytes para Plant.id. Os 14 pares únicos foram concluídos uma única vez, sem retry, falha, timeout, chamada textual ou `plant.health`. A revisão humana aprovou a interpretação contratual A: **Pl@ntNet é o principal gratuito** e **Plant.id é o secundário técnico de trial**, sem ser apresentado como alternativa gratuita durável.

P01 e P03-R6 permanecem blocked-terminal, P02 permanece completed e o release permanece pending. Este documento não integra provider ao produto, não altera API/mobile/configuração e não substitui garantia ou homologação.

## Corpus fixo

| Ordem | case_id | Referência congelada | Situação final |
|---:|---|---|---|
| 1 | `p04-id-01-epipremnum-aureum` | *Epipremnum aureum* | byte sanitizado, congelado e consumido nos dois slots |
| 2 | `p04-id-02-monstera-deliciosa` | *Monstera deliciosa* | byte sanitizado, congelado e consumido nos dois slots |
| 3 | `p04-id-03-zamioculcas-zamiifolia` | *Zamioculcas zamiifolia* | byte sanitizado, congelado e consumido nos dois slots |
| 4 | `p04-id-04-spathiphyllum-wallisii` | *Spathiphyllum wallisii* | byte sanitizado, congelado e consumido nos dois slots |
| 5 | `p04-id-05-dracaena-trifasciata` | *Dracaena trifasciata*; aceitar *Sansevieria trifasciata* | byte sanitizado, congelado e consumido nos dois slots |
| 6 | `p04-id-06-other-known-plant` | *Bellis perennis* | byte sanitizado, congelado e consumido nos dois slots |
| 7 | `p04-id-07-no-plant-control` | imagem decodificável sem planta | PNG geométrico congelado e consumido nos dois slots |

A fixture `ScanPlant-Final/assets/offline-proof/daisy.jpg`, antes considerada para o sexto caso, não foi usada. Ela foi substituída por uma obra *Bellis perennis* CC0 com página permanente e referência POWO independentes. A fixture local não prova nenhuma das cinco espécies-alvo.

Os demais candidatos locais permaneceram classificados como inelegíveis: `plantasfoto.png` contém várias plantas sem referência única ou licença local; `passoapasso.png` é uma composição de tutorial; `mapaimg.png` tem marca visual de terceiro e nenhuma licença local verificável; `placeholder.png` é um ícone de folha. Logos, controles e imagens de marca não são casos do corpus. O inventário detalhado, direitos, atribuições, sanitização, dimensões e hashes dos sete bytes finais estão em `corpus-manifest.json`.

## Protocolo reproduzível

1. U-101 congela os sete bytes finais fora do Git, seus SHA-256, origem/direitos, referência revisada e ausência de metadados pessoais/localização.
2. A coleta percorre a ordem da tabela. Para cada caso, Pl@ntNet e depois Plant.id recebem exatamente os mesmos bytes.
3. Há uma chamada por par caso/provider: sete por provider, no máximo 14 identificações. Concorrência 1, timeout 20 segundos e zero retry automático.
4. Antes da próxima chamada, persistir a observação sanitizada. Se houver interrupção, reconciliar `case_id` + `provider_id`; qualquer slot com `transmitted=true` jamais é repetido. Timeout ou resultado desconhecido após transmissão consome o teto.
5. Registrar identificador local estável, hash da imagem, referência esperada, instante UTC, status, duração, JSON válido ou não, versão/modelo quando informado, top-1 científico, avaliação, falha neutra e referência do registro sanitizado. Não versionar imagem, segredo ou resposta bruta.
6. Groq/Gemini foram marcados `not_applicable`: conhecimento textual é opcional e o catálogo offline continua obrigatório. O teto efetivo textual é zero. O limite condicional aprovado de até quatro chamadas não foi ativado.

Estados de chamada: `not_run`, `success`, `no_match`, `timeout`, `transport_error`, `provider_error`, `invalid_response` e `cancelled_before_transmission`. Avaliações: `correct`, `incorrect` ou `not_evaluable`.

Para os seis casos de planta, `correct` exige correspondência do top-1 científico com o nome/sinônimo congelado; `no_match` é `incorrect`. Para o controle sem planta, `no_match` ou ausência explícita de identificação é `correct`, enquanto espécie top-1 nomeada é `incorrect`. Falha/timeout é `not_evaluable` e reduz disponibilidade.

## Métricas predefinidas

Por provider:

- denominador planejado: 7;
- denominador transmitido: quantidade de slots realmente transmitidos;
- denominador avaliável: `success` ou `no_match` com referência congelada;
- acurácia avaliada: `correct / avaliável`, nula quando o denominador é zero;
- correção estrita: `correct / 7`, publicada somente com matriz completa para que falha/timeout não favoreça o resultado;
- disponibilidade observada: respostas terminais `success`/`no_match` válidas sobre 7;
- mediana de duração: mediana de todas as chamadas transmitidas com duração, incluindo falhas/timeouts; em contagem par, média dos dois valores centrais;
- pior duração: maior duração observada entre as chamadas transmitidas.

Não se inferem SLA, p95 ou acurácia de produção com sete casos. Os resultados abaixo descrevem somente esta amostra piloto congelada.

## Elegibilidade e escolha

Um provider só entra na ordenação se: o corpus e os direitos estiverem aprovados; as condições de privacidade forem aceitas; o orçamento for zero com cobrança automática desativada e limite duro; os sete slots forem únicos e completos; e as observações forem sanitizadas e reconciliadas.

Para ser alternativa gratuita aprovada, o volume informado deve caber sem compra obrigatória após trial, com limite publicado e gasto bloqueável. Um provider pago/trial pode ser comparação técnica ou secundário técnico, mas não alternativa gratuita aprovada.

Entre elegíveis, a ordenação é lexicográfica: direitos/privacidade/orçamento; correção estrita; acertos nas espécies-alvo; acerto do controle; disponibilidade; menos falhas; menor mediana; menor pior duração. O melhor elegível e gratuito torna-se principal; o próximo elegível torna-se secundário. Empate material, matriz parcial ou ausência de alternativa gratuita mantém a decisão sem seleção e P04 incompleto.

## Resultado observado e decisão

U-101 aprovou o corpus sanitizado, suas fontes, direitos, atribuições e referências; aceitou as condições de privacidade e retenção; confirmou custo zero, quotas e limites; e autorizou exatamente os 14 slots. A autorização foi integralmente consumida e não permite novas transmissões. As fontes oficiais vigentes na coleta, endpoints, gratuidade/trial, retenção, limites e nomes de credenciais estão registradas em `artifacts/bianchini/v2/evidence/P04-f1-api01/terms-and-authorization.md`.

| Caso | Pl@ntNet: top-1, avaliação, duração | Plant.id: top-1, avaliação, duração |
|---|---|---|
| 01 — *Epipremnum aureum* | *Epipremnum aureum*, correct, 2045 ms | *Epipremnum aureum*, correct, 1960 ms |
| 02 — *Monstera deliciosa* | *Monstera deliciosa*, correct, 1757 ms | *Monstera deliciosa*, correct, 1875 ms |
| 03 — *Zamioculcas zamiifolia* | *Zamioculcas zamiifolia*, correct, 2556 ms | *Zamioculcas zamiifolia*, correct, 2478 ms |
| 04 — *Spathiphyllum wallisii* | *Spathiphyllum floribundum*, incorrect, 2721 ms | *Zantedeschia aethiopica*, incorrect, 2304 ms |
| 05 — *Dracaena trifasciata* | *Dracaena zeylanica*, incorrect, 2773 ms | *Dracaena trifasciata*, correct, 3280 ms |
| 06 — *Bellis perennis* | *Bellis perennis*, correct, 2596 ms | *Bellis perennis*, correct, 2553 ms |
| 07 — controle sem planta | *Hedera helix*, incorrect, 832 ms | no_match, correct, 906 ms |

| Provider | Acertos | Correção estrita | Disponibilidade | Mediana | Pior duração | Papel aprovado |
|---|---:|---:|---:|---:|---:|---|
| Pl@ntNet | 4/7 | 57,14% | 7/7 | 2556 ms | 2773 ms | principal gratuito |
| Plant.id | 6/7 | 85,71% | 7/7 | 2304 ms | 3280 ms | secundário técnico de trial |

Pl@ntNet retornou HTTP 200 e versão `2026-03-20 (7.5)` nos sete casos. Plant.id retornou HTTP 201/`COMPLETED` e versão `plant_id:5.1.1` nos sete casos, com seis `success` e um `no_match`. O total é 10 `correct`, 4 `incorrect`, zero `not_evaluable`, falhas, timeouts ou retries.

A ordenação foi aplicada sem mudar os critérios aprovados. Plant.id teve melhor correção na amostra, mas o trial não satisfaz o papel de alternativa gratuita durável. Pl@ntNet satisfez direitos, privacidade, custo zero, completude e controle de chamadas para o volume documentado; por isso é o principal gratuito. Plant.id satisfez os gates da comparação e fica como secundário técnico, sem ser apresentado como provider gratuito contínuo. A ausência de dois providers gratuitos não impede esses papéis.

O piloto possui apenas sete casos: cinco espécies-alvo, uma outra planta conhecida e um controle sem planta. Ele não demonstra cobertura das 12 espécies do MVP, SLA, p95, acurácia de produção ou desempenho futuro. A decisão não integra provider, altera produto ou autoriza novas chamadas.

Após a revisão humana da slice e aprovação da interpretação A em 2026-09-10, P04/F1-API01 está **completed**. P01 e P03-R6 permanecem blocked-terminal por seus bloqueios independentes; P02 permanece completed e o release permanece pending. O roadmap apenas indica, depois da segurança do fallback, o manifesto completo das 12 espécies como item seguinte; nenhum novo marco é iniciado ou planejado por esta decisão.
