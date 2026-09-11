# P05 — F1-MAN01: manifesto canônico das 12 espécies e duas proteções

Único plano novo do ciclo v2. P01/P03-R6 blocked-terminal, P02/P04 completed; release pending. Proposta aguarda aprovação do digest e U-201. Sem código de produto, credenciais, provider, dataset, treinamento ou mutação.

Risco operacional low: artefato e validador documental reversíveis, sem consumidores ativos. Perfil standard preservado. Policy parser: grouped/plan_gate, mutation not_required, máximo 3 fix rounds no seam offline-manifest-contract, contador inicial 0 e breaker false; não afeta seams históricos. Design não requerido.

### Tarefa 1 — Manifesto completo, rastreável, validado e aceito

**Execution:** grouped

**Review:** plan_gate

**Change:** parser

**Readiness refs:** D-201, D-202, D-203, A-201, A-202, P-201, P-202, P-203, U-201, SD-201

**Test seams:** offline-manifest-contract; normalize_name; resolve_scientific_name; CLI documental e associação 1:1 roster/classes.

**Spec refs:** docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#entrada-humana-e-pesquisa-taxonômica, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#formato-e-entidades, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#normalização-e-comparação, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#semântica-das-proteções-e-compatibilidade, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#validador-e-critérios-objetivos, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#evidências-e-revisão-humana, docs/bianchini/changes/v2/specs/offline-class-manifest-change.md#gates-e-encerramento-do-plano, docs/bianchini/changes/v2/spec-deltas/offline-class-manifest.md

**Files:** criar na execução `docs/phase1/offline-class-manifest.v1.json`, `docs/phase1/F1-MAN01-offline-class-manifest.md`, `scripts/phase1/validate_offline_manifest.py`, `scripts/phase1/test_offline_manifest.py` e `artifacts/bianchini/v2/evidence/P05-f1-man01/{approved-species-roster.json,taxonomy-review.md,validation-report.json,SHA256SUMS}`; append somente em `artifacts/bianchini/v2/ledgers/P05.md`; atualização factual mínima de `docs/living/PROJECT_STATE.md` no gate. Não editar current/specs, planos/manifestos/ledgers anteriores ou aplicações.

**Contract:** U-201 é pré-condição de população: receber 12 táxons distintos do escopo já aprovado, registrar evidência sanitizada e congelar roster; não inventar sete ausentes nem incluir o controle Bellis perennis. Consulta textual oficial complementa somente nomes/aliases sem prova suficiente, sem imagens, API de identificação ou autenticação. Entregar, na mesma unidade, JSON 1.0.0 de 12 species + 2 protection, mapa estável species_01–species_12/outra_planta/imagem_invalida, índices 0–13, nomes científicos/comuns, aliases referenciados, normalização exata, documentos, CLI Python stdlib e suíte negativa/positiva. Só o responsável resolve escopo ambíguo e aceita os bytes finais. Falta de entrada/fonte/revisão mantém a unidade incompleta; não criar segundo plano ou reduzir escopo.

**Verification:** futuros comandos, cwd raiz do workspace v2 aprovado: `python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'` (exit 0; casos positivos/negativos da spec); `python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json` (exit 0; 12 species, 2 protection, 14 classes); `python3 -B -m json.tool artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json` (exit 0); `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS` (7/7 entradas OK, paths relativos à raiz); `git diff --check` (exit 0). O validador faz parse estrito também do roster. Revisar whitespace dos untracked e varrer segredos sem valores. Registrar comandos/exit codes e hashes; U-201 confere 12/12 táxons/fontes, cada alias, nomes comuns, IDs/ordem/proteções e aprova os hashes finais no gate único. Esses comandos referem-se a arquivos contratados a criar, não executados no planejamento.

**Done when:** todas as regras de schema/identidade/normalização e regressões documentais passam; fontes taxonômicas têm proveniência/data real e nenhuma espécie extra; roster e manifesto 1:1, 12+2 e ordem aceitos pelo responsável; evidência sanitizada e checksums conferem; alterações confinadas aos arquivos acima. Só então completar P05, preservar estados anteriores e release pending. A entrega documenta compatibilidade futura sem implementar treino, catálogo, modelo ou fluxo híbrido. Sem U-201 registrar fronteira e parar; sem instalações .NET/Android/DB e sem mutação. Execução posterior requer aprovação registrada, pacote commitado e workspace próprio; esta rodada para antes de execução/staging/commit/push.
