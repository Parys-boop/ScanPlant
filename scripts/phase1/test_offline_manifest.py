"""Documentary contract tests: synthetic taxa, stdlib, no product integration."""

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

import validate_offline_manifest as validator


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def fixture():
    names = [f"Test{letter} alba" for letter in "abcdefghijkl"]
    roster = {"schema_version": 1, "status": "approved", "approval_ref": "synthetic approval",
              "approved_on": "2020-01-01", "species": [
                  {"index": i, "approved_name": name, "source_ref": "synthetic fixture"}
                  for i, name in enumerate(names)]}
    raw = encode(roster)
    manifest = {"schema_version": 1, "manifest_version": "1.1.0", "normalization_version": "1",
                "roster_sha256": hashlib.sha256(raw).hexdigest(), "references": [
                    {"ref_id": "synthetic_ref", "authority": "kew_powo",
                     "url": "https://powo.science.kew.org/taxon/urn:lsid:ipni.org:names:87014-1",
                     "consulted_on": "2020-01-01", "title": "Synthetic structural reference"}],
                "classes": []}
    for i, name in enumerate(names):
        manifest["classes"].append({
            "index": i, "class_id": f"species_{i + 1:02}", "kind": "species",
            "scientific_name": name, "display_name": "rótulo",
            "common_names": ["rótulo"], "synonyms": [],
            "taxonomy_ref_ids": ["synthetic_ref"], "definition": None})
    manifest["classes"][0]["synonyms"] = [{"name": "Aliasa alba", "ref_ids": ["synthetic_ref"]}]
    for i, (cid, label) in enumerate(validator.PROTECTIONS, 12):
        manifest["classes"].append({
            "index": i, "class_id": cid, "kind": "protection", "scientific_name": None,
            "display_name": label, "common_names": [], "synonyms": [], "taxonomy_ref_ids": [],
            "definition": "Synthetic protection definition"})
    return manifest, raw


