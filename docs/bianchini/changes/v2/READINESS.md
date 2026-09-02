```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "c0a63881870ee18a0d70b47dee02d33a0084d9ef58a64a2ff8b8a6a747520363",
  "repository_revision": "2b79620fffd1c21e679889434663a8728436053b",
  "design_required": false,
  "impact_map": {
    "applications": ["ScanPlantAPI"],
    "modules": ["local-tool launcher", "MutationHarness", "external-fallback evidence"],
    "contracts": ["P03 mutation-evidence execution contract", "Git revision binding"],
    "data": ["ephemeral resolver cache and evidence only"],
    "platforms": ["ASP.NET Core .NET 8"]
  },
  "decisions": [
    {"id":"D-001","statement":"P01 permanece blocked-terminal; P02 permanece completed e não depende de novo gate P03.","evidence":"artifacts/bianchini/v2/ledgers/P01.md e artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"D-002","statement":"O contrato móvel já concluído não é reaberto por este replanejamento ambiental.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"D-004","statement":"P03-R2 é a revisão formal exclusiva de P03; o launcher real deve ser provado não mutacionalmente antes de uma nova campanha humana única.","evidence":"artifacts/bianchini/v2/evidence/P03-p01-mutation/execution-summary.json","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]}
  ],
  "assumptions": [
    {"id":"A-001","impact":"high","status":"confirmed","statement":"Os contratos funcionais P01/P02 aceitos permanecem registrados e não são alterados pelo gate ambiental.","evidence":"artifacts/bianchini/v2/ledgers/P01.md e artifacts/bianchini/v2/ledgers/P02.md","fallback":"manter o status atual se o escopo tentar reabrir produto ou mobile","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"A-003","impact":"critical","status":"bounded","statement":"O pacote local dotnet-stryker 4.16.0 já disponível pode materializar o resolver no DOTNET_CLI_HOME final sem rede.","evidence":".config/dotnet-tools.json, evidência P03-R1 e pesquisa targeted_web","fallback":"parar antes da campanha; não baixar, instalar, atualizar ou trocar ferramenta","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]}
  ],
  "pitfalls": [
    {"id":"P-001","impact":"critical","statement":"P02 não pode inferir aprovação de P01 nem ser reaberto por P03-R2.","prevention":"preservar P02 completed e limitar P03-R2 ao launcher/evidence","recovery":"manter P01 bloqueado e P02 completed","verification":"planning audit e ledger P02","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"P-002","impact":"high","statement":"A pendência de observabilidade não recebe waiver ou carry-forward.","prevention":"preservar P01 blocked-terminal até evidence verificável","recovery":"bloquear P01","verification":"ledger P01","destinations":["docs/bianchini/changes/v2/plans/P01-observability-followup.md"]},
    {"id":"P-003","impact":"critical","statement":"Evidence de mutação não pode ser vinculada ao HEAD de elaboração quando o checkpoint aprovado cria um novo HEAD.","prevention":"comparar revision, expected_revision e HEAD executável imediatamente antes da campanha e no verifier","recovery":"parar antes da campanha ou bloquear depois sem retry","verification":"mutation-evidence verify","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]},
    {"id":"P-004","impact":"critical","statement":"Manifest/list/cache isolados não provam que o launcher resolve no DOTNET_CLI_HOME sanitizado final; este foi o defeito de P03-R1.","prevention":"restore offline no CLI home final e invocação real --help com banner, PID e exit 0","recovery":"parar com campaign_count=0 e preservar diagnóstico","verification":"transcript do launcher, lifecycle, exit code e ausência de relatório","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]},
    {"id":"P-005","impact":"high","statement":"Confundir launcher preflight, MutationHarness preflight e campanha pode consumir autorização indevidamente.","prevention":"contadores e fases separados; somente a Tarefa 2 muda campaign_count para 1","recovery":"parar antes da Tarefa 2 se qualquer preflight falhar","verification":"evidence com fases, contadores e comandos separados","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]}
  ],
  "user_actions": [
    {"id":"U-001","needed_by":"P02","statement":"Aprovação histórica do pacote P02 permanece registrada e não cria autorização nova.","fallback":"manter P02 completed e não reabrir escopo","destinations":["docs/bianchini/changes/v2/USER_ACTIONS.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"can_continue_without":false,"evidence_required":"registro histórico de aprovação P02"},
    {"id":"U-004","needed_by":"P03","statement":"Aprovar o pacote P03-R2 para os preflights e, depois de eles passarem, autorizar explicitamente uma única campanha contra o HEAD executável.","fallback":"não executar preflight/campanha ou manter P01/P03-R2 bloqueados","destinations":["docs/bianchini/changes/v2/USER_ACTIONS.md","docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"],"can_continue_without":false,"evidence_required":"aprovação do digest P03-R2 e autorização posterior 1/1 com HEAD atual"}
  ],
  "spikes": [
    {"id":"S-001","status":"passed","statement":"P02 é tecnicamente independente do encerramento da observabilidade de P01.","evidence":"artifacts/bianchini/v2/ledgers/P02.md","destinations":["docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"],"decision":"Preservar P02 completed."},
    {"id":"S-002","status":"passed","statement":"Pesquisa oficial e precedente v3 confirmam que dotnet tool run aceita o tool local e que --help não precisa de projeto/configuração de mutação.","evidence":"docs/bianchini/changes/v2/STACK_RESEARCH.md e artifacts/bianchini/v2/evidence/P01-manual-final-v3/launcher-command.txt","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"],"decision":"Usar --help como prova de início real, com banner/lifecycle/exit e sem argumentos mutacionais."}
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {"id":"SD-001","statement":"Pré-condições técnicas históricas de P02 e bloqueio P01 permanecem separados.","source":"docs/bianchini/changes/v2/spec-deltas/replan-v2.md","target":"docs/bianchini/current/specs/replan-v2.md","destinations":["docs/bianchini/changes/v2/spec-deltas/replan-v2.md","docs/bianchini/changes/v2/plans/P01-observability-followup.md","docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"]},
    {"id":"SD-002","statement":"A próxima spec aceita deve exigir preflight real do launcher no ambiente final antes de campanha seletiva.","source":"docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","target":"docs/bianchini/current/specs/mutation-launcher-gate.md","destinations":["docs/bianchini/changes/v2/specs/replan-v2.md","docs/bianchini/changes/v2/spec-deltas/mutation-launcher-gate.md","docs/bianchini/changes/v2/plans/P03-p01-mutation-evidence-r2.md"]}
  ]
}
```
