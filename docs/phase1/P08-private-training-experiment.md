# Aditamento: treinamento experimental privado do recorte aceito

A autorização explícita do responsável nesta sessão amplia o uso das 24 imagens
do recorte aceito e publicado em `d47cb6b69a3bb896fdcfd32907c1931b8f0771ec`
para treinamento e exportação **experimentais privados**. O manifesto aceito é
`6253fe5cd88db3adb1c9361d00e95207be329c5eef86d81885ceea4757b22fd1`.
Este aditamento substitui somente a proibição anterior de treinamento desse
recorte. Não reabre coleta ou avaliações e não altera o catálogo aceito, os
rótulos provisórios, o plano original, o Método Bianchini 3.2.0 ou seu overlay.
Não aprova o gate pericial antigo, U-803/U-804 ou P08. O guard congelado, B1
resolvido na rodada 1 e seus contadores permanecem preservados. A validação
desta execução é técnica, separada da aprovação formal do guard.

São autorizados apenas ambiente isolado, dependências/pesos públicos com
proveniência e licença registradas, leitura das 24 referências aceitas e gravação
de resultados externos privados. Não há autorização para publicar imagens ou
modelos, contratar serviço, substituir o modelo do aplicativo ou fazer release.
Nenhum estado canônico é promovido. Dados, imagens, atribuições, observações e
históricos existentes são somente lidos. Não há staging, commit ou push.

## Protocolo fixado antes da execução final

A [estratégia existente](../PLANO_CANONICO_IA_HIBRIDA.md) prevê EfficientNet-Lite0
e comparação com MobileNetV2, exportação e medição em aparelho físico. Esta rodada
executa apenas a baseline MobileNetV2, sem escolher uma arquitetura vencedora.
O ambiente de aquisição anterior não contém bibliotecas de treinamento; usa
Python 3.14. Um novo ambiente externo usa CPython 3.12.11, TensorFlow CPU 2.20.0,
Keras 3.11.3, NumPy 2.2.6 e Pillow 11.3.0. O lock registra todas as dependências
e hashes dos wheels efetivamente instalados para Linux x86_64.

O pipeline aceita exclusivamente o manifesto e o catálogo aprovados e exige um
registro privado da autorização adicional de treinamento. Confere a identidade
dos 24 candidatos, referências e hashes originais/sanitizados, classes e rótulos.
As demais entradas do catálogo são lidas apenas para reconstruir relações entre
grupos; suas imagens nunca entram no treinamento. Relações de série explícitas,
representantes e hashes iguais são unificados transitivamente antes da divisão.
Conflitos de rótulo dentro de um grupo impedem a execução.

O seed é `20261015`. Para cada espécie com pelo menos dois grupos, um grupo
inteiro é reservado deterministicamente para avaliação; os outros ficam no
treino. Uma espécie com um só grupo fica exclusivamente no treino. Ausência de
relação conhecida não demonstra independência. As referências reservadas não
são incorporadas; suas relações ficam registradas. Neste recorte são 18 imagens
de treino e seis de avaliação, sem conjunto de teste adicional. Não há
augmentation, duplicação para preencher classes nem exemplos de proteção.

Usa-se MobileNetV2 alpha 1.0, sem topo ImageNet, com pesos oficiais do Keras e
pooling médio; todo o extrator fica congelado e é chamado com `training=False`.
A única parte treinada é uma camada densa de 12 saídas softmax. São 50 épocas,
Adam com learning rate 0,01 e lote completo das 18 imagens de treino, sem
early stopping, ajuste pelo holdout ou seleção de checkpoint/hiperparâmetros.
RGB é redimensionado somente em memória por bilinear para 224×224. A interface
Float32 recebe valores 0..255 e incorpora a escala para -1..1. A ordem das saídas
é exatamente a dos índices 0..11 das espécies no manifesto 1.1.0. Não é a
interface de 14 classes do produto, nem fornece rejeição de entradas desconhecidas.

São preservados Keras e SavedModel e tentadas exportações TFLite Float32,
Float16 e INT8. A calibração INT8 usa somente imagens de treino. Recarregamento,
formatos, shapes, dtypes, quantização, probabilidades e vínculo com `labels.json`
são verificados. Os limites prévios de diferença absoluta nas probabilidades
são 0,0001/0,02/0,15, respectivamente. Float32 é a exportação mínima obrigatória;
uma exportação opcional que ultrapasse seu limite é registrada como reprovada,
sem relaxá-lo. Concordância entre runtimes é verificação técnica, não desempenho
botânico. Acerto no treino não é apresentado como evidência de desempenho.

## Reprodução e evidências

Implementação: `scripts/phase1/train_experimental.py`; testes focais:
`scripts/phase1/test_train_experimental.py`. O lock é
`scripts/phase1/requirements-training.lock`. Um ambiente novo pode ser preparado
com Python 3.12.11 e:

```bash
export KERAS_HOME="$EXPERIMENT_ROOT/keras-home"
export PYTHONNOUSERSITE=1 PYTHONHASHSEED=20261015 TF_ENABLE_ONEDNN_OPTS=0
python3.12 -m venv "$EXPERIMENT_ROOT/.venv"
"$EXPERIMENT_ROOT/.venv/bin/python" -m pip install \
  -r scripts/phase1/requirements-training.lock
"$EXPERIMENT_ROOT/.venv/bin/python" -m unittest discover \
  -s scripts/phase1 -p test_train_experimental.py
"$EXPERIMENT_ROOT/.venv/bin/python" scripts/phase1/train_experimental.py \
  --manifest "$ACCEPTED_PRIVATE_MANIFEST" \
  --authorization "$PRIVATE_TRAINING_AUTHORIZATION" \
  --weights "$OFFICIAL_LOCAL_WEIGHTS" \
  --weights-sha256 f8aff69536bd77a692c594f559c798c19bf7f3f36668fc9fa00b21c6aab4797c \
  --output "$EXPERIMENT_ROOT/new-run" --epochs 50
"$EXPERIMENT_ROOT/.venv/bin/python" scripts/phase1/train_experimental.py \
  --manifest "$ACCEPTED_PRIVATE_MANIFEST" \
  --authorization "$PRIVATE_TRAINING_AUTHORIZATION" \
  --verify-run "$EXPERIMENT_ROOT/new-run"
```