class ManifestContractTests(unittest.TestCase):
    def setUp(self):
        self.manifest, self.roster = fixture()

    def test_positive_complete_contract(self):
        result = validator.validate_manifest(self.manifest, self.roster)
        self.assertEqual((result["species"], result["protection"], result["classes"]), (12, 2, 14))

    def test_positive_alias_and_case_whitespace(self):
        self.assertEqual(validator.resolve_scientific_name(self.manifest, " \tALIASA\u2003alba\n"),
                         "species_01")

    def test_positive_nfc_and_idempotence(self):
        for value in ["  Ro\u0301tulo\t COMUM ", "\u00a0Aliasa\n ALBA\u2003"]:
            normalized = validator.normalize_name(value)
            self.assertEqual(normalized, validator.normalize_name(normalized))
        self.assertEqual(validator.normalize_name("ro\u0301tulo"), "rótulo")

    def test_positive_common_homonym_separate_namespace(self):
        validator.validate_manifest(self.manifest, self.roster)
        self.assertIsNone(validator.resolve_scientific_name(self.manifest, "rótulo"))

    def test_positive_unknown_and_protection_are_not_scientific(self):
        for value in ["Unknown alba", "outra_planta", "imagem_invalida", "species_01",
                      "Testa", "Testa alba Author", "Aliasa alb", "Alías a"]:
            self.assertIsNone(validator.resolve_scientific_name(self.manifest, value))

    def test_positive_rename_preserves_roster_via_alias(self):
        entry = self.manifest["classes"][0]
        entry["synonyms"].append({"name": entry["scientific_name"], "ref_ids": ["synthetic_ref"]})
        entry["scientific_name"] = "Renamed alba"
        validator.validate_manifest(self.manifest, self.roster)
        self.assertEqual(validator.resolve_scientific_name(self.manifest, "Testa alba"), "species_01")

    def test_negative_species_order_with_indices_preserved(self):
        first, second = self.manifest["classes"][:2]
        first["scientific_name"], second["scientific_name"] = second["scientific_name"], first["scientific_name"]
        with self.assertRaises(validator.ContractError) as caught:
            validator.validate_manifest(self.manifest, self.roster)
        self.assertEqual(caught.exception.code, "E_ROSTER_MAPPING")

    def test_cli_valid_invalid_inaccessible_and_invocation(self):
        script = Path(validator.__file__).resolve()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            mpath, rpath = root / "manifest.json", root / "roster.json"
            mpath.write_bytes(encode(self.manifest))
            rpath.write_bytes(self.roster)
            base = [sys.executable, "-B", str(script)]
            args = ["--manifest", str(mpath), "--roster", str(rpath)]
            before = {p.name: p.read_bytes() for p in root.iterdir()}
            result = subprocess.run(base + args, capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["classes"], 14)
            self.assertEqual(before, {p.name: p.read_bytes() for p in root.iterdir()})
            mpath.write_bytes(b'{"sensitive_value_do_not_echo": 1}\n')
            result = subprocess.run(base + args, capture_output=True, check=False)
            self.assertEqual(result.returncode, 1)
            self.assertIn(b"E_FIELDS $", result.stderr)
            self.assertNotIn(b"sensitive_value_do_not_echo", result.stderr + result.stdout)
            mpath.unlink()
            self.assertEqual(subprocess.run(base + args, capture_output=True, check=False).returncode, 2)
            self.assertEqual(subprocess.run(base, capture_output=True, check=False).returncode, 2)

    def test_cli_no_network_or_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            mpath, rpath = Path(folder) / "manifest.json", Path(folder) / "roster.json"
            mpath.write_bytes(encode(self.manifest))
            rpath.write_bytes(self.roster)
            # Audit hook in an isolated subprocess catches filesystem writes and socket activity.
            code = (
                "import runpy,sys\n"
                "def audit(event,args):\n"
                " if event.startswith('socket.') or (event=='open' and "
                "((isinstance(args[1],str) and any(c in args[1] for c in 'wax+')) or "
                "(isinstance(args[2],int) and args[2] & 0x643))):\n"
                "  raise RuntimeError('forbidden side effect')\n"
                "sys.addaudithook(audit)\n"
                "sys.argv=sys.argv[1:]\n"
                "runpy.run_path(sys.argv[0],run_name='__main__')\n")
            result = subprocess.run([sys.executable, "-B", "-c", code, validator.__file__,
                                     "--manifest", str(mpath), "--roster", str(rpath)],
                                    capture_output=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)


def altered(path, value=None, delete=False):
    def change(manifest):
        target = manifest
        for part in path[:-1]:
            target = target[part]
        if delete:
            del target[path[-1]]
        else:
            target[path[-1]] = value
    return change


