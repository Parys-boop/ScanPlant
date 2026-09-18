"""P06: bounded Commons acquisition of licensed candidates, all quarantined.

No training, botanical validation or visual privacy review is performed here.
State is single-writer, external to Git; manifest.jsonl is an audit projection.
"""

import argparse
from collections import Counter
from datetime import datetime, timezone
import fcntl
import hashlib
from html.parser import HTMLParser
from io import BytesIO
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import unquote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import warnings

from PIL import Image, ImageOps, UnidentifiedImageError

from validate_offline_manifest import strict_load, validate_manifest, ContractError


ROOT = Path(__file__).resolve().parents[2]
API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "ScanPlant-P06/1.0 (https://github.com/Parys-boop/ScanPlant; licensed-image-research)"
MAX_BYTES = 20 * 1024 * 1024
MAX_PIXELS = 25_000_000
LICENSES = {
    "cc-by-4.0": ({"CC BY 4.0"}, "https://creativecommons.org/licenses/by/4.0/"),
    "cc0": ({"CC0", "CC0 1.0"}, "https://creativecommons.org/publicdomain/zero/1.0/"),
    "cc-zero": ({"CC0", "CC0 1.0"}, "https://creativecommons.org/publicdomain/zero/1.0/"),
}
FORMATS = {"JPEG": ({".jpg", ".jpeg"}, "image/jpeg", ".jpg"),
           "PNG": ({".png"}, "image/png", ".png")}


class AcquisitionError(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
                       allow_nan=False) + "\n").encode("utf-8")


def jsonl_bytes(records):
    return b"".join(json_bytes(r) for r in sorted(records, key=lambda r: r["sequence"]))


