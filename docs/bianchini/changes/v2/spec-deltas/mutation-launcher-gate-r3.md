# Delta de especificação — gate composto do launcher P03-R3

## Contrato pós-entrega

Antes de campanha, P03-R3 deve provar identidade exata de `dotnet-stryker` `4.16.0` por sinais combinados: manifest local; restore offline com exit `0` no `DOTNET_CLI_HOME` final; resolver desse cache com `Name=dotnet-stryker`, `Version=4.16.0`, `TargetFramework=net8.0` e `PathToExecutable` em `NUGET_PACKAGES/dotnet-stryker/4.16.0/`; existência do executável; e SHA-256 registrado quando aplicável. `dotnet tool list --local` é somente complementar.

No mesmo ambiente e cwd de campanha, `dotnet tool run dotnet-stryker -- --help` deve registrar processo/PID/lifecycle, exit `0` e help identificável como Stryker, correlacionado ao resolver acima. Não exige `Version: 4.16.0` no stdout. Sem `--project`, `--config-file`, `--mutate` e `--output`, deve provar nenhum projeto analisado, mutant, report, results/output de campanha e `campaign_count=0`.

O mesmo manifesto material de ambiente é reutilizado no restore, launcher, MutationHarness e eventual campanha. O harness existente só executa após o launcher composto e exige `net8.0`, `--no-build --no-restore`, lifecycle/exit confiáveis e `23/23`, ainda com `campaign_count=0`. A única campanha posterior exige autorização humana separada, `revision == expected_revision == HEAD` aprovado, commitado, sincronizado e limpo, e mantém o escopo seletivo fixado. (D-005, A-004, P-003, P-006, P-007, U-005, S-003, SD-003)
