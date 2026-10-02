# P07 — revisão do commit de implementação

Commit revisado: `a2dfd8805527e6323334fcc0a7b7f45c63c7d3c9`; base `822954421019ad611d4d14dc5461cc7a495b7db4`. Exatamente 14 caminhos, digest dos bytes aprovados `b93852dfb4feef58050ed85fa4205838830a9cd9f660661e8857be80f4427c9e`. Não houve alteração funcional posterior.

U-701/U-702 estão aceitas em `human-acceptance.json` externo. `accepted-human-decisions.json` preserva a decisão explícita do responsável: 2 rejected_quality, 8 needs_botanical_review, 7 needs_human_review; approved_for_dataset=0, usable=0, treinamento não autorizado. Rascunhos anteriores permanecem imutáveis. A aprovação de pareceres não equivale a perícia ou aprovação de imagens.

O caminho de decisões usado em --finalize é accepted-human-decisions.json para preservar human-decisions.json como proposta histórica do agente. Python 3.14.4/Pillow 12.3.0 no ambiente persistente /home/administradorarthur/.cache/scanplant/venvs/p07. Ajustes de caminho classificados bounded_amendment; plano congelado.

As provas abaixo foram emitidas pelo guard com execução real no checkout isolado do commit. O gate externo executa a CLI de análise, finalização e segunda finalização, valida 17 imagens/29 arquivos intactos, 136 pares e idempotência de bytes/mtimes. Todos os exits foram zero. 38 testes P07 e 162 afetados/históricos. A síntese Git do commit ainda é o rascunho aceito; somente o stage será atualizado documentalmente para refletir U-701.

## Provas

- synthetic-curation-tests: `proof-fca4c4bd92cd9e94c748b1f3b29316a9`
- affected-history-tests: `proof-702b429455daac93e6c70137660d1b8f`
- source-hash-reconciliation-human-17-decisions-idempotence: `proof-8c72823f3a9eca5f4b01ca262494633a`
- final-human-acceptance-and-sanitization: `proof-00f5529960203f3c9a2dab050b120e18`
- class-manifest: `proof-de39c12718d99c3b60b171ea760175c9`
- summary-json: `proof-338f34640de3aee72aabd89643686186`
- state: `proof-08e5bee8cc7474aedaaa108c90fed406`
- planning-snapshot: `proof-7d77fab4cf528554dec244aa69e3835b`
- strict-planning-audit: `proof-0786842479cae680b9cab6f06cd255f5`
- historical-checksums: `proof-5a04787cc1b55a96f55b7899246e4bfd`
- repo-hygiene: `proof-8672227f3ab494522e5c4e1914e7b18a`
- diff-check: `proof-cc68d0acc031dc78174ab33c2291ee5d`
