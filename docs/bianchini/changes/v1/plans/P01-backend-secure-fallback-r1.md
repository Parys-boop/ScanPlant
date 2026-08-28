# P01-R1 — Garantia de mutação pós-breaker do fallback externo

**Risco:** high
**Mecanismo formal:** revisão versionada do P01 após `material_change` invalidante; substitui somente a Tarefa 3 bloqueada e preserva as Tarefas 1 e 2 já concluídas.
**Política preservada:** `strict`, `per_task`, mutação `required_selective`, seam `external-fallback` acumulado em 3/3. O breaker permanece ativo até esta revisão ser aprovada; não há reset, renomeação de seam ou novo orçamento automático.
**Readiness herdado:** D-001, D-002, D-003, D-004, A-002, P-002, P-003, P-004, U-001, U-002, S-001, SD-001.

## Objetivo limitado e contratos preservados

Matar ou provar concretamente a equivalência dos sobreviventes materiais `982`, `1010`, `1012`, `1020`, `1026` e `1028`, e dar cobertura ou justificativa formal aos no-coverage que alcançam invariantes de segurança. O contrato HTTP, os DTOs neutros, o consentimento antes de qualquer provider, o limite de upload/dimensões/buffer, cancelamento/timeout sem retry, a tradução controlada de status e a degradação opcional de Groq permanecem inalterados.

Arquivos de produção permitidos, somente se uma asserção nova falhar contra o HEAD: `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs`. Arquivos de teste permitidos: `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/` e testes focados existentes de fallback. Não são permitidos providers reais, rede, banco, créditos, credenciais, migration, mobile, `scanplant-web` ou Nominatim.

## Inventário e hipótese causal

| Mutante | Região / operador / mudança | Comportamento e invariante | Classificação |
| --- | --- | --- | --- |
| 982 | `ExternalFallbackUploadValidator.cs:52`; BinaryExpression; `>` para `>=` | Rejeita exatamente `MaxImageBytes`, embora o limite contratado aceite `<= MaxImageBytes`; P-002 / SD-001 | lacuna de teste material |
| 1010 | `ExternalFallbackUploadValidator.cs:80`; BinaryExpression; largura `>` para `>=` | Rejeita largura exatamente máxima; dimensão válida no limite deve ser aceita; P-002 / SD-001 | lacuna de teste material |
| 1012 | `ExternalFallbackUploadValidator.cs:80`; BinaryExpression; altura `>` para `>=` | Rejeita altura exatamente máxima; dimensão válida no limite deve ser aceita; P-002 / SD-001 | lacuna de teste material |
| 1020 | `ExternalFallbackUploadValidator.cs:102`; Linq; `Math.Min` para `Math.Max` | Aloca chunk pelo máximo, podendo extrapolar a alocação transitória limitada; P-002 / SD-001 | lacuna de teste material, com risco de exaustão de memória |
| 1026 | `ExternalFallbackUploadValidator.cs:107`; BinaryExpression; `>` para `>=` | Rejeita stream com exatamente `MaxImageBytes`, quebrando o mesmo limite seguro; P-002 / SD-001 | lacuna de teste material |
| 1028 | `ExternalFallbackUploadValidator.cs:107`; BinaryExpression; `buffer.Length + read` para `buffer.Length - read` | Permite contabilidade subestimada e bytes acima do limite; P-002 / SD-001 | lacuna de teste material, com risco de buffer sem limite |

Hipótese inicial: o harness cobre rejeições acima do limite e dimensões excedidas, mas não as fronteiras iguais nem um stream que cruza o limite durante a leitura. Não há evidência de defeito de implementação no HEAD até uma asserção de fronteira falhar. Um resultado diferente classifica o achado como defeito e limita a menor alteração de produção aos dois arquivos permitidos.

## No-coverage da campanha anterior

