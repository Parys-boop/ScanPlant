# Ações humanas — P07

Projeção de `READINESS-p07.md`; nenhuma ação histórica P01–P06 é reaberta. A decisão humana desta rodada é somente aprovar ou rejeitar o pacote P07 pelo digest selado.

U-001 (P02), U-009 (P03), U-101 (P04) e U-201 (P05/P05-R1) aparecem no readiness apenas para validar referências históricas congeladas; todas estão consumidas ou concluídas, sem autorização nova.

## U-701 — parecer por imagem na execução

Após a análise técnica, o responsável examina as 17 imagens originais fora do Git, resolve pares sinalizados e registra para cada Q/R um dos sete estados P07, evidência botânica ou insuficiência, privacidade, responsável, timestamp e justificativa. Uma pendência `needs_botanical_review` ou `needs_human_review` é decisão válida, mas não libera imagem. Sem os 17 pareceres, somente a análise técnica pode continuar; P07 não fecha.

## U-702 — aceite dos bytes finais

Após gates e relatório, o responsável confere 17/17, contagens, lacunas, hashes externos e resumo sanitizado, e aceita explicitamente esses bytes antes de commit/push. A aprovação do plano não substitui esse aceite. Se faltante, preservar o resultado sem publicação e manter fechamento formal pendente.

## U-703 — acesso externo delimitado

Na execução, fornecer leitura do diretório P06 informado e escrita apenas em um diretório **novo e separado** de resultados P07 fora do Git. Sem esse acesso, continuar somente testes sintéticos; parar antes de persistir resultado real. Nenhuma imagem, manifesto ou decisão P06 será modificada.
