# Mudança ScanPlant — P05 / F1-MAN01: manifesto das classes offline

## Objetivo e limites

D-201, D-203, A-202. Uma unidade entrega o manifesto canônico, referências, validador documental, verificação negativa e revisão humana. Ainda não há consumidor de produto: treino, catálogo e inferência apenas recebem um contrato de compatibilidade. Sem interface; design_required false. Sem banco, migração, endpoint, autenticação nova, concorrência de usuários ou efeito externo de produto.

Preservar P01/P03-R6 blocked-terminal sem retry, P02/P04 completed, release pending e active_execution null durante planejamento. Pl@ntNet principal gratuito e Plant.id secundário técnico de trial permanecem decisões históricas; nenhuma chamada ou credencial é necessária. Não alterar backend/mobile/web, prova PT-05, modelos, fotos ou datasets. Nenhuma instalação, restore, build, teste de produto, Stryker, mutação ou plano de aquisição de imagens.

## Entrada humana e pesquisa taxonômica

A-201, U-201, P-201. A lista de 12 não foi localizada. O piloto documenta Epipremnum aureum, Monstera deliciosa, Zamioculcas zamiifolia, Spathiphyllum wallisii e Dracaena trifasciata; Sansevieria trifasciata é alias documentado, não nova classe. Nenhuma conclusão autoriza as outras sete; Bellis perennis é controle histórico, sem inclusão automática.

Antes de preencher o manifesto, U-201 deve fornecer a lista completa de 12 táxons distintos já aprovados, com fonte ou declaração explícita do responsável. Registrar na execução `artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`: objeto fechado com schema_version inteiro 1, status approved, approval_ref textual sanitizada, approved_on ISO YYYY-MM-DD real, species (12 objetos de index 0–11, approved_name e source_ref não vazios). A ordem humana é a primeira ordem canônica; se a fonte não for ordenada, ordenar uma única vez por nome aprovado normalizado, registrar essa decisão no roster e submetê-la ao aceite final. Não é permitida escolha de espécies pelo executor. Preenchimento desse dado previsto não altera o pacote; mudança de membros do escopo é material e exige nova decisão.

Consultar apenas páginas taxonômicas oficiais textuais, sem autenticação ou download de imagem/dataset. Priorizar POWO/Kew já usado em F1-G01; Flora e Funga do Brasil/JBRJ é fonte complementar. Para cada nome e sinônimo, registrar página direta do táxon, nome aceito apontado pela autoridade, tipo de relação e data real de consulta. Reutilizar prova específica já versionada preservando data histórica; não datar consulta não realizada. Autorias botânicas são metadados de referência, não parte da chave normalizada. Fonte indisponível, nome ambíguo, sinonímia conflitante, gênero/cultivar sem espécie ou dois itens humanos para o mesmo táxon bloqueiam a entrega na mesma U-201. Não resolver conflito por popularidade de provider nem obter sete espécies via busca web.

## Formato e entidades

D-202, SD-201. Artefato futuro `docs/phase1/offline-class-manifest.v1.json`, JSON estrito UTF-8 sem BOM, LF e newline final. Rejeitar chaves duplicadas, NaN/Infinity, campos desconhecidos, tipos coercíveis e boolean no lugar de inteiro. Objetos têm chaves contratuais; ordem de chaves não é semântica, ordem do array classes é.

Objeto raiz fechado: schema_version (inteiro 1), manifest_version (string 1.0.0 na primeira entrega), normalization_version (string 1), roster_sha256 (64 hex minúsculos dos bytes aprovados do roster), references (array de fontes), classes (array de 14 classes). Nenhum campo de provider, confiança, limiar, caminho de foto ou segredo.

Cada referência: ref_id único ASCII snake_case, authority em kew_powo ou jbrj_flora, url HTTPS sem userinfo/query/fragmento para página específica do táxon no host powo.science.kew.org, floradobrasil.jbrj.gov.br ou reflora.jbrj.gov.br, consulted_on data ISO válida não futura e title não vazio. A URL deve ser registro específico, não homepage/busca; conferência semântica humana obrigatória. Não persistir corpo integral de página, cookie ou identificador pessoal.

