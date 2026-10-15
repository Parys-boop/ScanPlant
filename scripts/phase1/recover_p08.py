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
# Exact accepted B1 bytes: compatibility never edits the original config/hash.
RIGHTS_REVIEW_PREDECESSOR = 'c77fc7844fb724bbd971edb5effdd3b68aa6f88ab24227168262b3183bb96de7'

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
    current=fingerprint()
    compatible=[current,*[{**current,'recover_p08.py':h} for h in (HTML_ORDER_PREDECESSOR,RIGHTS_REVIEW_PREDECESSOR)]]
    require(c['manifest_sha256']==sha(read(MANIFEST)) and c['code_sha256'] in compatible,'config_fingerprint')
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

def legal_url_for_comparison(url):
    # Only the two representations verified in the preserved Commons evidence.
    # Never rewrite provenance or follow arbitrary redirects to identify a grant.
    return {'http://creativecommons.org/publicdomain/zero/1.0/deed.en':
                'https://creativecommons.org/publicdomain/zero/1.0/',
            'https://creativecommons.org/licenses/by/4.0':
                'https://creativecommons.org/licenses/by/4.0/'}.get(url,url) if isinstance(url,str) else None


RIGHTS_SUBJECT_FIELDS=('source','media_id','class_ids','page_id','revision_id','file_url','source_page_url',
    'mime','declared_size','declared_width','declared_height','source_sha1','source_timestamp','author',
    'license_id','license_name','license_url','restrictions','credit','attribution','evidence_sha256',
    'rights_consistent','database_rights','mapping','mapping_reason','scientific_name_received',
    'taxonomic_confidence','observation_id','origin_fidelity','camera_original_verified')

def rights_subject_digest(c):
    """Bind a grant to immutable source facts, independent of later pixel triage."""
    return sha(encode({k:c.get(k) for k in RIGHTS_SUBJECT_FIELDS}))

def human_rights_clearance(c):
    d=c.get('rights_review') or {}
    return (isinstance(d,dict) and d.get('authority')=='human' and bool(d.get('reviewer')) and
            bool(d.get('reviewed_at')) and bool(d.get('rationale')) and
            d.get('decision')=='approved_for_transfer' and
            d.get('individual_rights')==d.get('database_rights')=='passed' and
            d.get('candidate_id')==candidate_id(c) and d.get('subject_digest')==rights_subject_digest(c) and
            d.get('source_evidence_sha256')==c.get('evidence_sha256') and
            bool(SHA.fullmatch(str(d.get('document_sha256','')))) and
            bool(SHA.fullmatch(str(d.get('imported_evidence_sha256','')))))

def rights(c):
    allowed={'cc-by-4.0':({'CC BY 4.0'},'https://creativecommons.org/licenses/by/4.0/'),
             'cc0':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/'),
             'cc-zero':({'CC0','CC0 1.0'},'https://creativecommons.org/publicdomain/zero/1.0/')}
    rule=allowed.get(c.get('license_id'))
    if not rule or c.get('license_name') not in rule[0] or legal_url_for_comparison(c.get('license_url'))!=rule[1]:return 'needs_license_review'
    if not c.get('author') or re.search(r'\b(unknown|anonymous|desconhecid[oa])\b',c['author'],re.I):return 'needs_license_review'
    if c.get('restrictions') or c.get('rights_consistent') is not True:return 'needs_license_review'
    if c.get('rights_review') and not human_rights_clearance(c):return 'needs_license_review'
    if c.get('database_rights')!='passed' and not human_rights_clearance(c):return 'needs_license_review'
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
    def __init__(self,root,config,offline=False,defer_compatibility=False):
        self.root=safe_path(root);self.config=config;self.offline=offline;self.events=[];self.fd=None
        self.defer_compatibility=defer_compatibility
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
            if not self.defer_compatibility:self.record_compatibility()
            return self
        except BaseException:
            os.close(self.fd);self.fd=None;raise
    def __exit__(self,*args):
        if self.fd is not None:os.close(self.fd);self.fd=None
    def record_compatibility(self):
        if self.config['code_sha256']!=fingerprint():
            transition={'from':self.config['code_sha256'],'to':fingerprint(),'reason':'rights_review_and_targeted_resume'}
            if transition not in self.select('code_compatibility'):self.append('code_compatibility',transition)
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
            if e['type']=='rights_review':
                review=d['rights_review']
                require(sha(read(self.path(review['document_path'])))==review['document_sha256'],'rights_document_hash')
                require(sha(read(self.path(review['imported_evidence_path'])))==review['imported_evidence_sha256'],'rights_evidence_hash')
            if e['type']=='local_acquisition_account':
                require(sha(read(self.path(d['document_path'])))==d['document_sha256'],'local_account_evidence_hash')
    def records(self):
        result={}
        for e in self.events:
            if e['type'] in {'committed','classified','rights_review'}:result[e['data']['candidate_id']]=dict(e['data'])
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
        reviewed_pending=bool(old and old['state'] in {'needs_license_review','discovered'} and
                              not old.get('original_sha256') and human_rights_clearance(old) and
                              c.get('rights_review')==old.get('rights_review'))
        if old and not reviewed_pending and not (old['state']=='transfer_failed' and set(old.get('reasons',[])) & RETRYABLE):
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
    def summary(self,records=None):
        recs=self.records() if records is None else records;coverage=[]
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
            accounts=self.ds.select('local_acquisition_account')
            require(sum(x['source']==source for x in reservations)+sum(x['request_debit'] for x in accounts if x['source']==source)<self.ds.config['limits']['requests'],'request_budget')
            media_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'])
            hour_total=sum(finished.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations
                           if x['media'] and x['epoch']>time.time()-3600)
            media_total+=sum(x['media_debit'] for x in accounts)
            hour_total+=sum(b['bytes'] for x in accounts for b in x['media_buckets'] if b['epoch']>time.time()-3600)
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
            attrs[-1]['changes']=r.get('local_import',{}).get('changes','EXIF orientation; RGB pixel reconstruction; metadata removal; JPEG quality 95 or PNG; no crop or enhancement')
            if r.get('local_import'):attrs[-1]['source_notices']=r['local_import']['notices_path']
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


