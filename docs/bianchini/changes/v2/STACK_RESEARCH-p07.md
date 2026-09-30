# Stack Research — P07

Research mode: targeted_web
Motivo: o repositório já usa Pillow, mas o P07 precisa fixar um método de nitidez e uma comparação perceptual reproduzível; a semântica das APIs de imagem e do dHash merece confirmação primária. Pesquisa restrita a essa decisão, sem instalação.

## Stack detectada

- Python 3.14.4 observado no host; `scripts/phase1/requirements-p06.txt` fixa Pillow 12.3.0. `acquire_commons.py` já usa Pillow para decodificação e grava imagens externas. Testes Python seguem `unittest` e fixtures sintéticas em `scripts/phase1/test_acquire_commons.py`.
- O conjunto externo P06 contém 17 JPEGs em `quarantine/`, `state.json`, `manifest.jsonl`, `coverage.json`, `inventory.json`, `SHA256SUMS` e 17 decisões em `review-2026-09-28/human-decisions.json`. Os arquivos externos não são insumos do snapshot Git.
- Sem dependência local NumPy, SciPy, OpenCV ou ImageHash declarada. `.github/workflows/deploy.yml` não fornece gate de curadoria.

## Fontes primárias

- Fonte primária: Pillow 12.3.0, `Image` e conceitos de resize/decodificação.
  URL: https://pillow.readthedocs.io/en/stable/reference/Image.html
  Acessado em: 2026-09-30. Aplicação: abrir/carregar JPEG, converter para luminância de 8 bits e redimensionar com `Resampling.LANCZOS`, sem salvar os pixels processados como imagem de origem.
- Fonte primária: Pillow 12.3.0, `ImageStat`.
  URL: https://pillow.readthedocs.io/en/stable/reference/ImageStat.html
  Acessado em: 2026-09-30. Aplicação: estatística de luminância/exposição; a documentação confirma média e variância por banda.
- Fonte primária: implementação upstream de `dhash` no projeto ImageHash, de Johannes Buchner.
  URL: https://github.com/JohannesBuchner/imagehash/blob/master/imagehash/__init__.py
  Acessado em: 2026-09-30. Aplicação: comparação horizontal entre colunas adjacentes após redução para 9×8 em cinza. É referência para o algoritmo, não dependência a instalar.
- Fonte primária: README upstream do ImageHash.
  URL: https://github.com/JohannesBuchner/imagehash
  Acessado em: 2026-09-30. Aplicação: hashes perceptuais sinalizam similaridade visual e distância de Hamming, sem equivaler a identidade; o upstream registra que `dhash` horizontal difere da variante vertical histórica.

## Decisões aplicadas

- **Pillow 12.3.0 é suficiente**: abertura/decodificação, pixels RGB/L, resize e estatísticas. SHA-256, JSON estrito, timestamps e Hamming vêm da biblioteca padrão. Não adicionar NumPy, SciPy, OpenCV ou ImageHash para 17 imagens.
- Nitidez de triagem: após conversão para `L` e resize 256×256 com LANCZOS, calcular em inteiros o Laplaciano assinado `4c − esquerda − direita − acima − abaixo` nos 254×254 pixels interiores e sua variância populacional. Fixar versão do algoritmo, Pillow, tamanho, fórmula e valor; `variance < 100` gera **sinal para revisão**, nunca rejeição. A métrica é sensível a textura/composição e não certifica foco.
- Exposição: na mesma luminância 256×256 registrar média e frações de pixels `≤ 15` e `≥ 240`; sinalizar média `< 40` ou `> 215`, ou fração de extremos `≥ 0,25`. Dimensão mínima `< 224` e proporção maior/menor lado `> 3,0` também são sinais, não vetos. Todos os limiares são heurísticos de triagem explícitos e testados em fixtures sintéticas nos pontos de fronteira; não são alegações de qualidade universal.
- dHash horizontal v1: `L` redimensionado para 9×8 com LANCZOS, 64 bits em ordem de linhas, bit 1 quando pixel à direita é estritamente mais claro que o da esquerda. Distância Hamming = `bit_count(hash_a XOR hash_b)`. SHA-256 igual é duplicata exata; para bytes diferentes, distância `0–6` é **candidato a quase duplicata**, `7–10` é **limítrofe para inspeção**, `11–64` sem sinal automático. Comparar todos os 136 pares dos 17 IDs, guardar pares, hashes, distâncias e limiares. Mesmo distância 0 não descarta automaticamente; crop, rotação, cor e composição podem enganar. O revisor resolve pares e colisões.
- Enquadramento, oclusão, múltiplas espécies, representatividade, identificáveis privados e identidade botânica exigem observação humana; nenhuma heurística concede `approved_for_dataset`. A revisão deve citar evidência suficiente ou manter `needs_botanical_review`/`needs_human_review`.

## Alternativas rejeitadas

- pHash/DCT via NumPy/SciPy ou ImageHash instalado: dependências extras sem necessidade comprovada para 17 imagens e sem ganho que dispense decisão humana.
- Rejeição automática por limiar de nitidez, exposição ou dHash: falso positivo possível; viola o contrato de revisão humana.
- Detecção automática de rosto/placa: exigiria modelo/dependência e ainda não substituiria revisão humana de privacidade.

## Riscos e lacunas

- Os limiares são política de **triagem**, não thresholds validados em corpus botânico; somente a execução com as 17 imagens e o parecer humano avaliarão adequação. Fixtures sintéticas testam determinismo/fronteiras, não acurácia botânica.
- Pillow pode variar entre versões; gravar `Pillow==12.3.0`, versão do algoritmo e hashes no resultado. Nenhuma imagem P06 deve ser recodificada, movida ou escrita.