| IDs | Região | Categoria | Tratamento obrigatório |
| --- | --- | --- | --- |
| 933 | `ExternalFallbackService.cs:58` | tradução de status para `no_match` | testar resultado neutro sem candidatos, ou justificar que o DTO não expõe o literal mutado. |
| 938, 939, 940, 941, 942 | `ExternalFallbackService.cs:73` | degradação opcional de Groq | testar conhecimento nulo/disponível e os dois status observáveis. |
| 944 | `ExternalFallbackService.cs:77` | cancelamento | testar propagação de `RequestAborted`; nenhuma equivalência por conveniência. |
| 946 | `ExternalFallbackService.cs:81` | timeout e Groq opcional | testar retorno neutro de timeout sem retry e identificação preservada. |
| 959, 961, 962 | `ExternalFallbackService.cs:103-111` | tradução controlada de indisponibilidade | testar que 503/indisponibilidade permanece neutra, sem detalhes de provider. |
| 964 | `ExternalFallbackUploadValidator.cs:21` | segurança de buffer/leitura somente | testar que a imagem validada expõe stream não gravável, ou provar pelo contrato do construtor que a mutação é inobservável. |
| 1029 | `ExternalFallbackUploadValidator.cs:108` | segurança do buffer | testar stream que excede durante leitura e deve rejeitar antes de provider. |
| 1036, 1037 | `ExternalFallbackUploadValidator.cs:123-124` | formato permitido e segurança de upload | testar JPEG permitido e formato desconhecido rejeitado. |

Não há no-coverage direto de consentimento ou de ausência de retry nesta campanha; ambos continuam invariantes de Tarefa 1 porque os testes existentes já os exercem e uma mutação futura pode reabrir a prova. A tabela não converte nenhum item automaticamente em aprovado: cobertura ou justificativa concreta é exigida para as linhas de segurança.

## Redesenho exigido pelo breaker

Esta revisão registra a nova hipótese de garantia, sem alterar a arquitetura de produto. Máquina de estados: `received` → `declared-limit-checked` → `buffered-within-limit` → `decoded` → `dimensions-checked` → `validated` → `provider-eligible`; terminais `rejected` e `request-cancelled`. Nenhum provider é elegível antes de `validated` e testes não cruzam a fronteira de rede.

O único efeito irreversível potencial é a chamada do provider, posterior à validação; a revisão não a executa. Não há persistência, transação, actor concorrente, crédito ou estado durável para retomar. Cancelamento ou crash no caminho em memória descartam o buffer; timeout/cancelamento não fazem retry. Matriz de falhas: igualdade de limite/dimensão preserva aceitação; excesso declarado ou lido rejeita antes de provider; buffer inseguro rejeita; `RequestAborted` propaga; timeout devolve falha neutra; 429/indisponibilidade mantém tradução controlada; falha Groq mantém identificação com conhecimento degradado.

### Tarefa 1 — Fronteiras de upload e buffer são demonstradas no harness puro

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-001, D-002, D-003, D-004, A-002, P-002, P-003, P-004, U-001, U-002, S-001, SD-001

**Test seams:** `ExternalFallbackUploadValidator`, `ReadWithinLimitAsync` exercido por upload, `ExternalFallbackService`

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#segurança-concorrência-e-integrações, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#invariantes-de-segurança

**Files:** `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/`, `ScanPlantAPI/ScanPlantAPI.Tests/`

**Contract:** adicionar somente testes puros que aceitem payload exatamente em `MaxImageBytes`, largura/altura exatamente máximas e leitura fragmentada exatamente no limite; rejeitem o primeiro byte acima e não aceitem contabilidade subtraída ou chunk não limitado. Revalidar ausência de consentimento, cancelamento/timeout sem retry, tradução controlada e Groq opcional sem rede.

**Verification:** `env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet test ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj --framework net8.0 --configuration Release`

**Done when:** os mutantes 982, 1010, 1012, 1020, 1026 e 1028 são atingidos por asserções observáveis; no-coverage de consentimento, upload, buffer, timeout, cancelamento, status e Groq recebe teste ou justificativa formal sem inventar equivalência.

