# Review Package

- Base: `7981377a433270c9e2072fcafdf89b690988fa08`
- Head: `HEAD`
- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md` (a9420f4134acc70580b544e268abe04d2f2b9e5056fbb82fc0b4a9e36a088b36)
- Report: `artifacts/bianchini/v2/codex/P08/fix-B1/implementer-report.md` (29f0379d43191f8030a94edf9496e43a15bbe2a3e636e660ef2ab6392ed28498)
- Security notice: sanitização heurística; 0 ocorrência(s) removida(s). Revise antes de compartilhar.

## Commits

```text

```

## Stat

```text

```

## Diff

```diff

```

## Uncommitted technical annex — not a submitted guard delta

The user prohibits commit/staging/push; this is independent technical review of round 1, not guard review. Review only B1 and actual delta regressions; return JSON findings. Reconstruct interrupted review from this package. No test rerun or mutations needed.

# Implementer Report — P08 B1, round 1

- Brief: `artifacts/bianchini/v2/codex/P08/task-brief.md`
- Status: TECHNICAL_FIX_READY_FOR_REVIEW; acceptance and commit pending.

## Changes

The preexisting fix in acquire_inat preserves str(error) only when error is RecoveryError and its code already belongs to RETRYABLE. All other caught errors retain inaturalist_contract_or_evidence. RETRYABLE itself is unchanged. The previous unconditional classification made a transient metadata timeout permanently skipped on restart by acquire.
Three existing synthetic tests cover timeout/restart/success, preserved journal prefix and config, cumulative request quotas, no premature page/cursor or candidate, one candidate exactly once, stable subsequent invocation, and fail-closed classification of contract/integrity/budget failures.

## Verification

Reused signed RED proof-6928ea925e6f438e3873543389326106 on original HEAD 7981377a433270c9e2072fcafdf89b690988fa08 only as historical defect evidence. Additional RED ran the three new tests against original production bytes (12 failed assertions). Reconciled current source/output fingerprints for GREEN: 3 new tests, 54 recovery, 15 adapter, 236 affected/history tests with five materially reached/killed selective mutants. These are working-byte records, not proofs for a future SHA. No test suite rerun during this resumption.
Fresh read-only Method preflight, diff check, complete evidence hash reconciliation and external bytes/mtime comparison passed. All unchanged suite dependencies match original HEAD; both modified files match the previous GREEN records. No network acquisition or downloads. See evidence-reconciliation.json.

## Decisions

Reuse round 1, existing correction, original commit and all documentary recovery. implementation_detail decision already recorded by bm change-policy. No start/red/fix command repeated. No staging, commit or push. The official review-package for base=head is an empty committed delta; its explicitly labeled working-tree annex enables technical review only. Formal submit-delta/review and fresh gates must wait for a separately authorized own commit.

## Concerns

Guard stays fixing, B1 open, round 1, redesign 0. P08 remains blocked, release pending. Historical human acceptance does not accept new bytes. External config/code fingerprint and old receipts remain intact and must not be silently migrated; new code is not authorized against the real dataset. 1088 pending candidates, zero transfers/approved_for_dataset/usable, no real iNaturalist crosswalk, no training, no P09.

```diff
diff --git a/scripts/phase1/recover_p08.py b/scripts/phase1/recover_p08.py
index 3def6c1..3e74f9b 100644
--- a/scripts/phase1/recover_p08.py
+++ b/scripts/phase1/recover_p08.py
@@ -549,21 +549,22 @@ def acquire_inat(ds,cls,transport,fixture):
                             taxonomic_confidence=initial['taxonomic_confidence'])
                 records.append(item)
             page=ds.save_page('inaturalist',cid,0,records,None)
             ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
                                       'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
         for c in page['candidates']:
             ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
         ds.advance(page)
         return 'budget_reached'
     except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
-        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':'inaturalist_contract_or_evidence'})
+        code=str(error) if isinstance(error,RecoveryError) and str(error) in RETRYABLE else 'inaturalist_contract_or_evidence'
+        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':code})
         return 'source_blocked'
 
 
 def acquire(ds,fixture=None):
     transport=Transport(ds)
     if fixture is not None:require(ds.offline,'fixture_mode')
     elif ds.offline:raise RecoveryError('fixture_required')
     for cls in canonical():
         for source in SOURCES:
             cid=cls['class_id']
diff --git a/scripts/phase1/test_recover_p08.py b/scripts/phase1/test_recover_p08.py
index aeb8b53..383cb8a 100644
--- a/scripts/phase1/test_recover_p08.py
+++ b/scripts/phase1/test_recover_p08.py
@@ -499,20 +499,124 @@ class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
             kinds = [event['type'] for event in ds.events]
             self.assertLess(kinds.index('page'), kinds.index('intention'))
             self.assertLess(kinds.index('committed'), kinds.index('cursor'))
         before = r.tree_fingerprint(self.root)
         (media/'123').unlink()  # A repeated execution must use the durable objects.
         process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
         self.assertEqual(process.returncode, 0, process.stderr)
         self.assertEqual(before, r.tree_fingerprint(self.root))
 
 
+class InaturalistResumeTests(DatasetCase, unittest.TestCase):
+    def prepare_round(self, request_cap=4):
+        from test_inaturalist_source import crosswalk, observation, page
+        cls = r.canonical()[0]
+        entry = crosswalk()
+        evidence = b'synthetic reviewed crosswalk evidence\n'
+        entry['taxonomy_ref_ids'] = cls['taxonomy_ref_ids']
+        entry['evidence'].update(path='evidence/crosswalk.json', sha256=r.sha(evidence))
+        self.config['crosswalk'][cls['class_id']] = entry
+        self.config['limits']['requests'] = request_cap
+        with self.open() as ds:
+            r.persist(ds.path(entry['evidence']['path']), evidence, immutable=True)
+            # Commons is already accounted for; exercise only the iNaturalist seam.
+            for item in r.canonical():
+                ds.append('source_status', {'source': 'commons', 'class_id': item['class_id'],
+                          'status': 'exhausted_within_query' if item['kind'] == 'species' else 'protection_not_queried'})
+        return cls, r.encode(page(observation()))
+
+    def test_timeout_then_restart_preserves_journal_limits_and_candidates(self):
+        cls, response = self.prepare_round()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertEqual([x['code'] for x in ds.select('response')], ['timeout'] * 3)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertEqual(ds.records(), [])
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [FakeResponse(body=response)])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 1)
+            self.assertEqual(len(ds.select('request')), self.config['limits']['requests'])
+            self.assertEqual(len(ds.select('response')), 4)
+            self.assertEqual(len({x['request_id'] for x in ds.select('request')}), 4)
+            self.assertEqual(len(ds.select('page')), 1)
+            self.assertEqual(len(ds.select('cursor')), 1)
+            self.assertEqual(len(ds.records()), 1)
+            self.assertEqual(ds.records()[0]['state'], 'needs_license_review')
+            self.assertEqual(ds.records()[0]['class_ids'], [cls['class_id']])
+            self.assertEqual(ds.select('intention'), [])
+            self.assertEqual(ds.select('committed'), [])
+            kinds = [e['type'] for e in ds.events]
+            self.assertLess(kinds.index('evidence'), kinds.index('page'))
+            self.assertLess(kinds.index('page'), kinds.index('classified'))
+            self.assertLess(kinds.index('classified'), kinds.index('cursor'))
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            self.assertEqual(ds.config['limits'], self.config['limits'])
+            self.assertEqual(ds.summary()['usable'], 0)
+        stable = r.tree_fingerprint(self.root)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 0)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+    def test_only_existing_transient_recovery_codes_allow_restart(self):
+        cls, _ = self.prepare_round()
+        errors = [(r.RecoveryError(code), code) for code in sorted(r.RETRYABLE)]
+        errors += [(r.RecoveryError(code), 'inaturalist_contract_or_evidence') for code in
+                   ['http_403', 'http_404', 'request_budget', 'crosswalk_evidence_hash', 'invalid_json', 'unsafe_url']]
+        errors += [(r.inat.ContractError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (OSError('timeout'), 'inaturalist_contract_or_evidence'),
+                   (KeyError('timeout'), 'inaturalist_contract_or_evidence')]
+        with self.open() as ds:
+            for error, expected in errors:
+                with self.subTest(error=type(error).__name__, code=str(error)):
+                    with patch.object(r.Transport, 'get', side_effect=error) as get:
+                        self.assertEqual(r.acquire_inat(ds, cls, r.Transport(ds), None), 'source_blocked')
+                    self.assertEqual(get.call_count, 1)
+                    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+
+    def test_timeout_restart_does_not_reset_request_budget(self):
+        self.prepare_round(request_cap=3)
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 3)
+            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
+        prefix = (self.root/'journal.jsonl').read_bytes()
+        config_bytes = (self.root/'config.json').read_bytes()
+        with self.open() as ds:
+            _, factory, _, _ = TransportTests.transport(self, ds, [])
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(factory.call_count, 0)
+            self.assertEqual(len(ds.select('request')), 3)
+            self.assertNotIn(ds.select('source_failure')[-1]['code'], r.RETRYABLE)
+            self.assertEqual(ds.records(), [])
+            self.assertEqual(ds.select('page'), [])
+            self.assertEqual(ds.select('cursor'), [])
+            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
+            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
+            stable = r.tree_fingerprint(self.root)
+            self.assertEqual(r.acquire(ds), 1)
+            self.assertEqual(r.tree_fingerprint(self.root), stable)
+
+
 class ContinuationProofs(DatasetCase, unittest.TestCase):
     def test_inspect_html_identical_after_journal_reload(self):
         with self.open() as ds:
             ds.ingest(candidate(),lambda _:image_bytes())
             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
         before=r.tree_fingerprint(self.root)
         with self.open() as ds:
             with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
         self.assertEqual(before,r.tree_fingerprint(self.root))
 

```

### artifacts/bianchini/v2/codex/P08/task-brief.md

```text
# Task Brief 1

- Plan: `docs/bianchini/changes/v2/plans/P08-dataset-recovery.md`
- Plan SHA-256: `1d7e4dd67033c9ff28ebf5a2463c12b5ff7b9795b2701b899addafc12ba1acfe`
- Kind: `task`
- Group ID: `n/a`
- Group SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`
- Unit `1` SHA-256: `33f19d884ecfc39bc7e8737428091955e08e0a20301540d23ab286eeac94c8af`

### Tarefa 1 — obter e preservar candidatos com decisões rastreáveis e aceite final

**Execution:** strict
**Review:** per_task
**Change:** data-transform
**Readiness refs:** D-801, D-802, D-803, D-804, D-805, A-801, A-802, P-801, P-802, U-801, U-802, U-803, U-804, S-801, SD-801
**Test seams:** p08-source-contract, p08-taxonomic-map, p08-journal-integrity, p08-sanitization, p08-human-approval.
**Spec refs:** docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md §1 autoridade; §2 arquitetura/CLI; §3 fontes/limites; §4 taxonomia/consultas; §5 direitos/storage; §6 journal; §7 triagem/estados; §8 resultado; §9 testes/aceite.
**Files:** criar scripts/phase1/recover_p08.py, scripts/phase1/inaturalist_source.py, scripts/phase1/test_recover_p08.py, scripts/phase1/test_inaturalist_source.py, scripts/phase1/test_p08_mutation.py, docs/phase1/P08-recovery.md, artifacts/phase1/p08/summary.json e artifacts/bianchini/v2/ledgers/P08.md; atualizar somente campos P08 de docs/living/PROJECT_STATE.md no fechamento futuro. Ler funções puras acquire_commons.py/curate_p07.py, requirements-p06.txt, manifesto canônico/roster e evidências P07; esses arquivos históricos permanecem inalterados. Config, crosswalk, imagens, journal, decisões e atribuição somente no diretório externo autorizado por U-802.
**Contract:** cumprir integralmente §§1–9 da spec. Após U-801 e autorização separada de implementação, construir extensão delimitada com stdlib/Pillow existente. RED deve comprovar que cada fronteira nova falha antes da implementação; GREEN cobre fixtures e replay. Não promover confiança comunitária a perícia, licença abreviada a autorização, título a taxon ID ou sanitização a privacidade. Commons+iNaturalist condicionais; demais fontes blocked, tetos 100 candidatos/20 transferências por fonte/classe, limites cumulativos de bytes/páginas/requisições. Preservar original servido e sanitizado por SHA, sem alegar original de câmera iNaturalist. Journal precede side effects e não reescreve eventos. A mesma entrega incorpora correção mínima do estado P07 publicado, já materializada documentalmente neste pacote.
**Verification:** no cwd da worktree P08, usar Python persistente P07 3.14.4/Pillow12.3.0. Fast: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_recover_p08.py'` e o mesmo comando com `test_inaturalist_source.py`; esses dois arquivos são entregáveis futuros, não testes alegadamente existentes. Plan: `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B -m unittest discover -s scripts/phase1 -p 'test_*.py'`, incluindo harness seletivo test_p08_mutation.py criado na entrega; `/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python -B scripts/phase1/validate_offline_manifest.py --manifest docs/phase1/offline-class-manifest.v1.json --roster artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json`; `sha256sum -c --strict artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS`; `git diff --check`. Gate espera saída 0, todos contratos executados, zero sobrevivente material dos cinco desvios §9, não número arbitrário de testes. Ambiente ausente bloqueia, não instalar automaticamente. Rede real só após U-802/U-803 e contratos offline passed; verify futuro prova journal, hashes/P07 17/17, aceites e allowlist. Gate release histórico continua blocked e não será executado ou substituído por unittest.
**Done when:** uma rodada autorizada contábil para as 14 classes, com esgotamento/limite/bloqueio por fonte explícito, originais/sanitizados/backup íntegros, P07 17/17 preservados, testes e revisão independente passed, parecer humano final por item incluindo pendências legítimas, atribuição completa e recibo U-804 do digest final. Falta de perito mantém pendências, podendo aceitar resultado zero; falta de autorização de execução/aceite ou falha de integridade impede completed. Zero aprovado e treinamento bloqueado são resultados válidos; nenhum mínimo de piloto, suficiência, split ou treino será criado.

Sequência dentro da unidade: confirmar autorização/workspace/baseline; validar manifesto/crosswalk/config; produzir RED/GREEN do percurso completo fake; implementar transporte/journal/curadoria/exportação limitados; executar regressão/mutação seletiva/revisão; somente com U-802, autorizar efeitos externos em rodada limitada; inspecionar/reconciliar com P07; obter U-803 por item e preservar inconclusões; gerar relatórios/backup/manifesto de bytes; obter U-804 e encerrar documentalmente. Revisão humana de fonte/ID/licença é requisito antes do download quando necessário. Não inventar prova para ultrapassar essas pausas.

A-801/A-802 limitam incerteza: fontes podem não fornecer candidatos elegíveis nem IDs/licenças suficientemente documentados. Fallback é fonte/item bloqueado e resultado vazio, sem expandir API/host/licença. P-801 impede aceite indevido; P-802 exige lock/durabilidade/hash/allowlist. U-801 autoriza somente pacote; U-802 ambiente e rede, U-803 qualificação/crosswalk/parecer, U-804 bytes finais. Sem staging, commit, push, merge/tag ou execução nesta sessão de planejamento. Sem autorização futura explícita dessas operações.

```

### docs/bianchini/changes/v2/specs/p08-dataset-recovery-change.md

```text
# P08 — recuperação limitada e rastreável do dataset

## 1. Objetivo e autoridade

D-801, D-805, A-801, U-801: enfrentar a insuficiência P07 mediante candidatos novos, verificáveis e preservados. Baseline b6844f9129d9edf862ae7958d8f043d9bdd5bd84, P07 completed/publicado, guard completed sem blockers, U-701/U-702 aceitas, 17 imagens: 2 rejected_quality, 8 needs_botanical_review, 7 needs_human_review, 0 approved_for_dataset/usable. As 14 classes estão sem aprovação; species_04 e species_08 e as duas proteções sem candidatos. Aceite anterior aceitou pareceres, não qualidade/identidade botânica das imagens. P06/P07 fechados não são reabertos. Preservar bloqueios históricos P01/P03 e release pending.

Só planejamento autorizado agora, sem código, rede de aquisição, download, staging, commit ou push. Aprovar este pacote não executa a coleta nem autoriza publicação. Excluídos do P08 treinamento, comparação de modelos, augmentation, partições train/validation/test, exportação TFLite, integração mobile/API, fluxo do produto, homologação, release, P09, merge/tag. Sem interface: design_required=false. Sem benchmark de modelo ou meta de suficiência.

## 2. Arquitetura delimitada

S-801, P-802: Python/Pillow 12.3.0/stdlib em Linux/WSL. Criar scripts/phase1/recover_p08.py como CLI/orquestração limitada e scripts/phase1/inaturalist_source.py como adapter; reutilizar funções puras de acquire_commons.py e curate_p07.py sem alterar contratos ou outputs P06/P07. CommonsClient existente pode servir consulta, mas transporte P08 deve impor Retry-After/orçamento de rede; nunca herdar sua pausa 0.25s como suficiente. Não chamar collect/_collect_locked P06 nem reconcile/run/validate_decisions P07 para dados novos: schemas fixos e journal inadequado. Métricas JPEG reutilizadas; para PNG usar mesmas funções de pixels sem transcodificar a imagem de dataset só para satisfazer P07. Nenhuma nova dependência pesada ou atualização de Pillow.

Seams públicos: p08-source-contract, p08-taxonomic-map, p08-journal-integrity, p08-sanitization, p08-human-approval. Externos: APIs públicas de metadados e hosts de mídia explicitamente permitidos; armazenamento local privado; revisor humano. Não há integração no app/API do ScanPlant. Configuração versionada de execução declara versão de schema, digest do manifesto, políticas/consultas/limites, fingerprints de código/ambiente e fontes; mudança material invalida retomada, não migra silenciosamente.

CLI futura (contrato a implementar, não comandos existentes): recover_p08.py com subcomandos acquire, inspect, finalize e verify. acquire exige --config e --output; inspect exige --output e --p07-source; finalize exige --output e --decisions; verify exige --output, --p07-source e, no fechamento, --acceptance. Um --offline-fixture para testes deve impedir toda rede e usar fixtures geradas fora do Git. Sucesso limitado/zero retorna 0; fonte/gate indisponível retorna 1; configuração/schema/hash/IO inválido retorna 2. Saída textual contém códigos seguros, não corpos HTTP/proveniência. Nenhum comando implementado ou executado neste planejamento.

## 3. Fontes e limites

