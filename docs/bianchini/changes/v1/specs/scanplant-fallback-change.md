# Mudança ScanPlant — F1-BE01: fallback externo seguro

## Objetivo e limites

O backend passa a ser a única fronteira para identificação botânica externa e conhecimento complementar. O mobile mantém câmera, galeria, geolocalização e persistência existentes, mas solicita confirmação antes de enviar a imagem à API ScanPlant. Este ciclo não modifica Nominatim, `scanplant-web`, dataset, modelo botânico, banco, migrations ou a prova PT-05. D-004, A-001, SD-001, SD-002.

## Arquitetura e seams

`PlantIdentificationController` recebe o upload e chama `ExternalFallbackService`. O serviço valida a entrada e orquestra `IPlantIdentificationProvider` seguido, quando habilitado, de `IPlantKnowledgeProvider`. Adaptadores Pl@ntNet/Groq isolam autenticação, request/response e códigos dos fornecedores. DTOs de fornecedor são internos aos adaptadores; o controller expõe somente DTOs ScanPlant. D-001, D-002, D-003, S-001.

## Contrato público

### POST /api/plant-identification/fallback

- Requer JWT válido e rate limit por usuário autenticado.
- Consome `multipart/form-data` com exatamente `image` e `consentToExternalProcessing=true`.
- A imagem deve estar dentro de limite configurado, ter MIME permitido, assinatura correspondente e dimensões aceitáveis; nome/extensão do cliente não são confiáveis e o arquivo não é persistido.
- Responde `ExternalFallbackResponseDto` com `source=external_fallback`, `matchStatus`, identificação normalizada, candidatos normalizados e conhecimento opcional/status. O DTO não contém provider, chave, URL, payload ou mensagem bruta de upstream.
- Falhas públicas: 400 para consentimento/imagem inválida, 401 para autenticação, 413 para tamanho, 415 para formato, 429 com `Retry-After` quando aplicável, 502/503 para indisponibilidade controlada e 504 para prazo excedido. Sem sugestão é resposta normal com `matchStatus=no_match`.

## Entidades e estados

`PlantIdentificationRequest` contém stream/imagem validada e metadados normalizados. `PlantIdentificationResult` contém candidatos científicos e score; `PlantKnowledgeRequest` só contém identidade textual normalizada; `PlantKnowledgeResult` contém campos de cuidado opcionais. `ExternalFallbackResult` combina os dois, sem persistência. D-002, D-003, SD-001.

Estados: `captured` → `awaiting_external_consent` → `uploading` → `identified|no_match|controlled_failure`; cancelar em `awaiting_external_consent` ou abortar a requisição não chama provider. A-001, P-001.

## Segurança, concorrência e integrações

Credenciais e seleção dos adaptadores vêm de ambiente/cofre do backend; `appsettings.json` só guarda chaves de configuração não secretas. `HttpClientFactory` e um prazo configurável criam token ligado a `RequestAborted`. Não há retry automático após timeout/429. O limitador local usa chave do `NameIdentifier` do JWT e devolve 429; um 429 externo é traduzido preservando somente `Retry-After` seguro. P-002, P-003, U-002.

Pl@ntNet é o provider inicial. Plant.id não é incluído. Groq é opcional: falha de Groq reduz `knowledgeStatus` e registra evento seguro, mas não descarta identificação obtida. Dados de imagem não seguem para Groq. D-001, D-003.

Antes de executar código, U-001 exige atualizar `origin` quando houver rede e obter autorização para o merge não-rebase. A-002 limita a análise atual à referência local já comparada; a divergência deve ser reavaliada somente após a ação autorizada.

## Jornada mobile e plataformas

Após captura ou escolha, `PhotoScreen` não chama fornecedor. Exibe aviso de envio externo; aceite manda multipart autenticado exclusivamente a `/api/plant-identification/fallback`; recusa mantém a foto local e permite cancelar/tentar depois. O cliente usa a descoberta e JWT existentes. Nominatim/geolocalização e a aplicação web não são tocados. P-001, A-001, SD-002.

## Dados, observabilidade e testes

Não há nova entidade ou migration. Logs estruturados registram somente categoria, provider interno, status e correlação; não registram bytes, nome de arquivo, chave ou payload externo. Fakes e handlers HTTP falsos cobrem mapeamentos, entrada, cancelamento, 429 e erros. Teste real Pl@ntNet só ocorre com flag e chave de ambiente explícitas. P-002, P-003, P-004, U-002.

## Referências

- Plano canônico, seções 2, 4, 5, 6 e 8.
- CHECKPOINT_FASE0_OFFLINE.md — prova PT-05 preservada.
- F1-G01 — nenhum modelo botânico de produto aprovado.
- STACK_RESEARCH.md — contratos e segurança de upload/fornecedores.
