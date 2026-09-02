# Ações externas do responsável — P03-R5

## U-001 — histórico P02 preservado

U-001 não cria ação nova: P02 permanece completed e fora deste replanejamento.

## U-007 — aprovação do pacote R5

Uma aprovação humana única do digest integral P03-R5 autoriza somente os preflights não consumidores, a preparação offline explícita, o launcher não mutacional e o gate final do MutationHarness. Sem ela, nenhum comando .NET é executado.

## U-008 — autorização posterior de campanha

Esta aprovação não autoriza campanha. Só após preflights, preparation e MutationHarness `23/23` passarem, com evidence íntegra e `revision == expected_revision == HEAD` executável aprovado, commitado, sincronizado, limpo e `0/0`, o supervisor pode conceder uma autorização explícita distinta para uma única campanha. Sem U-008, `campaign_count=0`.

P-013 permanece aplicável: o run-dir R5 é novo e não reutiliza evidence executiva R4.
