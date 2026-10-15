"""Isolated local-pair import boundaries; all people and assets are synthetic."""
import copy
from contextlib import ExitStack
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from PIL import Image
import recover_p08 as r
from test_recover_p08 import DatasetCase, candidate, image_bytes
import test_recover_p08 as contract


ORIGINAL_TRANSPORT_GET = r.Transport.get


class LocalImportTests(DatasetCase, unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.net = ExitStack()
        self.addCleanup(self.net.close)
        for target in ['Transport.get', 'PinnedHTTPS']:
            owner, name = target.split('.') if '.' in target else (None, target)
            self.net.enter_context(patch.object(getattr(r, owner) if owner else r, name,
                                               side_effect=AssertionError('network forbidden')))
        self.asset_root = Path(self.tmp.name)/'assets'
        self.asset_root.mkdir(mode=0o700)
        self.job_dir = Path(self.tmp.name)/'job'
        self.job_dir.mkdir(mode=0o700)
        self.job_file = self.job_dir/'job.json'

    def private_write(self, path, raw):
        path.write_bytes(raw)
        path.chmod(0o600)
        return {'path':str(path.relative_to(self.job_dir)), 'sha256':r.sha(raw)}

    def reference(self, name, value):
        return self.private_write(self.job_dir/name, r.encode(value) if not isinstance(value, bytes) else value)

    def save_job(self):
        self.private_write(self.job_file, r.encode(self.job))

    def update_ref(self, field, change):
        ref=self.job[field]
        path=self.job_dir/ref['path']
        data=json.loads(path.read_bytes());change(data)
        ref['sha256']=r.sha(r.encode(data));self.private_write(path,r.encode(data));self.save_job()

    def prepare(self, count=2):
        self.original=image_bytes()
        self.sanitized,_=r.sanitize(self.original,'https://upload.wikimedia.org/a/fixture.jpg','image/jpeg')
        self.records=[]
        with self.open() as ds:
            for i in range(count):
                c=candidate(self.original)
                c.update(media_id=str(800+i),page_id=800+i,revision_id=1800+i,
                         declared_width=240,declared_height=240,database_rights='pending',
                         file_url=f'https://upload.wikimedia.org/wikipedia/commons/a/a0/Synthetic{i}.jpg?utm_source=fixture&utm_campaign=fixture&utm_content=fixture',
                         source_page_url=f'https://commons.wikimedia.org/wiki/File:Synthetic{i}.jpg')
                raw=r.encode({'synthetic_source_metadata':c})
                digest=r.sha(raw);path=f'evidence/{digest}.json'
                r.persist(ds.path(path),raw,True);ds.append('evidence',{'path':path,'sha256':digest})
                c['evidence_sha256']=digest
                self.records.append(ds.classify(c,'needs_license_review','database_rights_pending'))
            ds.project()
            cfg=ds.config_hash
        review_path,review=contract.RightsResumeTests.review(self,self.records)
        proof=(review_path.parent/'evidence.txt').read_bytes()
        self.reference('evidence.txt',proof)
        rights=self.reference('rights.json',review)
        items=[];authorized=[];receipts=[]
        for i,c in enumerate(self.records):
            for kind,raw in [('original',self.original),('sanitized',self.sanitized)]:
                p=self.asset_root/f'{i}-{kind}.jpg';p.write_bytes(raw);p.chmod(0o600)
            orig={'path':f'{i}-original.jpg','sha256':r.sha(self.original)}
            clean={'path':f'{i}-sanitized.jpg','sha256':r.sha(self.sanitized)}
            validation=self.reference(f'{i}-validation.json',{
                'original_sha256':orig['sha256'],'sanitized_sha256':clean['sha256'],
                'width':240,'height':240,'method':'existing_sanitized_copy'})
            observation=self.reference(f'{i}-observation.json',{
                'authority':'human','reviewer':'Synthetic reviewer','reviewed_at':'2026-10-15',
                'candidate_id':c['candidate_id'],'sanitized_sha256':clean['sha256'],
                'observations':{'sharpness':'clear','illumination':'well lit'},
                'scope':'sharpness_and_illumination_only'})
            items.append({'candidate_id':c['candidate_id'],'subject_digest':r.rights_subject_digest(c),
                          'source_evidence_sha256':c['evidence_sha256'],'original':orig,'sanitized':clean,
                          'validation':validation,'observations':[observation]})
            authorized.append({'candidate_id':c['candidate_id'],'subject_digest':r.rights_subject_digest(c),
                               'original_sha256':orig['sha256'],'sanitized_sha256':clean['sha256']})
            receipts.append({'utc':'2026-10-15T00:00:00Z','requested_url':c['file_url'].split('?')[0],
                             'status':200,'bytes':len(self.original),'sha256':orig['sha256']})
        auth=self.reference('authorization.json',{'authority':'human','scope':'p08_local_quarantine_import',
            'config_sha256':cfg,'reviewer':'Synthetic responsible','reviewed_at':'2026-10-15T12:00:00Z',
            'rationale':'Synthetic limited private quarantine authorization.', 'items':authorized})
        acquisition=self.reference('acquisition.json',{'schema_version':1,'source':'commons',
                                                       'receipts':receipts,'unreceipted_metadata':[]})
        notices=self.reference('notices.txt',b'Synthetic photo: CC BY 4.0; author Synthetic fixture.\nPage text: CC BY-SA; metadata CC0.\n')
        self.job={'schema_version':1,'scope':'p08_local_quarantine_import','config_sha256':cfg,
                  'asset_root':str(self.asset_root),'authorization':auth,'rights_review':rights,
                  'acquisition':acquisition,'notices':notices,'items':items}
        self.save_job()
        return self.job

    def run_import(self, ds, **kw):
        with patch.object(r,'sanitize',side_effect=AssertionError('existing sanitization must be preserved')):
            return r.import_local_pairs(ds,self.job_file,**kw)

    def assert_rejected_without_events(self):
        with self.open() as ds:
            before=copy.deepcopy(ds.events)
            with self.assertRaises(r.RecoveryError):self.run_import(ds)
            self.assertEqual(before,ds.events)

    def test_import_exact_pairs_no_network_or_resanitization(self):
        self.prepare()
        config=(self.root/'config.json').read_bytes();prefix=(self.root/'journal.jsonl').read_bytes()
        with self.open() as ds:
            recs=self.run_import(ds)
            self.assertEqual([c['candidate_id'] for c in recs],[c['candidate_id'] for c in self.records])
            for rec,old in zip(recs,self.records):
                self.assertEqual((self.root/rec['original_path']).read_bytes(),self.original)
                self.assertEqual((self.root/rec['sanitized_path']).read_bytes(),self.sanitized)
                for key in ['candidate_id','file_url','source_page_url','author','license_url','evidence_sha256']:
                    self.assertEqual(rec[key],old[key])
                self.assertNotEqual(rec['state'],'approved_for_dataset')
                self.assertEqual(rec['database_rights'],'pending')
            self.assertEqual(ds.summary()['usable'],0)
            self.assertEqual(len(ds.select('request')),0)
            self.assertEqual(len(ds.select('intention')),2)
            self.assertTrue(all(x.get('mode')=='local_import' for x in ds.select('intention')))
            self.assertEqual(len(ds.select('local_acquisition_account')),1)
            digest=r.sha(self.job_file.read_bytes())
            self.assertTrue(all(x['job_sha256']==digest for x in ds.select('received')))
            self.assertTrue(all(x['local_import']['job_sha256']==digest for x in ds.select('committed')))
        self.assertEqual(config,(self.root/'config.json').read_bytes())
        self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))

    def test_works_outside_fixture_offline_mode(self):
        self.prepare(1)
        with self.open() as ds:
            ds.offline=False
            self.assertEqual(len(self.run_import(ds)),1)

    def test_replay_and_idempotence(self):
        self.prepare()
        with self.open() as ds:
            self.run_import(ds);stable=r.tree_fingerprint(self.root)
            self.run_import(ds);self.assertEqual(stable,r.tree_fingerprint(self.root))
        with self.open() as ds:
            self.run_import(ds);self.assertEqual(stable,r.tree_fingerprint(self.root))
            self.assertEqual(len(ds.select('received')),2)
            self.assertEqual(len(ds.select('committed')),2)
            self.assertEqual(len(ds.select('local_acquisition_account')),1)

    def test_crash_replay_every_durable_boundary(self):
        for stage in ['plan','evidence','rights_review','account','intention','received','original','sanitized','committed','projected']:
            with self.subTest(stage=stage):
                original_tmp=self.tmp
                with tempfile.TemporaryDirectory() as td:
                    self.tmp=type('Tmp',(),{'name':td})()
                    self.root=Path(td)/'synthetic';self.asset_root=Path(td)/'assets';self.asset_root.mkdir(mode=0o700)
                    self.job_dir=Path(td)/'job';self.job_dir.mkdir(mode=0o700);self.job_file=self.job_dir/'job.json'
                    self.prepare()
                    def crash(point):
                        if point==stage:raise RuntimeError('synthetic interruption')
                    with self.open() as ds:
                        with self.assertRaises(RuntimeError):self.run_import(ds,crash=crash)
                    with self.open() as ds:
                        recs=self.run_import(ds)
                        self.assertEqual(len(recs),2)
                        self.assertEqual(len(ds.select('intention')),2)
                        self.assertEqual(len(ds.select('received')),2)
                        self.assertEqual(len(ds.select('committed')),2)
                        self.assertEqual(len(ds.select('local_acquisition_account')),1)
                        self.assertEqual(ds.summary()['usable'],0)
                self.tmp=original_tmp

    def test_low_storage_budget_replay_counts_only_missing_destinations(self):
        self.config['limits']['storage_bytes']=128*1024
        original_tmp=self.tmp
        for stage in ['received','original','sanitized']:
            with self.subTest(stage=stage),tempfile.TemporaryDirectory() as td:
                self.tmp=type('Tmp',(),{'name':td})()
                self.root=Path(td)/'synthetic'
                self.asset_root=Path(td)/'assets';self.asset_root.mkdir(mode=0o700)
                self.job_dir=Path(td)/'job';self.job_dir.mkdir(mode=0o700)
                self.job_file=self.job_dir/'job.json';self.prepare()
                def crash(point):
                    if point==stage:raise RuntimeError('synthetic interruption')
                with self.open() as ds:
                    with self.assertRaises(RuntimeError):self.run_import(ds,crash=crash)
                with self.open() as ds:
                    recs=self.run_import(ds)
                    self.assertEqual(len(recs),2)
                    self.assertEqual(len(ds.select('intention')),2)
                    self.assertEqual(len(ds.select('received')),2)
                    self.assertEqual(len(ds.select('committed')),2)
                    self.assertEqual(len(ds.select('local_acquisition_account')),1)
                    stable=r.tree_fingerprint(self.root)
                    self.run_import(ds)
                    self.assertEqual(stable,r.tree_fingerprint(self.root))
                    self.assertLessEqual(sum(p.stat().st_size for p in self.root.rglob('*') if p.is_file()),128*1024)
        self.tmp=original_tmp

    def test_late_bad_item_rejects_entire_batch(self):
        self.prepare();self.job['items'][1]['sanitized']['sha256']='0'*64;self.save_job()
        self.assert_rejected_without_events()

    def test_changed_asset_hash_rejected(self):
        self.prepare();(self.asset_root/'0-original.jpg').write_bytes(b'corrupt')
        self.assert_rejected_without_events()

    def test_non_private_file_or_root_rejected(self):
        self.prepare();(self.asset_root/'0-original.jpg').chmod(0o644)
        self.assert_rejected_without_events()
        (self.asset_root/'0-original.jpg').chmod(0o600);self.asset_root.chmod(0o755)
        self.assert_rejected_without_events()

    def test_symlink_and_path_escape_rejected(self):
        self.prepare();p=self.asset_root/'0-original.jpg';raw=p.read_bytes();p.unlink()
        target=Path(self.tmp.name)/'other.jpg';target.write_bytes(raw);target.chmod(0o600);p.symlink_to(target)
        self.assert_rejected_without_events()
        self.job['items'][0]['original']['path']='../other.jpg';self.save_job()
        self.assert_rejected_without_events()

    def test_sanitized_metadata_rejected_even_with_updated_hashes(self):
        self.prepare();self.replace_sanitized(self.original)
        self.assert_rejected_without_events()

    def replace_sanitized(self, raw):
        item=self.job['items'][0];(self.asset_root/item['sanitized']['path']).write_bytes(raw)
        item['sanitized']['sha256']=r.sha(raw)
        ref=item['validation'];path=self.job_dir/ref['path'];v=json.loads(path.read_bytes())
        v['sanitized_sha256']=r.sha(raw);self.private_write(path,r.encode(v));ref['sha256']=r.sha(r.encode(v))
        self.update_ref('authorization',lambda a:a['items'][0].update(sanitized_sha256=r.sha(raw)))
        obs=item['observations'][0];p=self.job_dir/obs['path'];v=json.loads(p.read_bytes());v['sanitized_sha256']=r.sha(raw)
        self.private_write(p,r.encode(v));obs['sha256']=r.sha(r.encode(v));self.save_job()

    def test_invalid_sanitized_format_rejected(self):
        self.prepare();self.replace_sanitized(b'not a JPEG')
        self.assert_rejected_without_events()

    def test_sanitized_wrong_dimensions_rejected(self):
        self.prepare();out=io.BytesIO();Image.new('RGB',(120,240)).save(out,format='JPEG')
        self.replace_sanitized(out.getvalue());self.assert_rejected_without_events()

    def test_changed_source_evidence_rejected(self):
        self.prepare();self.job['items'][0]['source_evidence_sha256']='0'*64;self.save_job()
        self.assert_rejected_without_events()

    def test_wrong_job_scope_rejected(self):
        self.prepare();self.job['scope']='dataset_approval';self.save_job();self.assert_rejected_without_events()

    def test_unknown_or_duplicate_ids_rejected(self):
        self.prepare();self.job['items'][1]['candidate_id']='Cunknown';self.save_job();self.assert_rejected_without_events()
        self.job['items'][1]=copy.deepcopy(self.job['items'][0]);self.save_job();self.assert_rejected_without_events()

    def test_more_than_two_items_rejected(self):
        self.prepare(3);self.assert_rejected_without_events()

    def test_forged_authority_and_wrong_authorized_hash_rejected(self):
        self.prepare();self.update_ref('authorization',lambda a:a.update(authority='agent_proposal'))
        self.assert_rejected_without_events()
        self.update_ref('authorization',lambda a:a.update(authority='human'))
        self.update_ref('authorization',lambda a:a['items'][0].update(sanitized_sha256='0'*64))
        self.assert_rejected_without_events()

    def test_observation_hash_must_bind_existing_sanitized_copy(self):
        self.prepare()
        ref=self.job['items'][0]['observations'][0];path=self.job_dir/ref['path']
        value=json.loads(path.read_bytes());value['sanitized_sha256']='0'*64
        self.private_write(path,r.encode(value));ref['sha256']=r.sha(r.encode(value));self.save_job()
        self.assert_rejected_without_events()

    def test_orphan_destination_collisions_rejected_before_any_event(self):
        self.prepare()
        paths=['originals/'+r.sha(self.original),
               'evidence/'+r.sha(self.job_file.read_bytes())+'.local']
        for name in paths:
            with self.subTest(name=name):
                path=self.root/name;path.write_bytes(b'conflicting immutable orphan');path.chmod(0o600)
                self.assert_rejected_without_events()
                self.assertEqual(path.read_bytes(),b'conflicting immutable orphan')
                path.unlink()

    def test_observation_explicit_candidate_must_match_item(self):
        self.prepare()
        ref=self.job['items'][0]['observations'][0];path=self.job_dir/ref['path']
        value=json.loads(path.read_bytes());value['candidate_id']=self.records[1]['candidate_id']
        self.private_write(path,r.encode(value));ref['sha256']=r.sha(r.encode(value));self.save_job()
        self.assert_rejected_without_events()

    def test_pending_rights_cannot_release_import(self):
        self.prepare()
        def pending(review):review['decisions'][0].update(decision='pending',individual_rights='pending')
        self.update_ref('rights_review',pending);self.assert_rejected_without_events()

    def test_missing_or_changed_referenced_evidence_rejected(self):
        self.prepare();(self.job_dir/self.job['notices']['path']).write_bytes(b'changed')
        self.assert_rejected_without_events()

    def test_transfer_quota_checked_before_any_effects(self):
        self.config['limits']['transfers']=1;self.prepare();self.assert_rejected_without_events()

    def test_media_quota_checked_before_any_effects(self):
        self.config['limits']['media_bytes']=len(image_bytes());self.prepare();self.assert_rejected_without_events()

    def test_request_quota_checked_before_any_effects(self):
        self.config['limits']['requests']=1;self.prepare();self.assert_rejected_without_events()

    def test_recent_media_receipt_respects_hour_quota_before_effects(self):
        self.config['limits']['hour_bytes']=len(image_bytes());self.prepare()
        def recent(a):
            stamp=r.now()
            for receipt in a['receipts']:receipt['utc']=stamp
        self.update_ref('acquisition',recent);self.assert_rejected_without_events()

    def test_future_transport_consumes_local_request_debit(self):
        self.config['limits']['requests']=2;self.prepare()
        with self.open() as ds:
            self.run_import(ds);ds.offline=False
            before=copy.deepcopy(ds.events)
            with self.assertRaisesRegex(r.RecoveryError,'request_budget'):
                ORIGINAL_TRANSPORT_GET(r.Transport(ds),'https://upload.wikimedia.org/a/test.jpg','commons',True)
            self.assertEqual(before,ds.events)

    def test_future_transport_consumes_local_media_debit(self):
        self.config['limits']['media_bytes']=2*len(image_bytes());self.prepare()
        with self.open() as ds:
            self.run_import(ds);ds.offline=False
            before=copy.deepcopy(ds.events)
            with self.assertRaisesRegex(r.RecoveryError,'media_budget'):
                ORIGINAL_TRANSPORT_GET(r.Transport(ds),'https://upload.wikimedia.org/a/test.jpg','commons',True)
            self.assertEqual(before,ds.events)

    def test_storage_quota_checked_before_any_effects(self):
        self.config['limits']['storage_bytes']=1;self.prepare();self.assert_rejected_without_events()

    def test_imported_file_corruption_rejected_on_reopen(self):
        self.prepare(1)
        with self.open() as ds:rec=self.run_import(ds)[0]
        (self.root/rec['sanitized_path']).write_bytes(b'corrupt')
        with self.assertRaises(r.RecoveryError):
            with self.open():pass

    def test_network_url_validator_remains_strict(self):
        self.prepare()
        with self.assertRaises(r.RecoveryError):r.safe_url(self.records[0]['file_url'],'commons',True)
        with self.open() as ds:self.assertEqual(len(self.run_import(ds)),2)

    def test_original_sha1_mismatch_rejected(self):
        self.prepare()
        with self.open() as ds:
            c=dict(self.records[0]);c['source_sha1']='0'*40;ds.append('classified',c)
        self.assert_rejected_without_events()

    def test_failed_media_receipt_debits_conservative_bound(self):
        self.prepare()
        def failed(a):
            a['receipts'].insert(0,{'utc':'2026-10-14T23:59:00Z',
                'requested_url':a['receipts'][0]['requested_url'],'status':429})
        self.update_ref('acquisition',failed)
        with self.open() as ds:
            self.run_import(ds);account=ds.select('local_acquisition_account')[0]
            self.assertEqual(account['request_debit'],3)
            self.assertEqual(account['media_debit'],2*len(self.original)+self.config['limits']['file_bytes'])
            self.run_import(ds)
            self.assertEqual(len(ds.select('local_acquisition_account')),1)

    def test_duplicate_acquisition_receipt_rejected(self):
        self.prepare()
        self.update_ref('acquisition',lambda a:a['receipts'].append(copy.deepcopy(a['receipts'][0])))
        self.assert_rejected_without_events()

    def test_successful_receipt_required_for_each_imported_original(self):
        self.prepare()
        self.update_ref('acquisition',lambda a:a['receipts'].pop())
        self.assert_rejected_without_events()

    def test_mismatched_acquisition_receipt_rejected(self):
        self.prepare();self.update_ref('acquisition',lambda a:a['receipts'][1].update(sha256='0'*64))
        self.assert_rejected_without_events()


if __name__ == '__main__':
    unittest.main()
