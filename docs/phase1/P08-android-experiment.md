# P08 — consolidação do ensaio privado Float32 e diagnóstico das exportações

Esta rodada foi autorizada para adaptar a prova offline em modo de teste explícito,
validar o Float32 existente no Redmi A5 e diagnosticar as exportações menores.
Não houve treinamento, aquisição de fotografias, promoção canônica, build pago,
release ou ação Git. Os oito caminhos da entrega de treinamento anterior foram
preservados byte a byte, juntamente com suas evidências e ambientes. Este documento
é a atualização posterior; não reescreve o protocolo ou os resultados anteriores.

## Pipeline e pré-processamento

A [execução de treinamento](P08-private-training-experiment.md) continua sendo
MobileNetV2 congelado + Dense12, com 18 imagens de treino, seis de avaliação e
um acerto nas seis avaliadas. Não foi repetida ou ajustada. Os 24 rótulos são
provisórios; não há confirmação pericial ou independência demonstrada.

O único modelo autorizado para a prova é o Float32 de SHA-256
`82c7bab4de164c70cd97e6651397ab19078437852ea8f2246d99ebdd2dafbf3c`.
O arquivo ordenado de 12 rótulos tem SHA-256
`0299f64143a228cc0268ee8f92917ccb71f0e9971b3396dc5bb7cb12785a3c47`.
A entrada é Float32 `[1,224,224,3]`, RGB 0..255. A escala -1..1 está dentro do
modelo e não pode ser aplicada novamente. A saída é Float32 `[1,12]`, na ordem
dos índices 0..11 do manifesto das espécies.

A prova antiga usa uint8 e resize por vizinho mais próximo; reutilizar esse
pré-processamento criaria outra entrada. Por isso o ensaio prepara privadamente
24 tensores little-endian com o mesmo Pillow bilinear do pipeline, sem alterar
ou recodificar as imagens. O decoder JavaScript reproduziu exatamente os bytes
dos 24 tensores e conferiu modelo, rótulos e referências. Essa estratégia valida
a interface de inferência, não um novo pipeline de câmera/redimensionamento.

O aplicativo requer `EXPO_PUBLIC_P08_EXPERIMENTAL_PROOF=1` e o ID do pacote
privado. É incompatível com a ativação simultânea da prova PT05. O fluxo normal,
AppMain, tela PT05, modelo e assets antigos ficam preservados. Os novos modelos,
tensores, rótulos privados e resultados não são empacotados ou versionados.
A tela lê somente os arquivos privados previamente transferidos por USB.

O protocolo compara os 24 vetores com a referência do computador, usando erro
absoluto máximo 0,0001, e repete um tensor 20 vezes após dois aquecimentos. A
estabilidade usa erro máximo 0,000001. Mediana/p95/mínimo/máximo são tempos do
relógio monotônico JavaScript ao redor da chamada nativa aguardada, excluindo
leitura e pré-processamento; não são tempos exclusivos de kernel nem métricas
de qualidade botânica. Não foi inventado um orçamento de latência.

## Diagnóstico com os mesmos pesos e entradas

| Exportação | Erro máximo contra Keras | Limite anterior | Concordância Top-1 técnica |
|---|---:|---:|---:|
| Float32 | 0,000007093 | 0,0001 | 24/24 |
| Float16 | 0,020740211 | 0,02 | 24/24 |
| INT8 | 0,386428505 | 0,15 | 23/24 |

Esses limites foram critérios de engenharia fixados no ensaio anterior, não
limites oficiais de acurácia. A concordância compara runtimes, não espécies.
As tolerâncias não foram relaxadas e os artefatos originais não foram modificados.

No Float16, uma ablação controlada converteu de volta a armazenamento Float32
as 108 constantes half, conservando exatamente seus valores já arredondados e
removendo somente a desquantização correspondente. As saídas foram idênticas às
do Float16 nos 24 casos (erro 0). O erro contra o Float32 original permaneceu
0,020747304. Isso isola, neste conjunto, o efeito dos valores arredondados das
constantes. Não demonstra um defeito de implementação que justifique corrigir
o exportador ou aprovar esse artefato.

No INT8, conferiram-se entrada uint8 com escala 1/zero 0 e saída com escala
1/256/zero 0: a codificação e a leitura das probabilidades estão corretas.
O resize produz RGB inteiro 0..255 e a normalização permanece embutida. A
calibração continua restrita às 18 imagens de treino. A comparação de 66
ativações correspondentes mostrou erros de até 0,003922 na normalização,
1,381168 no pooling e 2,837323 nos logits, antes do softmax. Há valores Float32
fora de intervalos representáveis em alguns tensores, inclusive de treino;
contagens estritas também podem incluir arredondamentos nas bordas. Isso não
prova isoladamente uma falha da calibração, e zeros de ReLU não foram tratados
automaticamente como clipping. A evidência sustenta erro acumulado de
quantização, sem demonstrar um bug de entrada ou de conversão da saída.

