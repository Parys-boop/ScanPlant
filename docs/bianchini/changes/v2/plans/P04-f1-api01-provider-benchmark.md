# P04 — F1-API01: benchmark pequeno e decisão de provedores

Proposta, não autorização de execução. Único plano novo; P01/P03-R6 continuam blocked-terminal e P02 completed. Sem revisão de mutação ou mudança de produto. Risco medium, assurance standard; policy documentation: slice/per_slice, mutation not_required, seam provider-benchmark-evidence round 0, breaker false, máximo 3 fix rounds documentais. Esse seam é distinto de external-fallback/mutation-observability e não renomeia nem zera seus breakers.

### Tarefa 1 — Decisão de provedores sustentada por comparação piloto

**Execution:** slice

**Review:** per_slice

**Change:** documentation

**Readiness refs:** D-101, D-102, D-103, A-101, A-102, P-101, P-102, P-103, U-101, S-101, SD-101

**Test seams:** provider-benchmark-evidence; corpus-to-observations; no seam de código modificado.

**Spec refs:** docs/bianchini/changes/v2/specs/post-u009-continuity.md#protocolo-mínimo-de-comparação, docs/bianchini/changes/v2/specs/post-u009-continuity.md#artefatos-métricas-e-aceite, docs/bianchini/changes/v2/specs/post-u009-continuity.md#garantia-proporcional-e-reutilização, docs/bianchini/changes/v2/specs/post-u009-continuity.md#lição-de-isolamento--restrição-para-qualquer-proposta-futura, docs/bianchini/changes/v2/spec-deltas/provider-benchmark-decision.md

**Files:** `docs/phase1/F1-API01-benchmark-decision.md`, arquivos sanitizados `artifacts/bianchini/v2/evidence/P04-f1-api01/{corpus-manifest.json,observations.json,terms-and-authorization.md,SHA256SUMS}`, ledger append-only `artifacts/bianchini/v2/ledgers/P04.md`; somente atualização factual mínima de `docs/living/PROJECT_STATE.md` no gate. Não escrever código, cache, imagem pessoal, resposta bruta sensível ou arquivo aprovado R6.

**Contract:** após aprovação/commit do pacote em rodada própria e admissão regular do workspace, organizar o protocolo e confirmar pré-condições funcionais pelas evidências intactas. Antes de transmissão, exigir U-101: corpus autorizado, referência revisada, condições oficiais atuais, credenciais no executor backend-side, custo zero e teto de chamadas. Comparar 7 casos fixos entre Pl@ntNet/Plant.id, uma chamada por caso/provider, concorrência 1, timeout 20 segundos, sem retry; registrar métodos/versões e observações sanitizadas. No máximo 14 chamadas de identificação, mais 4 textuais somente se a necessidade Groq/Gemini for justificada antes. Sem consentimento/credencial/condição válida, preparar apenas protocolo e parar com coleta not_run; não fabricar comparação ou instalar runner. Calcular/revisar métricas e escolher principal/secundário com limites claros. Comparação é evidência documental: não cria integração, altera provider de produção, usa isolamento ou faz campanha. Se não for possível escolher com evidência suficiente, manter o marco incompleto e registrar impedimento objetivo.

**Verification:** comandos futuros, cwd raiz: `python3 -m json.tool artifacts/bianchini/v2/evidence/P04-f1-api01/corpus-manifest.json` e `python3 -m json.tool artifacts/bianchini/v2/evidence/P04-f1-api01/observations.json`, exit 0; cwd do diretório de evidence P04: `sha256sum -c --strict SHA256SUMS`, todas entradas OK; raiz: `git diff --check`, exit 0. Revisão documental da mesma slice reconcilia IDs/contagem sem duplicação, fontes/autorização, elegibilidade, limites, denominadores e recalcula métricas a partir das observações; varredura de segredos sem imprimir valores. Não executar esses comandos sobre resultados inexistentes nem confundir parser com prova de medição real. Nesta rodada executam-se apenas checkers do pacote de planejamento.

**Done when:** há decisão principal/secundário fundamentada na evidência comparável e nos critérios oficiais, limites e custos explícitos, sem segredos; ou o limite externo é registrado como bloqueio, sem declarar conclusão. Somente o primeiro caso completa P04/F1-API01 após revisão. P01/P03 permanecem blocked-terminal, release pending, campaign_count=2 e score U-009 indisponível. Nenhuma nova campanha, alteração funcional, reabertura de marco ou entrega final decorre deste gate.