def atomic_write(path, raw):
    """Only replace this tool's file; temporary bytes never go to the repository."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_symlink():
        raise ValueError("symlink_output")
    fd, temporary = tempfile.mkstemp(prefix=".p06-", suffix=".part", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def validate_output_root(output, repo=ROOT):
    resolved = output.expanduser().resolve()
    if resolved == repo or repo.resolve() in resolved.parents:
        raise ValueError("dataset_must_be_external")
    return resolved


def safe_url(url, host):
    parsed = urlsplit(url)
    if (parsed.scheme != "https" or parsed.netloc != host or not parsed.path.startswith("/")
            or parsed.fragment or parsed.username or parsed.password):
        raise AcquisitionError("unsafe_url")
    return url


class RestrictedRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        safe_url(newurl, urlsplit(request.full_url).netloc)
        return super().redirect_request(request, fp, code, msg, headers, newurl)


urlopen = build_opener(RestrictedRedirect()).open


class CommonsClient:
    def __init__(self, timeout=20, retries=2, sleep=time.sleep):
        if not 0 < timeout <= 60 or not 0 <= retries <= 3:
            raise ValueError("invalid_transport_limits")
        self.timeout, self.retries, self.sleep = timeout, retries, sleep

    def _get(self, url, limit):
        for attempt in range(self.retries + 1):
            self.sleep(0.25 if attempt == 0 else min(2 ** attempt, 8))
            try:
                request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json,image/jpeg,image/png"})
                with urlopen(request, timeout=self.timeout) as response:
                    length = response.headers.get("Content-Length")
                    if length and (not length.isdecimal() or int(length) > limit):
                        raise AcquisitionError("size_limit")
                    chunks, size = [], 0
                    started = time.monotonic()
                    while True:
                        if time.monotonic() - started > self.timeout:
                            raise TimeoutError()
                        chunk = response.read(min(65536, limit + 1 - size))
                        if not chunk:
                            break
                        chunks.append(chunk)
                        size += len(chunk)
                        if size > limit:
                            raise AcquisitionError("size_limit")
                    return b"".join(chunks)
            except HTTPError as error:
                code = f"http_{error.code}"
                error.close()
                if error.code not in {429, 500, 502, 503, 504}:
                    raise AcquisitionError(code) from None
            except TimeoutError:
                code = "timeout"
            except (URLError, ConnectionError, OSError):
                code = "network_error"
            if attempt == self.retries:
                raise AcquisitionError(code)

    def search(self, query, continuation):
        params = {"action": "query", "format": "json", "formatversion": 2,
                  "generator": "search", "gsrsearch": query, "gsrnamespace": 6,
                  "gsrlimit": 10, "gsrsort": "relevance", "prop": "imageinfo",
                  "iiprop": "url|mime|size|timestamp|sha1|extmetadata", "iilimit": 1,
                  "iiextmetadatalanguage": "en", "maxlag": 5}
        if continuation:
            if (set(continuation) - {"continue", "gsroffset"}
                    or type(continuation.get("gsroffset")) is not int):
                raise AcquisitionError("invalid_continuation")
            params.update(continuation)
        for attempt in range(self.retries + 1):
            try:
                value = json.loads(self._get(API + "?" + urlencode(params), 2 * 1024 * 1024))
                if not isinstance(value, dict):
                    raise ValueError()
            except (ValueError, UnicodeError):
                raise AcquisitionError("invalid_api_json") from None
            if value.get("error", {}).get("code") == "maxlag" and attempt < self.retries:
                self.sleep(5)
                continue
            if "error" in value or "warnings" in value:
                raise AcquisitionError("api_error")
            return value

    def download(self, url):
        return self._get(safe_url(url, "upload.wikimedia.org"), MAX_BYTES)


class PlainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_data(self, data):
        self.parts.append(data)


def plain(value):
    parser = PlainText()
    parser.feed(value)
    return " ".join(" ".join(parser.parts).split())


def inspect_page(page, item, query, timestamp):
    try:
        identifier = page["pageid"]
        if type(identifier) is not int or identifier <= 0 or page.get("ns") != 6:
            raise ValueError()
        info = (page.get("imageinfo") or [{}])[0]
        metadata = info.get("extmetadata", {})

        def field(key):
            value = metadata.get(key, {}).get("value", "")
            if not isinstance(value, str):
                raise ValueError()
            return value

        return {"class_id": item["class_id"], "query": query, "timestamp": timestamp,
                "page_id": identifier, "title": page["title"],
                "page_url": info.get("descriptionurl", ""), "file_url": info.get("url", ""),
                "author": plain(field("Artist")), "author_html": field("Artist"),
                "license": field("LicenseShortName"), "license_id": field("License"),
                "license_url": field("LicenseUrl"), "credit_html": field("Credit"),
                "attribution_html": field("Attribution"),
                "restrictions": field("Restrictions"), "copyrighted": field("Copyrighted"),
                "attribution_required": field("AttributionRequired"),
                "source_timestamp": info.get("timestamp"), "source_sha1": info.get("sha1"),
                "declared_mime": info.get("mime", ""), "declared_size": info.get("size"),
                "visual_review_performed": False, "botanical_validation_performed": False,
                "privacy_status": "unreviewed", "result": "pending", "reason": None}
    except (KeyError, TypeError, ValueError, AttributeError):
        raise AcquisitionError("invalid_api_page") from None


def eligibility_reason(record):
    license_id = record["license_id"]
    if license_id not in LICENSES:
        return "license_unproven"
    names, expected_url = LICENSES[license_id]
    # Localized deeds identify the same instrument; retain the exact source URL in the audit.
    url = record["license_url"].replace("http://", "https://", 1)
    url = re.sub(r"/deed\.[a-z]{2,3}(?:[_-][A-Za-z]{2,4})?/?$", "/", url).rstrip("/") + "/"
    if record["license"] not in names or url != expected_url:
        return "license_unproven"
    if not record["author"] or re.search(r"\b(unknown|anonymous|desconhecid[oa])\b", record["author"], re.I):
        return "author_missing"
    if record["restrictions"].strip():
        return "privacy_restriction"
    try:
        safe_url(record["page_url"], "commons.wikimedia.org")
        safe_url(record["file_url"], "upload.wikimedia.org")
    except (AcquisitionError, ValueError):
        return "unsafe_url"
    if Path(unquote(urlsplit(record["file_url"]).path)).suffix.lower() not in {".jpg", ".jpeg", ".png"}:
        return "extension_not_allowed"
    if type(record["declared_size"]) is not int or not 0 < record["declared_size"] <= MAX_BYTES:
        return "size_limit"
    return None


def sanitize_image(raw, url, mime):
    if not 0 < len(raw) <= MAX_BYTES:
        raise AcquisitionError("size_limit")
    extension = Path(unquote(urlsplit(url).path)).suffix.lower()
    if extension not in {".jpg", ".jpeg", ".png"}:
        raise AcquisitionError("extension_not_allowed")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(raw), formats=list(FORMATS)) as source:
                fmt = source.format
                suffixes, real_mime, suffix = FORMATS[fmt]
                if extension not in suffixes or mime != real_mime:
                    raise AcquisitionError("file_type_mismatch")
                if source.width * source.height > MAX_PIXELS or getattr(source, "n_frames", 1) != 1:
                    raise AcquisitionError("pixel_or_frame_limit")
                source.verify()
            with Image.open(BytesIO(raw), formats=[fmt]) as source:
                source.load()
                pixels = ImageOps.exif_transpose(source).convert("RGB")
                # Fresh pixel-only object: EXIF, GPS, XMP, comments and ICC never propagate.
                clean = Image.frombytes("RGB", pixels.size, pixels.tobytes())
                output = BytesIO()
                clean.save(output, format=fmt, **({"quality": 95} if fmt == "JPEG" else {}))
                result = output.getvalue()
                if len(result) > MAX_BYTES:
                    raise AcquisitionError("size_limit")
                return result, suffix
    except (UnidentifiedImageError, OSError, ValueError, SyntaxError,
            Image.DecompressionBombError, Image.DecompressionBombWarning):
        raise AcquisitionError("invalid_image") from None


def query_for(item):
    return '"' + item["scientific_name"] + '"' if item["kind"] == "species" else None


def latest_records(state):
    return {(r["class_id"], r["page_id"]): r for r in state["records"] if r.get("page_id") is not None}


def stored_valid(root, record):
    relative = record.get("stored_path", "")
    if not re.fullmatch(r"quarantine/[0-9a-f]{64}\.(jpg|png)", relative):
        return False
    path = root / relative
    return (path.is_file() and not path.is_symlink() and path.stat().st_size <= MAX_BYTES
            and sha256(path.read_bytes()) == record["sha256"])


def coverage(state, classes, root, cap, max_pages, blocked=False):
    current = latest_records(state)
    rows = []
    for item in classes:
        class_id = item["class_id"]
        records = [r for (c, _), r in current.items() if c == class_id]
        failures = [r for r in state["records"] if r["class_id"] == class_id and r["result"] == "failed"]
        accepted = [r for r in records if r["result"] == "accepted" and stored_valid(root, r)]
        rejected = [r for r in records if r["result"] == "rejected"]
        deferred = [r for r in records if r["result"] == "deferred"]
        rows.append({"class_id": class_id, "name": item["scientific_name"] or item["display_name"],
                     "query": query_for(item), "status": state["searches"][class_id]["status"],
                     "pages_fetched": state["searches"][class_id]["pages_fetched"],
                     "consulted": len(records), "accepted": len(accepted), "rejected": len(rejected),
                     "deferred": len(deferred),
                     "failures": len(failures), "quarantined": len(accepted), "usable": 0,
                     "reasons": dict(sorted(Counter(r["reason"] for r in rejected).items())),
                     "deferred_reasons": dict(sorted(Counter(r["reason"] for r in deferred).items())),
                     "failure_reasons": dict(sorted(Counter(r["reason"] for r in failures).items()))})
    return {"schema_version": 1, "status": "blocked" if blocked else "bounded_run_finished",
            "canonical_manifest_sha256": state["canonical_manifest_sha256"],
            "manifest_jsonl_sha256": sha256(jsonl_bytes(state["records"])),
            "accepted_cap_per_class": cap, "page_budget_per_class_per_run": max_pages,
            "classes": rows, "visual_review_performed": False, "training_ready": False,
            "failure_count_semantics": "cumulative_failed_attempts_including_recovered",
            "accepted_semantics": "license_and_file_checks_passed; quarantined; not_usable"}


def collect(classes, output, client, manifest_digest, cap=100, max_pages=2, now=utc_now, resume_only=False):
    if type(cap) is not int or not 1 <= cap <= 100 or not 1 <= max_pages <= 100:
        raise ValueError("invalid_acquisition_limits")
    output = validate_output_root(output)
    output.mkdir(parents=True, exist_ok=True)
    for child in ("state.json", "manifest.jsonl", "coverage.json", "quarantine", ".lock"):
        if (output / child).is_symlink():
            raise ValueError("symlink_output")
    with (output / ".lock").open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("dataset_in_use") from None
        return _collect_locked(classes, output, client, manifest_digest, cap, max_pages, now, resume_only)


def _collect_locked(classes, output, client, manifest_digest, cap, max_pages, now, resume_only):
    state_path = output / "state.json"
    if state_path.exists():
        state = json.loads(state_path.read_bytes())
        if state["schema_version"] != 1 or state["canonical_manifest_sha256"] != manifest_digest:
            raise ValueError("state_manifest_mismatch")
    else:
        if resume_only:
            raise ValueError("resume_requires_existing_state")
        state = {"schema_version": 1, "canonical_manifest_sha256": manifest_digest,
                 "records": [], "searches": {c["class_id"]: {
                     "continuation": None, "exhausted": False, "pages_fetched": 0,
                     "status": "not_attempted" if query_for(c) else "not_applicable_automatic_query"}
                     for c in classes}}
    blocked = False

    def save():
        atomic_write(state_path, json_bytes(state))
        atomic_write(output / "manifest.jsonl", jsonl_bytes(state["records"]))
        atomic_write(output / "coverage.json", json_bytes(coverage(state, classes, output, cap, max_pages, blocked)))

    def append(record):
        record["sequence"] = len(state["records"]) + 1
        state["records"].append(record)
        save()

    def accepted_for(class_id):
        return sum(r["result"] == "accepted" and stored_valid(output, r)
                   for (c, _), r in latest_records(state).items() if c == class_id)

    def process(record):
        record = dict(record, timestamp=now())
        for key in ("sequence", "stored_path", "sha256", "source_sha256", "transformation"):
            record.pop(key, None)
        reason = eligibility_reason(record)
        valid = [r for r in latest_records(state).values()
                 if r["result"] == "accepted" and stored_valid(output, r)]
        if not reason and any(r["page_id"] == record["page_id"] and r["class_id"] != record["class_id"]
                              and r["result"] in {"accepted", "rejected"}
                              for r in latest_records(state).values()):
            reason = "duplicate_id"
        if reason:
            record.update(result="rejected", reason=reason)
        else:
            try:
                raw = client.download(record["file_url"])
                clean, extension = sanitize_image(raw, record["file_url"], record["declared_mime"])
                record.update(source_sha256=sha256(raw), sha256=sha256(clean))
                if any(r["sha256"] == record["sha256"] or r["source_sha256"] == record["source_sha256"] for r in valid):
                    record.update(result="rejected", reason="duplicate_hash")
                else:
                    relative = "quarantine/" + record["sha256"] + extension
                    atomic_write(output / relative, clean)
                    record.update(result="accepted", reason=None, stored_path=relative,
                                  privacy_status="quarantined_pending_human_review",
                                  transformation="EXIF orientation applied; RGB re-encoded; all metadata removed")
            except AcquisitionError as error:
                rejected = error.code in {"size_limit", "invalid_image", "pixel_or_frame_limit",
                                          "file_type_mismatch", "extension_not_allowed", "unsafe_url"}
                record.update(result="rejected" if rejected else "failed", reason=error.code)
        append(record)

    if any(accepted_for(c["class_id"]) > cap for c in classes):
        raise ValueError("cap_below_existing_accepted_count")
    save()  # Rebuild derived files if interrupted after the last state write.
    for item in classes:
        class_id, query = item["class_id"], query_for(item)
        search = state["searches"][class_id]
        if not query:
            continue
        # Keep prior attempts; reevaluate license rejections only when current proof now passes.
        for (c, _), record in list(latest_records(state).items()):
            if c == class_id and (record["result"] in {"failed", "deferred"} or
                                 (record["result"] == "accepted" and not stored_valid(output, record)) or
                                 (record["result"] == "rejected" and record["reason"] == "license_unproven"
                                  and eligibility_reason(record) != "license_unproven")):
                if accepted_for(class_id) < cap or eligibility_reason(record) is not None:
                    process(record)
                elif record["result"] != "deferred":
                    append(dict(record, timestamp=now(), result="deferred", reason="accepted_cap_reached"))
        if accepted_for(class_id) >= cap:
            search["status"] = "accepted_cap_reached"
            continue
        if search["exhausted"] or resume_only:
            continue
        for _ in range(max_pages):
            try:
                response = client.search(query, search["continuation"])
                pages = response.get("query", {}).get("pages", [])
                if not isinstance(pages, list) or any(not isinstance(p, dict) for p in pages):
                    raise AcquisitionError("invalid_api_pages")
                continuation = response.get("continue")
                if continuation is not None and (not isinstance(continuation, dict)
                        or set(continuation) - {"continue", "gsroffset"}
                        or type(continuation.get("gsroffset")) is not int
                        or continuation["gsroffset"] <= (search["continuation"] or {}).get("gsroffset", -1)):
                    raise AcquisitionError("invalid_continuation")
                search["pages_fetched"] += 1
                search["status"] = "searching"
                for page in pages:
                    if accepted_for(class_id) >= cap:
                        break  # Keep this page's cursor so increasing the cap resumes remaining entries.
                    key = (class_id, page.get("pageid"))
                    previous = latest_records(state).get(key)
                    if previous is not None:
                        continue
                    process(inspect_page(page, item, query, now()))
                if accepted_for(class_id) >= cap:
                    search["status"] = "accepted_cap_reached"
                    break
                search["continuation"] = continuation
                search["exhausted"] = continuation is None
                search["status"] = "exhausted" if continuation is None else "page_budget_reached"
                save()
                if search["exhausted"]:
                    break
            except AcquisitionError as error:
                search["status"] = "blocked"
                blocked = True
                append({"class_id": class_id, "query": query, "page_id": None,
                        "timestamp": now(), "result": "failed", "reason": error.code,
                        "stage": "search", "title": None, "page_url": None, "file_url": None,
                        "author": None, "license": None, "license_id": None})
                break  # A failing API stops this run, without claiming other classes were searched.
        if blocked:
            break
    blocked = (blocked or any(r["result"] == "failed" for r in latest_records(state).values())
               or any(s["status"] == "blocked" for s in state["searches"].values()))
    save()
    return coverage(state, classes, output, cap, max_pages, blocked)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=ROOT / "docs/phase1/offline-class-manifest.v1.json")
    parser.add_argument("--roster", type=Path, default=ROOT / "artifacts/bianchini/v2/evidence/P05-f1-man01/approved-species-roster.json")
    parser.add_argument("--output", type=Path, default=Path.home() / "datasets/scanplant/p06")
    parser.add_argument("--max-accepted", type=int, default=100)
    parser.add_argument("--max-pages", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=20)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--resume-only", action="store_true", help="Reprocess eligible pending records without new searches")
    args = parser.parse_args(argv)
    try:
        raw = args.manifest.read_bytes()
        manifest = strict_load(raw)
        validate_manifest(manifest, args.roster.read_bytes())
        report = collect(manifest["classes"], args.output,
                         CommonsClient(args.timeout, args.retries), sha256(raw),
                         args.max_accepted, args.max_pages, resume_only=args.resume_only)
    except (OSError, ValueError, KeyError, ContractError):
        print("P06: invalid configuration, state or local IO; no sensitive diagnostic emitted", file=sys.stderr)
        return 2
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    return 1 if report["status"] == "blocked" else 0


if __name__ == "__main__":
    sys.exit(main())
