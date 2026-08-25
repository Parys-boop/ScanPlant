> **Documento histórico.** O estado e os próximos marcos foram consolidados em [`docs/PLANO_CANONICO_IA_HIBRIDA.md`](docs/PLANO_CANONICO_IA_HIBRIDA.md). Em caso de divergência, o plano canônico mais recente prevalece.

# Checkpoint de continuidade — 2026-08-24

## Estado do ScanPlant

- Repositório: `C:\Users\Administrador\Documents\Codex\ScanPlant`.
- Branch atual: `phase1-bianchini`.
- Checkpoint F1-G01: `9aa1d1979da2e9124399573d2a06cbfd6231f5e0` — `docs: registra gate F1-G01 da Fase 1`.
- Remoto esperado: `origin/phase1-bianchini`, no mesmo SHA do checkpoint.
- A árvore estava limpa no Git executado pelo Windows antes deste arquivo.
- A Fase 0 permanece concluída; não repetir seus testes sem nova necessidade explícita.
- A Fase 1 ainda não foi iniciada: não existe `.bianchini` no ScanPlant e não houve alteração de código, assets, dependências ou configurações do produto.

## F1-G01

- O gate documental está em `docs/phase1/F1-G01-matriz-modelos-botanicos.md`.
- Conclusão registrada: “Nenhum dos candidatos avaliados foi aprovado sob os critérios do F1-G01.”
- O próximo trabalho de produto não está autorizado por este checkpoint: qualquer treinamento, dataset, download de modelo, conversão ou revisão do escopo exige decisão e autorização separadas.

## Método Bianchini

- Clone oficial separado: `C:\Users\Administrador\Documents\Codex\bianchini-method`.
- Remote oficial: `https://github.com/felipebianchini2006/bianchini-method.git`.
- O clone foi atualizado por fast-forward para `a90be4f8445cbd6113541119cdd61a8ea714b2ea`.
- Versão declarada do pacote: `0.4.2`.
- Não há instalação concluída no perfil Codex Windows nem no perfil Codex do WSL.
- Não houve modificação do repositório oficial.

## Validação WSL e bloqueio atual

- Distribuição padrão: Ubuntu em WSL2; Python 3.14.4, Git 2.53.0 e Codex CLI 0.148.0 estavam disponíveis.
- A prova controlada no volume `/mnt/c` passou: criação, leitura, `os.open` com `O_DIRECTORY`, `os.fsync` e remoção do diretório temporário funcionaram.
- A prova removeu seu próprio diretório; não restou `.bm-wsl-probe-*` nem `.bianchini` no ScanPlant.
- O Git do WSL, porém, reportou modificações em massa de arquivos rastreados, enquanto o Git do Windows reportou a árvore limpa. Não corrigir conversão de finais de linha, resetar ou limpar o repositório sem autorização específica.
- Por esse motivo, a suíte oficial do Método Bianchini no WSL, o `bm.py --help` e a instalação das skills não foram executados nesta etapa.

## Próxima retomada recomendada

1. Diagnosticar de modo somente leitura a divergência de status entre Git Windows e Git WSL, incluindo configurações de finais de linha.
2. Mediante autorização explícita para tratar essa divergência, restabelecer a árvore limpa também no Git do WSL sem alterar conteúdo de produto.
3. Com a árvore limpa no WSL, executar a suíte oficial do Método Bianchini e `python3 scripts/bm.py --help`.
4. Somente se todos os shards passarem, inventariar conflitos e instalar as dez skills oficiais e `_shared` no perfil Codex Linux conforme o README 0.4.2.
5. Não inicializar um ciclo Bianchini no ScanPlant sem nova autorização.

## Restrições preservadas

- Sem commit, push, merge, rebase, reset, checkout, restore ou clean além do commit e push deste checkpoint autorizados.
- Sem testes da Fase 0.
- Sem instalação de pacotes de sistema ou uso de `sudo`.
- Sem alteração de ACLs, Defender, dependências, código, assets ou configurações do produto.
