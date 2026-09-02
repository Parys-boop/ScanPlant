# Stack Research — P03-R4 portabilidade ambiental

Research mode: repo_only

Motivo: a revisão não introduz API, biblioteca, versão ou infraestrutura nova. O contrato a corrigir, o manifest local, a evidence histórica e o layout local já determinam a decisão; pesquisar na web não alteraria o desenho mínimo.

## Stack detectada

- `.config/dotnet-tools.json` fixa `dotnet-stryker` `4.16.0`.
- P03-R3 fixa SDK `8.0.424`, runtime `Microsoft.NETCore.App 8.0.30`, `net8.0`, Stryker `4.16.0`, concurrency `1` e o seam `external-fallback`.
- O diagnóstico informado para este host confirma os mesmos componentes sob `$host_home/.dotnet-scanplant-8` e `$host_home/.nuget/packages`.

## Inventário local

- Manifests: `.config/dotnet-tools.json` e contratos P03-R3.
- Lockfiles: não relevantes à mudança; nenhuma dependência é alterada.
- CI: não consultada, pois não há mudança de produção, build ou pipeline.
- Testes: MutationHarness histórico permanece `net8.0`, `--no-build --no-restore`, com exigência futura `23/23`.
- Padrões locais: P03-R3 já usa `run-dir`, `DOTNET_CLI_HOME`, `HOME` e `TMPDIR` sanitizados; somente os recursos externos absolutos eram host-bound.

## Decisões aplicadas

- Capturar `host_home` natural antes da sanitização e derivar dele os três recursos externos autorizados.
- Congelar os valores derivados, não o template, no manifesto de uma execução; igualdade material compara esses valores congelados.
- Manter o HOME de execução isolado em `<run-dir>/home`, distinto do `host_home` usado apenas para resolver recursos.

## Alternativas rejeitadas

- Trocar `/home/arthur` por `/home/administradorarthur`: transfere a mesma fragilidade a outro host.
- Symlink, cópia, instalação automática, download, fallback para outro dotnet ou versão alternativa: mascara a pré-condição e muda a prova ambiental.

## Riscos e lacunas

- Cada host futuro deve provar os recursos locais antes de qualquer preflight. A ausência bloqueia com `campaign_count=0`; não existe fallback operacional.
