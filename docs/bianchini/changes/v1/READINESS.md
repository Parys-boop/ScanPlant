{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "2911045c093df8f8800d10546727af1285a2054e96cf43dd936e659d5545a0e4",
  "repository_revision": "22bbe55e4b0e6d5bb222b5d76572ce07d7533057",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlant-Final (mobile Expo/React Native)", "ScanPlantAPI (ASP.NET Core 8)"],
    "modules": ["PhotoScreen", "api.js", "Program.cs", "novo controller de identificação", "providers externos"],
    "contracts": ["POST /api/plant-identification/fallback", "IPlantIdentificationProvider", "IPlantKnowledgeProvider", "DTO público de fallback"],
    "data": ["imagem transitória em memória/arquivo temporário do multipart; sem persistência e sem migration"],
    "platforms": ["Android mobile por API HTTP", "backend .NET 8"]
  },
  "decisions": [
    {
      "id": "D-001",
      "statement": "Pl@ntNet é o único adaptador inicial de identificação; Plant.id fica fora do código do marco e somente como referência futura.",
      "evidence": "Plano canônico, seção 5, declara Pl@ntNet candidato preferencial e Plant.id referência secundária; pesquisa oficial em STACK_RESEARCH.md.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "D-002",
      "statement": "O contrato público é uma resposta ScanPlant neutra; nome, formato e erros de fornecedor não atravessam a fronteira mobile.",
      "evidence": "Plano canônico, seção 4, exige contratos substituíveis e DTO uniforme; PhotoScreen.js hoje contém o acoplamento a Plant.id/Groq.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    },
    {
      "id": "D-003",
      "statement": "Groq é enriquecimento textual opcional por IPlantKnowledgeProvider e não pode invalidar uma identificação já normalizada.",
      "evidence": "Plano canônico, seções 4 e 5; Groq atual é chamado somente depois de Plant.id em PhotoScreen.js.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "D-004",
      "statement": "A imagem do fallback é transitória e a prova PT-05 não é modificada, executada nem reinterpretada como classificador botânico de produto.",
      "evidence": "CHECKPOINT_FASE0_OFFLINE.md e F1-G01 registram PT-05 como prova técnica, não reconhecimento botânico; não há requisito de retenção no escopo aprovado.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    }
  ],
  "assumptions": [
    {
      "id": "A-001",
      "impact": "high",
      "status": "confirmed",
      "statement": "O produto ainda não possui classificador botânico offline para decidir automaticamente baixa confiança; F1-BE01 oferece apenas fallback explicitamente solicitado pelo usuário.",
      "evidence": "F1-G01 não aprovou modelo botânico; PhotoScreen.js faz chamada externa imediata e PT-05 usa MobileNet/ImageNet apenas como prova.",
      "fallback": "Não alegar decisão local inexistente; futura integração offline deverá chamar o mesmo endpoint apenas após sua própria decisão e consentimento.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    },
    {
      "id": "A-002",
      "impact": "high",
      "status": "bounded",
      "statement": "origin/master local aponta para 16d07f7 de 2026-06-01; a atualização remota não foi possível porque github.com não resolveu no ambiente.",
      "evidence": "git fetch origin --dry-run falhou por DNS nesta sessão; a comparação local encontrou somente appsettings.json em comum e merge-file retornou exit 0.",
      "fallback": "Não iniciar execução até autorização para atualizar origin e executar merge não-rebase; então repetir somente a comparação do ref atualizado.",
      "destinations": ["docs/bianchini/changes/v1/USER_ACTIONS.md", "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    }
  ],
  "pitfalls": [
    {
      "id": "P-001",
      "impact": "critical",
      "statement": "O bundle mobile hoje contém chamadas e nomes de chave de Plant.id/Groq; manter qualquer caminho direto viola o isolamento de segredos.",
      "prevention": "Remover constantes, URLs, fetches e entradas correspondentes do exemplo mobile; expor apenas cliente para a API ScanPlant.",
      "recovery": "Bloquear a entrega se busca estática ainda encontrar URL/chave/provider em ScanPlant-Final fora de documentação histórica não executável.",
      "verification": "Teste de contrato do cliente e busca estática focada no bundle mobile alterado.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    },
    {
      "id": "P-002",
      "impact": "critical",
      "statement": "multipart com arquivo controlado pelo usuário pode esgotar recursos ou encaminhar conteúdo não-imagem ao fornecedor.",
      "prevention": "Exigir uma imagem, limitar corpo/arquivo por configuração, conferir MIME permitido, assinatura e dimensões antes da chamada externa; não persistir arquivo nem usar nome do cliente.",
      "recovery": "Retornar ProblemDetails 400/413/415 seguro e descartar o stream sem chamar provider.",
      "verification": "Integração com arquivos ausente, excedido, MIME falso, assinatura inválida, dimensão inválida e imagem válida usando provider falso.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "P-003",
      "impact": "high",
      "statement": "Timeout, cancelamento e 429 de fornecedor podem degradar o endpoint ou induzir repetição de chamadas pagas.",
      "prevention": "Usar CancellationToken ligado a RequestAborted, prazo configurável, sem retry automático após timeout, rate limit por usuário e tradução explícita de 429/Retry-After.",
      "recovery": "Retornar 429, 502, 503 ou 504 sem corpo do fornecedor; manter identificação se apenas o conhecimento opcional falhar.",
      "verification": "Unitários com handler falso para 429/timeout/cancelamento e integração com provider falso controlado.",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "P-004",
      "impact": "high",
      "statement": "Não há projeto de testes .NET nem ferramenta de mutação, embora o seam de segurança seja alto risco.",
      "prevention": "Adicionar somente projeto/harness de teste e ferramenta seletiva com versão fixada na primeira entrega, sem atualizar dependências existentes.",
      "recovery": "Se restore da ferramenta não estiver disponível, manter a execução bloqueada antes de declarar o plano concluído e registrar a indisponibilidade.",
      "verification": "dotnet test da solução e mutação seletiva apenas nos validators/orquestrador do fallback.",
      "destinations": ["docs/bianchini/changes/v1/STACK_RESEARCH.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    }
  ],
  "user_actions": [
    {
      "id": "U-001",
      "needed_by": "P01",
      "statement": "Autorizar atualização de origin e merge de origin/master em phase1-bianchini, sem rebase, antes da execução do código.",
      "can_continue_without": false,
      "fallback": "Aguardar rede/autorização; não executar código, merge, rebase, commit, push ou PR nesta condição.",
      "evidence_required": "Ref origin/master atualizado, diff revisado e resultado do merge autorizado registrado no ledger da execução.",
      "destinations": ["docs/bianchini/changes/v1/USER_ACTIONS.md", "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "U-002",
      "needed_by": "P01",
      "statement": "Fornecer PlantNet__ApiKey somente se desejar ativar ou executar o teste externo opt-in; Groq__ApiKey apenas se desejar habilitar enriquecimento real.",
      "can_continue_without": true,
      "fallback": "Providers e handlers falsos cobrem desenvolvimento, integração e regressão; o teste externo fica skipado.",
      "evidence_required": "Variável no ambiente/cofre do backend e execução manual explicitamente opt-in, sem valor registrado em arquivo ou log.",
      "destinations": ["docs/bianchini/changes/v1/USER_ACTIONS.md", "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    }
  ],
  "spikes": [
    {
      "id": "S-001",
      "status": "passed",
      "statement": "Cartografia e pesquisa confirmaram que o mobile nativo usa o cliente ScanPlant para JWT/API base, mas PhotoScreen ainda chama Plant.id/Groq diretamente; o backend tem JWT/controllers e não tem providers/testes.",
      "evidence": ".superpowers/bianchini/cartography/22bbe55e4b0e6d5bb222b5d76572ce07d7533057-2911045c093df8f8800d10546727af1285a2054e96cf43dd936e659d5545a0e4.md e STACK_RESEARCH.md.",
      "decision": "Planejar dois planos: seam de segurança/backend estrito e adaptação mobile dependente, sem tocar geolocalização, web ou PT-05.",
      "destinations": ["docs/bianchini/changes/v1/STACK_RESEARCH.md", "docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    }
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {
      "id": "SD-001",
      "source": "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md",
      "target": "docs/bianchini/current/specs/external-plant-fallback.md",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/external-plant-fallback.md", "docs/bianchini/changes/v1/plans/P01-backend-secure-fallback.md"]
    },
    {
      "id": "SD-002",
      "source": "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md",
      "target": "docs/bianchini/current/specs/mobile-identification-client.md",
      "destinations": ["docs/bianchini/changes/v1/specs/scanplant-fallback-change.md", "docs/bianchini/changes/v1/spec-deltas/mobile-identification-client.md", "docs/bianchini/changes/v1/plans/P02-mobile-consented-client.md"]
    }
  ]
}
