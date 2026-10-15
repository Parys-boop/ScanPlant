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




class RightsResumeTests(DatasetCase, unittest.TestCase):
    """Synthetic human evidence; never opens the real P08 dataset."""

    def prepare(self, count=2):
        raw=image_bytes();records=[]
        with self.open() as ds:
            for i in range(count):
                c=candidate(raw);c['media_id']=str(900+i);c['database_rights']='pending'
                c['license_url']='https://creativecommons.org/licenses/by/4.0'
                records.append(ds.ingest(c,lambda _:self.fail('rights must precede media')))
            for cls in r.canonical():
                for source in r.SOURCES:
                    ds.append('source_status',{'source':source,'class_id':cls['class_id'],'status':'budget_reached' if cls['kind']=='species' else 'protection_not_queried'})
            ds.project()
        return raw,records

    def review(self, records):
        folder=Path(self.tmp.name)/'human';folder.mkdir(exist_ok=True)
        evidence=b'Synthetic rights holder and source-rights evidence; not a real approval.\n'
        (folder/'evidence.txt').write_bytes(evidence)
        decisions=[]
        for c in records:
            decisions.append({'candidate_id':c['candidate_id'],'record_digest':r.review_digest(c),
                'subject_digest':r.rights_subject_digest(c),'source_evidence_sha256':c['evidence_sha256'],
                'authority':'human','reviewer':'Synthetic responsible','reviewed_at':'2026-10-14T12:00:00Z',
                'rationale':'Synthetic documented individual grant and source/database clearance.',
                'decision':'approved_for_transfer','individual_rights':'passed','database_rights':'passed',
                'evidence':{'path':'evidence.txt','sha256':r.sha(evidence)}})
        data={'schema_version':1,'authority':'human','scope':'commons_candidate_rights',
              'config_sha256':r.sha(r.encode(self.config)),'decisions':decisions}
        file=folder/'review.json';file.write_bytes(r.encode(data));return file,data

    def test_exact_url_equivalences_keep_independent_gates(self):
        for code,name,url in [('cc0','CC0','http://creativecommons.org/publicdomain/zero/1.0/deed.en'),
                              ('cc-by-4.0','CC BY 4.0','https://creativecommons.org/licenses/by/4.0')]:
            c=candidate();c.update(license_id=code,license_name=name,license_url=url)
            before=copy.deepcopy(c)
            self.assertEqual(r.rights(c),'passed')
            self.assertEqual(c,before)
            for key,value in [('database_rights','pending'),('rights_consistent',False),('author',''),('restrictions','restriction')]:
                with self.subTest(code=code,key=key):self.assertNotEqual(r.rights({**c,key:value}),'passed')

    def test_url_variants_not_proven_are_rejected(self):
        for url in ['https://creativecommons.org.evil/licenses/by/4.0/',
                    'https://creativecommons.org/licenses/by/4.0/?x=1',
                    'https://creativecommons.org/licenses/by/3.0/',
                    'https://creativecommons.org/licenses/by-sa/4.0/',
                    'http://creativecommons.org/licenses/by/4.0',
                    'https://creativecommons.org/licenses/by/4.0/deed.fr',
                    'https://creativecommons.org/licenses/by/4.0/#x']:
            self.assertNotEqual(r.rights({**candidate(),'license_url':url}),'passed')

    def test_explicit_resume_after_review_no_discovery_or_duplicates(self):
        raw,records=self.prepare(3);file,_=self.review(records[:2]);ids=[x['candidate_id'] for x in records[:2]]
        config=(self.root/'config.json').read_bytes();prefix=(self.root/'journal.jsonl').read_bytes()
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            self.assertFalse(ds.select('intention'))
            with patch.object(r.Transport,'get',side_effect=AssertionError('discovery_or_network_forbidden')):
                calls=[];r.resume_candidates(ds,ids,download=lambda c:(calls.append(c['candidate_id']) or raw))
            self.assertEqual(calls,ids)
            self.assertEqual(len(ds.records()),3)
            self.assertEqual(len(ds.select('intention')),2)
            self.assertEqual(len(ds.select('committed')),2)
            self.assertEqual(ds.records()[2]['state'],'needs_license_review')
            self.assertTrue(all(x['state']!='approved_for_dataset' for x in ds.records()))
            self.assertEqual(ds.summary()['usable'],0)
            stable=r.tree_fingerprint(self.root)
            r.incorporate_rights_review(ds,file)
            r.resume_candidates(ds,ids,download=lambda _:self.fail('duplicate transfer'))
            self.assertEqual(stable,r.tree_fingerprint(self.root))
        self.assertEqual(config,(self.root/'config.json').read_bytes())
        self.assertTrue((self.root/'journal.jsonl').read_bytes().startswith(prefix))
        with self.open() as ds:
            before=r.tree_fingerprint(self.root)
            r.resume_candidates(ds,ids,download=lambda _:self.fail('restart transfer'))
            self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_review_rejects_forgery_staleness_and_wrong_scope_atomically(self):
        _,records=self.prepare();file,good=self.review(records)
        cases=[('authority','agent'),('scope','dataset_approval'),('config_sha256','0'*64)]
        for key,value in cases:
            bad=copy.deepcopy(good);bad[key]=value;file.write_bytes(r.encode(bad))
            with self.open() as ds:
                before=r.tree_fingerprint(self.root)
                with self.assertRaises(r.RecoveryError):r.incorporate_rights_review(ds,file)
                self.assertEqual(before,r.tree_fingerprint(self.root))
        for key,value in [('record_digest','0'*64),('subject_digest','0'*64),('source_evidence_sha256','0'*64),
                          ('reviewer',''),('authority','agent'),('reviewed_at','invalid'),('rationale',''),
                          ('candidate_id','Cunknown')]:
            bad=copy.deepcopy(good);bad['decisions'][1][key]=value;file.write_bytes(r.encode(bad))
            with self.open() as ds:
                before=r.tree_fingerprint(self.root)
                with self.assertRaises(r.RecoveryError):r.incorporate_rights_review(ds,file)
                self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_missing_or_changed_evidence_blocks_before_transfer(self):
        _,records=self.prepare();file,data=self.review(records)
        (file.parent/'evidence.txt').write_bytes(b'changed')
        with self.open() as ds:
            before=r.tree_fingerprint(self.root)
            with self.assertRaises(r.RecoveryError):r.incorporate_rights_review(ds,file)
            self.assertEqual(before,r.tree_fingerprint(self.root))
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[records[0]['candidate_id']],download=lambda _:self.fail('no review'))

    def test_pending_review_and_no_own_work_do_not_release_rights(self):
        _,records=self.prepare();file,data=self.review(records)
        data['decisions'][0]['decision']='pending';data['decisions'][0]['individual_rights']='pending'
        file.write_bytes(r.encode(data))
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[records[0]['candidate_id']],download=lambda _:self.fail('pending'))
            c=next(x for x in ds.records() if x['candidate_id']==records[1]['candidate_id'])
            self.assertEqual(c['database_rights'],'pending')
            self.assertEqual(r.rights(c),'passed')
            self.assertNotEqual(r.rights({**c,'rights_consistent':False}),'passed')
            self.assertNotEqual(r.rights({**c,'author':''}),'passed')
            self.assertNotEqual(r.rights({**c,'license_id':'cc-by-sa-4.0'}),'passed')

    def test_quota_unknown_ids_and_non_offline_callback_are_not_bypassed(self):
        raw,records=self.prepare();file,_=self.review(records)
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            for i in range(ds.config['limits']['transfers']):
                ds.append('intention',{'candidate_id':'Csynthetic'+str(i),'source':'commons','class_ids':['species_01'],'attempt':1})
            before=r.tree_fingerprint(self.root)
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[records[0]['candidate_id'],'Cunknown'],download=lambda _:self.fail('unknown'))
            self.assertEqual(before,r.tree_fingerprint(self.root))
            r.resume_candidates(ds,[records[0]['candidate_id']],download=lambda _:self.fail('quota'))
            self.assertEqual(len(ds.select('intention')),20)
            self.assertEqual(ds.record(records[0])['state'],'deferred_budget')
            ds.offline=False
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[records[1]['candidate_id']],download=lambda _:raw)

    def test_changed_subject_invalidates_clearance(self):
        _,records=self.prepare();file,_=self.review(records)
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            c=ds.record(records[0]);c['source_sha1']='0'*40;ds.append('classified',c)
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[c['candidate_id']],download=lambda _:self.fail('stale review'))
            self.assertNotEqual(r.rights(c),'passed')

    def test_new_evidence_invalidates_prior_decisions_and_reports(self):
        _,records=self.prepare();file,_=self.review(records)
        with self.open() as ds:
            before_digest=r.review_digest(ds.record(records[0]));r.incorporate_rights_review(ds,file)
            c=ds.record(records[0]);self.assertNotEqual(before_digest,r.review_digest(c))
            self.assertNotIn('decision',c)
            self.assertEqual(c['license_url'],records[0]['license_url'])
            self.assertEqual(c['evidence_sha256'],records[0]['evidence_sha256'])

    def test_imported_evidence_cannot_change_before_resume(self):
        _,records=self.prepare();file,_=self.review(records)
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            c=ds.record(records[0]);proof=ds.path(c['rights_review']['imported_evidence_path'])
            proof.write_bytes(b'corrupted')
            before=(self.root/'journal.jsonl').read_bytes()
            with self.assertRaises(r.RecoveryError):r.resume_candidates(ds,[c['candidate_id']],download=lambda _:self.fail('corrupt evidence'))
            self.assertEqual(before,(self.root/'journal.jsonl').read_bytes())

    def test_format_gate_remains_after_human_rights_review(self):
        raw,records=self.prepare(1)
        with self.open() as ds:
            c=ds.record(records[0]);c['mime']='image/webp';ds.append('classified',c);ds.project()
        file,_=self.review([c])
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            r.resume_candidates(ds,[c['candidate_id']],download=lambda _:self.fail('unsupported format'))
            self.assertEqual(ds.record(c)['state'],'rejected_format')
            self.assertFalse(ds.select('intention'))

    def test_partial_import_crash_replays_without_duplicate_reviews(self):
        _,records=self.prepare();file,_=self.review(records)
        with self.open() as ds:
            append=ds.append;seen=0
            def crash(kind,data):
                nonlocal seen
                event=append(kind,data)
                if kind=='rights_review':
                    seen+=1
                    if seen==1:raise RuntimeError('synthetic_crash')
                return event
            with patch.object(ds,'append',side_effect=crash):
                with self.assertRaisesRegex(RuntimeError,'synthetic_crash'):r.incorporate_rights_review(ds,file)
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            self.assertEqual(len(ds.select('rights_review')),2)
            self.assertEqual(len(ds.records()),2)
            before=r.tree_fingerprint(self.root);r.incorporate_rights_review(ds,file)
            self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_b1_code_predecessor_preserves_original_configuration(self):
        self.config['code_sha256']['recover_p08.py']=r.RIGHTS_REVIEW_PREDECESSOR
        with self.open() as ds:
            self.assertEqual(ds.events[0]['data'],self.config)
            self.assertEqual(ds.select('code_compatibility')[0]['reason'],'rights_review_and_targeted_resume')
        before=r.tree_fingerprint(self.root)
        with self.open():pass
        self.assertEqual(before,r.tree_fingerprint(self.root))

    def test_received_bytes_resume_without_another_reservation_or_download(self):
        raw,records=self.prepare(1);file,_=self.review(records);ids=[records[0]['candidate_id']]
        with self.open() as ds:
            r.incorporate_rights_review(ds,file)
            with patch.object(r,'sanitize',side_effect=RuntimeError('synthetic_crash_after_original')):
                with self.assertRaisesRegex(RuntimeError,'synthetic_crash_after_original'):
                    r.resume_candidates(ds,ids,download=lambda _:raw)
            self.assertEqual(len(ds.select('intention')),1)
            self.assertEqual(len(ds.select('received')),1)
        with self.open() as ds:
            r.resume_candidates(ds,ids,download=lambda _:self.fail('repeat media'))
            self.assertEqual(len(ds.select('intention')),1)
            self.assertEqual(len(ds.select('committed')),1)

    def test_evidence_path_escape_and_duplicate_ids_are_atomic(self):
        _,records=self.prepare();file,good=self.review(records)
        for change in ['path','ids','incomplete']:
            data=copy.deepcopy(good)
            if change=='path':data['decisions'][1]['evidence']['path']='../escape'
            elif change=='ids':data['decisions'][1]['candidate_id']=data['decisions'][0]['candidate_id']
            else:data['decisions'][1]['database_rights']='pending'
            file.write_bytes(r.encode(data))
            with self.open() as ds:
                before=r.tree_fingerprint(self.root)
                with self.assertRaises(r.RecoveryError):r.incorporate_rights_review(ds,file)
                self.assertEqual(before,r.tree_fingerprint(self.root))


if __name__ == '__main__':
    unittest.main()
