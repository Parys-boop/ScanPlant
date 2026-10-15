# P08 — recuperação limitada

A entrega técnica está publicada em `bm/v2-p08`, commit `19b019135d9d60f47df42939317b8e208c221ce2`, após aceite dos bytes e autorização Git. E2 e depois E1 foram integradas à quarentena, preservando os quatro hashes de original/sanitizada, origem, autoria, licenças, atribuição e avaliações humanas já fornecidas. Os outros 1.086 registros permanecem preservados e sem parecer humano. P06/P07 continuam somente de leitura e o plano aprovado permanece congelado.

O resultado de dados permanece `pending_human_acceptance`: 1.088 candidatos, duas imagens transferidas/importadas localmente e em `needs_human_review`, um registro em `needs_botanical_review` e 1.085 em `needs_license_review`; zero aprovadas e `usable=0`. A projeção pública `artifacts/phase1/p08/summary.json` corresponde ao resumo canônico privado. Partição, treinamento, publicação das imagens e release continuam sem liberação; a publicação autorizada de código/documentação não concede esses usos. P08 permanece `blocked`, sem iniciar P09.

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

Commons consulta apenas nomes científicos canônicos. A decisão humana real permite somente o uso privado de E2/E1 e dos registros necessários para quarentena e avaliação, nos termos documentados no dossiê. A decisão individual/adicional é separada dos metadados históricos `database_rights`, que permanecem pendentes; não há aprovação jurídica global. Preservam-se os avisos e a distinção entre a licença das fotografias e a dos textos/metadados da página. Os demais candidatos não recebem essa autorização. Licença individual, autoria, URL legal, proveniência e direitos adicionais são gates separados. iNaturalist permanece `no_crosswalk`: não houve consulta, ID inventado ou transferência. Esta atualização documental não autoriza descoberta, coleta ou novas transferências.

Sem prova de direitos, o candidato fica `needs_license_review`, sem original nem sanitizado. Hashes ausentes têm motivo explícito no pacote privado. Proteções permanecem vazias e sem consultas. Zero utilizável e classes vazias não demonstram suficiência para treinamento.

## Integridade e revisão

Journal canônico encadeado por SHA-256, intenção e reservas antes de rede, lock exclusivo, quotas cumulativas e persistência com fsync protegem a retomada. Corrupção/linha truncada bloqueia; não reparar ou truncar automaticamente. Originais e sanitizados são objetos separados e imutáveis. Comparação de hashes/dHash com as 17 imagens P07 é obrigatória; sinais perceptuais não constituem decisão humana.

O pacote externo `human-review.json` / `human-review.html` reúne IDs, fonte, autoria/licença/atribuição declaradas, hashes ou razão de ausência, classes propostas, taxonomia, qualidade, privacidade, duplicidade, recomendação técnica e decisões pendentes. Nenhuma imagem é aprovada por título, research grade ou ausência de EXIF.

## Verificação e limites de conclusão

Evidências desta continuação estão em `artifacts/bianchini/v2/codex/P08/`: inventário recuperado, RED recuperado, regressão, mutação seletiva e relatório de continuação. O checkpoint original permanece intacto.

A validação técnica das correções e do importador ocorreu por exceção de procedimento expressamente autorizada, distinta da aprovação formal do guard. Os 36 testes específicos, 287 afetados, cinco mutantes eliminados e revisão independente sem findings abertos são evidências existentes, vinculadas por fingerprints aos blobs publicados; ver `artifacts/bianchini/v2/codex/P08/local-import/` e a mensagem do commit. Não foram repetidos nesta atualização. O sidecar P08 e suas provas históricas permanecem intactos: B1 resolvido na rodada 1, gate humano histórico reprovado e nenhuma conclusão formal do P08.

As observações visuais existentes são parciais e conservam seus limites e vínculos aos hashes, sem solicitar nova conferência das mesmas imagens. Identidade botânica, duplicidade e dimensões não avaliadas continuam pendentes; não se acrescentaram pareceres aos outros 1.086 registros. O manifesto privado atual foi conferido contra os 156 arquivos resultantes, excluindo apenas o lock operacional, e será reutilizado para proposta de aceite limitado. Manifestos, recibos e checkpoints anteriores permanecem históricos. Esse aceite ainda não foi concedido, não substitui U-803 nem satisfaz sozinho o fechamento U-804/P08. Staging/commit/push desta atualização exclusivamente documental aguardam autorização própria.

## Importação local delimitada por autorização humana

`import-local --output <diretório-privado-p08-existente> --job <manifesto-privado.json>`
importa no máximo dois pares já existentes, sem rede, sem modo offline fictício e
sem gerar outra sanitizada. O comando não executa descoberta, finalize ou approve.
A configuração histórica permanece intacta. URLs de mídia com os três parâmetros
UTM comprovados podem ser referências de evidência local; a validação e a allowlist
dos destinos de rede permanecem inalteradas. O valor recebido não é reescrito.

O job privado usa `schema_version: 1`, `scope: p08_local_quarantine_import`,
`config_sha256`, `asset_root`, referências `{path, sha256}` para `authorization`,
`rights_review`, `acquisition`, `notices`, e uma lista `items` ordenada. Cada item
identifica `candidate_id`, `subject_digest`, `source_evidence_sha256`, os pares
`original`/`sanitized`, a prova `validation` e as referências `observations`.
Arquivos e diretórios de entrada devem pertencer ao usuário e ter modos 0600/0700;
não são aceitos symlinks, escapes, hashes divergentes ou destinos imutáveis em conflito.

A autorização humana vincula exatamente os IDs, subjects e hashes dos dois pares.
O documento separado de direitos conserva o escopo `commons_candidate_rights` e
as decisões reais individuais/adicionais. Não se interpreta observação visual
como decisão de direitos, botânica, privacidade, duplicidade ou treinamento.
Observações com hash explícito devem corresponder à sanitizada; as preliminares
sem hash conservam essa limitação no documento original, sem promoção de escopo.

Todo o lote e seus orçamentos são pré-validados antes do primeiro evento. Um
`local_import_plan` precede as cópias; evidências são content-addressed; checkpoints
`intention`, `received` e `committed` permitem retomada sem duplicar reservas.
A reserva de armazenamento considera apenas arquivos, eventos e crescimento de
projeções ainda faltantes, inclusive após uma queda. Os pares são copiados
integralmente, sem chamar o sanitizador. Os registros permanecem em revisão humana.

`local_acquisition_account` contabiliza os recibos reais da obtenção externa,
deduplicados por instante/URL/status. Exige recibo de sucesso para cada original;
respostas de mídia sem tamanho comprovado debitam conservadoramente o teto por
arquivo. Consultas de metadados sem recibo completo exigem evidência preservada e
contagem conservadora, sem inventar status ou horário. Essas contas também são
somadas aos limites de requisições/bytes/hora nas futuras chamadas do transporte.
A cópia local não produz requisição ou resposta HTTP fictícia.

Nova evidência altera os digests dos registros e invalida inspeções/decisões e
aceites dependentes. Manifestos anteriores permanecem históricos; uma nova
fotografia operacional dos bytes não é aceite U-804. O backup verificado precede
qualquer alteração canônica. As revisões e gates por exceção de procedimento são
registros técnicos separados, sem modificar ou representar aprovação do guard.
