# Escopo autorizado pelo responsável — P07, curadoria rastreável do conjunto adquirido

Decisão recebida em 2026-09-30. Base obrigatória: branch `bm/v2-p06-direct`, HEAD/upstream/remoto `3f0beaad06bfdd9b4f069a6f5f668ce9e9b93d97`, árvore e índice limpos, uma worktree, Method Bianchini 3.2.0, rota v2 standalone-adaptive, planning_version v2 e quality_version 2. Esta autorização cobre **somente o planejamento**; não aprova o pacote ainda não produzido nem sua execução.

## Resultado contratado

Um único plano P07, com uma única unidade coesa, para curar tecnicamente e por revisão humana as 17 imagens externas de `/home/administradorarthur/datasets/scanplant/p06-recovery-20260928/quarantine/`. Conferir SHA-256 e correspondência exata dos 17 IDs Q01–Q17/R01–R17; registrar decodificação, dimensões, proporção, nitidez, exposição, enquadramento, oclusão, múltiplas espécies e representatividade. Detectar igualdade exata por SHA-256 e candidatos a duplicata visual por método perceptual documentado, com distância e limiar explícitos. Revisar pessoas/rostos, placas, veículos, residências, documentos e outros identificáveis. Preservar autoria, licença e origem P06. Validar rótulo botânico somente com evidência suficiente.

Para cada imagem, produzir registro externo rastreável de ID estável, SHA-256, classe candidata, métricas e observações técnicas, duplicidade, privacidade, evidência botânica, decisão, responsável, timestamp e justificativa. Produzir JSON estrito e relatório humano legível, com aprovadas, rejeitadas, pendentes, lacunas por classe e classes sem candidato. Nenhuma decisão automática promove imagem; a aprovação visual anterior de P06 não equivale à validação botânica. P07 pode encerrar com zero aprovadas, pendências botânicas e classes vazias; isso nunca demonstra suficiência para treinamento.

Planejar estados inequívocos `approved_for_dataset`, `rejected_quality`, `rejected_duplicate`, `rejected_privacy`, `rejected_label`, `needs_botanical_review` e `needs_human_review`. O algoritmo somente sinaliza achados; o responsável humano decide qualquer rejeição ou promoção. As três decisões P06 `rejeitar` continuam vinculadas à proveniência e não são convertidas silenciosamente em aprovação P07.

## Invariantes e verificação futura

Preservar byte a byte as 17 imagens fora do Git; não excluir, mover, recodificar ou copiar para o repositório. Reconciliar conjunto esperado de hashes e conjunto processado, impedir artefato final incompleto, provar reexecução idempotente e usar fixtures sintéticas para filtros, duplicatas exatas, quase duplicatas e limites. Registrar revisão humana por imagem, aceitar bytes finais antes de commit/push, impedir segredos/dados pessoais no Git, `git diff --check`, preservar checksums/snapshots históricos. Não criar backup adicional.

Na mesma unidade, corrigir minimamente `docs/living/PROJECT_STATE.md` e a cronologia de `docs/PLANO_CANONICO_IA_HIBRIDA.md`: P06 concluído somente como mecanismo no commit acima, 17 em quarentena, usable 0, 11 anteriores perdidas, P07 planejado; P01/P03-R6 blocked-terminal, P02/P04/P05/P05-R1 completed, release pending e active_execution coerente. F1-BE01 tem base funcional P01/P02 sem homologação; F1-API01=P04; manifesto=P05/P05-R1; aquisição=P06; curadoria é próxima. Textos antigos seguem históricos. Não alterar planos, ledgers, evidências P01–P06 nem sincronizar current_specs.

## Exclusões

Sem nova aquisição/download, substitutos, meta artificial por classe, treinamento, aumento de dados, partições train/validation/test, EfficientNet-Lite0, MobileNetV2, TFLite, quantização, mobile, catálogo offline, API/fallback, banco, Java/Android SDK/ADB, PostgreSQL, Expo, homologação, release, P08, vídeo ou acompanhamento de plantas. Nesta rodada: sem implementação de script, curadoria real, alteração de imagem, instalação, staging, commit, push, merge, PR ou tag. O próximo ato humano é apenas aprovar ou rejeitar o pacote P07 e seu digest.
