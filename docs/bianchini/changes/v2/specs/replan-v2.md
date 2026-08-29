# Replanejamento v2 — P01-R1 e P02

## Objetivo e limites

Registrar a impossibilidade externa de observar o lifecycle Stryker e replanejar somente a dependência entre os planos. P01 não é aprovado nem concluído. A funcionalidade de fallback já implementada permanece intacta.

## Decisão de dependência

P02 depende tecnicamente apenas de: endpoint ScanPlant de fallback presente; contrato de consentimento explícito; DTO/respostas neutras; autorização JWT; limites e tratamento de erro já cobertos pelos gates funcionais registrados no ledger P01. O encerramento da evidência de mutação de P01 é uma pendência de qualidade/observabilidade, não um pré-requisito técnico para implementar o cliente móvel. (D-001, D-002, A-001, S-001)

## Invariantes

P02 nunca envia rede sem consentimento, usa somente a API ScanPlant, não expõe provider/URL/segredo, preserva a foto em falhas e não altera o fluxo PT-05. P01 continua explicitamente bloqueado e nenhuma evidência ausente é inferida. (P-001, P-002)
SD-001