def prepare_rights_review(ds,review_file):
    """Import a real, explicitly scoped human document without transferring media.

    All batch entries/evidence are validated before writing. Existing config,
    source metadata and events stay immutable; a rights_review event supersedes
    only the selected pending records. Repetition after a crash is idempotent.
    """
    ds.verify_objects()
    review_file=safe_path(review_file);raw=read(review_file);document=load(raw)
    require(set(document)=={'schema_version','authority','scope','config_sha256','decisions'},'rights_review_schema')
    require(document['schema_version']==1 and document['authority']=='human' and
            document['scope']=='commons_candidate_rights' and document['config_sha256']==ds.config_hash,'rights_review_scope')
    items=document['decisions'];require(isinstance(items,list) and bool(items),'rights_review_items')
    require(all(isinstance(d,dict) and isinstance(d.get('candidate_id'),str) for d in items),'rights_review_items')
    ids=[d['candidate_id'] for d in items];require(len(ids)==len(set(ids)),'duplicate_rights_reviews')
    records={c['candidate_id']:c for c in ds.records()};require(set(ids)<=set(records),'unknown_rights_candidate')
    document_hash=sha(raw);prepared=[]
    keys={'candidate_id','record_digest','subject_digest','source_evidence_sha256','authority','reviewer',
          'reviewed_at','rationale','decision','individual_rights','database_rights','evidence'}
    for d in items:
        require(set(d)==keys,'rights_review_fields')
        require(d['authority']=='human' and all(isinstance(d[k],str) and d[k].strip()
                for k in ['reviewer','reviewed_at','rationale']),'human_rights_authority')
        try:stamp=datetime.fromisoformat(d['reviewed_at'].replace('Z','+00:00'))
        except ValueError:raise RecoveryError('rights_review_date') from None
        require(stamp.tzinfo is not None,'rights_review_date')
        require(d['decision'] in {'approved_for_transfer','pending','rejected'} and
                d['individual_rights'] in {'passed','pending','rejected'} and
                d['database_rights'] in {'passed','pending','rejected'},'rights_review_decision')
        if d['decision']=='approved_for_transfer':
            require(d['individual_rights']==d['database_rights']=='passed','rights_review_incomplete')
        c=records[d['candidate_id']]
        require(c['source']=='commons' and d['subject_digest']==rights_subject_digest(c) and
                d['source_evidence_sha256']==c['evidence_sha256'],'stale_rights_subject')
        proof=d['evidence'];require(isinstance(proof,dict) and set(proof)=={'path','sha256'},'rights_evidence_schema')
        require(isinstance(proof['path'],str) and not Path(proof['path']).is_absolute() and
                '..' not in Path(proof['path']).parts and bool(SHA.fullmatch(str(proof['sha256']))),'rights_evidence_path')
        proof_raw=read(review_file.parent/proof['path'])
        require(sha(proof_raw)==proof['sha256'],'rights_evidence_hash')
        previous=c.get('rights_review') or {}
        same=previous.get('document_sha256')==document_hash
        if not same:
            require(not c.get('original_sha256') and c['state'] in {'needs_license_review','discovered'},'rights_candidate_state')
            require(d['record_digest']==review_digest(c),'stale_rights_record')
        prepared.append((c,d,proof_raw,same))
    return raw,prepared


