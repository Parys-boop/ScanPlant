# F1-MAN01 — contrato offline 1.0.0

Estado: implementação documental preliminar bloqueada em U-201 por quatro
binomiais homônimos; revisão humana dos bytes finais pendente.
O manifesto não está liberado para consumo por produto ou treinamento.

## Entrada, identidade e ordem

A decisão humana corrigida de U-201 está transcrita em
`artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md` e materializada
em `approved-species-roster.json` no mesmo diretório. O registro usa a data UTC
real e o papel responsável humano. A antiga enumeração de sinônimos foi revogada;
não constitui allowlist. O digest histórico do planejamento continua
`246eb9a8178fd2c2a4033ac25a7972f85705919619205275b92fbb50a77eeae5`.

| Posição | Índice | class_id | Nome científico ou proteção | Rótulo pt-BR |
|---|---|---|---|---|
| 1 | 0 | species_01 | Epipremnum aureum | jiboia |
| 2 | 1 | species_02 | Monstera deliciosa | costela-de-adão |
| 3 | 2 | species_03 | Zamioculcas zamiifolia | zamioculca |
| 4 | 3 | species_04 | Spathiphyllum wallisii | lírio-da-paz |
| 5 | 4 | species_05 | Dracaena trifasciata | espada-de-são-jorge |
| 6 | 5 | species_06 | Aloe vera | babosa |
| 7 | 6 | species_07 | Chlorophytum comosum | clorofito |
| 8 | 7 | species_08 | Codiaeum variegatum | cróton |
| 9 | 8 | species_09 | Ficus elastica | falsa-seringueira |
| 10 | 9 | species_10 | Kalanchoe blossfeldiana | flor-da-fortuna |
| 11 | 10 | species_11 | Nephrolepis exaltata | samambaia-americana |
| 12 | 11 | species_12 | Tradescantia zebrina | lambari-roxo |
| 13 | 12 | outra_planta | proteção | Outra planta |
| 14 | 13 | imagem_invalida | proteção | Imagem inválida |

As primeiras cinco posições preservam o piloto; as sete novas seguem a ordem
alfabética aprovada. A ordem humana é determinística e não representa confiança,
prioridade ou parentesco. IDs opacos não derivam de nomes ou sinônimos. Nenhuma
ordenação automática posterior pode mudar os índices. As proteções não são espécies.

## Formato e resolução

`offline-class-manifest.v1.json` usa schema_version inteiro 1, manifest_version
string 1.0.0 e normalization_version string 1. O hash do roster corresponde aos
bytes exatos da entrada registrada. Objetos são fechados; tipos não são coercíveis.
JSON deve ser UTF-8 sem BOM, LF, com newline final, sem chaves duplicadas ou números
não finitos. Cada espécie contém nome científico binomial sem autoria, rótulo
pt-BR, nomes comuns, sinônimos referenciados e fontes taxonômicas datadas.

Normalização: NFC, trim, colapso de whitespace Unicode em espaço ASCII e casefold,
nesta ordem. Não remove acentos, pontuação ou autoria; não faz aproximação.
Controles não whitespace e formatação invisível são inválidos. Chaves repetidas,
mesmo na própria classe, são erro. Nomes comuns pertencem a outro namespace;
homônimos entre espécies seriam documentados, sem resolução científica implícita.
No roster real os 12 rótulos comuns são distintos.

As funções públicas em `scripts/phase1/validate_offline_manifest.py` são
`normalize_name(texto)` e `resolve_scientific_name(manifesto_validado, texto)`.
A segunda recebe um manifesto já validado; retorna class_id por igualdade exata,
ou None (null em uma serialização JSON) para texto desconhecido. Não retorna
proteção para ausência de correspondência. O catálogo de aliases se limita ao
escopo aprovado; não é um resolvedor taxonômico universal. Autorias e homônimos
nomenclaturais estão explicitados na revisão taxonômica para aceite humano.

Sinônimos provêm da seção direta Synonyms da espécie aceita no POWO. A evidência
relaciona cada nome, autoria, relação e exclusão; não herda sinônimos de variedades
ou subespécies. São 83 aliases binomiais preliminares; quatro têm ambiguidade
comprovada na revisão e não foram aceitos como chaves finais. Spathiphyllum wallisii tem lista vazia
justificada pela página consultada. Nenhum nome infraspecífico é alias.

## Proteções e consumidores futuros

`outra_planta` designa imagem utilizável de planta cuja identidade de referência
está fora das 12 espécies. Não é um nome de espécie nem consequência automática
de baixa confiança. `imagem_invalida` designa conteúdo sem planta ou sem informação
suficiente para atribuição botânica única: vazio, objeto não vegetal, enquadramento
insuficiente ou mistura sem alvo inequívoco. Bytes ilegíveis são erro de entrada.

Treino e inferência futuros deverão usar as mesmas 14 posições, IDs e SHA-256.
Catálogo futuro vinculará as 12 espécies por class_id e não inventará cuidados
para proteções. Nenhum consumidor, tensor, modelo ou fluxo híbrido é implementado.
Não há afirmação de acurácia, latência, compatibilidade medida com Redmi A5 ou
disponibilidade comprovada de imagens.

Versionamento: mudança estrutural altera schema_version; quantidade, identidade
ou ordem exigem major e aprovação de escopo; alteração da resolução de nomes
exige minor e revisão de colisões; metadados sem efeito na resolução podem ser patch.
Cada versão aceita fixa os hashes dos bytes, sem regeneração silenciosa.

## Validação reproduzível

Python 3.12, somente biblioteca padrão, cwd na raiz do workspace:

```bash
python3 -B -m unittest discover -s scripts/phase1 -p 'test_offline_manifest.py'
python3 -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json
sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS
git diff --check
```

A CLI não escreve arquivos, não usa rede ou cache. Exit 0 indica contrato válido;
1, contrato inválido; 2, invocação inválida ou arquivo inacessível. Diagnósticos
contêm código e caminho JSON sem eco de valores de entrada. Sucesso informa
contagens, versões e hashes. Os testes usam espécies sintéticas em memória e
arquivos temporários; não constituem corpus ou campanha de mutação.

Resultados individuais, comandos e hashes constam em `validation-report.json`.
SHA256SUMS cobre os sete artefatos contratados, sem incluir a si mesmo, estado ou
ledger. Conferência automática de formato não verifica a semântica botânica da URL.

## Fronteira de aceite

A aprovação humana recebida autoriza o escopo e a execução; não contém o aceite
dos bytes produzidos depois dela. A revisão final deve conferir 12/12 identidades,
cada alias/fonte, nomes comuns, ordem, IDs e proteções, e registrar approved/rejected,
papel, data e hashes de manifesto/roster. O executor não substitui esse parecer.
P05 permanece incompleto até esse gate.

As provas do overlay Codex são presas a um commit real. Como staging e commit foram
expressamente proibidos, não é possível atestar estas alterações não commitadas
por `review_guard.py proof`. Não há sidecar ou aprovação de convergência simulados.
As validações aqui registradas são da working tree. O plano congelado, as specs,
o snapshot de 23 arquivos e o digest histórico foram preservados. P01/P03-R6
continuam blocked-terminal, P02/P04 completed e release pending.
