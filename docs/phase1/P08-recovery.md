# P08 — recuperação limitada

A rodada permanece `pending_human_acceptance`, com `usable=0`. P06/P07 são entradas somente de leitura; nenhuma partição, treino, publicação ou release é autorizada. O plano aprovado permanece congelado.

## Operação

Usar o ambiente Python 3.14.4/Pillow 12.3.0 já aprovado. Definir `P08_PY`, `P08_ROOT` e `P07_SOURCE` para os caminhos privados do recibo externo; nunca versionar dados, configuração privada, decisões, imagens ou HTML.

```bash
"$P08_PY" -B scripts/phase1/recover_p08.py acquire --config "$P08_ROOT/config.json" --output "$P08_ROOT"
"$P08_PY" -B scripts/phase1/recover_p08.py inspect --output "$P08_ROOT" --p07-source "$P07_SOURCE"
"$P08_PY" -B scripts/phase1/recover_p08.py verify --output "$P08_ROOT" --p07-source "$P07_SOURCE"
```

O arquivo de configuração é imutável por fingerprint. A primeira configuração é produzida pela função `default_config()` e arquivada pelo journal. `acquire` retoma páginas duráveis; uma repetição sem trabalho pendente não baixa nem reescreve arquivos. Código 0 representa rodada limitada contabilizada; 1 indica fonte indisponível; 2 indica configuração, schema, hash ou IO inválido. Esses códigos não representam aceite humano.

`finalize --decisions` só consome pareceres humanos reais. `verify --acceptance` exige recibo humano vinculado ao SHA-256 do manifesto final e à cobertura exata dos arquivos, excluindo o próprio recibo. Não executar esses modos com decisões preenchidas pelo agente.

## Autoridade e fontes

Commons consulta apenas nomes científicos canônicos. A rodada atual permite descoberta de metadados e mantém o exame de direitos adicional pendente; nenhum campo `passed` de aprovação jurídica foi inventado. Licença individual, autoria, URL legal, proveniência e direitos adicionais são gates separados. iNaturalist permanece `no_crosswalk`: não houve consulta, ID inventado ou transferência. Seu adaptador continua coberto por testes sintéticos.

Sem prova de direitos, o candidato fica `needs_license_review`, sem original nem sanitizado. Hashes ausentes têm motivo explícito no pacote privado. Proteções permanecem vazias e sem consultas. Zero utilizável e classes vazias não demonstram suficiência para treinamento.

## Integridade e revisão

Journal canônico encadeado por SHA-256, intenção e reservas antes de rede, lock exclusivo, quotas cumulativas e persistência com fsync protegem a retomada. Corrupção/linha truncada bloqueia; não reparar ou truncar automaticamente. Originais e sanitizados são objetos separados e imutáveis. Comparação de hashes/dHash com as 17 imagens P07 é obrigatória; sinais perceptuais não constituem decisão humana.

O pacote externo `human-review.json` / `human-review.html` reúne IDs, fonte, autoria/licença/atribuição declaradas, hashes ou razão de ausência, classes propostas, taxonomia, qualidade, privacidade, duplicidade, recomendação técnica e decisões pendentes. Nenhuma imagem é aprovada por título, research grade ou ausência de EXIF.

## Verificação e limites de conclusão

Evidências desta continuação estão em `artifacts/bianchini/v2/codex/P08/`: inventário recuperado, RED recuperado, regressão, mutação seletiva e relatório de continuação. O checkpoint original permanece intacto.

O guard opera commits e cria checkout isolado para `proof`. Esta rodada proíbe novos commits e worktrees; não se representa código untracked como prova do HEAD. Sem sidecar P08, sem `freeze` ou `complete` fictício. As provas locais estão vinculadas aos hashes dos arquivos. Aceite humano dos candidatos e bytes finais, conclusão formal do guard e autorização de staging/commit/push permanecem pendentes.
