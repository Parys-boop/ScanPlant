# Implementacao de TDD no ScanPlant

Esta branch adiciona uma base objetiva de TDD sobre o projeto existente:

- testes automatizados no backend com `xUnit`, `FluentAssertions` e `EF Core InMemory`;
- testes automatizados no frontend com `Vitest` e `Testing Library`;
- workflow de CI para validar API e web a cada `push` e `pull request`;
- cobertura de comportamentos reais do sistema, nao apenas configuracao da stack.

## O que esta coberto

### Backend

Arquivo: `ScanPlantAPI/ScanPlantAPI.Tests/Unit/Services/PlantQueryServiceTests.cs`

- retorno apenas de plantas da comunidade;
- ordenacao por `CreatedAt` decrescente;
- filtros por cidade, familia e lembrete;
- listagem de plantas por usuario;
- listagem de plantas orfas.

### Frontend

Arquivo: `scanplant-web/src/test/pages/SearchScreen.test.tsx`

- carregamento da lista de plantas via API;
- renderizacao dos itens recebidos;
- filtro pela categoria de busca selecionada;
- estado vazio quando nao ha plantas.

## Como validar

### Backend

```powershell
dotnet test ScanPlantAPI\ScanPlantAPI\ScanPlantAPI.sln --configuration Release --collect:"XPlat Code Coverage"
```

### Frontend

```powershell
cd scanplant-web
npm ci
npm run test -- --run
npm run build
```

## Observacao

O objetivo desta branch e deixar o projeto existente com uma fundacao de TDD verificavel em CI. Isso nao significa que 100% do sistema esteja coberto, mas sim que o projeto agora possui testes automatizados, pipeline de validacao e exemplos concretos de comportamento protegido por testes.
