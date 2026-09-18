"""P06 fixtures are synthetic and generated in memory; no network or image corpus."""

from copy import deepcopy
from io import BytesIO
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlsplit
from urllib.request import Request

from PIL import Image

import acquire_commons as acq


ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "docs/phase1/offline-class-manifest.v1.json"
CLASSES = json.loads(MANIFEST.read_text())["classes"]


def photo(color="green", exif=False):
    out = BytesIO()
    tags = Image.Exif()
    if exif:
        tags[315] = "Synthetic private camera owner"
        tags[34853] = {1: "N", 2: (1.0, 2.0, 3.0), 3: "E", 4: (4.0, 5.0, 6.0)}
    Image.new("RGB", (16, 12), color).save(out, format="JPEG", exif=tags)
    return out.getvalue()


def page(identifier=1, license_id="cc-by-4.0", author="Synthetic creator"):
    cc0 = license_id == "cc-zero"
    return {"pageid": identifier, "ns": 6, "title": f"File:Fixture {identifier}.jpg",
            "imageinfo": [{"url": f"https://upload.wikimedia.org/wikipedia/commons/a/ab/Fixture_{identifier}.jpg",
                           "descriptionurl": f"https://commons.wikimedia.org/wiki/File:Fixture_{identifier}.jpg",
                           "mime": "image/jpeg", "size": len(photo()), "timestamp": "2026-01-01T00:00:00Z",
                           "sha1": "synthetic-source-version",
                           "extmetadata": {"License": {"value": license_id},
                                           "LicenseShortName": {"value": "CC0" if cc0 else "CC BY 4.0"},
                                           "LicenseUrl": {"value": "https://creativecommons.org/" +
                                               ("publicdomain/zero/1.0/" if cc0 else "licenses/by/4.0/")},
                                           "Artist": {"value": author},
                                           "Attribution": {"value": "Synthetic credit"}}}]}


class FakeClient:
    def __init__(self, pages=None, bodies=None, failure=None):
        self.pages = pages or {None: {"query": {"pages": []}}}
        self.bodies = bodies or {}
        self.failure = failure
        self.calls = []
        self.downloads = []

    def search(self, query, continuation):
        self.calls.append((query, continuation))
        if self.failure:
            raise acq.AcquisitionError(self.failure)
        return deepcopy(self.pages[None if not continuation else continuation["gsroffset"]])

    def download(self, url):
        self.downloads.append(url)
        value = self.bodies.get(url, photo())
        if isinstance(value, Exception):
            raise value
        return value


class AcquisitionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="scanplant-p06-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_collect(self, client, cap=100, pages=2, classes=None):
        return acq.collect(classes or CLASSES, self.root, client, "fixture-digest", cap, pages,
                           now=lambda: "2026-09-18T12:00:00Z")

    def test_accepted_license_pairs(self):
        for license_id in ("cc-by-4.0", "cc-zero"):
            record = acq.inspect_page(page(license_id=license_id), CLASSES[0], "query", "time")
            self.assertEqual(record["license_id"], license_id)
            self.assertIsNone(acq.eligibility_reason(record))

    def test_observed_commons_cc0_deed_url(self):
        p = page(license_id="cc-zero")
        metadata = p["imageinfo"][0]["extmetadata"]
        metadata["License"]["value"] = "cc0"
        metadata["LicenseUrl"]["value"] = "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
        record = acq.inspect_page(p, CLASSES[0], "q", "t")
        self.assertIsNone(acq.eligibility_reason(record))
        for url in ("https://example.org/publicdomain/zero/1.0/deed.en",
                    "https://creativecommons.org/publicdomain/zero/1.0/deed.en?override=true",
                    "https://creativecommons.org/licenses/by-sa/4.0/deed.en"):
            record["license_url"] = url
            self.assertEqual(acq.eligibility_reason(record), "license_unproven")

    def test_reject_missing_incompatible_ambiguous_license_and_author(self):
        for field, value, reason in [
            ("License", "cc-by-sa-4.0", "license_unproven"),
            ("LicenseShortName", "CC BY 4.0 / GFDL", "license_unproven"),
            ("LicenseUrl", "https://creativecommons.org/licenses/by/3.0/", "license_unproven"),
            ("LicenseUrl", "", "license_unproven"),
            ("Artist", "", "author_missing"),
            ("Artist", "<span>Unknown author</span>", "author_missing"),
            ("Artist", "<span></span>", "author_missing"),
            ("Restrictions", "personality rights", "privacy_restriction"),
        ]:
            with self.subTest(field=field, value=value):
                p = page()
                p["imageinfo"][0]["extmetadata"][field] = {"value": value}
                self.assertEqual(acq.eligibility_reason(acq.inspect_page(p, CLASSES[0], "q", "t")), reason)

    def test_pagination_resume_dedup_id_and_hash_and_counts(self):
        first, second, third = page(1), page(2), page(3)
        third["imageinfo"][0]["extmetadata"]["License"]["value"] = "gfdl"
        client = FakeClient({None: {"query": {"pages": [first]},
                                        "continue": {"gsroffset": 1, "continue": "gsroffset||"}},
                             1: {"query": {"pages": [first, second, third]}}})
        report = self.run_collect(client)
        row = report["classes"][0]
        self.assertEqual((row["consulted"], row["accepted"], row["rejected"], row["failures"]), (3, 1, 2, 0))
        self.assertEqual(row["reasons"], {"duplicate_hash": 1, "license_unproven": 1})
        self.assertEqual(len(client.downloads), 2)
        self.assertTrue(client.calls[1][1]["gsroffset"] == 1)
        before = (self.root / "manifest.jsonl").read_bytes()
        resumed = FakeClient()
        self.run_collect(resumed)
        self.assertEqual(resumed.downloads, [])
        self.assertEqual(resumed.calls, [])
        self.assertEqual((self.root / "manifest.jsonl").read_bytes(), before)
        rows = [json.loads(line) for line in before.splitlines()]
        accepted = next(r for r in rows if r["result"] == "accepted")
        self.assertEqual(accepted["privacy_status"], "quarantined_pending_human_review")
        self.assertFalse(accepted["visual_review_performed"])
        self.assertEqual(acq.sha256((self.root / accepted["stored_path"]).read_bytes()), accepted["sha256"])
        self.assertEqual(len(report["classes"]), 14)
        self.assertEqual(report["classes"][-1]["consulted"], 0)
        self.assertEqual(report["classes"][-1]["status"], "not_applicable_automatic_query")

    def test_corrupt_stored_file_is_recovered(self):
        client = FakeClient({None: {"query": {"pages": [page()]}}})
        self.run_collect(client, classes=CLASSES[:1])
        record = json.loads((self.root / "manifest.jsonl").read_text().splitlines()[0])
        (self.root / record["stored_path"]).write_bytes(b"corrupt")
        self.run_collect(client, classes=CLASSES[:1])
        self.assertEqual(len(client.downloads), 2)
        self.assertEqual(acq.sha256((self.root / record["stored_path"]).read_bytes()), record["sha256"])

    def test_resume_only_reevaluates_proof_and_preserves_audit_without_new_searches(self):
        p = page(license_id="cc-zero")
        metadata = p["imageinfo"][0]["extmetadata"]
        metadata["License"]["value"] = "cc0"
        metadata["LicenseUrl"]["value"] = "http://creativecommons.org/publicdomain/zero/1.0/deed.en"
        client = FakeClient({None: {"query": {"pages": [p]}, "continue": {"gsroffset": 10}}})
        with patch.dict(acq.LICENSES, {"cc-by-4.0": acq.LICENSES["cc-by-4.0"]}, clear=True):
            first = self.run_collect(client, pages=1, classes=CLASSES[:1])
        self.assertEqual(first["classes"][0]["rejected"], 1)
        second = acq.collect(CLASSES[:1], self.root, client, "fixture-digest", resume_only=True)
        self.assertEqual(second["classes"][0]["accepted"], 1)
        self.assertEqual(second["classes"][0]["rejected"], 0)
        acq.collect(CLASSES[:1], self.root, client, "fixture-digest", resume_only=True)
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(len(client.downloads), 1)
        self.assertEqual(len((self.root / "manifest.jsonl").read_text().splitlines()), 2)

    def test_rechecked_license_over_cap_is_deferred_not_rejected(self):
        pages = [page(1), page(2, license_id="cc-zero")]
        client = FakeClient({None: {"query": {"pages": pages}}})
        with patch.dict(acq.LICENSES, {"cc-by-4.0": acq.LICENSES["cc-by-4.0"]}, clear=True):
            self.run_collect(client, classes=CLASSES[:1])
        report = acq.collect(CLASSES[:1], self.root, client, "fixture-digest", cap=1, resume_only=True)
        row = report["classes"][0]
        self.assertEqual((row["accepted"], row["rejected"], row["deferred"]), (1, 0, 1))
        self.assertEqual(len(client.downloads), 1)

    def test_retry_failed_download_on_resume(self):
        client = FakeClient({None: {"query": {"pages": [page()]}}},
                            {page()["imageinfo"][0]["url"]: acq.AcquisitionError("timeout")})
        report = self.run_collect(client, classes=CLASSES[:1])
        self.assertEqual(report["classes"][0]["failures"], 1)
        client.bodies.clear()
        report = self.run_collect(client, classes=CLASSES[:1])
        self.assertEqual(report["classes"][0]["accepted"], 1)
        self.assertEqual(report["classes"][0]["failures"], 1)  # Historical failure is preserved.

    def test_failure_and_zero_coverage(self):
        report = self.run_collect(FakeClient(failure="http_403"))
        self.assertEqual(report["classes"][0]["failures"], 1)
        self.assertEqual(report["classes"][1]["status"], "not_attempted")
        self.assertTrue(all(r["accepted"] == 0 for r in report["classes"]))
        self.assertEqual(report["status"], "blocked")
        resumed = acq.collect(CLASSES, self.root, FakeClient(), "fixture-digest", resume_only=True)
        self.assertEqual(resumed["status"], "blocked")

    def test_cap_and_resume_larger_cap(self):
        pages = [page(1), page(2), page(3)]
        client = FakeClient({None: {"query": {"pages": pages}}},
                            {p["imageinfo"][0]["url"]: photo(color) for p, color in zip(pages, ("red", "green", "blue"))})
        report = self.run_collect(client, cap=1, classes=CLASSES[:1])
        self.assertEqual(report["classes"][0]["accepted"], 1)
        self.assertEqual(len(client.downloads), 1)
        report = self.run_collect(client, cap=2, classes=CLASSES[:1])
        self.assertEqual(report["classes"][0]["accepted"], 2)
        for cap in (0, 101):
            with self.assertRaises(ValueError):
                self.run_collect(client, cap=cap)

    def test_hard_ceiling_of_one_hundred(self):
        pages = [page(i) for i in range(1, 102)]
        bodies = {}
        for i, p in enumerate(pages):
            buffer = BytesIO()
            Image.new("RGB", (4, 4), (i, 0, 0)).save(buffer, format="PNG")
            info = p["imageinfo"][0]
            info.update(url=info["url"].replace(".jpg", ".png"), mime="image/png", size=len(buffer.getvalue()))
            bodies[info["url"]] = buffer.getvalue()
        client = FakeClient({None: {"query": {"pages": pages}}}, bodies)
        report = self.run_collect(client, cap=100, classes=CLASSES[:1])
        self.assertEqual(report["classes"][0]["accepted"], 100)
        self.assertEqual(len(client.downloads), 100)
        with self.assertRaises(ValueError):
            self.run_collect(client, cap=99, classes=CLASSES[:1])

    def test_interruption_mid_page_does_not_redownload_registered_image(self):
        client = FakeClient({None: {"query": {"pages": [page(1), page(2)]}}})
        original = client.download

        def interrupted(url):
            if "Fixture_2" in url:
                raise KeyboardInterrupt()
            return original(url)

        client.download = interrupted
        with self.assertRaises(KeyboardInterrupt):
            self.run_collect(client, classes=CLASSES[:1])
        self.assertEqual(len(client.downloads), 1)
        client.download = original
        self.run_collect(client, classes=CLASSES[:1])
        self.assertEqual(len(client.downloads), 2)
        self.assertEqual(sum("Fixture_1" in url for url in client.downloads), 1)

    def test_page_budget_resumes_at_next_cursor(self):
        client = FakeClient({None: {"query": {"pages": [page(1)]}, "continue": {"gsroffset": 10}},
                            10: {"query": {"pages": [page(2)]}}})
        self.run_collect(client, pages=1, classes=CLASSES[:1])
        self.run_collect(client, pages=1, classes=CLASSES[:1])
        self.assertEqual(len(client.calls), 2)
        self.assertEqual(client.calls[1][1], {"gsroffset": 10})

    def test_empty_search_is_zero_not_failure(self):
        report = self.run_collect(FakeClient())
        for row in report["classes"]:
            self.assertEqual((row["consulted"], row["accepted"], row["rejected"], row["failures"]), (0, 0, 0, 0))
        self.assertEqual(report["classes"][0]["status"], "exhausted")

    def test_invalid_continuation_and_manifest_change_block(self):
        report = self.run_collect(FakeClient({None: {"query": {"pages": []}, "continue": {"prop": "private"}}}))
        self.assertEqual(report["classes"][0]["failure_reasons"], {"invalid_continuation": 1})
        with self.assertRaises(ValueError):
            acq.collect(CLASSES, self.root, FakeClient(), "different-manifest")

    def test_quarantine_symlink_refused(self):
        (self.root / "quarantine").symlink_to(ROOT, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.run_collect(FakeClient())

    def test_invalid_file_and_extension_and_size(self):
        for raw, url, mime, reason in [
            (b"not an image", "https://upload.wikimedia.org/x.jpg", "image/jpeg", "invalid_image"),
            (photo(), "https://upload.wikimedia.org/x.svg", "image/jpeg", "extension_not_allowed"),
            (photo(), "https://upload.wikimedia.org/x.png", "image/png", "file_type_mismatch"),
        ]:
            with self.subTest(reason=reason), self.assertRaises(acq.AcquisitionError) as caught:
                acq.sanitize_image(raw, url, mime)
            self.assertEqual(caught.exception.code, reason)
        with patch.object(acq, "MAX_BYTES", 10), self.assertRaises(acq.AcquisitionError):
            acq.sanitize_image(photo(), "https://upload.wikimedia.org/x.jpg", "image/jpeg")

    def test_exif_and_gps_removed(self):
        raw = photo(exif=True)
        with Image.open(BytesIO(raw)) as source:
            self.assertTrue(source.getexif().get_ifd(34853))
        sanitized, extension = acq.sanitize_image(raw, "https://upload.wikimedia.org/x.jpg", "image/jpeg")
        with Image.open(BytesIO(sanitized)) as result:
            self.assertEqual(dict(result.getexif()), {})
            self.assertNotIn("exif", result.info)
        self.assertNotIn(b"Synthetic private", sanitized)
        self.assertEqual(extension, ".jpg")

    def test_pixels_animation_and_truncated_image(self):
        raw = photo()
        with patch.object(acq, "MAX_PIXELS", 10), self.assertRaises(acq.AcquisitionError) as caught:
            acq.sanitize_image(raw, "https://upload.wikimedia.org/x.jpg", "image/jpeg")
        self.assertEqual(caught.exception.code, "pixel_or_frame_limit")
        with self.assertRaises(acq.AcquisitionError):
            acq.sanitize_image(raw[:-40], "https://upload.wikimedia.org/x.jpg", "image/jpeg")
        animated = BytesIO()
        Image.new("RGB", (4, 4), "red").save(animated, format="PNG", save_all=True,
                                            append_images=[Image.new("RGB", (4, 4), "blue")])
        with self.assertRaises(acq.AcquisitionError):
            acq.sanitize_image(animated.getvalue(), "https://upload.wikimedia.org/x.png", "image/png")

    def test_png_text_metadata_removed_and_orientation_preserved(self):
        from PIL.PngImagePlugin import PngInfo
        metadata = PngInfo()
        metadata.add_text("Location", "synthetic GPS location")
        buffer = BytesIO()
        Image.new("RGB", (3, 4)).save(buffer, format="PNG", pnginfo=metadata)
        raw, _ = acq.sanitize_image(buffer.getvalue(), "https://upload.wikimedia.org/x.png", "image/png")
        with Image.open(BytesIO(raw)) as decoded:
            self.assertEqual(decoded.info, {})
        buffer = BytesIO()
        exif = Image.Exif()
        exif[274] = 6
        Image.new("RGB", (3, 4)).save(buffer, format="JPEG", exif=exif)
        raw, _ = acq.sanitize_image(buffer.getvalue(), "https://upload.wikimedia.org/x.jpg", "image/jpeg")
        with Image.open(BytesIO(raw)) as decoded:
            self.assertEqual(decoded.size, (4, 3))

    def test_deterministic_jsonl(self):
        a = [{"sequence": 2, "b": 2, "a": "á"}, {"sequence": 1, "a": 0}]
        b = [{"a": 0, "sequence": 1}, {"a": "á", "b": 2, "sequence": 2}]
        self.assertEqual(acq.jsonl_bytes(a), acq.jsonl_bytes(b))
        self.assertEqual(acq.jsonl_bytes([]), b"")
        self.assertTrue(acq.jsonl_bytes(a).endswith(b"\n"))

    def test_external_dataset_only(self):
        with self.assertRaises(ValueError):
            acq.validate_output_root(ROOT / "datasets/p06", ROOT)

    def test_git_inventory_and_ignore(self):
        files = subprocess.check_output(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT).decode().splitlines()
        p06 = [p for p in files if "p06" in p.lower() or "commons" in p.lower()]
        self.assertFalse(any(Path(p).suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".part", ".tmp", ".jsonl"} for p in p06))
        for name in ("datasets/p06/file.jpg", "scripts/phase1/image.JPG", "artifacts/phase1/p06/manifest.jsonl", "cache/x.part"):
            result = subprocess.run(["git", "check-ignore", "-q", name], cwd=ROOT)
            self.assertEqual(result.returncode, 0, name)


