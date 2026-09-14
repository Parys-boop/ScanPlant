# Mudança contratual delimitada — P05-R1 / U-201

## Objetivo e fronteira

D-211, D-213, U-201. Aplicar futuramente a decisão humana de inelegibilidade de quatro
aliases homônimos, preservando sua evidência nomenclatural. O contrato completo esperado
está em `docs/bianchini/changes/v2/spec-deltas/offline-class-manifest-p05-r1.md` (SD-201). Só a elegibilidade authorless é replanejada;
nenhum arquivo de execução é alterado agora. P05 histórico permanece byte a byte e seu
digest não muda. O novo pacote aguarda aprovação própria; não substitui o aceite final.

## Regra pública e estados

D-211, A-211, P-211. Aloe maculata, Aloe variegata, Ficus clusiifolia e Ficus cordata
saem de synonyms resolvíveis e de scientific_map; resolve_scientific_name retorna None
após normalização aprovada. Quarentena é evidência explícita quarantined em taxonomy-review,
com autorias associada/conflitante, identidade conflitante, fontes, motivo e decisão U-201.
Sua sinonímia nas fontes é preservada. Autoria não vira chave nem é removida de entrada.
Qualquer outro homônimo encontrado bloqueia aceitação até revisão humana explícita.
Não há fuzzy, preferência por classe, aproximação ou resolução contextual.

Implementação futura deve rejeitar presença de um nome conhecido de Q no mapa,
inclusive reinserção no manifesto. Manifesto válido sem Q resolve os quatro para None;
manifesto adulterado com Q falha validação/mapa em vez de retornar uma classe.
Não exigir detecção automática de homonímia externa desconhecida: revisar elegibilidade
de cada alias com fontes existentes e não dar aceite se houver lacuna material.

Estado agora: política humana aprovada; P05-R1 planned/pending_approval, P05 blocked;
U-201 aberta para pacote, execução e aceite final. No futuro, após pacote aprovado,
commit/workspace e execução separadamente autorizados, produzir bytes/revisar e só então
registrar aceite humano vinculado aos hashes. Novo conflito ou teste falho impede conclusão.

## Invariantes e contagem

P-212, D-213. Preservar byte a byte roster e valores de classes exceto synonyms afetados;
12 espécies, todos os canônicos/comuns, IDs species_01–species_12/índices 0–11,
outra_planta/12, imagem_invalida/13, definições, normalização e namespaces inalterados.
Preservar ref_ids dos aliases restantes; referências de conflito ficam na evidência,
sem criar órfãs no manifesto. Não remover outro sinônimo elegível.

Usar o manifesto no checkpoint 77e93a como A0 imutável; prova local em
`artifacts/bianchini/v2/planning/p05-r1-preflight.json` mostra 83 aliases normalizados distintos e Q com quatro,
sem canônico sobreposto. Execução exige igualdade de conjuntos/mapeamentos
Afinal = A0 menos Q, diferenças por classe e nenhuma adição; esperado derivado 79,
mais 12 canônicos = 91 chaves. Se a prova divergir, parar e registrar a discrepância.

## Versionamento e arquitetura

D-212: propor manifest_version 1.1.0 conforme SemVer local que exige minor para mudança
de resolução. Preservar schema_version 1, normalization_version 1 e caminho .v1.json.
Atualizar futuramente validador/fixtures/relatório/docs de forma coerente com 1.1.0;
nenhuma alteração agora. Sem entidade de produto nova: Q é guarda do contrato documental
e registro de evidência; aliases continuam objetos name/ref_ids no schema existente.

Seams: normalize_name, scientific_map, resolve_scientific_name, validate_manifest e CLI.
Funções locais puras/somente leitura; sem concorrência, banco, migração, autenticação,
efeito externo ou integração. Não muda permissões/plataformas de produto. Sem interface,
design_required false; arquitetura manual/report-only não solicitada.

## Verificação e aceite

P-211, P-212, P-213, U-201. Uma unidade futura cobre alteração, regressão e documentação.
Testar todos os canônicos/aliases elegíveis; negativos dos quatro com caixa e whitespace;
reintrodução em cada classe; colisões canônico/alias/intra/interclasse; autoria não removida;
namespace comum separado; identidade/ordem/proteções/hash do roster preservados.
Asserções de conjunto com baseline independente impedem que remover outro alias passe
apenas por manter a contagem. Suite/CLI/checksums e revisão por fonte precedem aceite.

Atualizar relatório, docs, revisão, checksums e estado somente na execução futura. Parecer
humano final liga os hashes produzidos; se registrar parecer mudar bytes de evidência,
regerar seus checksums e submeter os bytes alterados. Preferir aceite em append no ledger
após selagem, para evitar ciclo de hashes. Nenhum approved fabricado.

## Segurança e execução

Perfil standard, parser low, grouped/plan_gate conforme policy registrada; nenhuma nova
ferramenta de mutação requerida. Máximo 3 fix rounds no seam existente, sem renomear
para zerar orçamento. Logs sanitizados e diagnósticos sem valores; JSON/JSONL estritos,
UTF-8/LF/newline, hashes e ausência de segredos/dados pessoais em todo delta planejado.
P01/P03-R6 e P02/P04/release preservados, nenhum novo teste de produto/campanha.
Sem rede taxonômica nesta rodada, provider, credenciais, imagens, dataset, treino,
modelo, integração, instalação, .NET/npm/Android/Docker/banco/Stryker.
Nenhum merge/staging/commit/push/implementação autorizado por este planejamento.
