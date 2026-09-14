# Escopo humano — P05-R1 / F1-MAN01 / U-201

Decisão explícita do responsável pelo produto recebida em 2026-09-14 nesta sessão.
Aprovação da política abaixo não é aprovação do novo pacote, de seu digest ou dos bytes finais.

## Decisão e política integral

Aprovar exclusão e quarentena de Aloe maculata, Aloe variegata, Ficus clusiifolia e
Ficus cordata como chaves científicas sem autoria. O contrato usa binômios sem
autoria e cada texto corresponde a mais de uma identidade nomenclatural segundo
a evidência já versionada; não há resolução inequívoca.

1. Nenhum dos quatro nomes sem autoria resolve para class_id; resolve_scientific_name
   retorna None/null após a normalização já aprovada.
2. Preservar os quatro na revisão taxonômica: autoria associada à espécie do manifesto,
   autoria conflitante, identidade/táxon conflitante, fontes, motivo da exclusão e estado
   explícito de quarentena. A exclusão não nega a sinonímia nomenclatural nas fontes;
   declara somente inelegibilidade como chave authorless do ScanPlant.
3. Sinônimo binomial só é elegível se sua forma normalizada sem autoria é inequívoca
   nas fontes taxonômicas aplicáveis. Os demais aliases elegíveis mantêm fonte oficial
   e todas as regras já aprovadas. Novo homônimo bloqueia aceitação até revisão explícita;
   associação silenciosa é proibida.
4. Não adicionar autoria às chaves, remover autoria recebida, implementar fuzzy matching,
   aproximação, preferência automática por classe ou resolução por contexto.
5. Preservar as 12 espécies, nomes científicos canônicos, nomes comuns pt-BR,
   species_01 a species_12, ordem/índices 0–11, outra_planta/12 e imagem_invalida/13,
   definições das proteções, normalização, namespaces e roster aprovado.
6. Escopo exclusivamente documental/local, sem imagem, dataset, treino, modelo,
   integração de produto ou provider. Aceite humano dos bytes finais e hashes permanece obrigatório.

## Checkpoint e fronteira desta rodada

Repositório Parys-boop/ScanPlant; worktree
`/home/administradorarthur/code/scanplant-handoffs/p05-f1-man01-taxonomy-blocked-20260911-77e93a`;
HEAD inicial detached e limpo `77e93a221dad3115c301b10317b626c236a3ba84`;
origem `origin/checkpoint/p05-f1-man01-taxonomy-blocked-20260911` no mesmo SHA.
Digest histórico P05 `246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5`.
Conferir HEAD, status, índice, binding, worktree, remoto, snapshot 23/23 e limpeza antes
de editar. Skill sdd-planning existente, lida integralmente; ausente exigiria parar sem instalar.
Usar bm/v2-p05-r1 a partir desse SHA somente se ausente local/remoto; existente exige
mesmo SHA e não ocupada. Divergência exige parar. Não publicar.

Executar change-policy oficial para alteração de contrato público; registrar resultado real.
Somente replanejar elegibilidade/quarentena; fronteira mais ampla exige parar. Preservar
pacote P05 histórico, plano, spec, planning review, manifesto aprovado e digest integralmente.
Ledger só append. PROJECT_STATE só alterações necessárias a P05-R1/U-201.
Não editar manifesto offline, roster, validator, testes, validation-report, taxonomy-review
ou documentação final F1-MAN01 nesta rodada. Não implementar.

## Aceite da execução futura

Exigir ausência dos quatro no mapa e retorno None; evidência com autoria e conflito;
nenhum outro alias elegível removido, nenhum canônico afetado e nenhuma colisão normalizada.
Testes positivos de todos os canônicos/aliases inequívocos, negativos específicos dos quatro
e teste que impeça reintrodução silenciosa de quarantined. Reconciliar 83 binômios
preliminares menos quatro quarentenados por prova de conjuntos e contagem, sem assumir total.
Decidir versionamento conforme SemVer registrada; atualizar documentação, relatório,
checksums e estado coerentemente. Revisão humana final vinculada aos hashes produzidos.

## Restrições e entrega do planejamento

Sem subagentes, instalação, pesquisa taxonômica em rede, providers/credenciais,
.NET, npm, Android, Docker, banco ou Stryker. Não editar worktree antigo bm/v2-p03,
remover backup, copiar PROJECT_STATE antigo, offline_species_XX, READINESS malformado
ou planos antigos para este pacote. O backup
`/home/administradorarthur/code/scanplant-handoffs/p05-local-a34da4-wxP2S0ll`
é apenas evidência histórica externa; antecedente de quarentena não é necessário à decisão atual.
Sem merge, staging, commit, push, implementação ou aprovação pelo agente.

Validar rota v2, change-policy, checker semântico, planning-audit --strict,
validate-state, snapshot, JSON/JSONL estritos, UTF-8/LF/newline final, git diff --check,
segredos/dados pessoais, digest P05 e preservação P01/P03-R6, P02/P04/release.
Entregar classificação, ID, arquivos, regra, versão proposta, testes/critérios,
resultados, novo digest exato, estado U-201, Git final e um pedido único de aprovação
humana do pacote/digest. Parar antes de staging, commit, push ou implementação.
