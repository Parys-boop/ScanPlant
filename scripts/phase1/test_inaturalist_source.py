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
