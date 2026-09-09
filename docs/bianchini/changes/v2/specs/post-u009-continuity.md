# Continuidade pós-U-009 — contrato de P04/F1-API01

## Objetivo, estados e limites

D-101, P-101, S-101: recomendar A e retomar o benchmark de providers do roadmap. P01/P03-R6 continuam blocked-terminal; P02 completed; release pending, sem RC. O ciclo v2 permanece aberto. `campaign_count=2`, `campaign_executed=true`, `U-008=consumed_non_reusable`, `U-009=consumed`, `exit_code=134`, `failure_stage=campaign`; contagens de mutantes e mutation score U-009 indisponíveis. Nenhuma execução adicional é permitida pelo R6.

Estados de P04: proposed → aprovado documentalmente → protocolo preparado → aguardando U-101 → evidência coletada → decisão revisada. Ausência de corpus, direito, limite de gasto ou prova real mantém a coleta not_run e o plano incompleto/bloqueado. Aprovação do plano não concede U-101 nem muda P01/P03. P04 não inclui restore/build/testes de produto, mutação, código de adaptadores, novos endpoints, configuração de provider, mobile, dados de treinamento, vídeo ou entrega de release. (D-102, A-102)

## Contratos preservados

O mobile usa apenas ScanPlant, com JWT e consentimento antes de transmitir; recusa não faz upload. O backend mantém imagem transitória validada, timeout/cancelamento sem retry, limites e erros neutros 400/413/415/429/502/503/504. Interfaces `IPlantIdentificationProvider`/`IPlantKnowledgeProvider` e DTO público não mudam. Groq é opcional; catálogo de cuidados offline não depende dele. Comparar um concorrente não o integra ao produto. Credenciais nunca entram em código, imagens, argumentos registrados ou evidência. (D-102, SD-101)

## Protocolo mínimo de comparação

O resultado é documental e não distribuível como software. Não criar framework, runner persistente ou adaptadores para o benchmark. A coleta é operada do lado backend/estação controlada, nunca do mobile nem de produção, usando requisições manuais da documentação oficial vigente; antes de qualquer transmissão, registrar método/endpoint/parâmetros sem segredo, versões, limites e autorização U-101. Nenhum comando de API desconhecida é presumido aprovado por este plano. Se a coleta exigir mudança de produto ou instalação nova, parar e registrar o impedimento.

Congelar um corpus piloto de **7 casos**, com origem, direitos/consentimento, SHA-256 e resposta de referência revisada: uma imagem válida para cada uma das cinco espécies do piloto F1-G01 (`Epipremnum aureum`, `Monstera deliciosa`, `Zamioculcas zamiifolia`, `Spathiphyllum wallisii`, `Dracaena trifasciata`, aceitando o sinônimo registrado `Sansevieria trifasciata`); uma outra planta com referência identificada; uma imagem decodificável sem planta. Não usar a fixture ImageNet como prova das espécies nem criar/reduzir o manifesto das 12 espécies do MVP. Sem metadados pessoais/localização ou imagem sem direitos. O tamanho reduzido limita a conclusão a uma comparação piloto, não valida acurácia de produção.

Pl@ntNet e Plant.id recebem os mesmos bytes, mesma ordem e uma chamada por caso: **14 chamadas no máximo**, concorrência 1, nenhum retry automático. Fixar timeout de 20 segundos por requisição, compatível com o default local documentado; timeout é resultado, não motivo para nova chamada. Falha após transmissão ou perda de contato conta no teto e fica registrada como resultado desconhecido/timeout; não presumir que o provider não recebeu. Salvar cada observação antes da próxima chamada e não retomar duplicando caso/provider já registrado. Interrupção antes da transmissão não fabrica resultado; parar com a matriz parcial.

Groq/Gemini: primeiro registrar se o complemento textual é necessário ao uso avaliado. Se não, marcar comparação não aplicável, fundamentada no caráter opcional e no catálogo offline obrigatório, sem remover comportamento entregue. Se sim, comparar **2 casos textuais fixos** derivados das espécies piloto nos dois providers, até **4 chamadas adicionais**, com a mesma disciplina. Necessidade, modelos e termos devem estar registrados antes da coleta, sem escolha automática de versão. (D-102, A-102, P-102, U-101)

## Artefatos, métricas e aceite

Destinos futuros em `artifacts/bianchini/v2/evidence/P04-f1-api01/`: `corpus-manifest.json`, `observations.json`, `terms-and-authorization.md`, `SHA256SUMS`. Decisão legível em `docs/phase1/F1-API01-benchmark-decision.md`. Imagens e respostas brutas só permanecem fora do Git em armazenamento controlado quando autorizado; versionar apenas metadados/observações sanitizados necessários. Nada de cache, binários ou credenciais. Ledger novo `artifacts/bianchini/v2/ledgers/P04.md`, append-only.

