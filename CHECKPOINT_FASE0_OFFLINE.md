# Checkpoint — Fase 0 offline

Data: 21/08/2026
Branch: phase0-offline
Último commit anterior: bec80f5

## Concluído

- Dependências do Expo SDK 51 instaladas.
- expo-dev-client configurado.
- Projeto criado e vinculado no EAS:
  - conta: josevaldo
  - projeto: scanplant
  - projectId: 979ef23a-b962-4098-8e88-38d4d0c07b40
- Development Build Android compilado com sucesso.
- Keystore Android criado e armazenado pelo EAS.
- APK instalado no aparelho Android.
- Build EAS:
  https://expo.dev/accounts/josevaldo/projects/scanplant/builds/6de1c73d-1c7f-4fd3-94a0-85132ef60ff9

## Atualização técnica — 21/08/2026

### Development Client e Metro por USB

- O Development Client Android foi aberto em aparelho físico Redmi A5, identificado pelo ADB como `25028RN03L`.
- Com `adb reverse`, foram encaminhadas as portas `tcp:8081` para o Metro e `tcp:5041` para a API.
- O log confirmou a abertura de `exp+scanplant`, a conclusão do bundle Android e a execução do aplicativo no aparelho.
- PT-04 está concluído: o Development Client carregou e executou fisicamente.

### Ambiente da API e validação automatizada

- O .NET 8 foi instalado localmente para o usuário no computador da faculdade.
- O PostgreSQL 18 estava em execução com o banco isolado `ScanPlantPhase0`; as migrations foram aplicadas.
- A API respondeu em `http://127.0.0.1:5041`; `GET /health` retornou `status: ok` e `environment: phase0`.
- O smoke test versionado `scripts/phase0/Test-Phase0Smoke.ps1` foi aprovado: `health` 200, `register` 200, `duplicate-register` 409, `login` 200, `auth-me` 200, `chats` 200, `auth-users` 200 e `plants` 200. Resumo final: `PASS=8 FAIL=0`.

### Validação manual no aparelho

Foram testados manualmente somente a abertura do aplicativo, o cadastro de uma conta descartável e a entrada na aplicação após o cadastro. Nenhuma outra tela ou funcionalidade foi declarada testada pela interface.

### Correção de configuração da API

- Em `ScanPlant-Final/components/apiConfig.js`, o health check passou a consultar `http://HOST:5041/health`.
- Os endpoints normais permanecem em `http://HOST:5041/api`.
- Foram preservados a descoberta sequencial, o timeout e a ausência de logs sensíveis.

## Situação da prova técnica

- PT-04: concluído.
- PT-05: concluído em 21/08/2026 no Redmi A5 (`25028RN03L`, Android 15, arm64-v8a).
- Build EAS usado: https://expo.dev/accounts/josevaldo/projects/scanplant/builds/3811afb7-648f-4e28-84d9-ee38dbf73b87
- Com Wi-Fi e dados desligados, o Development Client recebeu o bundle somente por `adb reverse tcp:8081`, carregou o MobileNet V1 TFLite empacotado, leu 1.001 labels, gerou RGB `224×224×3` (150.528 bytes) e concluiu CPU em 1.652 ms.
- Resultado determinístico: Top-1 `daisy` (score quantizado 252), `passed: true`. Esta prova valida inferência local TFLite; não afirma precisão botânica por espécie do produto.
- PT05_STAGE completo e índice sanitizado: `evidence/pt05/INDEX.md`. APK, logs completos e screenshots permanecem locais e ignorados.
- Wi-Fi e dados móveis foram restaurados após a prova. A Fase 0 está 100% concluída. Não iniciar a Fase 1 sem nova autorização.
