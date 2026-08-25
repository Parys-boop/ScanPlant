# SD-001 — Spec futura: fallback externo de plantas

Após F1-BE01, `docs/bianchini/current/specs/external-plant-fallback.md` descreverá integralmente este domínio.

## Propriedade e contrato

O backend ScanPlant possui `POST /api/plant-identification/fallback`, autenticado por JWT, e é o único componente autorizado a chamar providers botânicos. O contrato público recebe uma imagem multipart única e `consentToExternalProcessing=true`; devolve dados ScanPlant normalizados, sem expor fornecedor. D-001, D-002.

## Providers substituíveis

`IPlantIdentificationProvider` aceita `PlantIdentificationRequest` e devolve `PlantIdentificationResult`; `IPlantKnowledgeProvider` aceita `PlantKnowledgeRequest` e devolve `PlantKnowledgeResult?`. Pl@ntNet é a implementação inicial de identificação. Groq é implementação opcional de conhecimento. Plant.id não integra este domínio até decisão futura explícita. D-001, D-003.

## Invariantes de segurança

- Segredos, URLs de provider e modelos ficam apenas na configuração secreta do backend.
- Imagem é limitada, validada por MIME, assinatura/formato e dimensões, usada transitoriamente e nunca persistida por este domínio.
- Consentimento ausente/falso impede qualquer chamada externa.
- Rate limit é por `NameIdentifier`; timeout e cancelamento não geram retry automático.
- 429 e indisponibilidade retornam ProblemDetails seguro; conhecimento opcional não invalida identificação existente.
- Não há entidade, migration, armazenamento ou reuso de imagem. D-004, P-002, P-003.

## Testabilidade e operação

Todos os seams aceitam fakes/handlers HTTP falsos. Testes normais não chamam rede nem consomem créditos. Teste real Pl@ntNet exige `SCANPLANT_RUN_EXTERNAL_TESTS=1` e `PlantNet__ApiKey`; ausência de ambos significa skip explícito. U-002.