NEGATIVE_CASES = {
    "total_13": (lambda m: m["classes"].pop(), "E_CLASS_COUNT"),
    "total_15": (lambda m: m["classes"].append(deepcopy(m["classes"][0])), "E_CLASS_COUNT"),
    "species_11": (altered(["classes", 11, "kind"], "protection"), "E_KIND"),
    "species_13": (altered(["classes", 12, "kind"], "species"), "E_KIND"),
    "protection_absent": (altered(["classes", 12, "class_id"], "missing"), "E_CLASS_ID"),
    "protection_duplicate": (altered(["classes", 13, "class_id"], "outra_planta"), "E_CLASS_ID"),
    "protection_swapped": (lambda m: m["classes"].__setitem__(slice(12, 14), m["classes"][12:14][::-1]), "E_INDEX"),
    "index_missing": (altered(["classes", 0, "index"], delete=True), "E_FIELDS"),
    "index_duplicate": (altered(["classes", 1, "index"], 0), "E_INDEX"),
    "index_outside": (altered(["classes", 13, "index"], 14), "E_INDEX"),
    "index_boolean": (altered(["classes", 0, "index"], False), "E_INDEX"),
    "index_string": (altered(["classes", 0, "index"], "0"), "E_INDEX"),
    "index_float": (altered(["classes", 0, "index"], 0.0), "E_INDEX"),
    "array_order": (lambda m: m["classes"].reverse(), "E_INDEX"),
    "renumbered_order": (altered(["classes", 0, "scientific_name"], "Outside alba"), "E_ROSTER_MAPPING"),
    "id_duplicate": (altered(["classes", 1, "class_id"], "species_01"), "E_CLASS_ID"),
    "id_common_name": (altered(["classes", 0, "class_id"], "rótulo"), "E_CLASS_ID"),
    "canonical_duplicate": (altered(["classes", 1, "scientific_name"], "Testa alba"), "E_NAME_COLLISION"),
    "alias_equals_canonical": (altered(["classes", 0, "synonyms", 0, "name"], "Testa alba"), "E_NAME_COLLISION"),
    "alias_cross_canonical": (altered(["classes", 0, "synonyms", 0, "name"], "Testb alba"), "E_NAME_COLLISION"),
    "alias_intra_duplicate": (lambda m: m["classes"][0]["synonyms"].append(deepcopy(m["classes"][0]["synonyms"][0])), "E_NAME_COLLISION"),
    "alias_inter_duplicate": (lambda m: m["classes"][1]["synonyms"].extend(deepcopy(m["classes"][0]["synonyms"])), "E_NAME_COLLISION"),
    "alias_no_reference": (altered(["classes", 0, "synonyms", 0, "ref_ids"], []), "E_EMPTY"),
    "alias_reference_missing": (altered(["classes", 0, "synonyms", 0, "ref_ids"], ["unknown_ref"]), "E_REF_MISSING"),
    "alias_infraspecific": (altered(["classes", 0, "synonyms", 0, "name"], "Testa alba var. rubra"), "E_BINOMIAL"),
    "canonical_authorship": (altered(["classes", 0, "scientific_name"], "Testa alba L."), "E_BINOMIAL"),
    "canonical_hybrid": (altered(["classes", 0, "scientific_name"], "Testa ×alba"), "E_BINOMIAL"),
    "canonical_lowercase": (altered(["classes", 0, "scientific_name"], "testa alba"), "E_BINOMIAL"),
    "canonical_whitespace": (altered(["classes", 0, "scientific_name"], "Testa  alba"), "E_BINOMIAL"),
    "common_intra_duplicate": (altered(["classes", 0, "common_names"], ["rótulo", " RO\u0301TULO "]), "E_COMMON_DUPLICATE"),
    "common_empty": (altered(["classes", 0, "common_names"], []), "E_DISPLAY_NAME"),
    "display_outside_common": (altered(["classes", 0, "display_name"], "outro"), "E_DISPLAY_NAME"),
    "invisible_character": (altered(["classes", 0, "display_name"], "rótulo\u200b"), "E_UNICODE"),
    "control_character": (altered(["classes", 0, "display_name"], "rótulo\u0000"), "E_UNICODE"),
    "protection_as_species": (altered(["classes", 13, "kind"], "species"), "E_KIND"),
    "species_as_protection": (altered(["classes", 0, "kind"], "protection"), "E_KIND"),
    "protection_scientific_name": (altered(["classes", 12, "scientific_name"], "Testa alba"), "E_PROTECTION"),
    "protection_alias": (altered(["classes", 12, "synonyms"], [{"name": "Aliasa alba", "ref_ids": ["synthetic_ref"]}]), "E_PROTECTION"),
    "protection_label": (altered(["classes", 12, "display_name"], "Planta"), "E_PROTECTION"),
    "protection_definition_empty": (altered(["classes", 12, "definition"], " "), "E_EMPTY"),
    "species_definition": (altered(["classes", 0, "definition"], "unexpected"), "E_SPECIES_DEFINITION"),
    "schema_2": (altered(["schema_version"], 2), "E_SCHEMA"),
    "schema_bool": (altered(["schema_version"], True), "E_SCHEMA"),
    "manifest_version": (altered(["manifest_version"], "2.0.0"), "E_VERSION"),
    "normalization_version": (altered(["normalization_version"], 1), "E_VERSION"),
    "hash_wrong": (altered(["roster_sha256"], "0" * 64), "E_ROSTER_HASH"),
    "extra_root_field": (altered(["extra"], "secret"), "E_FIELDS"),
    "extra_class_field": (altered(["classes", 0, "extra"], 0), "E_FIELDS"),
    "extra_alias_field": (altered(["classes", 0, "synonyms", 0, "extra"], 0), "E_FIELDS"),
    "classes_wrong_type": (altered(["classes"], {}), "E_ARRAY"),
    "class_wrong_type": (altered(["classes", 0], []), "E_OBJECT"),
    "synonyms_wrong_type": (altered(["classes", 0, "synonyms"], None), "E_ARRAY"),
    "name_wrong_type": (altered(["classes", 0, "scientific_name"], 1), "E_STRING"),
    "reference_duplicate": (lambda m: m["references"].append(deepcopy(m["references"][0])), "E_REF_DUPLICATE"),
    "reference_orphan": (lambda m: m["references"].append(dict(m["references"][0], ref_id="orphan_ref")), "E_REF_ORPHAN"),
    "reference_id_format": (altered(["references", 0, "ref_id"], "Not Snake"), "E_REF_ID"),
    "reference_list_duplicate": (altered(["classes", 0, "taxonomy_ref_ids"], ["synthetic_ref", "synthetic_ref"]), "E_REF_DUPLICATE"),
    "reference_list_empty": (altered(["classes", 0, "taxonomy_ref_ids"], []), "E_EMPTY"),
    "date_impossible": (altered(["references", 0, "consulted_on"], "2024-02-30"), "E_DATE"),
    "date_future": (altered(["references", 0, "consulted_on"], "9999-12-31"), "E_DATE_FUTURE"),
    "url_unofficial": (altered(["references", 0, "url"], "https://example.org/taxon/87014-1"), "E_URL_AUTHORITY"),
    "url_homepage": (altered(["references", 0, "url"], "https://powo.science.kew.org/"), "E_URL_AUTHORITY"),
    "url_query": (altered(["references", 0, "url"], "https://powo.science.kew.org/taxon/87014-1?q=x"), "E_URL"),
    "url_fragment": (altered(["references", 0, "url"], "https://powo.science.kew.org/taxon/87014-1#x"), "E_URL"),
    "url_userinfo": (altered(["references", 0, "url"], "https://user@powo.science.kew.org/taxon/87014-1"), "E_URL"),
    "url_empty_userinfo": (altered(["references", 0, "url"], "https://@powo.science.kew.org/taxon/87014-1"), "E_URL"),
    "url_whitespace": (altered(["references", 0, "url"], "https://powo.science.kew.org/\ntaxon/87014-1"), "E_URL"),
    "authority_invalid": (altered(["references", 0, "authority"], "unknown"), "E_URL_AUTHORITY"),
}