Classes possuem exatamente index, class_id, kind, scientific_name, display_name, common_names, synonyms, taxonomy_ref_ids e definition:
- Espécies: índices 0–11, IDs species_01 até species_12 correspondentes; kind species; scientific_name binomial canônico sem autoria; display_name pt-BR não vazio pertencente a common_names; common_names lista não vazia de nomes comuns necessários ao produto; taxonomy_ref_ids não vazio apontando referências do nome canônico; definition null.
- synonyms: lista de objetos fechados name e ref_ids. Cada name é binomial sem autoria; ref_ids não vazio prova que é sinônimo do scientific_name da mesma classe. Aceitar todos os sinônimos ao nível de espécie listados pela fonte primária selecionada que correspondam ao mesmo táxon aprovado; não incorporar automaticamente variantes, cultivares, nomes mal aplicados ou táxons infraspecíficos como aliases. Evidência explica o recorte e os nomes excluídos. Lista vazia só é aceita se a revisão documentar que não foram encontrados aliases elegíveis, nunca como preenchimento desconhecido.
- Proteções: index 12/class_id outra_planta e index 13/class_id imagem_invalida; kind protection; scientific_name null; common_names, synonyms e taxonomy_ref_ids vazios; display_name respectivamente Outra planta e Imagem inválida; definition textual conforme a seção seguinte.
- IDs species_NN são opacos e não derivam de nome científico mutável; nomes canônicos/sinônimos devem ligar 1:1 cada índice ao approved_name do roster. Uma renomeação taxonômica só preserva a identidade se a fonte oficial provar o mesmo táxon, com aceite humano.

Binomial estrutural: exatamente dois termos ASCII separados por espaço simples, gênero `[A-Z][a-z]+`, epíteto `[a-z]+(?:-[a-z]+)*`. Casos fora desse contrato, inclusive híbrido ou infraspécie na lista aprovada, não são descartados nem convertidos silenciosamente: são divergência material do contrato que pausa antes da população para ajustar o pacote com o responsável.

## Normalização e comparação

D-202, P-202. Entradas string passam por Unicode NFC, remoção de espaços externos, colapso de qualquer sequência de whitespace Unicode em um espaço ASCII e casefold. Saída vazia é inválida. Não remover acentos, pontuação, autoria, hífens, palavras ou caracteres parecidos; não usar fuzzy match, prefixo, substring ou transliteração. Rejeitar controles Unicode não whitespace e caracteres de formatação invisíveis. Repetir normalização deve produzir o mesmo resultado.

Chaves taxonômicas: comparar igualdade exata da normalização de scientific_name e de cada synonym.name. Cada chave normalizada mapeia a exatamente uma espécie; repetir sinônimo na mesma classe, alias igual ao canônico ou colisão entre quaisquer classes causa erro. Texto não reconhecido retorna ausência de correspondência (null), nunca uma classe escolhida ou proteção implícita.

Nomes comuns têm namespace separado, somente exibição/pesquisa futura; não são aliases taxonômicos. Rejeitar duplicados normalizados dentro de common_names; homônimos entre espécies podem existir e devem ser explicitados na revisão, sem resolução automática para uma classe. class_id e indices usam igualdade exata, sem normalização de conveniência. Proteções não participam do mapa científico.

## Semântica das proteções e compatibilidade

P-201, P-202. outra_planta significa imagem utilizável de planta cuja identidade de referência está fora das 12 suportadas. Não significa espécie nomeada nem substitui resultado desconhecido por baixa confiança. imagem_invalida significa conteúdo sem planta ou sem informação visual suficiente para uma atribuição botânica única; exemplos sem aquisição de dados: imagem vazia, objeto não vegetal, enquadramento/qualidade insuficiente ou mistura sem alvo inequívoco. Espécie suportada de baixa confiança não muda de identidade taxonômica por limiar; essa decisão de fluxo pertence a integração futura. Bytes ilegíveis são erro de entrada, não amostra botânica a criar neste marco.

Congelar índices e IDs na revisão final. Saída futura terá 14 posições e a posição i corresponde ao class_id de classes[i]. Treino usará o mesmo mapa e hash; catálogo vinculará as 12 espécies por class_id, sem inventar cuidados para proteção. Apenas documentar, não implementar consumidores nem formato de tensor/modelo.

Versionamento: schema_version para mudanças estruturais; manifest_version SemVer; alteração de quantidade, identidade ou ordem exige nova major e aprovação de escopo; nomes/sinônimos com alteração de resolução exigem minor e revisão de colisões sem mudar IDs/índices; correção de metadados sem efeito na resolução pode ser patch. Cada versão aceita fixa SHA-256 dos bytes; nenhuma regeneração por ordem alfabética após o freeze.

## Validador e critérios objetivos

Criar na execução `scripts/phase1/validate_offline_manifest.py` e `scripts/phase1/test_offline_manifest.py`, Python 3.12 stdlib. CLI real proposto: `python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`. Esses caminhos não existem ainda e não serão executados no planejamento.

