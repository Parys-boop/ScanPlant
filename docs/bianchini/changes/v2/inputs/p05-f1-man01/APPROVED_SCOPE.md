# Escopo solicitado — P05 / F1-MAN01

Pedido humano de 2026-09-11: planejar exclusivamente o próximo marco canônico do ScanPlant, o manifesto completo das 12 espécies offline já aprovadas, sinônimos aceitos e classes de proteção `outra_planta` e `imagem_invalida`. O pedido aprova o escopo do planejamento; não aprova o pacote, o conteúdo taxonômico ou a execução.

## Checkpoint e precedência

Repositório Parys-boop/ScanPlant; branch `bm/v2-p03`; HEAD, upstream `origin/bm/v2-p03` e remoto `a34da4dd34eea58921862f0d0fa2d0016be5ce31`; commit `docs(p04): record provider benchmark decision`; divergência 0/0 e árvore inicial limpa, confirmados antes da edição. O estado versionado nesse HEAD prevalece sobre conversas e textos históricos.

P02/P04 completed; P01/P03-R6 blocked-terminal, sem retry; release pending; active_execution null. Pl@ntNet principal gratuito e Plant.id secundário técnico de trial. Nenhuma autorização de provider remanescente.

## Uma entrega integral

Exatamente 12 espécies suportadas e duas proteções, cada classe com identificador e ordem estáveis; nome científico canônico, nomes comuns necessários ao produto e sinônimos taxonômicos aceitos; normalização/comparação explícitas; distinção espécie/proteção; versão/formato; referências taxonômicas com data de consulta; validação automática de quantidade, unicidade, formato, sinônimos, classes e ordem; critérios de revisão humana. Definir a compatibilidade futura com treino, catálogo offline e saída do modelo sem implementar esses consumidores. Especificação, pesquisa taxonômica necessária, validação e revisão pertencem à mesma unidade de execução.

## Lacuna de escopo nominal

O roadmap §3 afirma que as 12 espécies são as previamente aprovadas, mas não as enumera. F1-G01 e a spec documental P04 identificam somente o piloto: Epipremnum aureum, Monstera deliciosa, Zamioculcas zamiifolia, Spathiphyllum wallisii e Dracaena trifasciata; o sinônimo Sansevieria trifasciata não é uma sexta espécie. A inspeção de documentos versionados não localizou uma lista inequívoca de 12. Nenhuma espécie adicional é presumida, inclusive Bellis perennis, que é controle P04.

A única fronteira de entrada U-201 exige a lista completa aprovada ou o documento autoritativo que a contenha antes de preencher o manifesto. Aprovar o plano não inventa essa lista. Uma lista recebida que apenas materializa as 12 já aprovadas é entrada prevista, registrada como evidência; inclusão/substituição de espécie fora desse escopo exige nova decisão de escopo e invalida a parte afetada do pacote. Referências web taxonômicas oficiais podem confirmar nomes, não escolher o escopo do produto.

## Exclusões e preservação

Sem aquisição/escolha/deduplicação de imagens, downloads ou criação de dataset, treino, EfficientNet/MobileNet, conversão TFLite, integração de classificador, catálogo implementado, alterações de backend/mobile/web, chamadas a Pl@ntNet/Plant.id/Groq/Gemini, credenciais, gastos, restore/build/testes de produto/Stryker/mutação, instalações, reabertura P01/P03-R6, plano de aquisição posterior ou release pronto. Sem outra skill ou subagentes nesta rodada; sem staging/commit/push. Planos, ledgers e manifestos históricos são imutáveis; criar somente pacote de planejamento novo e atualizar o estado vivo. Aprovação humana nunca é atribuída ao agente.

## Ambiente e método

Python 3.12 e rg presentes. .NET 8, Java, ADB, Android SDK, jq e pwsh ausentes; Docker daemon e PostgreSQL indisponíveis; Node 24 diverge do Node 22.20.0 EAS. Isso não bloqueia planejamento. A execução do manifesto exige apenas Python 3.12 stdlib, Git e acesso de leitura a fontes taxonômicas oficiais quando necessário, sem instalar dependências. Rg e sha256sum são conveniências já disponíveis; Python pode verificar hashes.

Usar sdd-planning instalada, quality_version 2, no máximo duas passagens do checker, auditoria estrita e snapshot novo. Solicitar uma única aprovação humana de digest e plano completo, explicitando U-201; aprovação do pacote não autoriza execução ou operações Git nesta rodada.
