# Contrato completo esperado — manifesto offline após P05-R1

SD-201, D-211, D-212, D-213, A-211, P-211, P-212, P-213, U-201.
Destino futuro: docs/bianchini/current/specs/offline-class-manifest.md, ainda inexistente.
Não sincronizar durante planejamento/execução; apenas no encerramento regular do ciclo.
Este delta substitui para a entrega futura a regra afetada do delta P05 histórico, sem editá-lo.

## Formato e identidade

Artefato docs/phase1/offline-class-manifest.v1.json; UTF-8 sem BOM, LF, newline final.
JSON estrito, objetos fechados, tipos exatos: rejeitar duplicatas, NaN/Infinity, não finitos,
campos desconhecidos e bool onde exige inteiro. Raiz: schema_version inteiro 1,
manifest_version string 1.1.0 proposta, normalization_version string 1,
roster_sha256 SHA-256 em 64 hex minúsculos, references e classes.

Roster aprovado preservado byte a byte: schema_version 1, status approved, approval_ref,
approved_on ISO real e species com 12 objetos index/approved_name/source_ref; hash permanece
350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b.
Não reordenar, renomear ou substituir espécies. Correspondência 1:1 com classes:

| Índice | class_id | scientific_name | display_name pt-BR |
|---|---|---|---|
| 0 | species_01 | Epipremnum aureum | jiboia |
| 1 | species_02 | Monstera deliciosa | costela-de-adão |
| 2 | species_03 | Zamioculcas zamiifolia | zamioculca |
| 3 | species_04 | Spathiphyllum wallisii | lírio-da-paz |
| 4 | species_05 | Dracaena trifasciata | espada-de-são-jorge |
| 5 | species_06 | Aloe vera | babosa |
| 6 | species_07 | Chlorophytum comosum | clorofito |
| 7 | species_08 | Codiaeum variegatum | cróton |
| 8 | species_09 | Ficus elastica | falsa-seringueira |
| 9 | species_10 | Kalanchoe blossfeldiana | flor-da-fortuna |
| 10 | species_11 | Nephrolepis exaltata | samambaia-americana |
| 11 | species_12 | Tradescantia zebrina | lambari-roxo |
| 12 | outra_planta | null | Outra planta |
| 13 | imagem_invalida | null | Imagem inválida |

Classes têm exatamente index, class_id, kind, scientific_name, display_name, common_names,
synonyms, taxonomy_ref_ids e definition. Índice coincide com posição; IDs opacos e estáveis.
Espécies 0–11: kind species, scientific_name binomial canônico, display_name em common_names
não vazio e pt-BR; taxonomy_ref_ids não vazio; definition null. Preservar todos os valores
do checkpoint desses campos. Binomial armazenado tem exatamente gênero [A-Z][a-z]+,
espaço simples e epíteto [a-z]+(?:-[a-z]+)*. Fora desse formato é divergência explícita,
sem converter ou descartar espécie silenciosamente.

Proteções 12/13: kind protection, scientific_name null, common_names/synonyms/taxonomy_ref_ids
vazios, display_name conforme tabela e definition textual inalterada. outra_planta é planta
utilizável fora das 12 identidades de referência. imagem_invalida é ausência de planta ou
informação visual insuficiente para atribuição botânica única (vazia, objeto não vegetal,
qualidade/enquadramento insuficiente, mistura sem alvo inequívoco). Baixa confiança não troca
identidade taxonômica; bytes ilegíveis são erro de entrada. Desconhecido não vira proteção.

## Referências e elegibilidade

references: objetos ref_id único ASCII snake_case, authority kew_powo/jbrj_flora, url HTTPS
direta de táxon em powo.science.kew.org, floradobrasil.jbrj.gov.br ou reflora.jbrj.gov.br,
sem userinfo/query/fragmento/porta; consulted_on ISO válida não futura; title não vazio.
Sem referência órfã ou ref_id inexistente. Cada relação exige fonte oficial específica.
Reusar a consulta de 2026-09-11 sem declarar acesso novo. Não persistir corpo de páginas,
cookies, credenciais ou identificadores pessoais.

synonyms contém objetos fechados name/ref_ids: binômio sem autoria, referências não vazias
que provam sinonímia com o canônico da classe. Incluir todos os sinônimos diretos ao nível
de espécie da fonte primária selecionada cuja chave normalizada sem autoria seja inequívoca
nas fontes taxonômicas aplicáveis. Não herdar aliases de táxons subordinados; não incorporar
automaticamente cultivares, infraspécies, variantes ou nomes mal aplicados. Lista vazia exige
justificativa, como Spathiphyllum wallisii na evidência existente. Ilegitimidade nomenclatural
isolada não autoriza excluir os demais aliases: preservar o recorte oficial já aprovado.

## Quarentena e resolução

Q é o conjunto normalizado dos quatro nomes abaixo. Estes ficam ausentes de synonyms e
do mapa científico resolvível, com evidência mantida como quarantined em taxonomy-review.md.
Cada registro preserva autoria da relação com espécie do manifesto, autoria conflitante,
táxon/identidade conflitante, fontes, motivo e estado explícito. Motivo comum: homonímia
torna chave sem autoria inequívoca impossível. A exclusão do resolvedor não revoga sinonímia
nomenclatural da fonte. Tabela derivada da evidência versionada, consulta 2026-09-11:

