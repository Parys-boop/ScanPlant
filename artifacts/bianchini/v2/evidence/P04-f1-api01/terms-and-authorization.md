# P04/F1-API01 — termos, limites e fronteira U-101

Estado em 2026-09-09: protocolo offline preparado; U-101 pendente; nenhuma conta autenticada, chave lida, imagem transmitida, chamada iniciada ou cobrança gerada. Esta síntese não substitui os termos oficiais nem aceita termos em nome do responsável.

## Pl@ntNet

Fontes oficiais consultadas em 2026-09-09:

- [Introdução e autenticação](https://my.plantnet.org/doc/getting-started/introduction): base `https://my-api.plantnet.org`, conta e chave de API exigidas.
- [Identificação v2](https://my.plantnet.org/doc/api/identify): `POST /v2/identify/{project}`, JPEG/PNG, até cinco imagens da mesma planta e resposta com candidatos, `bestMatch` e versão do engine quando disponível. P04 enviará uma imagem por chamada.
- [Quotas](https://my.plantnet.org/doc/api/quota): quota vinculada à conta/tipo de requisição, renovada diariamente à meia-noite UTC, consultável pela conta e refletida em headers de resposta.
- [Pricing](https://my.plantnet.org/pricing): plano gratuito publicamente anunciado a €0 e 500 identificações por dia; planos pagos e condições especiais existem. O valor da página não prova a configuração da conta que será usada.
- [Terms of use](https://my.plantnet.org/terms_of_use): conta obrigatória; o texto público informa processamento de imagens em memória volátil e não armazenamento das imagens, enquanto o histórico da consulta preserva data/hora e URLs quando aplicável. O uso gratuito/comercial e a atribuição devem ser confirmados para a finalidade concreta.

Gate U-101 específico: confirmar que a conta escolhida está no plano gratuito, sem meio de pagamento ou cobrança automática aplicável; reservar no máximo sete identificações para P04; aceitar a política de dados para as sete imagens autorizadas; manter a chave somente no executor controlado sob o nome já usado pelo backend `PlantNet__ApiKey`. O endpoint/base local usa as configurações `PlantNet:BaseUrl` e `PlantNet:ApiKey`, representáveis por `PlantNet__BaseUrl` e `PlantNet__ApiKey`; nenhum valor foi lido ou registrado.

## Plant.id by Kindwise

Fontes oficiais consultadas em 2026-09-09:

- [Documentação Plant.id](https://plant.id/docs) e [exemplo oficial v3](https://github.com/flowerchecker/plant-id-examples/blob/master/README.md): `POST https://api.plant.id/v3/identification`, imagens no corpo e autenticação no header `Api-Key`.
- [Handbook](https://www.kindwise.com/handbook): chave necessária; uso recomendado do header; resultados de identificação recuperáveis por até seis meses; nomes, sinônimos e imagens representativas possuem campos e condições próprias.
- [Pricing](https://www.kindwise.com/pricing): 100 créditos gratuitos após cadastro e créditos pagos por identificação depois da franquia; a gratuidade inicial é trial, não prova uma alternativa gratuita durável.
- [Admin panel FAQ](https://www.kindwise.com/faqs-admin-panel): créditos precisam ser atribuídos à chave; limites diário/semanal/mensal podem ser configurados como hard limit; alertas isolados não bloqueiam consumo.
- [API FAQ](https://www.kindwise.com/faq): uso é baseado em créditos, comunicação usa HTTPS/TLS e a documentação pública descreve armazenamento em Google Cloud Storage e dados relacionais na DigitalOcean.
- [Terms and Conditions](https://web.plant.id/wp-content/uploads/2023/04/Terms-and-Conditions.pdf): requisição aceita deduz crédito; o trial tem condições próprias e pode ser alterado ou encerrado. A versão contratual exibida na conta prevalece e deve ser aceita pelo responsável.
- [Privacy policy](https://www.kindwise.com/privacy-policy): política pública geral da Kindwise. Ela não resolve sozinha retenção, base legal e eventual contrato específico da conta/API para as imagens do corpus.

Gate U-101 específico: conta Kindwise/Plant.id com ao menos sete créditos de trial disponíveis; nenhuma compra, recarga automática ou cobrança; chave limitada por hard limit a no máximo sete identificações do P04; aceitação explícita da retenção/armazenamento e dos termos efetivos da conta. Não existe configuração backend Plant.id no produto. Para o executor efêmero, o nome documental esperado é `P04_PLANT_ID_API_KEY`; o valor deve existir apenas no ambiente/cofre do executor e nunca ser enviado pelo chat ou gravado no repositório. A variável web existente `VITE_PLANT_ID_API_KEY` não será usada no benchmark backend-side.

Plant.id pode participar da comparação usando créditos gratuitos de trial se U-101 confirmar custo zero, mas o contrato aprovado impede tratá-lo como alternativa gratuita aprovada sem oferta contínua que cubra o volume informado após o trial.

## Groq e Gemini

A comparação textual foi classificada como `not_applicable` neste protocolo. O contrato local mantém Groq opcional e o catálogo offline obrigatório; a decisão P04 de identificação não depende de Groq/Gemini. Portanto, o teto textual efetivo é zero, nenhum modelo foi selecionado e U-101 não pede credenciais textuais.

As fontes oficiais foram consultadas apenas para confirmar a fronteira:

- Groq: [API reference](https://console.groq.com/docs/api-reference), [rate limits](https://console.groq.com/docs/rate-limits), [data handling](https://console.groq.com/docs/your-data) e [billing FAQ](https://console.groq.com/docs/billing-faqs). Limites efetivos dependem da organização/modelo e dados de uso são registrados; isso exigiria nova justificativa antes de qualquer chamada.
- Gemini: [getting started](https://ai.google.dev/gemini-api/docs/generate-content/get-started), [rate limits](https://ai.google.dev/gemini-api/docs/rate-limits), [pricing](https://ai.google.dev/gemini-api/docs/pricing), [billing](https://ai.google.dev/gemini-api/docs/billing) e [terms](https://ai.google.dev/gemini-api/terms). Limites/preços dependem do modelo/tier; serviços não pagos possuem condições de uso de conteúdo incompatíveis com uma autorização implícita.

Nomes locais observados, sem valores: `Groq:BaseUrl`, `Groq:ApiKey`, `Groq:Model`, `Groq:Enabled`, equivalentes `Groq__BaseUrl`, `Groq__ApiKey`, `Groq__Model`, `Groq__Enabled`; `VITE_GEMINI_API_KEY` no web e a referência divergente `GEMINI_API_KEY` no README do web. Nenhum deles é necessário para P04 nesta rodada.

## Protocolo congelado antes de transmissão

- Sete casos e dois providers de identificação, sempre os mesmos bytes e a mesma ordem.
- Uma única chamada por `case_id`/`provider_id`: sete Pl@ntNet + sete Plant.id, teto total exato de 14.
- Concorrência 1, timeout de 20 segundos e zero repetição automática.
- Falha ou perda de resposta depois da transmissão consome o slot e o teto; não se presume que o provider deixou de receber.
- Cada observação sanitizada é persistida antes da próxima chamada. Uma retomada reconcilia a matriz e não repete slot já transmitido.
- Imagens e respostas brutas ficam fora do Git em armazenamento controlado; somente hashes e observações sanitizadas podem ser versionados.
- Textual: zero chamadas. O teto condicional aprovado de até quatro não foi ativado porque não há necessidade técnica demonstrada.

## Solicitação humana única U-101

Para liberar a primeira transmissão, o responsável precisa fornecer ou confirmar, em conjunto:

1. Os sete bytes finais fora do Git: uma imagem para cada uma de *Epipremnum aureum*, *Monstera deliciosa*, *Zamioculcas zamiifolia*, *Spathiphyllum wallisii* e *Dracaena trifasciata*; uma outra planta identificada; e uma imagem decodificável sem planta. Se a `daisy.jpg` local for aceita para o sexto caso, confirmar a variante CC-BY/atribuição, o nome científico revisado e seu uso externo; caso contrário, fornecer a sexta imagem também.
2. Para cada caso, origem e licença, direito autoral próprio ou consentimento verificável; referência humana revisada; confirmação de que a versão final não contém pessoa, dado pessoal ou metadado de localização; e autorização para transmitir exatamente aqueles bytes a Pl@ntNet e Plant.id.
3. Contas Pl@ntNet e Kindwise/Plant.id disponíveis no executor controlado. Disponibilizar os valores de `PlantNet__ApiKey` e `P04_PLANT_ID_API_KEY` somente no ambiente/cofre do executor; não enviar chaves no chat.
4. Confirmação de que Pl@ntNet está no plano gratuito aplicável e que Plant.id usará somente créditos gratuitos de trial já disponíveis; nenhuma compra, meio de pagamento ativo para consumo, recarga ou cobrança automática.
5. Limites duros de sete chamadas por provider e autorização total de 14 identificações, com concorrência 1, timeout 20 segundos e sem retry. Confirmar que o saldo/quota atual suporta esse teto sem custo.
6. Aceitação consciente das condições vigentes registradas acima, incluindo histórico do Pl@ntNet e retenção/infraestrutura publicada pela Kindwise, ou indicação de que algum provider deve ser declarado inelegível. Não haverá substituição silenciosa nem gasto para completar a matriz.
7. Autorização explícita U-101 para iniciar as transmissões. A aprovação do plano P04 já registrada não concede esta autorização.

Até todos os sete itens serem satisfeitos, `observations.json` permanece `not_run`, nenhum vencedor é selecionado, P04 permanece incompleto e o release continua pending. P01 e P03-R6 permanecem blocked-terminal; P02 permanece completed.
