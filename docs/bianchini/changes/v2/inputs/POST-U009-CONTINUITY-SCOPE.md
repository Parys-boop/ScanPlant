# Escopo da deliberação pós-U-009 — 2026-09-09

O responsável autorizou exclusivamente planejamento documental, pela skill sdd-planning e pelo Bianchini Method v2, após o encerramento terminal P03-R6/U-009. Este arquivo materializa essa autorização de planejamento, não aprovação do plano proposto nem autorização de execução.

Comparar somente: A, preservar P03 blocked-terminal e retomar o próximo marco funcional; B, planejar outra revisão de mutação apenas se uma evidência nova for indispensável a um critério que as provas existentes não atendem. Recomendar uma única linha, considerando prazo, risco e valor marginal da evidência. Não dispensar gates obrigatórios nem declarar P01 ou release concluídos.

A proposta é A, limitada à retomada de F1-API01, benchmark e decisão de provedores do roadmap vigente. Preservar os contratos de segurança e o escopo integral do produto. Não incluir troca de fornecedor em produção, nova integração mobile, dataset de treinamento, modelo botânico, vídeo ou acompanhamento. O benchmark pequeno não valida as 12 espécies offline nem encerra o MVP.

P01 e P03-R6 permanecem blocked-terminal; P02 completed. Estado terminal imutável: campaign_count=2, campaign_executed=true, U-008=consumed_non_reusable, U-009=consumed, exit_code=134, failure_stage=campaign, mutation score e contagens indisponíveis. Nenhuma nova execução é permitida pelo R6.

Não alterar planos/manifesto R6, evidência terminal, marcador, logs originais, feed/cache/preflight, checkpoint de preparação ou histórico Git. Não criar revisão/campanha/autorização de mutação. Não executar restore, build, testes, MutationHarness, vstest, Stryker, mutantes, launcher ou implementação nesta rodada. Não fazer staging, commit, push, merge, rebase, cherry-pick ou criação/troca de branch.

Qualquer isolamento futuro exige prova descartável da fronteira real, anterior à autorização e ao marcador: invocação/Bash, localhost e TCP controlador/VSTest, filhos, ausência de conectividade externa, disco, persistência WSL, insumos, seleção de projetos, timeout, logs, interrupções e consequência do marcador. A campanha real nunca é prova de comunicação.

Entregar pacote documental mínimo, validado e sem staging. A próxima parada é a aprovação humana única do digest e do plano de continuidade; este pedido não a concede.
