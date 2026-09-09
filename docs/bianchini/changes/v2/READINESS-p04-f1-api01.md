# Readiness — continuidade P04/F1-API01

Prontidão do planejamento, não da execução. Itens herdados são históricos; comandos P01/P03 continuam proibidos. O gate humano do pacote novo permanece pendente.

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "d556bf41a873a980bfca8cd2d4fa23c255cfbabad090a649675c4b82bd01f146",
  "repository_revision": "14980b1f181e00ba1ee259a27cc2209b0a013364",
  "design_required": false,
  "impact_map": {
    "applications": [
      "documentação de continuidade ScanPlant"
    ],
    "modules": [
      "decisão comparativa F1-API01"
    ],
    "contracts": [
      "protocolo de evidência e limite externo U-101; contratos API/mobile inalterados"
    ],
    "data": [
      "matriz sanitizada de benchmark futura; evidência U-009 imutável"
    ],
    "platforms": [
      "executor backend-side de coleta futura; nenhuma plataforma de produto alterada"
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "artifacts/bianchini/v2/checkpoints/P03-R5-U008-terminal-attempt-716ef26.json"
      ],
      "historical_only": true
    },
    {
      "id": "D-014",
      "statement": "The only future test project is ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj targeting net8.0.",
      "evidence": "MutationHarness csproj and R5 host-completion 23/23",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-015",
      "statement": "A generated run-dir-local solution with exactly API plus harness replaces automatic discovery of the versioned solution for R6 campaign context.",
      "evidence": "R5 log proves ScanPlantAPI.sln selected ScanPlantAPI.Tests.csproj and NETSDK1045",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-016",
      "statement": "R6 is a material-change replan of execution configuration only; source, csproj, TargetFrameworks, SDK, Stryker, targets, reporters and thresholds remain frozen.",
      "evidence": "bm.py change-policy result; R5 terminal log",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-101",
      "statement": "Recomendar A: P01/P03 blocked-terminal, P02 completed e release pending; propor somente continuidade F1-API01, sem waiver.",
      "evidence": "POST-U009-DELIBERATION.md: matriz de critérios, ledgers e regra terminal R6.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
      ]
    },
    {
      "id": "D-102",
      "statement": "P04 entrega protocolo, evidência comparativa e decisão; não cria adaptadores de produção nem troca provider/mobile.",
      "evidence": "Roadmap §6, marco seguinte F1-API01; contratos existentes e P02 completed.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md"
      ]
    },
    {
      "id": "D-103",
      "statement": "Não usar Stryker nem processos isolados em P04; preflight descartável real é obrigatório para qualquer proposta futura com isolamento.",
      "evidence": "Falha U-009 ocorreu após preflight que só criou namespace, sem provar comunicação de filhos.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
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
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
      ]
    },
    {
      "id": "A-102",
      "impact": "high",
      "status": "bounded",
      "statement": "A disponibilidade de corpus, direitos, credenciais e condições gratuitas atuais ainda não foi comprovada.",
      "evidence": "Roadmap exige revalidar termos na execução; ledgers não contêm benchmark comparativo aprovado.",
      "fallback": "Sem U-101, somente protocolo/documentação; dados not_run, sem vencedor ou encerramento artificial.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md"
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
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
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
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
      ]
    },
    {
      "id": "P-102",
      "impact": "high",
      "statement": "Medição externa pode expor dados/credenciais, gerar cobrança ou concluir além da amostra.",
      "prevention": "Corpus sem dados pessoais, direitos/consentimento, orçamento zero, teto de chamadas, sem retry; origem e versão por resultado.",
      "recovery": "Interromper no limite externo e preservar somente resultado sanitizado; nunca completar a matriz por estimativa.",
      "verification": "U-101, inventário/checksums, varredura de segredos e revisão de comparabilidade/limitações.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
      ]
    },
    {
      "id": "P-103",
      "impact": "high",
      "statement": "O diagnóstico terminal interpreta incorretamente lo_flags=0x9 como sem IFF_UP.",
      "prevention": "Registrar a contradição fora da evidência imutável; não apresentar causa exclusiva.",
      "recovery": "Manter causa específica indeterminada e nenhuma repetição diagnóstica da campanha.",
      "verification": "Conferir 0x9 & 0x1 = 0x1 e mensagens exatas de stryker.log.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p04-f1-api01.md"
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
        "docs/bianchini/changes/v2/USER_ACTIONS-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
        "docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r6.md"
      ],
      "can_continue_without": false,
      "evidence_required": "campaign-summary.txt e campaign-count da evidência terminal versionada.",
      "historical_only": true
    },
    {
      "id": "U-101",
      "needed_by": "P04",
      "statement": "Antes de transmissão real: corpus com direitos/consentimento, volume esperado, condições atuais, credenciais somente no executor, teto financeiro zero e teto de 14 chamadas de identificação mais 4 textuais somente se justificadas.",
      "can_continue_without": true,
      "fallback": "Preparar protocolo; coleta not_run e decisão incompleta até resolver a dependência, sem compra ou troca silenciosa de provider.",
      "evidence_required": "Registro sanitizado de autorização limitada, direitos do corpus, termos oficiais datados, teto de gasto/chamadas e identificação do executor; nenhum segredo no repositório.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p04-f1-api01.md",
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
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
        "docs/bianchini/changes/v2/STACK_RESEARCH-p03-r6.md",
        "docs/bianchini/changes/v2/specs/replan-v2-p03-r6.md",
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
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md"
      ]
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
        "docs/bianchini/changes/v2/spec-deltas/mutation-campaign-test-project-isolation-r6.md",
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
        "docs/bianchini/changes/v2/specs/post-u009-continuity.md",
        "docs/bianchini/changes/v2/plans/P04-f1-api01-provider-benchmark.md",
        "docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md"
      ]
    }
  ],
  "readiness_scope": "Planejamento documental P04 pronto para aprovação; não significa prontidão ambiental, autorização externa nem reativação de P01/P03.",
  "inherited_contracts": "Itens R6 abaixo marcados historical_only preservam a rastreabilidade dos planos congelados e não autorizam executar seus comandos. As pré-condições históricas não foram repetidas."
}
```
