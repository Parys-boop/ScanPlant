# Ações externas do responsável — P03-R6

## U-001 — histórico P02 preservado

U-001 não cria uma nova ação: P02 permanece completed e fora de P03-R6.

## U-008 — consumida e histórica

U-008 foi autorizada e consumida pela tentativa terminal R5. O launcher iniciou Stryker e registrou `campaign_count=1`; a falha de build inicial antes de mutantes não devolve nem reutiliza a autorização. Não há retry sob U-008.

## U-009 — autorização posterior da nova campanha

Depois que o preflight corretivo R6 passar no WSL normal, um responsável deve conceder autorização explícita, separada e única para uma nova campanha. No instante da concessão, o commit documental final de R6 deve satisfazer `revision == expected_revision == HEAD == upstream`, branch `bm/v2-p03`, árvore limpa e divergência `0/0`.

U-009 não autoriza preflight, download, SDK 10, alteração de projetos ou qualquer nova campanha automática. Ela permite somente a transição atômica `campaign_count=1 -> 2` do launcher R6, usando o MutationHarness `net8.0`, solução temporária isolada e os dois targets aprovados. Falha após essa transição mantém `campaign_count=2` e não admite retry.

P-016 é aplicado: a existência de marcador, autorização fora do binding ou tentativa de reutilizar U-008 interrompe antes de invocar Stryker.
