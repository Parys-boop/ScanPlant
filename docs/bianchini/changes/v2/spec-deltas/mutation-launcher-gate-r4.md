# Delta de especificação — gate portátil do launcher P03-R4

## Contrato pós-entrega

O gate P03 resolve recursos externos antes de sanitizar HOME: captura `host_home` natural, absoluto, existente, legível e não symlink; deriva `DOTNET_ROOT=<host-home>/.dotnet-scanplant-8`, `DOTNET_HOST_PATH=$DOTNET_ROOT/dotnet` e `NUGET_PACKAGES=<host-home>/.nuget/packages`. O template é portátil entre hosts equivalentes; os valores derivados são congelados para uma execução. Não é permitido trocar username literal, usar symlink/cópia, baixar, instalar automaticamente, acessar rede para preparar tools, escolher outro dotnet ou aceitar SDK/runtime/Stryker diferente.

Antes de qualquer preflight, prova-se localmente SDK `8.0.424`, `Microsoft.NETCore.App` e `Microsoft.AspNetCore.App` `8.0.30`, manifest `dotnet-stryker 4.16.0`, package e executável locais `4.16.0` e legibilidade/executabilidade dos paths. Falta ou divergência para com `campaign_count=0`.

`HOME=<run-dir>/home`, `DOTNET_CLI_HOME=<run-dir>/cli-home` e `TMPDIR=<run-dir>/tmp` são valores sanitizados, distintos de `host_home`. Um manifesto por run-dir congela e exige igualdade exata entre restore, launcher, MutationHarness e campanha para valores resolvidos `DOTNET_ROOT`, `DOTNET_HOST_PATH`, `NUGET_PACKAGES`, SDK, runtime, tool version, PATH final, CLI home, HOME sanitizado, TMPDIR, LANG, LC_ALL, cwd e run-dir. Valores podem variar entre hosts, não entre fases.

O restante do gate P03-R3 permanece: restore offline, prova composta do launcher sem banner obrigatório, ausência de mutação, harness existente `net8.0 --no-build --no-restore` com `23/23`, uma campanha futura somente após autorização humana separada e `revision == expected_revision == HEAD` executável aprovado/commitado/sincronizado/limpo `0/0`; targets exatos, concurrency `1`, Stryker `4.16.0` e seam `external-fallback` não mudam. (D-007, D-008, A-005, P-008, P-009, P-010, U-006, SD-004)
