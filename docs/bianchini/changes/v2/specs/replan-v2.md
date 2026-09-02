# Replanejamento v2 — P01/P02 preservados e P03-R2

## Objetivo e limites

P01 permanece blocked-terminal por garantia de mutação pendente; P02 permanece completed e não é reaberto. P03-R2 substitui somente a entrega de evidence bloqueada de P03-R1 para impedir a repetição da falha ambiental do local-tool resolver. Não há mudança de produto, teste, dependência, contrato público, design, credencial, provider, banco ou componente compartilhado do método. Os contratos funcionais aceitos continuam registrados e o escopo não permite enfraquecer a separação P01/P02. (D-001, D-002, D-004, A-001, P-001)

## Estados e relação entre planos

P03-R1 consumiu sua única campanha e falhou antes de qualquer mutante; seus artefatos ficam imutáveis como diagnóstico. P03-R2 não é retry: é uma revisão formal que exige novos preflights não consumidores e uma autorização humana futura para no máximo uma nova campanha. Se P03-R2 passar integralmente, P01 pode deixar o bloqueio somente depois da revisão humana documental aplicável; se bloquear, P01 e P03-R2 ficam blocked e release segue pending. P02 continua completed em ambos os casos. (D-004, P-004, P-005, U-004)

## P03-R2 launcher resolution gate

O ambiente sanitizado final fixa `DOTNET_ROOT=/home/arthur/.dotnet-scanplant-8`, SDK `8.0.424`, runtime `Microsoft.NETCore.App 8.0.30`, `DOTNET_MULTILEVEL_LOOKUP=0`, um `DOTNET_CLI_HOME` exclusivo do run e `NUGET_PACKAGES` já existente. Um restore local-tool somente offline materializa o resolver dentro desse CLI home; nenhum download é aceitável. O gate exige: manifest `dotnet-stryker` `4.16.0`; shim/cache em tal CLI home; `$DOTNET tool run dotnet-stryker -- --help` no cwd de campanha; banner `Version: 4.16.0`; PID/lifecycle e exit `0`; e ausência de configuração, projeto, mutação, output, relatório e contador de campanha. O mesmo manifesto de ambiente, cwd e CLI home será reutilizado sem alteração material na campanha. (D-004, A-003, P-004, S-002, SD-002)

## MutationHarness preflight e campanha condicional

O MutationHarness existente é preflight separado, não consumidor: só passa com artefatos observáveis, `net8.0`, `--no-build --no-restore`, lifecycle/exit confiáveis e `23/23`. Restore/build somente offline pode ocorrer se os artefatos estiverem ausentes; necessidade de rede ou mudança bloqueia. Após ambos os preflights e U-004, a única campanha usa `required_selective`, seam `external-fallback`, concurrency `1`, `net8.0`, cwd `ScanPlantAPI/ScanPlantAPI`, `--project ScanPlantAPI.csproj` e os dois caminhos relativos autorizados. (P-005, U-004, SD-002)

## Binding, evidence e parada

No momento da campanha, `revision == expected_revision == HEAD` limpo, aprovado e sincronizado. Como `release.candidate` é nulo, o `mutation-evidence verify` instalado deriva `expected_revision` do HEAD; o commit futuro do pacote aprovado substitui naturalmente o HEAD de elaboração. Evidence registra manifest/digest de ambiente, preflight launcher/harness, contador, comando/configuração efetiva, lifecycle, report, normalização, classificações e resultado do verificador. Antes da campanha, qualquer falha para sem consumir; depois de iniciar, `campaign_count=1` e qualquer falha interrompe sem retry. (P-003, P-004, P-005)
