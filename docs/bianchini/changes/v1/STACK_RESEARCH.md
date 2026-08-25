# Stack Research — F1-BE01

Research mode: targeted_web

Motivo: o ciclo cria uma fronteira HTTP autenticada, upload multipart e adaptadores de duas APIs externas cujos contratos, limites e práticas de segurança são temporalmente sensíveis.

## Stack detectada

- Backend: ASP.NET Core `net8.0`, controllers, JWT e EF Core em `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj` e `Program.cs`.
- Mobile: Expo SDK 51 / React Native, cliente `fetch` com JWT em `ScanPlant-Final/components/api.js` e descoberta de API em `apiConfig.js`.
- Testes: não existe projeto .NET de teste; scripts PT-05 são evidência concluída e não entram nos gates deste ciclo.

## Fontes primárias

- Fonte primária: Pl@ntNet API — referência da API REST; permite de uma a cinco imagens e retorna espécies prováveis com score.
  URL: https://docs.plantnet.org/en/reference/api-plantnet/
  Acessado em: 2026-08-25
  Aplicação: adaptador inicial `PlantNetIdentificationProvider`, escondendo o DTO do fornecedor.

- Fonte primária: Upload files in ASP.NET Core — upload multipart com `IFormFile`, validação no servidor, limite de tamanho e desconfiança do nome de arquivo.
  URL: https://learn.microsoft.com/en-us/aspnet/core/mvc/models/file-uploads?view=aspnetcore-8.0
  Acessado em: 2026-08-25
  Aplicação: endpoint recebe uma imagem única, limitada e transitória; não a persiste nem usa o nome do cliente.

- Fonte primária: Groq Rate Limits — limites podem retornar HTTP 429 e `retry-after`; variam por organização/modelo.
  URL: https://console.groq.com/docs/rate-limits
  Acessado em: 2026-08-25
  Aplicação: traduzir 429 para erro público seguro e respeitar `Retry-After`, sem codificar quota de fornecedor como garantia.

- Fonte primária: Groq API Reference — endpoint de chat requer `model` e `messages`; oferece modo JSON/JSON Schema quando suportado.
  URL: https://console.groq.com/docs/api-reference
  Acessado em: 2026-08-25
  Aplicação: `GroqPlantKnowledgeProvider` limita a saída a DTO normalizado e nunca recebe a imagem.

## Decisões aplicadas

- Usar `HttpClientFactory`, cliente tipado/nomeado por provider e `CancellationToken` encadeado ao cancelamento da requisição com prazo configurável.
- Usar `IFormFile` apenas para imagem pequena, transitória e previamente limitada; validar MIME declarado, assinatura/formato e dimensões antes de encaminhar ao provider.
- Aplicar rate limit local por identidade autenticada e preservar a semântica de `429`/`Retry-After` quando o upstream limitar.
- Tratar Groq como enriquecimento textual opcional: identificação válida não falha por indisponibilidade de conhecimento.

## Alternativas rejeitadas

- DTO Plant.id ou Pl@ntNet exposto ao mobile — acopla o contrato público ao fornecedor e contraria a troca por configuração.
- Chave no `.env` mobile — qualquer variável empacotada pode ser extraída do cliente.
- Fazer upload persistente ou criar tabela de auditoria — não há requisito de retenção; introduziria dado pessoal e migration sem necessidade comprovada.
- Usar quota/documentação externa como substituto de limite local por usuário — não isola abuso entre usuários nem estabiliza os limites do produto.

## Riscos e lacunas

- O contrato detalhado de autenticação/endpoint de Pl@ntNet será conferido sem chamada real quando a credencial for disponibilizada; fakes mantêm o desenvolvimento e os testes sem quota.
- Os limites efetivos de Pl@ntNet e Groq variam por conta; configurações do backend devem ser revalidadas antes de ativar produção.
- P-004: não há framework de mutação ou testes .NET no repositório; o primeiro plano adiciona somente o harness de teste e a ferramenta seletiva exigida para o seam de segurança, sem atualização geral de dependências.

## Spike encerrado

- S-001: a cartografia local e a leitura confirmaram o limite mobile/API e a ausência de testes/providers; a decisão aplicada é a separação entre P01 estrito e P02 dependente, sem ampliar para geolocalização, web ou PT-05.