CLI somente leitura, sem rede/cache, não reescreve manifesto. Exit 0 apenas com todas as regras satisfeitas; exit 1 para contrato inválido e 2 para invocação/arquivo inacessível. Diagnóstico contém código de erro e caminho JSON, sem eco de valores de entrada. Saída de sucesso resume 12 species, 2 protection, 14 classes, versões e SHA-256. Funções públicas normalize_name e resolve_scientific_name dão os seams testáveis sem integração de produto.

Aceite automático: schema fechado e tipos exatos; quantidade 12+2; índices contíguos e correspondentes à posição e ID; roster 12 aprovado/hash correto; cada nome do roster resolve ao índice correspondente, sem ausências/extras; IDs, fontes e chaves taxonômicas únicos; aliases referenciados corretamente; nenhuma referência órfã ou ID inexistente; binomiais, listas, versões, datas e URLs no formato; proteções completas/exclusivas; regras de normalização e namespace.

Na mesma unidade, unittest exercita fixture sintética mínima sem criar espécies de produto; usar deep copies em memória e arquivos temporários só nos testes documentais futuros. Positivos: contrato 12+2, alias conhecido, variação de caixa/whitespace/NFC, idempotência, homônimo comum sem resolução taxonômica, desconhecido null. Negativos: 11/13 espécies; proteção ausente/trocada; ID/índice duplicado, bool como índice, reordenação; canônico/alias repetido intra/interclasse; alias sem referência; formato/tipo/campo extra; nome fora do roster ou hash errado; data impossível/futura, URL não oficial, chaves JSON duplicadas/NaN e controles invisíveis. Verificar códigos de saída e ausência de escrita/rede. Não chamar isso de campanha de mutação.

Comando suíte futura: `python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'`. O teste do validador é documental, não teste de produto. Não instalar jsonschema, pytest ou qualquer dependência.

## Evidências e revisão humana

U-201, P-203. Produzir na execução `docs/phase1/F1-MAN01-offline-class-manifest.md` com uso/formato/normalização/proteções/compatibilidade, e em `artifacts/bianchini/v2/evidence/P05-f1-man01/`: approved-species-roster.json, taxonomy-review.md, validation-report.json e SHA256SUMS. taxonomy-review.md relaciona 12 registros aos nomes aprovados, fonte canônica e cada sinônimo, nomes excluídos/homônimos e evidência de datas; não copia textos extensos. Revisão humana final explicita approved/rejected, papel responsável, data e hashes do manifesto/roster. O agente nunca escreve approved sem decisão humana real. validation-report.json registra comandos, cwd relativo, exit codes, contagens e hashes, sem saída bruta sensível.

Critérios humanos: correspondência 12/12 com o escopo; nome aceito e todos os aliases incluídos com prova; nomes comuns adequados a pt-BR; distinção das proteções; tabela index/class_id aprovada; nenhum consumidor implementado ou taxa adicionada; revisão ligada aos bytes finais. Parser/hash não substitui esse aceite. Ausência de fonte ou parecer mantém P05 incompleto; não prometer acurácia de modelo.

SHA256SUMS cobre roster, taxonomy-review, validation-report e os quatro arquivos futuros (manifesto, documentação, validador e testes) por caminhos relativos à raiz; não inclui a si mesmo, estado ou ledger. Registrar por append no ledger P05 policy, comandos/resultados, fronteiras e revisão. Não incluir ledger vivo no snapshot de aprovação nem modificar pacotes/ledgers históricos. Validar paths/hash e segredos sem exibir valores.

## Gates e encerramento do plano

Fast: unittest focal e CLI do manifesto após U-201. Plan: mesma suíte completa do validador, CLI, JSON estrito da evidência, SHA256SUMS, git diff --check, whitespace também dos untracked e revisão humana U-201. Execução local requer só Python/Git; leitura taxonômica oficial pode ocorrer sem credenciais. Fix rounds máximos 3 no seam offline-manifest-contract segundo policy; gate final da única unidade, sem microtarefas.

Manifesto e validações pertencem à mesma rodada de execução; U-201 é fronteira, não outro plano. Planejamento atual só executa checkers documentais do pacote, audit e snapshot. Execução v2 posterior exige pacote aprovado e commitado e workspace separado conforme método; nenhuma branch/worktree é criada aqui. Aprovação humana do digest não autoriza staging/commit/push ou execução nesta rodada.

Concluir somente P05 após gates e aceite real. Não fechar ciclo v2 ou sincronizar current/specs; SD-201 só é sincronizado no encerramento regular futuro. Manter release pending: lifecycle/garantia seletiva de P01, fingerprint, suítes/build aplicáveis e homologação continuam gates independentes e não são substituídos por este manifesto.
