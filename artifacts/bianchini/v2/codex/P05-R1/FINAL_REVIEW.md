# Revisão humana dos bytes finais — P05-R1 / U-201

Status: pending. Nenhum aceite de bytes finais atribuído ao responsável.

## Commit local de aprovação

`c7012b942c36fe93fb136a376a1a73093f1e5aaa` — chore(p05-r1): approve alias quarantine plan.
Árvore limpa após commit; 14 arquivos de planejamento/aprovação, nenhum de implementação:

- `artifacts/bianchini/v2/approval/manifest-p05-r1.sha256`
- `artifacts/bianchini/v2/ledgers/P05.md`
- `artifacts/bianchini/v2/planning/checker-p05-r1.jsonl`
- `artifacts/bianchini/v2/planning/p05-r1-policy.json`
- `artifacts/bianchini/v2/planning/p05-r1-preflight.json`
- `docs/bianchini/changes/v2/PLANNING_REVIEW-p05-r1.md`
- `docs/bianchini/changes/v2/READINESS-p05-r1.md`
- `docs/bianchini/changes/v2/STACK_RESEARCH-p05-r1.md`
- `docs/bianchini/changes/v2/USER_ACTIONS-p05-r1.md`
- `docs/bianchini/changes/v2/inputs/p05-r1/APPROVED_SCOPE.md`
- `docs/bianchini/changes/v2/plans/P05-R1-authorless-alias-quarantine.md`
- `docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md`
- `docs/bianchini/changes/v2/specs/offline-alias-quarantine-change.md`
- `docs/living/PROJECT_STATE.md`

## Resultado para aceite

- Manifesto 1.1.0, schema/normalização 1, roster byte a byte preservado.
- Quatro homônimos quarantined: Aloe maculata, Aloe variegata, Ficus clusiifolia e Ficus cordata.
- Cada um retorna None/null, inclusive caixa/whitespace normalizados; reinserção é rejeitada.
- Evidência mantém autoria relacionada, autoria/táxon conflitantes, fontes, motivo e estado.
- Igualdade de conjuntos/mapeamentos: 83 preliminares menos quatro = 79 aliases; 12 canônicos;
  91 chaves únicas, 14 classes na mesma ordem, proteções fora do namespace científico.
- Nomes comuns, IDs, índices, definições e demais aliases preservados.
- 94/94 testes passaram; 81 anteriores preservados, 13 novos, zero skips. CLI e 7/7 checksums OK.
- Python 3.14.4 -B; diferença histórica 3.12.3 registrada, sem alterar contrato.
- Fontes taxonômicas reutilizadas de 2026-09-11; nenhuma consulta nova.

## Hashes dos sete artefatos

| Arquivo | SHA-256 |
|---|---|
| `artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json` | `350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b` |
| `artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md` | `272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23` |
| `artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json` | `f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee` |
| `docs/phase1/F1-MAN01-offline-class-manifest.md` | `adcb2b45ab76684a5a6ab1110137ee7b67f8c313a4506bbaadc78fd6b0300c24` |
| `docs/phase1/offline-class-manifest.v1.json` | `bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c` |
| `scripts/phase1/test_offline_manifest.py` | `88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe` |
| `scripts/phase1/validate_offline_manifest.py` | `d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed` |

SHA-256 do arquivo SHA256SUMS: `9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e`.
Ele fixa conjuntamente os sete artefatos; verificação reproduzível na raiz:

```bash
sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
```

## Limites e estados

Pacotes históricos preservados: P05
`246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5`;
P05-R1 `6c046775fcb4422b792202e7a3d2eb77dacf5123a75ad9b87363d7597e3a025f`.
A regra contratual está na spec/delta P05-R1 congelados. Sincronização de current/specs
somente no encerramento regular do ciclo conforme o plano, sem release/homologação agora.

Uma rodada de correção, zero redesigns. Sidecar
`artifacts/bianchini/v2/codex/convergence/P05-R1/T1.json` permanece fixing:
B1 corrigido na working tree e formalmente aberto no baseline até prova do commit autorizado.
Sem nova classificação stopped, sem aprovação de convergência simulada e sem replanejamento.

P05 blocked; P05-R1 in_progress; U-201 aguardando aceite humano dos bytes. P01/P03-R6
blocked-terminal, P02/P04 completed e release pending preservados. Implementação unstaged,
sem commit de implementação, push, merge, providers ou alterações no worktree antigo/backup.

## Decisão solicitada no único gate final

Aceite humano dos bytes identificados por estes hashes e autorização de commit e push.
Registrar a resposta por append; não editar retrospectivamente este pacote de bytes.