def apply_rights_review(ds,raw,prepared):
    document_hash=sha(raw)
    for c,d,proof_raw,same in prepared:
        if same:continue
        proof_path='evidence/'+sha(proof_raw)+'.rights';doc_path='evidence/'+document_hash+'.rights.json'
        for path,content in [(proof_path,proof_raw),(doc_path,raw)]:
            persist(ds.path(path),content,True)
            if not any(e['path']==path for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':sha(content)})
        c=dict(c);c.pop('decision',None)
        c['rights_review']={**d,'document_path':doc_path,'document_sha256':document_hash,
            'imported_evidence_path':proof_path,'imported_evidence_sha256':sha(proof_raw)}
        ds.append('rights_review',c)
    ds.project()


def incorporate_rights_review(ds,review_file):
    """Validate the entire human batch, then append evidence and scoped decisions."""
    apply_rights_review(ds,*prepare_rights_review(ds,review_file))


def resume_candidates(ds,ids,download=None):
    """Transfer only explicitly named existing candidates; never query discovery.

    Production transport is mandatory outside offline fixtures. This helper does
    not finalize content or grant botanical/privacy/duplicate approval.
    """
    require(isinstance(ids,list) and bool(ids) and all(isinstance(x,str) for x in ids) and
            len(ids)==len(set(ids)),'resume_candidate_ids')
    require(download is None or ds.offline,'resume_fixture_only')
    ds.verify_objects();records={c['candidate_id']:c for c in ds.records()}
    require(set(ids)<=set(records),'unknown_resume_candidate')
    for cid in ids:
        c=records[cid]
        require(c['source']=='commons' and cid==candidate_id(c) and human_rights_clearance(c) and
                rights(c)=='passed','resume_rights_pending')
        require(c.get('original_sha256') or c['state'] in {'needs_license_review','discovered','deferred_budget'} or
                c['state']=='transfer_failed' and bool(set(c.get('reasons',[])) & RETRYABLE),'resume_candidate_state')
    transport=Transport(ds)
    for cid in ids:
        c=records[cid]
        if c['state']=='deferred_budget':continue
        ds.ingest(c,download or (lambda record:transport.get(record['file_url'],'commons',True)))
    ds.project()


def local_file(base,reference,limit=2*1024**2):
    """Read a bounded, owner-only regular file under an explicitly supplied root."""
    require(isinstance(reference,dict) and set(reference)=={'path','sha256'} and
            isinstance(reference['path'],str) and SHA.fullmatch(str(reference['sha256'])),'local_reference')
    name=Path(reference['path']);require(not name.is_absolute() and '..' not in name.parts,'local_path')
    base=safe_path(base);path=safe_path(base/name)
    require(path!=base and base in path.parents,'local_path')
    for part in [base,*list(path.parents)[:list(path.parents).index(base)],path]:
        mode=part.stat()
        require(mode.st_uid==os.getuid() and stat.S_IMODE(mode.st_mode)==(0o700 if part.is_dir() else 0o600),'local_permissions')
    require(path.is_file() and 0<path.stat().st_size<=limit,'local_size')
    raw=read(path);require(len(raw)<=limit and sha(raw)==reference['sha256'],'local_hash')
    return raw


def local_evidence_url(c):
    """An evidence URL is not a network destination. Never rewrite source facts."""
    url=c['file_url'];p=urlsplit(url)
    # Existing network validator stays strict. Only these recorded tracking keys
    # may occur in an offline source reference; no request is made to this URL.
    from urllib.parse import parse_qsl, urlunsplit
    require(isinstance(url,str) and not any(ord(x)<33 for x in url),'unsafe_url')
    query=parse_qsl(p.query,keep_blank_values=True,strict_parsing=True)
    require(len(query)==len({k for k,v in query}) and
            all(k in {'utm_source','utm_campaign','utm_content'} and v and
                len(v)<=512 and not any(ord(x)<32 for x in v) for k,v in query),'local_evidence_query')
    safe_url(urlunsplit((p.scheme,p.netloc,p.path,'',p.fragment)),c['source'],True)
    require(p.path.startswith('/wikipedia/commons/'),'local_evidence_path')
    return url


def validate_local_image(raw,mime,sanitized=False):
    """Decode existing bytes; do not transform or encode any pixels."""
    import warnings
    with warnings.catch_warnings():
        warnings.simplefilter('error',Image.DecompressionBombWarning)
        try:
            with Image.open(BytesIO(raw),formats=['JPEG','PNG']) as image:
                require(image.format in {'JPEG','PNG'} and getattr(image,'n_frames',1)==1 and
                        image.width*image.height<=25_000_000,'local_image_format')
                require(mime=={'JPEG':'image/jpeg','PNG':'image/png'}[image.format],'local_mime')
                image.verify()
            with Image.open(BytesIO(raw),formats=['JPEG','PNG']) as image:
                image.load();width,height=image.size;orientation=image.getexif().get(274,1)
                if sanitized:
                    require(image.mode=='RGB' and not image.getexif() and orientation==1,'local_metadata')
                    allowed={'jfif','jfif_version','jfif_unit','jfif_density'} if image.format=='JPEG' else set()
                    require(set(image.info)<=allowed,'local_metadata')
                    if image.format=='JPEG':
                        # Inspect application/comment segments as well as Pillow's
                        # known metadata: retain structural JFIF only, no trailer.
                        pos=2;require(raw[:2]==b'\xff\xd8','local_jpeg')
                        while pos<len(raw):
                            require(raw[pos]==255,'local_jpeg');pos+=1
                            while pos<len(raw) and raw[pos]==255:pos+=1
                            require(pos<len(raw),'local_jpeg');marker=raw[pos];pos+=1
                            if marker==0xd9:
                                require(pos==len(raw),'local_metadata');break
                            if marker==1 or 0xd0<=marker<=0xd8:continue
                            require(pos+2<=len(raw),'local_jpeg');size=int.from_bytes(raw[pos:pos+2],'big')
                            require(size>=2 and pos+size<=len(raw),'local_jpeg');payload=raw[pos+2:pos+size]
                            if 0xe0<=marker<=0xef or marker==0xfe:
                                require(marker==0xe0 and payload.startswith(b'JFIF\0'),'local_metadata')
                            pos+=size
                            if marker==0xda:
                                while True:
                                    pos=raw.find(b'\xff',pos);require(pos>=0,'local_jpeg');n=pos+1
                                    while n<len(raw) and raw[n]==255:n+=1
                                    require(n<len(raw),'local_jpeg')
                                    if raw[n]==0 or 0xd0<=raw[n]<=0xd7:pos=n+1;continue
                                    break
                        else:raise RecoveryError('local_jpeg')
                return width,height,orientation
        except (OSError,ValueError,SyntaxError,Image.DecompressionBombWarning,Image.DecompressionBombError) as error:
            if isinstance(error,RecoveryError):raise
            raise RecoveryError('local_image_decode') from None


def local_acquisition_account(ds,raw,records):
    """Conservatively reconcile observed external acquisition, without fake HTTP."""
    from urllib.parse import parse_qs
    data=load(raw)
    require(set(data)=={'schema_version','source','receipts','unreceipted_metadata'} and
            data['schema_version']==1 and data['source']=='commons' and
            isinstance(data['receipts'],list) and isinstance(data['unreceipted_metadata'],list),'local_account_schema')
    require(len(data['receipts'])+len(data['unreceipted_metadata'])<=ds.config['limits']['requests'],'request_budget')
    receipt_ids=[];buckets=[];covered=set()
    for receipt in data['receipts']:
        require(isinstance(receipt,dict) and all(k in receipt for k in ['utc','requested_url','status']),'local_receipt')
        try:stamp=datetime.fromisoformat(receipt['utc'].replace('Z','+00:00'))
        except (ValueError,TypeError):raise RecoveryError('local_receipt_date') from None
        require(stamp.tzinfo is not None and stamp.timestamp()<=time.time()+60,'local_receipt_date')
        p=urlsplit(receipt['requested_url']);require(p.scheme=='https' and p.netloc in
                {'commons.wikimedia.org','upload.wikimedia.org'} and not p.fragment and
                not any(ord(x)<33 for x in receipt['requested_url']),'local_receipt_url')
        media=p.netloc=='upload.wikimedia.org'
        if media:
            safe_url(receipt['requested_url'],'commons',True)
            matches=[c for c in records if urlsplit(c['file_url']).path==p.path]
            require(bool(matches),'local_receipt_subject')
        else:
            q=parse_qs(p.query)
            require((p.path=='/w/api.php' and q.get('action')==['query'] and
                     q.get('pageids') in [[str(c['page_id'])] for c in records] and
                     not any(k.startswith(('gsr','generator')) for k in q)) or
                    (p.path=='/w/index.php' and q.get('action')==['raw'] and
                     q.get('oldid') in [[str(c['revision_id'])] for c in records]),'local_receipt_subject')
        require(type(receipt['status']) is int and 100<=receipt['status']<=599,'local_receipt_status')
        identity=sha(encode([receipt['utc'],receipt['requested_url'],receipt['status']]))
        require(identity not in receipt_ids,'duplicate_local_receipt');receipt_ids.append(identity)
        if media:
            if receipt['status']==200:
                require(type(receipt.get('bytes')) is int and 0<receipt['bytes']<=ds.config['limits']['file_bytes'] and
                        any(receipt['bytes']==c['declared_size'] and receipt.get('sha256')==c['_local_original_sha256'] for c in matches),'local_receipt_bytes')
                debit=receipt['bytes']
                covered.update(c['candidate_id'] for c in matches if receipt['bytes']==c['declared_size'] and
                               receipt.get('sha256')==c['_local_original_sha256'])
            else:debit=ds.config['limits']['file_bytes'] # unknown response bytes: reserve the whole bound
            buckets.append({'epoch':stamp.timestamp(),'bytes':debit})
    require(covered=={c['candidate_id'] for c in records},'local_acquisition_coverage')
    for item in data['unreceipted_metadata']:
        require(isinstance(item,dict) and set(item)=={'evidence','reason'} and
                isinstance(item['evidence'],dict) and bool(item['reason']),'local_unreceipted')
        identity='unreceipted:'+item['evidence']['sha256'];require(identity not in receipt_ids,'duplicate_local_receipt')
        receipt_ids.append(identity)
    return {'source':'commons','account_id':sha(raw),'request_debit':len(receipt_ids),
            'media_debit':sum(b['bytes'] for b in buckets),'media_buckets':buckets,'receipt_ids':receipt_ids,
            'document_path':'evidence/'+sha(raw)+'.local','document_sha256':sha(raw)}


def import_local_pairs(ds,job_file,crash=lambda _:None):
    """Import at most two explicitly authorized local pairs; never fetch or sanitize.

    Validate the whole batch before the first journal event. A plan precedes
    copies; received/committed checkpoints resume without another reservation.
    Rights and observations are evidence, never botanical/privacy/data approval.
    """
    require(ds.fd is not None,'lock_required');ds.verify_objects()
    job_file=safe_path(job_file);base=job_file.parent
    job_raw=local_file(base,{'path':job_file.name,'sha256':sha(read(job_file))});job=load(job_raw);job_hash=sha(job_raw)
    require(set(job)=={'schema_version','scope','config_sha256','asset_root','authorization','rights_review',
                       'acquisition','notices','items'} and job['schema_version']==1 and
            job['scope']=='p08_local_quarantine_import' and job['config_sha256']==ds.config_hash,'local_job_scope')
    items=job['items'];require(isinstance(items,list) and 0<len(items)<=2 and all(isinstance(i,dict) for i in items),'local_items')
    ids=[i.get('candidate_id') for i in items];require(all(isinstance(i,str) for i in ids) and len(ids)==len(set(ids)),'local_ids')
    records={c['candidate_id']:c for c in ds.records()};require(set(ids)<=set(records),'unknown_local_candidate')
    auth_raw=local_file(base,job['authorization']);auth=load(auth_raw)
    require(auth.get('authority')=='human' and auth.get('scope')==job['scope'] and
            auth.get('config_sha256')==ds.config_hash and all(isinstance(auth.get(k),str) and auth[k].strip()
                for k in ['reviewer','reviewed_at','rationale']),'local_authority')
    try:stamp=datetime.fromisoformat(auth['reviewed_at'].replace('Z','+00:00'))
    except ValueError:raise RecoveryError('local_authority_date') from None
    require(stamp.tzinfo is not None,'local_authority_date')
    documents=[auth_raw,local_file(base,job['notices']),local_file(base,job['acquisition']),local_file(base,job['rights_review'])]
    acquisition=load(documents[2])
    require(isinstance(acquisition.get('unreceipted_metadata'),list),'local_account_schema')
    for missing in acquisition['unreceipted_metadata']:
        require(isinstance(missing,dict) and 'evidence' in missing,'local_unreceipted')
        documents.append(local_file(base,missing['evidence']))
    rights_file=base/job['rights_review']['path']
    rights_data=load(documents[3]);require(isinstance(rights_data.get('decisions'),list) and
            {d.get('candidate_id') for d in rights_data['decisions']}==set(ids),'local_rights_coverage')
    for d in rights_data['decisions']:local_file(rights_file.parent,d['evidence'])
    rights_raw,prepared=prepare_rights_review(ds,rights_file)
    require(rights_raw==documents[3],'local_hash')
    reviewed={}
    for c,d,proof,same in prepared:
        review={**d,'document_path':'evidence/'+sha(rights_raw)+'.rights.json',
                'document_sha256':sha(rights_raw),'imported_evidence_path':'evidence/'+sha(proof)+'.rights',
                'imported_evidence_sha256':sha(proof)}
        reviewed[c['candidate_id']]={**c,'rights_review':review}
    asset_root=safe_path(job['asset_root']);require(asset_root!=ROOT and ROOT not in asset_root.parents,'local_assets_in_git')
    ready=[];approved=[]
    for item in items:
        require(set(item)=={'candidate_id','subject_digest','source_evidence_sha256','original','sanitized','validation','observations'},'local_item_fields')
        c=records[item['candidate_id']];require(c['source']=='commons' and c['candidate_id']==candidate_id(c) and
                rights_subject_digest(c)==item['subject_digest'] and c['evidence_sha256']==item['source_evidence_sha256'],'local_subject')
        require(bool(c['class_ids']) and set(c['class_ids'])<={x['class_id'] for x in canonical()[:12]},'candidate_class')
        require(any(e['sha256']==c['evidence_sha256'] for e in ds.select('evidence')),'local_source_evidence')
        local_evidence_url(c);require(rights(reviewed[c['candidate_id']])=='passed','local_rights_pending')
        existing=c.get('local_import')
        require((existing and existing['job_sha256']==job_hash) or not c.get('original_sha256') and
                c['state'] in {'needs_license_review','discovered'},'local_candidate_state')
        original=local_file(asset_root,item['original'],ds.config['limits']['file_bytes'])
        clean=local_file(asset_root,item['sanitized'],ds.config['limits']['file_bytes'])
        require(len(original)==c['declared_size'] and hashlib.sha1(original).hexdigest()==c['source_sha1'],'local_original_identity')
        w,h,orientation=validate_local_image(original,c['mime'])
        require((w,h)==(c['declared_width'],c['declared_height']),'local_dimensions')
        cw,ch,_=validate_local_image(clean,c['mime'],True)
        require((cw,ch)==((h,w) if orientation in {5,6,7,8} else (w,h)),'local_dimensions')
        validation_raw=local_file(base,item['validation']);validation=load(validation_raw);documents.append(validation_raw)
        require(all(validation.get(k)==v for k,v in {'original_sha256':sha(original),'sanitized_sha256':sha(clean),
                'width':cw,'height':ch}.items()),'local_sanitization_evidence')
        require(isinstance(item['observations'],list) and len(item['observations'])<=4,'local_observations')
        observation_hashes=[]
        for ref in item['observations']:
            observation=local_file(base,ref);documents.append(observation);observation_hashes.append(sha(observation))
            observed=load(observation);require(observed.get('authority')=='human','local_observations')
            if isinstance(observed.get('items'),list):
                matches=[x for x in observed['items'] if x.get('candidate_id')==c['candidate_id']]
                require(len(matches)==1,'local_observation_subject');observed=matches[0]
            require(observed.get('candidate_id',c['candidate_id'])==c['candidate_id'],'local_observation_subject')
            observed_hashes=[observed.get(k) for k in ['sanitized_sha256','viewed_image_sha256']]
            if isinstance(observed.get('subject'),dict):observed_hashes.append(observed['subject'].get('sha256'))
            require(all(value is None or value==sha(clean) for value in observed_hashes),'local_observation_hash')
        approved.append({'candidate_id':c['candidate_id'],'subject_digest':item['subject_digest'],
                         'original_sha256':sha(original),'sanitized_sha256':sha(clean)})
        ready.append((c,original,clean,observation_hashes))
    require(auth.get('items')==approved,'local_authorization_binding')
    account=local_acquisition_account(ds,documents[2],[{**c,'_local_original_sha256':sha(raw)} for c,raw,clean,obs in ready])
    accounts=ds.select('local_acquisition_account');previous=next((a for a in accounts if a['account_id']==account['account_id']),None)
    require(not any(set(a['receipt_ids']) & set(account['receipt_ids']) for a in accounts if a['account_id']!=account['account_id']),'local_account_overlap')
    require(not previous or previous==account,'local_account_mismatch')
    reservations=ds.select('request');responses={x['request_id']:x for x in ds.select('response')}
    new_accounts=accounts if previous else [*accounts,account]
    require(sum(x['source']=='commons' for x in reservations)+sum(a['request_debit'] for a in new_accounts)<=ds.config['limits']['requests'],'request_budget')
    media=sum(responses.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'])
    hour=sum(responses.get(x['request_id'],{}).get('received',x['reserved']) for x in reservations if x['media'] and x['epoch']>time.time()-3600)
    require(media+sum(a['media_debit'] for a in new_accounts)<=ds.config['limits']['media_bytes'],'media_budget')
    require(hour+sum(b['bytes'] for a in new_accounts for b in a['media_buckets'] if b['epoch']>time.time()-3600)<=ds.config['limits']['hour_bytes'],'hour_budget')
    intentions=ds.select('intention')
    for c,raw,clean,obs in ready:
        intents=[x for x in intentions if x['candidate_id']==c['candidate_id']]
        require(not intents or all(x.get('job_sha256')==job_hash for x in intents),'local_reservation_conflict')
        recv=[x for x in ds.select('received') if x['candidate_id']==c['candidate_id']]
        require(not recv or recv==[{'candidate_id':c['candidate_id'],
                'part_path':'parts/local-'+c['candidate_id']+'-'+job_hash+'.part',
                'original_sha256':sha(raw),'mode':'local_import','job_sha256':job_hash}],'local_received_conflict')
        for cls in c['class_ids']:
            count={x['candidate_id'] for x in intentions if x['source']==c['source'] and cls in x['class_ids']}
            count.update(r['candidate_id'] for r,_,_,_ in ready if cls in r['class_ids'])
            require(len(count)<=ds.config['limits']['transfers'],'transfer_budget')
        require(not c.get('local_import') or c['original_sha256']==sha(raw) and c['sanitized_sha256']==sha(clean),'local_existing_pair')
    planned={}
    for old,raw,clean,observations in ready:
        c=reviewed[old['candidate_id']]
        if old.get('local_import'):
            planned[c['candidate_id']]=old;continue
        original='originals/'+sha(raw)
        sanitized='quarantine/'+sha(clean)+('.jpg' if c['mime']=='image/jpeg' else '.png')
        rec={**c,'original_sha256':sha(raw),'original_path':original,'sanitized_sha256':sha(clean),'sanitized_path':sanitized,
             'state':'needs_human_review','reasons':['local_import_pending_human_gates'],'technical':technical(clean),
             'pairs':[],'resolved_url':None,'config_sha256':ds.config_hash,'manifest_sha256':ds.config['manifest_sha256'],
             'code_sha256':ds.config['code_sha256'],'local_import':{'job_sha256':job_hash,'mode':'local_import',
             'runtime_code_sha256':fingerprint(),'authorization_sha256':sha(auth_raw),'account_id':account['account_id'],
             'notices_path':'evidence/'+job['notices']['sha256']+'.local','observation_evidence_sha256':observations,
             'changes':'Existing final color-managed sRGB copy with metadata removed before import; original restricted; no pixel change or re-encoding during local import; source notices retained'}}
        rec.pop('decision',None)
        planned[c['candidate_id']]=rec
    # Detect immutable collisions and unsafe orphan destinations before any event.
    targets={'evidence/'+sha(document)+'.local':document for document in [job_raw,*documents]}
    for c,d,proof,same in prepared:
        targets['evidence/'+sha(proof)+'.rights']=proof
        targets['evidence/'+sha(rights_raw)+'.rights.json']=rights_raw
    for c,raw,clean,obs in ready:
        targets['parts/local-'+c['candidate_id']+'-'+job_hash+'.part']=raw
        targets['originals/'+sha(raw)]=raw
        targets['quarantine/'+sha(clean)+('.jpg' if c['mime']=='image/jpeg' else '.png')]=clean
    for relative,content in targets.items():
        destination=ds.path(relative)
        require(stat.S_IMODE(destination.parent.stat().st_mode)==0o700,'local_permissions')
        if destination.exists():
            require(stat.S_IMODE(destination.stat().st_mode)==0o600,'local_permissions')
            require(read(destination)==content,'immutable_hash_mismatch')
    # Budget only missing objects and remaining events. Checkpoints already
    # persisted by this job consume storage but must not be reserved a second time.
    future=[]
    if not any(x['job_sha256']==job_hash for x in ds.select('local_import_plan')):
        future.append(('local_import_plan',{'job_sha256':job_hash,'candidate_ids':ids,'authorization_sha256':sha(auth_raw)}))
    transition={'from':ds.config['code_sha256'],'to':fingerprint(),'reason':'rights_review_and_targeted_resume'}
    if transition['from']!=transition['to'] and transition not in ds.select('code_compatibility'):
        future.append(('code_compatibility',transition))
    known_evidence={e['path'] for e in ds.select('evidence')}
    for relative,content in targets.items():
        if relative.startswith('evidence/') and relative not in known_evidence:
            future.append(('evidence',{'path':relative,'sha256':sha(content)}));known_evidence.add(relative)
    for c,d,proof,same in prepared:
        if not same:future.append(('rights_review',reviewed[c['candidate_id']]))
    if not previous:future.append(('local_acquisition_account',account))
    for c,raw,clean,obs in ready:
        if c.get('local_import'):continue
        cid=c['candidate_id']
        if not any(x['candidate_id']==cid for x in intentions):
            future.append(('intention',{'candidate_id':cid,'source':'commons','class_ids':c['class_ids'],
                           'attempt':1,'mode':'local_import','job_sha256':job_hash}))
        if not any(x['candidate_id']==cid for x in ds.select('received')):
            future.append(('received',{'candidate_id':cid,'part_path':'parts/local-'+cid+'-'+job_hash+'.part',
                           'original_sha256':sha(raw),'mode':'local_import','job_sha256':job_hash}))
        future.append(('committed',planned[cid]))
    journal_growth=sum(len(encode({'seq':len(ds.events)+i,'timestamp':now(),'event_id':'0'*32,
        'prev_event_hash':'0'*64,'event_hash':'0'*64,'config_sha256':ds.config_hash,'type':kind,'data':data}))
        for i,(kind,data) in enumerate(future,1))
    projected={**records,**planned};intermediate={**records,**reviewed}
    projection_growth=0
    for name,variants in [('records.json',[encode(list(v.values())) for v in [intermediate,projected]]),
                          ('summary.json',[encode(ds.summary(list(v.values()))) for v in [intermediate,projected]])]:
        current=ds.path(name).stat().st_size if ds.path(name).exists() else 0
        projection_growth+=max([current,*map(len,variants)])-current
    used=sum(p.stat().st_size for p in ds.root.rglob('*') if p.is_file())
    missing=sum(len(content) for relative,content in targets.items() if not ds.path(relative).exists())
    require(used+missing+journal_growth+projection_growth+(2048 if future else 0)<=ds.config['limits']['storage_bytes'],'storage_budget')
    # All checks above are read-only. Preserve the exact plan before side effects.
    if not any(x['job_sha256']==job_hash for x in ds.select('local_import_plan')):
        ds.append('local_import_plan',{'job_sha256':job_hash,'candidate_ids':ids,'authorization_sha256':sha(auth_raw)})
    crash('plan');ds.record_compatibility()
    for document in [job_raw,*documents]:
        path='evidence/'+sha(document)+'.local';persist(ds.path(path),document,True)
        if not any(e['path']==path for e in ds.select('evidence')):ds.append('evidence',{'path':path,'sha256':sha(document)})
    crash('evidence');apply_rights_review(ds,rights_raw,prepared);crash('rights_review')
    if not previous:ds.append('local_acquisition_account',account)
    crash('account');result=[]
    for old,raw,clean,observations in ready:
        c=ds.record(old);cid=c['candidate_id']
        if c.get('local_import'):
            result.append(c);continue
        intents=[x for x in ds.select('intention') if x['candidate_id']==cid]
        require(not intents or all(x.get('job_sha256')==job_hash for x in intents),'local_reservation_conflict')
        if not intents:ds.append('intention',{'candidate_id':cid,'source':'commons','class_ids':c['class_ids'],
                                            'attempt':1,'mode':'local_import','job_sha256':job_hash})
        crash('intention');part='parts/local-'+cid+'-'+job_hash+'.part';persist(ds.path(part),raw,True)
        received={'candidate_id':cid,'part_path':part,'original_sha256':sha(raw),'mode':'local_import','job_sha256':job_hash}
        old_received=[x for x in ds.select('received') if x['candidate_id']==cid]
        require(not old_received or old_received==[received],'local_received_conflict')
        if not old_received:ds.append('received',received)
        crash('received');original='originals/'+sha(raw);persist(ds.path(original),raw,True);crash('original')
        suffix='.jpg' if c['mime']=='image/jpeg' else '.png';sanitized='quarantine/'+sha(clean)+suffix
        persist(ds.path(sanitized),clean,True);crash('sanitized')
        rec=planned[cid]
        rec.pop('decision',None);ds.append('committed',rec);result.append(rec);crash('committed')
    ds.project();crash('projected');return result


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
    local=sub.add_parser('import-local');local.add_argument('--output',required=True);local.add_argument('--job',required=True)
    args=parser.parse_args(argv)
    try:
        config=load(read(args.config if args.command=='acquire' else Path(args.output)/'config.json'))
        if args.command=='import-local':
            require(Path(args.output).is_dir() and (Path(args.output)/'journal.jsonl').is_file() and
                    (Path(args.output)/'journal.jsonl').stat().st_size>0,'local_existing_dataset')
        with Dataset(args.output,config,offline=bool(getattr(args,'offline_fixture',None)),
                     defer_compatibility=args.command=='import-local') as ds:
            if args.command=='acquire':code=acquire(ds,load(read(args.offline_fixture)) if args.offline_fixture else None)
            elif args.command=='inspect':inspect(ds,args.p07_source);code=0
            elif args.command=='finalize':finalize(ds,args.decisions);code=0
            elif args.command=='import-local':import_local_pairs(ds,args.job);code=0
            else:code=verify(ds,args.p07_source,args.acceptance)
        print(json.dumps({'command':args.command,'status':'passed' if code==0 else 'source_blocked'}));return code
    except (OSError,ValueError,KeyError,TypeError):
        print('p08_invalid_config_schema_hash_or_io',file=sys.stderr);return 2
    except KeyboardInterrupt:
        print('p08_cancelled_replay_required',file=sys.stderr);return 1

if __name__=='__main__':raise SystemExit(main())
