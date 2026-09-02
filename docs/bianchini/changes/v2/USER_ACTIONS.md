# Ações externas do responsável — P03-R2

## U-004 — aprovar pacote e, depois, uma única campanha condicional

Primeiro, aprovar uma única vez o digest integral de P03-R2 para que os preflights não consumidores possam ocorrer. Depois de o launcher real, o ambiente idêntico, o MutationHarness e o binding de revisão passarem, aprovar explicitamente uma campanha seletiva `1/1` contra o HEAD executável então limpo e sincronizado. Essa segunda aprovação não existe ainda e não pode ser inferida da aprovação do pacote.

Sem a primeira aprovação, nenhum preflight é executado. Sem a segunda, a campanha não inicia. Se qualquer preflight ou a campanha falhar, o fallback é manter P01/P03-R2 bloqueados e release pending; não há download, alteração de código ou retry.

## U-001 — histórico de aprovação P02

Esta referência documental preserva que P02 exigiu aprovação de seu pacote antes de execução. Como P02 está completed, ela não autoriza nem exige ação nova nesta revisão.

## U-001 — histórico P02 preservado

P02 já está `completed`; esta revisão não reabre o plano nem requer ação sobre o cliente móvel.

## U-002 — credenciais somente para ativação/teste real histórico

Fora do escopo de P03-R2. Nenhuma credencial, provider, banco ou crédito externo é necessário ou permitido para os preflights ou a campanha seletiva.
