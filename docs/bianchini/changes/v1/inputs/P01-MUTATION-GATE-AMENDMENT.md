# Escopo aprovado — amendment P01-R1: garantia de mutação do fallback externo

## Decisão formal registrada

O supervisor autorizou exclusivamente o replanejamento da garantia seletiva do P01 depois do breaker do seam `external-fallback`. A decisão não dispensa, substitui ou reduz o gate: os sobreviventes materiais devem ser mortos ou receber prova concreta de equivalência.

## Escopo limitado

- Inventariar e tratar somente os mutantes materiais `982`, `1010`, `1012`, `1020`, `1026` e `1028`, e os mutantes sem cobertura ligados a invariantes de segurança.
- Manter a mutação em `ExternalFallbackUploadValidator.cs` e `ExternalFallbackService.cs`, pelo harness puro `net8.0`, SDK isolado 8.0.424 e `dotnet-stryker` 4.16.0 já declarados.
- Permitir alterações de produção somente nesses dois arquivos, quando uma asserção nova demonstrar defeito; limitar os testes ao harness e aos testes focados de fallback.

## Limites preservados

Não alterar contratos públicos, providers, rede, credenciais, créditos, banco, migrations, mobile, `scanplant-web` ou Nominatim. P02 continua bloqueado até P01 passar o gate. Não há nova dependência além do `dotnet-stryker` 4.16.0 já justificado.

## Regra de parada

O contador histórico de `external-fallback` permanece em 3/3; esta revisão não o renomeia nem o zera. Ela autoriza uma única execução corretiva planejada, sem loop automático de fix rounds. Qualquer sobrevivente material, no-coverage de invariante de segurança, timeout não determinístico, falha de produto ou necessidade de segunda correção encerra a unidade como bloqueada e exige nova decisão formal do supervisor.
