# P02 — Cliente móvel consentido (desacoplado)

### Tarefa 1 — Cliente móvel depende de pré-condições técnicas verificáveis

**Risco:** medium  
**Execution:** slice  
**Review:** per_slice  
**Change:** authorization  
**Readiness refs:** D-002, A-001, P-001, U-001, S-001, SD-001  
**Test seams:** PhotoScreen consent gate, multipart API ScanPlant, ProblemDetails mapping  
**Spec refs:** docs/bianchini/changes/v2/specs/replan-v2.md#decisão-de-dependência, docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md  
**Files:** `ScanPlant-Final/components/PhotoScreen.js`, `ScanPlant-Final/components/api.js`, `ScanPlant-Final/.env.example`  
**Contract:** executar somente após confirmar as pré-condições técnicas de P01 no ledger: endpoint/DTO/consentimento/JWT e falhas neutras presentes e cobertos pelos gates funcionais já aprovados. Não exigir `P01 completed`; não alterar critérios de segurança, privacidade ou contrato.  
**Verification:** `git diff --check` e os comandos funcionais móveis aprovados no fechamento do plano.  
**Done when:** consentimento precede qualquer upload; recusa não gera rede; o cliente usa somente ScanPlant; respostas 400/413/415/429/502/503/504 são neutras; referências executáveis a providers externos são removidas; P01 continua bloqueado separadamente.
U-001 S-001 SD-001
