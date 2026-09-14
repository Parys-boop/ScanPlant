# Task Brief 1

- Plan: `docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md`
- Plan SHA-256: `625164b23b6cab84ec1512c95987cb4f74936374c49fd4b9f9b35c1a46e3b666`
- Kind: `task`
- Group ID: `n/a`
- Group SHA-256: `7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6`
- Unit `1` SHA-256: `7ac3a29767795b689ea7490c284141935deb0b2424b9297aaee7e4c7ae20cab6`

### Tarefa 1 — Mapa inequívoco, quarentena rastreável e bytes finais aceitos

**Execution:** grouped

**Review:** plan_gate

**Change:** parser

**Readiness refs:** D-211, D-212, D-213, A-211, P-211, P-212, P-213, U-201, SD-201

**Test seams:** normalize_name; scientific_map; resolve_scientific_name; validate_manifest;
CLI documental; associação de aliases/canônicos por class_id e roster.

**Spec refs:** docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#regra-pública-e-estados,
docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#invariantes-e-contagem,
docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#versionamento-e-arquitetura,
docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md#verificação-e-aceite,
docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#formato-e-identidade,
docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#referências-e-elegibilidade,
docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#quarentena-e-resolução,
docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#versão-e-compatibilidade,
docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md#verificação-evidência-e-aceite.

**Files:** alterar futuramente docs/phase1/offline-class-manifest.v1.json,
scripts/phase1/validate_offline_manifest.py, scripts/phase1/test_offline_manifest.py,
docs/phase1/F1-MAN01-offline-class-manifest.md,
artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md,
artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json,
artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS;
append artifacts/bianchini/v2/ledgers/P05.md e atualizar docs/living/PROJECT_STATE.md
somente por fatos. Roster approved-species-roster.json é entrada imutável, sem edição.
Nenhum arquivo acima é alterado nesta rodada de planejamento, exceto append de planejamento
no ledger e estado. Planos/specs/manifestações de aprovação históricas e current/specs preservados.

**Contract:** depois de aprovação explícita do pacote, autorização separada de execução,
pacote commitado e workspace v2 válido, remover somente Aloe maculata, Aloe variegata,
Ficus clusiifolia e Ficus cordata de synonyms e do mapa científico, retornar None para
essas entradas normalizadas no manifesto válido e rejeitar reintrodução no mapa/validação.
Manter registros quarantined com autoria associada, autoria conflitante, identidade,
fontes, motivo e vínculo U-201, preservando sinonímia da fonte. Não acrescentar autoria
às chaves ou remover autoria recebida. Novo homônimo bloqueia aceitação até revisão explícita.
Implementar proposta minor 1.1.0, schema/normalização 1. Preservar integralmente os 12
canônicos, nomes comuns, IDs/ordem/índices/proteções e roster. Baseline para comparação:
manifesto do commit 77e93a221dad3115c301b10317b626c236a3ba84, SHA-256
39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5.
Não alterar nenhuma outra regra de elegibilidade já aprovada ou retirar alias elegível.

**Verification:** cwd raiz de workspace v2 válido, Python stdlib e Git já disponíveis;
registrar `python3 --version`. No gate fast executar
`python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'`
e `python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`.
Ambos exit 0; CLI deve reportar 12 species, 2 protection, 14 classes, versão 1.1.0
e hashes corretos. Testes antes/depois da correção devem tornar visível a falha original
dos quatro nomes, preservando regressões. No gate plan, executar a mesma suíte e CLI
após últimas alterações, `python3 -B -m json.tool artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json`,
`sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS` (7/7),
`git diff --check`, parse JSON estrito do relatório/manifesto/roster (sem chaves duplicadas,
NaN/Infinity/números não finitos), UTF-8/LF/newline, paths, segredos e revisão humana.
Usar strict_load já existente também no teste do relatório; json.tool isolado não prova
JSON estrito. Inspecionar diff completo e untracked. Não executar gates de produto/release.

Matriz obrigatória dentro da suíte documental e revisão da mesma unidade:

| Caso | Resultado exigido |
|---|---|
| 12 canônicos + todos os aliases não ambíguos | class_id esperado, sem alteração |
| Quatro Q, cada um e variantes de caixa/whitespace Unicode | None; ausentes de scientific_map |
| Reinserir cada Q como alias em qualquer classe | rejeição explícita; nenhuma associação silenciosa |
| Autoria recebida e nomes comuns/proteções | sem remoção de autoria ou resolução indevida |
| Colisões normalizadas canônico/alias, intra/interclasse | erro de contrato |
| Conjuntos e mapeamentos por classe | A0 com 83; Q com 4; Afinal = A0 menos Q, sem adições/trocas |
| Contagem derivada | 79 aliases, 91 chaves com canônicos; Aloe 11→9, Ficus 12→10 |
| Roster, IDs, ordem, canônicos/comuns e definições | igualdade com baseline, hash roster preservado |
| Evidência de cada Q | quarantined, ambas autorias, identidade conflitante, fontes e motivo |
| Todos os demais aliases | fonte oficial e elegibilidade individual; novo conflito bloqueia |
| Versão/schema/normalização | 1.1.0 / 1 / 1 em manifesto, validator, testes, docs e relatório |

Prova de conjuntos deve ler baseline imutável pelo Git ou fixture derivada identificada
pelo hash acima; não gerar expectativa do próprio manifesto modificado. Reconciliar por
classe e conjunto normalizado, não só subtração numérica. Teste de reintrodução deve
adulterar dados em memória e observar falha, sem persistir mudança em manifesto real.
Fixtures 1.0.0 legadas não podem mascarar expectativa 1.1.0 no novo gate. Manter regressões
aplicáveis de JSON/Unicode, formatos, fontes, tipos, erros CLI e ausência de escrita/rede.

**Done when:** gates passam, alterações limitadas à regra e artefatos autorizados;
evidência e relatório reconciliam aliases e versão, sete hashes conferem, e responsável
aceita explicitamente bytes finais/hashes após revisão U-201. Sem esse aceite, P05-R1
e P05 não são completed e U-201 permanece aberta; decisão de política não dá aceite
de bytes. Registrar parecer real em append depois da selagem. Manter P01/P03-R6
blocked-terminal, P02/P04 completed, release pending. Não sincronizar current/specs,
fechar ciclo, instalar ferramentas ou realizar integração de produto, imagens, dataset,
treino, modelo, provider, credencial, .NET, npm, Android, Docker, banco ou Stryker.
Esta rodada encerra no pedido de aprovação do pacote, antes de staging/commit/push/implementação.
