# P08 — critério do catálogo experimental privado

Em 15/10/2026, o responsável autorizou expressamente substituir a confirmação
botânica pericial por rotulagem provisória documentada, exclusivamente para uso
acadêmico experimental privado. Esta é uma alteração material do critério do
projeto, não do Método Bianchini 3.2.0 ou de seu overlay. A classificação somente
de leitura de `bm.py change-policy --public-contract-change --critical-invariant`
foi `material_change`; este suplemento registra o escopo autorizado diretamente,
sem refazer o plano, o snapshot aprovado ou as transições do guard.

O [plano aprovado](../bianchini/changes/v2/plans/P08-dataset-recovery.md) e a
[especificação aprovada](../bianchini/changes/v2/specs/p08-dataset-recovery-change.md)
permanecem intactos como histórico. A substituição vale somente para o catálogo
separado descrito aqui. Não representa aprovação retroativa do gate pericial,
conclusão de U-803/U-804/P08 ou promoção dos estados canônicos antigos. O guard,
B1 resolvido na rodada 1 e as provas históricas permanecem preservados.

## Critério autorizado

Cada rótulo exige uma declaração científica explícita sobre o arquivo, na
descrição preservada da fonte, correspondente ao nome canônico ou a um sinônimo
documentado no manifesto `offline-class-manifest.v1.json` 1.1.0. O catálogo registra
o trecho, revisão, localizador, digest da evidência, correspondência taxonômica,
fundamento e incerteza. Busca, título, nome comum, categoria isolada e sugestão de
IA não bastam. Não se corrige grafia divergente nem se escolhe entre alvos
conflitantes por inferência. Casos insuficientes ficam fora dos rótulos admitidos;
não são convertidos em classes de proteção.

O status do rótulo é `provisional_source_supported`, de comparação documental
pelo agente. Não é parecer humano sobre espécie, confirmação pericial ou garantia
da identificação do espécime. Não são preenchidos `expert_confirmation` ou
`human_validated`. A possibilidade de erro da declaração da fonte permanece
explicitamente registrada em cada item.

Direitos, autoria, atribuição, avisos, integridade, qualidade, privacidade e
duplicidade continuam independentes. As concessões individuais e decisões reais
já existentes cobrem preservação, quarentena e avaliação privada deste material;
não constituem liberação global da fonte ou autorização para treinamento e
publicação. A licença da fotografia não é estendida aos textos/metadados da página.
Sinais de série não são decisões de duplicidade, e ausência de sinal de hash/dHash
não constitui parecer humano de independência.

## Resultado desta aplicação

O catálogo privado referencia os 99 originais e as 92 sanitizadas já existentes,
sem copiar ou reescrever imagens. A auditoria de rótulos abrangeu as 68 imagens com
nitidez, iluminação e clareza do alvo aceitas na galeria e as observações parciais
anteriores de E1/E2, preservadas com seus vínculos próprios, sem nova avaliação.
Foram admitidos 39 rótulos provisórios: 38 dessas 68 imagens e E2. E1 permanece sem
sustentação científica suficiente na descrição, sem invalidar suas observações.

| Espécie | Rótulos sustentados | Sem sinal de série pendente |
|---|---:|---:|
| Epipremnum aureum | 2 | 2 |
| Monstera deliciosa | 2 | 2 |
| Zamioculcas zamiifolia | 1 | 1 |
| Spathiphyllum wallisii | 15 | 1 |
| Dracaena trifasciata | 2 | 0 |
| Aloe vera | 4 | 4 |
| Chlorophytum comosum | 5 | 5 |
| Codiaeum variegatum | 1 | 1 |
| Ficus elastica | 0 | 0 |
| Kalanchoe blossfeldiana | 3 | 3 |
| Nephrolepis exaltata | 0 | 0 |
| Tradescantia zebrina | 4 | 2 |
| **Total** | **39** | **21** |

