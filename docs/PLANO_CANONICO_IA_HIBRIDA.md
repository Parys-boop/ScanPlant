# Plano canônico — IA híbrida e continuidade do ScanPlant

**Atualizado em:** 25/08/2026  
**Branch de continuidade:** `phase1-bianchini`  
**Função deste documento:** ser a referência principal para qualquer pessoa ou IA que retome o desenvolvimento.

**Deliberação de continuidade em 09/09/2026 — pendente de aprovação:** o estado vigente está em `docs/living/PROJECT_STATE.md`. P02 está completed; P01 e P03-R6/U-009 permanecem blocked-terminal, com release pending. A [proposta pós-U-009](bianchini/changes/v2/POST-U009-DELIBERATION.md) recomenda retomar F1-API01 pelo plano P04, sem reabrir R6, repetir mutação ou dispensar a garantia pendente de P01. O texto datado abaixo preserva a ordem funcional; referências antigas a branch e “ainda sem implementação” não substituem o estado atual. Esta proposta não autoriza execução ou entrega final.

## 1. Regra de continuidade

Antes de propor ou executar trabalho no ScanPlant:

1. conferir a branch e o último commit remoto;
2. ler este documento;
3. ler `CHECKPOINT_FASE0_OFFLINE.md`;
4. consultar o documento específico do marco atual;
5. não reabrir marcos concluídos sem regressão concreta;
6. executar um único marco por vez, reunindo implementação, testes e correções relacionadas;
7. solicitar autorização apenas para commit, push, merge, exclusão de dados/arquivos importantes ou mudança de escopo.

O estado remoto e os documentos versionados mais recentes prevalecem sobre conversas antigas, prompts anteriores e instruções históricas do README.

## 2. Estado confirmado

### Fase 0 — concluída

A prova técnica confirmou no Redmi A5:

- Development Build Android reproduzível;
- carregamento do bundle por USB/ADB;
- `react-native-fast-tflite` funcional;
- modelo TFLite empacotado;
- pré-processamento RGB `224×224×3`;
- inferência local em CPU sem internet;
- resultado determinístico em 1.652 ms;
- smoke test da API com `PASS=8 FAIL=0`.

O MobileNet V1/ImageNet usado nessa prova demonstra compatibilidade técnica. Ele não é o modelo botânico definitivo e não deve ser apresentado como reconhecimento das espécies do produto.

### Fase 1 — ainda sem implementação de produto

A branch `phase1-bianchini` contém o gate documental `F1-G01`. Foram avaliados quatro candidatos de modelo pronto, mas nenhum foi aprovado. Nenhum dataset, treinamento, conversão, novo modelo botânico ou fluxo híbrido definitivo foi implementado.

## 3. Escopo funcional preservado

O MVP continua prevendo:

- reconhecimento local prioritário;
- 12 espécies suportadas offline;
- classes de proteção `outra_planta` e `imagem_invalida`;
- catálogo de cuidados offline para as 12 espécies;
- serviço externo somente como fallback;
- confirmação do usuário antes de enviar imagem;
- funcionamento útil sem internet;
- coleta manual de fotos próprias apenas para lacunas e validação final;
- arquitetura que permita trocar provedores sem reescrever o aplicativo.

As 12 espécies permanecem as definidas no escopo aprovado. O recorte de cinco espécies usado no F1-G01 foi apenas uma auditoria piloto e não altera o escopo.

## 4. Decisão de arquitetura para APIs externas

O aplicativo móvel não poderá:

- chamar diretamente Plant.id, Pl@ntNet, Groq, Gemini ou outro provedor;
- conter chaves ou segredos dos provedores;
- escolher fornecedor por nome dentro das telas;
- enviar imagem externamente sem consentimento;
- depender de IA generativa para os cuidados básicos das 12 espécies locais.

Toda integração externa ficará no backend, atrás de contratos substituíveis:

- `IPlantIdentificationProvider`: identificação externa por imagem;
- `IPlantKnowledgeProvider`: complemento textual opcional;
- DTO uniforme, independente do fornecedor;
- configuração de provedor e credenciais somente no servidor;
- timeout, cancelamento, limite de requisições e erros controlados;
- registro da origem do resultado;
- troca de fornecedor por configuração, sem alterar o fluxo mobile.

O modelo local será sempre a primeira tentativa. O fallback externo será oferecido apenas para baixa confiança, `outra_planta`, espécie não suportada ou falha controlada.

## 5. Estratégia de escolha dos provedores

Nenhum fornecedor é permanente. A seleção será feita por um benchmark pequeno e reproduzível.

### Identificação botânica

**Candidato inicial preferencial para avaliação: Pl@ntNet API.**

Motivo: em 25/08/2026, a página oficial informa plano gratuito de até 500 identificações por dia e alternativa gratuita para uso educacional ou científico mediante contato. A página também declara mais de 50 mil espécies identificáveis.

Fontes:

- https://my.plantnet.org/pricing
- https://my.plantnet.org/terms_of_use

**Plant.id/Kindwise permanece como referência de comparação, não como escolha gratuita padrão.**

