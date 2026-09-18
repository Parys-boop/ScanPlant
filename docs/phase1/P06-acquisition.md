# P06 — aquisição de candidatos do Wikimedia Commons

Execução direta autorizada, sobre `2a8a6902fd6e33b794628235757b0279f580b02a`,
na branch `bm/v2-p06-direct`. O rascunho de planejamento do outro computador
não foi usado. Este documento descreve o mecanismo implementado; não é um novo
pacote de planejamento, aprovação de dataset ou gate de release.

Resultado real de 2026-09-18: [relatório agregado](../../artifacts/phase1/p06/coverage.json).
Foram consultados 109 candidatos em 12 páginas, com 11 aceitos em quarentena
(7 CC BY 4.0 e 4 CC0 1.0), 94 rejeitados, 4 pendentes pelo teto e zero falhas.
As 14 classes, inclusive as que ficaram em zero, estão discriminadas no relatório.
O manifesto externo final tem SHA-256
`98bf4332edd7b97b99ee9229a84fed6afaa59b03817a568699ee716754ca7198`.
Foram verificados 11/11 hashes e arquivos sem EXIF/GPS; isso não é revisão visual.

## Executar e retomar

Python 3.12+ em Linux/WSL e Pillow fixado em
`scripts/phase1/requirements-p06.txt`. Instale em ambiente virtual local, nunca
global. A coleta usa apenas GET público, sem chaves, cookies ou autenticação.

```bash
python3 -m venv /tmp/scanplant-p06-venv
/tmp/scanplant-p06-venv/bin/python -m pip install -r scripts/phase1/requirements-p06.txt
/tmp/scanplant-p06-venv/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
/tmp/scanplant-p06-venv/bin/python -B scripts/phase1/acquire_commons.py --max-accepted 2 --max-pages 1 --timeout 15 --retries 1
```

Por padrão, a saída é `$HOME/datasets/scanplant/p06`. `--output` pode selecionar
outro diretório externo. Destino dentro do repositório é recusado. O ambiente
precisa permitir rede e escrita nesse destino. Se a distribuição não fornecer
`venv`/`ensurepip`, provisione o ambiente Python antes dos comandos; não altere o
Python de sistema para executar a coleta.

Repita a mesma CLI para retomar. Itens aceitos registrados, com arquivo existente
e SHA-256 correto, não são baixados novamente. Falhas de transferência e arquivos
ausentes/corrompidos são tentados novamente. Consultas esgotadas não são repetidas.
Um limite de páginas encerra somente a invocação; a próxima retoma o cursor salvo.
Se o teto de aceitos interromper uma página, seu cursor é mantido para permitir
aumento posterior do teto sem perder candidatos. A API pode mudar entre execuções;
a ordem e o conteúdo da pesquisa ao vivo não são um snapshot imutável do Commons.

`--resume-only` retoma somente registros existentes, sem novas pesquisas/páginas.
Rejeições por licença são reavaliadas apenas quando a prova registrada passa na
regra atual (por exemplo, a representação CC0 `cc0` com `deed.en` observada na API).
O resultado anterior continua no histórico. Arquivos válidos continuam preservados.
Se a prova passar mas o teto já estiver atingido, o registro torna-se `deferred`
com motivo `accepted_cap_reached`; não é falsamente rejeitado por licença.
Um teto menor que a quantidade já aceita é recusado sem apagar arquivos.

O padrão é até 100 aceitos por classe e duas páginas por invocação. `--max-accepted`
aceita 1–100, jamais exige atingir o teto. `--max-pages` aceita 1–100. Cada página
pede até 10 arquivos, pois `extmetadata` é uma propriedade custosa. A execução
real controlada desta entrega usa teto 2 e uma página por classe. Zero é um
resultado válido; não há alegação de suficiência para treinamento.

## Identidade, consulta e critérios

Antes da rede, a CLI valida os bytes do manifesto canônico 1.1.0 e seu roster
com o validador existente de P05-R1. O SHA-256 do manifesto fica no estado; sua
mudança impede retomada silenciosa. As 14 classes e sua ordem vêm exclusivamente
desse manifesto.

