# Readiness — P05 / F1-MAN01

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "581b4bcc7b5ff777c9fd6b8e655862bb780b7d5f69e228056b3d644a94b5d9e3",
  "repository_revision": "a34da4dd34eea58921862f0d0fa2d0016be5ce31",
  "design_required": false,
  "impact_map": {
    "applications": [
      "artefatos documentais ScanPlant; nenhuma aplicação de produto alterada"
    ],
    "modules": [
      "manifesto de classes offline e validador documental Python"
    ],
    "contracts": [
      "14 classes ordenadas; resolução de nomes; revisão taxonômica"
    ],
    "data": [
      "12 espécies aprovadas via U-201, sinônimos e duas proteções"
    ],
    "platforms": [
      "Python 3.12 stdlib em Linux/WSL2; consumidores futuros fora do escopo"
    ]
  },
  "decisions": [
    {
      "id": "D-001",
      "statement": "P01 permanece blocked-terminal e não é reaberto por R6.",
      "evidence": "ledger P01",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-002",
      "statement": "P02 permanece completed e independente de P03.",
      "evidence": "ledger P02",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-013",
      "statement": "P03-R5/U-008 is immutable terminal evidence: campaign_count is 1, U-008 is consumed, and no mutant/report exists.",
      "evidence": "/tmp/p03-r5-u007.h8rfIr/u008-campaign-started/campaign-count; u008-campaign-results/log",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-014",
      "statement": "The only future test project is ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj targeting net8.0.",
      "evidence": "MutationHarness csproj and R5 host-completion 23/23",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-015",
      "statement": "A generated run-dir-local solution with exactly API plus harness replaces automatic discovery of the versioned solution for R6 campaign context.",
      "evidence": "R5 log proves ScanPlantAPI.sln selected ScanPlantAPI.Tests.csproj and NETSDK1045",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-016",
      "statement": "R6 is a material-change replan of execution configuration only; source, csproj, TargetFrameworks, SDK, Stryker, targets, reporters and thresholds remain frozen.",
      "evidence": "bm.py change-policy result; R5 terminal log",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-101",
      "statement": "Recomendar A: P01/P03 blocked-terminal, P02 completed e release pending; propor somente continuidade F1-API01, sem waiver.",
      "evidence": "POST-U009-DELIBERATION.md: matriz de critérios, ledgers e regra terminal R6.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-102",
      "statement": "P04 entrega protocolo, evidência comparativa e decisão; não cria adaptadores de produção nem troca provider/mobile.",
      "evidence": "Roadmap §6, marco seguinte F1-API01; contratos existentes e P02 completed.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-103",
      "statement": "Não usar Stryker nem processos isolados em P04; preflight descartável real é obrigatório para qualquer proposta futura com isolamento.",
      "evidence": "Falha U-009 ocorreu após preflight que só criou namespace, sem provar comunicação de filhos.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-201",
      "statement": "Criar somente P05/F1-MAN01 no ciclo v2 existente: manifesto completo, referências, validador e revisão em uma unidade; preservar todos os estados terminais e completed.",
      "evidence": "PROJECT_STATE.md no HEAD obrigatório e roadmap §6; inventário mostra P01 a P04 e nenhum identificador F1-MAN prévio.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md"
      ]
    },
    {
      "id": "D-202",
      "statement": "Contrato JSON UTF-8 v1 com 12 classes species e 2 protection, IDs e índices estáveis, nomes e sinônimos com proveniência, normalização exata e colisões rejeitadas.",
      "evidence": "Resultados explicitamente solicitados; nenhum manifesto botânico atual encontrado.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md"
      ]
    },
    {
      "id": "D-203",
      "statement": "Execução futura usa somente Python 3.12 stdlib/Git e leitura taxonômica oficial; sem produto, instalação, dataset ou mutação. Design não requerido.",
      "evidence": "Inspeção do ambiente e manifestos; escopo documental sem consumidores ativos.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md"
      ]
    }
  ],
  "assumptions": [
    {
      "id": "A-001",
      "impact": "high",
      "status": "confirmed",
      "statement": "P02 não depende da conclusão de P01/P03.",
      "evidence": "ledger P02",
      "fallback": "preservar P02 completed",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-007",
      "impact": "critical",
      "status": "bounded",
      "statement": "O cache/feed/toolchain foi pré-condição histórica R6, não insumo nem prontidão atual de P04.",
      "evidence": "progress.log terminal registra preflight aprovado; não houve revalidação ambiental nesta deliberação.",
      "fallback": "Não usar ou modificar esses insumos por P04; qualquer plano futuro terá preflight próprio não consumidor.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-101",
      "impact": "high",
      "status": "bounded",
      "statement": "Provas funcionais históricas permanecem relevantes nos caminhos comparados, mas não são fingerprint de RC atual.",
      "evidence": "Git diff dos caminhos externos/harness contra a9d245d9a832f98bcbaadc93973959d61cf936df e de ScanPlant-Final contra 0faf65bcee27da1a33e924cfc5d826f31bdacdca: vazios.",
      "fallback": "Mudança no seam ou regressão comprovada impede reutilizar a prova; manter release pending.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-102",
      "impact": "high",
      "status": "bounded",
      "statement": "A disponibilidade de corpus, direitos, credenciais e condições gratuitas atuais ainda não foi comprovada.",
      "evidence": "Roadmap exige revalidar termos na execução; ledgers não contêm benchmark comparativo aprovado.",
      "fallback": "Sem U-101, somente protocolo/documentação; dados not_run, sem vencedor ou encerramento artificial.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-201",
      "impact": "high",
      "status": "bounded",
      "statement": "A lista nominal completa das 12 espécies não está demonstrada no repositório; o piloto de cinco é apenas subconjunto documentado.",
      "evidence": "Roadmap §3/§6, F1-G01 §Escopo e spec P04 §Protocolo; busca nominal/documental no HEAD não encontrou lista completa.",
      "fallback": "U-201 é indispensável antes de preencher qualquer lista canônica; manter P05 incompleto, sem completar por inferência ou fonte web.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md"
      ]
    },
    {
      "id": "A-202",
      "impact": "medium",
      "status": "confirmed",
      "statement": "Python 3.12 stdlib basta para JSON, Unicode, hashes, asserts e unittest do validador documental; nenhuma dependência nova.",
      "evidence": "Python 3.12.3 e ferramentas já inspecionados; JSON/documentos locais seguem essa estratégia.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md"
      ]
    }
  ],
  "pitfalls": [
    {
      "id": "P-001",
      "impact": "critical",
      "statement": "P02 não pode ser reaberto pelo replanejamento P03.",
      "prevention": "preservar status P02",
      "recovery": "manter P02 completed",
      "verification": "ledger P02",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-002",
      "impact": "high",
      "statement": "P01 não recebe waiver por uma campanha R6.",
      "prevention": "preservar bloqueio terminal",
      "recovery": "manter P01 blocked-terminal",
      "verification": "ledger P01",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-014",
      "impact": "critical",
      "statement": "An empty TestProjects list can select the multi-target project and invalidate SDK 8 execution before mutation.",
      "prevention": "require explicit harness path and reject any multi-target project before build",
      "recovery": "stop preflight with campaign_count=1 and do not invoke Stryker",
      "verification": "launcher/config parse and temporary-solution member audit",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-015",
      "impact": "critical",
      "statement": "A solution-context build can reintroduce ScanPlantAPI.sln even when a test project is explicit.",
      "prevention": "pass only the generated two-member net8 solution and verify its exact members before build/campaign",
      "recovery": "stop before U-009 with campaign_count=1",
      "verification": "temporary solution text/hash plus build transcript showing no net10.0",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-016",
      "impact": "critical",
      "statement": "U-008 cannot be reused and a new campaign must not reset the accumulated count.",
      "prevention": "U-009 is separately approved after preflight and launcher permits only atomic 1 -> 2",
      "recovery": "existing or invalid marker stops without a new invocation",
      "verification": "state transition evidence and launcher guard",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-017",
      "impact": "high",
      "statement": "The Codex sandbox blocks VSTest local sockets despite valid loopback.",
      "prevention": "run targeted preflight only in WSL normal",
      "recovery": "do not interpret sandbox SocketException as product/test failure or retry there",
      "verification": "WSL transcript records executor and 23/23",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-101",
      "impact": "critical",
      "statement": "Progressão pode ser confundida com dispensa de garantia ou release concluído.",
      "prevention": "Preservar P01/P03 blocked, release pending e ausência de score U-009; não reabrir R6.",
      "recovery": "Parar fechamento de release; registrar a lacuna, sem criar autorização de mutação.",
      "verification": "Estado, deliberação e revisão semântica concordam; manifestos históricos íntegros.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-102",
      "impact": "high",
      "statement": "Medição externa pode expor dados/credenciais, gerar cobrança ou concluir além da amostra.",
      "prevention": "Corpus sem dados pessoais, direitos/consentimento, orçamento zero, teto de chamadas, sem retry; origem e versão por resultado.",
      "recovery": "Interromper no limite externo e preservar somente resultado sanitizado; nunca completar a matriz por estimativa.",
      "verification": "U-101, inventário/checksums, varredura de segredos e revisão de comparabilidade/limitações.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-103",
      "impact": "high",
      "statement": "O diagnóstico terminal interpreta incorretamente lo_flags=0x9 como sem IFF_UP.",
      "prevention": "Registrar a contradição fora da evidência imutável; não apresentar causa exclusiva.",
      "recovery": "Manter causa específica indeterminada e nenhuma repetição diagnóstica da campanha.",
      "verification": "Conferir 0x9 & 0x1 = 0x1 e mensagens exatas de stryker.log.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-201",
      "impact": "high",
      "statement": "Nomes comuns, sinônimos, controles e piloto podem ser confundidos com novas espécies do escopo.",
      "prevention": "U-201 exige 12 táxons aprovados; cada mapeamento deve ter fonte, sem adicionar Bellis perennis por ser controle.",
      "recovery": "Rejeitar a entrada ambígua e manter P05 pendente na mesma U-201; não inventar substituições.",
      "verification": "Revisão humana 12/12 contra fonte aprovada e testes de táxon/alias duplicado.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md"
      ]
    },
    {
      "id": "P-202",
      "impact": "high",
      "statement": "Normalização agressiva, colisões e reordenação silenciosa corromperiam contratos futuros.",
      "prevention": "Separar namespace taxonômico e nomes comuns; normalização Unicode definida; índices 0–13 contíguos e freeze explícito de IDs/ordem.",
      "recovery": "Validador falha fechado; divergência taxonômica material retorna a U-201; versão major exigida por alteração futura de ordem/membresia.",
      "verification": "Casos negativos para colisões canônico/sinônimo, repetição, missing class, bool como índice e reordenação.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md"
      ]
    },
    {
      "id": "P-203",
      "impact": "medium",
      "statement": "Acrescentar o ledger vivo ao pacote causaria drift do snapshot após append; conclusão do manifesto não encerra gates de release.",
      "prevention": "Ledger P05 append-only fora do snapshot; fatos congelados/policy ficam na pesquisa/review; estado vivo e manifesto não integram a própria lista.",
      "recovery": "Manter release pending; não alterar manifestos antigos para fazê-los conferir com arquivos vivos.",
      "verification": "Snapshot novo e diff de todos os históricos contra HEAD; estados anteriores preservados.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md"
      ]
    }
  ],
  "user_actions": [
    {
      "id": "U-001",
      "needed_by": "P02",
      "statement": "A aprovação histórica de P02 é preservada.",
      "fallback": "não reabrir P02",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "can_continue_without": false,
      "evidence_required": "ledger P02",
      "historical_only": true
    },
    {
      "id": "U-009",
      "needed_by": "P03",
      "statement": "U-009 foi consumida na execução terminal; nenhuma ação nova é permitida por este item histórico.",
      "fallback": "Não invocar campanha, não recriar marcador, preservar campaign_count=2.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "can_continue_without": false,
      "evidence_required": "campaign-summary.txt e campaign-count da evidência terminal versionada.",
      "historical_only": true
    },
    {
      "id": "U-101",
      "needed_by": "P04",
      "statement": "Autorização histórica P04 consumida em 14 identificações, zero texto e zero retry; P04 completed. Nenhuma nova transmissão autorizada.",
      "can_continue_without": false,
      "fallback": "Preservar P04 completed e não repetir slots.",
      "evidence_required": "Registro sanitizado de autorização limitada, direitos do corpus, termos oficiais datados, teto de gasto/chamadas e identificação do executor; nenhum segredo no repositório.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "U-201",
      "needed_by": "P05",
      "status": "pending",
      "statement": "Responsável fornece a lista completa das 12 espécies já aprovadas ou sua fonte autoritativa; confirma mapeamento taxonômico ambíguo e, no gate final da mesma unidade, revisa os 12 registros e as duas proteções.",
      "can_continue_without": false,
      "needed_at": "Antes de iniciar a população do manifesto; aceite taxonômico e semântico novamente no gate único da entrega.",
      "fallback": "Sem lista inequívoca, P05 permanece incompleto; planejamento do contrato pode ser aprovado, porém nenhuma espécie é escolhida automaticamente. Fonte oficial indisponível ou conflito permanece nesta fronteira, sem aceite fictício.",
      "evidence_required": "Documento/relação explícita de 12 táxons aprovada pelo responsável, registrada sem PII em approved-species-roster.json na execução; revisão final vinculada ao SHA-256 do manifesto e da evidência taxonômica.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md"
      ]
    }
  ],
  "spikes": [
    {
      "id": "S-001",
      "status": "passed",
      "statement": "P02 é independente do bloqueio de P01/P03.",
      "evidence": "ledger P02",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "decision": "Preservar P02 completed.",
      "historical_only": true
    },
    {
      "id": "S-006",
      "status": "passed",
      "statement": "The terminal R5 log identifies the exact failing graph and the harness graph is locally distinguishable without modifying projects.",
      "evidence": "/tmp/p03-r5-u007.h8rfIr/u008-campaign-results/logs/log-20260908.txt; csproj and solution inspection",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "decision": "Use explicit harness selection plus a generated two-member solution.",
      "historical_only": true
    },
    {
      "id": "S-101",
      "status": "passed",
      "statement": "Leitura documental encerrou a deliberação de dependência; não foi realizado experimento.",
      "evidence": "POST-U009-DELIBERATION.md, comparação Git estática, regra R6 e ledgers P01/P02.",
      "decision": "Propor A para F1-API01, preservando bloqueio de release e rejeitando B nesta rodada.",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    }
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {
      "id": "SD-001",
      "statement": "P01/P02 mantêm contratos e estados históricos.",
      "source": "docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md",
      "target": "docs/bianchini/current/specs/replan-v2.md",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "historical_only": true
    },
    {
      "id": "SD-006",
      "statement": "The accepted future campaign contract binds one net8 harness and one run-dir-local two-member solution, with U-009 and a monotonic 1 -> 2 counter.",
      "source": "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
      "target": "docs/bianchini/current/specs/mutation-campaign-test-project-isolation.md",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "SD-101",
      "statement": "Contrato completo da decisão comparativa, sem mudança de contratos de produto.",
      "source": "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md",
      "target": "docs/bianchini/current/specs/provider-benchmark-decision.md",
      "destinations": [
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ],
      "historical_only": true
    },
    {
      "id": "SD-201",
      "statement": "Contrato integral esperado do manifesto offline, condicionado à entrada U-201, com sincronização proibida até encerramento regular do ciclo.",
      "source": "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
      "target": "docs/bianchini/current/specs/offline-class-manifest.md",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md"
      ]
    }
  ],
  "readiness_scope": "Ready significa contrato de planejamento e fronteiras definidos. Não afirma que a lista completa ou a taxonomia final já foram obtidas. U-201 impede população e conclusão; o pacote não concede execução.",
  "inherited_contracts": "Projeção mínima de referências dos quatro planos históricos para satisfazer rastreabilidade do audit. historical_only não constitui aprovação nova, autorização de campanha ou repetição de benchmark. Fontes históricas não foram reexecutadas; nenhum log P03 foi percorrido."
}
```