def negative_method(change, expected):
    def test(self):
        change(self.manifest)
        with self.assertRaises(validator.ContractError) as caught:
            validator.validate_manifest(self.manifest, self.roster)
        self.assertEqual(caught.exception.code, expected)
        self.assertTrue(caught.exception.path.startswith("$"))
    return test


for case_name, (mutation, expected_code) in NEGATIVE_CASES.items():
    setattr(ManifestContractTests, "test_negative_" + case_name, negative_method(mutation, expected_code))


class RosterAndTransportTests(unittest.TestCase):
    def test_roster_negative_cases(self):
        manifest, raw = fixture()
        for name, change, expected in [
            ("eleven", lambda r: r["species"].pop(), "E_ROSTER_COUNT"),
            ("thirteen", lambda r: r["species"].append(r["species"][0]), "E_ROSTER_COUNT"),
            ("index", altered(["species", 0, "index"], True), "E_INDEX"),
            ("duplicate", altered(["species", 1, "approved_name"], "Testa alba"), "E_ROSTER_DUPLICATE"),
            ("schema", altered(["schema_version"], True), "E_SCHEMA"),
            ("approval", altered(["status"], "pending"), "E_APPROVAL"),
            ("approval_ref", altered(["approval_ref"], ""), "E_EMPTY"),
            ("source_ref", altered(["species", 0, "source_ref"], ""), "E_EMPTY"),
            ("extra", altered(["extra"], 0), "E_FIELDS"),
            ("order", lambda r: r["species"].reverse(), "E_INDEX"),
            ("date", altered(["approved_on"], "2020-00-00"), "E_DATE"),
            ("infraspecific", altered(["species", 0, "approved_name"], "Testa alba var. rubra"), "E_BINOMIAL"),
        ]:
            with self.subTest(case=name):
                roster = json.loads(raw)
                change(roster)
                changed_raw = encode(roster)
                manifest["roster_sha256"] = hashlib.sha256(changed_raw).hexdigest()
                with self.assertRaises(validator.ContractError) as caught:
                    validator.validate_manifest(manifest, changed_raw)
                self.assertEqual(caught.exception.code, expected)

    def test_strict_transport_rejections(self):
        for raw, expected in [
            (b'{"a":1,"a":2}\n', "E_JSON_DUPLICATE_KEY"),
            (b'{"a":{"b":1,"b":2}}\n', "E_JSON_DUPLICATE_KEY"),
            (b'{"a":NaN}\n', "E_JSON_NONFINITE"),
            (b'{"a":Infinity}\n', "E_JSON_NONFINITE"),
            (b'{"a":-Infinity}\n', "E_JSON_NONFINITE"),
            (b'{"a":1e999}\n', "E_JSON_NONFINITE"),
            (b'\xef\xbb\xbf{}\n', "E_ENCODING"),
            (b'{}\r\n', "E_ENCODING"),
            (b'{}', "E_ENCODING"),
            (b'{"a":"\xff"}\n', "E_ENCODING"),
            (b'{}garbage\n', "E_JSON"),
            (b'{"a":' + b'9' * 5000 + b'}\n', "E_JSON"),
        ]:
            with self.subTest(raw=repr(raw)):
                with self.assertRaises(validator.ContractError) as caught:
                    validator.strict_load(raw)
                self.assertEqual(caught.exception.code, expected)

    def test_roster_duplicate_json_keys_rejected(self):
        manifest, _ = fixture()
        with self.assertRaises(validator.ContractError) as caught:
            validator.validate_manifest(manifest, b'{"schema_version":1,"schema_version":1}\n')
        self.assertEqual(caught.exception.code, "E_JSON_DUPLICATE_KEY")

    def test_normalization_invalid_inputs(self):
        for value in [None, 1, "", " \t\n", "a\u0000", "a\u200b", "a\ud800"]:
            with self.subTest(value=repr(value)), self.assertRaises(validator.ContractError):
                validator.normalize_name(value)