Manifesto: schema_version, case_id único, categoria, nome científico esperado/sinônimos, origem/direitos, consentimento, SHA-256 e critério de avaliação. Observações: schema_version, case_id, provider/modelo/versão, instante, request_id local não pessoal, status observado, duração_ms, top1 correto/incorreto/não avaliável, falha neutra, JSON válido, observação de privacidade e referência do registro sanitizado. Nunca inventar precisão quando o provider não responde. Para texto, registrar JSON estruturado, qualidade pt-BR, nome científico e afirmações sem suporte contra referência revisada.

A revisão reconcilia exatamente os IDs do corpus com cada provider, sem duplicação; separa not_run de falha, calcula acertos sobre denominadores explícitos, disponibilidade, latência mediana e pior caso **observados**, sem inferir SLA/p95 estatístico dessa amostra. Fontes oficiais de limites, preço, privacidade e validade do serviço devem ter data da coleta; os valores de agosto no roadmap não são prova vigente. Definição de gratuito preservada: volume acadêmico informado coberto sem compra obrigatória após trial, limites publicados, gasto bloqueável e substituibilidade.

Selecionar principal e secundário por esta ordem: direitos/privacidade e orçamento elegíveis; identificação correta nos casos de referência e rejeição/ausência de falsa certeza nos controles; falhas/estabilidade; latência observada como desempate. Secundário técnico pago/trial pode constar como comparação, mas não como alternativa gratuita aprovada. Se a evidência não permite seleção válida dos papéis exigidos, registrar conclusão limitada e impedimento; não marcar F1-API01 completed nem ativar o candidato. Preservar em todos os resultados a lacuna P01/P03 e release pending. (SD-101, P-101, P-102)

## Garantia proporcional e reutilização

A-101: ledgers P01/P02 e comparação estática dos caminhos sustentam reutilizar provas históricas, sem executá-las novamente por este delta documental. O verificador seletivo histórico passou, mas a falha de lifecycle mantém P01 bloqueado; não há transferência de score ou fingerprint para U-009/RC.

P04: risco medium, execution slice, review per_slice, change documentation; policy retorna mutation not_required porque não há lógica material ou contrato de produto alterado. Gate rápido: parser dos JSON produzidos e diff --check. Gate do plano: reconciliação/revisão da matriz, fontes/autorização, cálculo independente das métricas, segredos e checksums. Não criar testes de produto para validar documentação. Se aparecer necessidade de alterar um seam, esta execução para nesse limite e não usa essa classificação documental para dispensar seus testes. Release continua bloqueado nos gates históricos e requer a garantia/homologação própria; P04 não os substitui.

## Lição de isolamento — restrição para qualquer proposta futura

D-103, P-103: P04 não inicia processos isolados e não faz experimentos de localhost/VSTest. A leitura do diagnóstico U-009 revelou `0x9 & 0x1 = 0x1`: o texto preservado que afirma ausência de IFF_UP é contraditório. Fato comprovado é o timeout de conexão, não a causa exclusiva. A evidência original não será corrigida in-place.

Se outro plano futuro realmente envolver isolamento, antes de aprovação de execução e de qualquer marcador irreversível ele deverá materializar e provar, na **mesma fronteira real**:

1. Caminho, hash, cwd, ambiente e forma exata de invocação do launcher; bit executável válido ou uso explícito de Bash, sem alterar conteúdo aprovado.
2. Estado administrativo do loopback com teste correto de IFF_UP; IPv4/IPv6 que o controlador usa; comunicação TCP local controlador/VSTest e criação/conexão de filhos no mesmo namespace e política do executor.
3. Namespace sem conectividade externa, mas com localhost funcional. Apenas conseguir executar `unshare --user --map-root-user --net -- true` não prova comunicação.
4. Espaço/inodes disponíveis em /tmp e /var/tmp; insumos duráveis fora de /tmp, persistência após reinício do WSL e compatibilidade de links sem substituição destrutiva.
5. Feed/cache locais por manifesto e hashes; SDK/Stryker exatos; solução/projetos explicitamente selecionados; nenhum restore/fonte remota implícita.
6. Timeout e limites de espera, caminhos de progress/stryker/exit/output, captura de lifecycle e comportamento em interrupção/perda de sessão: verificar processo, marcador e logs antes de agir, nunca presumir não início.
7. Consequência precisa do marcador e contagem monotônica: falha posterior consome a oportunidade e não permite repetir; prova anterior jamais cria marcador real.

A prova de comunicação deve ser descartável, não consumível e independente de mutação, exercendo spawn/handshake local inclusive com VSTest somente sob autorização futura apropriada. É proibido usar a campanha real para testar essa fronteira. Este checklist não é novo plano operacional, revisão R6, identificador ou autorização de campanha.
