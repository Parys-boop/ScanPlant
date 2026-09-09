# Stack Research — continuidade pós-U-009

Research mode: repo_only
Motivo: deliberação e protocolo documental sobre stack conhecida; não se escolhe API/versão nova, preço vigente ou vencedor sem futura evidência. A solicitação limita o fundamento aos documentos e evidências locais.

## Stack detectada

API ASP.NET Core net8.0; providers internos substituíveis `IPlantIdentificationProvider` e `IPlantKnowledgeProvider`. `Program.cs` registra Pl@ntNet e Groq; a interface ser substituível não significa que já exista selector por configuração ou adaptador Plant.id/Gemini. Mobile Expo 51/React Native 0.74.5, React 18.2.0. Nada será atualizado.

## Inventário local

- Manifests: `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj`, `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj`, `ScanPlant-Final/package.json`, `.config/dotnet-tools.json`.
- Lockfiles: `ScanPlant-Final/package-lock.json` existente; nenhum `packages.lock.json` versionado localizado. Manifestos/cache R6 são históricos, não insumos do benchmark.
- CI: `.github/workflows/deploy.yml` publica `scanplant-web` em push master; não é comprovação dos gates API/mobile nem será acionada aqui.
- Testes: scripts locais `test:mobile-consent` e `validate:pt05`; testes xUnit de upload/service/integração e MutationHarness net8. Histórico dos comandos/resultados nos ledgers P01/P02. Nenhum foi executado nesta rodada.
- Padrões locais: `Services/ExternalProviders/ExternalFallbackContracts.cs`, `ExternalFallbackOptions.cs` e `Program.cs` mantêm providers no backend; `components/api.js` e `PhotoScreen.js` mantêm JWT, API-only e consentimento. Nenhum código entra no pacote novo.

Leitura localizada suficiente: apenas contratos de fallback, seams de testes, cliente e documentos de continuidade. Não há fluxo multiaplicação sendo modificado; não se cria cartografia artificial de áreas de treino, banco, web, vídeo ou acompanhamento.

## Decisões aplicadas

D-101: continuidade A, sem fechar garantia P01. D-102: benchmark como artefato de decisão, sem integração de novos providers no produto. O roadmap é fonte da comparação, não de preços atuais. Leituras oficiais futuras serão evidência de coleta, sem importação automática de dependências. D-103: nenhuma campanha, instalação ou preflight de processos isolados pertence a P04.

## Riscos e lacunas

A-101: os caminhos comparados com os commits de evidência funcional não mudaram, mas isto não cria RC válido. A-102: corpus autorizado, contas, condições atuais e medições comparativas não constam como aprovados; U-101 limita a coleta e impede selecionar vencedor sem dados. P-101: interpretar score ausente como waiver enfraqueceria aceite. P-102: dados pessoais/créditos e amostra pequena exigem autorização, minimização e conclusão limitada. P-103: a interpretação de `0x9` no diagnóstico terminal está incorreta; não usar como causa exclusiva.
