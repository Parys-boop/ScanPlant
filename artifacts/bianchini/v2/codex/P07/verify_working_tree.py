"""P07 evidence for uncommitted working bytes, never a review_guard proof.

Run with the existing Pillow 12.3.0 interpreter. --external verifies and reruns
already persisted drafts without changing their bytes; never accepts proposals.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from itertools import combinations
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / 'scripts/phase1'))
import curate_p07 as c

BASE = '822954421019ad611d4d14dc5461cc7a495b7db4'
SOURCE = Path('/home/administradorarthur/datasets/scanplant/p06-recovery-20260928')
OUTPUT = SOURCE.parent / 'p07-curation-20260928'
BM = '/home/administradorarthur/.agents/skills/_shared/scripts/bm.py'
EXTERNAL_INITIAL = {
    'analysis.json': '6f857cb52ad60fc596834698dd77ffb10d830d5cf907d10479b12ed76ee56338',
    'curation.draft.json': '7b27bb37bf62b5a100407948154cec0a3a2c88214396c134a91872180559bc0c',
    'human-decisions.json': '0d81616cd8ab79e2d8614a93b15ff7fdcc5f3e7f6f6adfa8c681afb3d697e195',
    'report.draft.md': '6e054680bbbbb17bf01e720aaec6e48024655cbbef73bada11abac9724a4ef6d',
    'source-before.json': 'eda50f599cd7e1bba996ae8e25760073903b122ff181ef38cb401804278b125c',
    'summary.draft.json': '97c73477c4f5d6eabce2fd3f4333fb7c92725466bf7e1b41c31140a825c57353',
}


def external():
    before = c.strict_load((OUTPUT / 'source-before.json').read_bytes())
    assert c.tree_hashes(SOURCE) == before
    assert all(c.sha((OUTPUT / n).read_bytes()) == h for n, h in EXTERNAL_INITIAL.items())
    a = c.strict_load((OUTPUT / 'analysis.json').read_bytes())
    d = c.strict_load((OUTPUT / 'human-decisions.json').read_bytes())
    r = c.strict_load((OUTPUT / 'curation.draft.json').read_bytes())
    assert c.curate(a, d, draft=True) == r
    assert c.report(r) == (OUTPUT / 'report.draft.md').read_bytes()
    assert c.encode(c.summary(r)) == (OUTPUT / 'summary.draft.json').read_bytes()
    assert (ROOT / 'artifacts/phase1/p07/summary.json').read_bytes() == (OUTPUT / 'summary.draft.json').read_bytes()
    assert a['source_hashes'] == before
    assert a['pairs'] == [c.compare_pair(x, y) for x, y in combinations(a['records'], 2)]
    assert len(a['pairs']) == len({p['pair_id'] for p in a['pairs']}) == 136
    assert {x['sha256'] for x in a['records']} == {h for p, h in before.items() if p.startswith('quarantine/')}
    assert [x['id'] for x in a['records']] == c.IDS
    assert d['authority'] == 'agent_proposal' and r['counts']['approved_for_dataset'] == 0
    assert all(not x['botanical']['expert_confirmation'] for x in d['decisions'])
    assert all(x['usable'] == 0 for x in c.strict_load((SOURCE / 'coverage.json').read_bytes())['classes'])
    old_hashes = c.tree_hashes(OUTPUT)
    old_mtimes = {n: (OUTPUT / n).stat().st_mtime_ns for n in old_hashes}
    # Same CLI as approved analysis, and bounded draft variant until U-701.
    commands = [
        [sys.executable, '-B', 'scripts/phase1/curate_p07.py', '--source', str(SOURCE), '--output', str(OUTPUT), '--analyze-only'],
        [sys.executable, '-B', 'scripts/phase1/curate_p07.py', '--source', str(SOURCE), '--output', str(OUTPUT), '--review-draft', '--decisions', str(OUTPUT / 'human-decisions.json')],
    ]
    runs = []
    for command in commands:
        run = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=120)
        assert run.returncode == 0, (command, run.stderr)
        runs.append({'argv': command, 'exit_code': run.returncode, 'stdout': run.stdout.strip()})
    assert old_hashes == c.tree_hashes(OUTPUT)
    assert old_mtimes == {n: (OUTPUT / n).stat().st_mtime_ns for n in old_hashes}
    after = c.tree_hashes(SOURCE)
    assert before == after and len(after) == 29
    result = {
        'source_files_unchanged': 29, 'images_unchanged': 17,
        'images': [{'id': x['id'], 'sha256_before': before[x['stored_path']],
                    'sha256_after': after[x['stored_path']]} for x in a['records']],
        'comparison_count': 136, 'minimum_hamming': min(p['hamming_distance'] for p in a['pairs']),
        'automatic_duplicate_signals': sum(p['signal'] != 'no_algorithmic_signal' for p in a['pairs']),
        'visual_pairs': [{'pair_id': p['pair_id'], 'hamming_distance': p['hamming_distance']}
                         for p in a['pairs'] if p['pair_id'] in {'Q01-Q02', 'Q14-Q15'}],
        'counts': r['counts'], 'human_acceptance': 'pending', 'usable': 0,
        'idempotence': {'bytes_equal': True, 'mtimes_equal': True, 'commands': runs},
        'external_artifacts': EXTERNAL_INITIAL,
    }
    # Idempotent evidence write, no source mutation or backups.
    c.persist(OUTPUT, {'verification.json': c.encode(result)})
    print(json.dumps({'external': 'passed', 'images': 17, 'pairs': 136, 'idempotence': 'bytes_and_mtimes_equal'}))


def gates():
    commands = [
        ('p07_tests', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_curate_p07.py']),
        ('affected_and_historical_tests', [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'scripts/phase1', '-p', 'test_*.py']),
        ('class_manifest', [sys.executable, '-B', 'scripts/phase1/validate_offline_manifest.py', '--manifest', 'docs/phase1/offline-class-manifest.v1.json', '--roster', 'artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json']),
        ('summary_json', [sys.executable, '-B', '-m', 'json.tool', 'artifacts/phase1/p07/summary.json']),
        ('state', ['python3', '-B', BM, 'validate-state', 'docs/living/PROJECT_STATE.md']),
        ('planning_snapshot', ['python3', '-B', BM, 'snapshot', 'verify', 'docs/living/PROJECT_STATE.md', '--root', '.']),
        ('strict_planning_audit', ['python3', '-B', BM, 'planning-audit', 'docs/living/PROJECT_STATE.md', '--root', '.', '--strict']),
        ('historical_checksums', ['sha256sum', '-c', '--strict', 'artifacts/bianchini/v2/evidence/P05-f1-man01/SHA256SUMS']),
        ('repo_hygiene', ['python3', '-B', BM, 'repo-hygiene', 'check', '--repo', '.']),
        ('workspace', ['python3', '-B', BM, 'workspace', 'check', '--repo', '.']),
        ('diff_check', ['git', 'diff', '--check']),
        ('p06_checksums', ['sha256sum', '-c', '--strict', str(SOURCE / 'SHA256SUMS')]),
    ]
    results = []
    for name, argv in commands:
        cwd = SOURCE if name == 'p06_checksums' else ROOT
        start = datetime.now(timezone.utc).isoformat()
        run = subprocess.run(argv, cwd=cwd, capture_output=True, text=True, timeout=180)
        results.append({'gate': name, 'argv': argv, 'cwd': str(cwd), 'started_at': start,
                        'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
        print(name, run.returncode, flush=True)
    evidence = {'schema_version': 1, 'evidence_kind': 'uncommitted_working_tree_not_guard_proof',
                'base_revision': BASE, 'implementation_sha256': c.sha((ROOT / 'scripts/phase1/curate_p07.py').read_bytes()),
                'tests_sha256': c.sha((ROOT / 'scripts/phase1/test_curate_p07.py').read_bytes()),
                'commands': results, 'human_acceptance': 'pending', 'guard_proofs': 'not_run_no_commit_or_new_worktree_authorized'}
    target = ROOT / 'artifacts/bianchini/v2/codex/P07/verification.json'
    assert not target.exists(), 'Preserve prior evidence; diagnose before rerunning gates.'
    target.write_bytes(c.encode(evidence))
    assert all(x['exit_code'] == 0 for x in results), 'gate_failed'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--external', action='store_true')
    parser.add_argument('--gates', action='store_true')
    args = parser.parse_args()
    assert args.external != args.gates, 'Choose exactly one operation'
    external() if args.external else gates()