### Tarefa 2 — A menor correção de produto, somente se a fronteira provar defeito, preserva a coreografia segura

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** D-002, D-004, P-002, P-003, P-004, SD-001

**Test seams:** `ExternalFallbackUploadValidator`, `ExternalFallbackService`, fakes de identificação/conhecimento

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#segurança-concorrência-e-integrações, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#invariantes-de-segurança

**Files:** `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackUploadValidator.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs`, `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/`, `ScanPlantAPI/ScanPlantAPI.Tests/`

**Contract:** somente se a Tarefa 1 provar falha no comportamento aprovado, corrigir a menor expressão de limite, buffer ou cancelamento necessária para restaurar o invariante, sem alterar DTO, status público, provider, retry, timeout, consentimento ou target de produção. Se a Tarefa 1 estiver verde, esta tarefa não altera produção.

**Verification:** `env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet test ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj --framework net8.0 --configuration Release --filter FullyQualifiedName~ExternalFallback`

**Done when:** testes afetados ficam verdes e nenhuma chamada externa, credencial, crédito, banco ou provider real é usado.

### Tarefa 3 — O gate seletivo declarado decide a garantia sem ampliar o backend

**Execution:** strict

**Review:** per_task

**Change:** security

**Readiness refs:** P-002, P-003, P-004, SD-001

**Test seams:** `ExternalFallbackUploadValidator`, `ExternalFallbackService`, relatório Stryker do harness

**Spec refs:** docs/bianchini/changes/v1/specs/scanplant-fallback-change.md#dados-observabilidade-e-testes, docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md#testabilidade-e-operação

**Files:** `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/`, `.config/dotnet-tools.json`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackUploadValidator.cs`, `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs`

**Contract:** restaurar o `dotnet-stryker` 4.16.0 declarado e executar, a partir do harness, SDK isolado 8.0.424, `net8.0`, concorrência 1, sem solution mode e somente nos dois arquivos aprovados. Logs e relatórios ficam em `/tmp`; nenhuma dependência adicional é atualizada.

**Verification:** `cd ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness && env DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8 PATH=/home/arthur/.dotnet-scanplant-8:$PATH dotnet tool run dotnet-stryker --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --mutate Services/ExternalProviders/ExternalFallbackUploadValidator.cs --mutate Services/ExternalProviders/ExternalFallbackService.cs --output /tmp/scanplant-p01r1-mutation`

**Done when:** todos os seis sobreviventes materiais são mortos ou têm prova concreta de equivalência; no-coverage de invariante de segurança é coberto ou justificado; o escopo efetivo contém somente os dois arquivos; não há score global novo.

## Semântica de resultados e regra de parada

`Killed` e timeout reproduzível que detecta alteração material contam como detecção, não como aprovação por percentual. `Survived` bloqueia quando altera consentimento, limite, buffer, status ou cancelamento; somente equivalência concreta, baseada no contrato e no teste observável, pode encerrar um sobrevivente. `NoCoverage` de segurança exige teste ou justificativa; os demais são inventariados, não aprovados nem reprovados automaticamente. `CompileError` é mutação inexequível e não conta como morta; deve ser registrado e revisto. `Ignored` é exclusão/filtro da ferramenta e não transfere prova. Os timeouts 928 (remoção de `CancelAfter`) e 1022 (loop `ReadAsync >= 0`) devem permanecer reproduzíveis, limitados e classificados como detecção de timeout/cancelamento; se forem flake ou ambiente, bloqueiam.

Não existe segunda execução corretiva automática. Após uma campanha final, qualquer mutante material sobrevivente, no-coverage de segurança sem prova, timeout não reproduzível, erro de produto, necessidade de nova dependência ou segunda alteração de produção encerra P01-R1 como bloqueado para nova decisão formal do supervisor. P02 não inicia antes da conclusão do P01 revisado.
