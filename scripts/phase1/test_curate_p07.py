"""P07 public seams; synthetic images only, no external corpus or network."""
from copy import deepcopy
from io import BytesIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from PIL import Image
import curate_p07 as c


def jpeg(value):
    out = BytesIO()
    Image.new("RGB", (24, 16), (value * 10, value * 5, value * 3)).save(out, format="JPEG")
    return out.getvalue()


def source_fixture(root):
    root.mkdir()
    (root / "quarantine").mkdir()
    (root / "review-2026-09-28").mkdir()
    classes = json.loads(c.CLASS_MANIFEST.read_text())["classes"]
    records, decisions = [], []
    for i in range(1, 18):
        raw = jpeg(i)
        digest = c.sha(raw)
        stored = f"quarantine/{digest}.jpg"
        (root / stored).write_bytes(raw)
        record = dict.fromkeys(c.RECORD_KEYS, "synthetic")
        record.update(sequence=i, result="accepted", sha256=digest, class_id="species_01",
                      stored_path=stored, botanical_validation_performed=False,
                      visual_review_performed=False)
        records.append(record)
        d = dict.fromkeys(c.P06_DECISION_KEYS, False)
        d.update(decision_id=f"Q{i:02}", review_id=f"R{i:02}", sha256=digest, class_id="species_01",
                 decision="aprovar_para_curadoria_futura", stored_path=stored, physical_location="quarantine")
        decisions.append(d)
    manifest = b"".join((json.dumps(r, sort_keys=True) + "\n").encode() for r in records)
    (root / "manifest.jsonl").write_bytes(manifest)
    canonical_sha = c.sha(c.CLASS_MANIFEST.read_bytes())
    write = lambda name, value: (root / name).write_bytes(c.encode(value))
    write("state.json", {"schema_version": 1, "records": records, "canonical_manifest_sha256": canonical_sha,
                         "searches": {x["class_id"]: {"continuation": None, "exhausted": False,
                                      "pages_fetched": 1, "status": "finished"} for x in classes}})
    cv = []
    for x in classes:
        v = dict.fromkeys("accepted class_id consulted deferred deferred_reasons failure_reasons failures name pages_fetched quarantined query reasons rejected status usable".split(), 0)
        v.update(class_id=x["class_id"], accepted=17 if x["class_id"] == "species_01" else 0,
                 quarantined=17 if x["class_id"] == "species_01" else 0)
        cv.append(v)
    coverage = dict.fromkeys("accepted_cap_per_class accepted_semantics canonical_manifest_sha256 classes failure_count_semantics manifest_jsonl_sha256 page_budget_per_class_per_run schema_version status training_ready visual_review_performed".split(), 0)
    coverage.update(canonical_manifest_sha256=canonical_sha, classes=cv, manifest_jsonl_sha256=c.sha(manifest),
                    training_ready=False)
    write("coverage.json", coverage)
    prior = dict.fromkeys("confirmation_source decisions human_grouped_decision_confirmed notice p06_status recorded_at release_status remote_metadata_requeried review_method run_id schema_version totals training_ready".split(), "fixture")
    prior.update(decisions=decisions, run_id=c.RUN, human_grouped_decision_confirmed=True, training_ready=False,
                 totals={"aprovar_para_curadoria_futura": 17})
    write("review-2026-09-28/human-decisions.json", prior)
    write("run-metadata.json", {"run_id": c.RUN, "totals": {"accepted": 17}})
    rehash(root)


def rehash(root):
    inventory = [{"path": str(p.relative_to(root)), "sha256": c.sha(p.read_bytes()), "bytes": p.stat().st_size}
                 for p in sorted(root.rglob("*")) if p.is_file() and p.name not in {"inventory.json", "SHA256SUMS"}]
    (root / "inventory.json").write_bytes(c.encode(inventory))
    lines = [f"{c.sha(p.read_bytes())}  {p.relative_to(root)}\n" for p in sorted(root.rglob("*"))
             if p.is_file() and p.name != "SHA256SUMS"]
    (root / "SHA256SUMS").write_text("".join(lines))


