# Checkpoint — Fase 0 offline

Data: 20/08/2026
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

## Bloqueio atual

## Atualizacao da validacao local

- PT-04 e login foram validados anteriormente e nao devem ser repetidos manualmente.
- A causa do erro 42703 em /api/plants foi confirmada: EnsureCreated nao atualiza tabelas preexistentes; o ScanPlantDB antigo nao recebeu IsInCommunity e IsLocationPublic.
- O ScanPlantDB permanece uma divida tecnica e nao deve ser alterado nesta fase.
- Foi preparada a rotina scripts/phase0/ para ambiente, API isolada, Metro/ADB, logs filtrados e smoke test de cadastro, login, usuario atual, chats, usuarios e plantas.
- Confirmacao fisica ainda pendente: abrir o Development Client e observar o carregamento do bundle do Metro; nao repetir login.
- Evidencias locais: `dotnet build --no-restore` passou; parser do Windows PowerShell 5.1 passou; `Test-Phase0Environment.ps1` passou; `npx.cmd expo-doctor` passou 17/17.
- A execucao integrada da API/smoke permanece pendente da senha local do PostgreSQL para iniciar o banco isolado. O smoke falha de modo controlado quando `/health` nao confirma `phase0`.

O Development Client foi instalado e aberto, mas ainda não carregou o JavaScript do Metro.

Tentativas realizadas:

- conexão LAN em 192.168.15.23:8081 falhou por timeout;
- celular e computador chegaram a ficar na mesma sub-rede;
- endereço /status não ficou acessível no celular;
- túnel do Expo falhou com "ngrok tunnel took too long to connect";
- a rede do computador provavelmente bloqueia LAN e ngrok.

## Próxima ação

Continuar em outro computador usando um cabo USB e ADB:

1. instalar ou localizar Android SDK Platform-Tools;
2. ativar Depuração USB no celular;
3. confirmar o aparelho com `adb devices`;
4. executar `adb reverse tcp:8081 tcp:8081`;
5. iniciar `npx.cmd expo start --dev-client --localhost --clear`;
6. abrir o aplicativo e validar o carregamento.

A pasta Platform-Tools foi baixada neste computador em Downloads, mas o executável adb ainda não foi localizado/validado.

## Situação da prova técnica

- PT-04: build criado e APK instalado; falta validar o carregamento completo do projeto no aparelho.
- PT-05 em diante: ainda não iniciadas.
- react-native-fast-tflite ainda não foi instalado.
- modelo TFLite ainda não foi integrado.
- teste de classificação offline ainda não foi executado.
- não avançar para a Fase 1 antes da decisão final da prova técnica.
