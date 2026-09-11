# Revisão taxonômica P05/F1-MAN01

Registro UTC: 2026-09-11T19:05:33Z. Responsável pela decisão de produto: responsável humano.

## Decisao humana corrigida U-201

Transcrição da decisão corrigida; substitui somente a política anterior ainda não materializada. O timestamp é o momento real deste registro, não uma estimativa do envio da mensagem.

SHA-256 do texto UTF-8 entre as cercas, incluindo newline final: `8ba368f75fead7272018915181348f6572cc564379ed75529168a0000f63a7e9`.

```text
Corrijo e substituo integralmente a parte referente aos sinônimos da minha decisão humana anterior.

A lista das 12 espécies, seus nomes comuns, a ordem das classes e as duas proteções continuam aprovadas sem alteração. Somente a política de sinônimos da declaração anterior é revogada e substituída pela política compatível com o contrato P05 congelado.

Não solicito alteração da spec, do plano ou do pacote aprovado. Não autorizei aliases infraspecíficos.

Decisão humana corrigida para U-201:

Aprovo como escopo offline do ScanPlant esta lista ordenada:

1. Epipremnum aureum — jiboia
2. Monstera deliciosa — costela-de-adão
3. Zamioculcas zamiifolia — zamioculca
4. Spathiphyllum wallisii — lírio-da-paz
5. Dracaena trifasciata — espada-de-são-jorge
6. Aloe vera — babosa
7. Chlorophytum comosum — clorofito
8. Codiaeum variegatum — cróton
9. Ficus elastica — falsa-seringueira
10. Kalanchoe blossfeldiana — flor-da-fortuna
11. Nephrolepis exaltata — samambaia-americana
12. Tradescantia zebrina — lambari-roxo

Aprovo também:

13. outra_planta — classe de proteção, não espécie
14. imagem_invalida — classe de proteção, não espécie

Na indexação técnica de base zero:

- espécies 1–12: índices 0–11;
- outra_planta: índice 12;
- imagem_invalida: índice 13.

Política de sinônimos aprovada:

1. Siga exatamente a regra congelada em:
   docs/bianchini/changes/v2/specs/offline-class-manifest-change.md

2. Para cada uma das 12 espécies, registre todos os sinônimos binomiais elegíveis retornados pela fonte taxonômica oficial definida no contrato, aplicando integralmente os filtros, regras de normalização e critérios de elegibilidade da spec.

3. Uma lista de sinônimos somente pode ficar vazia quando a fonte oficial não possuir sinônimo binomial elegível depois da aplicação dos filtros aprovados.

4. Exclua:
   - nomes infraspecíficos;
   - variedades;
   - subespécies;
   - formas;
   - autônimos;
   - nomes com três ou mais componentes taxonômicos quando não forem binomiais elegíveis;
   - nomes comuns;
   - aliases não sustentados pela fonte oficial;
   - sinônimos que colidam com o nome canônico de outra classe.

5. `Kalanchoe globulifera var. coccinea` está expressamente excluído porque é infraspecífico e não satisfaz o formato binomial exigido pelo contrato.

6. Os sinônimos enumerados na minha declaração anterior não formam uma allowlist nem um conjunto congelado. Aquela enumeração está substituída integralmente por esta política derivada da fonte e da spec aprovada.

7. Os nomes comuns aprovados são somente rótulos pt-BR do produto. Eles não são nomes científicos, sinônimos taxonômicos ou IDs canônicos.

Esta decisão humana corrigida resolve U-201 somente se o mecanismo de change-policy confirmar que ela é compatível com o contrato P05 já aprovado.
```

## Compatibilidade e fonte

`bm.py change-policy` sem flags de alteração: implementation_detail; plan_invalidating=false; reapproval_required=false. A comparação considerou exclusivamente esta decisão corrigida. Nenhum plano/spec/digest de aprovação foi alterado.