D-802/D-803, A-802, U-802: após autorização separada de execução, Commons e iNaturalist são fontes elegíveis somente pelos contratos abaixo. GBIF, cache GBIF, publishers genéricos, PlantCLEF, Pl@ntNet-300K e qualquer fonte não listada têm acquisition_enabled=false, teto 0. Sem fallback silencioso de fonte/licença. Fonte elegível que não comprove schema/termos necessários termina blocked_source; não força atividade em outra fonte.

Commons: GET https://commons.wikimedia.org/w/api.php, generator=search, namespace 6, nome científico canônico entre aspas, imageinfo url/mime/size/timestamp/sha1/extmetadata. Usar continue/gsroffset validados, guardar página pendente/índice antes de avançar. Mídia apenas HTTPS upload.wikimedia.org, URL original retornada, sem thumbnails. ID de arquivo pageid/revisão é identidade da mídia; não é ID taxonômico. Sem inferência de espécie por categoria/título isolado.

iNaturalist: GET público https://api.inaturalist.org/v1/observations, taxon_id do crosswalk aprovado, photos=true, quality_grade=research, order_by=id, order=asc, per_page=100; confirmar filtros/shape no schema oficial durante implementação autorizada e fixture de contrato. Taxon ID identifica espécie aceita, não aceitar descendente/híbrido automaticamente. Página/índice de foto e id_above após página consumida, checkpoint de cutoff temporal da rodada para não incorporar observações posteriores. Research grade filtra candidatos, nunca aprova. Dados/metadados da observação têm exame de licença independente. Fotos via HTTPS inaturalist-open-data.s3.amazonaws.com/photos/{photo_id}/original.{ext}, somente quando relação ID/extensão/URL estiver provada no contrato oficial/resposta. Não trocar string de thumbnail arbitrariamente. Páginas www.inaturalist.org/observations/{id} e /photos/{id} servem evidência; não scraper genérico. Link legal por foto deve comprovar versão. Se API trouxer apenas código abreviado, evidência legal humana complementar vinculada ao ID é obrigatória antes do download; falta implica needs_license_review sem baixar. Original aqui é o maior arquivo disponibilizado pelo serviço, que pode ser redimensionado; origin_fidelity=provider_original, camera_original_verified=false. Não inventar acesso à câmera nem baixar dumps do Open Data.

Tetos cumulativos da rodada, persistidos inclusive entre invocações: por fonte/classe até 100 candidatos distintos examinados e 20 IDs reservados para transferência, mesmo que depois falhem/rejeitem. Commons até 10 páginas de 10; iNaturalist até 1 página de 100 observações, examinando no máximo 100 fotos, resto conhecido deferred_budget. Até 240 transferências distintas/fonte, 480 totais, não promessa de arquivos/aprovações. Repetir item para recuperação consome requisições/bytes, não cria vaga ou reseta teto. Proteções: zero consultas/transferências. Até 1000 requisições por fonte/rodada, 1 GiB de mídia total/rodada, 256 MiB/h; cada arquivo até 20 MiB, total recebido contabilizado mesmo em falha. Teto mais restritivo vence. Originais + sanitizados até 2 GiB para rodada; exigir ao menos 3 GiB livres no destino e parada segura antes de esgotar disco. São limites pequenos para revisar manualmente e conter custo, não número necessário para treino. Nenhum aumento automático se poucas aprovações.

Transporte: uma conexão global, ≥1s entre requisições, User-Agent identificável com URL pública do projeto. timeout 20s; até duas novas tentativas por requisição e orçamento global; 403/404 sem retry. 429/503/maxlag: respeitar Retry-After (segundos/data), maxlag=5 Commons, backoff 2/4s quando sem instrução; espera exigida maior que orçamento encerra com resume_after, nunca encurta espera. 500/502/504/timeout retomáveis no mesmo teto. Sem proxies/IPs/chaves para contornar quotas. Validar HTTPS, host/porta, redirects em cada salto e IP público; negar loopback/rede privada, userinfo, portas não padrão, traversal e URLs externas ao contrato. Mudança de host/termos exige nova autorização/avaliação, não expansão dinâmica de allowlist.

## 4. Taxonomia e consultas por classe

D-804, U-803, P-801: única verdade de IDs/ordem/nomes/normalização é docs/phase1/offline-class-manifest.v1.json 1.1.0, validado contra artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json. Os quatro aliases quarantined ficam excluídos; não expandir sinônimos nesta rodada. Nome comum não participa de busca/mapeamento. Não alterar manifesto/resolver. A tabela deriva do manifesto; divergência bloqueia.

| Índice | Classe | Nome científico e consulta Commons | iNaturalist |
| --- | --- | --- | --- |
| 0 | species_01 | "Epipremnum aureum" | taxon_id do crosswalk desta espécie |
| 1 | species_02 | "Monstera deliciosa" | taxon_id do crosswalk desta espécie |
| 2 | species_03 | "Zamioculcas zamiifolia" | taxon_id do crosswalk desta espécie |
| 3 | species_04 | "Spathiphyllum wallisii" | taxon_id do crosswalk desta espécie |
| 4 | species_05 | "Dracaena trifasciata" | taxon_id do crosswalk desta espécie |
| 5 | species_06 | "Aloe vera" | taxon_id do crosswalk desta espécie |
| 6 | species_07 | "Chlorophytum comosum" | taxon_id do crosswalk desta espécie |
| 7 | species_08 | "Codiaeum variegatum" | taxon_id do crosswalk desta espécie |
| 8 | species_09 | "Ficus elastica" | taxon_id do crosswalk desta espécie |
| 9 | species_10 | "Kalanchoe blossfeldiana" | taxon_id do crosswalk desta espécie |
| 10 | species_11 | "Nephrolepis exaltata" | taxon_id do crosswalk desta espécie |
| 11 | species_12 | "Tradescantia zebrina" | taxon_id do crosswalk desta espécie |
| 12 | outra_planta | sem consulta automática | not_applicable_automatic_query |
| 13 | imagem_invalida | sem consulta automática | not_applicable_automatic_query |

Não preencher IDs numéricos por memória: esta sessão não coletou taxa. Antes de consulta de imagens, um crosswalk externo revisado liga classe, fonte, source_taxon_id com namespace, scientific_name recebido, authorship quando disponível (null com razão quando ausente), rank/status/synonym_of, fonte/URL/versão/data da evidência e revisor. Usar referências taxonômicas já aprovadas no manifesto para reconciliação; ID da comunidade/Wikidata isolado não basta. Fonte sem ID confiável pode gerar candidatos Commons por nome canônico, mas nunca aprovação; iNaturalist sem crosswalk não é consultado. Conflito de autoria/homônimo => needs_botanical_review, sem reintrodução dos quatro aliases.

Cada item registra esse mapeamento e taxonomic_confidence=unmapped|proposed|source_supported|human_validated|conflict; human_validated exige perito identificado, qualificação e evidência visual diagnóstica do item final. IA/Plant.id/dHash/research_grade e sugestão do agente nunca satisfazem confirmação. Botânico pode rejeitar identidade ou declarar inconclusivo. Proteções mantêm definições P05; rejeição técnica não vira imagem_invalida, espécie desconhecida não vira outra_planta. Permanecem vazias, sem geração de exemplos negativos.

## 5. Direitos, entidades e armazenamento

D-803/D-805, P-801/P-802: preservar dados completos somente em diretório P08 externo novo autorizado, nunca P06/P07, Git, /tmp ou pasta compartilhada pública. Permissões diretório 0700/arquivos 0600; responsável mantém backup verificado por hash antes do fechamento. Não incluir originals em páginas de revisão abertas. Original baixado é immutable por SHA256 em originals; derivado sanitizado em quarantine; aprovação cria referência no catálogo, não altera bytes.

Registro privado por item: schema/run/config/manifest/code digests, candidate_id estável derivado de fonte+media_id, todas class associations, source/observation/photo/page/revision IDs, scientific_name recebido, source_taxon_id/namespace, authorship, mapping evidence/confidence/reviewer, query/cursor/timestamps, autor/licensor/credit, license code/version/legal URL/evidence hash, restrições e notices, source_page_url/file_url/resolved_url, MIME/dimensões declaradas/reais, source SHA declarado, original_sha256/sanitized_sha256, sanitization version, origin_fidelity, métricas/estados/razões, duplicate group e decisões humanas por hashes. Campos não disponíveis ficam null com reason, nunca valores inventados. HTML de origem é dado inerte, não renderizar como confiável. Não guardar coordenadas em projeções; snapshots probatórios integrais privados só quando indispensáveis para autoria/licença.

Exigir CC0 1.0 ou CC BY 4.0 com URL legal canônica e evidência por arquivo de titular/autoria/proveniência consistente. Divergência dos campos, multi-licença ambígua, restrição extra, domínio público genérico, NC/ND/SA ou licença ausente/outra versão => needs_license_review ou rejected_license; nunca baixar com base só no rótulo. Obter prova antes dos bytes. Autoria desconhecida bloqueia mesmo CC0 por política de rastreabilidade. Fonte pode ter direitos de banco/observação adicionais: examinar separadamente, bloquear incompatibilidade. Manter evidência temporal; alteração posterior de termos/metadados não apaga histórico nem revoga automaticamente licença anterior, mas suspende promoção até revisão de titularidade.

Attributions.jsonl/NOTICE.md privados ligam cada hash a autor/credit/licensor, título se necessário, página de origem, URL legal, avisos/disclaimer e indicação de alterações (orientação EXIF, RGB, recodificação, remoção de metadados). Gerar bundle de atribuição com cada redistribuição futura, inclusive CC0 por política. Redistribuição não está autorizada agora. BY/CC0 não exigem SA por si; não estender essa conclusão a contratos/terceiros nem declarar licença do futuro modelo/app. SA/NC/ND ficam bloqueadas nesta política. Treinamento requer decisão futura sobre dados efetivos, direitos e protocolo, mesmo com itens aprovados.

## 6. Journal, integridade e retomada

P-802: journal JSONL realmente append-only é autoridade; state/index/report são projeções reconstruíveis. Eventos com seq, timestamp UTC, event_id, prev_event_hash e event_hash (SHA256 de JSON canônico sem event_hash), config digest e tipo; JSON UTF-8/chaves ordenadas/LF final. Lock fcntl exclusivo por dataset; segundo escritor falha antes de rede. Validar prefixo/ordem/hash e hashes de objetos antes de continuar. Snapshot de página + candidatos e reservas durável antes de transferências; cursor só avança após todos os itens consumidos ou explicitamente deferred no checkpoint.

Sequência: reservar orçamento e registrar intenção/fsync; receber bytes limitados em .part externo; hash/verificação; persistir original por rename sem overwrite + fsync diretório; sanitizar/reabrir/verificar metadados e persistir sanitizado igualmente; append evento committed com ambos hashes/fsync; atualizar projeções atomicamente. Original de formato inválido recebido dentro do teto fica preservado em área restrita rejeitada, nunca decodificado em viewer; excesso interrompido não é original completo nem conta como íntegro. Nenhuma falha altera arquivos históricos.

Crash antes/depois de cada fronteira: replay reconcilia apenas objetos já vinculados a intenção e hashes; órfão não é aprovação. Arquivo existente íntegro não é baixado/recodificado; mesmo input/decisão repetido não adiciona evento nem muda bytes/mtime de projeções. Retry de tentativa fracassada adiciona evento e consome orçamento; idempotência não promete congelar API viva. Se original remoto muda, registrar nova revisão pendente, nunca substituir anterior. Journal com linha final parcial/corrupção bloqueia; não truncar/reparar automaticamente. Recuperação humana preserva arquivo original e prefixo validado em segmento novo ligado por digest, ou encerra blocked_integrity. Config/canonical digest incompatível, symlink/path escape, arquivo faltante ou hash divergente bloqueiam aprovação até reconciliação explícita; não reparar P06/P07.

## 7. Triagem e estados

D-804/D-805: aceitar JPEG/PNG, MIME/extensão/formato decodificado coerentes, um frame, até 20 MiB entrada/saída e 25 milhões pixels; verificar corrupção/truncamento/bombas. Aplicar orientação EXIF e reconstruir pixels RGB com função P06 (JPEG qualidade 95); remover EXIF/GPS/XMP/comentários/ICC/text chunks. Não cortar, borrar, melhorar exposição ou fazer augmentation; original intacto. Metadata retirada do arquivo não apaga avisos de atribuição externos. Reabrir arquivo final e confirmar ausência de metadados proibidos.

Métricas P07: menor dimensão <224, aspecto >3, média luminância <40 ou >215, frações pixels <=15 ou >=240 ≥25%, variância Laplaciana <100 geram sinais de revisão, não aceite/rejeição automática de conteúdo. Documentar transformação cinza 256x256 apenas analítica. Inspeção humana da imagem final em resolução disponível registra fotografia/ilustração, derivada, montagem, texto/marca d'água, órgão/espécime vivo ou seco/herbário, alvo único/delimitado, nitidez e exposição. Ilustração/montagem, texto que domina alvo, herbário inadequado ou alvo não identificável são rejected_quality com razão; dúvida => needs_human_review. Não remover marca d'água para tornar utilizável.

Privacidade visual: pessoas/rostos/corpos identificáveis, placas, números/endereço de residências, telas/documentos, localização e sinais sensíveis. Presença/risco não resolvido => rejected_privacy ou needs_privacy_review; ausência de EXIF não basta. Originais mantidos com acesso restrito para auditoria; não publicados. Botânico inspeciona imagem final, fonte e crosswalk; insuficiência => needs_botanical_review; incompatibilidade => rejected_label. Aprovação requer confirmação pericial explícita, não simples aceite de parecer do agente.

Dedup global: media ID, original SHA256, sanitizado SHA256, aliases de proveniência e dHash64 P07. Comparar novos entre si e contra os 17 SHA/dHash P07, inclusive rejeitados/pendentes, sem promovê-los/rejeitá-los novamente. Hash original P07 só se evidência histórica o possuir; não inventar original perdido. Recalcular dHash das cópias sanitizadas preservadas em leitura. Distância <=6 sinal near_duplicate; 7..10 borderline; >10 não prova diferença (pares P07 a distância35 reforçam revisão). Pares sinalizados e mesma observação/série exigem decisão humana distinct/duplicate/pending; conflito de classe no mesmo objeto bloqueia todas associações. Rejeição exata por hash não apaga arquivo; ponteiro duplicate_of mantém referência. Grupo perceptual decidido por humano, nunca limiar como verdade.

Estados derivados de gates independentes: discovered, needs_license_review, needs_taxonomic_mapping, deferred_budget, transfer_failed, quarantined, needs_human_review, needs_privacy_review, needs_botanical_review, needs_duplicate_review, rejected_license, rejected_format, rejected_quality, rejected_privacy, rejected_label, rejected_duplicate, approved_for_dataset. Razões múltiplas preservadas; estado principal prioriza rejeição definitiva, depois pendências licença/taxonomia/transferência/técnica/privacidade/botânica/duplicidade e finalmente aprovado. approved_for_dataset exige todos gates passed, hashes íntegros, original preservado, atribuição pronta, revisão humana final+botânica pericial e pares resolvidos. Nenhuma flag computada promove automaticamente. Qualquer mudança de bytes/decisão/mapeamento invalida aceites dependentes.

## 8. Resultado, suficiência e conclusão

A-801, U-804: por classe/fonte informar teto operacional, encontrados (IDs examinados, não estimativa total da API), transferidos, tecnicamente íntegros, licença válida, rótulo pericial validado, aprovados, rejeitados e pendentes. Os gates são conjuntos independentes; aprovados pertencem à interseção, não somar contagens como funil automático. Contar global por objeto e por classe explicitamente, sem duplicação inflar approved. Todas 14 classes aparecem na ordem original.

Classe vazia distingue not_attempted/authorization_missing, no_crosswalk, source_blocked, exhausted_within_query, budget_reached, all_rejected, review_pending e protection_not_queried. Esgotar consulta não prova ausência universal da espécie. Minimum_experimental_pilot=null (não estabelecido neste escopo); scientific_sufficiency=not_demonstrated, production_sufficiency=not_demonstrated, training_authorized=false, partition_authorized=false, training_status=blocked. Usable representa aprovados para catálogo após aceite final, nunca autorização/suficiência de treinamento.

No Git só código/testes sintéticos futuros, manual P08 e resumo de enums/contagens/IDs internos opacos/classes/hash dos recibos e objetos aceitos. Nunca imagens/base64, paths privados, autores/revisores identificáveis, URLs de itens, GPS/EXIF, respostas brutas, HTML ou texto livre de pareceres. Relatórios externos incluem proveniência completa; exportação pública allowlist rejeita campo extra e é inspecionada por humano. Estado vivo recebe apenas referência sanitizada de resultado e conserva release pending/active_execution null ao terminar.

Conclusão do mecanismo+rodada exige todas classes contabilizadas, reservas/cursos/respostas reconciliados, journal válido, dados preservados/backup, comparação P07 17/17, testes/gates passed, revisão dos candidatos com estados explícitos (pendências legítimas), bundle de atribuição, relatório fiel, revisão independente e recibo U-804 dos hashes finais. Zero aprovadas, fontes bloqueadas e treino bloqueado podem ser conclusão aceita; falha não resolvida de integridade, licença indevidamente promovida, vazamento, acesso P07 ausente, gate indispensável indisponível ou ausência de aceite impedem conclusão. Interromper uma fonte por termos/limite não significa execução técnica total passed; relatar source_blocked e submeter resultado limitado ao humano. Não requer forçar candidato por classe nem resolver botânica inconclusiva.

## 9. Verificação futura e aceite

Uma unidade strict, risco high localizado de persistência/autoridade; perfil standard; revisão independente e RED/GREEN nos seams modificados. Testes sintéticos com transport fake e rede proibida: licenças/names/version/URL contraditórios, licença foto diferente observação, direitos de banco, falta autor, espécie homônima/alias quarantined/nome comum/source ID ausente, rótulo pericial false; todos gates booleanos e desconhecidos; JPEG/PNG válidos/truncados/limites 20MiB/25M/1 frame; EXIF/GPS/XMP e orientação; métricas abaixo/igual/acima dos limites; dHash 6/7/10/11 e duplicata exata cruzando fonte/P07/classe; imagens sintéticas de texto/montagem apenas exercitam sinais e estados, não alegam detector universal.

Fronteiras de IO: crash em cada etapa de §6, disco cheio/fsync/rename/linha parcial, arquivo órfão/faltante/corrompido, alteração config/manifesto, lock concorrente, malicious redirects/SSRF/symlink/traversal, esquema API incompleto, paginação repetida/regressiva, cursor no meio, teto atingido com zero aprovados, orçamento cumulativo após restart, Retry-After e cancelamento. Testar CLI success/zero/error/exit codes, replay byte+mtime estável e projeção allowlist. Contadores/report de 14 classes sem coerção para treino. P06/P07 regressão sem alteração de bytes.

