```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "26b08b9714ffcc1a0dc3948d75c7bd28985e5986493f452b370a2cc5b70af832",
  "repository_revision": "80b7ca2bc93209301b9f69e88c727ec7f43cbffb",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlantAPI"],
    "modules": ["local-tool resolver", "Stryker launcher", "MutationHarness", "external-fallback evidence"],
    "contracts": ["P03-R3 composite launcher proof", "sanitized environment equality", "Git revision binding"],
    "data": ["ephemeral resolver cache and evidence only"],
    "platforms": ["ASP.NET Core .NET 8"]
  },
  "decisions": [
    {"id":"D-001","statement":"P01 permanece blocked-terminal e P02 completed; P03-R3 não reabre produto ou mobile.","evidence":"artifacts/bianchini/v2/ledgers/P01.md e artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"D-002","statement":"O contrato móvel concluído permanece separado deste replanejamento do launcher.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"D-005","statement":"P03-R3 substitui somente o gate de banner de P03-R2 por prova composta de identidade, resolução e não mutação.","evidence":"artifacts/bianchini/v2/evidence/P03-p01-mutation-r2/preflight-run-ZBwbUU/task-1-blocked.json e SHA256SUMS com digest cba24f19e17666608797375be8cea833f92d552ba286ee2ab8bfeadaf44c74b6","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]}
  ],
  "assumptions": [
    {"id":"A-001","impact":"high","status":"confirmed","statement":"Os contratos funcionais P01/P02 não são alterados pelo gate ambiental de P03-R3.","evidence":"ledgers P01 e P02","fallback":"manter P01 bloqueado e P02 completed se o escopo tentar alterar produto ou mobile","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"A-004","impact":"critical","status":"bounded","statement":"O pacote local dotnet-stryker 4.16.0 pode ser restaurado offline e resolvido no CLI home sanitizado final.","evidence":"P03-R2: manifest, restore exit 0, resolver cache e PathToExecutable para /home/arthur/.nuget/packages/dotnet-stryker/4.16.0/tools/net8.0/any/Stryker.CLI.dll","fallback":"parar antes da campanha; não baixar, instalar, atualizar ou trocar ferramenta","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]}
  ],
  "pitfalls": [
    {"id":"P-001","impact":"critical","statement":"P02 não pode inferir aprovação de P01 nem ser reaberto por P03-R3.","prevention":"preservar P02 completed e limitar P03-R3 ao launcher/evidence","recovery":"manter P01 bloqueado e P02 completed","verification":"planning audit e ledger P02","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"P-002","impact":"high","statement":"A pendência de observabilidade não recebe waiver ou carry-forward.","prevention":"preservar P01 blocked-terminal até evidence verificável","recovery":"bloquear P01","verification":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"P-003","impact":"critical","statement":"Evidence futura não pode ser vinculada ao HEAD de elaboração.","prevention":"comparar revision, expected_revision e HEAD executável antes da campanha e no verifier","recovery":"parar antes da campanha ou bloquear depois sem retry","verification":"mutation-evidence verify","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]},
    {"id":"P-005","impact":"high","statement":"Confundir launcher preflight, MutationHarness e campanha pode consumir autorização indevidamente.","prevention":"fases, lifecycle e contador separados; somente Tarefa 2 muda o contador","recovery":"parar antes da Tarefa 2 se qualquer preflight falhar","verification":"evidence com fases e campaign_count separados","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]},
    {"id":"P-006","impact":"critical","statement":"Banner de versão no stdout de --help não é prova garantida de versão nem de resolução.","prevention":"exigir sinais compostos de manifest, restore, resolver, alvo, hash aplicável e launcher real","recovery":"replanejar somente se a prova composta for impossibilitada; nunca forçar argumento mutacional","verification":"evidence estrutural e transcript do launcher","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]},
    {"id":"P-007","impact":"critical","statement":"Validar launcher em CLI home diferente do harness/campanha invalida a prova.","prevention":"um run-dir e manifesto com comparação material entre todas as fases","recovery":"parar com campaign_count=0","verification":"digests/manifestos de ambiente e cwd coincidentes","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]}
  ],
  "user_actions": [
    {"id":"U-001","needed_by":"P02","statement":"A aprovação histórica P02 é preservada e não cria autorização nova.","fallback":"manter P02 completed e não reabrir escopo","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r3.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"can_continue_without":false,"evidence_required":"registro histórico de aprovação P02"},
    {"id":"U-005","needed_by":"P03","statement":"Aprovar P03-R3 para os preflights e, somente depois de passarem, autorizar explicitamente uma campanha contra o HEAD executável.","fallback":"não executar preflight/campanha; manter P01/P03-R3 bloqueados","destinations":["docs/bianchini/changes/v2/USER_ACTIONS-p03-r3.md","docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"],"can_continue_without":false,"evidence_required":"aprovação do digest P03-R3 e autorização posterior 1/1 com HEAD executável"}
  ],
  "spikes": [
    {"id":"S-001","status":"passed","statement":"P02 é tecnicamente independente do encerramento de observabilidade P01.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"decision":"Preservar P02 completed."},
    {"id":"S-003","status":"passed","statement":"A evidence P03-R2 prova que --help é caminho real de launcher, mas não emite o banner de versão exigido por P03-R2.","evidence":"launcher-preflight stdout/lifecycle, resolver cache, tool restore e task-1-blocked.json em preflight-run-ZBwbUU","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"],"decision":"Separar identidade de versão da semântica de help e usar prova composta não mutacional."}
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {"id":"SD-001","statement":"P01/P02 preservam seus estados e contratos separados.","source":"docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md","target":"docs/bianchini/current/specs/replan-v2.md","destinations":["docs/bianchini/changes/v2/spec-deltas/replan-v2-p03-r3.md","docs/bianchini/changes/v2/plans/P01-observability-followup.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"SD-003","statement":"A próxima spec aceita exige gate composto de identidade/resolução/não mutação, sem banner de versão em --help.","source":"docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","target":"docs/bianchini/current/specs/mutation-launcher-gate.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2-p03-r3.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate-r3.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r3.md"]}
  ]
}
```
