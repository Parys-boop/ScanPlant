# Parecer de segurança — P01-R1-T01

**Veredito:** sem impedimento de segurança para a Tarefa 1. Não há finding que abra fix round.

## Escopo e evidência

- Brief: `.superpowers/bianchini/v1/p01/P01-R1-T01-brief.md`.
- Pacote revisado: `artifacts/bianchini/v1/reviews/P01-R1-T01.md`; commit `702aeb0` altera exclusivamente `ScanPlantAPI.Tests/MutationHarness/ExternalFallbackMutationHarnessTests.cs` (120 adições, 3 remoções).
- Invariantes aplicáveis: imagem limitada e validada por MIME, assinatura/formato e dimensões; ausência de consentimento impede chamada externa; não há persistência/reuso da imagem.
- Código adjacente examinado: `ExternalFallbackUploadValidator.cs`, `ExternalFallbackService.cs`, `PlantIdentificationController.cs`, `ExternalFallbackOptions.cs` e os testes já existentes do validador.

## Findings

| Severidade | Quantidade | Finding |
|---|---:|---|
| Crítica | 0 | — |
| Alta | 0 | — |
| Média | 0 | — |
| Baixa | 0 | — |

Não foram encontrados findings com cenário de exploração plausível no diff.

## Validação do boundary de upload

- O teste de limite exato aceita uma imagem de `MaxImageBytes` e confirma que o conteúdo validado mantém o tamanho completo (`ExternalFallbackMutationHarnessTests.cs:53-65`). Isto cobre a fronteira permitida do validador, cuja pré-checagem usa somente `>` (`ExternalFallbackUploadValidator.cs:52-55`).
- A leitura fragmentada limita cada solicitação de buffer a `MaxImageBytes + 1`, preserva todos os bytes e falha se o validador solicitar buffer maior (`ExternalFallbackMutationHarnessTests.cs:81-95`). Isso é coerente com a sentinela de um byte e com o chunk limitado do código produtivo (`ExternalFallbackUploadValidator.cs:98-115`), evitando regressão para leitura não limitada.
- O caso em que o tamanho declarado está no limite, mas o stream contém o primeiro byte adicional, exige `PayloadTooLarge` (`ExternalFallbackMutationHarnessTests.cs:97-108`). Portanto, uma manipulação do `DeclaredLength` não permite contornar a contagem da leitura efetiva: o acumulado é verificado antes de cada escrita (`ExternalFallbackUploadValidator.cs:105-112`).
- A aceitação de largura e altura exatamente máximas (`ExternalFallbackMutationHarnessTests.cs:67-79`) preserva o limite inclusivo e complementa a rejeição de dimensões acima dele. O decodificador ainda valida formato/MIME e decodifica pixels antes de retornar a imagem transitória (`ExternalFallbackUploadValidator.cs:70-93`).
- O harness mantém evidência de que consentimento ausente bloqueia o provider e que cancelamento/timeout não repetem chamadas (`ExternalFallbackMutationHarnessTests.cs:110-159`). A mudança não introduz rede, segredo, persistência, autorização nova ou alteração de rate limit.

## Áreas não analisadas

Não foram revisados adaptadores HTTP de PlantNet/Groq, configuração/secret store, política de rate limit em runtime, autenticação/JWT e infraestrutura de hospedagem: não são alterados por este diff e estão fora do escopo estrito da tarefa. Não foram executados testes, conforme instrução de revisão somente leitura.
