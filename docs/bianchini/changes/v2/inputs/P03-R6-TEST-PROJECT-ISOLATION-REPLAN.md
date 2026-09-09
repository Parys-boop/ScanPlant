# Escopo aprovado — P03-R6: isolamento do projeto de testes da campanha

## Decisão e classificação

A tentativa U-008 de P03-R5 é evidência terminal e imutável em `/tmp/p03-r5-u007.h8rfIr`. O launcher iniciou Stryker `4.16.0` sob SDK `8.0.424`, criou uma única transição `campaign_count=1`, e falhou no build inicial antes de criar ou executar mutantes. O log prova `TestProjects=[]`, seleção automática de `ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj`, build de `ScanPlantAPI.sln` e `NETSDK1045` ao alcançar seu target versionado `net10.0`.

`bm.py change-policy --public-contract-change --plan-command --file-location --critical-invariant` classificou a divergência como `material_change`, com `invalidate_package_and_replan_affected_scope` e reaprovação obrigatória. P03-R6 é uma única rodada corretiva mínima do contrato da campanha; não recria P03 nem altera P01/P02.

## Estado factual congelado

- branch `bm/v2-p03`; `HEAD == upstream == 716ef26c8621251a1851b4b44f08dbb60c66e45c`; divergência `0/0`; árvore limpa antes deste planejamento;
- P03-R5 é terminal por tentativa U-008 falha; U-008 foi autorizada, consumida e não reutilizável;
- `campaign_count` acumulado é `1`; nenhum mutante foi criado/executado e não existe `mutation-report`;
- o preflight R5 passou no WSL normal; o MutationHarness canônico `net8.0` terminou `23/23`;
- SDK `8.0.424`, Stryker `4.16.0`, integridade oficial do pacote e feed offline de 79 pacotes permanecem aprovados e não serão repetidos;
- nenhum SDK 10, alteração de `TargetFramework(s)`, produção, projeto versionado, cache global, download ou rede é autorizado.

## Resultado autorizado para planejar

Definir um preflight R6 focalizado, a executar no WSL normal, que antes de nova campanha prove: (1) `ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj` é o único projeto de testes; (2) um contexto temporário isolado contém apenas a API `net8.0` e o harness `net8.0`; (3) `ScanPlantAPI.sln` e `ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj` multi-target não são selecionáveis; (4) o launcher/configuração temporários passam sintaxe, SHA-256 e binding; (5) o build do contexto isolado passa; e (6) o MutationHarness permanece `23/23`.

A futura campanha, se e somente se o preflight passar e existir U-009 humana, será uma nova campanha distinta: seu contador só pode transitar atomicamente `1 -> 2`. U-008 jamais é reutilizada, e qualquer falha depois de `2` interrompe sem retry.

## Limites imutáveis

Não executar nesta rodada restore, build, testes, Stryker, mutação, campanha, provider, banco, credenciais, download, commit ou push. Não sobrescrever evidência R5. Não modificar código, arquivos `.csproj`, `TargetFrameworks`, dependências, tool manifest, SDK/runtime, thresholds, reporters, targets de mutação ou cache global.
