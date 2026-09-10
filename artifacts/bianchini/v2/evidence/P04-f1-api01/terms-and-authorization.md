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

Plant.id permanece comparação técnica de trial e não satisfaz por si só a definição documental de alternativa gratuita durável após os créditos iniciais. A autorização humana da coleta acrescentou a instrução de manter `selection=none` se houvesse provider inelegível; essa restrição explica a decisão inicial preservada no ledger. A revisão offline abaixo distingue essa instrução de execução dos critérios de elegibilidade por papel do contrato aprovado. P01 e P03-R6 permanecem blocked-terminal, P02 permanece completed e o release continua pending.

## Resultado da coleta autorizada

A coleta única ocorreu entre 2026-09-10T22:26:20.753Z e 2026-09-10T22:26:51.679Z a partir do checkpoint `4aa485eafcca167f753d70e5e579d8a3fd4cbb88`. Foram iniciadas e concluídas exatamente sete chamadas Pl@ntNet e sete Plant.id, em 14 slots únicos, concorrência 1, sem repetição, timeout, falha, retry, chamada textual ou `plant.health`. Todas as respostas HTTP esperadas foram JSON válido: Pl@ntNet retornou 200 nos sete casos e versão `2026-03-20 (7.5)`; Plant.id retornou 201 nos sete casos, estado `COMPLETED` e versão `plant_id:5.1.1`. Identificadores Plant.id foram persistidos somente como SHA-256, e nenhuma resposta bruta, chave ou header de autenticação foi registrado.

Pl@ntNet acertou `Epipremnum aureum`, `Monstera deliciosa`, `Zamioculcas zamiifolia` e `Bellis perennis`; errou `Spathiphyllum wallisii` como `Spathiphyllum floribundum`, `Dracaena trifasciata` como `Dracaena zeylanica` e o controle sem planta como `Hedera helix`. Resultado: 4/7 (57,14285714%), disponibilidade 7/7, mediana 2556 ms e pior duração 2773 ms.

Plant.id acertou `Epipremnum aureum`, `Monstera deliciosa`, `Zamioculcas zamiifolia`, `Dracaena trifasciata`, `Bellis perennis` e rejeitou corretamente o controle sem planta; errou `Spathiphyllum wallisii` como `Zantedeschia aethiopica`. Resultado: 6/7 (85,71428571%), disponibilidade 7/7, mediana 2304 ms e pior duração 3280 ms.

A comparação técnica favorece Plant.id em acertos e no controle sem planta. A revisão independente corrigiu a conclusão para **Pl@ntNet principal gratuito e Plant.id secundário técnico de trial**, sem aprovar Plant.id como alternativa gratuita contínua. O responsável humano aprovou essa interpretação e a revisão da slice em 2026-09-10; P04 está completed. O release permanece pending.

## Revisão final independente offline — 2026-09-10

Esta revisão leu integralmente plano, spec, spec-delta, planning review, protocolo F1-API01, PROJECT_STATE, ledger e os quatro arquivos de evidência. Nenhuma skill, API, slot, credencial, download ou execução de produto foi usada. As variáveis `PlantNet__ApiKey` e `P04_PLANT_ID_API_KEY` estavam ausentes; as afirmações de credenciais presentes no checkpoint e no manifesto são fatos históricos do preflight U-101, não desta sessão.

O estado local inicial e final é branch `bm/v2-p03`, HEAD e upstream `4aa485eafcca167f753d70e5e579d8a3fd4cbb88`, divergência local 0/0, seis arquivos documentais modificados e unstaged. A única tentativa de rede permitida pelo pedido foi Git somente de leitura: `ls-remote` falhou por DNS no sandbox e a tentativa fora dele terminou por timeout de 25 segundos. O remoto atual não foi reconfirmado; permanece a evidência histórica do push bem-sucedido do checkpoint antes da coleta. Não houve fetch, staging, commit ou push nesta revisão.

Antes das correções, os seis arquivos e o diff foram copiados para `/var/tmp/scanplant-p04-f1-api01-offline-review-20260910-C1jRVaco`. O arquivo `BACKUP-SHA256SUMS` contém os sete hashes e foi validado; seu SHA-256 é `bb142d09bb17e1d911ab77d523e786379a656bedb1315b9f4b4b41c35038071d`. O hash do diff original é `372fef375acf2e0f266aa0fe87aedff20633db2d7d049b31245c4fd60a1dcb3a`.

### Interpretação literal comprovada: A

As referências seguintes são aos arquivos históricos preservados no repositório, com linhas contadas antes desta revisão:

