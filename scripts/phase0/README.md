# Rotina reproduzível — Fase 0 offline

Execute no Windows PowerShell 5.1, a partir da raiz do repositório:

```powershell
.\scripts\phase0\Test-Phase0Environment.ps1
.\scripts\phase0\Start-Phase0Api.ps1
.\scripts\phase0\Start-Phase0Metro.ps1
.\scripts\phase0\Test-Phase0Smoke.ps1
```

Para PT-05, não execute o smoke da API. Depois de instalar um novo Development Build do perfil `phase0-offline` e iniciar o Metro em USB, execute:

```powershell
.\scripts\phase0\Test-PT05Static.ps1
.\scripts\phase0\Test-PT05OfflineAdb.ps1
```

O segundo script mantém somente `adb reverse tcp:8081`, desliga Wi-Fi e dados móveis durante a inferência, registra somente o evento sanitizado `PT05_RESULT`, salva screenshot em `evidence\pt05` e restaura conectividade e reversões anteriores no fim.

Na prova aprovada de 21/08/2026, o script abriu explicitamente `exp+scanplant://expo-development-client/?url=http%3A%2F%2F127.0.0.1%3A8081`, aguardou `PT05_STAGE screen-mounted` e confirmou `PT05_RESULT` com Top-1 `daisy` em 1.652 ms. Para uma retomada reproduzível, inicie Metro com `EXPO_PUBLIC_PT05_OFFLINE_PROOF=1`, `--dev-client --localhost --clear`, e execute somente `Test-PT05OfflineAdb.ps1`.

`Start-Phase0Api.ps1` pede a senha do PostgreSQL em campo seguro, cria apenas `ScanPlantPhase0` quando ele não existe e passa conexão/JWT efêmero somente ao processo da API. Se o banco isolado já existir e estiver incompatível, a API para sem modificá-lo. O script nunca seleciona `ScanPlantDB`.

`Test-Phase0Environment.ps1` não encerra processos: apenas informa ocupantes das portas e exige exatamente um dispositivo ADB autorizado. `Get-Phase0SafeLogs.ps1` mostra somente linhas relevantes do Android já redigidas.

O smoke test cria um usuário descartável sem excluir dados. No checkpoint de 21/08/2026, ele foi aprovado com `PASS=8 FAIL=0`. A confirmação física do Development Client também foi concluída no Redmi A5 (`25028RN03L`) via USB/ADB, com `adb reverse` para as portas `8081` (Metro) e `5041` (API).

Na validação manual desse checkpoint foram testados somente a abertura do aplicativo, o cadastro de uma conta descartável e a entrada na aplicação após o cadastro. Não repetir testes já aprovados nem declarar outras telas ou funcionalidades como testadas pela interface sem nova evidência.
