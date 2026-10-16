# P08 — recuperação limitada

A entrega técnica está publicada em `bm/v2-p08`, commit `19b019135d9d60f47df42939317b8e208c221ce2`, após aceite dos bytes e autorização Git. E2 e depois E1 foram integradas à quarentena, preservando os quatro hashes de original/sanitizada, origem, autoria, licenças, atribuição e avaliações humanas já fornecidas. Naquela entrega, os outros 1.086 registros foram preservados sem parecer humano; as avaliações posteriores são descritas abaixo. P06/P07 continuam somente de leitura e o plano aprovado permanece congelado.

O lote posterior de 97 candidatos tem decisão humana real para aquisição privada, baseada na adoção do relatório documental do agente, sem alegação de inspeção pessoal das páginas ou garantia de titularidade. A retomada dos 20 adiados, após liberação da janela horária, obteve 19 sanitizadas e rejeitou um MPO com três quadros. No total do lote, há 90 sanitizadas novas e sete originais recusados por formato (seis MPO com dois quadros, um com três), todos preservados. Doze sanitizadas correspondem a duplicatas exatas por hash e foram rejeitadas tecnicamente, sem parecer humano de duplicidade. Não restam transferências adiadas. E1/E2 não foram baixadas ou avaliadas novamente.

O resultado canônico permanece `pending_human_acceptance`: 1.089 candidatos, 100 originais preservados e 93 sanitizadas, zero aprovadas e `usable=0`. A revisão anterior da galeria local, vinculada aos hashes do snapshot e das cópias exibidas, registrou oito rejeições por qualidade e aprovação de somente nitidez, iluminação e clareza do alvo vegetal em 68 imagens pendentes. O complemento posterior registrou as observações reais de privacidade e de ausência percebida de ilustração/montagem/microscopia/texto dominante nas cópias examinadas; o alcance de E2 foi confirmado expressamente. Não se inferem confirmação pericial, ausência total de pessoas, independência ou aprovação dos gates canônicos. Dois impedimentos anteriores e todas as rejeições permanecem; o texto de formulário não foi tratado como arquivo ou exceção de revisão.

Os estados atuais são 73 `needs_human_review`, oito `rejected_quality`, 12 `rejected_duplicate`, sete `rejected_format`, um `needs_botanical_review` e 988 `needs_license_review`. Os registros canônicos permanecem intactos; a avaliação da imagem mais recente foi registrada apenas no catálogo experimental, com vínculo ao hash da cópia exibida. As dez observações anteriores sobre páginas de origem permanecem históricas, sem serem convertidas retroativamente em revisão das sanitizadas. Nenhuma rejeição mudou as classes propostas ou gerou exemplo de classe de proteção. A projeção pública `artifacts/phase1/p08/summary.json` corresponde ao resumo canônico privado. Partição, treinamento, publicação das imagens e release continuam sem liberação. P08 permanece `blocked`, sem iniciar P09.

O responsável autorizou posteriormente o [critério de rotulagem provisória para
experimento privado](P08-experimental-private-criterion.md), substituindo somente
a confirmação botânica pericial nesse catálogo separado. O complemento visual e
o aceite delimitado consolidaram 21 imagens; o lote seguinte preservou essas 21 e
selecionou uma representante de Dracaena e uma de Ficus, totalizando 23 elegíveis
privadas. Os dois Ficus já obtidos têm declaração estruturada por arquivo, com
nome científico resolvido e referência Kew correspondente ao manifesto; apenas a
vista indicada foi selecionada, mantendo a possível relação de sessão com a
outra. A relação da série de Dracaena também permanece explícita, com uma única
representante. Dezoito outras referências de rótulo sustentado ficam reservadas.
Não se afirma independência nem se autoriza distribuição das relações entre
treino/teste. A avaliação visual real da nova Nephrolepis foi posteriormente
vinculada ao hash exato da única cópia exibida, sem confirmar identidade botânica.
Nome científico declarado, concessão BY 4.0 reconciliada com a conta autora,
integridade e verificações existentes continuam válidos. O catálogo consolidado
agora tem 24 elegíveis privadas e nenhuma imagem nova aguardando essa avaliação;
as 12 espécies estão representadas, com contagens 2/2/1/1/1/4/5/1/1/3/1/2 na ordem
do manifesto. As observações e os 23 registros experimentais anteriores foram
preservados; 18 outras referências continuam reservadas e 58 excluídas/impedidas.
A galeria de uma imagem é preservada como o snapshot examinado.
O suplemento preserva o resultado de sua primeira aplicação como histórico; os
catálogos e recibos posteriores permanecem privados. Nenhum estado canônico foi
promovido pelo catálogo e o gate pericial histórico não foi aprovado. A entrega do
recorte está consolidada; o aceite limitado dos bytes finais permanece proposto.
O manifesto privado final tem SHA-256
`6253fe5cd88db3adb1c9361d00e95207be329c5eef86d81885ceea4757b22fd1`.
Esse aceite não encerrará por inferência U-803/U-804 do plano original ou P08.

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

