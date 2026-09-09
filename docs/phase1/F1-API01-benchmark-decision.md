# F1-API01 — protocolo de benchmark e decisão de providers

## Estado da decisão

**Aguardando U-101.** A parte offline e reversível de P04 foi preparada em 2026-09-09. Não houve chamada, transmissão, autenticação, uso de credencial, consumo de crédito ou gasto. A matriz contém 14 observações `not_run`, métricas nulas e nenhum provider principal ou secundário selecionado.

P01 e P03-R6 permanecem blocked-terminal, P02 permanece completed e o release permanece pending. Este documento não integra provider ao produto, não altera API/mobile/configuração e não substitui garantia ou homologação.

## Corpus fixo

| Ordem | case_id | Referência exigida | Situação offline |
|---:|---|---|---|
| 1 | `p04-id-01-epipremnum-aureum` | *Epipremnum aureum* | imagem ausente |
| 2 | `p04-id-02-monstera-deliciosa` | *Monstera deliciosa* | imagem ausente |
| 3 | `p04-id-03-zamioculcas-zamiifolia` | *Zamioculcas zamiifolia* | imagem ausente |
| 4 | `p04-id-04-spathiphyllum-wallisii` | *Spathiphyllum wallisii* | imagem ausente |
| 5 | `p04-id-05-dracaena-trifasciata` | *Dracaena trifasciata*; aceitar *Sansevieria trifasciata* | imagem ausente |
| 6 | `p04-id-06-other-known-plant` | outra planta com nome científico revisado | `daisy.jpg` depende de confirmação humana |
| 7 | `p04-id-07-no-plant-control` | imagem decodificável sem planta | imagem ausente |

A fixture `ScanPlant-Final/assets/offline-proof/daisy.jpg` tem SHA-256 `0c9affbefd33536dab5547b42893221508e198cca435aa758a969bd88a9ba6bc`, origem, crédito e declaração CC-BY no manifesto local. Ela só é candidata ao sexto caso: ainda faltam confirmação da variante/atribuição, referência científica revisada e autorização explícita para transmissão. Ela não prova nenhuma das cinco espécies-alvo.

Os demais candidatos locais foram classificados como inelegíveis: `plantasfoto.png` contém várias plantas sem referência única ou licença local; `passoapasso.png` é uma composição de tutorial; `mapaimg.png` tem marca visual de terceiro e nenhuma licença local verificável; `placeholder.png` é um ícone de folha. Logos, controles e imagens de marca não são casos do corpus. O inventário detalhado e os hashes estão em `corpus-manifest.json`.

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

Não se inferem SLA, p95 ou acurácia de produção com sete casos. Enquanto não houver observação real, todos os resultados derivados permanecem nulos.

## Elegibilidade e escolha

Um provider só entra na ordenação se: o corpus e os direitos estiverem aprovados; as condições de privacidade forem aceitas; o orçamento for zero com cobrança automática desativada e limite duro; os sete slots forem únicos e completos; e as observações forem sanitizadas e reconciliadas.

Para ser alternativa gratuita aprovada, o volume informado deve caber sem compra obrigatória após trial, com limite publicado e gasto bloqueável. Um provider pago/trial pode ser comparação técnica ou secundário técnico, mas não alternativa gratuita aprovada.

Entre elegíveis, a ordenação é lexicográfica: direitos/privacidade/orçamento; correção estrita; acertos nas espécies-alvo; acerto do controle; disponibilidade; menos falhas; menor mediana; menor pior duração. O melhor elegível e gratuito torna-se principal; o próximo elegível torna-se secundário. Empate material, matriz parcial ou ausência de alternativa gratuita mantém a decisão sem seleção e P04 incompleto.

## Condições oficiais e U-101

As fontes oficiais vigentes, endpoints, gratuidade/trial, retenção, limites, nomes de credenciais e a solicitação humana única estão registradas em `artifacts/bianchini/v2/evidence/P04-f1-api01/terms-and-authorization.md`.

O responsável ainda precisa resolver os sete slots: fornecer seis imagens ausentes e confirmar ou substituir a `daisy.jpg`; revisar origem/licença/direito/consentimento e referência de cada uma; confirmar ausência de dados pessoais/localização; provisionar contas e chaves somente no executor; confirmar Pl@ntNet gratuito, sete créditos Plant.id de trial sem custo, cobrança automática desativada e hard limits; aceitar as condições de dados; e conceder U-101 explicitamente para exatamente 14 transmissões. Valores de chaves não devem ser enviados pelo chat.

Até essa autorização única, o resultado permanece: **nenhum provider vencedor; benchmark real não iniciado**.