Float16 e INT8 continuam **reprovados por paridade numérica**. A ablação é um
artefato diagnóstico privado, não uma nova exportação candidata. Não houve busca
de parâmetros pelo holdout, nova calibração, treinamento ou alteração dos modelos.
Referências: [Float16 no LiteRT](https://developers.google.com/edge/litert/conversion/tensorflow/quantization/post_training_float16_quant),
[quantização inteira](https://developers.google.com/edge/litert/conversion/tensorflow/quantization/post_training_integer_quant),
[interface fast-tflite 2.0.0](https://github.com/mrousavy/react-native-fast-tflite/blob/v2.0.0/src/TensorflowLite.ts).

## Android: evidências reais e interrupção

O ADB inicialmente informou `unauthorized`; posteriormente houve autorização
e identificação do Redmi A5, modelo 25028RN03L, Android 15. O pacote privado foi
transferido para o sandbox do Development Client existente, sem substituir APK
ou modelo anterior. Foram lidos de volta e conferidos os SHA-256 dos 27 arquivos:
modelo, rótulos, manifesto e 24 tensores.

A primeira tentativa parou antes de solicitar inferência porque o campo global
legado `mobile_data` permanecia em 1. A reprodução comprovou que o Android 15
alterava `mobile_data<subId>` para 0 na assinatura ativa, mantendo o legado em 1.
O runner foi corrigido para conferir e restaurar o indicador da assinatura real;
continua exigindo Wi-Fi desativado, dados ativos desativados e ausência de rede
padrão. Também foi corrigida a confirmação dos hashes: `adb exec-in` envia stdin,
mas não confirma stdout remoto; a verificação agora lê todos os hashes por
`exec-out` e rejeita retorno vazio, parcial ou divergente.

Na segunda tentativa, os hashes e o estado offline passaram, mas a conexão USB
foi perdida após solicitar a abertura do Development Client. Não foi recebido
um resultado da tela experimental. **Carregamento nativo, inferência, paridade
computador/aparelho, estabilidade e latência físicas não estão validados.** A
existência de inferência durante a interrupção não pode ser confirmada.

A primeira tentativa restaurou os rádios e reversões. A segunda tentou restaurar
todos eles, porém o aparelho já estava ausente; Wi-Fi/dados permanecem com
restauração **não confirmada**. Os valores anteriores eram habilitados. Os
timeouts de consulta e restauração foram limitados para evitar longas esperas
após perda de USB. Logs, checksums, snapshots e falhas ficam privados; não foram
apagados nem transformados em sucesso.

O bundle Android/Hermes dos bytes finais da tela compilou na cópia privada
isolada. Somente os três assets históricos da prova PT05 foram exportados;
nenhum dos novos artefatos ou tensores privados entrou no bundle. O transporte
local Windows→Metro no WSL **falhou** na verificação separada: o servidor estava
pronto dentro do WSL, porém não era alcançável pelo Windows em 127.0.0.1:8081.
Uma tentativa com o Node existente do Windows também não confirmou prontidão
nesse endereço e foi encerrada. Nenhum proxy ou configuração global foi criado.
O runner agora bloqueia antes de alterar os rádios se o host Windows do ADB não
conseguir alcançar o Metro. A integração desse transporte permanece pendente;
não houve teste físico concluído.
Os testes novos cobrem contratos, falhas de paridade/estabilidade, ablação,
assinatura móvel, confirmação completa dos hashes, ausência de efeitos com USB
não autorizado, restauração após falhas e timeouts limitados. As suítes anteriores
continuam reutilizadas com seus fingerprints, sem nova execução.

## Retomada e pendências

A ação manual necessária é reconectar o Redmi por USB, desbloqueá-lo e aceitar
a chave de depuração se solicitada. No PowerShell do Windows:

```powershell
adb devices -l
adb shell svc wifi enable
adb shell svc data enable
```

O estado deve ser `device`; os dois últimos comandos restauram os valores
habilitados documentados antes da interrupção. Se o USB ainda não funcionar,
os mesmos rádios podem ser reativados pelos controles do aparelho.

Após recuperar a conexão e os rádios, o runner existente nesta entrega executa
a prova somente quando a disponibilidade do Metro no host do ADB estiver
resolvida, reutilizando os arquivos e conferindo todos os hashes:

```bash
"$TRAINING_PYTHON" scripts/phase1/run_p08_android.py \
  --adb "$WINDOWS_ADB_EXE" --app "$ISOLATED_APP" \
  --bundle "$PRIVATE_BUNDLE" --evidence "$NEW_PRIVATE_EVIDENCE_DIRECTORY"
```

Os valores exatos desses caminhos e o comando pronto ficam no material privado.
A saída deve ser nova, sem sobrescrever a tentativa interrompida. O runner não
instala APK, não baixa dados, não treina nem toma um Metro/port mapping alheio.
Antes de repetir a prova, a restauração interrompida precisa ser resolvida.

Mesmo uma prova física futura aprovada demonstrará somente execução técnica.
Continuam os limites do recorte de 24 imagens, rótulos provisórios, seis espécies
sem avaliação separada, ausência das classes de proteção, arquitetura ainda não
comparada e requisitos originais U-803/U-804/P08. Guard, B1 resolvido, contadores,
dataset, avaliações e os arquivos operacionais permanecem preservados. Não há
aprovação canônica, publicação de imagens, substituição do modelo normal ou release.

## Checkpoint para continuação em outro computador

O responsável solicitou salvar agora o projeto no GitHub para continuar no
computador da faculdade. Esta publicação registra **trabalho experimental parcial**,
sem aceite inventado do modelo ou do guard. A versão proposta inclui os oito
caminhos anteriores intactos, o modo de teste e seus contratos, diagnóstico,
runner, testes novos e esta consolidação. O inventário integral fica no material
privado e liga cada caminho ao SHA-256 de seus bytes; guard e 51 arquivos
operacionais ficam fora do staging.

As próximas ações são recuperar a conexão e os rádios, resolver o transporte
local Metro/ADB e executar a prova com evidências novas. Não é necessário repetir
treinamento, avaliações humanas ou downloads de fotografias. O GitHub contém
somente código/documentação sanitizados: o catálogo, as imagens, o modelo, os
tensores e logs continuam privados e precisam acompanhar a retomada por meio
privado. A cópia existente desses materiais foi preservada no computador atual.