def decisions_for(analysis, draft=False):
    decisions = []
    for r in analysis["records"]:
        d = {k: r[k] for k in ("id", "review_id", "sha256", "class_id")}
        d.update(state="needs_botanical_review", reviewer_id="synthetic-reviewer",
                 reviewer_role="agent" if draft else "human", timestamp="2026-09-30T12:00:00+00:00",
                 rationale="Insufficient species evidence", original_resolution_review=True,
                 visual=dict.fromkeys(c.VISUAL, "Synthetic observation"),
                 privacy={**dict.fromkeys(c.PRIVACY, "not_observed"), "assessment": "Synthetic privacy review"},
                 botanical={"status": "insufficient", "evidence": "No taxonomic evidence", "expert_confirmation": False},
                 gates=dict.fromkeys(c.GATES, "pending"), duplicate_of=None,
                 pair_reviews=[{"pair_id": p["pair_id"], "outcome": "pending", "rationale": "Collision review pending"}
                               for p in analysis["pairs"] if r["id"] in (p["left"], p["right"])
                               and p["signal"] != "no_algorithmic_signal"])
        decisions.append(d)
    return {"schema_version": 1, "run_id": c.RUN, "analysis_sha256": c.sha(c.encode(analysis)),
            "authority": "agent_proposal" if draft else "human", "decisions": decisions}


