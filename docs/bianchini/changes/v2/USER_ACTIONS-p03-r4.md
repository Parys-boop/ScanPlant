# Ações externas do responsável — P03-R4

## U-006 — aprovação do pacote e autorização separada da campanha

Uma aprovação humana única do digest integral P03-R4 autoriza somente os preflights não consumidores no linked worktree canônico. Antes deles, o executor deve provar que os recursos locais resolvidos estão presentes sem rede nem download.

Depois de todos os preflights, inclusive launcher composto e MutationHarness `23/23`, uma segunda autorização humana explícita, posterior e vinculada ao HEAD executável é indispensável para iniciar a única campanha `1/1`. Sem essa segunda autorização, não há campanha. Falha antes dela preserva `campaign_count=0`; falha depois de iniciá-la registra `1` e não admite retry.

## U-001 — P02 histórico preservado

P02 continua `completed`; esta revisão não reabre o cliente móvel nem exige ação nova.