As 12 espécies usam o nome científico canônico entre aspas na pesquisa Commons,
namespace 6, ordenação por relevância. Sinônimos não são expandidos nesta coleta
limitada. `outra_planta` e `imagem_invalida` constam com contagens zero e status
`not_applicable_automatic_query`: são proteções sem nome científico, e um resultado
de busca genérica não prova suas definições. Sua curadoria não é simulada.

A licença é examinada por arquivo, usando a combinação exata de `License`,
`LicenseShortName` e `LicenseUrl` em `imageinfo.extmetadata`:

| Identificador Commons | Nome aceito | URL normalizada |
|---|---|---|
| `cc0` ou `cc-zero` | `CC0` ou `CC0 1.0` | `https://creativecommons.org/publicdomain/zero/1.0/` |
| `cc-by-4.0` | `CC BY 4.0` | `https://creativecommons.org/licenses/by/4.0/` |

Somente esquema HTTP→HTTPS, barra final e sufixo localizado `deed.<idioma>` da URL
de licença são normalizados, preservando a URL original no manifesto externo.
Licenças ausentes, outras versões, BY-SA, múltiplas/ambíguas ou campos conflitantes
são rejeitados. Domínio público genérico não é prova de CC0. Autoria vazia ou
indicada como desconhecida/anônima é rejeitada. `Restrictions` não vazio é
rejeitado conservadoramente como `privacy_restriction`.

Todos os candidatos que passam os filtros ficam em `quarantine/`. A aceitação
significa apenas licença/autoria e arquivo aprovados automaticamente. Eles têm
`privacy_status=quarantined_pending_human_review`, `visual_review_performed=false`
e `botanical_validation_performed=false`. Não existe promoção automática para
uso posterior. Nenhuma ausência de pessoas, consentimento, correção taxonômica,
qualidade ou revisão visual é afirmada. Nem o conteúdo visual nem os metadados
do Commons constituem garantia botânica ou verificação independente da titularidade.

## Arquivos, privacidade e rastreabilidade

Arquivos permitidos: JPEG (`.jpg`, `.jpeg`) e PNG (`.png`), até 20 MiB de entrada
e de saída e 25 milhões de pixels. O tipo decodificado deve coincidir com a
extensão e o MIME informado pela API. Arquivos ilegíveis, truncados, animados,
excessivos ou de outro formato são rejeitados. Download e redirecionamentos
aceitam somente HTTPS no host Wikimedia esperado.

A imagem é inteiramente decodificada, orientada segundo EXIF e reconstruída a
partir de pixels RGB em objeto novo. EXIF, GPS, XMP, comentários e ICC não são
copiados. JPEG é recodificado com qualidade 95; PNG permanece sem perda dos pixels
RGB resultantes (alpha/perfil de cores não são preservados). Isso não é
normalização de treino. O original permanece apenas em memória. SHA-256 do original
e do arquivo limpo são registrados; deduplicação global usa ID Commons e ambos
os hashes. Não há deduplicação perceptual.

O diretório externo contém:

- `state.json`: fonte de retomada, registros de tentativas e cursores por classe;
- `manifest.jsonl`: projeção de auditoria, ordenada por sequência;
- `coverage.json`: contagens e motivos sem autoria ou dados brutos dos arquivos;
- `quarantine/<sha256>.jpg|png`: arquivos limpos aguardando revisão;
- `.lock`: trava do sistema operacional para uma única execução por destino.

Cada registro de candidato preserva classe, consulta, timestamp UTC, ID, título,
URL da página e do arquivo, autor em texto e HTML original, crédito/atribuição,
licença/nome/identificador/URL, restrições, timestamp e SHA-1 declarados da origem,
resultado/motivo e, quando armazenado, hashes e transformação. HTML é dado de
auditoria, não deve ser renderizado como conteúdo confiável. Falhas de busca têm
campos indisponíveis explicitamente nulos, sem inventar candidatos.

