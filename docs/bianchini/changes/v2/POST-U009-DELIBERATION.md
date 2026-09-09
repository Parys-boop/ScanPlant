# Deliberação pós-P03-R6/U-009

Data: 2026-09-09. Base documental: `14980b1f181e00ba1ee259a27cc2209b0a013364`, branch `bm/v2-p03`, upstream `origin/bm/v2-p03`, divergência inicial 0/0 e árvore limpa. Proposta pendente de aprovação humana.

## Recomendação única: A

Manter P03-R6 encerrado **como blocked-terminal**, sem reabertura, e retomar **F1-API01 — benchmark e decisão de provedores**. P04 propõe somente a entrega de evidência comparativa e decisão, sem mudar o produto. Não declarar F1-BE01 integralmente homologado, P01 completed ou release ready. A separação entre avanço funcional e fechamento de garantia é explícita, não um waiver.

## Fundamento e critérios de aceite

| Fonte canônica / critério exato | Consequência para esta decisão |
| --- | --- |
| `docs/PLANO_CANONICO_IA_HIBRIDA.md`, §6, F1-BE01 itens 1–11 e marco seguinte F1-API01 | Contratos, endpoint seguro e cliente são a base funcional; o próximo resultado é comparar provedores no backend com casos fixos, não outra campanha de mutação. |
| Mesmo roadmap, §8 | Encerramento requer código do escopo, testes relacionados aprovados, ausência de segredos, documentação e pendências reais. Não estabelece score global. |
| `docs/bianchini/changes/v1/plans/P01-backend-secure-fallback-r1.md`, Tarefa 3 / Done when e Semântica de resultados | Gate seletivo material: matar ou provar equivalência de seis sobreviventes, tratar no-coverage de segurança e classificar timeouts. Declara que não há score global novo. Não é evidência meramente opcional para concluir P01. |
| `docs/bianchini/changes/v1/inputs/P01-MUTATION-GATE-AMENDMENT.md`, Decisão formal | Proíbe dispensar, substituir ou reduzir aquele gate. Esta proposta não o faz. |
| `docs/bianchini/changes/v2/inputs/APPROVED_SCOPE.md` e `plans/P02-mobile-consented-client.md`, Contract | Decisão posterior desacopla avanço funcional do encerramento de observabilidade: P02 depende das pré-condições técnicas de P01, não de P01 completed. O texto v1 que impedia P02 foi superado expressamente para P02. |
| `artifacts/bianchini/v2/ledgers/P02.md`, gate e conclusão formal | P02 completed, provas funcionais e exportação aprovadas; RC/fingerprint/proof-map não aplicáveis enquanto release pending por P01. |
| `docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md`, U-009, binding e parada; plano R6, Tarefa 2 | Falha após marcador mantém contador 2, U-009 consumida e bloqueio terminal, sem retry. |

A extensão desse desacoplamento a F1-API01 é a **decisão proposta para aprovação**, não uma aprovação histórica atribuída ao roadmap. É defensável porque comparar evidências sem alterar os seams do produto não depende de demonstrar um novo score nem permite fechar o gate de P01. O ciclo v2 não é encerrado, arquivado ou renumerado; P01/P03 continuam no estado ativo como blocked para impedir fechamento indevido.

## Provas aproveitáveis e seus limites

- O ledger v1 P01 registra gates funcionais de JWT, consentimento, upload, cancelamento/timeout, erros neutros e degradação opcional, com unitários/integração e build aprovados. O ledger v2 P02 registra consentimento/API-only e build/exportação. Não foram repetidos.
- `artifacts/bianchini/v1/mutation/P01-R1-final-evidence-verify.json` registra `passed`, nenhum blocking mutant e 17 sobreviventes aceitos na revisão `a9d245d9a832f98bcbaadc93973959d61cf936df`. É evidência histórica de sensibilidade material, **não** relatório U-009 nem prova de lifecycle/RC atual. O ledger mantém o bloqueio por ausência do exit final observável.
- Comparação estática entre essa revisão e HEAD não encontrou diferenças em `ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/`, `ScanPlantAPI/ScanPlantAPI/Controllers/PlantIdentificationController.cs` e `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/`. Comparação de `ScanPlant-Final/` com `0faf65bcee27da1a33e924cfc5d826f31bdacdca` também foi vazia. Isso preserva relevância histórica dos caminhos comparados, não transfere fingerprint de release.
- `progress.log` terminal registra preflight aprovado, MutationHarness 23/23, uma transição claimed 1→2, um started e um failed. `campaign-summary.txt` registra exit 134 na campanha. `stryker.log` registra Stryker 4.16.0 e timeout de conexão em 90 segundos com filhos 9090/9091 ainda ativos. Nenhum total de mutantes ou mutation score U-009 está disponível. Não confundir ausência de medição com score zero.