Mutação seletiva requerida por policy: aprovar previamente harness stdlib unittest.mock em scripts/phase1/test_p08_mutation.py, sem instalação. Injetar, um por vez, bypass licença, bypass perito, ignore_hash_mismatch, advance_cursor_before_commit e allow_private_export; executar contratos focais em subprocesso e exigir falha do teste para cada desvio material. Harness prova alteração do ramo (não stub irrelevante), descarta cópia temporária externa após ensaio; gate falha se mutante sobreviver/nenhum teste rodar. Sem score global, sem reativar campanha .NET histórica. Evidência por fingerprint do código/testes e comandos; não executar mutação na fase fast nem agora.

U-804: manifesto final privado inclui journal/objetos/decisões/attribution/relatórios e resumo sanitizado; recibo separado aponta digest, revisor/data/escopo e decisão. Recibo não entra em seu próprio digest. Aceite verifica bytes finais e possibilidade legítima de zero/pendências; não equivale a treino. Alteração posterior exige novo recibo. Staging/commit/push futuros só após esse aceite e autorização explícita separada, nunca nesta sessão.

SD-801: contrato completo esperado em spec-deltas/dataset-recovery.md; current/specs congelado/ausente, sem sincronização neste planejamento.

```

### scripts/phase1/recover_p08.py

```text
"""P08 bounded recovery. Private datasets, append-only journal, explicit human gates.

No training or automatic botanical/privacy approval. P06/P07 are read-only inputs.
"""
import argparse
from collections import Counter
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import fcntl
import hashlib
from html import escape
import http.client
from io import BytesIO
import ipaddress
import json
import os
from pathlib import Path
import re
import shutil
import socket
import ssl
import stat
import sys
import time
from urllib.parse import urlencode, urlsplit, unquote, urljoin
import PIL
from PIL import Image
import acquire_commons as commons
import inaturalist_source as inat
from curate_p07 import dhash, flags_for, laplacian_variance
from validate_offline_manifest import validate_manifest

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT/'docs/phase1/offline-class-manifest.v1.json'
ROSTER = ROOT/'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json'
MAX_BYTES = 20*1024*1024
SOURCES = ('commons','inaturalist')
RETRYABLE={'timeout','network_error','response_timeout','http_429','http_500','http_502','http_503','http_504','maxlag','resume_after'}
STATES = {'discovered','needs_license_review','needs_taxonomic_mapping','deferred_budget','transfer_failed',
          'quarantined','needs_human_review','needs_privacy_review','needs_botanical_review','needs_duplicate_review',
          'rejected_license','rejected_format','rejected_quality','rejected_privacy','rejected_label',
          'rejected_duplicate','approved_for_dataset'}
LIMITS = {'candidates':100,'transfers':20,'pages':10,'requests':1000,'media_bytes':1024**3,
          'hour_bytes':256*1024**2,'storage_bytes':2*1024**3,'file_bytes':MAX_BYTES,'wait_seconds':60}
SHA = re.compile(r'[a-f0-9]{64}')
# Exact predecessor from the verified real round. The only behavior change is
# deterministic key ordering in review HTML; config and acquisition stay frozen.
HTML_ORDER_PREDECESSOR = '14c4b86cff4b82e9278ecb705bbb05bb429aaaf209a2cc385a6a1c881a0cfd57'

class RecoveryError(ValueError): pass

def require(condition,code):
    if not condition: raise RecoveryError(code)

