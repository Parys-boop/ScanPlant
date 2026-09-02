# Replanejamento v2 — P03-R4: portabilidade de recursos externos

## Objetivo e limites

P03-R4 é a revisão formal mínima do contrato ambiental rígido P03-R3. Ela não altera o ScanPlant, produção, testes, MutationHarness, dependências, manifest de tools, SDK/runtime/tool version, targets, concurrency, reporters, thresholds, risk seam, exigência `23/23`, contadores, worktree ou evidence histórica. P01 permanece blocked-terminal; P02 permanece completed; P03-R1/R2 são históricos blocked. P03-R3 permanece aprovado, mas não executável neste host sob os seus literais externos; não é falha de produto. P01 e P02 preservam seus contratos separados, também congelados pelo delta histórico SD-001. (D-001, D-002, D-006, A-001, A-005, P-001, P-010, S-004, SD-001)

## Resolução portátil antes da sanitização

Antes de criar ou exportar o ambiente sanitizado, o executor captura `host_home`: HOME natural absoluto do processo host, existente, legível, diretório e não symlink. Este valor é evidencia factual do host e pode variar entre hosts equivalentes. Só então resolve e valida:

- `resolved_toolchain_root=$host_home/.dotnet-scanplant-8`;
- `resolved_dotnet_root=$resolved_toolchain_root`;
- `resolved_dotnet_host_path=$resolved_toolchain_root/dotnet`;
- `resolved_nuget_packages=$host_home/.nuget/packages`.

O host deve provar localmente, sem download, rede, instalação, cópia ou symlink, que esses paths são legíveis/executáveis conforme aplicável e que entregam SDK `8.0.424`, `Microsoft.NETCore.App 8.0.30`, `Microsoft.AspNetCore.App 8.0.30`, package e executável locais de `dotnet-stryker 4.16.0`, com `.config/dotnet-tools.json` ainda declarando `4.16.0`. Ausência, versão distinta, path derivado fora do host_home ou qualquer workaround interrompe antes do preflight e mantém `campaign_count=0`. (D-007, A-005, P-010, S-004)

## Ambiente sanitizado e igualdade material congelada

Após a resolução, um único `run-dir` recebe um manifesto congelado. O `HOME` final é sempre `sanitized_home=<run-dir>/home`; ele não substitui nem participa da resolução de `host_home`. `DOTNET_CLI_HOME=<run-dir>/cli-home` e `TMPDIR=<run-dir>/tmp` também são distintos e locais ao run-dir.

O manifesto congela `host_home` como fato de proveniência e compara, como igualdade material entre restore, launcher, MutationHarness e eventual campanha: `resolved_dotnet_root`/`DOTNET_ROOT`, `resolved_dotnet_host_path`/`DOTNET_HOST_PATH`, `resolved_nuget_packages`/`NUGET_PACKAGES`, SDK, runtimes, versão de tool, `PATH` final (iniciando em `resolved_toolchain_root`), `DOTNET_CLI_HOME`, `sanitized_home`/`HOME`, `TMPDIR`, `LANG=C`, `LC_ALL=C`, cwd e run-dir. `DOTNET_MULTILEVEL_LOOKUP=0` permanece fixo. A resolução pode diferir entre hosts equivalentes; após ser registrada, qualquer diferença entre fases é material e interrompe antes da campanha. (D-007, D-008, P-008, P-009, SD-004)

## Preflights, campanha e segurança

Sob o manifesto congelado, P03-R4 preserva o restore offline, launcher composto exatamente `dotnet tool run dotnet-stryker -- --help`, prova de não mutação e, depois, MutationHarness existente em `net8.0 --no-build --no-restore` com `23/23`. Nenhum launcher/preflight/harness consome campanha. O launcher não recebe `--project`, `--config-file`, `--mutate` ou `--output`.

Somente após todos esses gates passarem e U-006 posterior, uma campanha seletiva única poderá começar com os únicos targets `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`, `net8.0`, Stryker `4.16.0`, concurrency `1`, reporters/thresholds existentes e seam `external-fallback`. `campaign_count` fica `0` até o início, então muda para `1`; nunca existe segunda campanha automática. Download, rede para preparar ferramenta, instalação automática, symlink, cópia para satisfazer gate, fallback silencioso para outro dotnet, SDK/runtime/tool alternativos são proibidos. (A-005, P-009, P-010, U-006, SD-004)

## Binding, workspace e policy

O linked worktree canônico isolado é obrigatório. Antes de campanha, e no verificador, `revision == expected_revision == HEAD` executável; esse HEAD deve estar aprovado, commitado, sincronizado, limpo e `0/0`. O HEAD futuro é determinado apenas depois do checkpoint aprovado P03-R4, não pelo HEAD desta elaboração.

`bm.py policy` para o seam histórico retorna breaker no round acumulado 3. Isto não é contornado nem reiniciado por P03-R4: não há patch novo nesta revisão; ela é o redesign documental mínimo do contrato ambiental invalidado. Qualquer novo patch do seam segue a regra do breaker. A aprovação P03-R4 não autoriza campanha: apenas preflights; a campanha continua U-006 separada. (D-006, P-009, U-006)