Fonte primária: POWO/Kew, seção Synonyms diretamente subordinada ao registro da espécie aceita, consultada em 2026-09-11. O recorte não percorre sinônimos de variedades/subespécies aceitas, que representam táxons subordinados distintos. Não transfere aliases entre ranks por inferência. Todos os binomiais dessa seção são relacionados abaixo; autorias e notas nomenclaturais ficam nesta evidência, fora das chaves normalizadas. Nomes ilegítimos ou não validamente publicados ainda listados como sinônimos não são automaticamente apagados: a spec não estabelece filtro por validade nomenclatural. A revisão final deve avaliar ambiguidades sem confundir validade do nome com aceitação do táxon.

Consulta textual; nenhum corpo de resposta externa, foto, dataset ou arquivo de modelo persistido. As listas e observações são transcrição factual de nomes, não reprodução de páginas.

## 1. Epipremnum aureum

Nome aceito: **Epipremnum aureum (Linden & André) G.S.Bunting**. Nome comum aprovado: jiboia. [POWO](https://powo.science.kew.org/taxon/87014-1), consulta 2026-09-11. Sinônimos diretos: 4; binomiais: 4; excluídos pelo formato: 0.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Pothos aureus | Linden & André | homotypic | incluído |
| Rhaphidophora aurea | (Linden & André) Birdsey | homotypic | incluído |
| Scindapsus aureus | (Linden & André) Engl. | homotypic | incluído |
| Epipremnum mooreense | Nadeaud | heterotypic | incluído |

## 2. Monstera deliciosa

Nome aceito: **Monstera deliciosa Liebm.**. Nome comum aprovado: costela-de-adão. [POWO](https://powo.science.kew.org/taxon/87478-1), consulta 2026-09-11. Sinônimos diretos: 8; binomiais: 6; excluídos pelo formato: 2.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Tornelia fragrans | Gutierrez ex Schott; nom. illeg. | homotypic | incluído |
| Monstera borsigiana | K.Koch | heterotypic | incluído |
| Monstera deliciosa var. borsigiana | (K.Koch) Engl. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Monstera deliciosa var. sierrana | G.S.Bunting | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Monstera lennea | K.Koch | heterotypic | incluído |
| Philodendron anatomicum | Morsch | heterotypic | incluído |
| Philodendron fenestratum | Linden | heterotypic | incluído |
| Philodendron pertusum | Kunth & C.D.Bouché | heterotypic | incluído |

## 3. Zamioculcas zamiifolia

Nome aceito: **Zamioculcas zamiifolia (G.Lodd.) Engl.**. Nome comum aprovado: zamioculca. [POWO](https://powo.science.kew.org/taxon/89402-1), consulta 2026-09-11. Sinônimos diretos: 3; binomiais: 3; excluídos pelo formato: 0.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Caladium zamiifolium | G.Lodd. | homotypic | incluído |
| Zamioculcas loddigesii | Schott; nom. illeg. superfl. | homotypic | incluído |
| Zamioculcas lanceolata | Peter | heterotypic | incluído |

## 4. Spathiphyllum wallisii

Nome aceito: **Spathiphyllum wallisii Regel**. Nome comum aprovado: lírio-da-paz. [POWO](https://powo.science.kew.org/taxon/89011-1), consulta 2026-09-11. Sinônimos diretos: 0; binomiais: 0; excluídos pelo formato: 0.

Lista vazia justificada: o registro aceito consultado não apresenta seção Synonyms nem sinônimos; não é placeholder de informação desconhecida.

## 5. Dracaena trifasciata

Nome aceito: **Dracaena trifasciata (Prain) Mabb.**. Nome comum aprovado: espada-de-são-jorge. [POWO](https://powo.science.kew.org/taxon/77164235-1), consulta 2026-09-11. Sinônimos diretos: 1; binomiais: 1; excluídos pelo formato: 0.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Sansevieria trifasciata | Prain | homotypic | incluído |

## 6. Aloe vera

Nome aceito: **Aloe vera (L.) Burm.f.**. Nome comum aprovado: babosa. [POWO](https://powo.science.kew.org/taxon/530017-1), consulta 2026-09-11. Sinônimos diretos: 17; binomiais: 11; excluídos pelo formato: 6.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Aloe perfoliata var. vera | L. | homotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe barbadensis | Mill. | heterotypic | incluído |
| Aloe barbadensis var. chinensis | Haw. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe chinensis | Loudon | heterotypic | incluído |
| Aloe elongata | Murray | heterotypic | incluído |
| Aloe flava | Pers. | heterotypic | incluído |
| Aloe indica | Royle | heterotypic | incluído |
| Aloe lanzae | Tod. | heterotypic | incluído |
| Aloe littoralis | J.Koenig ex Baker; not validly publ. | heterotypic | incluído |
| Aloe maculata | Forssk.; nom. illeg. homonym. post. | heterotypic | incluído |
| Aloe perfoliata var. barbadensis | (Mill.) Aiton | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe rubescens | DC. | heterotypic | incluído |
| Aloe variegata | Forssk.; nom. illeg. homonym. post. | heterotypic | incluído |
| Aloe vera var. chinensis | (Loudon) Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe vera var. lanzae | Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe vera var. littoralis | J.Koenig ex Baker | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Aloe vulgaris | Lam. | heterotypic | incluído |

## 7. Chlorophytum comosum

Nome aceito: **Chlorophytum comosum (Thunb.) Jacques**. Nome comum aprovado: clorofito. [POWO](https://powo.science.kew.org/taxon/532810-1), consulta 2026-09-11. Sinônimos diretos: 37; binomiais: 34; excluídos pelo formato: 3.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Anthericum comosum | Thunb. | homotypic | incluído |
| Hartwegia comosa | (Thunb.) Nees | homotypic | incluído |
| Hollia comosa | (Thunb.) Heynh. | homotypic | incluído |
| Phalangium comosum | (Thunb.) Poir. | homotypic | incluído |
| Caesia comosa | (Thunb.) Spreng. | homotypic | incluído |
| Anthericum longituberosum | Poelln. | heterotypic | incluído |
| Anthericum picturatum | Dreer | heterotypic | incluído |
| Anthericum sternbergianum | Schult. & Schult.f. | heterotypic | incluído |
| Anthericum vallis-trappii | Poelln. | heterotypic | incluído |
| Anthericum vittatum | Anon.; unknown publication | heterotypic | incluído |
| Anthericum vittatum variegatum | Hovey | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Anthericum williamsii | T.Moore & Mast. | heterotypic | incluído |
| Chlorophytum brevipes | Baker | heterotypic | incluído |
| Chlorophytum bukobense | Engl. | heterotypic | incluído |
| Chlorophytum bukobense var. kilimandscharicum | Engl. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Chlorophytum burchellii | Baker | heterotypic | incluído |
| Chlorophytum delagoense | Baker | heterotypic | incluído |
| Chlorophytum elatulum | Poelln. | heterotypic | incluído |
| Chlorophytum gazense | Rendle | heterotypic | incluído |
| Chlorophytum glaucidulum | Engl. ex Poelln. | heterotypic | incluído |
| Chlorophytum glaucidulum var. pauper | Poelln. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Chlorophytum inopinum | Poelln. | heterotypic | incluído |
| Chlorophytum kirkii | Baker | heterotypic | incluído |
| Chlorophytum limurense | Rendle | heterotypic | incluído |
| Chlorophytum longum | Poelln. | heterotypic | incluído |
| Chlorophytum magnum | Peter ex Poelln. | heterotypic | incluído |
| Chlorophytum miserum | Rendle | heterotypic | incluído |
| Chlorophytum nemorosum | Poelln. | heterotypic | incluído |
| Chlorophytum paludicola | Poelln. | heterotypic | incluído |
| Chlorophytum ramiferum | Rendle | heterotypic | incluído |
| Chlorophytum rugosum | Poelln. | heterotypic | incluído |
| Chlorophytum sternbergianum | (Schult. & Schult.f.) Steud. | heterotypic | incluído |
| Chlorophytum turritum | Peter ex Poelln. | heterotypic | incluído |
| Chlorophytum usambarense | Engl. ex Poelln. | heterotypic | incluído |
| Cordyline vivipara | Steud. | heterotypic | incluído |
| Phalangium viviparum | Reinw. ex Kunth | heterotypic | incluído |
| Narthecium sarmentosum | Philippar | heterotypic | incluído |

## 8. Codiaeum variegatum

Nome aceito: **Codiaeum variegatum (L.) Rumph. ex A.Juss.**. Nome comum aprovado: cróton. [POWO](https://powo.science.kew.org/taxon/85073-3), consulta 2026-09-11. Sinônimos diretos: 6; binomiais: 5; excluídos pelo formato: 1.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Codiaeum chrysosticton | Rumph. ex Spreng.; nom. illeg. | homotypic | incluído |
| Codiaeum variegatum var. genuinum | Müll.Arg.; not validly publ. | homotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Croton variegatus | L. | homotypic | incluído |
| Crozophyla variegata | (L.) Raf. | homotypic | incluído |
| Oxydectes variegata | (L.) Kuntze | homotypic | incluído |
| Phyllaurea variegata | (L.) W.Wight | homotypic | incluído |

## 9. Ficus elastica

Nome aceito: **Ficus elastica Roxb. ex Hornem.**. Nome comum aprovado: falsa-seringueira. [POWO](https://powo.science.kew.org/taxon/60458499-2), consulta 2026-09-11. Sinônimos diretos: 22; binomiais: 12; excluídos pelo formato: 10.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Stilpnophyllum elasticum | (Roxb. ex Hornem.) Drury | homotypic | incluído |
| Urostigma elasticum | (Roxb. ex Hornem.) Miq. | homotypic | incluído |
| Visiania elastica | (Roxb. ex Hornem.) Gasp. | homotypic | incluído |
| Macrophthalma elastica | (Roxb. ex Hornem.) Gasp. | homotypic | incluído |
| Ficus clusiifolia | Summerh.; nom. illeg. homonym. post. | heterotypic | incluído |
| Ficus cordata | Kunth & C.D.Bouché; nom. illeg. homonym. post. | heterotypic | incluído |
| Ficus elastica var. belgica | L.H.Bailey & E.Z.Bailey | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. benghalensis | Blume | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. decora | Guillaumin | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. karet | (Miq.) Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. minor | Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. odorata | (Miq.) Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. rubra | L.H.Bailey & E.Z.Bailey | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. rubrinervis | Sata; without a Latin descr. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus elastica var. variegata | W.Bull | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Ficus karet | (Miq.) King | heterotypic | incluído |
| Ficus skytinodermis | Summerh. | heterotypic | incluído |
| Ficus taeda | Kunth & C.D.Bouché | heterotypic | incluído |
| Urostigma circumscissum | Miq. | heterotypic | incluído |
| Urostigma elasticum var. latifolium | Miq. | heterotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Urostigma karet | Miq. | heterotypic | incluído |
| Urostigma odoratum | Miq. | heterotypic | incluído |

## 10. Kalanchoe blossfeldiana

Nome aceito: **Kalanchoe blossfeldiana Poelln.**. Nome comum aprovado: flor-da-fortuna. [POWO](https://powo.science.kew.org/taxon/274279-1), consulta 2026-09-11. Sinônimos diretos: 3; binomiais: 1; excluídos pelo formato: 2.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Kalanchoe coccinea | (H.Perrier) Boiteau; contrary to Art. 34.2 ICBN (1994) | homotypic | incluído |
| Kalanchoe coccinea var. blossfeldiana | (Poelln.) Boiteau; contrary to Art. 34.2 ICBN (1994) | homotypic | excluído: infraspecífico ou três componentes taxonômicos |
| Kalanchoe globulifera var. coccinea | H.Perrier | homotypic | excluído: infraspecífico ou três componentes taxonômicos |

## 11. Nephrolepis exaltata

Nome aceito: **Nephrolepis exaltata (L.) Schott**. Nome comum aprovado: samambaia-americana. [POWO](https://powo.science.kew.org/taxon/17160830-1), consulta 2026-09-11. Sinônimos diretos: 4; binomiais: 4; excluídos pelo formato: 0.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Aspidium exaltatum | (L.) Sw. | homotypic | incluído |
| Hypopeltis exaltata | (L.) Bory | homotypic | incluído |
| Nephrodium exaltatum | (L.) R.Br. | homotypic | incluído |
| Polypodium exaltatum | L. | homotypic | incluído |

## 12. Tradescantia zebrina

Nome aceito: **Tradescantia zebrina Regel**. Nome comum aprovado: lambari-roxo. [POWO](https://powo.science.kew.org/taxon/77369906-1), consulta 2026-09-11. Sinônimos diretos: 2; binomiais: 2; excluídos pelo formato: 0.

| Nome | Autoria / nota da fonte | Relação com o nome aceito | Destino |
|---|---|---|---|
| Commelina zebrina | (Regel) André | homotypic | incluído |
| Cyanotis zebrina | (Regel) Nees | homotypic | incluído |

## Exclusões de táxons subordinados e antiga enumeração

As variedades e subespécies aceitas relacionadas nas páginas de Dracaena trifasciata, Codiaeum variegatum, Nephrolepis exaltata e Tradescantia zebrina não são aliases. Em particular, Zebrina pendula e Tradescantia pendula da declaração revogada apontam no POWO para Tradescantia zebrina var. zebrina; não constam nos dois sinônimos diretos da espécie atualmente selecionada. A variedade nominal foi consultada em 2026-09-11 em https://powo.science.kew.org/taxon/77170928-1. Também não incorporados desse registro subordinado: Cyanotis vittata, Tradescantia argentea, Tradescantia tricolor e Zebrina purpusii; nem Cyanotis vittata vittata, Zebrina pendula f. quadricolor ou Zebrina pendula var. quadricolor. Não são aliases automaticamente herdados.

Kalanchoe globulifera var. coccinea está excluído expressamente e pelo formato. Homônimos entre nomes comuns das 12 classes: nenhum. Os nomes comuns não são utilizados por resolve_scientific_name.

## Revisão humana final

Status: blocked_pending_human_taxonomy. A decisão de produto foi recebida; o aceite dos bytes finais não foi concedido. A conferência complementar confirmou ambiguidade taxonômica nos quatro binomiais abaixo. O manifesto já materializado é preliminar e não pode ser entregue como contrato aceito. Não foram removidos aliases silenciosamente nem incluídas autorias nas chaves. Nenhum parecer approved/rejected foi atribuído ao responsável para estes bytes.

| Chave sem autoria | Nome listado para a classe do rascunho | Outro nome e táxon oficial |
|---|---|---|
| Aloe maculata | Forssk., sinônimo de Aloe vera | [Aloe maculata All., espécie aceita distinta](https://powo.science.kew.org/taxon/77122815-1) |
| Aloe variegata | Forssk., sinônimo de Aloe vera | [Aloe variegata L., sinônimo de Gonialoe variegata](https://powo.science.kew.org/taxon/530009-1) |
| Ficus clusiifolia | Summerh., sinônimo de Ficus elastica | [Ficus clusiifolia Schott, espécie aceita distinta](https://powo.science.kew.org/taxon/852625-1) |
| Ficus cordata | Kunth & C.D.Bouché, sinônimo de Ficus elastica | [Ficus cordata Thunb., espécie aceita distinta](https://powo.science.kew.org/taxon/852662-1) |

Consulta complementar real em 2026-09-11, somente textual. Esses quatro nomes históricos estão presentes na seção primária como homônimos posteriores ilegítimos. Remover a autoria, como exige a chave binomial, torna indistinguíveis os nomes ligados a táxons diferentes. Não há colisão entre as 12 classes, mas isso não resolve a ambiguidade demonstrada. Os outros táxons desta tabela são evidência de conflito, não novas espécies do produto, candidatos ou referências órfãs a inserir no manifesto.

Aplica-se a cláusula congelada: "Fonte indisponível, nome ambíguo, sinonímia conflitante, gênero/cultivar sem espécie ou dois itens humanos para o mesmo táxon bloqueiam a entrega na mesma U-201." O change-policy da decisão corrigida permanece implementation_detail; a política humana é compatível, mas a conferência de dados revelou esta fronteira. U-201 tem entrada de escopo registrada, porém permanece aberta quanto à ambiguidade e ao aceite dos bytes. P05 fica blocked, incompleto; não houve alteração de plano/spec ou replanejamento. A quantidade 83 é a população preliminar estrutural, não um conjunto taxonômico final aprovado.

Os hashes do manifesto e roster a submeter à revisão são registrados abaixo e em SHA256SUMS. P05 não pode ser completed enquanto faltar esse aceite.

Manifesto SHA-256: `39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5`.
Roster SHA-256: `350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b`.