- `docs/phase1/F1-API01-benchmark-decision.md:55`: “Um provider só entra na ordenação se: o corpus e os direitos estiverem aprovados; as condições de privacidade forem aceitas; o orçamento for zero com cobrança automática desativada e limite duro; os sete slots forem únicos e completos; e as observações forem sanitizadas e reconciliadas.”
- Mesmo protocolo, linha 57: “Um provider pago/trial pode ser comparação técnica ou secundário técnico, mas não alternativa gratuita aprovada.”
- Mesmo protocolo, linha 59: “O melhor elegível e gratuito torna-se principal; o próximo elegível torna-se secundário.” E: “Empate material, matriz parcial ou ausência de alternativa gratuita mantém a decisão sem seleção e P04 incompleto.”
- `docs/bianchini/changes/v2/specs/post-u009-continuity.md:31`: “Secundário técnico pago/trial pode constar como comparação, mas não como alternativa gratuita aprovada.”
- `docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md:7`: “Matriz incompleta ou ausência de candidato elegível mantém impedimento explícito, sem vencedor fabricado e sem declarar o marco concluído.”

Esses trechos distinguem elegibilidade geral para comparação e elegibilidade para o papel gratuito. Pl@ntNet satisfaz ambas; Plant.id satisfaz os gates da comparação e somente o papel secundário técnico de trial. O conjunto de candidatos a principal gratuito contém apenas Pl@ntNet. Plant.id ter melhor correção não o promove ao papel gratuito, nem elimina Pl@ntNet. A ausência de uma **segunda** oferta gratuita durável não é a “ausência de alternativa gratuita” prevista no protocolo, pois Pl@ntNet existe e está elegível. Nenhum dos documentos exige dois providers gratuitos, acurácia mínima ou acerto obrigatório do controle como gate eliminatório; esses resultados compõem a ordenação e permanecem publicados. Portanto, B não encontra requisito de elegibilidade faltante, e C não é necessária porque o secundário técnico está expressamente permitido.

A frase “não selecione vencedor se a matriz estiver incompleta ou houver provider inelegível” veio do pedido humano que autorizou a coleta. Ela não foi inventada pelo executor, mas também não é uma regra global do plano/spec/protocolo previamente aprovados. Aplicá-la a qualquer inelegibilidade de papel explica a seleção nula inicial; tratá-la como exigência contratual de dois providers gratuitos seria incorreto. O pedido humano atual determina reaplicar literalmente os critérios previamente aprovados. Esta correção altera somente a interpretação dos resultados; a decisão inicial e sua origem permanecem no ledger e na cópia de segurança.

### Gates dos providers e limite local Pl@ntNet

| Gate | Pl@ntNet | Plant.id |
|---|---|---|
| Direitos e privacidade | U-101 aceitou fontes, licenças, atribuições e termos para os sete hashes | Mesma autorização U-101, incluindo retenção Kindwise |
| Custo da coleta | Plano Free e quota suficiente confirmados; sem compra ou cobrança habilitada | Ao menos sete créditos gratuitos de trial; sem compra, recarga ou cobrança |
| Limite duro executado | Teto local de sete explicitamente aceito pelo humano; contador, reserva persistente e bloqueio de repetição | Usage limit de sete confirmado pelo humano e mesmo controle local |
| Completude/controle | 7/7 únicos, transmitidos e concluídos; zero retry, falha e timeout | 7/7 únicos, transmitidos e concluídos; zero retry, falha e timeout |
| Papel gratuito contínuo | Elegível para o volume documentado do piloto; plano Free publicado sem compra após trial | Inelegível: os créditos iniciais são trial |
| Papel recomendado | Principal gratuito | Secundário técnico, somente comparação de trial |

A fronteira U-101 deste documento já exigia aceitar expressamente o teto local de sete Pl@ntNet porque não se demonstrou um hard limit configurável de conta exatamente em sete. O humano o aceitou: `corpus-manifest.json#/u101_resolution/plantnet_local_hard_ceiling_accepted` é `true`. A inspeção estática do artefato temporário de coleta confirmou a verificação de contador menor que sete, teto global 14, marcador exclusivo, reserva persistida antes do envio e gravação terminal antes do próximo slot. Os journals confirmam seu cumprimento. A ausência de configuração de conta em sete não permanece bloqueante nesta autorização; não se está dispensando um controle que faltou executar.

Direitos, aceitação de termos, configuração de conta e custo zero estão comprovados no nível de evidência exigido pelo contrato: declarações humanas U-101, fontes oficiais datadas da coleta e registros locais. A revisão offline não inspecionou painéis ou faturamento, nem revalidou termos online. Os sete hashes, tamanhos, MIME, dimensões e estrutura sem APP/COM/EXIF/GPS/comentários conferem; a ausência visual de pessoas/localização permanece sustentada pela revisão humana dos mesmos bytes. Atribuições públicas necessárias foram preservadas. A recomendação limita-se ao piloto e às condições documentadas; não presume volume futuro maior, SLA, acurácia de produção ou gratuidade permanente. A substituibilidade é preservada pela decisão documental, sem integração ou mudança de código.