JSON usa UTF-8, LF final, chaves ordenadas e separadores fixos; JSONL é determinístico
para os mesmos registros e timestamps, não entre pesquisas ao vivo distintas.
Cada tentativa é preservada no histórico; contagens de itens usam o resultado
mais recente por classe/ID. `consulted` conta IDs distintos efetivamente examinados;
`pages_fetched` conta respostas de página recebidas, inclusive repetidas após
interrupção. `failures` conta tentativas com falha, inclusive recuperadas. Aceitos
com arquivo íntegro contam também como `quarantined`; `usable` permanece zero.
`reasons` cobre rejeições vigentes e `failure_reasons` cobre falhas históricas.
`deferred` e `deferred_reasons` registram candidatos conhecidos aguardando espaço
no teto, sem download nem aceite. As contagens não presumem treinamento liberado.

Estado é substituído atomicamente antes das projeções. Cada candidato é salvo
individualmente; se a execução parar no meio da página, a retomada ignora decisões
já registradas. Um arquivo limpo órfão de interrupção antes do registro não é
considerado aceito. Projeções são reconstruídas a partir do estado na retomada.
Temporários ficam no próprio destino externo, nunca na worktree. Não edite o
estado manualmente nem misture versões do coletor no mesmo dataset.

Timeout padrão: 20 s por operação de rede/leitura; a leitura também verifica um
orçamento decorrido (uma leitura bloqueada ainda pode consumir seu timeout).
Até duas novas tentativas por requisição por padrão, máximo configurável de três;
403/404 não são repetidos. 429/500/502/503/504, timeout e falha de rede têm espera
limitada. `maxlag` da API tem novas tentativas limitadas separadas. O user-agent
identifica ScanPlant, versão e URL pública do projeto. Há pausa entre requisições.

Falha de busca interrompe a rodada, registra o bloqueio e preserva classes ainda
não tentadas com esse status. Exit codes: 0 para rodada limitada sem falha pendente,
1 para bloqueio de aquisição, 2 para configuração/estado/IO local inválidos.
Erros não imprimem corpos HTTP, caminhos pessoais, cookies ou credenciais.

## Git e verificação

Código, dependência fixada, testes sintéticos, este documento e relatório agregado
podem ser versionados. Os testes geram imagens mínimas em memória e as armazenam
somente em temporários externos. `.gitignore` bloqueia datasets, quarentena,
imagens novas, bytecode e temporários. Assets já rastreados do aplicativo continuam
no inventário histórico; não são imagens adquiridas em P06. Não copiar o manifesto
externo ou suas atribuições para Git. O relatório seguro não inclui títulos,
autores, URLs de arquivos ou caminhos pessoais.

```bash
python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'
python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json
python3 /caminho/da/skill/_shared/scripts/bm.py validate-state docs/living/PROJECT_STATE.md
sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
git diff --check
```

`python` nos dois primeiros comandos deve ser o ambiente isolado com Pillow.
Testes cobrem licenças/autoria, paginação, zeros, retomada e interrupção, corrupção,
deduplicação, teto 100, timeout/HTTP, tipo/bytes/pixels, EXIF/GPS/orientação,
serialização e inventário Git. Não são executados treinamento, mutação,
homologação, release, build mobile ou alterações da API.

## Referências técnicas

Consultadas em 2026-09-18; somente os contratos usados na implementação:

- [MediaWiki Imageinfo](https://www.mediawiki.org/wiki/API:Imageinfo): metadados por arquivo e limites de consulta.
- [MediaWiki Search](https://www.mediawiki.org/wiki/API:Search): generator, namespace e paginação.
- [Commons Machine-readable data](https://commons.wikimedia.org/wiki/Commons:Machine-readable_data): campos de autoria, licença e restrições.
- [Wikimedia User-Agent Policy](https://foundation.wikimedia.org/wiki/Policy:Wikimedia_Foundation_User-Agent_Policy): identificação do cliente.
- [Pillow Image](https://pillow.readthedocs.io/en/stable/reference/Image.html): decodificação, verificação e limites de pixels.
- [CC0 1.0 deed.en](https://creativecommons.org/publicdomain/zero/1.0/deed.en): representação observada na API e sua URL canônica.
