"""Focused boundaries for the new experiment; synthetic fixtures contain no source data."""
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import train_experimental as experiment


LABELS = [{"index": i, "class_id": f"species_{i+1:02d}", "scientific_name": f"Genus species{i}"}
          for i in range(12)]


def fixture_selection():
    return [{"candidate_id": f"candidate-{i}-{j}", "class_id": label["class_id"],
             "scientific_name": label["scientific_name"],
             "original": {"sha256": f"original-{i}-{j}"},
             "sanitized": {"sha256": f"sanitized-{i}-{j}"}}
            for i, label in enumerate(LABELS) for j in range(2)]


class GroupTests(unittest.TestCase):
    def setUp(self):
        self.rows = fixture_selection()
        self.catalog = {"items": copy.deepcopy(self.rows), "reserved": [], "excluded": []}

    def split(self):
        return experiment.grouped_split(self.rows, self.catalog, LABELS)

    def test_deterministic_order_and_seed(self):
        result = self.split()
        self.catalog["items"].reverse()
        self.rows.reverse()
        self.assertEqual(result, self.split())
        self.assertEqual(sum(r["split"] == "evaluation" for r in result), 12)

    def test_singleton_is_training_only(self):
        self.rows.pop()
        result = self.split()
        self.assertEqual([r["split"] for r in result if r["class_id"] == "species_12"], ["train"])

    def test_transitive_relation_through_reserved_and_excluded(self):
        self.catalog["items"][0]["source_series_signals"] = ["session-A"]
        self.catalog["items"][1]["source_series_signals"] = ["session-B"]
        self.catalog["reserved"] = [{"candidate_id": "reserved", "source_series_signals": ["session-A", "bridge"]}]
        self.catalog["excluded"] = [{"candidate_id": "excluded", "source_series_signals": ["bridge", "session-B"]}]
        result = [r for r in self.split() if r["class_id"] == "species_01"]
        self.assertEqual(len({r["group_id"] for r in result}), 1)
        self.assertEqual({r["split"] for r in result}, {"train"})

    def test_excluded_record_without_image_is_only_relationship_metadata(self):
        self.catalog["excluded"] = [{"candidate_id": "not-an-image", "original": None,
                                     "sanitized": None, "source_series_signals": []}]
        self.assertEqual(len(self.split()), 24)

    def test_representative_keeps_other_member_group(self):
        self.catalog["items"][0]["series_representative_selection"] = {
            "group_id": "known", "other_member": self.rows[1]["candidate_id"]}
        result = self.split()
        self.assertEqual(result[0]["group_id"], result[1]["group_id"])
        self.assertEqual(result[0]["split"], result[1]["split"])

    def test_same_bytes_never_cross_splits(self):
        self.catalog["items"][1]["sanitized"] = self.catalog["items"][0]["sanitized"]
        result = self.split()
        self.assertEqual(result[0]["split"], result[1]["split"])

    def test_conflicting_labels_in_related_group_fail(self):
        self.catalog["items"][2]["sanitized"] = self.catalog["items"][0]["sanitized"]
        with self.assertRaisesRegex(ValueError, "conflicting"):
            self.split()

    def test_repeated_candidate_fails(self):
        self.rows.append(self.rows[0])
        with self.assertRaisesRegex(ValueError, "Repeated"):
            self.split()

    def test_missing_training_class_fails(self):
        self.rows = self.rows[2:]
        with self.assertRaisesRegex(ValueError, "without a training"):
            self.split()


