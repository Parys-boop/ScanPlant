# P04/F1-API01 — termos, limites e fronteira U-101

Estado em 2026-09-10: o responsável humano aprovou e congelou os sete bytes finais sanitizados fora do Git e resolveu U-101 exclusivamente para as 14 identificações descritas neste documento. As duas credenciais foram confirmadas como presentes e não vazias no ambiente sem leitura ou registro de valor ou derivado. No instante deste checkpoint, nenhuma imagem havia sido transmitida, nenhuma chamada de identificação havia sido iniciada e nenhuma cobrança havia sido gerada. Esta síntese não substitui os termos oficiais.

## Corpus candidato para a fronteira U-101

O diretório explícito `/var/tmp/scanplant-p04-f1-api01-corpus-20260910` contém exatamente sete arquivos finais candidatos: cinco espécies-alvo, *Bellis perennis* como a outra planta conhecida e um controle geométrico local sem planta. Os seis casos botânicos usam obras do Wikimedia Commons sob domínio público, CC0 ou CC BY-SA e nomes aceitos no Plants of the World Online/Kew. A `daisy.jpg` do repositório não foi usada porque sua variante e cadeia de atribuição não foram presumidas; foi substituída pelo caso *Bellis perennis* com página de obra, CC0 1.0 e referência taxonômica independentes.

Para cada JPEG, todos os segmentos APP0–APP15 e COM foram removidos sem recompressão dos pixels; o controle foi gerado como PNG mínimo contendo somente `IHDR`, `IDAT` e `IEND`. Os hashes pós-sanitização, MIME, dimensões, tamanhos, autoria, licença, atribuição, URLs original/downloadada, referência taxonômica e resultado da inspeção visual estão em `corpus-manifest.json`. A inspeção final confirmou conteúdo decodificável e ausência de pessoa, texto, marca, documento, placa, endereço ou localização visível. A análise estrutural confirmou ausência de EXIF, GPS, comentários e demais metadados embutidos nos bytes finais. Esses fatos preparam a decisão humana, mas não equivalem a consentimento para transmissão.

## Pl@ntNet

Fontes oficiais reconsultadas em 2026-09-10:

