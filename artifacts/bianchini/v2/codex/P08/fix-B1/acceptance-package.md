# P08 B1 — rodada 1, pacote para aceite

Branch bm/v2-p08, HEAD original 7981377a433270c9e2072fcafdf89b690988fa08. Method Bianchini 3.2.0, strict. Sem staging, commit, push, coleta ou download nesta retomada.

## Causa e correção

acquire_inat convertia qualquer falha capturada em inaturalist_contract_or_evidence. Como esse código não pertence a RETRYABLE, acquire ignorava a fonte após um timeout transitório. A correção preserva str(error) somente para RecoveryError já classificado em RETRYABLE. Demais erros continuam bloqueados. O conjunto RETRYABLE não mudou.

## Evidências e revisão

RED histórico proof-6928ea925e6f438e3873543389326106 no SHA original, mais RED dos três testes novos contra produção original (12 assertions falharam). GREEN reutilizado: três testes novos, 54 P08, 15 adaptador, 236 suíte afetada, incluindo cinco mutações seletivas mortas. Todos os hashes de fontes, logs e saídas conferem; demais dependências rastreadas da suíte coincidem com HEAD. Não se repetiu suíte por troca de sessão. evidence-reconciliation.json registra fontes e resultados.

Executados agora: workspace resume/check, route, validate-state, snapshot verify, planning-audit strict, repo-hygiene, git diff --check; reconciliação de hashes; comparação read-only de bytes/mtimes externos; revisão independente e inspeção Git. Nenhum teste ou mutação reexecutado agora.

Os testes exercitam timeout com três tentativas, restart com sucesso na quarta requisição, orçamento cumulativo esgotado sem nova conexão, journal/config preservados, ausência de página/cursor/candidato antes do sucesso, um candidato pendente após sucesso e repetição estável sem duplicação. Contrato/integridade/limites não viram retry.

Revisor independente retornou findings vazio. Revisão técnica passed nos bytes não commitados. Guard preservado em fixing, rodada 1, B1 open, redesign 0, pending_delta null. Não há resolução formal nem gates da correção; os gates no sidecar são históricos, sobre o SHA original. P08 permanece blocked, release pending. O checkpoint oficial copia a prosa histórica do estado; o último bloco do ledger registra a instrução atual, sem inserir campos de convergência em PROJECT_STATE.

## Separação de arquivos

Correção: scripts/phase1/recover_p08.py e scripts/phase1/test_recover_p08.py, idênticos ao início desta retomada. Evidências da rodada e deste aceite estão em fix-B1/.

Recuperação documental anterior: docs/living/PROJECT_STATE.md, bloco Closure recovery do ledger, closure/*, store de proofs e sidecar. Todos preservados; somente um novo bloco foi acrescentado ao ledger. preexisting-inventory.json e recovery-documentary-before.patch separam os bytes anteriores ao fix; session-start-inventory.json registra o ponto desta retomada. O sidecar/backup já haviam mudado pelo fix oficial antes da interrupção e não foram alterados agora.

O inventário exato proposto está em commit-inventory.txt; commit-inventory.json classifica cada path e lista exclusões locais. acceptance-manifest.sha256 contém SHA-256 de todos os arquivos propostos, exceto o próprio manifesto e acceptance-digest.txt. O digest aceito é o SHA-256 dos bytes desse manifesto. O inventário inclui ambos os arquivos derivados; não há autorreferência. O futuro recibo humano fica fora deste digest. Qualquer mudança de payload exige regenerar manifesto e novo aceite.

## Dados e inspeção

1088 candidatos pendentes, zero transferências, approved_for_dataset=0, usable=0. Bytes e mtimes de P06/P07/P08 e backup conferem com o início da rodada (29/13/139/138 arquivos, incluindo locks). iNaturalist real continua sem crosswalk humano. Treinamento não autorizado; P09 não iniciado. Nenhuma migração da configuração, code fingerprint ou journal externo.

Inspeção abrange arquivos novos, modificados e os 33 paths da implementação original para distinguir história de inclusão nova. Fixtures/URLs/EXIF/revisores sintéticos em testes e pacotes de revisão são exemplos de contrato; logs guard contêm metadados operacionais históricos, não respostas reais de candidatos. Nenhuma imagem, base64 de imagem, credencial, .env, chave privada, autor/revisor real ou resposta bruta privada nova identificada. O inventário granular do dataset externo e os backups/lock operacionais do guard ficam preservados fora do commit proposto. Não é aprovação botânica ou de privacidade dos candidatos.

## Sequência posterior condicionada

1. Aceite explícito do novo digest; registrar recibo separado sem reusar o aceite original. Aceitar bytes não implica permissão de staging/commit/push; obter autorização Git expressa no escopo necessário.
2. Revalidar HEAD, branch, workspace, índice e cada hash/inventário; realizar staging apenas dos paths listados e criar commit próprio (sugestão: fix(p08): preserve transient iNaturalist failures on resume). Não amendar/regravar original. Nada de push inferido.
3. No novo SHA, emitir proof GREEN para B1 com argv e cwd idênticos ao RED, como exige o guard. Atenção: o wrapper histórico grava dois logs em closure/ por path absoluto. Preservar previamente esses bytes/mtimes, arquivar separadamente a saída GREEN e restabelecer/verificar os logs históricos; nunca apresentá-los sobrescritos como nova evidência. Registrar stdout/stderr/hash do proof novo. Não modificar o comando para simular equivalência.
4. submit-delta --kind fix com base igual ao last_review_head original e head igual ao novo SHA; somente então review-package oficial do delta e review em awaiting_review. Finding B1 source=frozen/resolution=resolved deve referenciar o novo proof GREEN, conservando contrato/prova RED. Não repetir fix nem incrementar rodada por troca de sessão.
5. Emitir proofs no novo SHA e registrar todos os gates obrigatórios, inclusive suíte/mutação seletiva do plano no SHA final, integridade read-only, aceite novo e inspeção. Reutilizar evidência histórica apenas como contexto; ela não satisfaz gates do novo SHA. Não executar aquisição/finalização/migração real para satisfazer gate. Se a checagem de integridade exigir o runtime antigo, preservar sua identidade e provar separadamente os bytes externos sem forçar atualização do dataset.
6. Fechar guard somente com B1 formalmente resolvido, HEAD revisado e gates obrigatórios passed no novo SHA; depois atualizar fechamento P08 pelo método. Confirmar pendências legítimas dos candidatos e zero aprovados sem inventar parecer pericial. Não avançar release, treino, P09 ou push por inferência. Artefatos posteriores ao commit formam registro de fechamento separado, sem amend do commit da correção.
