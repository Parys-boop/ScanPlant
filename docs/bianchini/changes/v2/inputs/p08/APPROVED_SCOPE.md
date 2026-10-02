# Escopo aprovado para planejar P08

Autoridade: instrução explícita do responsável nesta sessão, 2026-10-01. Aprova o escopo do planejamento, não o pacote nem execução. Usar sdd-planning, Bianchini Method 3.2.0, v2 standalone, quality_version 2. Esta transcrição estruturada preserva os resultados, limites e obrigações solicitados.

## Baseline e workspace

Repositório /home/administradorarthur/code/scanplant-current/ScanPlant; continuidade origin/bm/v2-p07; commit obrigatório b6844f9129d9edf862ae7958d8f043d9bdd5bd84. Commits publicados a2dfd8805527e6323334fcc0a7b7f45c63c7d3c9 (feat(p07): add traceable dataset curation) e b6844f9129d9edf862ae7958d8f043d9bdd5bd84 (chore(p07): close traceable dataset curation). Confirmar HEAD, upstream, remoto, limpeza, worktrees e método antes de escrever. Autorizada criação local de branch bm/v2-p08-planning e worktree persistente /home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08-planning; conflito exige parar, sem sobrescrever. Planejamento nunca em /tmp.

Estado esperado: P07 completed, guard completed sem blockers, U-701/U-702 aceitas; approved_for_dataset=0, usable=0, rejected_quality=2, needs_botanical_review=8, needs_human_review=7; 14 classes sem candidato aprovado; release pending; active_execution null; P08 inexistente.

## Resultado solicitado

Planejar a menor intervenção segura para recuperar a insuficiência de dados após P07: obter, validar e preservar candidatos potencialmente utilizáveis para 12 classes botânicas canônicas mantendo 2 proteções. Zero aprovadas, classes vazias, fontes inviáveis, licenças incompatíveis, rótulos inconclusivos e treinamento ainda bloqueado são resultados legítimos. Quantidade não é garantia de disponibilidade ou qualidade.

Incluir na mesma entrega a correção mínima do PROJECT_STATE: P07 publicado em b6844f9129d9edf862ae7958d8f043d9bdd5bd84, completed, guard completed, usable=0, release pending, P08 em planejamento e nenhuma autorização de treino. Não criar plano para essa correção.

## Pesquisa e taxonomia

Pesquisa proporcional rastreável com documentação oficial/fontes primárias: avaliar continuação/ampliação Wikimedia Commons, iNaturalist, GBIF e provedores originais, datasets botânicos acadêmicos oficialmente publicados com documentação/licença verificáveis; outra fonte só com justificativa concreta. Por opção verificar licença por arquivo/dataset, redistribuição/processamento/eventual treinamento, atribuição, autoria/proveniência, restrições, API/paginação/rate limits, estabilidade/retomada, original, identificador taxonômico, privacidade (localização/pessoas/placas/residências), rótulos incorretos, imagens derivadas/montagens/ilustrações/espécimes inadequados e obrigações sobre derivados/dataset/modelo/aplicação. Nome de licença não prova compatibilidade; registrar incerteza e bloquear fonte/item ambíguo. Blogs, respostas informais e agregadores não são autoridade de licença.

Preservar integralmente P05/P05-R1: 12+2 classes, IDs, ordem, nomes, normalização, quatro aliases ambíguos em quarentena; nunca reintroduzir homônimos nem aceitar por nome comum. Ligar item à classe, nome científico recebido, ID da fonte, autoria taxonômica disponível, evidência do mapeamento, confiança e decisão humana. Plant.id, sugestão automática ou outro classificador não confirmam botânica pericial.

## Contrato obrigatório

Fontes autorizadas/bloqueadas; consultas/limites por fonte e classe; retomada idempotente; journal append-only; hashes original/sanitizado; autoria/licença/página/URL do arquivo; atribuição; remoção EXIF/GPS; original e dataset externos ao Git; estados candidato/rejeição/pendência/aprovação; dedup exata/perceptual e comparação contra 17 P07; formato/dimensões/corrupção/nitidez/exposição; detecção de ilustração/montagem/texto excessivo/alvo mal delimitado; privacidade; validação botânica humana; classes vazias; resultados sanitizados permitidos no Git; conclusão/bloqueio objetivos; testes sintéticos/fronteiras/integridade/idempotência; aceite humano dos bytes finais antes de commit/push. Avaliar extensão delimitada P06/P07 e evitar reescrita suficiente sem necessidade.

Distinguir limite de aquisição, encontrados, íntegros, licença válida, rótulo validado, aprovados, mínimo experimental de eventual piloto e suficiência científica/produtiva. Não inventar dataset suficiente. Meta por classe exige justificativa operacional/experimental. Nenhuma partição ou treinamento no P08.

## Exclusões e entrega

Nesta sessão: nenhuma implementação, coleta real, download de imagens, alteração/exclusão de imagens/datasets existentes, commit/staging/push/merge/tag. No P08: nenhuma reabertura P06/P07, treinamento/comparação de modelos, augmentation, train/validation/test, TFLite, mobile/API/fluxo de produto, homologação, release ou P09.

Preferir um plano coeso, dividir unidades somente com fronteira técnica/de autoridade concreta. Perfil/risco proporcionais, decisões humanas como ações explícitas. Pacote inclui escopo, pesquisa, readiness, ações, spec, spec-delta, plano, policy, checker, planning review, manifesto/digest e atualização mínima do estado. Checker no máximo duas passagens, sem ciclo. Encerrar com baseline, diagnóstico, comparação/recomendação, contagem planos/unidades, perfil/risco, arquivos, condições futuras, ações humanas, exclusões, validações, digest único, git diff --stat e git status completo. Parar para uma única decisão humana do pacote/digest. Aprovação não revoga a proibição de staging/commit/push nesta sessão.