- [Introdução e autenticação](https://my.plantnet.org/doc/getting-started/introduction): base `https://my-api.plantnet.org`, conta e chave de API exigidas.
- [Identificação v2](https://my.plantnet.org/doc/api/identify): `POST /v2/identify/{project}`, JPEG/PNG, até cinco imagens da mesma planta e resposta com candidatos, `bestMatch` e versão do engine quando disponível. P04 enviará uma imagem por chamada.
- [Quotas](https://my.plantnet.org/doc/api/quota): quota vinculada à conta/tipo de requisição, renovada diariamente à meia-noite UTC, consultável pela conta e refletida em headers de resposta.
- [Pricing](https://my.plantnet.org/pricing): plano gratuito publicamente anunciado a €0 e 500 identificações por dia; planos pagos e condições especiais existem. O valor da página não prova a configuração da conta que será usada.
- [Terms of use](https://my.plantnet.org/terms_of_use): conta obrigatória; o texto público informa processamento de imagens em memória volátil e não armazenamento das imagens, enquanto o histórico da consulta preserva data/hora e URLs quando aplicável. O uso gratuito/comercial e a atribuição devem ser confirmados para a finalidade concreta.

Passos humanos para criar ou conferir a conta gratuita:

1. Acessar [o cadastro de desenvolvedor](https://my.plantnet.org/signup), criar somente uma conta permitida por pessoa/entidade e confirmar os termos vigentes.
2. Entrar na conta e conferir que o plano exibido é **Free (€0)**, não Pro, e que a quota disponível comporta sete identificações. A página pública anuncia 500 identificações/dia, mas não comprova o plano ou o consumo atual da conta concreta.
3. Em `/settings/api-key`, gerar ou localizar a chave privada. Não habilitar exposição CORS para este benchmark backend-side.
4. Colocar o valor somente no ambiente/cofre do executor como `PlantNet__ApiKey`; se a base precisar ser explicitada, usar `PlantNet__BaseUrl`. Não enviar valores pelo chat nem gravá-los no Git.
5. Manter o teto local de sete slots Pl@ntNet, concorrência 1, timeout 20 segundos e zero retry. A documentação pública consultada não demonstra um limite configurável de conta exatamente igual a sete; portanto, a suficiência desse controle local e a ausência de contrato/cobrança Pro ainda exigem confirmação humana antes de U-101.

Gate U-101 específico: confirmar que a conta escolhida está no plano gratuito, sem contrato Pro ou cobrança aplicável; aceitar a política de dados para as sete imagens candidatas; confirmar a quota disponível e aceitar explicitamente que o teto de sete é imposto pelo executor, não por um hard limit de conta documentado. O endpoint/base local usa as configurações `PlantNet:BaseUrl` e `PlantNet:ApiKey`, representáveis por `PlantNet__BaseUrl` e `PlantNet__ApiKey`; nenhum valor foi lido ou registrado.

## Plant.id by Kindwise

Fontes oficiais reconsultadas em 2026-09-10:

- [Documentação Plant.id](https://plant.id/docs) e [exemplo oficial v3](https://github.com/flowerchecker/plant-id-examples/blob/master/README.md): `POST https://api.plant.id/v3/identification`, imagens no corpo e autenticação no header `Api-Key`.
- [Handbook](https://www.kindwise.com/handbook): chave necessária; uso recomendado do header; resultados de identificação recuperáveis por até seis meses; nomes, sinônimos e imagens representativas possuem campos e condições próprias.
- [Pricing](https://www.kindwise.com/pricing): 100 créditos gratuitos após cadastro e créditos pagos por identificação depois da franquia; a gratuidade inicial é trial, não prova uma alternativa gratuita durável.
- [Admin panel FAQ](https://www.kindwise.com/faqs-admin-panel): créditos precisam ser atribuídos à chave; limites diário/semanal/mensal podem ser configurados como hard limit; alertas isolados não bloqueiam consumo.
- [API FAQ](https://www.kindwise.com/faq): uso é baseado em créditos, comunicação usa HTTPS/TLS e a documentação pública descreve armazenamento em Google Cloud Storage e dados relacionais na DigitalOcean.
- [Terms and Conditions](https://web.plant.id/wp-content/uploads/2023/04/Terms-and-Conditions.pdf): requisição aceita deduz crédito; o trial tem condições próprias e pode ser alterado ou encerrado. A versão contratual exibida na conta prevalece e deve ser aceita pelo responsável.
- [Privacy policy](https://www.kindwise.com/privacy-policy): política pública geral da Kindwise. Ela não resolve sozinha retenção, base legal e eventual contrato específico da conta/API para as imagens do corpus.

Passos humanos para criar ou conferir a conta de trial:

1. Seguir o link **Get plant.id API key**/[cadastro de API](https://www.kindwise.com/plant-id), criar a conta Kindwise e confirmar os termos efetivos exibidos. O material público informa 100 créditos gratuitos após o cadastro, mas o saldo concreto deve ser conferido no painel.
2. No Admin Panel, usar **Create new API key**, escolher o serviço `plant.id`, nomear uma chave isolada para P04 e atribuir somente créditos gratuitos; não ativar `plant.health` nem endpoints adicionais que consumam créditos extras.
3. Confirmar ao menos sete créditos de trial disponíveis para a chave. Não cadastrar faturamento ou meio de pagamento, não comprar créditos e não habilitar modalidade retroativa.
4. Nos detalhes da chave, configurar **Usage limit** — não apenas **Usage alert** — em sete créditos na janela adequada. A documentação informa janelas móveis diária, semanal ou mensal e que o usage limit bloqueia consumo excedente; conferir que uso prévio da janela não inviabiliza os sete slots.
5. Colocar a chave somente no ambiente/cofre do executor como `P04_PLANT_ID_API_KEY`. Não usar `VITE_PLANT_ID_API_KEY`, não enviar o valor pelo chat e não gravá-lo no Git.

Gate U-101 específico: conta Kindwise/Plant.id com ao menos sete créditos de trial disponíveis; nenhuma compra, faturamento retroativo, recarga ou cobrança; chave isolada com usage limit de sete créditos; requisições sem `plant.health` ou detalhes pagos; aceitação explícita da retenção/armazenamento e dos termos efetivos da conta. Não existe configuração backend Plant.id no produto. Para o executor efêmero, o nome documental esperado é `P04_PLANT_ID_API_KEY`; nenhum valor foi lido ou registrado.

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

## Fronteira humana U-101

O checklist exigido para liberar a primeira transmissão é:

1. Aprovar ou rejeitar em conjunto os sete bytes candidatos existentes em `/var/tmp/scanplant-p04-f1-api01-corpus-20260910` e seus SHA-256. O sexto caso proposto é *Bellis perennis*; a `daisy.jpg` local foi substituída e não integra o corpus candidato.
2. Conferir, para cada caso, a página da obra, URL original/downloadada, autor, licença/versão, atribuição, referência POWO, inspeção visual e relatório de sanitização registrados em `corpus-manifest.json`; então congelar explicitamente os sete hashes e autorizar exatamente esses bytes, sem presumir que a preparação técnica já constitui aprovação humana.
3. Contas Pl@ntNet e Kindwise/Plant.id disponíveis no executor controlado. Disponibilizar os valores de `PlantNet__ApiKey` e `P04_PLANT_ID_API_KEY` somente no ambiente/cofre do executor; não enviar chaves no chat.
4. Confirmação de que Pl@ntNet está no plano gratuito aplicável e que Plant.id usará somente créditos gratuitos de trial já disponíveis; nenhuma compra, meio de pagamento ativo para consumo, recarga ou cobrança automática.
5. Limite de sete créditos por **Usage limit** na chave Kindwise/Plant.id e teto local de sete chamadas Pl@ntNet, total de 14 identificações, concorrência 1, timeout 20 segundos e sem retry. Confirmar que saldo/quota e eventual uso anterior suportam esse teto sem custo; confirmar também que o controle local Pl@ntNet é aceitável, pois não foi localizado um hard limit de conta configurável exatamente em sete.
6. Aceitação consciente das condições vigentes registradas acima, incluindo histórico do Pl@ntNet e retenção/infraestrutura publicada pela Kindwise, ou indicação de que algum provider deve ser declarado inelegível. Não haverá substituição silenciosa nem gasto para completar a matriz.
7. Autorização explícita U-101 para iniciar as transmissões. A aprovação do plano P04 já registrada não concede esta autorização.

Em 2026-09-10T22:14:38Z, o responsável humano confirmou os sete itens em conjunto: revisão visual; aceitação das fontes, licenças e atribuições; ausência de pessoas, dados pessoais e localização; aceitação das condições de privacidade/retenção; plano Free e quota Pl@ntNet suficientes com teto local exato de sete; ao menos sete créditos gratuitos Plant.id com `Usage limit` de sete; ausência de compra, recarga, cobrança automática ou retroativa e `plant.health`; duas credenciais somente nas variáveis documentadas; e autorização de exatamente 14 transmissões dos sete bytes congelados, sem retry e sem chamadas textuais.

## Preflight sem transmissão e contrato executável

O preflight confirmou branch `bm/v2-p03`, HEAD/upstream/remoto `494cf7ad0bf7f031af4ca7667b531c83d59f2d07`, divergência 0/0 e somente os seis arquivos documentais permitidos modificados. Os sete arquivos e seus hashes, MIME, dimensões e tamanhos coincidem com `corpus-manifest.json`; os seis JPEG não contêm segmentos APP0–APP15 nem COM, e o PNG contém somente `IHDR`, `IDAT` e `IEND`. A inspeção visual humana e a revisão local confirmaram ausência de pessoas, texto identificável e localização. Os dois JSON e `SHA256SUMS` passaram.

As variáveis `PlantNet__ApiKey` e `P04_PLANT_ID_API_KEY` estavam presentes e não vazias; nenhum valor, tamanho, prefixo, sufixo ou hash foi lido ou registrado. Não há variável de proxy configurada, o executor e PID 1 usam o mesmo namespace de rede, DNS e HTTPS com validação TLS alcançaram `my-api.plantnet.org` e `api.plant.id`, e uma escrita efêmera com fsync, substituição atômica e releitura passou em `/var/tmp`. Há espaço e inodes amplos no filesystem comum ao corpus e ao workspace.

As fontes oficiais registradas fixam o envio Pl@ntNet como `POST https://my-api.plantnet.org/v2/identify/all?api-key=...&nb-results=1`, uma parte multipart `images`, com `organs` omitido para o default oficial `auto`; o top-1 científico é `results[0].species.scientificNameWithoutAuthor`, a versão é o campo top-level `version`, e `404 Species not found` é `no_match`. Para Plant.id, o envio é `POST https://api.plant.id/v3/identification`, header `Api-Key` e corpo JSON somente com `images`, contendo base64 dos mesmos bytes; o top-1 é `result.classification.suggestions[0].name`, o controle usa `result.is_plant.binary`, a versão é `model_version`, o estado é `status` e `access_token`, se presente, será persistido somente como SHA-256. Nenhum detalhe, localização, data, chamada textual ou saúde vegetal será solicitado.

Plant.id permanece comparação técnica de trial e não satisfaz por si só a definição documental de alternativa gratuita durável após os créditos iniciais. Mesmo com matriz completa, a regra humana desta execução mantém `selection=none` se qualquer provider for inelegível. P01 e P03-R6 permanecem blocked-terminal, P02 permanece completed e o release continua pending.