def sha(raw): return hashlib.sha256(raw).hexdigest()
def encode(value): return (json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'),allow_nan=False)+'\n').encode()
def now(): return datetime.now(timezone.utc).isoformat(timespec='microseconds').replace('+00:00','Z')
def load(raw):
    def pairs(items):
        d={}
        for k,v in items:
            require(k not in d,'duplicate_json_key');d[k]=v
        return d
    try: return json.loads(raw,object_pairs_hook=pairs,parse_constant=lambda _: (_ for _ in ()).throw(RecoveryError('nonfinite_json')))
    except (UnicodeError,ValueError,TypeError): raise RecoveryError('invalid_json') from None

def safe_path(path):
    p=Path(os.path.abspath(path))
    require(not any(q.is_symlink() for q in (p,*p.parents)),'symlink')
    return p

def read(path):
    p=safe_path(path)
    with os.fdopen(os.open(p,os.O_RDONLY|os.O_NOFOLLOW),'rb') as f:
        require(stat.S_ISREG(os.fstat(f.fileno()).st_mode),'not_regular')
        return f.read()

def fsync_dir(path):
    fd=os.open(path,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
    try: os.fsync(fd)
    finally: os.close(fd)

def persist(path,raw,immutable=False):
    path=safe_path(path)
    if path.exists():
        old=read(path)
        if old==raw:return
        require(not immutable,'immutable_hash_mismatch')
    part=path.with_name('.'+path.name+'.'+os.urandom(8).hex()+'.part')
    fd=os.open(part,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'wb') as f: f.write(raw);f.flush();os.fsync(f.fileno())
    if immutable:
        try: os.link(part,path,follow_symlinks=False)
        except FileExistsError: require(read(path)==raw,'immutable_hash_mismatch')
        part.unlink()
    else: os.replace(part,path)
    fsync_dir(path.parent)

def tree_fingerprint(root):
    return {str(p.relative_to(root)):{'sha256':sha(read(p)),'mtime_ns':p.stat().st_mtime_ns}
            for p in sorted(Path(root).rglob('*')) if p.is_file()}

def fingerprint():
    return {p.name:sha(read(p)) for p in [Path(__file__),ROOT/'scripts/phase1/inaturalist_source.py',
                                        ROOT/'scripts/phase1/acquire_commons.py',ROOT/'scripts/phase1/curate_p07.py'] if p.exists()}

def canonical():
    m=load(read(MANIFEST)); validate_manifest(m,read(ROSTER))
    # The historic validator raises on contract violations and returns diagnostics.
    require(m['manifest_version']=='1.1.0' and len(m['classes'])==14,'canonical_manifest')
    return m['classes']

def default_config(offline=False):
    return {'schema_version':1,'run_id':'p08-recovery','manifest_sha256':sha(read(MANIFEST)),
            'code_sha256':fingerprint(),'python':'.'.join(map(str,sys.version_info[:3])),
            'pillow':PIL.__version__,'offline':offline,'cutoff':now(),'limits':dict(LIMITS),
            'sources':list(SOURCES),'crosswalk':{},'legal_evidence':{},'source_contracts':{},
            'user_agent':'ScanPlant-P08/1.0 (https://github.com/Parys-boop/ScanPlant; dataset-recovery)'}

def validate_config(c,offline):
    require(set(c)==set(default_config(offline)),'config_fields')
    require(c['schema_version']==1 and c['offline'] is offline,'config_mode')
    current=fingerprint();previous={**current,'recover_p08.py':HTML_ORDER_PREDECESSOR}
    require(c['manifest_sha256']==sha(read(MANIFEST)) and c['code_sha256'] in (current,previous),'config_fingerprint')
    require(c['python']=='.'.join(map(str,sys.version_info[:3])) and c['pillow']==PIL.__version__=='12.3.0','environment')
    require(c['sources']==list(SOURCES) and set(c['limits'])==set(LIMITS),'sources_limits')
    for k,v in c['limits'].items():require(type(v)is int and 0<v<=LIMITS[k],'limit')
    require(isinstance(c['crosswalk'],dict) and isinstance(c['source_contracts'],dict),'config_schema')
    require(c['user_agent'].startswith('ScanPlant-P08/') and 'https://github.com/Parys-boop/ScanPlant' in c['user_agent'],'user_agent')
    require(datetime.fromisoformat(c['cutoff'].replace('Z','+00:00')).tzinfo is not None,'cutoff')
    canonical()

def safe_url(url,source,media=False):
    require(isinstance(url,str) and not any(ord(c)<33 for c in url),'unsafe_url')
    p=urlsplit(url); host=({'commons':'upload.wikimedia.org','inaturalist':'inaturalist-open-data.s3.amazonaws.com'} if media else
                         {'commons':'commons.wikimedia.org','inaturalist':'api.inaturalist.org'})[source]
    require(p.scheme=='https' and p.netloc==host and not p.fragment and not p.username and not p.password,'unsafe_url')
    path=unquote(unquote(p.path));require('\\' not in path and '..' not in path.split('/') and path.startswith('/'),'unsafe_path')
    if not media:require(p.path==('/w/api.php' if source=='commons' else '/v1/observations'),'unsafe_endpoint')
    else:
        require(not p.query and Path(path).suffix.lower() in {'.jpg','.jpeg','.png'},'unsafe_media')
        if source=='inaturalist':require(re.fullmatch(r'/photos/[1-9][0-9]*/original\.(jpg|jpeg|png)',path),'unsafe_media')
    return url

def public_addresses(host):
    addresses=list(dict.fromkeys(row[4][0] for row in socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)))
    require(bool(addresses) and all(ipaddress.ip_address(a).is_global for a in addresses),'nonpublic_address')
    return addresses

def candidate_id(c): return 'C'+sha((c['source']+':'+str(c['media_id'])).encode())[:24]

def rights(c):
    allowed={'cc-by-4.0':({'CC BY 4.0'},'https://creativecommons.org/licenses/by/4.0/'),
             'cc0':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/'),
             'cc-zero':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/')}
    rule=allowed.get(c.get('license_id'))
    if not rule or c.get('license_name') not in rule[0] or c.get('license_url')!=rule[1]:return 'needs_license_review'
    if not c.get('author') or re.search(r'\b(unknown|anonymous|desconhecid[oa])\b',c['author'],re.I):return 'needs_license_review'
    if c.get('restrictions') or c.get('rights_consistent') is not True or c.get('database_rights')!='passed':return 'needs_license_review'
    if not isinstance(c.get('evidence_sha256'),str) or not SHA.fullmatch(c['evidence_sha256']):return 'needs_license_review'
    return 'passed'

def sanitize(raw,url,mime):
    try:
        clean,suffix=commons.sanitize_image(raw,url,mime)
        with Image.open(BytesIO(clean)) as im:
            im.load();require(not im.getexif() and not(set(im.info)&{'exif','xmp','XML:com.adobe.xmp','comment','icc_profile','text'}),'sanitization_metadata')
        return clean,suffix
    except commons.AcquisitionError:raise RecoveryError('invalid_image') from None

def technical(raw):
    with Image.open(BytesIO(raw)) as im:
        im.load();w,h=im.size;px=list(im.convert('L').resize((256,256),Image.Resampling.LANCZOS).get_flattened_data())
        mean=sum(px)/len(px);dark=sum(x<=15 for x in px)/len(px);bright=sum(x>=240 for x in px)/len(px)
        var=laplacian_variance(px,256,256)
        return {'decode':'ok','width':w,'height':h,'format':im.format,'dhash64':dhash(im),'mean_luminance':mean,
                'dark_fraction':dark,'bright_fraction':bright,'laplacian_variance':var,'flags':flags_for(w,h,mean,dark,bright,var)}

def review_digest(c):return sha(encode({k:v for k,v in c.items() if k not in {'state','decision'}}))

def decide(c,d):
    require(d.get('authority')=='human' and d.get('reviewer') and d.get('reviewed_at') and d.get('rationale'),'human_authority')
    require(all(d.get(k)==c.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256']),'decision_hash')
    require(d.get('evidence_digest')==review_digest(c),'stale_decision')
    if rights(c)!='passed':return 'needs_license_review'
    if not c.get('original_sha256') or not c.get('sanitized_sha256') or c.get('technical',{}).get('decode')!='ok':return 'rejected_format'
    for key,state in [('quality','rejected_quality'),('privacy','rejected_privacy'),('botanical','rejected_label'),('duplicates','rejected_duplicate')]:
        if d.get(key)=='rejected':return state
    for key,state in [('quality','needs_human_review'),('privacy','needs_privacy_review'),('botanical','needs_botanical_review'),('duplicates','needs_duplicate_review')]:
        if d.get(key)!='passed':return state
    if not (d.get('expert_confirmation') is True and d.get('qualification') and d.get('botanical_evidence') and
            isinstance(d.get('mapping'),dict) and d['mapping'].get('confidence')=='human_validated' and
            d['mapping'].get('source_taxon_id') and d['mapping'].get('evidence_sha256')):return 'needs_botanical_review'
    if len(c['class_ids'])!=1:return 'needs_botanical_review'
    cls=next(x for x in canonical() if x['class_id']==c['class_ids'][0]);mapping=d['mapping']
    if any(mapping.get(k)!=v for k,v in {'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],
                                        'rank':'species','status':'accepted','taxonomy_ref_ids':cls['taxonomy_ref_ids']}.items()):return 'needs_botanical_review'
    if not mapping.get('namespace') or not SHA.fullmatch(str(mapping.get('evidence_sha256',''))):return 'needs_botanical_review'
    visual=d.get('visual',{});privacy=d.get('privacy_checks',{})
    if set(visual)!={'photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'} or not all(v is True for v in visual.values()):return 'needs_human_review'
    if set(privacy)!={'people','faces','plates','residences','screens_documents','sensitive_location'} or not all(v=='absent' for v in privacy.values()):return 'needs_privacy_review'
    pairs=c.get('pairs',[])
    if any(p.get('signal')=='exact_duplicate' for p in pairs):return 'rejected_duplicate'
    if any(d.get('pair_decisions',{}).get(p['pair_id'])!='distinct' for p in pairs):return 'needs_duplicate_review'
    return 'approved_for_dataset'

class Dataset:
    def __init__(self,root,config,offline=False):
        self.root=safe_path(root);self.config=config;self.offline=offline;self.events=[];self.fd=None
        validate_config(config,offline);self.config_hash=sha(encode(config))
        require(ROOT not in self.root.parents and self.root!=ROOT,'dataset_in_git')
        if not offline:
            require(Path('/tmp') not in self.root.parents and self.root.name.startswith('p08-'),'private_p08_root')
            require(shutil.disk_usage(self.root.parent).free>=3*1024**3,'insufficient_disk')
    def path(self,name):
        require(isinstance(name,str) and not Path(name).is_absolute() and '..' not in Path(name).parts,'path_escape')
        return safe_path(self.root/name)
    def __enter__(self):
        self.root.mkdir(mode=0o700,parents=False,exist_ok=True)
        require(stat.S_IMODE(self.root.stat().st_mode)==0o700,'private_permissions')
        self.fd=os.open(self.path('.lock'),os.O_RDWR|os.O_CREAT|os.O_NOFOLLOW,0o600)
        try:
            try:fcntl.flock(self.fd,fcntl.LOCK_EX|fcntl.LOCK_NB)
            except BlockingIOError:raise RecoveryError('writer_locked') from None
            for name in ['originals','quarantine','parts','evidence']:
                self.path(name).mkdir(mode=0o700,exist_ok=True)
            self.replay()
            if not self.events:
                self.append('config',self.config)
                persist(self.path('config.json'),encode(self.config),True)
            else:require(self.events[0]['data']==self.config,'config_changed')
            self.verify_objects()
            if self.config['code_sha256']!=fingerprint():
                transition={'from':self.config['code_sha256'],'to':fingerprint(),'reason':'deterministic_review_html_key_order'}
                if transition not in self.select('code_compatibility'):self.append('code_compatibility',transition)
            return self
        except BaseException:
            os.close(self.fd);self.fd=None;raise
    def __exit__(self,*args):
        if self.fd is not None:os.close(self.fd);self.fd=None
    def replay(self):
        p=self.path('journal.jsonl')
        if not p.exists():return
        raw=read(p);require(not raw or raw.endswith(b'\n'),'journal_partial')
        prev='0'*64
        for seq,line in enumerate(raw.splitlines(keepends=True),1):
            e=load(line);require(set(e)=={'seq','timestamp','event_id','prev_event_hash','event_hash','config_sha256','type','data'},'event_schema')
            hashed={k:v for k,v in e.items() if k!='event_hash'}
            require(encode(e)==line and e['seq']==seq and e['prev_event_hash']==prev and sha(encode(hashed))==e['event_hash'],'journal_hash')
            require(e['config_sha256']==self.config_hash,'config_changed')
            self.events.append(e);prev=e['event_hash']
    def append(self,kind,data):
        require(self.fd is not None,'lock_required')
        e={'seq':len(self.events)+1,'timestamp':now(),'event_id':os.urandom(16).hex(),
           'prev_event_hash':self.events[-1]['event_hash'] if self.events else '0'*64,
           'config_sha256':self.config_hash,'type':kind,'data':data}
        e['event_hash']=sha(encode(e))
        fd=os.open(self.path('journal.jsonl'),os.O_WRONLY|os.O_APPEND|os.O_CREAT|os.O_NOFOLLOW,0o600)
        with os.fdopen(fd,'ab') as f:f.write(encode(e));f.flush();os.fsync(f.fileno())
        fsync_dir(self.root);self.events.append(e);return e
    def select(self,kind):return [e['data'] for e in self.events if e['type']==kind]
    def verify_objects(self):
        for e in self.events:
            d=e['data']
            if e['type'] in {'received','committed'}:
                for pathkey,hashkey in [('original_path','original_sha256'),('sanitized_path','sanitized_sha256'),('part_path','original_sha256')]:
                    if d.get(pathkey):require(sha(read(self.path(d[pathkey])))==d[hashkey],'object_hash_mismatch')
            if e['type']=='evidence':require(sha(read(self.path(d['path'])))==d['sha256'],'evidence_hash_mismatch')
    def records(self):
        result={}
        for e in self.events:
            if e['type'] in {'committed','classified'}:result[e['data']['candidate_id']]=dict(e['data'])
        return list(result.values())
    def record(self,c):return next((x for x in self.records() if x['candidate_id']==candidate_id(c)),None)
    def classify(self,c,state,reason):
        r={**c,'candidate_id':candidate_id(c),'state':state,'reasons':[reason]}
        self.append('classified',r);return r
    def save_page(self,source,class_id,cursor,candidates,next_cursor):
        require(source in SOURCES and class_id.startswith('species_'),'page_class')
        key=sha(encode([source,class_id,cursor]))
        old=next((p for p in self.select('page') if p['page_id']==key),None)
        if old:return old
        ids=[candidate_id(c) for c in candidates];require(len(ids)==len(set(ids)),'duplicate_page_ids')
        require(len(ids)<= (10 if source=='commons' else 100),'page_size')
        pages=[p for p in self.select('page') if p['source']==source and p['class_id']==class_id]
        require(len(pages)<(self.config['limits']['pages'] if source=='commons' else 1),'page_budget')
        if next_cursor is not None:require(type(next_cursor)is int and next_cursor>cursor,'cursor_regression')
        page={'page_id':key,'source':source,'class_id':class_id,'cursor':cursor,'next_cursor':next_cursor,'candidates':candidates}
        self.append('page',page);return page
    def advance(self,page):
        if page['page_id'] in [a['page_id'] for a in self.select('cursor')]:return
        done={x['candidate_id'] for x in self.records()}
        require(all(candidate_id(c) in done for c in page['candidates']),'cursor_before_commit')
        self.append('cursor',{'page_id':page['page_id'],'next_cursor':page['next_cursor']})
    def ingest(self,c,download,crash=lambda _:None):
        cid=candidate_id(c);old=self.record(c)
        if old and not (old['state']=='transfer_failed' and set(old.get('reasons',[])) & RETRYABLE):
            require(old['source']==c['source'] and old['file_url']==c['file_url'],'remote_revision_changed')
            if not set(c['class_ids']) <= set(old['class_ids']):
                old['class_ids']=sorted(set(old['class_ids']) | set(c['class_ids']))
                old.update(state='needs_botanical_review', reasons=['conflicting_class_associations'])
                old.pop('decision',None)
                self.append('classified',old);self.project()
            for field in ['revision_id','source_timestamp','source_sha1']:
                if c.get(field)!=old.get(field):
                    raise RecoveryError('remote_revision_changed')
            self.project()
            return old
        require(c['source'] in SOURCES and c['class_ids'] and set(c['class_ids'])<= {x['class_id'] for x in canonical()[:12]},'candidate_class')
        if rights(c)!='passed':return self.classify(c,'needs_license_review','individual_rights_unproven')
        try:safe_url(c['file_url'],c['source'],True)
        except RecoveryError as error:return self.classify(c,'rejected_format',str(error))
        if c.get('mime') not in {'image/jpeg','image/png'} or (c.get('declared_size') is not None and
                (type(c['declared_size'])is not int or not 0<c['declared_size']<=self.config['limits']['file_bytes'])):
            return self.classify(c,'rejected_format','declared_format_or_size')
        recv=next((x for x in self.select('received') if x['candidate_id']==cid),None)
        intents=[x for x in self.select('intention') if x['candidate_id']==cid]
        if not recv:
            counts={cls:len({x['candidate_id'] for x in self.select('intention') if x['source']==c['source'] and cls in x['class_ids']}) for cls in c['class_ids']}
            if not intents and any(n>=self.config['limits']['transfers'] for n in counts.values()):return self.classify(c,'deferred_budget','transfer_budget')
            intent={'candidate_id':cid,'source':c['source'],'class_ids':c['class_ids'],'attempt':len(intents)+1}
            self.append('intention',intent);crash('intention')
            try:raw=download(c)
            except RecoveryError as error:return self.classify(c,'transfer_failed',str(error))
            require(isinstance(raw,bytes) and 0<len(raw)<=self.config['limits']['file_bytes'],'file_size')
            part='parts/'+cid+'-'+str(len(intents)+1)+'.part'
            persist(self.path(part),raw,True)
            recv={'candidate_id':cid,'part_path':part,'original_sha256':sha(raw)}
            self.append('received',recv);crash('received')
        raw=read(self.path(recv['part_path']))
        require(sha(raw)==recv['original_sha256'],'object_hash_mismatch')
        original='originals/'+sha(raw)
        used=sum(p.stat().st_size for base in ['originals','quarantine'] for p in self.path(base).iterdir() if p.is_file())
        require(used+(0 if self.path(original).exists() else len(raw))+MAX_BYTES<=self.config['limits']['storage_bytes'],'storage_budget')
        persist(self.path(original),raw,True);crash('original')
        rec={**c,'candidate_id':cid,'original_sha256':sha(raw),'original_path':original,'state':'needs_human_review',
             'sanitized_sha256':None,'sanitized_path':None,'technical':{},'reasons':['human_review_required'], 'pairs':[],'resolved_url':c['file_url'],'config_sha256':self.config_hash,'manifest_sha256':self.config['manifest_sha256'],'code_sha256':self.config['code_sha256']}
        try:
            if c.get('source_sha1'):require(hashlib.sha1(raw).hexdigest()==c['source_sha1'],'declared_hash_mismatch')
            require(c.get('declared_size') in (None,len(raw)),'declared_size_mismatch')
            clean,suffix=sanitize(raw,c['file_url'],c['mime']);rec['technical']=technical(clean)
            rec['sanitized_sha256']=sha(clean);rec['sanitized_path']='quarantine/'+sha(clean)+suffix
            persist(self.path(rec['sanitized_path']),clean,True);crash('sanitized')
        except RecoveryError as error:rec.update(state='rejected_format',reasons=[str(error)])
        self.append('committed',rec);crash('committed')
        self.project();return rec
    def project(self):
        persist(self.path('records.json'),encode(self.records()))
        persist(self.path('summary.json'),encode(self.summary()))
    def summary(self):
        recs=self.records();coverage=[]
        for cls in canonical():
            for source in SOURCES:
                subset=[r for r in recs if r['source']==source and cls['class_id'] in r['class_ids']]
                stopped=[x for x in self.select('source_status') if x['source']==source and x['class_id']==cls['class_id']]
                status=stopped[-1]['status'] if stopped else ('protection_not_queried' if cls['kind']=='protection' else 'not_attempted')
                coverage.append({'class_id':cls['class_id'],'source':source,'status':status,'candidate_cap':0 if cls['kind']=='protection' else self.config['limits']['candidates'],
                                 'transfer_cap':0 if cls['kind']=='protection' else self.config['limits']['transfers'], 'found':len(subset),
                                 'transferred':sum(bool(r.get('original_sha256')) for r in subset),
                                 'technical_integrity':sum(bool(r.get('sanitized_sha256')) for r in subset),
                                 'license_valid':sum(rights(r)=='passed' for r in subset),
                                 'expert_validated':sum(r['state']=='approved_for_dataset' for r in subset),
                                 'approved':sum(r['state']=='approved_for_dataset' for r in subset),
                                 'rejected':sum(r['state'].startswith('rejected_') for r in subset),
                                 'pending':sum(not r['state'].startswith(('approved_','rejected_')) for r in subset)})
        result={'schema_version':1,'stage':'pending_human_acceptance','coverage':coverage,'counts':dict(sorted(Counter(r['state'] for r in recs).items())),
                'unique_objects':len(recs),'usable':0,'minimum_experimental_pilot':None,'scientific_sufficiency':'not_demonstrated',
                'production_sufficiency':'not_demonstrated','training_authorized':False,'partition_authorized':False,'training_status':'blocked'}
        validate_public(result);return result

PUBLIC_KEYS={'schema_version','stage','coverage','counts','unique_objects','usable','minimum_experimental_pilot','scientific_sufficiency','production_sufficiency','training_authorized','partition_authorized','training_status'}
COVERAGE_KEYS={'class_id','source','status','candidate_cap','transfer_cap','found','transferred','technical_integrity','license_valid','expert_validated','approved','rejected','pending'}
STATUSES={'not_attempted','no_crosswalk','source_blocked','exhausted_within_query','budget_reached','all_rejected','review_pending','protection_not_queried'}
def validate_public(value):
    require(set(value)==PUBLIC_KEYS,'private_export')
    require(value['stage']=='pending_human_acceptance' and value['usable']==0 and value['minimum_experimental_pilot'] is None,'public_authority')
    require(value['training_authorized'] is False and value['partition_authorized'] is False and value['training_status']=='blocked','public_training')
    require(value['scientific_sufficiency']==value['production_sufficiency']=='not_demonstrated','public_sufficiency')
    require(set(value['counts'])<=STATES and all(type(v)is int and v>=0 for v in value['counts'].values()),'public_counts')
    expected=[(c['class_id'],s) for c in canonical() for s in SOURCES]
    require([(c['class_id'],c['source']) for c in value['coverage']]==expected,'public_classes')
    for c in value['coverage']:
        require(set(c)==COVERAGE_KEYS and c['status'] in STATUSES,'private_export')
        require(all(type(v)is int and v>=0 for k,v in c.items() if k not in {'class_id','source','status'}),'public_types')
    require(type(value['schema_version'])is int and value['schema_version']==1 and type(value['unique_objects'])is int,'public_schema')

class PinnedHTTPS(http.client.HTTPSConnection):
    """Pin a validated public address; TLS still verifies the original hostname."""
    def connect(self):
        address=public_addresses(self.host)[0]
        sock=socket.create_connection((address,443),self.timeout)
        try:self.sock=self._context.wrap_socket(sock,server_hostname=self.host)
        except BaseException:sock.close();raise

def retry_delay(value,attempt,clock=None):
    clock=clock or time.time
    if value:
        try:
            delay=int(value) if value.isdecimal() else parsedate_to_datetime(value).timestamp()-clock()
            return max(0,delay)
        except (ValueError,TypeError,OverflowError):raise RecoveryError('invalid_retry_after') from None
    return 2**(attempt+1)

class Transport:
    def __init__(self,ds):self.ds=ds;self.last=0
    def get(self,url,source,media=False):
        require(not self.ds.offline,'offline_network_forbidden')
        limit=self.ds.config['limits']['file_bytes'] if media else 2*1024**2
        safe_url(url,source,media)
        for attempt in range(3):
            reservations=self.ds.select('request');finished={x['request_id']:x for x in self.ds.select('response')}
            require(sum(x['source']==source for x in reservations)<self.ds.config['limits']['requests'],'request_budget')
            media_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'])
            hour_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations
                           if x['media'] and x['epoch']>time.time()-3600)
            if media:
                require(media_total+limit<=self.ds.config['limits']['media_bytes'],'media_budget')
                require(hour_total+limit<=self.ds.config['limits']['hour_bytes'],'hour_budget')
            requests_after=[x for x in self.ds.select('resume_after') if x['source']==source]
            if requests_after:require(time.time()>=requests_after[-1]['epoch'],'resume_after')
            delay=max(0,1-(time.time()-reservations[-1]['epoch'])) if reservations else 0
            if delay:time.sleep(delay)
            rid=os.urandom(16).hex()
            self.ds.append('request',{'request_id':rid,'source':source,'media':media,'reserved':limit,'epoch':time.time(),'url':url})
            received=0;conn=None;status=None;retry=None;code='network_error';spool=None
            try:
                p=urlsplit(url);conn=PinnedHTTPS(p.hostname,timeout=20,context=ssl.create_default_context())
                conn.request('GET',p.path+('?' + p.query if p.query else ''),headers={'User-Agent':self.ds.config['user_agent'],'Accept':'application/json,image/jpeg,image/png','Accept-Encoding':'identity'})
                response=conn.getresponse();status=response.status
                if status in {301,302,303,307,308}:
                    # Validated redirect is reported for explicit source reconciliation; never silently switches objects.
                    safe_url(urljoin(url,response.getheader('Location','')),source,media)
                    raise RecoveryError('redirect_requires_reconciliation')
                if status!=200:
                    retry=response.getheader('Retry-After');code='http_'+str(status)
                    raise RecoveryError(code)
                length=response.getheader('Content-Length')
                require(not length or length.isdecimal() and int(length)<=limit,'response_size')
                require(response.getheader('Content-Encoding','identity')=='identity','content_encoding')
                chunks=[];started=time.monotonic()
                if media:
                    require(shutil.disk_usage(self.ds.root).free>=3*1024**3,'insufficient_disk')
                    spool=os.fdopen(os.open(self.ds.path('parts/request-'+rid+'.part'),os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600),'wb')
                while True:
                    require(time.monotonic()-started<=20,'response_timeout')
                    chunk=response.read(min(65536,limit+1-received))
                    if not chunk:break
                    received+=len(chunk);chunks.append(chunk)
                    if spool:spool.write(chunk);spool.flush();os.fsync(spool.fileno())
                    require(received<=limit,'response_size')
                raw=b''.join(chunks)
                if not media:
                    data=load(raw)
                    if isinstance(data,dict) and data.get('error',{}).get('code')=='maxlag':
                        status=503;retry=response.getheader('Retry-After');raise RecoveryError('maxlag')
                require(not length or received==int(length),'response_length_mismatch')
                code='ok'
                return raw
            except (OSError,http.client.HTTPException) as error:
                code='timeout' if isinstance(error,TimeoutError) else 'network_error'
            except RecoveryError as error:
                code=str(error)
                if code not in RETRYABLE:raise
            finally:
                if spool:spool.close();fsync_dir(self.ds.path('parts'))
                if conn:conn.close()
                self.ds.append('response',{'request_id':rid,'received':received,'status':status,'code':code})
            if attempt==2:raise RecoveryError(code)
            delay=retry_delay(retry,attempt)
            if delay>self.ds.config['limits']['wait_seconds']:
                self.ds.append('resume_after',{'source':source,'epoch':time.time()+delay})
                raise RecoveryError('resume_after')
            time.sleep(delay)
        raise RecoveryError('transfer_failed')


def commons_query(cls,cursor):
    require(cls['kind']=='species','protection_query')
    return {'action':'query','format':'json','formatversion':2,'generator':'search','gsrsearch':'"'+cls['scientific_name']+'"',
            'gsrnamespace':6,'gsrlimit':10,'gsroffset':cursor,'gsrsort':'relevance','prop':'imageinfo|revisions',
            'rvprop':'ids','iiprop':'url|mime|size|timestamp|sha1|extmetadata','iilimit':1,'iiextmetadatalanguage':'en','iiextmetadatafilter':'Artist|Credit|Attribution|Restrictions|Copyrighted|AttributionRequired|License|LicenseShortName|LicenseUrl|Permission','maxlag':5}

def commons_page(data,cls,evidence,config):
    require(isinstance(data,dict) and not ('error' in data or 'warnings' in data),'commons_schema')
    require('query' in data or data.get('batchcomplete') is True,'commons_schema')
    pages=data.get('query',{}).get('pages',[])
    require(isinstance(pages,list) and len(pages)<=10,'commons_pages')
    result=[]
    for page in pages:
        try:
            old=commons.inspect_page(page,cls,'"'+cls['scientific_name']+'"',config['cutoff'])
            info=page['imageinfo'][0];meta=info.get('extmetadata',{})
            record={'source':'commons','media_id':str(old['page_id']),'class_ids':[cls['class_id']],
                    'page_id':old['page_id'],'revision_id':(page.get('revisions') or [{}])[0].get('revid'),
                    'file_url':old['file_url'],'source_page_url':old['page_url'],'mime':old['declared_mime'],
                    'declared_size':old['declared_size'],'declared_width':info.get('width'),'declared_height':info.get('height'),
                    'source_sha1':old['source_sha1'],'source_timestamp':old['source_timestamp'],
                    'author':old['author'],'license_id':old['license_id'],'license_name':old['license'],
                    'license_url':old['license_url'],'restrictions':old['restrictions'],
                    'credit':commons.plain(old['credit_html']),'attribution':commons.plain(old['attribution_html']),
                    'title':old['title'],'evidence_sha256':evidence,'rights_consistent':False,
                    'database_rights':'passed' if config['source_contracts'].get('commons',{}).get('database_rights')=='passed' else 'pending',
                    'mapping':None,'mapping_reason':'source_taxon_id_unproven','scientific_name_received':None,
                    'taxonomic_confidence':'unmapped','observation_id':None,'origin_fidelity':'provider_original',
                    'camera_original_verified':False}
            # Require the actual individual grant, known photographer and coherent authorship/source.
            record['rights_consistent']=bool(record['revision_id'] and meta.get('LicenseUrl') and meta.get('Artist') and
                                              not meta.get('Permission',{}).get('value') and 'own work' in record['credit'].lower() and record['source_page_url'].startswith('https://commons.wikimedia.org/wiki/'))
            result.append(record)
        except (KeyError,TypeError,ValueError,commons.AcquisitionError):raise RecoveryError('commons_item_schema') from None
    continuation=data.get('continue');next_cursor=None
    if continuation is not None:
        require(isinstance(continuation,dict) and set(continuation)<={'continue','gsroffset'} and type(continuation.get('gsroffset'))is int,'commons_cursor')
        next_cursor=continuation['gsroffset']
    return result,next_cursor


def acquire_inat(ds,cls,transport,fixture):
    cid=cls['class_id'];crosswalk=ds.config['crosswalk'][cid]
    try:
        query=inat.build_query(crosswalk,cls,ds.config['cutoff'])
        # A reviewed evidence document must actually be present and match its digest.
        ev=crosswalk['evidence'];require(sha(read(ds.path(ev['path'])))==ev['sha256'],'crosswalk_evidence_hash')
        saved=next((p for p in ds.select('page') if p['source']=='inaturalist' and p['class_id']==cid),None)
        if saved:page=saved
        else:
            raw=encode(fixture['inaturalist'][cid]) if fixture is not None else transport.get(inat.API_URL+'?'+urlencode(query),'inaturalist')
            digest=sha(raw);path='evidence/'+digest+'.json';persist(ds.path(path),raw,True)
            if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
            data=load(raw);parsed=inat.parse_page(data,crosswalk,cls,ds.config['cutoff'])
            by_photo={}
            for observation in data['results']:
                for photo in observation['photos']:
                    by_photo.setdefault(str(photo['id']),(photo,observation))
            records=[]
            for initial in parsed['candidates']:
                media_id=initial['media_id'];photo,observation=by_photo[media_id]
                proof=ds.config['legal_evidence'].get(media_id)
                if proof:
                    for key in ['photo','observation']:
                        require(sha(read(ds.path(proof[key]['path'])))==proof[key]['evidence_sha256'],'rights_evidence_hash')
                item=inat.photo_record(photo,observation,proof)
                eligible=item['download_allowed'] and initial['taxonomic_confidence']=='source_supported'
                item.update(class_ids=[cid],license_id='cc-by-4.0' if item['license_code']=='cc-by' else item['license_code'],
                            license_name='CC BY 4.0' if item['license_code']=='cc-by' else 'CC0 1.0',license_url=item['legal_url'],
                            restrictions='',rights_consistent=eligible,database_rights='passed' if item['database_rights_passed'] else 'pending',
                            evidence_sha256=item['license_evidence_sha256'],mapping=crosswalk,declared_size=None,
                            mime='image/png' if (item['file_url'] or '').endswith('.png') else 'image/jpeg',
                            taxonomic_confidence=initial['taxonomic_confidence'])
                records.append(item)
            page=ds.save_page('inaturalist',cid,0,records,None)
            ds.append('inat_deferred',{'class_id':cid,'known_deferred_photos':parsed['deferred_photo_count'],
                                      'examined_photos':parsed['examined_photo_count'],'proposed_id_above':parsed['next_id_above']})
        for c in page['candidates']:
            ds.ingest(c,lambda record:read(Path(fixture['synthetic_media'])/record['media_id']) if fixture is not None else transport.get(record['file_url'],'inaturalist',True))
        ds.advance(page)
        return 'budget_reached'
    except (inat.ContractError,RecoveryError,KeyError,OSError) as error:
        code=str(error) if isinstance(error,RecoveryError) and str(error) in RETRYABLE else 'inaturalist_contract_or_evidence'
        ds.append('source_failure',{'source':'inaturalist','class_id':cid,'code':code})
        return 'source_blocked'


def acquire(ds,fixture=None):
    transport=Transport(ds)
    if fixture is not None:require(ds.offline,'fixture_mode')
    elif ds.offline:raise RecoveryError('fixture_required')
    for cls in canonical():
        for source in SOURCES:
            cid=cls['class_id']
            statuses=[s for s in ds.select('source_status') if s['source']==source and s['class_id']==cid]
            if statuses:
                failed=[e for e in ds.select('source_failure') if e['source']==source and e['class_id']==cid]
                if statuses[-1]['status']!='source_blocked' or not failed or failed[-1]['code'] not in RETRYABLE:continue
            status='protection_not_queried'
            if cls['kind']=='species':
                if source=='inaturalist' and cid not in ds.config['crosswalk']:
                    status='no_crosswalk'
                elif source=='inaturalist':
                    status=acquire_inat(ds,cls,transport,fixture)
                else:
                    cursor=0;status='budget_reached'
                    for page_index in range(ds.config['limits']['pages']):
                        saved=next((p for p in ds.select('page') if p['source']==source and p['class_id']==cid and p['cursor']==cursor),None)
                        try:
                            if saved:page=saved
                            else:
                                if fixture is not None:
                                    raw=encode(fixture.get(cid,{}).get(str(cursor),{'batchcomplete':True}))
                                else:raw=transport.get('https://commons.wikimedia.org/w/api.php?'+urlencode(commons_query(cls,cursor)),source)
                                digest=sha(raw);path='evidence/'+digest+'.json'
                                persist(ds.path(path),raw,True)
                                if not any(e['sha256']==digest for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':digest})
                                candidates,next_cursor=commons_page(load(raw),cls,digest,ds.config)
                                page=ds.save_page(source,cid,cursor,candidates,next_cursor)
                            examined={candidate_id(c) for p in ds.select('page') if p['source']==source and p['class_id']==cid for c in p['candidates']}
                            require(len(examined)<=ds.config['limits']['candidates'],'candidate_budget')
                            for c in page['candidates']:
                                def download(record):
                                    if fixture is not None:
                                        require('synthetic_media' in fixture,'fixture_media_missing')
                                        return read(Path(fixture['synthetic_media'])/str(record['media_id']))
                                    return transport.get(record['file_url'],source,True)
                                ds.ingest(c,download)
                            ds.advance(page)
                            retryable=[ds.record(c) for c in page['candidates'] if ds.record(c)['state']=='transfer_failed'
                                       and set(ds.record(c).get('reasons',[])) & RETRYABLE]
                            if retryable:
                                raise RecoveryError(retryable[0]['reasons'][0])
                            if page['next_cursor'] is None:
                                status='exhausted_within_query';break
                            cursor=page['next_cursor']
                        except RecoveryError as error:
                            ds.append('source_failure',{'source':source,'class_id':cid,'code':str(error)})
                            status='source_blocked';break
            ds.append('source_status',{'source':source,'class_id':cid,'status':status})
    ds.project()
    return 1 if any(c['status']=='source_blocked' for c in ds.summary()['coverage']) else 0


def historical(source):
    """Read-only verification against the frozen P07 closure (never P07 finalizers)."""
    source=safe_path(source);closure=load(read(ROOT/'artifacts/bianchini/v2/codex/P07/closure-evidence.json'))
    p07=source.parent/'p07-curation-20260928'
    for n,h in closure['external_final_sha256'].items():require(sha(read(p07/n))==h,'p07_reference_hash')
    before=load(read(p07/'source-before.json'))
    actual={str(p.relative_to(source)):sha(read(p)) for p in source.rglob('*') if p.is_file()}
    require(before==actual and len(actual)==29,'p06_source_hashes')
    records=[]
    for item in closure['images_before_after']:
        h=item['sha256_after'];path=source/'quarantine'/f'{h}.jpg';raw=read(path)
        require(sha(raw)==h,'p07_image_hash')
        records.append({'candidate_id':item['id'],'sanitized_sha256':h,'technical':technical(raw),'class_ids':[],
                        'original_sha256':None,'observation_id':None})
    return actual,records


def inspect(ds,source):
    hashes,prior=historical(source);recs=ds.records();pairs=[]
    combined=[*prior,*[r for r in recs if r.get('sanitized_sha256')]]
    for i,a in enumerate(combined):
        for b in combined[i+1:]:
            if a['candidate_id'].startswith('Q') and b['candidate_id'].startswith('Q'):continue
            dist=(int(a['technical']['dhash64'],16)^int(b['technical']['dhash64'],16)).bit_count()
            exact=bool(a.get('sanitized_sha256')==b.get('sanitized_sha256') or a.get('original_sha256') and a.get('original_sha256')==b.get('original_sha256'))
            same=bool(a.get('observation_id') and a.get('observation_id')==b.get('observation_id'))
            signal='exact_duplicate' if exact else 'near_duplicate' if dist<=6 else 'borderline' if dist<=10 else 'same_series' if same else 'no_algorithmic_signal'
            pairs.append({'pair_id':a['candidate_id']+'-'+b['candidate_id'],'left':a['candidate_id'],'right':b['candidate_id'],'distance':dist,'signal':signal})
    for rec in recs:
        related=[p for p in pairs if rec['candidate_id'] in {p['left'],p['right']} and p['signal']!='no_algorithmic_signal']
        if rec.get('pairs')!=related:
            rec['pairs']=related;rec.pop('decision',None)
            if rec.get('sanitized_sha256'):
                rec['state']='rejected_duplicate' if any(p['signal']=='exact_duplicate' for p in related) else 'needs_duplicate_review' if related else 'needs_human_review'
            ds.append('classified',rec)
    ds.project()
    report={'p07_images':len(prior),'p06_hashes':hashes,'pairs':pairs,'records':recs,'summary':ds.summary()}
    persist(ds.path('inspection.json'),encode(report))
    rows=[];attrs=[]
    for r in recs:
        image=f'<img loading="lazy" width="240" src="{escape(r["sanitized_path"])}">' if r.get('sanitized_path') else ''
        detail=escape(json.dumps(r,ensure_ascii=False,indent=2,sort_keys=True))
        rows.append(f'<article><h2>{r["candidate_id"]}</h2>{image}<pre>{detail}</pre></article>')
        if r.get('original_sha256'):
            attrs.append({k:r.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256','author','credit','attribution','title','source_page_url','license_url','restrictions']})
            attrs[-1]['changes']='EXIF orientation; RGB pixel reconstruction; metadata removal; JPEG quality 95 or PNG; no crop or enhancement'
    html='<!doctype html><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; img-src \'self\'; style-src \'unsafe-inline\'"><title>P08 private review</title><h1>P08 — pending human review</h1>'+''.join(rows)
    persist(ds.path('review.html'),html.encode())
    persist(ds.path('Attributions.jsonl'),b''.join(encode(a) for a in attrs))
    persist(ds.path('NOTICE.md'),('P08 private attribution bundle; no redistribution authorized.\n\n'+''.join(json.dumps(a,ensure_ascii=False)+'\n\n' for a in attrs)).encode())
    persist(ds.path('decisions.template.json'),encode({'authority':'human','decisions':[
        {'candidate_id':r['candidate_id'],'original_sha256':r.get('original_sha256'),'sanitized_sha256':r.get('sanitized_sha256'),
         'evidence_digest':review_digest(r),'reviewer':None,'reviewed_at':None,'authority':'human','quality':'pending',
         'privacy':'pending','botanical':'pending','duplicates':'pending','expert_confirmation':False,
         'qualification':None,'botanical_evidence':None,'mapping':None,'rationale':None} for r in recs]}))
    return report


def finalize(ds,decisions):
    data=load(read(decisions));require(data.get('authority')=='human' and isinstance(data.get('decisions'),list),'human_authority')
    ids=[d.get('candidate_id') for d in data['decisions']];require(len(ids)==len(set(ids)),'duplicate_decisions')
    recs={r['candidate_id']:r for r in ds.records()};require(set(ids)==set(recs),'decision_coverage')
    for d in data['decisions']:
        rec=recs[d['candidate_id']]
        if rec.get('decision')==d:continue
        state=decide(rec,d)
        if state=='approved_for_dataset':
            inspection=load(read(ds.path('inspection.json')))
            require(inspection.get('p07_images')==17 and any(review_digest(item)==review_digest(rec)
                    for item in inspection['records']),'inspection_binding')
            attrs=[load(line) for line in read(ds.path('Attributions.jsonl')).splitlines()]
            require(any(all(item.get(k)==rec.get(k) for k in ['candidate_id','original_sha256','sanitized_sha256',
                         'author','license_url','source_page_url']) for item in attrs),'attribution_binding')
            require(sha(read(ds.path(d['mapping']['evidence_path'])))==d['mapping']['evidence_sha256'],'mapping_evidence_hash')
            require(sha(read(ds.path(d['botanical_evidence_path'])))==d['botanical_evidence'],'botanical_evidence_hash')
        rec.update(state=state,decision=d);ds.append('classified',rec)
    ds.project()


def verify(ds,source,acceptance=None):
    ds.verify_objects();historical(source);validate_public(ds.summary())
    require(len({(s['source'],s['class_id']) for s in ds.select('source_status')})==28,'incomplete_round')
    require({p['page_id'] for p in ds.select('page')}=={p['page_id'] for p in ds.select('cursor')},'pending_pages')
    if acceptance:
        a=load(read(acceptance));manifest=read(ds.path('final-manifest.json'))
        require(a.get('decision')=='accepted' and a.get('authority')=='human' and a.get('reviewer') and a.get('reviewed_at') and a.get('manifest_sha256')==sha(manifest),'human_acceptance')
        files=load(manifest)['files']
        actual={str(p.relative_to(ds.root)):sha(read(p)) for p in ds.root.rglob('*') if p.is_file() and str(p.relative_to(ds.root)) not in {'.lock','final-manifest.json','acceptance.json'}}
        require(files==actual,'acceptance_coverage_or_bytes')
        require({'journal.jsonl','config.json','records.json','summary.json','inspection.json','Attributions.jsonl','NOTICE.md','review.html'} <= set(files),'acceptance_required_files')
        require(a.get('training_authorized') is False,'acceptance_not_training')
    return 0


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    for name in ['acquire','inspect','finalize','verify']:
        p=sub.add_parser(name);p.add_argument('--output',required=True);p.add_argument('--offline-fixture')
        if name=='acquire':p.add_argument('--config',required=True)
        if name in {'inspect','verify'}:p.add_argument('--p07-source',required=True)
        if name=='finalize':p.add_argument('--decisions',required=True)
        if name=='verify':p.add_argument('--acceptance')
    args=parser.parse_args(argv)
    try:
        config=load(read(args.config if args.command=='acquire' else Path(args.output)/'config.json'))
        with Dataset(args.output,config,offline=bool(args.offline_fixture)) as ds:
            if args.command=='acquire':code=acquire(ds,load(read(args.offline_fixture)) if args.offline_fixture else None)
            elif args.command=='inspect':inspect(ds,args.p07_source);code=0
            elif args.command=='finalize':finalize(ds,args.decisions);code=0
            else:code=verify(ds,args.p07_source,args.acceptance)
        print(json.dumps({'command':args.command,'status':'passed' if code==0 else 'source_blocked'}));return code
    except (OSError,ValueError,KeyError,TypeError):
        print('p08_invalid_config_schema_hash_or_io',file=sys.stderr);return 2
    except KeyboardInterrupt:
        print('p08_cancelled_replay_required',file=sys.stderr);return 1

if __name__=='__main__':raise SystemExit(main())

```

### scripts/phase1/test_recover_p08.py

```text
"""Public P08 boundaries, synthetic data only; no network in these tests."""
import copy
from contextlib import ExitStack
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
import recover_p08 as r


def image_bytes(fmt='JPEG'):
    out = io.BytesIO()
    im = Image.new('RGB', (240, 240), (100, 160, 40))
    exif = Image.Exif(); exif[270] = 'synthetic-private-metadata'; exif[274] = 6
    im.save(out, format=fmt, exif=exif)
    return out.getvalue()


def candidate(raw=None):
    raw = raw or image_bytes()
    return {'source': 'commons', 'media_id': '123', 'class_ids': ['species_01'],
            'file_url': 'https://upload.wikimedia.org/a/test.jpg',
            'source_page_url': 'https://commons.wikimedia.org/wiki/File:Test.jpg',
            'mime': 'image/jpeg', 'declared_size': len(raw), 'source_sha1': __import__('hashlib').sha1(raw).hexdigest(),
            'author': 'Synthetic fixture', 'license_id': 'cc-by-4.0', 'license_name': 'CC BY 4.0',
            'license_url': 'https://creativecommons.org/licenses/by/4.0/', 'restrictions': '',
            'credit': 'Synthetic fixture', 'attribution': 'Synthetic fixture', 'evidence_sha256': 'a'*64,
            'rights_consistent': True, 'database_rights': 'passed', 'mapping': None,
            'observation_id': None, 'origin_fidelity': 'provider_original', 'camera_original_verified': False}


class DatasetCase:
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)/'synthetic'
        self.config = r.default_config(offline=True)

    def open(self):
        return r.Dataset(self.root, self.config, offline=True)


class RecoveryTests(DatasetCase, unittest.TestCase):

    def test_rights_gate(self):
        c = candidate()
        self.assertEqual(r.rights(c), 'passed')
        for key, val in [('license_url', 'https://creativecommons.org/licenses/by/3.0/'),
                         ('license_name','CC BY-SA 4.0'),('license_id','cc-by'),
                         ('author','unknown'),('restrictions','extra'),('rights_consistent',False),
                         ('evidence_sha256',None),('database_rights','pending')]:
            with self.subTest(key=key):
                bad=copy.deepcopy(c); bad[key]=val
                self.assertNotEqual(r.rights(bad),'passed')

    def test_expert_gate(self):
        c = candidate(); c.update(candidate_id=r.candidate_id(c),original_sha256='b'*64,sanitized_sha256='c'*64,
                                technical={'decode':'ok'},pairs=[],state='quarantined')
        d = {'candidate_id':c['candidate_id'], 'original_sha256':'b'*64,'sanitized_sha256':'c'*64,
             'evidence_digest':r.review_digest(c),'reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z',
             'authority':'human','quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
             'expert_confirmation':False,'qualification':'','botanical_evidence':'','mapping':None,
             'rationale':'Synthetic decision'}
        self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
        for flag in [None, 'true',1]:
            d['expert_confirmation']=flag
            self.assertNotEqual(r.decide(c,d),'approved_for_dataset')
        d['authority']='agent_proposal'
        with self.assertRaises(r.RecoveryError): r.decide(c,d)

    def test_original_sanitization_resume(self):
        raw=image_bytes(); c=candidate(raw)
        with self.open() as ds:
            rec=ds.ingest(c,lambda _:raw)
            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)
            self.assertNotEqual(rec['original_sha256'],rec['sanitized_sha256'])
            with Image.open(self.root/rec['sanitized_path']) as im:
                self.assertFalse(im.getexif()); self.assertNotIn('xmp',im.info)
            before=r.tree_fingerprint(self.root)
            ds.ingest(c,lambda _:self.fail('repeat download'))
            self.assertEqual(before,r.tree_fingerprint(self.root))
        with self.open() as ds:
            self.assertEqual(len(ds.records()),1)
            before=r.tree_fingerprint(self.root)
            ds.ingest(c,lambda _:self.fail('restart download'))
            self.assertEqual(before,r.tree_fingerprint(self.root))
            self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')

    def test_hash_mismatch(self):
        with self.open() as ds:
            rec=ds.ingest(candidate(),lambda _:image_bytes())
        (self.root/rec['original_path']).write_bytes(b'corrupt')
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass

    def test_journal_partial(self):
        with self.open(): pass
        with (self.root/'journal.jsonl').open('ab') as f: f.write(b'{')
        before=(self.root/'journal.jsonl').read_bytes()
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass
        self.assertEqual(before,(self.root/'journal.jsonl').read_bytes())

    def test_journal_chain(self):
        with self.open() as ds: ds.append('test',{'x':1})
        p=self.root/'journal.jsonl'; raw=p.read_bytes().replace(b'"x":1',b'"x":2');p.write_bytes(raw)
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass

    def test_lock(self):
        with self.open():
            with self.assertRaises(r.RecoveryError):
                with self.open(): pass

    def test_changed_config(self):
        with self.open(): pass
        self.config['limits']['pages']=1
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass

    def test_symlink(self):
        self.root.symlink_to(Path(self.tmp.name),target_is_directory=True)
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass

    def test_cursor_gate(self):
        with self.open() as ds:
            page=ds.save_page('commons','species_01',0,[candidate()],None)
            with self.assertRaises(r.RecoveryError): ds.advance(page)
            ds.ingest(candidate(),lambda _:image_bytes())
            ds.advance(page)
            before=r.tree_fingerprint(self.root);ds.advance(page)
            self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_private_export(self):
        with self.open() as ds: value=ds.summary()
        self.assertEqual(len(value['coverage']),28)
        self.assertFalse(value['training_authorized'])
        self.assertEqual(value['usable'],0)
        r.validate_public(value)
        for key in ['author','url','gps','free_text']:
            bad=copy.deepcopy(value);bad[key]='PRIVATE'
            with self.assertRaises(r.RecoveryError):r.validate_public(bad)
        bad=copy.deepcopy(value);bad['coverage'][0]['author']='PRIVATE'
        with self.assertRaises(r.RecoveryError):r.validate_public(bad)

    def test_download_budget_restart(self):
        self.config['limits']['transfers']=1
        with self.open() as ds:
            ds.ingest(candidate(),lambda _:image_bytes())
        with self.open() as ds:
            c=candidate();c['media_id']='124'
            rec=ds.ingest(c,lambda _:self.fail('budget exceeded'))
            self.assertEqual(rec['state'],'deferred_budget')

    def test_crash_boundaries(self):
        for stage in ['intention','received','original','sanitized','committed']:
            with self.subTest(stage=stage),tempfile.TemporaryDirectory() as td:
                root=Path(td)/'synthetic'
                with r.Dataset(root,self.config,offline=True) as ds:
                    def crash(point):
                        if point==stage: raise RuntimeError('crash')
                    with self.assertRaises(RuntimeError):ds.ingest(candidate(),lambda _:image_bytes(),crash=crash)
                with r.Dataset(root,self.config,offline=True) as ds:
                    rec=ds.ingest(candidate(),lambda _:image_bytes())
                    self.assertTrue((root/rec['original_path']).exists())
                    self.assertEqual(len(ds.records()),1)
                    self.assertEqual(rec['state'],'needs_human_review')

    def test_format_invalid_preserved(self):
        raw=b'not image';c=candidate(raw)
        with self.open() as ds:
            rec=ds.ingest(c,lambda _:raw)
            self.assertEqual(rec['state'],'rejected_format')
            self.assertEqual((self.root/rec['original_path']).read_bytes(),raw)

    def test_symlink_object(self):
        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
        p=self.root/rec['original_path'];raw=p.read_bytes();p.unlink()
        q=Path(self.tmp.name)/'fixture';q.write_bytes(raw);p.symlink_to(q)
        with self.assertRaises(r.RecoveryError):
            with self.open(): pass

    def test_url_boundaries(self):
        good='https://upload.wikimedia.org/a/a.jpg'
        self.assertEqual(r.safe_url(good,'commons',True),good)
        for u in ['http://upload.wikimedia.org/a.jpg','https://upload.wikimedia.org:444/a.jpg',
                  'https://user@upload.wikimedia.org/a.jpg','https://evil.invalid/a.jpg',
                  'https://upload.wikimedia.org/%2e%2e/a.jpg','https://upload.wikimedia.org/a.jpg#x']:
            with self.subTest(u=u),self.assertRaises(r.RecoveryError):r.safe_url(u,'commons',True)
        with patch('socket.getaddrinfo',return_value=[(2,1,6,'',('127.0.0.1',443))]):
            with self.assertRaises(r.RecoveryError):r.public_addresses('upload.wikimedia.org')

    def test_metadata_and_dimensions(self):
        for fmt in ['JPEG','PNG']:
            raw=image_bytes(fmt);suffix='jpg' if fmt=='JPEG' else 'png'
            clean,ext=r.sanitize(raw,'https://upload.wikimedia.org/a.'+suffix,'image/'+('jpeg' if fmt=='JPEG' else 'png'))
            with Image.open(io.BytesIO(clean)) as im:
                self.assertFalse(im.getexif());self.assertEqual(im.mode,'RGB')
        with self.assertRaises(r.RecoveryError):r.sanitize(b'', 'https://upload.wikimedia.org/a.jpg','image/jpeg')
        with self.assertRaises(r.RecoveryError):r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.jpg','image/jpeg')

    def test_cli_invalid_safe(self):
        p=subprocess.run([sys.executable,'-B',str(r.Path(r.__file__)),'verify','--output',str(self.root),'--p07-source',str(self.root)],capture_output=True,text=True)
        self.assertEqual(p.returncode,2)
        self.assertNotIn(str(self.root),p.stderr)

class ExtendedTests(DatasetCase, unittest.TestCase):
    """Risk neighbors through durable acquisition and transport boundaries."""
    def test_retry_transfer(self):
        with self.open() as ds:
            def fail(_):raise r.RecoveryError('timeout')
            self.assertEqual(ds.ingest(candidate(),fail)['state'],'transfer_failed')
        with self.open() as ds:
            self.assertEqual(ds.ingest(candidate(),lambda _:image_bytes())['state'],'needs_human_review')
            self.assertEqual(len(ds.select('intention')),2)

    def test_zero_round_replay(self):
        with self.open() as ds:
            self.assertEqual(r.acquire(ds,{}),0)
            ds.project();before=r.tree_fingerprint(self.root)
            self.assertEqual(r.acquire(ds,{}),0)
            self.assertEqual(before,r.tree_fingerprint(self.root))
            coverage=ds.summary()['coverage']
            self.assertEqual(sum(x['status']=='no_crosswalk' for x in coverage),12)
            self.assertEqual(sum(x['status']=='protection_not_queried' for x in coverage),4)

    def test_same_object_class_conflict(self):
        with self.open() as ds:
            ds.ingest(candidate(),lambda _:image_bytes())
            c=candidate();c['class_ids']=['species_02']
            rec=ds.ingest(c,lambda _:self.fail('duplicate download'))
            self.assertEqual(rec['class_ids'],['species_01','species_02'])
            self.assertEqual(rec['state'],'needs_botanical_review')
            self.assertEqual(len(ds.records()),1)

    def test_fsync_failure_preserves_source(self):
        with self.open() as ds:
            with patch.object(r.os,'fsync',side_effect=OSError('synthetic full disk')):
                with self.assertRaises(OSError):ds.ingest(candidate(),lambda _:self.fail('before durable intent'))

    def test_missing_object(self):
        with self.open() as ds:rec=ds.ingest(candidate(),lambda _:image_bytes())
        (self.root/rec['sanitized_path']).unlink()
        with self.assertRaises(OSError):
            with self.open():pass

    def test_png_pixels_and_metrics(self):
        clean,_=r.sanitize(image_bytes('PNG'),'https://upload.wikimedia.org/a.png','image/png')
        tech=r.technical(clean)
        self.assertEqual(tech['format'],'PNG')
        self.assertEqual(len(tech['dhash64']),16)
        for mean,expected in [(39,True),(40,False),(215,False),(216,True)]:
            flags=r.flags_for(224,224,mean,0,0,100)
            self.assertEqual('dark_mean' in flags or 'bright_mean' in flags,expected)
        self.assertIn('dark_fraction',r.flags_for(224,224,100,.25,0,100))
        self.assertNotIn('small_dimension',r.flags_for(224,224,100,0,0,100))
        self.assertIn('small_dimension',r.flags_for(223,224,100,0,0,100))
        self.assertNotIn('extreme_aspect',r.flags_for(224,672,100,0,0,100))
        self.assertIn('extreme_aspect',r.flags_for(224,673,100,0,0,100))
        self.assertIn('low_laplacian_variance',r.flags_for(224,224,100,0,0,99))

    def test_retry_after(self):
        self.assertEqual(r.retry_delay('120',0),120)
        self.assertEqual(r.retry_delay(None,0),2)
        self.assertEqual(r.retry_delay(None,1),4)
        self.assertEqual(r.retry_delay('Thu, 01 Jan 1970 00:02:00 GMT',0,clock=lambda:0),120)
        with self.assertRaises(r.RecoveryError):r.retry_delay('invalid',0)

    def test_offline_transport_never_network(self):
        with self.open() as ds,patch.object(r.socket,'create_connection',side_effect=AssertionError('network')):
            with self.assertRaises(r.RecoveryError):r.Transport(ds).get('https://commons.wikimedia.org/w/api.php','commons')

    def test_final_positive_authority_and_mapping(self):
        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
        cls=r.canonical()[0]
        d={'authority':'human','reviewer':'Synthetic human','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
           'evidence_digest':r.review_digest(c),'expert_confirmation':True,'qualification':'synthetic botanist',
           'botanical_evidence':'a'*64,'quality':'passed','privacy':'passed','botanical':'passed','duplicates':'passed',
           'mapping':{'confidence':'human_validated','source_taxon_id':'fixture','namespace':'fixture','evidence_sha256':'a'*64,
                      'class_id':cls['class_id'],'scientific_name':cls['scientific_name'],'rank':'species','status':'accepted',
                      'taxonomy_ref_ids':cls['taxonomy_ref_ids']},
           'visual':dict.fromkeys(['photograph','single_target','live_specimen','diagnostic_detail','no_dominant_text','no_montage','exposure','sharpness'],True),
           'privacy_checks':dict.fromkeys(['people','faces','plates','residences','screens_documents','sensitive_location'],'absent')}
        self.assertEqual(r.decide(c,d),'approved_for_dataset')
        for key in ['scientific_name','class_id','taxonomy_ref_ids','namespace']:
            bad=copy.deepcopy(d);bad['mapping'][key]=None
            self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')
        for gate in ['quality','privacy','botanical','duplicates']:
            for value in [None,True,'unknown','pending']:
                bad=copy.deepcopy(d);bad[gate]=value
                self.assertNotEqual(r.decide(c,bad),'approved_for_dataset')


class FakeResponse:
    def __init__(self, status=200, body=b'{}', headers=None, read_error=None):
        self.status = status
        self.body = io.BytesIO(body)
        self.headers = headers or {}
        self.read_error = read_error
        self.read_calls = 0

    def getheader(self, name, default=None):
        return self.headers.get(name, default)

    def read(self, count):
        self.read_calls += 1
        if self.read_error and self.read_calls > 1:
            raise self.read_error
        return self.body.read(count)


class FakeConnection:
    def __init__(self, result):
        self.result = result
        self.requests = []
        self.closed = False

    def request(self, *args, **kwargs):
        self.requests.append((args, kwargs))

    def getresponse(self):
        if isinstance(self.result, BaseException):
            raise self.result
        return self.result

    def close(self):
        self.closed = True


class TransportTests(DatasetCase, unittest.TestCase):
    api = 'https://commons.wikimedia.org/w/api.php'
    media = 'https://upload.wikimedia.org/a/synthetic.jpg'

    def transport(self, ds, responses):
        stack = ExitStack()
        self.addCleanup(stack.close)
        connections = [FakeConnection(response) for response in responses]
        factory = stack.enter_context(patch.object(r, 'PinnedHTTPS', side_effect=connections))
        stack.enter_context(patch.object(ds, 'offline', False))
        stack.enter_context(patch.object(r.socket, 'create_connection', side_effect=AssertionError('network_forbidden')))
        stack.enter_context(patch.object(r.socket, 'getaddrinfo', side_effect=AssertionError('network_forbidden')))
        clock = [1000.0]
        stack.enter_context(patch.object(r.time, 'time', side_effect=lambda: clock[0]))
        stack.enter_context(patch.object(r.time, 'monotonic', side_effect=lambda: clock[0]))
        sleeps = stack.enter_context(patch.object(r.time, 'sleep', side_effect=lambda value: clock.__setitem__(0, clock[0]+value)))
        stack.enter_context(patch.object(r.shutil, 'disk_usage', return_value=type('Disk', (), {'free': 4*1024**3})()))
        return r.Transport(ds), factory, connections, sleeps

    def test_403_never_retries(self):
        with self.open() as ds:
            transport, factory, connections, sleeps = self.transport(ds, [FakeResponse(403)])
            with self.assertRaisesRegex(r.RecoveryError, 'http_403'):
                transport.get(self.api, 'commons')
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(len(ds.select('request')), 1)
            self.assertEqual(ds.select('response')[0]['status'], 403)
            self.assertTrue(connections[0].closed)
            sleeps.assert_not_called()

    def test_429_wait_above_budget_persists_resume_after(self):
        with self.open() as ds:
            transport, factory, _, sleeps = self.transport(ds, [FakeResponse(429, headers={'Retry-After': '120'})])
            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
                transport.get(self.api, 'commons')
            self.assertEqual(ds.select('resume_after')[0]['epoch'], 1120)
            self.assertEqual(factory.call_count, 1)
            sleeps.assert_not_called()
            with self.assertRaisesRegex(r.RecoveryError, 'resume_after'):
                transport.get(self.api, 'commons')
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(len(ds.select('request')), 1)

    def test_timeout_three_attempts_and_cumulative_quota(self):
        self.config['limits']['requests'] = 3
        with self.open() as ds:
            transport, factory, connections, sleeps = self.transport(ds, [TimeoutError('synthetic') for _ in range(3)])
            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
                transport.get(self.api, 'commons')
            self.assertEqual(factory.call_count, 3)
            self.assertEqual(len(ds.select('request')), 3)
            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)
            self.assertEqual([call.args[0] for call in sleeps.call_args_list], [2, 4])
            self.assertTrue(all(connection.closed for connection in connections))
        with self.open() as ds:
            transport, factory, _, _ = self.transport(ds, [])
            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
                transport.get(self.api, 'commons')
            factory.assert_not_called()

    def test_request_reservation_survives_crash_without_response(self):
        self.config['limits']['requests'] = 1
        with self.open() as ds:
            ds.append('request', {'request_id': 'synthetic-interrupted', 'source': 'commons', 'media': True,
                                  'reserved': 16, 'epoch': 1000, 'url': self.media})
        with self.open() as ds:
            transport, factory, _, _ = self.transport(ds, [])
            with self.assertRaisesRegex(r.RecoveryError, 'request_budget'):
                transport.get(self.media, 'commons', True)
            factory.assert_not_called()

    def test_malicious_redirect_does_not_connect_to_destination(self):
        with self.open() as ds:
            transport, factory, _, _ = self.transport(ds, [FakeResponse(302, headers={'Location': 'https://127.0.0.1/a'})])
            with self.assertRaisesRegex(r.RecoveryError, 'unsafe_url'):
                transport.get(self.api, 'commons')
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(ds.select('response')[0]['status'], 302)

    def test_public_hostname_resolving_private_ip_is_rejected_before_connect(self):
        for ip in ['127.0.0.1', '10.0.0.1', '169.254.169.254', '::1', 'fc00::1']:
            with self.subTest(ip=ip), patch.object(r.socket, 'getaddrinfo', return_value=[(2, 1, 6, '', (ip, 443))]), patch.object(r.socket, 'create_connection', side_effect=AssertionError('must_not_connect')) as connect:
                with self.assertRaisesRegex(r.RecoveryError, 'nonpublic_address'):
                    r.PinnedHTTPS('upload.wikimedia.org', timeout=20).connect()
                connect.assert_not_called()

    def test_oversized_response_counts_received_bytes_and_failure(self):
        self.config['limits']['file_bytes'] = 8
        self.config['limits']['media_bytes'] = 16
        with self.open() as ds:
            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'123456789')])
            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
                transport.get(self.media, 'commons', True)
            self.assertEqual(ds.select('response')[0]['received'], 9)
            self.assertEqual(ds.select('response')[0]['code'], 'response_size')
            with self.assertRaisesRegex(r.RecoveryError, 'media_budget'):
                transport.get(self.media, 'commons', True)
            self.assertEqual(factory.call_count, 1)

    def test_partial_timeout_counts_bytes_on_every_retry(self):
        self.config['limits']['file_bytes'] = 16
        with self.open() as ds:
            transport, factory, _, _ = self.transport(ds, [FakeResponse(body=b'1234', read_error=TimeoutError('synthetic')) for _ in range(3)])
            with self.assertRaisesRegex(r.RecoveryError, 'timeout'):
                transport.get(self.media, 'commons', True)
            self.assertEqual(factory.call_count, 3)
            self.assertEqual([e['received'] for e in ds.select('response')], [4, 4, 4])
            self.assertEqual([e['code'] for e in ds.select('response')], ['timeout']*3)

    def test_declared_oversize_rejected_before_body(self):
        self.config['limits']['file_bytes'] = 8
        response = FakeResponse(body=b'123456789', headers={'Content-Length': '9'})
        with self.open() as ds:
            transport, _, _, _ = self.transport(ds, [response])
            with self.assertRaisesRegex(r.RecoveryError, 'response_size'):
                transport.get(self.media, 'commons', True)
            self.assertEqual(response.read_calls, 0)
            self.assertEqual(ds.select('response')[0]['received'], 0)


