# Stack Research — P03-R5 contrato do MutationHarness

Research mode: repo_only

Motivo: layout, projetos, pacote local, evidence R4 e evidence histórica versionada determinam o contrato. Não há API, versão, dependência ou infraestrutura nova a pesquisar.

## Stack detectada

## Inventário local

- Manifests: `.config/dotnet-tools.json`, os três csproj do grafo e `NuGet.Config` R4 com fontes limpas.
- Lockfiles: nenhum lockfile altera o contrato; dependências permanecem congeladas.
- CI: ausente do escopo; não há mudança de pipeline.
- Testes: o csproj do harness é `net8.0`; histórico exige resultado final `23/23`.
- Padrões locais: evidence P01 v3/v5 usou o cwd do harness, assets explícitos e final `--no-build --no-restore`.

- `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj` é o projeto real, `TargetFramework=net8.0`, e referencia `../../ScanPlantAPI/ScanPlantAPI.csproj`.
- `ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj` exclui `MutationHarness/**/*.cs`; o harness é isolado do projeto pai.
- A solução `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln` contém somente a API; não é o grafo do harness.
- `.config/dotnet-tools.json` fixa `dotnet-stryker` `4.16.0`; nenhum arquivo de dependência ou configuração será alterado.
- R4 registrou que o cwd do launcher `ScanPlantAPI/ScanPlantAPI` não contém `ScanPlantAPI.MutationHarness.csproj`, enquanto o projeto real fica em `ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness` e não havia assets/output net8.0.
- A evidence manual versionada P01 v3/v5 registra `HARNESS_DIR=<repo>/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness`, prova `obj/project.assets.json` e `bin/Debug/net8.0/ScanPlantAPI.Tests.dll`, e executa o comando final no próprio harness. Checkpoints históricos registram build do harness com SDK `8.0.424`/runtime `8.0.30` seguido de harness `23/23`. (S-005)

## Decisões aplicadas

- O cwd canônico do harness será `<repo>/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness`; o nome local do csproj é robusto porque esse diretório é a autoridade do layout e da evidence histórica.
- A preparação é explícita e separada: primeiro restore offline do csproj usando um `NuGet.Config` de run-dir com `<clear />` para fontes, depois build `net8.0 --no-restore` do mesmo csproj. O build transita legitimamente o `ProjectReference` da API e materializa os outputs do harness sem alterar fontes.
- O gate final preserva exatamente `--no-build --no-restore`; falha de preparação impede sua execução.
- A igualdade ambiental será comum para valores de toolchain e específica para cwd contratado por fase; cwd diferente e declarado não é drift.

## Alternativas rejeitadas

- Usar o cwd da API com nome literal do csproj: R4 provou que não resolve o projeto.
- Apontar um path relativo a partir do cwd do launcher: menos direto que o cwd histórico do harness e mantém acoplamento artificial entre fases.
- Remover `--no-build` ou `--no-restore`: elimina a prova do gate final.
- Reutilizar artifacts/evidence R4: R4 não os tinha e cada R5 deve produzir run-dir próprio.

## Riscos e lacunas

Os packages/SDK precisam existir localmente; uma fonte, asset ou output ausente bloqueia antes do gate final e conserva `campaign_count=0`. R5 não autoriza download como fallback.