| Binômio quarantined | Autoria no manifesto / espécie | Autoria conflitante / identidade | Fontes POWO já documentadas |
|---|---|---|---|
| Aloe maculata | Forssk. / Aloe vera | All. / Aloe maculata, espécie aceita distinta | https://powo.science.kew.org/taxon/530017-1 ; https://powo.science.kew.org/taxon/77122815-1 |
| Aloe variegata | Forssk. / Aloe vera | L. / Gonialoe variegata | https://powo.science.kew.org/taxon/530017-1 ; https://powo.science.kew.org/taxon/530009-1 |
| Ficus clusiifolia | Summerh. / Ficus elastica | Schott / Ficus clusiifolia, espécie aceita distinta | https://powo.science.kew.org/taxon/60458499-2 ; https://powo.science.kew.org/taxon/852625-1 |
| Ficus cordata | Kunth & C.D.Bouché / Ficus elastica | Thunb. / Ficus cordata, espécie aceita distinta | https://powo.science.kew.org/taxon/60458499-2 ; https://powo.science.kew.org/taxon/852662-1 |

normalize_name preserva seu algoritmo: NFC, trim, colapso de whitespace Unicode para
espaço ASCII e casefold; idempotente; rejeita vazio, controles não whitespace, caracteres
de formatação invisíveis e surrogates. Não remove acentos, pontuação, hífens, autoria ou
palavras. Não faz fuzzy matching, transliteração, prefixo, substring, aproximação ou contexto.
Nomes comuns em namespace separado: duplicados normalizados na mesma classe são rejeitados;
homônimos entre classes podem ser documentados, sem resolução científica automática.
IDs/índices usam igualdade exata. Proteções não entram no mapa científico.

resolve_scientific_name(manifest, name) recebe manifesto validado; usa igualdade exata
da chave normalizada com canônico ou alias elegível, retornando class_id único ou None
(null no contrato). Para os quatro Q, retorna None, inclusive variações de caixa/whitespace
admitidas pelo normalizador. Entrada com autoria permanece intacta após normalização e
não é convertida em chave binomial; sem chave correspondente retorna None.
scientific_map/validação devem rejeitar reintrodução de Q como alias ou chave canônica:
erro explícito de contrato, sem escolher classe ou descartar silenciosamente um input inválido.
Um novo homônimo identificado durante revisão bloqueia aceitação e U-201 até decisão explícita;
o parser não pretende detectar sozinho toda homonímia externa ainda desconhecida.

Unicidade global: IDs, índices, ref_ids, chaves canônicas e aliases. Repetição intraclasse,
alias igual a canônico e colisão entre classes são erros. Nenhum canônico pode ser alterado
para resolver quarentena. Não adicionar campo ou autoria às chaves nem mudar schema nesta revisão.

## Versão e compatibilidade

Regra SemVer já registrada: major para identidade/quantidade/ordem; minor para alteração
de resolução por nomes/aliases com IDs/ordem estáveis; patch só metadados sem efeito resolutivo.
P05-R1 propõe minor 1.0.0 → 1.1.0, mesmo sendo o baseline preliminar sem aceite final;
explicita mudança de resolução. schema_version 1 e normalization_version 1; caminho .v1.json
preservado. Não declarar 1.0.0 previamente entregue nem a nova versão aprovada antes da decisão.
Futura saída reserva 14 posições por classes[i].class_id; catálogo vincula espécies por ID.
Somente contrato de compatibilidade, nenhum consumidor ou tensor/modelo implementado.

## Verificação, evidência e aceite

CLI Python stdlib somente leitura e sem rede/cache valida manifesto/roster, 12+2, versões,
hashes, fontes, tipos, identidade, ordem, normalização, colisões e quarentena conhecida.
Exit 0 com contagens/versões/hashes; exit 1 contrato inválido; exit 2 invocação/arquivo.
Diagnóstico só código e caminho JSON sem valores da entrada. Unitários e CLI provam positivos
de 12 canônicos e todos os aliases restantes, quatro negativos, reintrodução e invariantes.

Reconciliar conjuntos por class_id e chave normalizada: A0 = 83 aliases preliminares únicos;
Q tem quatro elementos presentes exatamente uma vez e nenhum canônico; Afinal = A0 menos Q,
sem inserção/troca. Assim esperado 79 aliases, mapa de 91 chaves com 12 canônicos.
Contagem é consequência dessa prova, não critério suficiente. Aloe vera 11→9;
Ficus elastica 12→10; demais contagens 4,6,3,0,1,34,5,1,4,2 permanecem.
Se outros homônimos surgirem, não forçar 79; bloquear até revisão explícita.

Manter coerência entre docs/phase1/F1-MAN01-offline-class-manifest.md, taxonomy-review.md,
validation-report.json, SHA256SUMS e estado/ledger. Relatório registra comandos, cwd relativo,
versão real Python, exit codes, contagens derivadas e hashes. SHA256SUMS cobre os sete
artefatos existentes (manifesto, roster, documentação, revisão, relatório, validador, testes),
sem si mesmo/estado/ledger. Regerar hashes depois dos bytes correspondentes, sem autorreferência;
registrar o aceite humano posterior e hashes em append no ledger/estado.

Revisão humana final U-201 confere 12/12, cada alias, fontes, autorias, exclusões e nomes comuns,
IDs/ordem/proteções, então registra parecer explícito ligado aos hashes dos bytes finais.
Parser e checksums não concedem esse aceite. P05 e U-201 incompletos até todos os gates.
P01/P03-R6 blocked-terminal, P02/P04 completed, release pending permanecem; sem fechar ciclo,
waiver, campanha, provider, imagem, dataset, treino ou integração de produto.
