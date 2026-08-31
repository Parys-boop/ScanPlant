# Ações externas do responsável — F1-BE01

## U-003 — aprovar campanha seletiva P03

Antes da execução, aprovar o plano P03 e exatamente uma campanha Stryker seletiva vinculada ao HEAD atual. Sem aprovação, manter P01 `blocked-terminal`.

## U-001 — merge autorizado antes da execução

Necessária antes de P01: autorizar atualização de `origin` e merge de `origin/master` em `phase1-bianchini`, sem rebase. A-002: a referência local analisada é `16d07f7`; a atualização remota falhou por resolução DNS de `github.com` nesta sessão. Não há fallback que autorize implementação antes desse merge; aguardar conectividade e autorização, repetir apenas o diff do ref atualizado e registrar a resolução.

## U-002 — credenciais somente para ativação/teste real

P01 pode prosseguir com fakes sem credencial. Para teste externo opt-in, disponibilizar `PlantNet__ApiKey` no ambiente/cofre do backend e definir `SCANPLANT_RUN_EXTERNAL_TESTS=1`; o teste permanece desabilitado sem ambos. `Groq__ApiKey` é necessário somente para habilitar enriquecimento real. Não colocar valores em Git, appsettings versionado, `.env.example`, bundle mobile ou log.