class CommonsCLIFlowTests(DatasetCase, unittest.TestCase):
    def test_fake_commons_cli_snapshot_ingest_and_restart(self):
        raw = image_bytes()
        c = candidate(raw)
        media = Path(self.tmp.name)/'media'
        media.mkdir()
        (media/'123').write_bytes(raw)
        fields = {'Artist': 'Synthetic fixture', 'License': 'cc-by-4.0', 'LicenseShortName': 'CC BY 4.0',
                  'LicenseUrl': c['license_url'], 'Credit': 'Own work', 'Attribution': 'Synthetic fixture'}
        page = {'pageid': 123, 'ns': 6, 'title': 'File:Synthetic.jpg', 'revisions': [{'revid': 456}],
                'imageinfo': [{'url': c['file_url'], 'descriptionurl': c['source_page_url'],
                               'mime': c['mime'], 'size': len(raw), 'width': 240, 'height': 240,
                               'sha1': c['source_sha1'], 'timestamp': '2026-10-04T00:00:00Z',
                               'extmetadata': {key: {'value': value} for key, value in fields.items()}}]}
        fixture = {'species_01': {'0': {'query': {'pages': [page]}, 'continue': {'continue': 'gsroffset||', 'gsroffset': 10}},
                                  '10': {'batchcomplete': True}}, 'synthetic_media': str(media)}
        fixture_path = Path(self.tmp.name)/'fixture.json'
        fixture_path.write_bytes(r.encode(fixture))
        self.config['source_contracts']['commons'] = {'database_rights': 'passed'}
        config_path = Path(self.tmp.name)/'run.json'
        config_path.write_bytes(r.encode(self.config))
        script = ('import sys\nfrom unittest.mock import patch\n'
                  'sys.path.insert(0, sys.argv.pop(1))\nimport recover_p08\n'
                  'with patch("socket.create_connection", side_effect=AssertionError("network_forbidden")), patch("socket.getaddrinfo", side_effect=AssertionError("network_forbidden")):\n'
                  ' raise SystemExit(recover_p08.main(sys.argv[1:]))\n')
        argv = [sys.executable, '-B', '-c', script, str(Path(r.__file__).parent), 'acquire', '--config', str(config_path),
                '--output', str(self.root), '--offline-fixture', str(fixture_path)]
        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(process.stdout)['status'], 'passed')
        with self.open() as ds:
            record = ds.records()[0]
            self.assertEqual(len(ds.records()), 1)
            self.assertEqual((self.root/record['original_path']).read_bytes(), raw)
            self.assertEqual(record['state'], 'needs_human_review')
            self.assertEqual(len(ds.select('intention')), 1)
            self.assertEqual(len(ds.select('source_status')), 28)
            for event in ds.select('evidence'):
                self.assertEqual(r.sha((self.root/event['path']).read_bytes()), event['sha256'])
            pages = [p for p in ds.select('page') if p['class_id'] == 'species_01']
            self.assertEqual([p['cursor'] for p in pages], [0, 10])
            kinds = [event['type'] for event in ds.events]
            self.assertLess(kinds.index('page'), kinds.index('intention'))
            self.assertLess(kinds.index('committed'), kinds.index('cursor'))
        before = r.tree_fingerprint(self.root)
        (media/'123').unlink()  # A repeated execution must use the durable objects.
        process = subprocess.run(argv, capture_output=True, text=True, timeout=30)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(before, r.tree_fingerprint(self.root))


