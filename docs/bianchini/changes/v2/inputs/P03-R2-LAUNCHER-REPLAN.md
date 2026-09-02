# Escopo aprovado — revisão formal P03-R2: gate de resolução do launcher

## Objetivo

Replanejar exclusivamente a entrega de evidence seletiva P03 após o bloqueio ambiental de P03-R1. Antes de qualquer nova campanha, provar sem mutação e sem consumir campanha que o launcher local `dotnet-stryker` `4.16.0` resolve e inicia no mesmo ambiente .NET sanitizado que será usado pela campanha.

## Fato causal preservado

P03-R1 consumiu uma única campanha (`1/1`) em `50013c8b89860c112c46499ac93a6b9d4366cf73`. O launcher recebeu um `DOTNET_CLI_HOME` sanitizado sem o resolver cache do local tool e encerrou com `Run "dotnet tool restore" to make the "dotnet-stryker" command available.` antes de análise de mutantes. Não houve relatório, normalização, classificações ou `mutation-evidence verify`. A falha é de ambiente/launcher, não de produto ou testes; não autoriza retry de P03-R1.

## Escopo limitado de P03-R2

- Registrar e executar futuramente um preflight não mutacional que prepara, de modo offline, o resolver do tool local no `DOTNET_CLI_HOME` sanitizado final e prova a invocação real de `dotnet-stryker --help`.
- Preservar `DOTNET_ROOT` `/home/arthur/.dotnet-scanplant-8`, SDK `8.0.424`, runtime `Microsoft.NETCore.App 8.0.30`, `net8.0`, `dotnet-stryker` `4.16.0`, concorrência `1`, policy `required_selective`, seam `external-fallback` e o MutationHarness existente.
- Depois de preflights aprovados e de uma autorização humana separada, permitir no máximo uma nova campanha seletiva a partir de `ScanPlantAPI/ScanPlantAPI`, com `--project ScanPlantAPI.csproj` e somente `Services/ExternalProviders/ExternalFallbackUploadValidator.cs` e `Services/ExternalProviders/ExternalFallbackService.cs`.
- Vincular a evidence futura ao `HEAD` limpo, aprovado e sincronizado existente no instante de execução. O HEAD de elaboração (`2b79620fffd1c21e679889434663a8728436053b`) não é o binding futuro, porque o checkpoint aprovado deste pacote poderá criar novo commit.

## Limites e proibições

Esta rodada e a futura execução não alteram produção, testes, MutationHarness, dependências, manifesto/filtros/thresholds, provider, banco, credenciais, crédito externo, rede de aplicação, `METHOD_CONTRACT.md`, `bm.py`, `bm_mutation.py` ou componentes compartilhados do método. Não há carry-forward, segunda campanha automática, restore/download em rede, RC, fingerprint, proof-map, commit, push, merge, rebase ou PR nesta rodada. O restore offline do tool e o restore/build do harness somente são permitidos na futura execução quando o gate descrito no plano os requerer e quando não acionarem rede/download.

## Aprovação necessária

Este escopo autoriza somente o planejamento. A aprovação humana única do pacote P03-R2 é necessária para executar seus preflights. A campanha real requer, depois de todos os preflights passarem e contra a revisão então válida, uma segunda autorização humana explícita de `1` campanha; sem ela P01 permanece bloqueado.
