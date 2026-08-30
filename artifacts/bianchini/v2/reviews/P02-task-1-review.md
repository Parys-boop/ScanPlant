# P02 Tarefa 1 — revisão de slice

**Veredito:** aprovado e pronto para revisão/commit; `critical: 0`, `important: 0`, `minor: 0`, `note: 1`.

## Spec

- O diff atende ao contrato da tarefa: `PhotoScreen` só chega a `identifyPlant` pelo botão `Continuar` do alerta de consentimento; `Recusar` não tem callback de rede.
- `api.js` envia exclusivamente o multipart `image` e `consentToExternalProcessing=true` ao endpoint ScanPlant, com JWT já armazenado. Não há header, URL ou chave de provider externo no fluxo móvel.
- O mapeamento contém todas as falhas neutras exigidas: 400, 413, 415, 429, 502, 503 e 504. A imagem segue preservada em estado em qualquer falha.
- P01 não foi alterado e sua condição `blocked` não foi inferida como conclusão.

## Qualidade

- O multipart não fixa `Content-Type`; isso preserva o boundary gerado pelo runtime React Native.
- O teste local verifica o seam de consentimento/API-only sem rede, segredo, provider ou banco. `git diff --check` e a sintaxe de `api.js` passaram.
- A exportação web local da CLI Expo instalada pelo lockfile passou; a tela JSX também foi transformada por Babel. O lockfile não mudou.
- Não há efeito irreversível, persistência nova ou concorrência introduzida nesta slice.

## Nota

- O pacote determinístico do CLI contém somente o intervalo Git (`base..HEAD`) e fica sem diff enquanto a mudança permanece deliberadamente sem commit. A revisão acima examinou o delta local de `git diff 095f2e1514ccf12f4aeeae312e15702aacd5082b`; nenhum finding aberto resulta disso.