class MetricsTests(unittest.TestCase):
    def test_invalid_decoder(self):
        self.assertEqual(c.metrics(b"not an image")["decode"], "failed")

    def test_mpo_and_non_jpeg_not_accepted(self):
        out = BytesIO()
        Image.new("RGB", (10, 10)).save(out, format="PNG")
        self.assertEqual(c.metrics(out.getvalue())["decode"], "failed")

    def test_dimensions_flat_luminance_and_laplacian(self):
        m = c.metrics(jpeg(10))
        self.assertEqual((m["width"], m["height"]), (24, 16))
        self.assertEqual(m["laplacian_variance"], 0)
        self.assertEqual(m["dhash64"], "0000000000000000")
        self.assertIn("low_laplacian_variance", m["flags"])
        self.assertNotIn("decision", m)

    def test_signed_laplacian_known_values(self):
        # 3x3 interiors of 5x5 checkerboard alternate +/-1020: population var.
        pixels = [255 * ((x + y) % 2) for y in range(5) for x in range(5)]
        expected = (9 * 1020**2 * 9 - 1020**2) / 81
        self.assertEqual(c.laplacian_variance(pixels, 5, 5), expected)
        self.assertEqual(c.laplacian_variance([7] * 25, 5, 5), 0)

    def test_dhash_bit_order_and_strict_greater(self):
        im = Image.new("L", (9, 8))
        im.putdata([x * 20 for _ in range(8) for x in range(9)])
        self.assertEqual(c.dhash(im), "ffffffffffffffff")
        im.putdata([160 - x * 20 for _ in range(8) for x in range(9)])
        self.assertEqual(c.dhash(im), "0000000000000000")
        im.putdata([0, 255, 0, 0, 0, 0, 0, 0, 0] + [0] * 63)
        self.assertEqual(c.dhash(im), "8000000000000000")

    def test_near_duplicate_synthetic_bytes_different(self):
        a, b = jpeg(10), jpeg(11)
        self.assertNotEqual(c.sha(a), c.sha(b))
        result = c.compare_pair({"id": "Q01", "sha256": c.sha(a), "technical": c.metrics(a)},
                                {"id": "Q02", "sha256": c.sha(b), "technical": c.metrics(b)})
        self.assertEqual(result["signal"], "near_duplicate_candidate")
        self.assertEqual(result["hamming_distance"], 0)
        self.assertNotIn("decision", result)

    def test_exact_duplicate_precedes_perceptual_signal(self):
        a = {"id": "Q01", "sha256": "same", "technical": {"dhash64": "0" * 16}}
        b = {"id": "Q02", "sha256": "same", "technical": {"dhash64": "f" * 16}}
        self.assertEqual(c.compare_pair(a, b)["signal"], "exact_duplicate")

    def test_textured_near_duplicate_and_different_color_collision(self):
        im = Image.new("RGB", (90, 80))
        im.putdata([(x * 2, y * 2, (x + y) % 255) for y in range(80) for x in range(90)])
        blobs = []
        for quality in (90, 95):
            stream = BytesIO()
            im.save(stream, format="JPEG", quality=quality)
            blobs.append(stream.getvalue())
        self.assertNotEqual(c.sha(blobs[0]), c.sha(blobs[1]))
        a, b = [dict(id=f"Q{i+1:02}", sha256=c.sha(raw), technical=c.metrics(raw)) for i, raw in enumerate(blobs)]
        self.assertLessEqual(c.compare_pair(a, b)["hamming_distance"], 6)
        self.assertEqual(c.dhash(Image.new("RGB", (20, 20), "red")),
                         c.dhash(Image.new("RGB", (20, 20), "blue")))

    def test_hamming_all_boundaries(self):
        for distance, expected in [(0, "near_duplicate_candidate"), (6, "near_duplicate_candidate"),
                                   (7, "borderline_visual_pair"), (10, "borderline_visual_pair"),
                                   (11, "no_algorithmic_signal"), (64, "no_algorithmic_signal")]:
            a = {"id": "Q01", "sha256": "a", "technical": {"dhash64": "0" * 16}}
            b = {"id": "Q02", "sha256": "b", "technical": {"dhash64": f"{(1 << distance) - 1:016x}"}}
            self.assertEqual(c.compare_pair(a, b)["signal"], expected)
            self.assertEqual(c.compare_pair(a, b)["hamming_distance"], distance)

    def test_missing_hash_is_human_review(self):
        a = {"id": "Q01", "sha256": "a", "technical": {"dhash64": None}}
        b = {"id": "Q02", "sha256": "b", "technical": {"dhash64": "0" * 16}}
        self.assertEqual(c.compare_pair(a, b)["signal"], "needs_human_review")

    def test_quality_boundary_operators(self):
        self.assertEqual(c.flags_for(224, 672, 40, .249, .249, 100), [])
        self.assertEqual(c.flags_for(224, 672, 215, .249, .249, 100), [])
        self.assertIn("small_dimension", c.flags_for(223, 400, 100, 0, 0, 100))
        self.assertIn("extreme_aspect", c.flags_for(224, 673, 100, 0, 0, 100))
        for mean, flag in [(39.999, "dark_mean"), (215.001, "bright_mean")]:
            self.assertIn(flag, c.flags_for(224, 224, mean, 0, 0, 100))
        self.assertIn("dark_fraction", c.flags_for(224, 224, 100, .25, 0, 100))
        self.assertIn("bright_fraction", c.flags_for(224, 224, 100, 0, .25, 100))
        self.assertIn("low_laplacian_variance", c.flags_for(224, 224, 100, 0, 0, 99.999))

    def test_exposure_pixel_thresholds(self):
        for luminance, dark, bright in [(15, 1, 0), (16, 0, 0), (239, 0, 0), (240, 0, 1)]:
            out = BytesIO()
            Image.new("L", (256, 256), luminance).save(out, format="JPEG", quality=100)
            m = c.metrics(out.getvalue())
            self.assertEqual((m["dark_fraction"], m["bright_fraction"]), (dark, bright))


class ReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.source = Path(cls.tmp.name) / "source"
        source_fixture(cls.source)
        cls.analysis = c.analyze(cls.source)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_all_136_unique_pairs_no_decisions(self):
        a = self.analysis
        self.assertEqual(len(a["records"]), 17)
        self.assertEqual(len({p["pair_id"] for p in a["pairs"]}), 136)
        self.assertEqual([r["id"] for r in a["records"]], c.IDS)
        self.assertTrue(all("decision" not in r for r in a["records"]))

    def test_zero_approved_human_reviews_are_valid(self):
        out = c.curate(self.analysis, decisions_for(self.analysis))
        self.assertEqual(out["counts"]["needs_botanical_review"], 17)
        self.assertEqual(out["counts"]["approved_for_dataset"], 0)
        self.assertFalse(out["training_authorized"])
        self.assertEqual(len(out["classes_without_approved"]), 14)

    def test_agent_draft_explicit_and_cannot_finalize(self):
        decisions = decisions_for(self.analysis, True)
        out = c.curate(self.analysis, decisions, draft=True)
        self.assertEqual(out["stage"], "agent_proposals_pending_human")
        with self.assertRaisesRegex(c.CurationError, "human_authority_required"):
            c.curate(self.analysis, decisions)

    def test_agent_never_approves(self):
        d = decisions_for(self.analysis, True)
        d["decisions"][0]["state"] = "approved_for_dataset"
        with self.assertRaisesRegex(c.CurationError, "no_agent_approval"):
            c.curate(self.analysis, d, draft=True)

    def test_approval_requires_botanical_quality_privacy_pairs(self):
        d = decisions_for(self.analysis)
        d["decisions"][0]["state"] = "approved_for_dataset"
        with self.assertRaises(c.CurationError):
            c.curate(self.analysis, d)
        for x in d["decisions"]:
            x["gates"] = dict.fromkeys(c.GATES, "sufficient")
            x["botanical"]["status"] = "sufficient"
            x["state"] = "approved_for_dataset"
            for p in x["pair_reviews"]:
                p["outcome"] = "distinct"
        self.assertEqual(c.curate(self.analysis, d)["counts"]["approved_for_dataset"], 17)
        for key in c.GATES:
            bad = deepcopy(d)
            bad["decisions"][0]["gates"][key] = "pending"
            with self.assertRaises(c.CurationError):
                c.curate(self.analysis, bad)
        bad = deepcopy(d)
        bad["decisions"][0]["privacy"]["faces"] = "uncertain"
        with self.assertRaises(c.CurationError):
            c.curate(self.analysis, bad)

    def test_no_p06_auto_promotion(self):
        out = c.curate(self.analysis, decisions_for(self.analysis))
        self.assertTrue(all(r["prior_p06_decision"] == "aprovar_para_curadoria_futura" for r in out["records"]))
        self.assertEqual(out["counts"]["approved_for_dataset"], 0)

    def test_decision_fields_identity_and_types(self):
        for key, value in [("id", "Q02"), ("review_id", "R02"), ("sha256", "a" * 64),
                           ("class_id", "species_02"), ("state", "approved"),
                           ("reviewer_role", "agent"), ("timestamp", "2026-09-30T00:00:00"),
                           ("rationale", ""), ("original_resolution_review", "true")]:
            with self.subTest(key=key):
                d = decisions_for(self.analysis)
                d["decisions"][0][key] = value
                with self.assertRaises(c.CurationError):
                    c.curate(self.analysis, d)
        d = decisions_for(self.analysis)
        d["decisions"][0]["unknown"] = 1
        with self.assertRaises(c.CurationError):
            c.curate(self.analysis, d)

    def test_missing_or_duplicate_decision(self):
        for mutation in (lambda d: d["decisions"].pop(),
                         lambda d: d["decisions"].__setitem__(1, d["decisions"][0])):
            d = decisions_for(self.analysis)
            mutation(d)
            with self.assertRaises(c.CurationError):
                c.curate(self.analysis, d)

    def test_missing_and_inconsistent_pair_reviews(self):
        d = decisions_for(self.analysis)
        d["decisions"][0]["pair_reviews"].pop()
        with self.assertRaisesRegex(c.CurationError, "missing_pair_review"):
            c.curate(self.analysis, d)
        d = decisions_for(self.analysis)
        d["decisions"][0]["pair_reviews"][0]["outcome"] = "distinct"
        with self.assertRaisesRegex(c.CurationError, "inconsistent_pair_reviews"):
            c.curate(self.analysis, d)

    def test_report_roundtrip_is_byte_identical(self):
        result = c.curate(self.analysis, decisions_for(self.analysis))
        self.assertEqual(c.report(result), c.report(c.strict_load(c.encode(result))))

    def test_duplicate_rejection_requires_explicit_pair_decision(self):
        d = decisions_for(self.analysis)
        d["decisions"][0].update(state="rejected_duplicate", duplicate_of="Q02")
        with self.assertRaisesRegex(c.CurationError, "duplicate_pair_evidence"):
            c.curate(self.analysis, d)

    def test_duplicate_rejection_requires_keeper(self):
        d = decisions_for(self.analysis)
        d["decisions"][0]["state"] = "rejected_duplicate"
        with self.assertRaisesRegex(c.CurationError, "duplicate_reference_required"):
            c.curate(self.analysis, d)
        d["decisions"][0]["duplicate_of"] = "Q02"
        d["decisions"][0]["gates"]["uniqueness"] = "insufficient"
        for entry in d["decisions"][:2]:
            next(p for p in entry["pair_reviews"] if p["pair_id"] == "Q01-Q02")["outcome"] = "duplicate"
        self.assertEqual(c.curate(self.analysis, d)["counts"]["rejected_duplicate"], 1)
        d["decisions"][1]["state"] = "rejected_quality"
        d["decisions"][1]["gates"]["quality"] = "insufficient"
        with self.assertRaisesRegex(c.CurationError, "duplicate_keeper"):
            c.curate(self.analysis, d)

    def test_manual_pair_without_algorithmic_signal_is_reviewable(self):
        a = deepcopy(self.analysis)
        for p in a["pairs"]:
            p["signal"] = "no_algorithmic_signal"
        d = decisions_for(a)
        pair = {"pair_id": "Q01-Q02", "outcome": "pending", "rationale": "Visual scene overlap"}
        d["decisions"][0]["pair_reviews"] = [pair]
        d["decisions"][1]["pair_reviews"] = [deepcopy(pair)]
        self.assertEqual(c.curate(a, d)["counts"]["needs_botanical_review"], 17)
        d["decisions"][1]["pair_reviews"] = []
        with self.assertRaisesRegex(c.CurationError, "inconsistent_pair_reviews"):
            c.curate(a, d)

    def test_rejected_label_and_privacy_need_matching_evidence(self):
        for state in ("rejected_quality", "rejected_label", "rejected_privacy"):
            d = decisions_for(self.analysis)
            d["decisions"][0]["state"] = state
            with self.assertRaises(c.CurationError):
                c.curate(self.analysis, d)

    def test_summary_excludes_private_text_and_origin(self):
        d = decisions_for(self.analysis)
        d["decisions"][0]["rationale"] = "PRIVATE_SENTINEL email@example.invalid plate123"
        result = c.curate(self.analysis, d)
        raw = c.encode(c.summary(result))
        for secret in (b"PRIVATE_SENTINEL", b"email@", b"plate123", b"provenance", b"reviewer_id", b"synthetic-reviewer"):
            self.assertNotIn(secret, raw)
        self.assertEqual(set(c.summary(result)["records"][0]), {"id", "review_id", "sha256", "class_id", "state"})


class PersistenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.output = self.root / "output"
        source_fixture(self.source)

    def test_analysis_then_human_finalize_idempotent(self):
        before = c.tree_hashes(self.source)
        c.run(self.source, self.output)
        a = c.strict_load((self.output / "analysis.json").read_bytes())
        decisions = self.output / "human-decisions.json"
        decisions.write_bytes(c.encode(decisions_for(a)))
        c.run(self.source, self.output, decisions_path=decisions)
        first = c.tree_hashes(self.output)
        mtimes = {p: (self.output / p).stat().st_mtime_ns for p in first}
        c.run(self.source, self.output, decisions_path=decisions)
        self.assertEqual(first, c.tree_hashes(self.output))
        self.assertEqual(mtimes, {p: (self.output / p).stat().st_mtime_ns for p in first})
        self.assertEqual(before, c.tree_hashes(self.source))

    def test_draft_does_not_create_final_files(self):
        c.run(self.source, self.output)
        a = c.strict_load((self.output / "analysis.json").read_bytes())
        d = self.output / "human-decisions.json"
        d.write_bytes(c.encode(decisions_for(a, True)))
        c.run(self.source, self.output, decisions_path=d, draft=True)
        self.assertTrue((self.output / "curation.draft.json").exists())
        self.assertFalse((self.output / "curation.json").exists())
        with self.assertRaises(c.CurationError):
            c.run(self.source, self.output, decisions_path=d)

    def test_modified_image_missing_extra_symlink_block(self):
        image = next((self.source / "quarantine").iterdir())
        old = image.read_bytes()
        image.write_bytes(old + b"modified")
        with self.assertRaises(c.CurationError):
            c.run(self.source, self.output)
        image.write_bytes(old)
        extra = self.source / "quarantine/extra.jpg"
        extra.write_bytes(old)
        rehash(self.source)
        with self.assertRaisesRegex(c.CurationError, "image_set_17"):
            c.run(self.source, self.output)
        extra.unlink()
        image.unlink()
        with self.assertRaises(c.CurationError):
            c.run(self.source, self.output)
        image.symlink_to(self.source / "manifest.jsonl")
        with self.assertRaisesRegex(c.CurationError, "symlink"):
            c.run(self.source, self.output)
        self.assertFalse((self.output / "analysis.json").exists())

    def test_state_manifest_mismatch_even_with_updated_checksums(self):
        state = c.strict_load((self.source / "state.json").read_bytes())
        state["records"][0]["class_id"] = "species_02"
        (self.source / "state.json").write_bytes(c.encode(state))
        rehash(self.source)
        with self.assertRaisesRegex(c.CurationError, "state_manifest_mismatch"):
            c.analyze(self.source)

    def test_qr_mapping_error(self):
        p = self.source / "review-2026-09-28/human-decisions.json"
        d = c.strict_load(p.read_bytes())
        d["decisions"][0]["review_id"] = "R02"
        p.write_bytes(c.encode(d))
        rehash(self.source)
        with self.assertRaisesRegex(c.CurationError, "qr_mapping"):
            c.analyze(self.source)

    def test_source_change_during_decode_no_output(self):
        original = c.metrics
        def mutate(raw):
            value = original(raw)
            (self.source / "unexpected").write_text("change")
            return value
        with patch.object(c, "metrics", side_effect=mutate):
            with self.assertRaisesRegex(c.CurationError, "source_changed"):
                c.run(self.source, self.output)
        self.assertFalse((self.output / "analysis.json").exists())

    def test_output_conflict_preserves_previous_result(self):
        self.output.mkdir()
        (self.output / "b").write_bytes(b"old")
        with self.assertRaisesRegex(c.CurationError, "output_conflict"):
            c.persist(self.output, {"a": b"new", "b": b"different"})
        self.assertEqual((self.output / "b").read_bytes(), b"old")
        self.assertFalse((self.output / "a").exists())

    def test_lock_excludes_concurrent_writer(self):
        with c.output_lock(self.output, self.source):
            with self.assertRaisesRegex(c.CurationError, "output_locked"):
                with c.output_lock(self.output, self.source):
                    self.fail("lock accepted")

    def test_output_cannot_be_source_or_git_or_symlink(self):
        for p in (self.source, self.source / "child", self.root):
            with self.assertRaises(c.CurationError):
                with c.output_lock(p, self.source):
                    self.fail("overlap accepted")
        repo = self.root / "fake-git"
        repo.mkdir()
        (repo / ".git").mkdir()
        (repo / ".git/HEAD").write_text("ref: refs/heads/test\n")
        with self.assertRaisesRegex(c.CurationError, "output_inside_git"):
            with c.output_lock(repo / "outputs", self.source):
                self.fail("git accepted")
        self.output.symlink_to(repo, target_is_directory=True)
        with self.assertRaisesRegex(c.CurationError, "symlink"):
            with c.output_lock(self.output, self.source):
                self.fail("symlink accepted")

    def test_unknown_state_field_fails_closed(self):
        path = self.source / "state.json"
        state = c.strict_load(path.read_bytes())
        state["unknown"] = 1
        path.write_bytes(c.encode(state))
        rehash(self.source)
        with self.assertRaisesRegex(c.CurationError, "object_fields"):
            c.analyze(self.source)


class StrictJSONTests(unittest.TestCase):
    def test_reject_nonfinite_duplicate_encoding_and_coercion(self):
        for raw in (b'{"a":1,"a":2}\n', b'{"a":NaN}\n', b'{"a":Infinity}\n', b'{"a":1e999}\n',
                    b'{}\r\n', b'{}', b'\xef\xbb\xbf{}\n', b'\xff\n'):
            with self.subTest(raw=raw), self.assertRaises(c.CurationError):
                c.strict_load(raw)
        self.assertEqual(c.strict_load(b'{"a":true}\n'), {"a": True})
        self.assertEqual(c.strict_load(c.encode({"v": "á"})), {"v": "á"})


if __name__ == "__main__":
    unittest.main()