Em 25/08/2026, a documentação oficial informa 100 créditos iniciais de teste. Depois disso, as identificações são pagas por crédito, com valores publicados entre €0,01 e €0,05 por chamada.

Fontes:

- https://www.kindwise.com/pricing
- https://www.kindwise.com/faqs-admin-panel

### Conhecimento e cuidados

Para as 12 espécies locais, a fonte principal será o catálogo offline revisado. Um modelo generativo poderá complementar respostas apenas quando houver internet.

Groq e Gemini permanecem candidatos para o complemento textual. A escolha não será feita apenas por velocidade ou nome do modelo. O benchmark deverá medir:

- disponibilidade de plano gratuito real, não apenas teste;
- limites por minuto e por dia;
- validade do JSON estruturado;
- qualidade em português brasileiro;
- consistência de nomes científicos e cuidados;
- frequência de respostas inventadas;
- latência mediana e pior caso;
- tratamento de dados e termos de uso;
- estabilidade e política de descontinuação dos modelos.

Fontes de limites e preços que deverão ser revalidadas no momento da implementação:

- https://console.groq.com/docs/rate-limits
- https://ai.google.dev/gemini-api/docs/pricing

As condições gratuitas podem mudar. Portanto, nenhum limite será tratado como permanente no código ou na documentação de arquitetura.

### Critério mínimo de “gratuito”

Para este MVP, “gratuito” significa:

- permitir o volume esperado do projeto acadêmico sem pagamento;
- não exigir compra obrigatória após um teste curto;
- possuir limites oficiais publicados;
- permitir bloquear gasto inesperado;
- não impedir futura substituição do fornecedor.

## 6. Ordem canônica dos próximos marcos

### Preparação da branch

`phase1-bianchini` divergiu de `master`. Antes de implementar produto, integrar `master` por merge autorizado, preservando a configuração segura da branch: nenhuma connection string ou chave JWT deverá voltar para `appsettings.json`.

Não usar rebase na branch já publicada.

### Marco imediato — F1-BE01: fallback externo seguro

Entregar em uma única rodada:

1. contratos dos provedores;
2. configuração segura no backend;
3. provedor botânico inicial atrás da interface;
4. provedor de conhecimento opcional atrás da interface;
5. endpoint autenticado de identificação;
6. validação de imagem, tamanho e formato;
7. timeout, cancelamento, limite de requisições e erros uniformes;
8. DTO único para resultados;
9. cliente mobile do novo endpoint;
10. remoção das chamadas Plant.id/Groq e das chaves do `PhotoScreen.js`;
11. testes unitários e de integração do marco.

O primeiro provedor pode ser um adaptador da integração existente para preservar comportamento. A troca para o vencedor do benchmark ocorrerá sem mudar o contrato mobile.

### Marco seguinte — F1-API01: benchmark e decisão de provedores

Comparar no backend, com conjunto fixo de casos:

- Pl@ntNet e Plant.id para identificação;
- Groq e Gemini para complemento textual, se esse complemento ainda for necessário.

Registrar qualidade, latência, limites, privacidade, falhas e gratuidade. Selecionar provedor principal e secundário por evidência.

### Depois da segurança do fallback

1. manifesto completo das 12 espécies, sinônimos e duas classes de proteção;
2. aquisição rastreável de imagens CC0/CC BY;
3. filtros, deduplicação e revisão humana;
4. treinamento EfficientNet-Lite0 e comparação com MobileNetV2;
5. exportação Float16/INT8 e teste no Redmi A5;
6. integração do classificador e catálogo offline;
7. fluxo híbrido com consentimento para fallback;
8. análise guiada por vídeo;
9. acompanhamento do desenvolvimento das plantas.

Não iniciar treinamento, vídeo ou acompanhamento durante F1-BE01.

## 7. Método Bianchini e ambiente

O Método Bianchini organiza o trabalho, mas não é dependência de execução do ScanPlant.

Para evitar falsos diffs de finais de linha:

- não corrigir em massa o clone Windows acessado por `/mnt/c`;
- preferir um clone novo no sistema de arquivos nativo do WSL, por exemplo `~/code/scanplant-work/ScanPlant`;
- manter o repositório oficial do método separado do projeto;
- não modificar o método oficial para adaptar o ScanPlant;
- futuramente, criar um método próprio independente em vez de disputar ou substituir o projeto original.

Problemas de instalação do método não devem autorizar mudanças improvisadas no código do produto.

## 8. Critérios para encerrar cada marco

Um marco só é encerrado quando houver:

- código do escopo definido;
- testes diretamente relacionados aprovados;
- verificação de ausência de segredos;
- documentação/checkpoint atualizados;
- lista objetiva de pendências reais;
- commit e push somente após autorização;
- nenhuma funcionalidade futura iniciada prematuramente.

## 9. Documentos relacionados

- `CHECKPOINT_FASE0_OFFLINE.md` — evidência da prova técnica concluída;
- `docs/phase1/F1-G01-matriz-modelos-botanicos.md` — auditoria inicial de modelos;
- `CHECKPOINT_CONTINUIDADE_2026-08-24.md` — registro histórico do ambiente anterior;
- este arquivo — fonte canônica para continuidade e próximos marcos.