Os outros 31 casos examinados foram excluídos dos rótulos provisórios: 22 por
evidência científica insuficiente, quatro por dois alvos científicos não
desambiguados, três por descrição incompatível com a classe proposta, um por
grafia sem equivalência documentada e um por alegação infraespecífica não
conciliada. Os demais 29 mantêm os impedimentos anteriores: oito rejeições de
qualidade, 12 duplicatas técnicas, sete formatos rejeitados e dois alvos pouco
claros. Não há exemplos de proteção. As classes sem rótulo sustentado são
`species_09` e `species_11`; isso não demonstra ausência das espécies na fonte.

Em 18 dos 39 rótulos há sinal documental de três séries fotográficas, com autoria,
data, descrição e sequência de títulos correspondentes. A eventual seleção dessas
imagens ainda exige resolução real de duplicidade. As outras duas séries do lote
afetam somente casos já fora dos rótulos admitidos. A comparação de hashes e das
métricas dHash existentes contra as 92 sanitizadas e as 17 referências P07 não
encontrou novo sinal algorítmico nos 39 rótulos admitidos; não houve nova inspeção
das fotografias.

Os 39 estão aptos à análise documental do catálogo provisório, mas **zero estão
declarados prontos para execução de experimento**: faltam os aspectos finais de
qualidade e privacidade não fornecidos nas avaliações existentes. As pendências
incluem fotografia/espécime vivo, detalhe diagnóstico, montagem/texto dominante e
sinais sensíveis ou identificáveis; aceites já fornecidos não serão repetidos.
Nas 18 imagens das séries, falta também a decisão sobre as relações indicadas.
Não foi estabelecida quantidade mínima, suficiência científica, desempenho ou
partição. Treinamento e uso público continuam não autorizados.

## Rastreabilidade e preservação

O catálogo completo e sua evidência individual ficam exclusivamente fora do Git.
SHA-256 de `catalog.json`:
`0e734580b745c79078a68dce02754bc66ea159c419650ef349b5c45355edf9a3`.
SHA-256 do inventário privado `SHA256SUMS`:
`3c57864a85590ca23b7df1d98e8504f8d6e834fdfb30f055c7642ee0e786f951`.
O pacote contém a autorização, o catálogo, orientação de leitura, inventário
anterior do canônico e validação limitada. Referências e hashes ligam cada item
ao original, à sanitizada disponível, à fonte, aos direitos e às avaliações
efetivamente existentes, sem ampliar seus escopos.

A validação conferiu os 191 objetos originais/sanitizados, os SHA1 declarados dos
99 originais, as evidências de direitos e os vínculos das avaliações. Os 552
arquivos canônicos, seus bytes, permissões e mtimes permanecem iguais, incluindo
configuração, journal, decisões e imagens. As métricas e evidências técnicas
válidas foram reutilizadas; não houve alteração de código nem repetição de
suítes. O resumo canônico continua com zero aprovadas/usable. Não houve rede,
aquisição, treinamento, staging, commit, push ou exclusão.

## Consolidação posterior do recorte

Os resultados e digests acima preservam a primeira aplicação deste critério como
histórico. As observações humanas complementares, a escolha autorizada de uma
representante por série e a recuperação documental de identificação foram
consolidadas posteriormente em um catálogo privado de 24 imagens, distribuídas
pelas 12 espécies. A última avaliação visual está vinculada à sanitizada exibida;
não confirmou a identidade botânica. Há 18 referências reservadas e 58 exclusões
ou impedimentos preservados no lote de 100 arquivos obtidos. Os outros registros
canônicos não recebem novas avaliações por esse aceite.

O manifesto privado final do recorte tem SHA-256
`6253fe5cd88db3adb1c9361d00e95207be329c5eef86d81885ceea4757b22fd1`.
Ele vincula os bytes das 24 referências, o catálogo, a observação real e o snapshot
canônico preservado. Seu aceite limitado ainda é proposto, não registrado. Não
afirma perícia, independência, suficiência, desempenho, aprovação canônica,
treinamento ou uso público. O manual e o ledger descrevem o estado consolidado;
o plano original e seu guard permanecem incompletos e inalterados.
