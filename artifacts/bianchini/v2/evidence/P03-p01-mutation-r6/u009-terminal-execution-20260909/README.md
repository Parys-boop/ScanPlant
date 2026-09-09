# P03-R6/U-009 — execução terminal preservada

## Contexto

A única campanha U-009 autorizada foi invocada via Bash uma única vez após o preflight R6 aprovado. O launcher criou o marcador atômico antes de iniciar Stryker e a campanha terminou com exit code 134.

- `campaign_count_before=1`; `campaign_count_after=2`.
- `U-008=consumed_non_reusable`; `U-009=consumed`.
- `failure_stage=campaign`.
- Stryker 4.16.0 iniciou, analisou o projeto e falhou antes de produzir mutantes ou relatórios de mutação.
- O plano R6 determina que falha posterior ao marcador é terminal: não há retry nem nova autorização/campanha R6.

## Fatos dos logs

O `stryker.log` registra que Stryker falhou ao conectar a `vstest.console` após 90 segundos; no timeout, os processos 9090 e 9091 ainda estavam em execução. O log não registra total de mutantes, mortos, sobreviventes, ignorados, sem cobertura, timeout de mutante, erro de compilação por mutante ou mutation score. O diretório `output/` contém somente `.gitignore`.

## Diagnóstico de loopback

A observação efêmera independente está em `namespace-loopback-diagnosis.txt`. Ela prova que um novo namespace criado com `unshare --user --map-root-user --net` tinha `lo` sem a flag `IFF_UP`. Isso é consistente com a impossibilidade de conexões locais de VSTest dentro desse namespace, mas não prova sozinho causalidade exclusiva para a falha: a conclusão causal é inferida, não fato do log.

## Sanitização e integridade

A varredura de credenciais, tokens, segredos, variáveis privadas e dados pessoais não encontrou material de credencial. O `stryker.log` continha caminho de usuário local; somente esse segmento foi substituído por `<LOCAL_USER>` na cópia preservada. `SHA256SUMS` cobre todos os arquivos preservados, exceto ele próprio.

## Próximo estado permitido

P03-R6 permanece bloqueado terminalmente. Esta evidência não cria nenhum novo identificador, campanha ou autorização. Qualquer decisão posterior exige deliberação humana formal fora do plano R6.
