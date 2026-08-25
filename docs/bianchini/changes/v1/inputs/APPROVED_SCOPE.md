# Escopo aprovado — F1-BE01: fallback externo seguro pelo backend

## Objetivo

Mover para a API ScanPlant as integrações externas de identificação botânica e conhecimento hoje chamadas pelo aplicativo móvel, preservando o uso offline e exigindo consentimento explícito antes de qualquer envio externo.

## Resultados obrigatórios

- Contratos `IPlantIdentificationProvider` e `IPlantKnowledgeProvider`, DTOs internos e públicos independentes de fornecedor e orquestração no backend.
- Endpoint autenticado `multipart/form-data` de fallback, com consentimento explícito, validação de tipo, tamanho e conteúdo da imagem, timeout, `CancellationToken`, rate limit por usuário e erros controlados, inclusive `429`.
- Pl@ntNet como adaptador inicial de identificação; Plant.id apenas como referência de futuro provider secundário; Groq opcional atrás de `IPlantKnowledgeProvider`.
- Credenciais, seleção de provider e limites somente no backend. O mobile chama somente a API ScanPlant para identificação e conhecimento e não contém Plant.id, Groq, URLs ou credenciais correspondentes.
- Testes unitários e de integração com providers e handlers HTTP falsos; teste real opt-in, desabilitado por padrão e condicionado a variável de ambiente; nenhuma chamada real durante testes normais.
- Sem migration, salvo necessidade concreta comprovada durante a execução; preservar integralmente a prova TFLite/PT-05.

## Limites obrigatórios

- Não alterar Nominatim ou o fluxo de geolocalização.
- Não alterar `scanplant-web`.
- Não iniciar dataset, treinamento, conversão ou modelo botânico; não alterar vídeo, rastreamento ou câmera contínua.
- Não repetir testes concluídos da Fase 0, não atualizar dependências de forma geral e não executar chamadas que consumam créditos.
- Não executar merge, commit, push ou PR neste ciclo de planejamento. O merge de `origin/master` é ação externa pendente de autorização, sem rebase.

## Referências canônicas

- `docs/PLANO_CANONICO_IA_HIBRIDA.md`
- `CHECKPOINT_FASE0_OFFLINE.md`
- `docs/phase1/F1-G01-matriz-modelos-botanicos.md`
