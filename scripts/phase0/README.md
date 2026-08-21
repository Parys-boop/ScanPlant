# Rotina reproduzível — Fase 0 offline

Execute no Windows PowerShell 5.1, a partir da raiz do repositório:

```powershell
.\scripts\phase0\Test-Phase0Environment.ps1
.\scripts\phase0\Start-Phase0Api.ps1
.\scripts\phase0\Start-Phase0Metro.ps1
.\scripts\phase0\Test-Phase0Smoke.ps1
```

`Start-Phase0Api.ps1` pede a senha do PostgreSQL em campo seguro, cria apenas `ScanPlantPhase0` quando ele não existe e passa conexão/JWT efêmero somente ao processo da API. Se o banco isolado já existir e estiver incompatível, a API para sem modificá-lo. O script nunca seleciona `ScanPlantDB`.

`Test-Phase0Environment.ps1` não encerra processos: apenas informa ocupantes das portas e exige exatamente um dispositivo ADB autorizado. `Get-Phase0SafeLogs.ps1` mostra somente linhas relevantes do Android já redigidas.

O smoke test cria um usuário descartável sem excluir dados; a única confirmação manual remanescente é observar o Development Client carregar o bundle após o Metro iniciar.
