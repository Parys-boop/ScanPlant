# P02 — Mobile: cliente consentido da API ScanPlant

**Risco:** medium
**Política calculada:** `slice`, `per_slice`, mutação não requerida.
**Dependência:** P01 concluído; U-001 resolvida antes de iniciar execução.

### Tarefa 1 — Tela móvel solicita consentimento e usa somente a API ScanPlant para fallback

**Execution:** slice

**Review:** per_slice

**Change:** authorization

**Readiness refs:** D-002, D-004, A-001, P-001, S-001, SD-002

**Test seams:** `PhotoScreen` consent gate, método multipart em `api.js`, resposta `ExternalFallbackResponseDto`

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#jornada-mobile-e-plataformas, docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md#jornada, docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md#fronteira-de-rede

**Files:** `ScanPlant-Final/components/PhotoScreen.js`, `ScanPlant-Final/components/api.js`, `ScanPlant-Final/.env.example`

**Contract:** captura/galeria preservam foto e pedem confirmação explícita antes do fallback. Ao aceitar, `api.js` envia `image` e `consentToExternalProcessing=true` ao endpoint ScanPlant com JWT e sem header manual multipart incompatível. Ao recusar, não envia rede. A resposta neutra atualiza os campos existentes. Remover Plant.id/Groq, URLs, headers e chaves correspondentes do bundle/exemplo. Não modificar Nominatim, geolocalização, PT-05, App.js, AppMain.js ou `scanplant-web`.

**Verification:** `git diff --check`

**Done when:** inspeção focada confirma que identificação/conhecimento móveis só usam API ScanPlant, consentimento precede o upload e não restam referências executáveis a Plant.id/Groq no mobile; o fluxo PT-05 permanece intocado e seus testes não são repetidos.

### Tarefa 2 — Falhas controladas do endpoint preservam a jornada de foto sem expor detalhes externos

**Execution:** slice

**Review:** per_slice

**Change:** behavioral

**Readiness refs:** A-001, P-001, SD-002

**Test seams:** mapeamento de ProblemDetails para mensagens da tela, estados loading/erro/cancelar

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#contrato-público, docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md#estados-e-falhas

**Files:** `ScanPlant-Final/components/PhotoScreen.js`, `ScanPlant-Final/components/api.js`

**Contract:** 400/413/415/429/502/503/504 recebem mensagens locais seguras e mantêm a foto; o mobile não mostra resposta bruta, URL ou nome de provider. O estado `no_match` não é erro de transporte e a indisponibilidade de conhecimento não apaga uma identificação recebida.

**Verification:** `git diff --check`

**Done when:** os estados de UI cobrem aceite, recusa, no_match e falhas públicas com mensagem compreensível; não é introduzida dependência mobile nem alteração fora dos arquivos permitidos.
