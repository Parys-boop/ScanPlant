# P03-R1 — Evidência de mutação P01 vinculada à revisão atual

**Mecanismo formal:** revisão documental pré-publicação após a correção factual de cinco trailing whitespaces; substitui somente o artefato de plano P03 no pacote e preserva integralmente o contrato de execução.

## Objetivo

Produzir, em uma única campanha seletiva explicitamente autorizada, mutation evidence verificável e formalmente vinculada ao `HEAD` de `bm/v2-p02`, sem reutilizar artificialmente evidência histórica.

### Tarefa 1 — campanha seletiva e binding formal

**Execution:** strict
**Review:** per_task
**Change:** security
**Readiness refs:** D-003, A-002, P-003, U-003, SD-001
**Test seams:** mutation-observability
**Spec refs:** `docs/bianchini/changes/v2/specs/replan-v2.md` (Binding de mutation evidence)

**Files:** Permitidos somente `artifacts/bianchini/v2/evidence/P03-p01-mutation/` e, após os verificadores autorizarem, os registros P01 em `artifacts/bianchini/v2/ledgers/P01.md` e `docs/living/PROJECT_STATE.md`. Proibidos produção, testes, MutationHarness, filtros, dependências, METHOD_CONTRACT, bm.py, bm_mutation.py e evidências v1/v5.

**Contract:** Stryker 4.16.0, net8.0, concurrency 1, MutationHarness existente, policy `required_selective`, risk seam `external-fallback`, exatamente os dois mutate paths `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs`. Sem rede de aplicação, provider real, banco, credenciais ou crédito externo; sem alteração de código/testes/filtros/threshold/classificações. A evidence deve registrar `revision` e `expected_revision` iguais ao HEAD atual, com relatório, classificações e digests canônicos.

**Verification:** preflights oficiais; uma campanha Stryker observável; wrappers oficiais; `mutation-evidence verify` com revisão atual; `git diff --check`. Não executar nesta rodada de planejamento.

**Stop rule:** uma única campanha. Parar se lifecycle não for observável, exit code não for confiável, relatório/evidence for incompleto ou verificável, houver `revision-mismatch`, mutante material novo/sobrevivente não classificado, ou necessidade de alterar código, teste, dependência ou filtro. Nenhuma segunda campanha corretiva.

**Done when:** verificadores oficiais passam, evidence completa está vinculada ao HEAD atual e revisão humana aprova a transição documental. Caso contrário, P01 permanece `blocked-terminal`.
