# Readiness P08

```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "1ad0136669f82fcf9307b7dce287f544ed256c1205a70e2a717a041867167197",
  "repository_revision": "b6844f9129d9edf862ae7958d8f043d9bdd5bd84",
  "design_required": false,
  "impact_map": {
    "applications": [
      "nenhuma alteração de produto"
    ],
    "modules": [
      "scripts/phase1 aquisição e curadoria P08"
    ],
    "contracts": [
      "persistência externa",
      "mapeamento taxonômico",
      "licença e aceite humano"
    ],
    "data": [
      "candidatos novos externos; 17 P07 somente leitura"
    ],
    "platforms": [
      "Python/Pillow em Linux/WSL"
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
      ],
      "historical_only": true
    },
    {
      "id": "D-202",
      "statement": "Contrato JSON UTF-8 v1 com 12 classes species e 2 protection, IDs e índices estáveis, nomes e sinônimos com proveniência, normalização exata e colisões rejeitadas.",
      "evidence": "Resultados explicitamente solicitados; nenhum manifesto botânico atual encontrado.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-203",
      "statement": "Execução futura usa somente Python 3.12 stdlib/Git e leitura taxonômica oficial; sem produto, instalação, dataset ou mutação. Design não requerido.",
      "evidence": "Inspeção do ambiente e manifestos; escopo documental sem consumidores ativos.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/STACK_RESEARCH-p05-f1-man01.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-211",
      "statement": "Decisão humana U-201: quatro homônimos inelegíveis como chaves authorless; None, evidência e quarentena explícita; novo conflito bloqueia aceite.",
      "evidence": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md; artifacts/bianchini/v2/planning/p05-r1-policy.json",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-212",
      "statement": "Proposta para aprovação: manifest_version 1.1.0 conforme minor local por mudança de resolução; schema e normalização permanecem 1.",
      "evidence": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md; artifacts/bianchini/v2/planning/p05-r1-policy.json",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-213",
      "statement": "Replanejar só P05-R1, preservar histórico P05 e todos os outros planos/release; nenhum código alterado nesta rodada.",
      "evidence": "docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md; artifacts/bianchini/v2/planning/p05-r1-policy.json",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-701",
      "statement": "P07 é somente curadoria das 17 imagens externas, uma unidade; P06 e todos os estados históricos permanecem imutáveis.",
      "evidence": "APPROVED_SCOPE P07; P06-recovery-20260928.md; PROJECT_STATE no HEAD",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-702",
      "statement": "Somente decisão humana por imagem pode aprovar ou rejeitar; critérios automáticos geram sinais e pendências, nunca promoção.",
      "evidence": "APPROVED_SCOPE P07; P06 human-decisions não concede aprovação botânica",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-703",
      "statement": "Pillow 12.3.0 e stdlib bastam; nitidez usa variância Laplaciana e duplicata visual usa dHash horizontal 64 bits/Hamming com limiares de triagem versionados.",
      "evidence": "STACK_RESEARCH-p07.md com fontes primárias Pillow e ImageHash",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-704",
      "statement": "Resultado completo e privado fica fora do Git; resumo sanitizado no Git; zero aprovadas e classes vazias são conclusões válidas.",
      "evidence": "APPROVED_SCOPE P07; recovery-20260928.json usable=0",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "D-801",
      "statement": "Uma unidade P08 coesa; manter v2 aberto sem homologação/cycle-close e corrigir publicação P07 no estado vivo.",
      "evidence": "Escopo P08 e STACK_RESEARCH-p08.md; baseline b6844f9.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "D-802",
      "statement": "Commons e iNaturalist elegíveis condicionalmente; GBIF/outros publishers e datasets acadêmicos bloqueados; limites 20 arquivos/100 candidatos por fonte/classe.",
      "evidence": "Escopo P08 e STACK_RESEARCH-p08.md; baseline b6844f9.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "D-803",
      "statement": "CC0 1.0/CC BY 4.0 somente com prova por item; atribuição externa; ambiguidade bloqueia.",
      "evidence": "Escopo P08 e STACK_RESEARCH-p08.md; baseline b6844f9.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "D-804",
      "statement": "Manifesto P05/P05-R1 imutável; ID taxonômico e confirmação botânica humana obrigatórios para aprovar.",
      "evidence": "Escopo P08 e STACK_RESEARCH-p08.md; baseline b6844f9.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "D-805",
      "statement": "Original/journal/dataset externos e integridade P07 preservada; zero e treino bloqueado são conclusão válida.",
      "evidence": "Escopo P08 e STACK_RESEARCH-p08.md; baseline b6844f9.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
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
      ],
      "historical_only": true
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
      ],
      "historical_only": true
    },
    {
      "id": "A-211",
      "impact": "high",
      "status": "bounded",
      "statement": "Os demais 79 aliases esperados continuam sujeitos à conferência taxonômica oficial individual; contagem não prova elegibilidade.",
      "evidence": "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md (consulta histórica 2026-09-11); artifacts/bianchini/v2/planning/p05-r1-preflight.json",
      "fallback": "Se surgir outro homônimo ou prova insuficiente, bloquear U-201/aceite até revisão explícita, sem associação automática.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-701",
      "statement": "Os 17 arquivos externos e suas relações Q/R estarão disponíveis e íntegros na execução.",
      "impact": "high",
      "status": "bounded",
      "evidence": "Preflight de planejamento viu 17 arquivos e os manifestos externos; hashes não foram recalculados nesta rodada.",
      "fallback": "Falha de SHA/conjunto bloqueia curadoria e não cria decisão ou substituto.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-702",
      "statement": "As métricas e hashes perceptuais são sinais de revisão, não prova botânica nem de privacidade.",
      "impact": "medium",
      "status": "confirmed",
      "evidence": "Algoritmo definido em STACK_RESEARCH-p07.md; contrato humano no escopo.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "A-801",
      "statement": "Disponibilidade suficiente não demonstrada.",
      "impact": "high",
      "status": "bounded",
      "evidence": "P07 summary: usable=0; pesquisa sem consultas de inventário.",
      "fallback": "Encerrar com zero/classes vazias e treino bloqueado.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "A-802",
      "statement": "API/prova legal e taxonômica por item podem ser insuficientes.",
      "impact": "high",
      "status": "bounded",
      "evidence": "R05–R14; API iNaturalist dinâmica sem schema integral legível nesta pesquisa.",
      "fallback": "Fixtures até limite de execução; fonte/item indisponível, sem substituir licença/ID por inferência.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
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
      ],
      "historical_only": true
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
      ],
      "historical_only": true
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
      ],
      "historical_only": true
    },
    {
      "id": "P-211",
      "impact": "high",
      "statement": "Apagar evidência ou reinserir homônimo silenciosamente.",
      "prevention": "Manter evidência quarantined com autorias/conflito/fontes e rejeitar inclusão no mapa.",
      "recovery": "Bloquear aceitação; corrigir na mesma unidade conforme policy.",
      "verification": "Teste negativo de reintrodução dos quatro e revisão humana da evidência.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-212",
      "impact": "high",
      "statement": "Contagem igual pode ocultar perda ou troca de alias/canônico.",
      "prevention": "Comparar conjuntos e mapeamentos normalizados por class_id contra o checkpoint.",
      "recovery": "Parar em qualquer diferença além de Q.",
      "verification": "Final = baseline menos Q; 12 canônicos, todos os outros aliases e roster idênticos.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-213",
      "impact": "high",
      "statement": "Confundir decisão recebida, aprovação do pacote e aceite dos bytes.",
      "prevention": "Separar estados da política, planejamento, execução e aceite final.",
      "recovery": "Manter P05 incompleto, U-201 aberta e release pending.",
      "verification": "Hashes finais ligados a decisão humana; históricos íntegros.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-701",
      "statement": "Mutação acidental do dataset P06 ou perda de proveniência.",
      "impact": "high",
      "prevention": "Abrir entradas somente em leitura, fixar conjunto/hash antes e depois, saída separada e nenhuma recodificação ou deleção.",
      "recovery": "Parar e preservar evidence; não corrigir bytes nem buscar substitutos no P07.",
      "verification": "17/17 hashes e conjunto iguais antes/depois; manifesto e decisões P06 byte-iguais.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-702",
      "statement": "Falso positivo de limiar pode rejeitar imagem útil ou par distinto.",
      "impact": "high",
      "prevention": "Limiar apenas sinaliza; revisão humana por imagem/par é obrigatória; nenhum estado final automático.",
      "recovery": "Manter needs_human_review ou needs_botanical_review até parecer registrado.",
      "verification": "Fixtures de fronteira e prova de que nenhum caminho algorítmico emite approved_for_dataset ou rejected_*.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-703",
      "statement": "Metadados e observações privadas podem vazar para Git.",
      "impact": "high",
      "prevention": "Per-image completo externo; no Git somente resumo sem autoria, URLs de arquivo, imagem ou descrição de identificáveis.",
      "recovery": "Bloquear publicação e corrigir artefato sanitizado antes de aceite final.",
      "verification": "Inspeção de arquivos novos e diffs, allowlist de campos, zero imagem/segredo/dado pessoal no Git.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "P-801",
      "statement": "Promover rótulo/licença/privacidade inconclusivos.",
      "impact": "high",
      "prevention": "Gates independentes, prova por item e perito para botânica.",
      "recovery": "Manter pendente/rejeitado; nunca preencher por classificador.",
      "verification": "Testes de licença divergente, alias homônimo, perito ausente e privacidade incerta.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "P-802",
      "statement": "Perda, sobrescrita ou vazamento em retomada.",
      "impact": "high",
      "prevention": "Journal durável, lock, hashes, diretório novo externo, projeção allowlist.",
      "recovery": "Bloquear em corrupção; preservar prefixo/órfãos para reconciliação explícita.",
      "verification": "Crash boundaries, concorrência, traversal/symlink, hashes P07 antes/depois e inspeção de Git.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
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
      "needed_by": "P05-R1",
      "status": "completed",
      "statement": "U-201 e P05/P05-R1 concluídos no histórico; nenhuma ação nova é concedida.",
      "can_continue_without": true,
      "needed_at": "Antes de iniciar a população do manifesto; aceite taxonômico e semântico novamente no gate único da entrega.",
      "fallback": "Preservar P05/P05-R1 completed e hashes aceitos; não reabrir.",
      "evidence_required": "Ledger P05 e aceite humano versionado.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-f1-man01.md",
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
        "docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "U-701",
      "needed_by": "P07",
      "status": "pending",
      "statement": "Revisor humano examina cada uma das 17 imagens em resolução original e decide estado ou pendência com responsável, instante e justificativa; aprovação de imagem exige evidência botânica suficiente.",
      "needed_at": "Após análise técnica, antes de concluir P07.",
      "can_continue_without": true,
      "fallback": "Continuar apenas análise técnica; P07 não conclui sem 17 pareceres humanos, ainda que alguns permaneçam needs_*.",
      "evidence_required": "17 decisões vinculadas a Q/R, SHA-256, classe, responsável e timestamp.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "U-702",
      "needed_by": "P07",
      "status": "pending",
      "statement": "Responsável aceita os bytes finais e hashes do pacote de curadoria antes de qualquer commit ou push.",
      "needed_at": "Após relatório e gates, antes de commit/push; não é aprovação do planejamento.",
      "can_continue_without": true,
      "fallback": "Preservar resultado não publicado e P07 sem fechamento formal até aceite.",
      "evidence_required": "Aceite humano explícito de versão, hash do JSON externo e resumo Git, contagens e limitações.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "U-703",
      "needed_by": "P07",
      "status": "pending",
      "statement": "Disponibilizar leitura do P06 externo e escrita somente em diretório externo novo de resultados P07; não alterar P06.",
      "needed_at": "Antes da execução que persistir resultados externos.",
      "can_continue_without": true,
      "fallback": "Planejar e testar com fixtures sintéticas; parar antes de escrita externa ou conclusão real se acesso faltar.",
      "evidence_required": "Caminho externo autorizado, prova de isolamento e integridade 17/17 do P06.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p07.md",
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "U-801",
      "needed_by": "P08",
      "status": "pending",
      "statement": "Decidir pacote/digest P08; aprovação de planejamento não autoriza execução, staging, commit ou push.",
      "needed_at": "Antes de qualquer implementação.",
      "can_continue_without": true,
      "fallback": "Manter pacote pendente e nenhum código novo.",
      "evidence_required": "Aceite explícito do digest e, em outra instrução, escopo de execução.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "U-802",
      "needed_by": "P08",
      "status": "pending",
      "statement": "Autorizar rodada de rede, fontes/limites, diretório persistente externo novo, acesso somente leitura P06/P07 e responsável pela guarda.",
      "needed_at": "Antes de aquisição real.",
      "can_continue_without": true,
      "fallback": "Somente fixtures sintéticas e relatório not_run; não declarar execução concluída.",
      "evidence_required": "Diretório absoluto autorizado fora de Git, sem conflito, permissões restritas e backup validado.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "U-803",
      "needed_by": "P08",
      "status": "pending",
      "statement": "Designar revisor botânico qualificado e responsável por direitos/privacidade; validar crosswalk e pareceres por hash.",
      "needed_at": "Antes de consultas por taxon ID e antes de qualquer aprovação de imagem.",
      "can_continue_without": true,
      "fallback": "Classe sem crosswalk não consultada; imagens sem confirmação permanecem pendentes, zero aprovadas possível.",
      "evidence_required": "Identidade/qualificação do perito, evidência taxonômica, decisão humana por item, recibos privados.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
      ]
    },
    {
      "id": "U-804",
      "needed_by": "P08",
      "status": "pending",
      "statement": "Aceitar resultados e bytes finais pelo digest de dataset/decisões/resumo; decidir eventual publicação em autorização separada.",
      "needed_at": "Após testes e curadoria e antes de qualquer staging/commit/push futuro.",
      "can_continue_without": true,
      "fallback": "Entrega pending_human_acceptance; nenhuma publicação.",
      "evidence_required": "Recibo humano do digest final, incluindo zero/vazios/pendências, sem autorização de treino.",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS-p08.md",
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
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
    },
    {
      "id": "S-701",
      "status": "passed",
      "statement": "Pesquisa técnica delimitada de Pillow/dHash e inventário local das entradas P06.",
      "evidence": "STACK_RESEARCH-p07.md e cartografia scratch vinculada ao HEAD/escopo.",
      "decision": "Usar Pillow 12.3.0 + stdlib, sem dependência pesada; todas as métricas são triagem.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "S-801",
      "status": "passed",
      "statement": "Inspeção estática encerrada: extensão delimitada das funções puras, sem coleta ou experimento.",
      "evidence": "STACK_RESEARCH-p08.md; acquire_commons.py e curate_p07.py lidos no baseline.",
      "decision": "Orquestrador P08 e adapter iNaturalist; não reutilizar finalizador fixo de P07.",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md"
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
      "statement": "Contrato completo esperado do manifesto após P05-R1: minor 1.1.0 e quarentena authorless, roster preservado; sincronização somente no encerramento regular do ciclo.",
      "source": "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md",
      "target": "docs/bianchini/current/specs/offline-class-manifest.md",
      "destinations": [
        "docs/bianchini/changes/v2/specs/offline-class-manifest-change.md",
        "docs/bianchini/changes/v2/plans/P05-f1-man01-offline-class-manifest.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md",
        "docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md",
        "docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md",
        "docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md"
      ],
      "historical_only": true
    },
    {
      "id": "SD-701",
      "statement": "Contrato completo da curadoria rastreável P07, sem sincronização de current_specs antes do encerramento regular.",
      "source": "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md",
      "target": "docs/bianchini/current/specs/traceable-dataset-curation.md",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p07-curation-change.md",
        "docs/bianchini/changes/v2/plans/P07-traceable-dataset-curation.md",
        "docs/bianchini/changes/v2/spec-deltas/traceable-dataset-curation.md"
      ],
      "historical_only": true
    },
    {
      "id": "SD-801",
      "statement": "Contrato completo da recuperação de dataset; current/specs não sincronizado.",
      "source": "docs/bianchini/changes/v2/spec-deltas/dataset-recovery.md",
      "target": "docs/bianchini/current/specs/dataset-recovery.md",
      "destinations": [
        "docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md",
        "docs/bianchini/changes/v2/plans/P08-dataset-recovery.md",
        "docs/bianchini/changes/v2/spec-deltas/dataset-recovery.md"
      ]
    }
  ],
  "readiness_scope": "Somente P08 novo; prontidão para aprovar planejamento; execução real condicionada às U-801..804. Registros anteriores são históricos.",
  "inherited_contracts": "P07 completed/publicado; P01/P03 bloqueios terminais preservados; P06/P07 não reabertos; release pending; nenhuma autorização de treinamento."
}
```
