# P03-R6 / U-009 — preparação offline preservada

Tipo: checkpoint de continuidade não canônico.

Branch funcional:

bm/v2-p03

Revisão funcional:

79f2a5a834c2678130a3d44c81373a8b75a0d29d

Digest aprovado P03-R6:

18cef0bf86bc6eecfaa10a8ee241e0c4fa3d543fbcdcd90cca75d6b661c032e1

## Estado

U-009 permanece reservada e não autorizada.

campaign_count=1
campaign_executed=false
U-009=reserved_not_authorized

Nenhuma campanha foi executada durante esta preparação.

Não foram executados restore, build, testes, Stryker ou mutantes.

## Preparação anterior

/var/tmp/p03-r6-u009-prepared.3nxiyJ

A preparação anterior foi preservada integralmente em:

previous-preparation/

## Preparação corrigida

/var/tmp/p03-r6-u009-prepared-offline.N4w7Ls

Preservada integralmente em:

new-preparation/

Launcher SHA-256:

6cc75d09946043233bbfb996a35e85f8a0b93b1890f18e0c0b9a3336347d6438

Configuração SHA-256:

07f34de6a941f022ae1de64597442bd54a6b31ba6dd265f4a22c1b59527339dd

## Isolamento NuGet

RestoreConfigFile aponta para o NuGet.Config local da preparação.

RestoreSources aponta exclusivamente para:

/tmp/p03-r5-u007.h8rfIr/local-feed

NUGET_PACKAGES aponta para:

/var/tmp/p03-r6-host-preflight.Yw7rqr/nuget-packages

NuGet.Config contém <clear /> e somente o feed local.

RestoreIgnoreFailedSources=false.

Não é usado --ignore-failed-sources.

A futura execução usa namespace de rede isolado via:

unshare --user --map-root-user --net

## Stryker

A inspeção estática local do Stryker 4.16.0 indicou que --no-restore
não é suportado.

A flag não foi adicionada.

## SHA256SUMS

A preparação corrigida valida SHA256SUMS entrando primeiro em RUN_DIR,
portanto a validação é independente do cwd do chamador.

## Comando futuro — NÃO AUTORIZADO

U009_AUTHORIZATION=granted /var/tmp/p03-r6-u009-prepared-offline.N4w7Ls/u009-campaign-launcher.sh

Esse comando está registrado apenas para continuidade.

Não foi executado neste checkpoint.

## Caches

Os bytes do feed local e do cache NuGet não são versionados neste
checkpoint.

Seus inventários e SHA-256 completos estão preservados em manifests/.

Este checkpoint não concede U-009 e não autoriza campanha.

Checkpoint UTC: 2026-09-09T04:04:43Z