### Reconciliação independente dos 14 journals

Os 14 arquivos em `/var/tmp/scanplant-p04-f1-api01-exec-4aa485eafcca167f753d70e5e579d8a3fd4cbb88/slots` foram lidos e reconciliados campo a campo com as observações: checkpoint, par, identificador local, hash, início/reserva, conclusão, HTTP, status, duração, avaliação e falha. Top-1 e versões foram conferidos nas observações sanitizadas; os journals não armazenam esses campos. Não há resposta bruta preservada para uma nova extração. As avaliações foram recalculadas contra as referências/sinônimos congelados, sem confiar nos totais anteriores.

| Caso, na ordem congelada | Pl@ntNet: top-1 / avaliação / ms | Plant.id: top-1 / avaliação / ms |
|---|---|---|
| 01 — Epipremnum aureum | Epipremnum aureum / correct / 2045 | Epipremnum aureum / correct / 1960 |
| 02 — Monstera deliciosa | Monstera deliciosa / correct / 1757 | Monstera deliciosa / correct / 1875 |
| 03 — Zamioculcas zamiifolia | Zamioculcas zamiifolia / correct / 2556 | Zamioculcas zamiifolia / correct / 2478 |
| 04 — Spathiphyllum wallisii | Spathiphyllum floribundum / incorrect / 2721 | Zantedeschia aethiopica / incorrect / 2304 |
| 05 — Dracaena trifasciata | Dracaena zeylanica / incorrect / 2773 | Dracaena trifasciata / correct / 3280 |
| 06 — Bellis perennis | Bellis perennis / correct / 2596 | Bellis perennis / correct / 2553 |
| 07 — controle sem planta | Hedera helix / incorrect / 832 | null, no_match / correct / 906 |

Por provider, planejadas/iniciadas/transmitidas/concluídas = 7/7/7/7; total = 14/14/14/14. Pl@ntNet: sete HTTP 200, sete `success`, versão `2026-03-20 (7.5)`, 4 correct e 3 incorrect, 3/5 espécies-alvo, controle incorreto. Plant.id: sete HTTP 201/`COMPLETED`, seis `success` e um `no_match`, versão `plant_id:5.1.1`, 6 correct e 1 incorrect, 4/5 espécies-alvo, controle correto. Total: 10 correct, 4 incorrect, zero not_evaluable, falhas, timeouts e retries. Disponibilidade: 7/7 para ambos. Acurácia avaliada e correção estrita: 4/7 e 6/7; medianas: 2556 e 2304 ms; piores durações: 2773 e 3280 ms, respectivamente. Todas as métricas anteriores conferiram e foram preservadas.

Há exatamente um journal por `case_id`/`provider_id`, sempre Pl@ntNet antes de Plant.id, com intervalo de 9 a 22 ms entre a conclusão de um slot e o início do seguinte. Não há duplicação nem sobreposição temporal registrada. `duration_ms` mede a chamada com relógio monotônico; o intervalo UTC do slot inclui reserva/persistência e é de 6 a 11 ms maior, sem inconsistência de medição. Todos os 14 slots continuam `transmitted=true` e `call_completed=true`; nenhum journal foi alterado ou executado.

### Estado correto de P04 e revisão humana

O plano `docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md:25` estabelece: “Somente o primeiro caso completa P04/F1-API01 após revisão.” Esse primeiro caso é a decisão principal/secundário fundamentada. O planning review aprovado, `docs/bianchini/changes/v2/PLANNING_REVIEW-p04-f1-api01.md:15`, explicita: “revisão humana da slice verifica semântica/métricas.”

A revisão independente concluiu que a evidência permite os dois papéis e removeu `B-P04-NO-ELIGIBLE-SECONDARY`. Em 2026-09-10, o responsável humano aprovou a revisão da slice, a interpretação A, Pl@ntNet como principal gratuito e Plant.id como secundário técnico de trial. P04 está **completed**, sem bloqueio de trial ou exigência de dois gratuitos. O commit final único e o push exclusivo para `origin/bm/v2-p03` foram autorizados em rodada posterior à revisão.

O protocolo e os critérios aprovados em `docs/phase1/F1-API01-benchmark-decision.md` foram preservados, e o mesmo documento agora registra o resultado factual final. Plano, spec, spec-delta, planning review, manifesto aprovado e referências do corpus não foram alterados. O manifesto de aprovação conserva o digest `9657abcbb1520701a59bbd8fcecf34ff5d7a34fb901ad5d84defd6df34a31d23`; não foi regenerado para refletir arquivos vivos modificados depois da aprovação. P01/P03-R6 continuam blocked-terminal, P02 completed e release pending.