class TransportTests(unittest.TestCase):
    class Response(BytesIO):
        def __init__(self, data, headers=None):
            super().__init__(data)
            self.headers = headers or {}

    def test_search_generator_namespace_and_continuation(self):
        with patch.object(acq, "urlopen", return_value=self.Response(b'{"batchcomplete":true}')) as opener:
            acq.CommonsClient(sleep=lambda _: None).search('"Testa alba"', {"gsroffset": 10, "continue": "gsroffset||"})
            params = parse_qs(urlsplit(opener.call_args.args[0].full_url).query)
            self.assertEqual(params["gsrnamespace"], ["6"])
            self.assertEqual(params["gsroffset"], ["10"])
            self.assertEqual(params["gsrsearch"], ['"Testa alba"'])
            self.assertIn("extmetadata", params["iiprop"][0])

    def test_redirect_cannot_change_host(self):
        with self.assertRaises(acq.AcquisitionError):
            acq.RestrictedRedirect().redirect_request(Request("https://upload.wikimedia.org/x.jpg"), None,
                                                      302, "", {}, "https://example.org/x.jpg")

    def test_transport_size_limit_and_invalid_json(self):
        with patch.object(acq, "urlopen", return_value=self.Response(b"too long")):
            with self.assertRaises(acq.AcquisitionError) as caught:
                acq.CommonsClient(sleep=lambda _: None)._get(acq.API, 3)
            self.assertEqual(caught.exception.code, "size_limit")
        with patch.object(acq, "urlopen", return_value=self.Response(b"x", {"Content-Length": "999999999"})):
            with self.assertRaises(acq.AcquisitionError):
                acq.CommonsClient(sleep=lambda _: None).download("https://upload.wikimedia.org/x.jpg")
        with patch.object(acq, "urlopen", return_value=self.Response(b"invalid JSON")):
            with self.assertRaises(acq.AcquisitionError) as caught:
                acq.CommonsClient(sleep=lambda _: None).search("query", None)
            self.assertEqual(caught.exception.code, "invalid_api_json")

    def test_timeout_retry_is_bounded(self):
        with patch.object(acq, "urlopen", side_effect=TimeoutError) as opener:
            client = acq.CommonsClient(timeout=1, retries=2, sleep=lambda _: None)
            with self.assertRaises(acq.AcquisitionError) as caught:
                client.download("https://upload.wikimedia.org/x.jpg")
            self.assertEqual(caught.exception.code, "timeout")
            self.assertEqual(opener.call_count, 3)
            self.assertEqual(opener.call_args.kwargs["timeout"], 1)
            self.assertIn("ScanPlant", opener.call_args.args[0].get_header("User-agent"))

    def test_http_permanent_and_transient(self):
        for status, attempts in ((403, 1), (429, 3), (503, 3)):
            with self.subTest(status=status), patch.object(acq, "urlopen", side_effect=HTTPError("url", status, "", {}, None)) as opener:
                with self.assertRaises(acq.AcquisitionError):
                    acq.CommonsClient(retries=2, sleep=lambda _: None).download("https://upload.wikimedia.org/x.jpg")
                self.assertEqual(opener.call_count, attempts)

    def test_download_host_restriction(self):
        for url in ("http://upload.wikimedia.org/x.jpg", "https://example.org/x.jpg", "file:///etc/passwd"):
            with self.assertRaises(acq.AcquisitionError):
                acq.CommonsClient().download(url)


if __name__ == "__main__":
    unittest.main()