class InaturalistResumeTests(DatasetCase, unittest.TestCase):
    def prepare_round(self, request_cap=4):
        from test_inaturalist_source import crosswalk, observation, page
        cls = r.canonical()[0]
        entry = crosswalk()
        evidence = b'synthetic reviewed crosswalk evidence\n'
        entry['taxonomy_ref_ids'] = cls['taxonomy_ref_ids']
        entry['evidence'].update(path='evidence/crosswalk.json', sha256=r.sha(evidence))
        self.config['crosswalk'][cls['class_id']] = entry
        self.config['limits']['requests'] = request_cap
        with self.open() as ds:
            r.persist(ds.path(entry['evidence']['path']), evidence, immutable=True)
            # Commons is already accounted for; exercise only the iNaturalist seam.
            for item in r.canonical():
                ds.append('source_status', {'source': 'commons', 'class_id': item['class_id'],
                          'status': 'exhausted_within_query' if item['kind'] == 'species' else 'protection_not_queried'})
        return cls, r.encode(page(observation()))

    def test_timeout_then_restart_preserves_journal_limits_and_candidates(self):
        cls, response = self.prepare_round()
        config_bytes = (self.root/'config.json').read_bytes()
        with self.open() as ds:
            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
            self.assertEqual(r.acquire(ds), 1)
            self.assertEqual(factory.call_count, 3)
            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
            self.assertEqual(len(ds.select('request')), 3)
            self.assertEqual([x['code'] for x in ds.select('response')], ['timeout'] * 3)
            self.assertEqual(ds.select('page'), [])
            self.assertEqual(ds.select('cursor'), [])
            self.assertEqual(ds.records(), [])
        prefix = (self.root/'journal.jsonl').read_bytes()
        with self.open() as ds:
            _, factory, _, _ = TransportTests.transport(self, ds, [FakeResponse(body=response)])
            self.assertEqual(r.acquire(ds), 0)
            self.assertEqual(factory.call_count, 1)
            self.assertEqual(len(ds.select('request')), self.config['limits']['requests'])
            self.assertEqual(len(ds.select('response')), 4)
            self.assertEqual(len({x['request_id'] for x in ds.select('request')}), 4)
            self.assertEqual(len(ds.select('page')), 1)
            self.assertEqual(len(ds.select('cursor')), 1)
            self.assertEqual(len(ds.records()), 1)
            self.assertEqual(ds.records()[0]['state'], 'needs_license_review')
            self.assertEqual(ds.records()[0]['class_ids'], [cls['class_id']])
            self.assertEqual(ds.select('intention'), [])
            self.assertEqual(ds.select('committed'), [])
            kinds = [e['type'] for e in ds.events]
            self.assertLess(kinds.index('evidence'), kinds.index('page'))
            self.assertLess(kinds.index('page'), kinds.index('classified'))
            self.assertLess(kinds.index('classified'), kinds.index('cursor'))
            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
            self.assertEqual(ds.config['limits'], self.config['limits'])
            self.assertEqual(ds.summary()['usable'], 0)
        stable = r.tree_fingerprint(self.root)
        with self.open() as ds:
            _, factory, _, _ = TransportTests.transport(self, ds, [])
            self.assertEqual(r.acquire(ds), 0)
            self.assertEqual(factory.call_count, 0)
            self.assertEqual(r.tree_fingerprint(self.root), stable)

    def test_only_existing_transient_recovery_codes_allow_restart(self):
        cls, _ = self.prepare_round()
        errors = [(r.RecoveryError(code), code) for code in sorted(r.RETRYABLE)]
        errors += [(r.RecoveryError(code), 'inaturalist_contract_or_evidence') for code in
                   ['http_403', 'http_404', 'request_budget', 'crosswalk_evidence_hash', 'invalid_json', 'unsafe_url']]
        errors += [(r.inat.ContractError('timeout'), 'inaturalist_contract_or_evidence'),
                   (OSError('timeout'), 'inaturalist_contract_or_evidence'),
                   (KeyError('timeout'), 'inaturalist_contract_or_evidence')]
        with self.open() as ds:
            for error, expected in errors:
                with self.subTest(error=type(error).__name__, code=str(error)):
                    with patch.object(r.Transport, 'get', side_effect=error) as get:
                        self.assertEqual(r.acquire_inat(ds, cls, r.Transport(ds), None), 'source_blocked')
                    self.assertEqual(get.call_count, 1)
                    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
            self.assertEqual(ds.select('page'), [])
            self.assertEqual(ds.select('cursor'), [])

    def test_timeout_restart_does_not_reset_request_budget(self):
        self.prepare_round(request_cap=3)
        with self.open() as ds:
            _, factory, _, _ = TransportTests.transport(self, ds, [TimeoutError()] * 3)
            self.assertEqual(r.acquire(ds), 1)
            self.assertEqual(factory.call_count, 3)
            self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
        prefix = (self.root/'journal.jsonl').read_bytes()
        config_bytes = (self.root/'config.json').read_bytes()
        with self.open() as ds:
            _, factory, _, _ = TransportTests.transport(self, ds, [])
            self.assertEqual(r.acquire(ds), 1)
            self.assertEqual(factory.call_count, 0)
            self.assertEqual(len(ds.select('request')), 3)
            self.assertNotIn(ds.select('source_failure')[-1]['code'], r.RETRYABLE)
            self.assertEqual(ds.records(), [])
            self.assertEqual(ds.select('page'), [])
            self.assertEqual(ds.select('cursor'), [])
            self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
            self.assertEqual((self.root/'config.json').read_bytes(), config_bytes)
            stable = r.tree_fingerprint(self.root)
            self.assertEqual(r.acquire(ds), 1)
            self.assertEqual(r.tree_fingerprint(self.root), stable)


