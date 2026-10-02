# Planning review P08 — passagem 1

```json
{"verdict":"passed","findings":[]}
```

Revisão semântica documental pelo agente planejador, sem alegar revisão independente de implementação. Essa revisão independente é gate futuro da unidade strict. Nenhum subagente utilizado. Primeira e única passagem proposta; CLI registrará digests do pacote e deste relatório. Máximo permitido duas, sem revisão por preferência.

## Evidência examinada

- Baseline, remoto e guard: P08-BASELINE.md; summary/closure/human-acceptance/convergence P07. published b6844f9 confirmado por ls-remote, não apenas tracking ref. P07 completed, zero aprovado/usable e 14 classes vazias de aprovação; P01/P03 continuam bloqueios de release.
- Escopo integral mapeado à spec §§1–9 e unidade única. Nenhum requisito quantitativo se tornou promessa. Contagens independentes, piloto null, suficiência não demonstrada e treino/partição proibidos.
- Pesquisa R01–R16 somente oficial/primária, termos por foto/dataset/provedor distintos. Fontes acadêmicas avaliadas e bloqueadas quando licença/original/termos não verificáveis; API GBIF não concede direitos de imagem. iNaturalist elegível somente com prova legal por item e crosswalk; schema dinâmico e original limitado explicitamente registrados, sem inventar dados. Sem coleta real nesta pesquisa.
- Taxonomia P05-R1 permanece byte a byte: manifesto/roster/normalização, 12+2 e aliases em quarentena. Spec §4 exige source ID/evidência/perito, não nome comum/Plant.id/research_grade. Proteções não absorvem rejeições.
- Contrato §5–7 cobre proveniência, original/sanitizado, atribuição fora do Git, persistência com fsync/lock, append-only, replay, limites/Retry-After, dedup exata/perceptual e comparação 17 P07, formato/métricas/visuais/privacidade/botânica. Alias/source/titular inconclusivos nunca aprovam.
- Unidade única justificada pelo mesmo resultado verificável e mesmas invariantes; U-801..804 são limites explícitos de autoridade, não aprovação presumida. Standard/high strict/per_task e policy data-transform impõem mutação seletiva; harness stdlib com cinco desvios concretos está contratado, sem ferramenta nova instalada e sem campanha .NET histórica.
- Testes/comandos distinguem existência atual de entregável futuro; testes P08 não foram alegados como executados. Testes sintéticos e fronteiras de corrupção/concorrência/retomada/privacidade/limites estão em §9. Gates reais de dados e aceite não são substituídos por testes sintéticos.
- Estado mantém sete planos históricos e acrescenta apenas P08 planned; prior_p07_approval conserva aprovação anterior. Release/active_execution preservados. Escopo e aprovação nova separados; nenhum staging/commit/push autorizado por aceite do planejamento.
- Spec-delta contém contrato completo; target current/specs ausente no baseline e não foi criado. Históricos/readiness herdados no pacote atendem compatibilidade do estado sem reabrir planos. Correção viva de publicação P07 congelada no documento baseline (estado não se inclui no próprio manifesto).

## Conclusão e limites

Não há finding material aberto no planejamento. Fontes/itens ambíguos, ausência de perito, disponibilidade zero e gates externos são resultados/ações explicitamente contratados, não lacunas escondidas. Pacote está pronto para decisão humana; execução continua não autorizada. Snapshot/CLI devem passar antes de apresentar digest; qualquer mudança posterior invalida esse passe e consome a única correção permitida. Não executar homologação/treino/release para validar planejamento.