## Ressalva técnica nova, sem alterar a evidência preservada

O diagnóstico terminal contém contradição interna: registra `lo_flags=0x9`, mas afirma que esse valor não contém `IFF_UP=0x1`. A operação `0x9 & 0x1 = 0x1` demonstra o contrário. `operstate=unknown` e o erro `Cannot open netlink socket: Operation not permitted` tampouco comprovam interface administrativamente desativada. Além disso, a observação descrita é de outro namespace efêmero, não dos processos da campanha.

Fato de log: `Stryker failed to connect to vstest.console` e `process failed to connect to vstest.console process after 90 seconds`; o próprio texto sugere lentidão como possibilidade, não diagnóstico provado. Evidência do namespace: somente os valores brutos e a falha de inspeção acima. Inferência sustentada: a fronteira de comunicação controlador/filhos não foi comprovada pelo preflight que só criou um namespace. Bloqueio de TCP/localhost, política do executor ou lentidão permanecem hipóteses; loopback desativado não pode ser tratado como fato nem como causa forte demonstrada por esses bytes. Não houve nova observação de namespace nesta deliberação.

## Alternativa rejeitada: B nesta rodada

Não criar outra revisão de mutação. Nenhum documento exige novo score numérico para iniciar F1-API01, e já existe evidência seletiva histórica sem bloqueantes materiais. Uma nova tentativa buscaria sanar o lifecycle de P01, cujo fechamento permanece pendente, mas não é pré-condição comprovada do benchmark documental independente. Repetir esse investimento agora adicionaria risco ambiental e prazo sem entregar a comparação de provedores. A rejeição não resolve nem cancela o gate seletivo de P01 para release.

## Escopo mínimo, gates e prazo

P04 tem uma entrega verificável: matriz pequena de casos fixos, medições reais backend-side autorizadas e decisão documentada de principal/secundário, incluindo gratuidade, limites, privacidade e falhas. Sem framework de benchmark, refatoração, nova dependência ou troca de provider. Groq/Gemini só entram se a necessidade do complemento opcional for demonstrada; catálogo offline continua obrigatório e fora deste marco.

Gates já registrados: contratos funcionais P01, P02 concluído, preflight 23/23 e preservação terminal. Gates restantes de P04: aprovação deste digest, corpus com direitos/consentimento, condições oficiais vigentes verificadas na coleta futura, autorização limitada dos efeitos externos, medições comparáveis sem segredos, revisão da decisão e integridade documental. Prova ausente é not_run/blocked, nunca medição simulada. Gates de release permanecem pendentes, incluindo a garantia de P01 e homologação; esta proposta não autoriza entrega final.

O prazo é considerado reduzindo retrabalho: reaproveitar provas intactas, uma amostra piloto pequena, nenhuma repetição das suítes antigas sem alteração nos seams, nenhum novo score perseguido. Se faltarem corpus, credenciais ou gratuidade, parar no limite externo U-101 sem instalar ferramentas ou ampliar gastos.

## Aprovação e preservação

A skill exige uma aprovação humana única do manifesto novo e do plano P04. P01/P02/P03 são incluídos somente como contratos históricos imutáveis com seus estados preservados, não para reexecutá-los. `planning_status=pending_approval`, `approval.status=pending`, sem execução ativa. Não há nova autorização de mutação.

Manifesto R6 preservado: `artifacts/bianchini/v2/approval/manifest-p03-r6.sha256`, digest `18cef0bf86bc6eecfaa10a8ee241e0c4fa3d543fbcdcd90cca75d6b661c032e1`. Aprovação histórica R6: supervisor, `2026-09-09T01:38:16Z`; checkpoint de preparação `cc5907c75b59f39cd5d5f8f11538448068ab91b3` permanece separado. Nenhum desses vínculos é autorização reutilizável.