Commons consulta apenas nomes científicos canônicos. A decisão humana real permite somente o uso privado de E2/E1, dos 97 sujeitos delimitados no recibo privado e dos registros necessários para transferência, preservação, quarentena e avaliação. A decisão individual/adicional é separada dos metadados históricos `database_rights`, que permanecem pendentes; não há aprovação jurídica global do Commons. Preservam-se os avisos e a distinção entre a licença das fotografias e a dos textos/metadados da página. Os demais candidatos não recebem essa autorização. Licença individual, autoria, URL legal, proveniência e direitos adicionais são gates separados. iNaturalist permanece `no_crosswalk`: não houve consulta, ID inventado ou transferência. A retomada não expandiu o lote nem reiniciou descoberta.

Sem prova de direitos, o candidato fica `needs_license_review`, sem original nem sanitizado. Hashes ausentes têm motivo explícito no pacote privado. Proteções permanecem vazias e sem consultas. Zero utilizável e classes vazias não demonstram suficiência para treinamento.

## Integridade e revisão

Journal canônico encadeado por SHA-256, intenção e reservas antes de rede, lock exclusivo, quotas cumulativas e persistência com fsync protegem a retomada. Corrupção/linha truncada bloqueia; não reparar ou truncar automaticamente. Originais e sanitizados são objetos separados e imutáveis. Comparação de hashes/dHash com as 17 imagens P07 é obrigatória; sinais perceptuais não constituem decisão humana.

O pacote externo `human-review.json` / `human-review.html` reúne IDs, fonte, autoria/licença/atribuição declaradas, hashes ou razão de ausência, classes propostas, taxonomia, qualidade, privacidade, duplicidade, recomendação técnica e decisões pendentes. Nenhuma imagem é aprovada por título, research grade ou ausência de EXIF.

## Verificação e limites de conclusão

Evidências desta continuação estão em `artifacts/bianchini/v2/codex/P08/`: inventário recuperado, RED recuperado, regressão, mutação seletiva e relatório de continuação. O checkpoint original permanece intacto.

A validação técnica das correções e do importador ocorreu por exceção de procedimento expressamente autorizada, distinta da aprovação formal do guard. Os 36 testes específicos, 287 afetados, cinco mutantes eliminados e revisão independente sem findings abertos são evidências existentes, vinculadas por fingerprints aos blobs publicados; ver `artifacts/bianchini/v2/codex/P08/local-import/` e a mensagem do commit. Não foram repetidos nesta atualização. O sidecar P08 e suas provas históricas permanecem intactos: B1 resolvido na rodada 1, gate humano histórico reprovado e nenhuma conclusão formal do P08.

As observações visuais existentes de E1/E2 são parciais e conservam seus limites e vínculos, sem solicitar nova conferência. A revisão local posterior foi registrada separadamente para 76 cópias (oito rejeições e 68 aprovações restritas a três aspectos), preservando as dez observações de páginas e os dois impedimentos não reavaliados. Identidade botânica, privacidade, dimensões visuais não fornecidas e duplicidade não resolvida continuam pendentes; a decisão dos 97 trata somente de direitos para o uso privado delimitado. A galeria privada portátil organiza 92 sanitizadas em cópias exatas dentro de `assets/`, com caminhos relativos ao HTML, sem imagens remotas nem caminhos Linux absolutos nos atributos `src`. O snapshot examinado e seus assets permanecem imutáveis; os estados exibidos nele são os anteriores à revisão posterior, cujos resultados atuais estão nos registros e no recibo privado. Nenhuma imagem foi recodificada, baixada ou reavaliada pelo agente. Para abrir o snapshot, usar `explorer.exe "$(wslpath -w '<caminho-privado-da-galeria>/index.html')"`; copiar a pasta completa preserva os assets. O recibo privado da revisão guarda as resoluções, escopo e hashes individuais. Manifestos, recibos e checkpoints anteriores permanecem históricos; o aceite limitado anterior continua vinculado aos seus bytes e não encerrou U-803/U-804 ou P08. Sem staging/commit/push nesta rodada.

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