class Boundaries(unittest.TestCase):
    def bound_fixture(self, root):
        canonical = root / "canonical"; canonical.mkdir()
        rows = fixture_selection()
        for i, row in enumerate(rows):
            for kind in ("original", "sanitized"):
                path = canonical / f"{i}-{kind}"; path.write_bytes(f"{i}-{kind}".encode())
                row[kind] = {"path": str(path), "sha256": experiment.sha(path)}
        items = [{**row, "eligible_for_private_experiment": True,
                  "provisional_label": {"class_id": row["class_id"],
                      "scientific_name": row["scientific_name"], "confidence": "provisional_source_supported"}}
                 for row in rows]
        catalog = root / "catalog.json"; catalog.write_text(json.dumps({"items": items}))
        labels = root / "classes.json"
        labels.write_text(json.dumps({"classes": [{**label, "kind": "species"} for label in LABELS]}))
        manifest = root / "manifest.json"
        m = {"catalog": {"path": str(catalog), "sha256": experiment.sha(catalog)},
             "class_manifest": {"path": str(labels), "sha256": experiment.sha(labels)},
             "selection": rows, "canonical_snapshot": {"root": str(canonical)}}
        manifest.write_text(json.dumps(m))
        auth = root / "authorization.json"
        auth.write_text(json.dumps({"data_manifest_sha256": experiment.sha(manifest),
            "training_authorized": True, "private_only": True, "public_use_authorized": False,
            "owner_instruction": "synthetic test authorization"}))
        return manifest, auth, catalog, rows

    def test_full_bound_input_admits_only_accepted_24(self):
        with tempfile.TemporaryDirectory() as d:
            m, a, c, rows = self.bound_fixture(Path(d))
            with patch.object(experiment, "ACCEPTED_MANIFEST", experiment.sha(m)), \
                    patch.object(experiment, "ACCEPTED_CATALOG", experiment.sha(c)):
                _, labels, result = experiment.prepare_inputs(m, a)
                self.assertEqual(len(result), 24)
                self.assertEqual(labels, LABELS)
                self.assertEqual({r["candidate_id"] for r in result}, {r["candidate_id"] for r in rows})

    def test_changed_input_bytes_fail_before_any_training(self):
        with tempfile.TemporaryDirectory() as d:
            m, a, c, rows = self.bound_fixture(Path(d))
            Path(rows[0]["sanitized"]["path"]).write_bytes(b"tampered")
            with patch.object(experiment, "ACCEPTED_MANIFEST", experiment.sha(m)), \
                    patch.object(experiment, "ACCEPTED_CATALOG", experiment.sha(c)):
                with self.assertRaisesRegex(ValueError, "changed bound input"):
                    experiment.prepare_inputs(m, a)

    def test_catalog_cannot_add_reserved_item_to_selection(self):
        with tempfile.TemporaryDirectory() as d:
            m, a, c, rows = self.bound_fixture(Path(d))
            cat = json.loads(c.read_text()); cat["items"].append({**cat["items"][0], "candidate_id": "reserved"})
            c.write_text(json.dumps(cat))
            with patch.object(experiment, "ACCEPTED_MANIFEST", experiment.sha(m)):
                with self.assertRaisesRegex(ValueError, "changed bound input"):
                    experiment.prepare_inputs(m, a)

    def test_native_label_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            m, a, c, rows = self.bound_fixture(Path(d))
            cat = json.loads(c.read_text()); cat["items"][0]["provisional_label"]["scientific_name"] = "Conflicting name"
            c.write_text(json.dumps(cat))
            data = json.loads(m.read_text()); data["catalog"]["sha256"] = experiment.sha(c)
            m.write_text(json.dumps(data))
            auth = json.loads(a.read_text()); auth["data_manifest_sha256"] = experiment.sha(m)
            a.write_text(json.dumps(auth))
            with patch.object(experiment, "ACCEPTED_MANIFEST", experiment.sha(m)), \
                    patch.object(experiment, "ACCEPTED_CATALOG", experiment.sha(c)):
                with self.assertRaisesRegex(ValueError, "mismatched label"):
                    experiment.prepare_inputs(m, a)

    def test_labels_exclude_protection_and_keep_indices(self):
        classes = [{**label, "kind": "species"} for label in LABELS]
        classes.append({"kind": "protection", "class_id": "imagem_invalida", "index": 12})
        self.assertEqual(experiment.labels_from_manifest({"classes": classes}), LABELS)
        classes[0]["index"] = 1
        with self.assertRaises(ValueError):
            experiment.labels_from_manifest({"classes": classes})

    def test_bound_hash_and_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bytes"; p.write_bytes(b"original")
            ref = {"path": str(p), "sha256": experiment.sha(p)}
            self.assertEqual(experiment.read_bound(ref), p)
            p.write_bytes(b"changed")
            with self.assertRaises(ValueError):
                experiment.read_bound(ref)
            p.write_bytes(b"original")
            link = Path(d) / "link"; link.symlink_to(p)
            with self.assertRaises(ValueError):
                experiment.read_bound({**ref, "path": str(link)})

    def test_output_never_overwrites_or_enters_forbidden_root(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); protected = root / "canonical"; protected.mkdir()
            with self.assertRaises(ValueError):
                experiment.safe_output(protected / "new", [protected])
            out = experiment.safe_output(root / "run", [protected])
            with self.assertRaises(ValueError):
                experiment.safe_output(out, [protected])
            link = root / "link"; link.symlink_to(root, target_is_directory=True)
            with self.assertRaises(ValueError):
                experiment.safe_output(link / "run2", [])
            with self.assertRaises(ValueError):
                experiment.safe_output(root / ".." / root.name / "canonical" / "run3", [protected])

    def test_optional_quantization_failure_is_reported_without_relaxing_tolerance(self):
        result = experiment.parity_status("float16", 0.020740211009979248)
        self.assertFalse(result["numerical_parity_passed"])
        self.assertEqual(result["status"], "rejected_numerical_drift")
        self.assertEqual(result["tolerance"], 0.02)
        with self.assertRaises(ValueError):
            experiment.parity_status("float32", 0.001)

    def test_reject_unaccepted_manifest_before_authorization(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "manifest.json"; p.write_text("{}")
            with self.assertRaisesRegex(ValueError, "accepted data manifest"):
                experiment.prepare_inputs(p, p)

    def test_accepted_bytes_require_new_explicit_private_authorization(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); m = root / "manifest.json"; m.write_text("{}")
            a = root / "authorization.json"
            for auth in ({}, {"data_manifest_sha256": experiment.sha(m), "training_authorized": True,
                               "private_only": True, "public_use_authorized": True, "owner_instruction": "test"}):
                a.write_text(json.dumps(auth))
                with patch.object(experiment, "ACCEPTED_MANIFEST", experiment.sha(m)):
                    with self.assertRaisesRegex(ValueError, "authorization required"):
                        experiment.prepare_inputs(m, a)

    def test_json_does_not_silently_overwrite_evidence(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "proof.json"; experiment.write_json(p, {"old": True})
            with self.assertRaises(FileExistsError):
                experiment.write_json(p, {"new": True})


if __name__ == "__main__":
    unittest.main()
