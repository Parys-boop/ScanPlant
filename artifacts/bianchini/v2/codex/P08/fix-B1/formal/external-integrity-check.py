from pathlib import Path
import sys,json,hashlib,stat,fcntl,subprocess,re
from unittest.mock import patch
sys.path.insert(0,str(Path.cwd()/'scripts/phase1'))
import recover_p08 as r
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
root=Path.cwd();base=Path('/home/administradorarthur/datasets/scanplant');data=base/'p08-recovery-20261005';backup=base/'p08-recovery-20261005-backup';source=base/'p06-recovery-20260928'
receipt=json.loads((root/'artifacts/bianchini/v2/codex/P08/human-acceptance.json').read_bytes())
assert receipt['decision']=='accepted' and receipt['authority']=='human' and receipt['scope']=='technical_and_documentary_bytes_only'
assert receipt['approved_git_delivery_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/final-files.sha256')
assert receipt['approved_checkpoint_sha256']==h(root/'artifacts/bianchini/v2/codex/P08/continuation-checkpoint.json')
assert receipt['baseline']=='24de252d27a137281c02cad50533280bb82dd80d'
assert receipt['counts']==dict(candidates_pending=1088,transferred=0,p08_images=0,approved_for_dataset=0,usable=0)
assert receipt['zero_transfer_result_accepted'] is True and receipt['U-803']=='candidate_opinions_pending'
for k in ['candidate_approval','download_authorized','authorship_confirmation','rights_approval','botanical_confirmation','privacy_approval','duplicate_decisions_conclusive','training_authorized','partition_authorized','p09_started']:assert receipt[k] is False,k
assert receipt['release']=='pending'
before={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}
manifest=json.loads((data/'final-manifest.json').read_bytes())
for folder in [data,backup]:
 assert h(folder/'final-manifest.json')==receipt['approved_external_manifest_sha256']=='334789e383c74c264190b42216cdfa37831d5209eba5180189f189712ccab716'
 actual={str(p.relative_to(folder)):h(p) for p in folder.rglob('*') if p.is_file() and p.name not in ['.lock','final-manifest.json']}
 assert actual==manifest['files'] and len(actual)==137
 assert stat.S_IMODE(folder.stat().st_mode)==0o700
 for p in folder.rglob('*'):
  assert not p.is_symlink()
  assert stat.S_IMODE(p.stat().st_mode)==(0o700 if p.is_dir() else 0o600)
  assert p.suffix.lower() not in {'.jpg','.jpeg','.png','.webp','.gif'}
assert (data/'.lock').read_bytes()==b''
config=r.load(r.read(data/'config.json'));assert r.sha(r.encode(config))==manifest['config_sha256']
original_runtime={name:hashlib.sha256(subprocess.check_output(['git','show','7981377a433270c9e2072fcafdf89b690988fa08'+':scripts/phase1/'+name])).hexdigest() for name in r.fingerprint()}
assert manifest['runtime_code_sha256']==original_runtime
assert {k for k,v in r.fingerprint().items() if v!=original_runtime[k]}=={'recover_p08.py'}
assert manifest['code_sha256']==config['code_sha256']
assert config['code_sha256']['recover_p08.py']==r.HTML_ORDER_PREDECESSOR
with (data/'.lock').open('rb') as lock,patch('socket.socket.connect',side_effect=AssertionError('network_forbidden')),patch('socket.getaddrinfo',side_effect=AssertionError('network_forbidden')):
 fcntl.flock(lock,fcntl.LOCK_SH|fcntl.LOCK_NB)
 ds=r.Dataset(data,config);ds.replay();ds.verify_objects()
 assert ds.events[0]['data']==config
 assert {'from':config['code_sha256'],'to':original_runtime,'reason':'deterministic_review_html_key_order'} in ds.select('code_compatibility')
 assert r.verify(ds,source)==0
 hashes,images=r.historical(source);assert len(hashes)==29 and len(images)==17
 records=ds.records();summary=ds.summary()
 assert len(records)==1088 and summary==r.load(r.read(data/'summary.json'))==r.load(r.read(root/'artifacts/phase1/p08/summary.json'))
 assert summary['usable']==0 and summary['training_authorized'] is False and summary['partition_authorized'] is False
 assert all(x['state']!='approved_for_dataset' and not x.get('original_sha256') and not x.get('sanitized_sha256') for x in records)
 assert len(ds.select('page'))==len(ds.select('cursor'))==120 and not ds.select('committed') and not ds.select('received') and not ds.select('source_failure')
 assert all(x['status']=='no_crosswalk' for x in summary['coverage'] if x['source']=='inaturalist' and x['class_id'].startswith('species_'))
 assert len(summary['coverage'])==28 and all(x['transferred']==x['approved']==0 for x in summary['coverage'])
 review=r.load(r.read(data/'human-review.json'));objects=r.load(r.read(data/'object-hashes.json'));decisions=r.load(r.read(data/'decisions.template.json'))
 assert len(review['candidates'])==len(objects)==len(decisions['decisions'])==1088
 assert {x['candidate_id'] for x in review['candidates']}=={x['candidate_id'] for x in records}=={x['candidate_id'] for x in decisions['decisions']}
 assert all(x['reviewer'] is None and x['expert_confirmation'] is False for x in decisions['decisions'])
 assert r.read(data/'Attributions.jsonl')==b''
 assert len(ds.select('request'))==120
 for n in ['historical-before.json','historical-before-after.json']:
  historical=r.load(r.read(data/n));assert len(historical)==17
 # Replay and verification are read-only: no acquisition/inspection/finalization invocation.
 ds2=r.Dataset(data,config);ds2.replay();assert ds2.events==ds.events and ds2.summary()==summary
assert before=={str(p):r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}
print(json.dumps({'result':'passed','external_files_each':138,'manifest_sha256':receipt['approved_external_manifest_sha256'],'historical_files':29,'historical_images':17,'p07_receipt_hashes':7,'candidates_pending':1088,'transferred':0,'approved_for_dataset':0,'usable':0,'read_only_replay_bytes_and_mtimes_unchanged':True,'acceptance':'technical_bytes_only','candidate_review':'pending','inat':'no_crosswalk','training_authorized':False,'release':'pending','p09_started':False},sort_keys=True))

original_before=json.loads(Path('/home/administradorarthur/code/scanplant-current/.worktrees/ScanPlant/p08/artifacts/bianchini/v2/codex/P08/fix-B1/external-before.json').read_text())
assert {p.name:r.tree_fingerprint(p) for p in [data,backup,source,base/'p07-curation-20260928']}==original_before