class ContinuationProofs(DatasetCase, unittest.TestCase):
    def test_inspect_html_identical_after_journal_reload(self):
        with self.open() as ds:
            ds.ingest(candidate(),lambda _:image_bytes())
            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
        before=r.tree_fingerprint(self.root)
        with self.open() as ds:
            with patch.object(r,'historical',return_value=({},[])):r.inspect(ds,self.root)
        self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_exact_projection_predecessor_is_journaled_without_changing_config(self):
        self.config['code_sha256']['recover_p08.py']=r.HTML_ORDER_PREDECESSOR
        with self.open() as ds:
            self.assertEqual(len(ds.select('code_compatibility')),1)
            self.assertEqual(ds.select('code_compatibility')[0]['to'],r.fingerprint())
        before=r.tree_fingerprint(self.root)
        with self.open() as ds:self.assertEqual(len(ds.select('code_compatibility')),1)
        self.assertEqual(before,r.tree_fingerprint(self.root))
        self.config['code_sha256']['inaturalist_source.py']='0'*64
        with self.assertRaisesRegex(r.RecoveryError,'config_fingerprint'):
            with self.open():pass

    def test_full_round_retries_transient_media_without_requery(self):
        c=candidate()
        with self.open() as ds:
            ds.save_page('commons','species_01',0,[c],None)
            def fail(_):raise r.RecoveryError('timeout')
            ds.ingest(c,fail);ds.advance(ds.select('page')[0])
            ds.append('source_failure',{'source':'commons','class_id':'species_01','code':'timeout'})
            ds.append('source_status',{'source':'commons','class_id':'species_01','status':'source_blocked'})
        media=Path(self.tmp.name)/'media';media.mkdir();(media/'123').write_bytes(image_bytes())
        with self.open() as ds:
            self.assertEqual(r.acquire(ds,{'synthetic_media':str(media)}),0)
            self.assertEqual(ds.records()[0]['state'],'needs_human_review')
            self.assertEqual(len(ds.select('intention')),2)
            before=r.tree_fingerprint(self.root)
            self.assertEqual(r.acquire(ds,{}),0)
            self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_round_marks_failed_media_retryable_instead_of_exhausted(self):
        with self.open() as ds:
            ds.save_page('commons','species_01',0,[candidate()],None)
            with patch.object(r,'read',side_effect=r.RecoveryError('timeout')):
                # Only the media loader uses read during this cached synthetic page.
                with patch.object(r,'canonical',return_value=[{'class_id':'species_01','kind':'species'}]), patch.object(r,'validate_public'):
                    self.assertEqual(r.acquire(ds,{'synthetic_media':self.tmp.name}),1)
            self.assertEqual(ds.select('source_status')[0]['status'],'source_blocked')
            self.assertEqual(ds.select('source_failure')[0]['code'],'timeout')

    def test_lock_in_other_process_precedes_network(self):
        script='''import sys
from unittest.mock import patch
sys.path.insert(0,sys.argv[1])
import recover_p08 as r
c=r.load(r.read(r.Path(sys.argv[2])/'config.json'))
with patch('socket.create_connection',side_effect=AssertionError('network')):
 try:
  with r.Dataset(sys.argv[2],c,offline=True):raise AssertionError('concurrent writer')
 except r.RecoveryError as e:
  assert str(e)=='writer_locked'
'''
        with self.open():
            p=subprocess.run([sys.executable,'-B','-c',script,str(Path(r.__file__).parent),str(self.root)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)

    def test_missing_and_changed_taxonomic_evidence_blocks_finalization(self):
        with self.open() as ds:
            c=ds.ingest(candidate(),lambda _:image_bytes())
            # Mock only the pure decision to isolate the durable evidence gate.
            inspection={'p07_images':17,'records':[c]}
            r.persist(ds.path('inspection.json'),r.encode(inspection))
            r.persist(ds.path('Attributions.jsonl'),r.encode(c))
            r.persist(ds.path('evidence/map'),b'map')
            r.persist(ds.path('evidence/botanical'),b'botanical')
            d={'candidate_id':c['candidate_id'],'mapping':{'evidence_path':'evidence/map','evidence_sha256':r.sha(b'map')},
               'botanical_evidence_path':'evidence/botanical','botanical_evidence':r.sha(b'botanical')}
            file=Path(self.tmp.name)/'decision.json'
            file.write_bytes(r.encode({'authority':'human','decisions':[d]}))
            with patch.object(r,'decide',return_value='approved_for_dataset'):
                r.persist(ds.path('evidence/map'),b'changed')
                with self.assertRaisesRegex(r.RecoveryError,'mapping_evidence_hash'):r.finalize(ds,file)
                self.assertNotEqual(ds.records()[0]['state'],'approved_for_dataset')
                r.persist(ds.path('evidence/map'),b'map')
                r.persist(ds.path('evidence/botanical'),b'changed')
                with self.assertRaisesRegex(r.RecoveryError,'botanical_evidence_hash'):r.finalize(ds,file)
                r.persist(ds.path('evidence/botanical'),b'botanical')
                r.finalize(ds,file)
                before=r.tree_fingerprint(self.root);r.finalize(ds,file)
                self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_decision_stale_after_taxonomy_or_class_change(self):
        with self.open() as ds:c=ds.ingest(candidate(),lambda _:image_bytes())
        d={'authority':'human','reviewer':'Synthetic','reviewed_at':'2026-10-05T00:00:00Z','rationale':'synthetic',
           'candidate_id':c['candidate_id'],'original_sha256':c['original_sha256'],'sanitized_sha256':c['sanitized_sha256'],
           'evidence_digest':r.review_digest(c)}
        for key,value in [('mapping',{'source_taxon_id':123}),('class_ids',['species_02']),('author','Changed')]:
            changed=copy.deepcopy(c);changed[key]=value
            with self.assertRaisesRegex(r.RecoveryError,'stale_decision'):r.decide(changed,d)

    def test_acceptance_binds_all_final_files(self):
        with self.open() as ds:
            r.acquire(ds,{})
            for name in ['inspection.json','Attributions.jsonl','NOTICE.md','review.html']:
                r.persist(ds.path(name),b'{}\n')
            files={str(p.relative_to(self.root)):r.sha(p.read_bytes()) for p in self.root.rglob('*') if p.is_file() and p.name!='.lock'}
            manifest=r.encode({'files':files});r.persist(ds.path('final-manifest.json'),manifest)
            acceptance=Path(self.tmp.name)/'acceptance.json'
            acceptance.write_bytes(r.encode({'decision':'accepted','authority':'human','reviewer':'Synthetic',
                  'reviewed_at':'2026-10-05T00:00:00Z','manifest_sha256':r.sha(manifest),'training_authorized':False}))
            with patch.object(r,'historical',return_value=({},[])):
                self.assertEqual(r.verify(ds,self.root,acceptance),0)
                r.persist(ds.path('new-unbound-file'),b'x')
                with self.assertRaisesRegex(r.RecoveryError,'acceptance_coverage_or_bytes'):r.verify(ds,self.root,acceptance)

    def test_duplicate_comparison_against_17_with_boundary_distances(self):
        with self.open() as ds:
            rec=ds.ingest(candidate(),lambda _:image_bytes())
            h=int(rec['technical']['dhash64'],16)
            prior=[{'candidate_id':'Q'+str(i),'sanitized_sha256':'f'*64,'original_sha256':None,'observation_id':None,
                    'technical':{'dhash64':format(h^((1<<n)-1),'016x')}} for i,n in enumerate([6,7,10,11]+[20]*13)]
            with patch.object(r,'historical',return_value=({},prior)):
                report=r.inspect(ds,self.root)
                self.assertEqual(len(report['pairs']),17)
                self.assertEqual([p['signal'] for p in report['pairs'][:4]],['near_duplicate','borderline','borderline','no_algorithmic_signal'])
                before=r.tree_fingerprint(self.root);r.inspect(ds,self.root)
                self.assertEqual(before,r.tree_fingerprint(self.root))
                prior[0]['sanitized_sha256']=rec['sanitized_sha256']
                r.inspect(ds,self.root)
                self.assertEqual(ds.records()[0]['state'],'rejected_duplicate')
                self.assertTrue(ds.path(rec['original_path']).exists())

    def test_bad_schema_and_regressive_page(self):
        with self.assertRaises(r.RecoveryError):r.commons_page({},r.canonical()[0],'a'*64,self.config)
        with self.open() as ds:
            with self.assertRaisesRegex(r.RecoveryError,'cursor_regression'):ds.save_page('commons','species_01',10,[],10)
            for i in range(10):ds.save_page('commons','species_01',i*10,[],None)
            with self.assertRaisesRegex(r.RecoveryError,'page_budget'):ds.save_page('commons','species_01',100,[],None)

    def test_unsupported_media_classified_without_transfer(self):
        with self.open() as ds:
            c=candidate();c['file_url']='https://upload.wikimedia.org/a/a.svg'
            self.assertEqual(ds.ingest(c,lambda _:self.fail('unsupported media downloaded'))['state'],'rejected_format')
            self.assertEqual(ds.select('intention'),[])


class ExtraTransportProofs(DatasetCase, unittest.TestCase):
    transport=TransportTests.transport
    api=TransportTests.api
    media=TransportTests.media
    def test_retryable_http_and_maxlag(self):
        for status,body in [(429,b''),(500,b''),(502,b''),(503,b''),(504,b''),(200,b'{"error":{"code":"maxlag"}}')]:
            with self.subTest(status=status),tempfile.TemporaryDirectory() as td:
                with r.Dataset(Path(td)/'synthetic',self.config,offline=True) as ds:
                    transport,factory,_,sleeps=self.transport(ds,[FakeResponse(status,body,{'Retry-After':'2'}),FakeResponse()])
                    self.assertEqual(transport.get(self.api,'commons'),b'{}')
                    self.assertEqual(factory.call_count,2)
                    self.assertEqual(ds.select('response')[-1]['code'],'ok')
                    self.assertEqual(sleeps.call_args_list[0].args,(2,))

    def test_hour_and_media_reservations_survive_restart(self):
        for limit,reason in [('hour_bytes','hour_budget'),('media_bytes','media_budget')]:
            with self.subTest(limit=limit),tempfile.TemporaryDirectory() as td:
                config=copy.deepcopy(self.config);config['limits']['file_bytes']=8;config['limits'][limit]=12
                root=Path(td)/'synthetic'
                with r.Dataset(root,config,offline=True) as ds:
                    ds.append('request',{'request_id':'interrupted','source':'commons','media':True,'reserved':8,'epoch':1000})
                with r.Dataset(root,config,offline=True) as ds:
                    transport,factory,_,_=self.transport(ds,[])
                    with self.assertRaisesRegex(r.RecoveryError,reason):transport.get(self.media,'commons',True)
                    factory.assert_not_called()

    def test_retry_after_http_date_and_cancelled_request_accounting(self):
        with self.open() as ds:
            transport,factory,_,_=self.transport(ds,[FakeResponse(503,headers={'Retry-After':'Thu, 01 Jan 1970 00:20:00 GMT'})])
            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
            self.assertEqual(ds.select('resume_after')[0]['epoch'],1200)
        with self.open() as ds:
            transport,factory,_,_=self.transport(ds,[])
            with self.assertRaisesRegex(r.RecoveryError,'resume_after'):transport.get(self.api,'commons')
            factory.assert_not_called()


if __name__ == '__main__':
    unittest.main()

```

### scripts/phase1/test_inaturalist_source.py

```text
"""Synthetic iNaturalist adapter contracts; no network or real identifiers."""
import copy
import unittest
from inaturalist_source import ContractError, build_query, parse_page, photo_record


CUTOFF = "2026-10-05T00:00:00Z"
CLASS = {"class_id": "species_01", "kind": "species", "scientific_name": "Epipremnum aureum", "taxonomy_ref_ids": ["kew_species_01"]}


def crosswalk():
    return {"class_id": "species_01", "source": "inaturalist", "namespace": "inaturalist", "source_taxon_id": 999999001,
            "scientific_name": CLASS["scientific_name"], "rank": "species", "status": "active", "synonym_of": None,
            "authorship": None, "authorship_missing_reason": "Not supplied by synthetic source", "taxonomy_ref_ids": ["kew_species_01"],
            "evidence": {"url": "https://www.inaturalist.org/taxa/999999001", "version": "fixture-v1", "date": "2026-10-04", "sha256": "a" * 64},
            "reviewer": {"id": "synthetic-reviewer", "qualification": "synthetic botanist", "decision": "approved"}}


def observation(identifier=999999002):
    return {"id": identifier, "created_at": "2026-10-04T00:00:00Z", "quality_grade": "research", "license_code": "cc0",
            "taxon": {"id": 999999001, "name": CLASS["scientific_name"], "rank": "species", "is_active": True},
            "photos": [{"id": 999999003, "license_code": "cc-by", "attribution": "Synthetic author, CC BY", "url": "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg"}]}


def legal():
    return {"photo_id": 999999003, "observation_id": 999999002, "reviewer": "synthetic-reviewer", "reviewed_at": CUTOFF,
            "author": "Synthetic author", "licensor": "Synthetic author", "credit": "Synthetic credit", "decision": "approved",
            "photo": {"license_code": "cc-by", "version": "4.0", "legal_url": "https://creativecommons.org/licenses/by/4.0/", "evidence_sha256": "b" * 64, "source_url": "https://www.inaturalist.org/photos/999999003", "restrictions": []},
            "observation": {"license_code": "cc0", "version": "1.0", "legal_url": "https://creativecommons.org/publicdomain/zero/1.0/", "evidence_sha256": "c" * 64, "source_url": "https://www.inaturalist.org/observations/999999002", "restrictions": []},
            "database_rights": "compatible"}


def page(*observations):
    return {"total_results": len(observations), "page": 1, "per_page": 100, "results": list(observations)}


class AdapterTests(unittest.TestCase):
    def test_query_exact_contract(self):
        query = build_query(crosswalk(), CLASS, CUTOFF)
        self.assertEqual(query["taxon_id"], 999999001)
        self.assertEqual(query["created_d2"], "2026-10-05")
        self.assertEqual((query["order_by"], query["order"], query["per_page"]), ("id", "asc", 100))
        self.assertEqual(query["quality_grade"], "research")
        self.assertEqual(query["photos"], "true")

    def test_crosswalk_required_fields_and_identity(self):
        for key in crosswalk():
            entry = crosswalk()
            del entry[key]
            if key == "authorship_missing_reason":
                pass
            with self.subTest(key=key), self.assertRaises(ContractError):
                build_query(entry, CLASS, CUTOFF)
        for key, value in [("scientific_name", "Pothos aureus"), ("namespace", "wikidata"), ("source_taxon_id", True), ("rank", "subspecies"), ("status", "inactive"), ("synonym_of", 9), ("taxonomy_ref_ids", [])]:
            entry = crosswalk()
            entry[key] = value
            with self.subTest(key=key), self.assertRaises(ContractError):
                build_query(entry, CLASS, CUTOFF)

    def test_protection_never_queries(self):
        for class_id in ("outra_planta", "imagem_invalida"):
            with self.assertRaises(ContractError):
                build_query(crosswalk(), {"class_id": class_id, "kind": "protection"}, CUTOFF)

    def test_cutoff_must_have_timezone(self):
        with self.assertRaises(ContractError):
            build_query(crosswalk(), CLASS, "2026-10-05")

    def test_photo_code_alone_never_authorizes(self):
        obs = observation()
        result = photo_record(obs["photos"][0], obs)
        self.assertFalse(result["download_allowed"])
        self.assertIsNone(result["file_url"])
        self.assertIn("needs_license_review", result["reasons"])
        obs["photos"][0]["license_code"] = ["cc-by"]
        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])

    def test_documented_size_mapping_and_individual_evidence(self):
        obs = observation()
        result = photo_record(obs["photos"][0], obs, legal())
        self.assertTrue(result["download_allowed"])
        self.assertTrue(result["file_url"].endswith("/999999003/original.jpg"))
        self.assertEqual(result["origin_fidelity"], "provider_original")
        self.assertFalse(result["camera_original_verified"])

    def test_observation_rights_do_not_inherit_photo_rights(self):
        obs = observation()
        obs["license_code"] = "cc-by-nc"
        self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])

    def test_legal_proof_must_bind_ids_and_version_author_and_database(self):
        for field, value in [("photo_id", 9), ("observation_id", 9), ("author", ""), ("licensor", ""), ("credit", ""), ("reviewer", ""), ("database_rights", "unknown")]:
            proof = legal()
            proof[field] = value
            obs = observation()
            with self.subTest(field=field):
                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])
        for field, value in [("version", "3.0"), ("legal_url", "https://creativecommons.org/licenses/by/3.0/"), ("restrictions", ["extra"]), ("evidence_sha256", None), ("source_url", "https://www.inaturalist.org/photos/9")]:
            proof = legal()
            proof["photo"][field] = value
            obs = observation()
            with self.subTest(field=field):
                self.assertFalse(photo_record(obs["photos"][0], obs, proof)["download_allowed"])

    def test_url_confusion_does_not_generate_original(self):
        urls = ["http://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com.evil.invalid/photos/999999003/square.jpg", "https://user@inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com:444/photos/999999003/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/9/square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/../square.jpg", "https://inaturalist-open-data.s3.amazonaws.com/photos/999999003/square.gif", "https://static.inaturalist.org/photos/999999003/square.jpg"]
        for url in urls:
            obs = observation()
            obs["photos"][0]["url"] = url
            with self.subTest(url=url):
                self.assertFalse(photo_record(obs["photos"][0], obs, legal())["download_allowed"])

    def test_page_preserves_pending_without_location(self):
        obs = observation()
        obs["location"] = "0,0"
        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
        self.assertEqual(len(result["candidates"]), 1)
        self.assertFalse(result["candidates"][0]["download_allowed"])
        self.assertNotIn("location", result["candidates"][0])
        self.assertEqual(result["next_id_above"], obs["id"])

    def test_exact_species_and_active_required(self):
        for key, value in [("id", 999999004), ("name", "Pothos aureus"), ("rank", "subspecies"), ("is_active", False)]:
            obs = observation()
            obs["taxon"][key] = value
            result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
            self.assertEqual(result["candidates"][0]["taxonomic_confidence"], "conflict")
            self.assertIn("needs_taxonomic_mapping", result["candidates"][0]["reasons"])

    def test_regressive_duplicate_or_after_cutoff_page_fails(self):
        for observations in [(observation(), observation()), (observation(999999004), observation()), (dict(observation(), created_at="2026-10-06T00:00:00Z"),)]:
            with self.assertRaises(ContractError):
                parse_page(page(*observations), crosswalk(), CLASS, CUTOFF)
        with self.assertRaises(ContractError):
            parse_page(page(observation()), crosswalk(), CLASS, CUTOFF, id_above=999999002)

    def test_schema_failures(self):
        for response in [{}, {"results": []}, dict(page(), per_page=101), dict(page(), page=2), dict(page(), total_results=True), page(dict(observation(), photos=None)), page(dict(observation(), quality_grade="casual"))]:
            with self.subTest(response=response), self.assertRaises(ContractError):
                parse_page(response, crosswalk(), CLASS, CUTOFF)

    def test_100_photo_ceiling_with_deferred_accounting(self):
        obs = observation()
        obs["photos"] = [dict(obs["photos"][0], id=999999100+i) for i in range(105)]
        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
        self.assertEqual(len(result["candidates"]), 100)
        self.assertEqual(result["deferred_photo_count"], 5)

    def test_duplicate_media_not_inflated(self):
        obs = observation()
        obs["photos"].append(copy.deepcopy(obs["photos"][0]))
        result = parse_page(page(obs), crosswalk(), CLASS, CUTOFF)
        self.assertEqual(len(result["candidates"]), 1)
        self.assertEqual(result["duplicate_photo_count"], 1)


