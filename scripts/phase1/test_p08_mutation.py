"""Selective P08 mutations: five material seams, no global mutation score.

Each focal baseline and mutant runs in a fresh subprocess against a disposable
source copy. unittest.mock replaces the real public boundary. A shadow call to
the unchanged boundary confirms the harmful input actually changes behavior;
mock invocation alone is insufficient. No subprocess may use the network.
"""
from contextlib import ExitStack
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
SEAMS = {
    "bypass_license": ("rights", "test_rights_gate"),
    "bypass_expert": ("decide", "test_expert_gate"),
    "ignore_hash_mismatch": ("verify_objects", "test_hash_mismatch"),
    "advance_cursor_before_commit": ("advance", "test_cursor_gate"),
    "allow_private_export": ("validate_public", "test_private_export"),
}
COPY_FILES = tuple("scripts/phase1/" + name for name in (
    "recover_p08.py", "test_recover_p08.py", "inaturalist_source.py",
    "acquire_commons.py", "curate_p07.py", "validate_offline_manifest.py",
)) + (
    "docs/phase1/offline-class-manifest.v1.json",
    "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json",
)


def worker(seam, mode, source):
    """Return a failing test exit for a killed mutant, never a forged failure."""
    sys.path.insert(0, str(Path(source)/"scripts/phase1"))
    import recover_p08 as recovery
    import test_recover_p08 as contract
    attribute, focal = SEAMS[seam]
    owner = recovery.Dataset if attribute in {"verify_objects", "advance"} else recovery
    original = getattr(owner, attribute)
    changed = 0

    def replacement(*args, **kwargs):
        nonlocal changed
        if attribute in {"rights", "decide"}:
            forced = "passed" if attribute == "rights" else "approved_for_dataset"
            try:
                observed = original(*args, **kwargs)
            except recovery.RecoveryError:
                observed = "rejected_by_original"
            changed += int(observed != forced)
            return forced
        try:
            original(*args, **kwargs)
        except recovery.RecoveryError as error:
            # Only the specified risk branch is bypassed. Unexpected errors
            # must not make a mutant look material or killed for this seam.
            expected = {"verify_objects": {"object_hash_mismatch", "evidence_hash_mismatch"},
                        "advance": {"cursor_before_commit"},
                        "validate_public": {"private_export"}}[attribute]
            if str(error) not in expected:
                raise
            changed += 1
            if attribute == "advance":
                dataset, page = args
                dataset.append("cursor", {"page_id": page["page_id"], "next_cursor": page["next_cursor"]})
            # Observable no-op validation; the original rejection is suppressed.
        return None

    with ExitStack() as stack:
        denied = []
        for boundary in ("socket.create_connection", "socket.getaddrinfo", "socket.socket.connect", "socket.socket.connect_ex"):
            denied.append(stack.enter_context(patch(boundary, side_effect=AssertionError("mutation_network_forbidden"))))
        mocked = None
        if mode == "mutant":
            mocked = stack.enter_context(patch.object(owner, attribute, autospec=True, side_effect=replacement))
        suite = unittest.TestSuite([contract.RecoveryTests(focal)])
        result = unittest.TextTestRunner(stream=sys.stderr, verbosity=1).run(suite)
        report = {"seam": seam, "mode": mode, "tests_run": result.testsRun,
                  "failures": len(result.failures), "errors": len(result.errors),
                  "mock_calls": mocked.call_count if mocked is not None else 0,
                  "material_changes_reached": changed, "network_calls": sum(x.call_count for x in denied),
                  "source_sha256": hashlib.sha256(Path(recovery.__file__).read_bytes()).hexdigest(),
                  "tests_sha256": hashlib.sha256(Path(contract.__file__).read_bytes()).hexdigest()}
    print(json.dumps(report, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


class SelectiveMutationTests(unittest.TestCase):
    def check_seam(self, seam):
        with tempfile.TemporaryDirectory(prefix="p08-selective-") as temporary:
            copied = Path(temporary)/"source"
            for relative in COPY_FILES:
                target = copied/relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT/relative, target)
            reports = []
            for mode in ("baseline", "mutant"):
                process = subprocess.run(
                    [sys.executable, "-B", str(Path(__file__).resolve()), "--worker", seam, mode, str(copied)],
                    cwd=temporary, capture_output=True, text=True, timeout=45,
                )
                self.assertIn(process.returncode, (0, 1), process.stderr)
                report = json.loads(process.stdout)
                self.assertEqual(report["tests_run"], 1, process.stderr)
                self.assertEqual(report["errors"], 0, process.stderr)
                self.assertEqual(report["network_calls"], 0, process.stderr)
                if mode == "baseline":
                    self.assertEqual(process.returncode, 0, process.stderr)
                    self.assertEqual(report["failures"], 0)
                else:
                    self.assertEqual(process.returncode, 1, "material mutant survived")
                    self.assertGreater(report["failures"], 0, process.stderr)
                    self.assertGreater(report["mock_calls"], 0, "mutated boundary was never called")
                    self.assertGreater(report["material_changes_reached"], 0, "mutation never changed the approved risk branch")
                reports.append(report)
            self.assertEqual(reports[0]["source_sha256"], reports[1]["source_sha256"])
            self.assertEqual(reports[0]["tests_sha256"], reports[1]["tests_sha256"])
            print(json.dumps({"selective_mutation": seam, "baseline": reports[0], "mutant": reports[1]}, sort_keys=True))
        self.assertFalse(copied.exists(), "disposable mutation copy was not removed")

    def test_bypass_license(self):
        self.check_seam("bypass_license")

    def test_bypass_expert(self):
        self.check_seam("bypass_expert")

    def test_ignore_hash_mismatch(self):
        self.check_seam("ignore_hash_mismatch")

    def test_advance_cursor_before_commit(self):
        self.check_seam("advance_cursor_before_commit")

    def test_allow_private_export(self):
        self.check_seam("allow_private_export")


if __name__ == "__main__":
    if len(sys.argv) == 5 and sys.argv[1] == "--worker":
        raise SystemExit(worker(sys.argv[2], sys.argv[3], sys.argv[4]))
    unittest.main()
