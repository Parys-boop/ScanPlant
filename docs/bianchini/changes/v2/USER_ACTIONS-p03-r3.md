# Ações externas do responsável — P03-R3

## U-005 — aprovar o pacote e depois uma única campanha condicional

Primeiro, aprovar uma única vez o digest integral de P03-R3 para permitir somente os preflights não consumidores. Depois de a prova composta do launcher, a igualdade de ambiente, o MutationHarness `23/23` e o revision binding passarem, autorizar explicitamente uma única campanha `1/1` contra o HEAD executável então aprovado, commitado, sincronizado e limpo.

Sem a primeira aprovação, nenhum preflight é executado. Sem a segunda, a campanha não inicia. Falha em qualquer preflight mantém `campaign_count=0`; falha após início registra `campaign_count=1` e não admite retry. O fallback é manter P01 blocked-terminal, P03-R3 blocked e release pending.

## U-001 — histórico de aprovação P02 preservado

P02 está `completed`; esta revisão não reabre o cliente móvel nem requer ação nova sobre ele.