if __name__ == "__main__":
    unittest.main()

```

### Reconciled evidence
```json
{
  "kind": "working_bytes_evidence_reconciliation_not_guard_proof",
  "checked_at": "2026-10-07T23:08:02.977490+00:00",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "records": {
    "regression-red": {
      "record_sha256": "2864ff57364b9b510b1adca8f51c35a70760fe247af4e149cb1c1c0b31538a74",
      "source_and_output_hashes_match": true,
      "exit_code": 1,
      "stderr_summary": [
        "----------------------------------------------------------------------",
        "Ran 3 tests in 0.125s",
        "",
        "FAILED (failures=12)"
      ]
    },
    "regression-green": {
      "record_sha256": "25d8cf974fbca0acc4efdf9db4e7f031922ad419011f13098b983513429c775b",
      "source_and_output_hashes_match": true,
      "exit_code": 0,
      "stderr_summary": [
        "----------------------------------------------------------------------",
        "Ran 3 tests in 0.205s",
        "",
        "OK"
      ]
    },
    "focal-recovery": {
      "record_sha256": "f11a87b06b5d6685436b8fef49b5701cbdd4c55a749cc991ce4dedef69fe5083",
      "source_and_output_hashes_match": true,
      "exit_code": 0,
      "stderr_summary": [
        "----------------------------------------------------------------------",
        "Ran 54 tests in 3.052s",
        "",
        "OK"
      ]
    },
    "focal-adapter": {
      "record_sha256": "e436f8a3c87bcb8f47b277eb584c48b1fb470df3d18dff91e0e7d88fa77791aa",
      "source_and_output_hashes_match": true,
      "exit_code": 0,
      "stderr_summary": [
        "----------------------------------------------------------------------",
        "Ran 15 tests in 0.007s",
        "",
        "OK"
      ]
    },
    "affected-history": {
      "record_sha256": "e7b361798327987874e95052d1f9f900d37dae9871cb298b3aedb6f97676c25f",
      "source_and_output_hashes_match": true,
      "exit_code": 0,
      "stderr_summary": [
        "----------------------------------------------------------------------",
        "Ran 236 tests in 10.852s",
        "",
        "OK"
      ]
    }
  },
  "historical_red_proof_id": "proof-6928ea925e6f438e3873543389326106",
  "historical_red_commit": "7981377a433270c9e2072fcafdf89b690988fa08",
  "mutations_reused": [
    "advance_cursor_before_commit",
    "allow_private_export",
    "bypass_expert",
    "bypass_license",
    "ignore_hash_mismatch"
  ],
  "preexisting_documents_unchanged": true,
  "preexisting_changed_only_by_authorized_fix_transition": [
    "artifacts/bianchini/v2/codex/convergence/P08/1.json",
    "artifacts/bianchini/v2/codex/convergence/P08/1.json.bak"
  ],
  "external_bytes_and_mtimes_unchanged": true,
  "external_counts": {
    "p06-recovery-20260928": 29,
    "p07-curation-20260928": 13,
    "p08-recovery-20261005": 139,
    "p08-recovery-20261005-backup": 138
  },
  "external_inventory_sha256": "6f35f2692d2901aa6bffbdea44912940267bbddf069452f2b0a3650374d9a30f",
  "dependency_hashes": {
    "artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS": "9320075a4d42195b90473ff11a945e37746f80d7691876f2c95dfc8f80241e3e",
    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json": "350eafe638c4e143b0f63a0c8b0f49c70d64a11010d9072d4766c1acd885419b",
    "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md": "272b3f3d1817897bbfb39f0a2938c60519ee3fa88ec182530c2412e6f6c41e23",
    "artifacts/bianchini/v2/evidence/P05-f1-man01/validation-report.json": "f343ca45d1cfca2ff0cfa79c2d34ebf5849729b825533247652e912424f927ee",
    "docs/phase1/offline-class-manifest.v1.json": "bb07a888733b989bec1530584a3536b46dc87a0d8dd583f810fcfae0b41e930c",
    "scripts/phase1/acquire_commons.py": "ddd2bf5d5f6c7e75fe090af8fd0313a9785fefccb30ee3a62b070a48f0ba6046",
    "scripts/phase1/curate_p07.py": "8e06110673ebcb6ba8c8d354d0e49873e8cde184adf53d9523cc8c2f99970307",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
    "scripts/phase1/requirements-p06.txt": "41b54a6fb2918667ca47a61d73b522629d84490f3d78f0f20b21135faba10d35",
    "scripts/phase1/test_acquire_commons.py": "3d7781ef2e70f9ee57331cff72848ac3b61be3c9ec33f627ae8c8b4fb01d622e",
    "scripts/phase1/test_curate_p07.py": "421143b0674c3ccbaa9bafa3096ecf4dee5ecac2525779bc926c499244787cb5",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_offline_manifest.py": "88a892ee8935c87a74a4ac0ed6878f391945b3c54fb934485eb52c7b24e8c0fe",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/validate_offline_manifest.py": "d7e7776d99a756d7f6eeaee5ec4c92769abe37435a4f3861010d9ae3c66469ed"
  },
  "new_test_executions": 0,
  "guard_proofs_for_fixed_bytes": false
}
```

### regression-red
```json
{
  "kind": "working_bytes_not_guard_proof",
  "argv": [
    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
    "-B",
    "-m",
    "unittest",
    "discover",
    "-s",
    "scripts/phase1",
    "-p",
    "test_recover_p08.py",
    "-k",
    "InaturalistResumeTests",
    "-v"
  ],
  "cwd": ".",
  "started_at": "2026-10-07T22:56:35.344637+00:00",
  "exit_code": 1,
  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stderr_sha256": "075c3b2c347da14449578a2d7767c01ef8b62bf9c54bace09fb9e20e1bd27ded",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "source_sha256": {
    "scripts/phase1/recover_p08.py": "61beac0f921cf8853459fe7ec907cde7d812176e705acd09372974dec5aecf65",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
  }
}

```
```text
test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... 
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after') ... FAIL
  test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout') ... FAIL
test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... FAIL
test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... FAIL

======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_429')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'http_429'
- inaturalist_contract_or_evidence
+ http_429


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_500')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'http_500'
- inaturalist_contract_or_evidence
+ http_500


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_502')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'http_502'
- inaturalist_contract_or_evidence
+ http_502


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_503')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'http_503'
- inaturalist_contract_or_evidence
+ http_503


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='http_504')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'http_504'
- inaturalist_contract_or_evidence
+ http_504


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='maxlag')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'maxlag'
- inaturalist_contract_or_evidence
+ maxlag


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='network_error')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'network_error'
- inaturalist_contract_or_evidence
+ network_error


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='response_timeout')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'response_timeout'
- inaturalist_contract_or_evidence
+ response_timeout


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='resume_after')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'resume_after'
- inaturalist_contract_or_evidence
+ resume_after


======================================================================
FAIL: test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) (error='RecoveryError', code='timeout')
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 584, in test_only_existing_transient_recovery_codes_allow_restart
    self.assertEqual(ds.select('source_failure')[-1]['code'], expected)
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
- inaturalist_contract_or_evidence
+ timeout


======================================================================
FAIL: test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 594, in test_timeout_restart_does_not_reset_request_budget
    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
- inaturalist_contract_or_evidence
+ timeout


======================================================================
FAIL: test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/scripts/phase1/test_recover_p08.py", line 534, in test_timeout_then_restart_preserves_journal_limits_and_candidates
    self.assertEqual(ds.select('source_failure')[-1]['code'], 'timeout')
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 'inaturalist_contract_or_evidence' != 'timeout'
- inaturalist_contract_or_evidence
+ timeout


----------------------------------------------------------------------
Ran 3 tests in 0.125s

FAILED (failures=12)

```

### regression-green
```json
{
  "kind": "working_bytes_not_guard_proof",
  "argv": [
    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
    "-B",
    "-m",
    "unittest",
    "discover",
    "-s",
    "scripts/phase1",
    "-p",
    "test_recover_p08.py",
    "-k",
    "InaturalistResumeTests",
    "-v"
  ],
  "cwd": ".",
  "started_at": "2026-10-07T22:56:42.229752+00:00",
  "exit_code": 0,
  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stderr_sha256": "6f0e4d46faa4c6c557f82641ba8841467d29ef7b476c78e8d2e92b63426da1b0",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "source_sha256": {
    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
  }
}

```
```text
test_only_existing_transient_recovery_codes_allow_restart (test_recover_p08.InaturalistResumeTests.test_only_existing_transient_recovery_codes_allow_restart) ... ok
test_timeout_restart_does_not_reset_request_budget (test_recover_p08.InaturalistResumeTests.test_timeout_restart_does_not_reset_request_budget) ... ok
test_timeout_then_restart_preserves_journal_limits_and_candidates (test_recover_p08.InaturalistResumeTests.test_timeout_then_restart_preserves_journal_limits_and_candidates) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.205s

OK

```

### focal-recovery
```json
{
  "kind": "working_bytes_not_guard_proof",
  "argv": [
    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
    "-B",
    "-m",
    "unittest",
    "discover",
    "-s",
    "scripts/phase1",
    "-p",
    "test_recover_p08.py"
  ],
  "cwd": ".",
  "started_at": "2026-10-07T22:56:52.443028+00:00",
  "exit_code": 0,
  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stderr_sha256": "d6807d48dc59e538aaffafb4ba2b5efb940298a9b4424081573c8fc748b23ec3",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "source_sha256": {
    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
  }
}

```
```text
......................................................
----------------------------------------------------------------------
Ran 54 tests in 3.052s

OK

```

### focal-adapter
```json
{
  "kind": "working_bytes_not_guard_proof",
  "argv": [
    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
    "-B",
    "-m",
    "unittest",
    "discover",
    "-s",
    "scripts/phase1",
    "-p",
    "test_inaturalist_source.py"
  ],
  "cwd": ".",
  "started_at": "2026-10-07T22:56:55.827623+00:00",
  "exit_code": 0,
  "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "stderr_sha256": "edecde55c6deed9a44f005853dbf1b80bb79f5daf63b49aa23fa401cf6e41cc0",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "source_sha256": {
    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
  }
}

```
```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.007s

OK

```

### affected-history
```json
{
  "kind": "working_bytes_not_guard_proof",
  "argv": [
    "/home/administradorarthur/.cache/scanplant/venvs/p07/bin/python",
    "-B",
    "-m",
    "unittest",
    "discover",
    "-s",
    "scripts/phase1",
    "-p",
    "test_*.py"
  ],
  "cwd": ".",
  "started_at": "2026-10-07T22:56:55.924807+00:00",
  "exit_code": 0,
  "stdout_sha256": "c61e3282e6e192011393ad68feb5d3f44ee3708d73723b8f203eddacb405f687",
  "stderr_sha256": "de07d34fe95e1ee883614ee22f0e61ab7946a79b4622248b652462640df72eac",
  "head": "7981377a433270c9e2072fcafdf89b690988fa08",
  "source_sha256": {
    "scripts/phase1/recover_p08.py": "c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7",
    "scripts/phase1/test_recover_p08.py": "389408e2c122d4f52b809c56b48138a2067bed671d16a3c056ca3825bab8a239",
    "scripts/phase1/inaturalist_source.py": "bbca4e7d174bdb82e9a75784390dcfd979524ff3cea35754b79cc4c32dac5366",
    "scripts/phase1/test_inaturalist_source.py": "bfddf7c6bb58cce85795c18ff992b96c226d385cb806de813103908a8606967e",
    "scripts/phase1/test_p08_mutation.py": "ee69b259e0e311b2123acd0041e6ffc742c624721f9514ccd1ddab23c21ca7ad"
  }
}

```
```text
............................................................................................................................................................................................................................................
----------------------------------------------------------------------
Ran 236 tests in 10.852s

OK

```