As variáveis apontam para material privado existente, não para novos downloads
de fotografias. A saída deve ser nova, fora do repositório, dataset e pacote
aceito; nunca é sobrescrita. O registro de autorização contém
`data_manifest_sha256`, `training_authorized=true`, `private_only=true`,
`public_use_authorized=false` e a instrução real em `owner_instruction`.
Não é produzido automaticamente como um parecer humano ou autorização genérica.

Os pesos locais são o arquivo oficial
`mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5`, obtido de
`https://storage.googleapis.com/tensorflow/keras-applications/mobilenet_v2/`.
O dossiê privado conserva URL, digest, momento e avisos do download, código
correspondente do Keras, declaração MIT do pacote Keras-Applications, origem
dos checkpoints TensorFlow Slim e avisos Apache-2.0/MIT aplicáveis. Essas
declarações não concedem licença sobre as imagens do ImageNet nem constituem
parecer jurídico global ou autorização de redistribuição do modelo resultante.
Referências oficiais: [Keras MobileNet](https://keras.io/api/applications/mobilenet/),
[Keras-Applications](https://pypi.org/project/Keras-Applications/1.0.8/),
[origem dos checkpoints](https://github.com/tensorflow/models/tree/master/research/slim/nets/mobilenet),
[instalação TensorFlow](https://www.tensorflow.org/install/pip).

Cada execução preserva divisão e grupos privados, autorização, ordem de rótulos,
perdas de treino, previsões do holdout, exports e seus erros numéricos, hashes
do código, lock, dados e pesos. Um inventário dos artefatos permite recarregar
em processo novo e detectar alteração. Snapshot antes/depois cobre todos os
bytes, mtimes e permissões canônicos; uma execução interrompida não recebe
inventário de conclusão e não altera o dataset. Dependências, licenças e logs
de instalação ficam no ambiente externo; nenhuma proveniência de fotografia
entra no Git.

## Limites e encaminhamento

O treino de 50 épocas foi concluído, com **1 acerto em seis imagens de avaliação**
(16,7%), sem usar essas imagens para ajustar o modelo. Esse denominador é pequeno
demais para sustentar uma estimativa de desempenho. Os 20 testes focais passaram;
um processo novo recarregou Keras, SavedModel e os três TFLite, verificou o
inventário e repetiu as verificações técnicas de entrada, saída e rótulos.

| Exportação | Bytes | Maior desvio nas probabilidades | Resultado numérico |
|---|---:|---:|---|
| TFLite Float32 | 8.931.960 | 0,000007093 | Passou o limite 0,0001 |
| TFLite Float16 | 4.499.924 | 0,02074021 | Reprovada: limite 0,02 |
| TFLite INT8 | 2.731.576 | 0,38642851 | Reprovada: limite 0,15 |

As três carregam e têm as dimensões esperadas; isso não transforma as duas
reprovadas em exportações aceitas. O artefato entregue para inferência técnica
é Float32, SHA-256
`82c7bab4de164c70cd97e6651397ab19078437852ea8f2246d99ebdd2dafbf3c`.
Entrada `[1,224,224,3]` Float32 RGB 0..255; saída `[1,12]` Float32 softmax.
O inventário privado dos artefatos finais tem SHA-256
`e60d5d1f61b6f2fae774e16fe446d6c6165f0b66482f34621fc58033db2ae2e8`.

A tentativa inicial e seus logs foram preservados: uma referência nula de
arquivo em registro excluído foi corrigida antes do treino; a primeira execução
foi interrompida pelo Float16 fora da tolerância. O tratamento foi corrigido
para registrar honestamente uma exportação opcional reprovada, preservando o
Float32 obrigatório e sem alterar tolerâncias. A execução final repetiu o mesmo
seed, dados, divisão e hiperparâmetros; não houve escolha entre modelos baseada
na avaliação. Também foi bloqueado o uso de `..` para contornar a proteção da
pasta de saída. Os testes cobrem essas correções e os limites do novo pipeline.

Os 563 arquivos canônicos permaneceram com bytes, mtimes e permissões iguais.
O ambiente anterior, os 51 arquivos operacionais locais, guard e HEAD foram
preservados. Não se repetiram suítes do coletor ou avaliações humanas. Evidência
agregada: `artifacts/phase1/p08/private-training-summary.json`; resultados,
predições individuais, avisos, autorização e comandos exatos ficam privados.

A avaliação cobre somente seis espécies,
com um exemplo por espécie; as seis espécies com uma imagem não permitem
avaliação separada. Não há confirmação pericial, independência demonstrada,
suficiência amostral, medição no aparelho, proteção contra entradas fora do
conjunto, calibração ou autorização pública. Antes de qualquer avanço de produto,
permanecem necessárias ampliação autorizada e avaliação adequada do conjunto,
decisão sobre os gates originais, comparação de arquiteturas e validação de
classes de proteção, interface, latência e memória no dispositivo. Nada disso
é declarado realizado pelo presente experimento.
