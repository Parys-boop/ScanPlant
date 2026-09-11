# Planning review — P05 / F1-MAN01

Revisão semântica local, passagem 1; sem subagentes ou outras skills. Escopo desta revisão: contrato de planejamento, não existência do manifesto final ou aceite taxonômico.

```json
{
  "verdict": "passed",
  "findings": [
    {
      "id": "F-201",
      "severity": "note",
      "summary": "A lista completa das 12 espécies não está demonstrada; U-201 é pré-condição obrigatória de população e conclusão, explicitamente não concedida pelo planejamento.",
      "evidence": "Roadmap §3/§6 remete ao escopo; F1-G01 e spec P04 enumeram cinco. A-201 e U-201 propagadas à spec, delta, plano e ações humanas; nenhuma outra espécie foi selecionada."
    }
  ]
}
```

## Checagens semânticas

- Fidelidade integral: um único plano novo, uma unidade contendo manifesto, pesquisa de nomes/referências faltantes, documentação, validador, regressões e revisão humana. Nenhum requisito transferido ao marco de imagens, nenhum plano de treino, nenhum consumidor de produto.
- Readiness distingue contrato pronto de entrada indisponível. U-201 impede a população sem lista autoritativa de 12; pesquisa web não substitui escopo humano. Entradas previstas são materializadas como evidência na execução; substituição de táxon ou incompatibilidade com o contrato é mudança material e não detalhe delegado.
- Schema fechado, tipos exatos, 12+2, IDs/índices estáveis, aliases com fontes, chaves normalizadas sem colisões, nomes comuns em namespace separado e semântica de proteção têm aceite objetivo. Normalizador não remove autoria/acento nem faz aproximação.
- Suíte documental cobre erros reais de quantidade, identidade, ordem, referência, Unicode e JSON; CLI tem códigos de saída, é somente leitura/sem rede e não ecoa entradas. Comandos futuros estão explicitamente vinculados aos arquivos a criar; nenhum comando de produto é fingido como executado.
- Risco operacional low localizado, Change parser factual, grouped/plan_gate conforme policy. Falha do artefato reversível não é consumida pelo produto; verdade taxonômica e escopo dependem de revisão humana. Perfil standard conserva maior risco histórico. Não reduzir riscos de P01/P03, não renomear seam de mutação.
- Python 3.12 stdlib e Git bastam; toolchains .NET/Android/DB ausentes não impedem planejamento ou execução deste artefato. Disponibilidade de fontes oficiais é fronteira de evidência; zero credenciais/custo.
- Estados P01/P03 blocked-terminal, P02/P04 completed, release pending e execução inativa preservados. Novos pointers não encerram ciclo v2 ou sincronizam current/specs; referências históricas são somente rastreabilidade mínima, sem autorização de comandos.
- Ledger P05 append-only fora do snapshot; package não contém estado nem manifesto próprio, tampouco logs de campanha. Aprovação antiga é preservada em referência ao HEAD e manifesto imutável; novo digest não revalida os bytes vivos de P04 como se fossem os aprovados originalmente.
- Aprovação humana única futura cobre digest e P05 completo; planos históricos incluídos continuam nos mesmos estados. Não confundir passagem automatizada, U-201, aprovação do pacote, autorização de commit e execução. Este pedido proíbe staging/commit/push e execução nesta rodada.

## Limites

Não foi verificada taxonomia das sete espécies não identificadas nem reaberto benchmark. F-201 é limite de entrada explícito, não uma espécie inventada ou suposição tratada como confirmada. A revisão humana final continua obrigatória no gate da entrega. Auditoria arquitetural não foi solicitada e é manual/report-only segundo a skill; não foi executada.
