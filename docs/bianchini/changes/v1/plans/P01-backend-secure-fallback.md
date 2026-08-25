# P01 — Backend: fallback externo seguro

**Risco:** high
**Política calculada:** `strict`, `per_task`, mutação `required_selective`, no máximo 3 fix rounds para o seam `external-fallback`.
**Dependência externa antes da execução:** U-001.

### Tarefa 1 — Contratos neutros, configuração secreta e validação segura de upload disponíveis no backend

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-001, D-002, D-004, A-002, P-002, P-004, U-001, S-001, SD-001

**Test seams:** `IPlantIdentificationProvider`, `IPlantKnowledgeProvider`, validador de imagem, opções de fallback

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#arquitetura-e-seams, docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#segurança-concorrência-e-integrações, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#invariantes-de-segurança

**Files:** `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/`, `ScanPlantAPI/ScanPlantAPI/DTOs/Identification/`, `ScanPlantAPI/ScanPlantAPI/Program.cs`, `ScanPlantAPI/ScanPlantAPI/appsettings.json`, `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj`, `ScanPlantAPI/ScanPlantAPI.Tests/`, `ScanPlantAPI/ScanPlantAPI.sln`, `.config/dotnet-tools.json`

**Contract:** criar requests/results internos e DTO público sem campos de fornecedor; registrar opções não secretas, clients e rate limiter por `NameIdentifier`; aceitar somente uma imagem transitória que passe limite, MIME, assinatura/formato e dimensões. Nenhuma chave é versionada, nenhuma imagem é persistida, nenhuma migration é criada. O projeto de teste e ferramenta de mutação são adicionados com versões fixadas, sem atualizar dependências existentes.

**Verification:** `dotnet test ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release`

**Done when:** fakes de contratos e testes de entrada cobrem ausência, consentimento futuro incompatível, tamanho, MIME, assinatura e dimensão; o projeto de testes compila; não há migration nem segredo versionado.

### Tarefa 2 — Endpoint autenticado orquestra Pl@ntNet/Groq com cancelamento, limite e falhas controladas

**Execution:** strict

**Review:** per_task

**Change:** integration

**Readiness refs:** D-001, D-002, D-003, P-002, P-003, U-001, U-002, SD-001

**Test seams:** `POST /api/plant-identification/fallback`, `ExternalFallbackService`, handler HTTP Pl@ntNet falso, handler HTTP Groq falso

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#contrato-público, docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#segurança-concorrência-e-integrações, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#providers-substituíveis

**Files:** `ScanPlantAPI/ScanPlantAPI/Controllers/PlantIdentificationController.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/PlantNetIdentificationProvider.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/GroqPlantKnowledgeProvider.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalProviderExceptions.cs`, `ScanPlantAPI/ScanPlantAPI/Program.cs`, `ScanPlantAPI/ScanPlantAPI.Tests/`

**Contract:** endpoint exige JWT e consentimento verdadeiro, usa RequestAborted e prazo configurável, limita requisições por usuário e mapeia resposta Pl@ntNet para DTO neutro. Groq recebe somente nome científico normalizado e é opcional. 429 preserva Retry-After seguro; timeout/cancelamento não tenta novamente; falha opcional de conhecimento mantém identificação. Plant.id permanece ausente.

**Verification:** `dotnet test ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --configuration Release --filter FullyQualifiedName~ExternalFallback`

**Done when:** integração com token de teste e fakes prova 401, consentimento ausente, upload inválido, sucesso, no_match, rate limit local, 429 upstream, timeout, cancelamento e falha Groq opcional; nenhuma chamada externa acontece.

### Tarefa 3 — Garantia seletiva sem crédito e caminho real opt-in estão documentados no harness

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** P-003, P-004, U-002, SD-001

**Test seams:** validators, tradução de status de provider, guard do teste externo

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#dados-observabilidade-e-testes, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#testabilidade-e-operação

**Files:** `ScanPlantAPI/ScanPlantAPI.Tests/`, `.config/dotnet-tools.json`, `ScanPlantAPI/ScanPlantAPI/README.md`

**Contract:** testes ordinários usam somente doubles; o teste real de Pl@ntNet é marcado e skipado sem `SCANPLANT_RUN_EXTERNAL_TESTS=1` e `PlantNet__ApiKey`. A mutação seletiva alcança somente validação/orquestração alteradas; não há teste real de Groq nem consumo por padrão.

**Verification:** `dotnet stryker --solution ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln --project ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj`

**Done when:** mutação seletiva é executável e qualquer sobrevivente que altere consentimento, limite, status ou cancelamento recebe teste ou justificativa de equivalência; o comando externo continua explicitamente opt-in.
