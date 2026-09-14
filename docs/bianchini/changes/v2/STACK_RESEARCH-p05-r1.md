# Stack Research — P05-R1

Research mode: repo_only
Motivo: alteração localizada de contrato documental existente; decisão humana e evidência
taxonômica de 2026-09-11 bastam, sem pesquisa em rede ou dependência nova.

## Stack detectada

Python stdlib, JSON, unittest, Git e CLI bm.py existente. Python observado nesta sessão:
3.14.4; o baseline registrou 3.12.3. Nenhum teste de implementação executado agora.
Usar stdlib compatível com o contrato Python 3.12; gates futuros devem registrar versão
real do interpretador, sem instalar ou alegar reprodução em 3.12 nesta sessão.

## Inventário local

- Manifests: `docs/phase1/offline-class-manifest.v1.json`, `artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`; schema 1, manifest_version 1.0.0, normalization_version 1.
- Lockfiles: nenhum requerido por este seam stdlib; lockfiles das aplicações não participam.
- CI: `.github/workflows/deploy.yml` histórico de produto; não acionado ou alterado.
- Testes: `scripts/phase1/test_offline_manifest.py`; unittest discover e CLI existentes no plano.
- Padrões locais: `scripts/phase1/validate_offline_manifest.py`, `artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md`, ledger P05 append-only,
  SHA256SUMS; manifesto P05 aprovado preservado. Não existe current/specs/offline-class-manifest.md.

## Decisões aplicadas

D-211: os quatro homônimos serão excluídos de synonyms resolvíveis e mantidos na evidência.
O mapa atual apenas detecta colisões internas; isso não prova ausência de homônimos externos.
Não foi feita consulta nova às URLs; a data factual das fontes continua 2026-09-11.
D-212: SemVer local exige minor por alteração de resolução: propor 1.1.0, schema/normalização 1.
D-213: P05-R1 fica no ciclo v2; P05 histórico e planos anteriores são base imutável.
O novo readiness projeta referências históricas para satisfazer o checker sem reabrir decisões;
SD-201 passa a apontar ao delta esperado P05-R1 apenas no novo readiness, com target inalterado.
O readiness histórico permanece intacto. Aprovação atual passa a pending; aprovação P05 é preservada
em prior_p05_approval, com referência ao estado do checkpoint.

Leitura localizada de um contrato sem consumidores ativos: não atravessa aplicações e não
exige cartografia artificial. Sem subagentes. Backup externo apenas inventariado; nenhum
arquivo interno importado nem necessário como fonte normativa.

## Riscos e lacunas

A-211: ausência de outros homônimos não é demonstrável por parser; revisão de cada alias
contra evidência oficial e fronteira U-201 continuam obrigatórias. Novo conflito bloqueia aceitação.
P-211: quarentena não revoga sinonímia nas fontes. P-212: usar conjuntos e não apenas 83-4.
P-213: testes/hash não dão aceite humano nem liberam release.

## Policy executada

Resultados integrais em `artifacts/bianchini/v2/planning/p05-r1-policy.json`. change-policy --public-contract-change:
material_change, invalidate_package_and_replan_affected_scope, plan_invalidating true,
plan_files_mutable false, reapproval_required true, extra_review_required true,
redesign_allowed true. Limite aplicado: só elegibilidade de aliases homônimos.

Policy da única unidade futura: parser, risk low, perfil standard, grouped/plan_gate,
mutation not_required, máximo 3 fix rounds no mesmo seam offline-manifest-contract,
rodada 0, breaker false. Ledger histórico registra nenhuma rodada formal consumida nesse seam;
não reiniciar contadores P01/P03. Risco operacional local/reversível, sem consumidor ativo,
igual à classificação histórica; material_change descreve invalidade contratual, não eleva
automaticamente risco operacional. Revisão semântica adicional é esta planning review P05-R1;
revisão de execução e aceite humano ficam no gate futuro.