class ApprovedQuarantineTests(unittest.TestCase):
    """Compare the real contract to an independently pinned, pre-quarantine baseline."""

    ROOT = Path(__file__).resolve().parents[2]
    MANIFEST = "docs/phase1/offline-class-manifest.v1.json"
    ROSTER = "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json"
    BASE = "77e93a221dad3115c301b10317b626c236a3ba84"
    BASE_SHA256 = "39c8ce592df66ee51fc598f289fa61b498579d4d46a1b4dba68d2d49214dbbd5"
    QUARANTINED = ("Aloe maculata", "Aloe variegata", "Ficus clusiifolia", "Ficus cordata")

    @classmethod
    def setUpClass(cls):
        raw = subprocess.check_output(["git", "show", cls.BASE + ":" + cls.MANIFEST], cwd=cls.ROOT)
        if hashlib.sha256(raw).hexdigest() != cls.BASE_SHA256:
            raise AssertionError("Historical baseline hash mismatch")
        cls.baseline = validator.strict_load(raw)
        cls.manifest = validator.strict_load((cls.ROOT / cls.MANIFEST).read_bytes())
        cls.roster_bytes = (cls.ROOT / cls.ROSTER).read_bytes()

    @staticmethod
    def aliases(manifest):
        return {validator.normalize_name(alias["name"]): item["class_id"]
                for item in manifest["classes"] for alias in item["synonyms"]}

    def test_exact_alias_sets_and_counts(self):
        before, after = self.aliases(self.baseline), self.aliases(self.manifest)
        quarantined = {validator.normalize_name(name) for name in self.QUARANTINED}
        self.assertEqual(len(before), 83)
        self.assertTrue(quarantined <= before.keys())
        self.assertEqual(before.keys() - after.keys(), quarantined)
        self.assertEqual(after, {key: value for key, value in before.items() if key not in quarantined})
        self.assertEqual(sum(len(c["synonyms"]) for c in self.manifest["classes"]), 79)
        self.assertEqual(len(after), 79)
        self.assertEqual(len(validator.scientific_map(self.manifest)), 91)

    def test_only_approved_manifest_changes(self):
        expected = deepcopy(self.baseline)
        expected["manifest_version"] = "1.1.0"
        for item in expected["classes"]:
            item["synonyms"] = [a for a in item["synonyms"] if a["name"] not in self.QUARANTINED]
        self.assertEqual(self.manifest, expected)
        historical_roster = subprocess.check_output(
            ["git", "show", self.BASE + ":" + self.ROSTER], cwd=self.ROOT)
        self.assertEqual(self.roster_bytes, historical_roster)
        self.assertEqual(hashlib.sha256(self.roster_bytes).hexdigest(), self.manifest["roster_sha256"])

    def test_all_twelve_canonicals_resolve(self):
        species = self.baseline["classes"][:12]
        self.assertEqual(len(species), 12)
        for item in species:
            with self.subTest(name=item["scientific_name"]):
                self.assertEqual(validator.resolve_scientific_name(self.manifest, item["scientific_name"]),
                                 item["class_id"])

    def test_all_seventy_nine_eligible_aliases_resolve(self):
        expected = {key: value for key, value in self.aliases(self.baseline).items()
                    if key not in {validator.normalize_name(n) for n in self.QUARANTINED}}
        self.assertEqual(len(expected), 79)
        for name, class_id in expected.items():
            with self.subTest(name=name):
                self.assertEqual(validator.resolve_scientific_name(self.manifest, name), class_id)

    def test_normalized_quarantined_inputs_return_none(self):
        for name in self.QUARANTINED:
            for value in (name, name.upper(), "\t" + name.lower().replace(" ", "\u2003\n") + "\u00a0"):
                with self.subTest(name=name, variant=value):
                    self.assertIsNone(validator.resolve_scientific_name(self.manifest, value))
                    self.assertNotIn(validator.normalize_name(value), validator.scientific_map(self.manifest))

    def test_fixture_reintroduction_rejected_in_every_species(self):
        for name in self.QUARANTINED:
            for index in range(12):
                with self.subTest(name=name, index=index):
                    manifest, roster = fixture()
                    manifest["classes"][index]["synonyms"].append({"name": name, "ref_ids": ["synthetic_ref"]})
                    with self.assertRaises(validator.ContractError) as caught:
                        validator.validate_manifest(manifest, roster)
                    self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")

    def test_scientific_map_rejects_normalized_reintroduction(self):
        for name in self.QUARANTINED:
            for value in (name, name.upper(), "\t" + name.replace(" ", "\u00a0\n") + " "):
                for field in ("synonyms", "scientific_name"):
                    with self.subTest(name=name, value=value, field=field):
                        manifest, _ = fixture()
                        if field == "synonyms":
                            manifest["classes"][0][field].append({"name": value, "ref_ids": ["synthetic_ref"]})
                        else:
                            manifest["classes"][0][field] = value
                        with self.assertRaises(validator.ContractError) as caught:
                            validator.scientific_map(manifest)
                        self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")

    def test_canonical_reintroduction_is_rejected(self):
        for name in self.QUARANTINED:
            with self.subTest(name=name):
                manifest, roster = fixture()
                manifest["classes"][0]["scientific_name"] = name
                with self.assertRaises(validator.ContractError) as caught:
                    validator.validate_manifest(manifest, roster)
                self.assertEqual(caught.exception.code, "E_NAME_QUARANTINED")

    def test_authorship_is_not_removed(self):
        for name in self.QUARANTINED + ("Epipremnum aureum", "Sansevieria trifasciata"):
            with self.subTest(name=name):
                value = name + " L."
                self.assertTrue(validator.normalize_name(value).endswith(" l."))
                self.assertIsNone(validator.resolve_scientific_name(self.manifest, value))

    def test_no_normalized_collisions_and_protections_excluded(self):
        keys = [validator.normalize_name(name) for item in self.manifest["classes"][:12]
                for name in [item["scientific_name"]] + [a["name"] for a in item["synonyms"]]]
        self.assertEqual(len(keys), len(set(keys)))
        for item in self.manifest["classes"]:
            for name in [item["class_id"], item["display_name"]] + item["common_names"]:
                with self.subTest(name=name):
                    self.assertIsNone(validator.resolve_scientific_name(self.manifest, name))
        self.assertEqual(self.manifest["classes"][12:], self.baseline["classes"][12:])
        self.assertEqual([c["index"] for c in self.manifest["classes"]], list(range(14)))

    def test_real_validator_version_and_counts(self):
        result = validator.validate_manifest(self.manifest, self.roster_bytes)
        self.assertEqual(result["manifest_version"], "1.1.0")
        self.assertEqual((result["aliases"], result["scientific_keys"]), (79, 91))
        self.assertEqual((result["species"], result["protection"], result["classes"]), (12, 2, 14))

    def test_preliminary_version_is_no_longer_accepted(self):
        manifest, roster = fixture()
        manifest["manifest_version"] = "1.0.0"
        with self.assertRaises(validator.ContractError) as caught:
            validator.validate_manifest(manifest, roster)
        self.assertEqual(caught.exception.code, "E_VERSION")

    def test_taxonomy_evidence_preserves_conflicts_and_eligible_aliases(self):
        path = self.ROOT / "artifacts/bianchini/v2/evidence/P05-f1-man01/taxonomy-review.md"
        text = path.read_text(encoding="utf-8")
        blocks = re.findall(r"```json\n(.*?)\n```", text, re.S)
        self.assertEqual(len(blocks), 1)
        records = validator.strict_load((blocks[0] + "\n").encode("utf-8"))["quarantined_aliases"]
        self.assertEqual(len(records), 4)
        self.assertEqual({r["name"] for r in records}, set(self.QUARANTINED))
        authors = {"Aloe maculata": ("Forssk.", "All."), "Aloe variegata": ("Forssk.", "L."),
                   "Ficus clusiifolia": ("Summerh.", "Schott"),
                   "Ficus cordata": ("Kunth & C.D.Bouché", "Thunb.")}
        for record in records:
            with self.subTest(name=record["name"]):
                self.assertEqual(record["status"], "quarantined")
                self.assertEqual((record["related_authorship"], record["conflicting_authorship"]),
                                 authors[record["name"]])
                self.assertEqual(record["normalized_authorless_name"], validator.normalize_name(record["name"]))
                self.assertTrue(record["conflicting_taxon"])
                self.assertTrue(record["reason"])
                self.assertTrue(record["nomenclatural_synonymy_retained"])
                self.assertIsNone(record["scientific_resolution"])
                self.assertEqual(record["consulted_on"], "2026-09-11")
                self.assertEqual(len(record["source_urls"]), 2)
                self.assertTrue(all(url.startswith("https://powo.science.kew.org/taxon/")
                                    for url in record["source_urls"]))
                self.assertEqual(record["related_class_id"], self.aliases(self.baseline)[record["normalized_authorless_name"]])
        included = re.findall(r"^\| ([^|]+) \| [^|]+ \| [^|]+ \| incluído \|$", text, re.M)
        self.assertEqual(len(included), 79)
        self.assertEqual({validator.normalize_name(n) for n in included}, self.aliases(self.manifest).keys())


if __name__ == "__main__":
    unittest.main()
