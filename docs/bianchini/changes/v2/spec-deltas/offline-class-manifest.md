# Contrato de domínio esperado — manifesto offline

SD-201, D-201, D-202, U-201. Destino futuro: `docs/bianchini/current/specs/offline-class-manifest.md`, inexistente no checkpoint. Não criar/editar esse target durante planejamento ou execução; sincronização só no encerramento regular do ciclo, ainda impedido pelos gates de release.

## Artefato e população autorizada

O domínio é o manifesto JSON canônico do classificador offline, versão inicial schema_version 1, manifest_version 1.0.0 e normalization_version 1. UTF-8 sem BOM, LF e newline final; campos fechados e tipos exatos. Nenhuma espécie além da lista completa das 12 aprovada pelo responsável pode entrar. A lista é entrada obrigatória U-201, não inferível do piloto de cinco nem de fonte web. Sem lista, fonte taxonômica ou aceite final, o domínio não está entregue.

Raiz: schema_version, manifest_version, normalization_version, roster_sha256, references e classes. roster_sha256 fixa os bytes do roster aprovado contendo exatamente 12 itens index/approved_name/source_ref em índices 0–11; seu envelope contém schema_version 1, status approved, approval_ref e approved_on reais. Não confundir dados humanos recebidos com aprovação gerada pelo agente.

references contém ref_id único, authority (kew_powo/jbrj_flora), url HTTPS direta do táxon em host oficial POWO/Kew ou Flora/JBRJ, consulted_on ISO válida não futura e title. Não há query, fragmento, userinfo, segredo ou corpo de resposta. Datas históricas específicas podem ser reaproveitadas sem fingir consulta nova.

## Classes e identidade

Array de 14 classes; posição deve coincidir com index. Cada classe tem exatamente index, class_id, kind, scientific_name, display_name, common_names, synonyms, taxonomy_ref_ids e definition. Indices 0–11 são species, IDs species_01 a species_12. As 12 identidades correspondem 1:1 aos nomes aprovados no roster por nome aceito ou sinônimo provado. A ordem inicial segue a entrada aprovada; fonte não ordenada é ordenada uma única vez por approved_name normalizado, com registro e aceite. Depois do freeze nunca reordenar.

Espécie tem scientific_name binomial canônico sem autoria, display_name presente em common_names pt-BR não vazio, synonyms como objetos name/ref_ids e taxonomy_ref_ids não vazio para o nome aceito; definition null. Binomial: gênero [A-Z][a-z]+ e epíteto [a-z]+(?:-[a-z]+)* separados por espaço simples. Cada sinônimo ao nível de espécie da fonte primária que aponta ao mesmo táxon precisa de referência; registrar exclusões de nomes mal aplicados/infraspécies/cultivares. Lista vazia exige justificativa de revisão. Nome aprovado fora do contrato exige resolver a divergência, não descartar espécie.

Índice 12 é outra_planta, índice 13 imagem_invalida; kind protection, scientific_name null, common_names/synonyms/taxonomy_ref_ids vazios; display_name Outra planta/Imagem inválida e definition não vazia. outra_planta representa planta utilizável cuja referência está fora das 12. imagem_invalida representa ausência de planta ou informação insuficiente para atribuição botânica única. Proteção não é espécie ou rótulo taxonômico; baixa confiança e nome desconhecido não se convertem automaticamente em proteção. Bytes ilegíveis continuam erro de entrada fora deste artefato.

## Resolução e invariantes

normalize_name aplica NFC, trim, colapso de whitespace Unicode para espaço e casefold; rejeita vazio, controles não whitespace e formatação invisível. Não remove acentos/autoria/pontuação nem faz correspondência aproximada. resolve_scientific_name usa igualdade exata dessa chave com scientific_name ou synonym.name, retorna class_id único ou null. Nomes comuns são namespace separado de exibição; homônimos entre espécies são explicitados e nunca resolvidos implicitamente. IDs/indices usam igualdade exata.

Unicidade global de IDs, índices, ref_ids e chaves canônicas/sinônimos; rejeitar aliases repetidos na mesma classe, alias igual ao canônico e colisões interclasse. Nomes comuns não duplicam dentro de uma classe. Referências devem existir, ser usadas e provar a relação correta. Sem NaN/Infinity, chave duplicada JSON, campo extra, coerção ou bool como inteiro.

## Verificação e uso futuro

CLI Python 3.12 stdlib, somente leitura, sem rede: valida schema, 12+2 classes, ordem/IDs, versão, hash/12 nomes do roster, binomiais, normalização, aliases e referências. Exit 0 com contagens/hashes; 1 contrato inválido; 2 invocação/arquivo inacessível; erro por código e caminho, sem eco de entrada. Testes documentais positivos e negativos cobrem quantidade, duplicatas, proteções, colisões, reorder, tipos, formatos, roster e Unicode.

Revisão humana confere 12/12 identidades, nomes comuns, nome científico e cada alias contra fontes datadas, aprova mapa index/class_id e semântica das proteções; registrar parecer e hashes finais, jamais inferir aceite a partir de parser. Evidência rastreável e SHA256SUMS acompanham manifesto/documentação/validador/testes. Nenhuma implementação de treino, catálogo, saída real ou frontend pertence ao domínio entregue.

Saída futura reserva 14 posições por classes[i].class_id; catálogo vincula 12 espécies por class_id, sem cuidados para proteções. Major muda identidade/quantidade/ordem sob nova aprovação; minor altera resolução taxonômica mantendo IDs/ordem e exige revisão; patch altera apenas metadados sem efeito semântico. SHA-256 fixa os bytes de cada versão aceita. Nenhuma compatibilidade de modelo/treinamento foi testada ou prometida. P05 não fecha gates P01/P03 ou release.
