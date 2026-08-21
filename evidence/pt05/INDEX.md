# Evidência sanitizada — PT-05

Data: 21/08/2026 16:40 BRT
Build EAS: `3811afb7-648f-4e28-84d9-ee38dbf73b87`
Dispositivo: Redmi A5 (`25028RN03L`, Android 15, arm64-v8a)

Resultado: aprovado. Com Wi-Fi e dados móveis desligados, o Development Client recebeu o bundle somente pelo `adb reverse tcp:8081`, carregou o modelo TFLite empacotado e executou a inferência CPU.

Sequência confirmada:

`screen-mounted → labels-start → labels-loaded (1001) → image-start → image-loaded → decode-start → decode-finished (240×240) → model-start → model-loaded (1001) → inference-start → inference-finished (1001)`

`PT05_RESULT`: Top-1 `daisy`, score quantizado `252`, buffer RGB `150528` bytes, duração `1652 ms`, `passed: true`.

Conectividade final: Wi-Fi e dados móveis restaurados. A única reversão mantida é `tcp:8081` para o Metro USB.

Artefatos locais não versionados: APK EAS, logs completos do ADB/Metro e screenshots em `evidence/pt05/`; eles são reproduzíveis e podem conter ruído de sistema.
