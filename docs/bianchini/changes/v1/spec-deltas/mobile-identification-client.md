# SD-002 — Spec futura: cliente móvel de identificação

Após F1-BE01, `docs/bianchini/current/specs/mobile-identification-client.md` descreverá integralmente este comportamento.

## Jornada

`PhotoScreen` mantém captura e seleção de foto. Antes do fallback externo, mostra uma confirmação que explica o envio da imagem ao backend ScanPlant e a um serviço externo. Recusa não transmite imagem; aceite chama somente o endpoint ScanPlant autenticado em multipart. A-001, P-001.

## Fronteira de rede

Para identificação e conhecimento, o mobile usa `components/api.js` e `apiConfig.js` existentes, portanto transporta apenas JWT para a API ScanPlant. Não possui constante, variável de ambiente, URL, header ou credencial de Plant.id/Groq. Os formatos do fornecedor não chegam à tela. D-002, P-001.

## Estados e falhas

Enquanto envia, a tela informa processamento externo. A resposta normalizada atualiza os mesmos campos de identificação/cuidado consumidos pelo fluxo de salvar. 429, timeout, formato inválido e indisponibilidade mostram mensagem segura e preservam a foto para nova tentativa. Não há inferência local nova neste marco. A-001.

## Exclusões preservadas

Nominatim, permissões/localização, `scanplant-web`, dados de planta e a prova PT-05 não mudam. PT-05 continua selecionada por `App.js` e não é executada ou revalidada neste ciclo. D-004.
