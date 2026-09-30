"""P07: read-only source reconciliation, deterministic triage and reviewed decisions.

No network, image writes, automatic approval, or P06 mutation. Pillow==12.3.0.
Human decisions are inputs; agent proposals can only create explicitly draft results.
"""
import argparse
from collections import Counter
from contextlib import contextmanager
from datetime import datetime
import fcntl
import hashlib
from io import BytesIO
from itertools import combinations
import json
import math
import os
from pathlib import Path
import platform
import re
import stat
import sys
import tempfile
import warnings

import PIL
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
CLASS_MANIFEST = ROOT / "docs/phase1/offline-class-manifest.v1.json"
STATES = ("approved_for_dataset", "rejected_quality", "rejected_duplicate",
          "rejected_privacy", "rejected_label", "needs_botanical_review", "needs_human_review")
IDS = [f"Q{i:02}" for i in range(1, 18)]
RUN = "p06-recovery-20260928"
SHA = re.compile(r"[0-9a-f]{64}")
PRIVACY = ("people", "faces", "plates", "vehicles", "residences", "documents", "other_identifiable")
VISUAL = ("framing", "occlusion", "multiple_species", "representativeness")
GATES = ("integrity", "provenance", "quality", "privacy", "uniqueness", "botanical_label")
METHOD = {
    "algorithm": "p07-triage-v1", "pillow": "12.3.0", "luminance_size": [256, 256],
    "resize": "LANCZOS", "laplacian": "4c-left-right-up-down; interior; population_variance",
    "dhash": "horizontal-v1; L 9x8; right>left; row-major; first-bit-most-significant",
    "thresholds": {"minimum_side_lt": 224, "aspect_gt": 3.0, "mean_lt": 40,
                   "mean_gt": 215, "dark_lte": 15, "bright_gte": 240,
                   "extreme_fraction_gte": 0.25, "laplacian_variance_lt": 100,
                   "near_distance_lte": 6, "borderline_distance_lte": 10}}
RECORD_KEYS = set("attribution_html attribution_required author author_html botanical_validation_performed class_id copyrighted credit_html declared_mime declared_size file_url license license_id license_url page_id page_url privacy_status query reason restrictions result sequence sha256 source_sha1 source_sha256 source_timestamp stored_path timestamp title transformation visual_review_performed".split())
P06_DECISION_KEYS = set("assistant_visual_review_performed botanical_assessment class_id decision decision_id expert_taxonomic_confirmation manifest_attribution_license_origin_coherent original_resolution_review physical_location privacy_assessment quality_and_framing rationale review_id sha256 stored_path training_authorized".split())


class CurationError(ValueError):
    """Safe diagnostics contain stable codes, never private input values."""


def require(condition, code):
    if not condition:
        raise CurationError(code)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode("utf-8")


def strict_load(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate_json_key")
            result[key] = value
        return result
    def constant(_):
        raise CurationError("nonfinite_json")
    try:
        require(type(raw) is bytes and not raw.startswith(b"\xef\xbb\xbf"), "json_encoding")
        require(b"\r" not in raw and raw.endswith(b"\n"), "json_utf8_lf")
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)
        # Reject exponent overflow too (1e999 is not a parse_constant token).
        def finite(v):
            if type(v) is float:
                require(math.isfinite(v), "nonfinite_json")
            elif type(v) is dict:
                for x in v.values():
                    finite(x)
            elif type(v) is list:
                for x in v:
                    finite(x)
        finite(value)
        return value
    except (UnicodeError, json.JSONDecodeError):
        raise CurationError("invalid_json") from None


def obj(value, keys):
    require(type(value) is dict and set(value) == set(keys), "object_fields")


def text(value):
    require(type(value) is str and bool(value.strip()), "nonempty_text")


def no_symlinks(path):
    path = Path(os.path.abspath(path))
    require(not any(p.is_symlink() for p in (path, *path.parents)), "symlink")
    return path


def read_file(path):
    path = no_symlinks(path)
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, "rb") as stream:
        require(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), "not_regular_file")
        return stream.read()


def tree_hashes(root):
    root = no_symlinks(root)
    require(root.is_dir(), "source_missing")
    result = {}
    for path in sorted(root.rglob("*")):
        no_symlinks(path)
        if path.is_dir():
            continue
        result[path.relative_to(root).as_posix()] = sha(read_file(path))
    return result


def reconcile(source, class_manifest=CLASS_MANIFEST):
    """Reconcile all P06 witnesses before any image decoding."""
    source = no_symlinks(source)
    before = tree_hashes(source)
    load = lambda name: strict_load(read_file(source / name))
    inventory = load("inventory.json")
    require(type(inventory) is list, "inventory_type")
    inv = {}
    for item in inventory:
        obj(item, {"path", "bytes", "sha256"})
        path = item["path"]
        require(type(path) is str and path not in inv and path in before, "inventory_set")
        require(type(item["bytes"]) is int and item["bytes"] == (source / path).stat().st_size,
                "inventory_size")
        require(item["sha256"] == before[path], "inventory_hash")
        inv[path] = item["sha256"]
    require(set(inv) == set(before) - {"inventory.json", "SHA256SUMS"}, "inventory_coverage")
    checksums = {}
    for line in read_file(source / "SHA256SUMS").decode("ascii").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        require(match is not None, "checksum_syntax")
        digest, name = match.groups()
        require(name not in checksums and before.get(name) == digest, "checksum_mismatch")
        checksums[name] = digest
    require(set(checksums) == set(before) - {"SHA256SUMS"}, "checksum_coverage")
    classes_raw = read_file(class_manifest)
    canonical = strict_load(classes_raw)
    require(canonical["manifest_version"] == "1.1.0", "class_manifest_version")
    classes = [{"class_id": c["class_id"], "name": c["scientific_name"] or c["display_name"]}
               for c in canonical["classes"]]
    class_ids = {c["class_id"] for c in classes}
    require(len(classes) == len(class_ids) == 14, "class_set")
    state = load("state.json")
    obj(state, {"schema_version", "canonical_manifest_sha256", "records", "searches"})
    require(type(state["schema_version"]) is int and state["schema_version"] == 1, "state_schema")
    require(state["canonical_manifest_sha256"] == sha(classes_raw), "class_manifest_hash")
    manifest = [strict_load(line + b"\n") for line in read_file(source / "manifest.jsonl").splitlines()]
    require(type(state["records"]) is list and state["records"] == manifest, "state_manifest_mismatch")
    require(type(state["searches"]) is dict and set(state["searches"]) == class_ids, "search_classes")
    for search in state["searches"].values():
        obj(search, {"continuation", "exhausted", "pages_fetched", "status"})
        require(type(search["exhausted"]) is bool and type(search["pages_fetched"]) is int,
                "search_types")
        if search["continuation"] is not None:
            obj(search["continuation"], {"continue", "gsroffset"})
    accepted = {}
    for i, record in enumerate(manifest, 1):
        require(type(record) is dict and set(record) <= RECORD_KEYS, "record_fields")
        require(type(record.get("sequence")) is int and record["sequence"] == i, "sequence")
        require(record.get("class_id") in class_ids, "record_class")
        if record.get("result") != "accepted":
            continue
        obj(record, RECORD_KEYS)
        digest = record["sha256"]
        require(type(digest) is str and SHA.fullmatch(digest) and digest not in accepted, "accepted_hash_set")
        require(record["stored_path"] == f"quarantine/{digest}.jpg", "stored_path")
        require(before.get(record["stored_path"]) == digest, "image_hash")
        for key in ("license", "license_id", "license_url", "page_url", "file_url", "author"):
            text(record[key])
        accepted[digest] = record
    actual = {p for p in before if p.startswith("quarantine/")}
    require(len(accepted) == 17 and actual == {r["stored_path"] for r in accepted.values()}, "image_set_17")
    coverage = load("coverage.json")
    obj(coverage, set("accepted_cap_per_class accepted_semantics canonical_manifest_sha256 classes failure_count_semantics manifest_jsonl_sha256 page_budget_per_class_per_run schema_version status training_ready visual_review_performed".split()))
    require(coverage["canonical_manifest_sha256"] == sha(classes_raw) and
            coverage["manifest_jsonl_sha256"] == before["manifest.jsonl"], "coverage_hash")
    require(coverage["training_ready"] is False, "source_training_flag")
    require(type(coverage["classes"]) is list and len(coverage["classes"]) == 14, "coverage_classes")
    seen_classes = set()
    for c in coverage["classes"]:
        obj(c, set("accepted class_id consulted deferred deferred_reasons failure_reasons failures name pages_fetched quarantined query reasons rejected status usable".split()))
        require(c["class_id"] in class_ids and c["class_id"] not in seen_classes, "coverage_class_set")
        seen_classes.add(c["class_id"])
        count = sum(r["class_id"] == c["class_id"] for r in accepted.values())
        require(type(c["accepted"]) is int and c["accepted"] == count and
                type(c["quarantined"]) is int and c["quarantined"] == count and
                type(c["usable"]) is int and c["usable"] == 0, "coverage_counts")
    prior = load("review-2026-09-28/human-decisions.json")
    obj(prior, set("confirmation_source decisions human_grouped_decision_confirmed notice p06_status recorded_at release_status remote_metadata_requeried review_method run_id schema_version totals training_ready".split()))
    require(prior["run_id"] == RUN and prior["human_grouped_decision_confirmed"] is True and
            prior["training_ready"] is False, "prior_run")
    require(type(prior["decisions"]) is list and len(prior["decisions"]) == 17, "prior_count")
    records, seen = [], set()
    for i, d in enumerate(sorted(prior["decisions"], key=lambda x: x["decision_id"]), 1):
        obj(d, P06_DECISION_KEYS)
        require(d["decision_id"] == f"Q{i:02}" and d["review_id"] == f"R{i:02}", "qr_mapping")
        digest = d["sha256"]
        require(digest in accepted and digest not in seen, "decision_hash_set")
        seen.add(digest)
        r = accepted[digest]
        require(d["class_id"] == r["class_id"] and d["stored_path"] == r["stored_path"], "decision_identity")
        require(d["decision"] in {"aprovar_para_curadoria_futura", "manter_em_quarentena", "rejeitar"}, "prior_decision")
        require(d["training_authorized"] is False and d["physical_location"] == "quarantine", "prior_quarantine")
        records.append({"id": d["decision_id"], "review_id": d["review_id"], "sha256": digest,
                        "class_id": d["class_id"], "stored_path": d["stored_path"],
                        "prior_p06_decision": d["decision"], "provenance": r})
    require(Counter(d["decision"] for d in prior["decisions"]) == prior["totals"], "prior_counts")
    metadata = load("run-metadata.json")
    require(metadata.get("run_id") == RUN and metadata.get("totals", {}).get("accepted") == 17,
            "metadata_run")
    return before, records, classes


def flags_for(width, height, mean, dark, bright, variance):
    checks = [(min(width, height) < 224, "small_dimension"),
              (max(width, height) / min(width, height) > 3, "extreme_aspect"),
              (mean < 40, "dark_mean"), (mean > 215, "bright_mean"),
              (dark >= .25, "dark_fraction"), (bright >= .25, "bright_fraction"),
              (variance < 100, "low_laplacian_variance")]
    return [name for condition, name in checks if condition]


def laplacian_variance(pixels, width, height):
    require(width >= 3 and height >= 3 and len(pixels) == width * height, "laplacian_shape")
    values = [4 * pixels[y * width + x] - pixels[y * width + x - 1] - pixels[y * width + x + 1]
              - pixels[(y - 1) * width + x] - pixels[(y + 1) * width + x]
              for y in range(1, height - 1) for x in range(1, width - 1)]
    n, total, squares = len(values), sum(values), sum(v * v for v in values)
    return (squares * n - total * total) / (n * n)


def dhash(image):
    pixels = list(image.convert("L").resize((9, 8), Image.Resampling.LANCZOS).get_flattened_data())
    bits = 0
    for y in range(8):
        for x in range(8):
            bits = (bits << 1) | (pixels[y * 9 + x + 1] > pixels[y * 9 + x])
    return f"{bits:016x}"


def metrics(raw):
    require(PIL.__version__ == "12.3.0", "pillow_version")
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(BytesIO(raw)) as check:
                require(check.format == "JPEG" and getattr(check, "n_frames", 1) == 1, "image_format")
                check.verify()
            with Image.open(BytesIO(raw)) as image:
                image.load()
                width, height = image.size
                gray = image.convert("L").resize((256, 256), Image.Resampling.LANCZOS)
                pixels = list(gray.get_flattened_data())
                mean = sum(pixels) / len(pixels)
                dark = sum(x <= 15 for x in pixels) / len(pixels)
                bright = sum(x >= 240 for x in pixels) / len(pixels)
                variance = laplacian_variance(pixels, 256, 256)
                return {"decode": "ok", "format": image.format, "width": width, "height": height,
                        "aspect": max(width, height) / min(width, height), "mean_luminance": mean,
                        "dark_fraction": dark, "bright_fraction": bright,
                        "laplacian_variance": variance, "dhash64": dhash(image),
                        "flags": flags_for(width, height, mean, dark, bright, variance)}
    except (OSError, ValueError, Image.DecompressionBombWarning, Image.DecompressionBombError):
        return {"decode": "failed", "format": None, "width": None, "height": None, "aspect": None,
                "mean_luminance": None, "dark_fraction": None, "bright_fraction": None,
                "laplacian_variance": None, "dhash64": None, "flags": ["decode_failed"]}


def compare_pair(a, b):
    ah, bh = a["technical"]["dhash64"], b["technical"]["dhash64"]
    distance = None if ah is None or bh is None else (int(ah, 16) ^ int(bh, 16)).bit_count()
    if a["sha256"] == b["sha256"]:
        signal = "exact_duplicate"
    elif distance is None:
        signal = "needs_human_review"
    else:
        signal = ("near_duplicate_candidate" if distance <= 6 else
                  "borderline_visual_pair" if distance <= 10 else "no_algorithmic_signal")
    return {"pair_id": a["id"] + "-" + b["id"], "left": a["id"], "right": b["id"],
            "hamming_distance": distance, "signal": signal}


def analyze(source, class_manifest=CLASS_MANIFEST):
    before, records, classes = reconcile(source, class_manifest)
    for record in records:
        raw = read_file(Path(source) / record["stored_path"])
        require(sha(raw) == record["sha256"], "image_changed_before_decode")
        record["technical"] = metrics(raw)
    pairs = [compare_pair(a, b) for a, b in combinations(records, 2)]
    require(len(pairs) == 136, "pair_count")
    require(tree_hashes(source) == before, "source_changed")
    return {"schema_version": 1, "run_id": RUN, "method": METHOD,
            "python": platform.python_version(), "source_hashes": before,
            "classes": classes, "records": records, "pairs": pairs,
            "comparison_count": 136, "training_sufficiency": "not_demonstrated"}


def validate_decisions(value, analysis, *, draft=False):
    obj(value, {"schema_version", "run_id", "analysis_sha256", "authority", "decisions"})
    require(type(value["schema_version"]) is int and value["schema_version"] == 1, "decision_schema")
    require(value["run_id"] == RUN and value["analysis_sha256"] == sha(encode(analysis)), "decision_analysis")
    require(value["authority"] == ("agent_proposal" if draft else "human"), "human_authority_required")
    entries = value["decisions"]
    require(type(entries) is list and len(entries) == 17, "decision_count")
    fields = {"id", "review_id", "sha256", "class_id", "state", "reviewer_id", "reviewer_role",
              "timestamp", "rationale", "visual", "privacy", "botanical", "gates",
              "pair_reviews", "duplicate_of", "original_resolution_review"}
    result = []
    for index, d in enumerate(sorted(entries, key=lambda x: x.get("id", ""))):
        obj(d, fields)
        record = analysis["records"][index]
        require(all(d[k] == record[k] for k in ("id", "review_id", "sha256", "class_id")), "decision_identity")
        require(type(d["state"]) is str and d["state"] in STATES, "decision_state")
        require(d["reviewer_role"] == ("agent" if draft else "human"), "reviewer_role")
        for key in ("reviewer_id", "timestamp", "rationale"):
            text(d[key])
        try:
            stamp = datetime.fromisoformat(d["timestamp"])
            require(stamp.utcoffset() is not None, "timestamp_timezone")
        except ValueError:
            raise CurationError("timestamp") from None
        require(type(d["original_resolution_review"]) is bool, "original_review_type")
        obj(d["visual"], VISUAL)
        for v in d["visual"].values():
            text(v)
        obj(d["privacy"], {*PRIVACY, "assessment"})
        for key in PRIVACY:
            require(d["privacy"][key] in {"not_observed", "present", "uncertain"}, "privacy_value")
        text(d["privacy"]["assessment"])
        obj(d["botanical"], {"status", "evidence", "expert_confirmation"})
        require(d["botanical"]["status"] in {"sufficient", "insufficient", "incompatible"}, "botanical_status")
        text(d["botanical"]["evidence"])
        require(type(d["botanical"]["expert_confirmation"]) is bool, "botanical_type")
        obj(d["gates"], GATES)
        require(all(type(v) is str and v in {"sufficient", "insufficient", "pending"}
                    for v in d["gates"].values()), "gate_values")
        applicable = {p["pair_id"] for p in analysis["pairs"] if d["id"] in (p["left"], p["right"])
                      and p["signal"] != "no_algorithmic_signal"}
        require(type(d["pair_reviews"]) is list, "pair_reviews")
        possible = {p["pair_id"] for p in analysis["pairs"] if d["id"] in (p["left"], p["right"])}
        reviewed = set()
        for p in d["pair_reviews"]:
            obj(p, {"pair_id", "outcome", "rationale"})
            require(p["pair_id"] in possible and p["pair_id"] not in reviewed, "pair_review_set")
            reviewed.add(p["pair_id"])
            require(p["outcome"] in {"distinct", "duplicate", "pending"}, "pair_outcome")
            text(p["rationale"])
        require(applicable <= reviewed, "missing_pair_review")
        require(d["duplicate_of"] is None or (d["duplicate_of"] in IDS and d["duplicate_of"] != d["id"]), "duplicate_reference")
        if d["state"] == "approved_for_dataset":
            require(not draft, "no_agent_approval")
            require(d["original_resolution_review"] and record["technical"]["decode"] == "ok", "approval_decode_review")
            require(all(v == "sufficient" for v in d["gates"].values()) and
                    d["botanical"]["status"] == "sufficient", "approval_gates")
            require(all(d["privacy"][k] == "not_observed" for k in PRIVACY), "approval_privacy")
            require(all(p["outcome"] == "distinct" for p in d["pair_reviews"]), "approval_pairs")
        if d["state"] == "rejected_duplicate":
            require(d["duplicate_of"] is not None, "duplicate_reference_required")
            pair_id = "-".join(sorted((d["id"], d["duplicate_of"])))
            require(d["gates"]["uniqueness"] == "insufficient" and
                    any(p["pair_id"] == pair_id and p["outcome"] == "duplicate"
                        for p in d["pair_reviews"]), "duplicate_pair_evidence")
        else:
            require(d["duplicate_of"] is None, "unexpected_duplicate_reference")
        if d["state"] == "needs_botanical_review":
            require(d["botanical"]["status"] == "insufficient", "botanical_pending")
        if d["state"] == "rejected_quality":
            require(d["gates"]["quality"] == "insufficient", "quality_rejection_evidence")
        if d["state"] == "rejected_privacy":
            require(d["gates"]["privacy"] == "insufficient" and
                    any(d["privacy"][k] != "not_observed" for k in PRIVACY), "privacy_rejection_evidence")
        if d["state"] == "rejected_label":
            require(d["gates"]["botanical_label"] == "insufficient" and
                    d["botanical"]["status"] == "incompatible", "label_rejection_evidence")
        if d["state"] == "needs_human_review":
            require("pending" in d["gates"].values(), "human_pending_reason")
        result.append(d)
    by_id = {d["id"]: d for d in result}
    for d in result:
        if d["state"] == "rejected_duplicate":
            require(by_id[d["duplicate_of"]]["state"] in
                    {"approved_for_dataset", "needs_botanical_review", "needs_human_review"}, "duplicate_keeper")
        for p in d["pair_reviews"]:
            other = next(q for q in p["pair_id"].split("-") if q != d["id"])
            peer = next((x for x in by_id[other]["pair_reviews"] if x["pair_id"] == p["pair_id"]), None)
            require(peer is not None and peer["outcome"] == p["outcome"], "inconsistent_pair_reviews")
    return result


def curate(analysis, decisions, *, draft=False):
    checked = validate_decisions(decisions, analysis, draft=draft)
    records = [{**r, "review": d} for r, d in zip(analysis["records"], checked)]
    counts = {s: sum(d["state"] == s for d in checked) for s in STATES}
    coverage = []
    for c in analysis["classes"]:
        selected = [d for d in checked if d["class_id"] == c["class_id"]]
        coverage.append({**c, "candidates": len(selected), "approved": sum(d["state"] == "approved_for_dataset" for d in selected),
                         "rejected": sum(d["state"].startswith("rejected_") for d in selected),
                         "pending": sum(d["state"].startswith("needs_") for d in selected)})
    return {"schema_version": 1, "run_id": RUN, "stage": "agent_proposals_pending_human" if draft else "human_decisions_recorded",
            "analysis_sha256": sha(encode(analysis)), "decisions_sha256": sha(encode(decisions)),
            "source_hashes": analysis["source_hashes"], "method": analysis["method"], "python": analysis["python"],
            "records": records, "pairs": analysis["pairs"], "comparison_count": len(analysis["pairs"]),
            "counts": counts, "coverage": coverage,
            "classes_without_candidates": [c["class_id"] for c in coverage if c["candidates"] == 0],
            "classes_without_approved": [c["class_id"] for c in coverage if c["approved"] == 0],
            "training_sufficiency": "not_demonstrated", "training_authorized": False,
            "final_bytes_human_acceptance": "pending"}


def summary(curation):
    """Only closed, validated identifiers/enums/counts: never copy prose or provenance."""
    return {k: curation[k] for k in ("schema_version", "stage", "counts", "comparison_count", "coverage",
            "classes_without_candidates", "classes_without_approved", "training_sufficiency", "training_authorized")} | {
            "records": [{"id": r["id"], "review_id": r["review_id"], "sha256": r["sha256"],
                         "class_id": r["class_id"], "state": r["review"]["state"]} for r in curation["records"]]}


def report(curation):
    lines = ["# P07 — pareceres de curadoria", "", "Stage: " + curation["stage"], "",
             "Zero aprovações é válido. Suficiência para treinamento não demonstrada; treinamento não autorizado.",
             "Pareceres do agente exigem aceite humano. Não constituem perícia botânica.", "",
             f"Comparações: {curation['comparison_count']}; contagens: {json.dumps({state: curation['counts'][state] for state in STATES})}", ""]
    for r in curation["records"]:
        lines += ["## " + r["id"], "", "```json", encode(r).decode().rstrip(), "```", ""]
    return ("\n".join(lines) + "\n").encode()


@contextmanager
def output_lock(output, source):
    output, source = no_symlinks(output), no_symlinks(source)
    require(output != source and source not in output.parents and output not in source.parents, "output_source_overlap")
    require(not any((p / ".git").is_file() or (p / ".git/HEAD").is_file() for p in (output, *output.parents)), "output_inside_git")
    output.mkdir(parents=True, exist_ok=True)
    lock_path = no_symlinks(output / ".p07.lock")
    fd = os.open(lock_path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
    with os.fdopen(fd, "a+b") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise CurationError("output_locked") from None
        try:
            yield output
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def persist(output, files):
    # Precheck ALL targets before replacing any. Never silently change prior bytes.
    for name, raw in files.items():
        target = no_symlinks(output / name)
        require(not target.exists() or read_file(target) == raw, "output_conflict_new_version_required")
    for name, raw in files.items():
        target = output / name
        if target.exists():
            continue
        fd, temporary = tempfile.mkstemp(prefix=".p07-", dir=output)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(raw)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, target)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    fd = os.open(output, os.O_RDONLY | os.O_DIRECTORY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def run(source, output, *, decisions_path=None, draft=False, class_manifest=CLASS_MANIFEST):
    with output_lock(output, source) as destination:
        analysis = analyze(source, class_manifest)
        files = {"analysis.json": encode(analysis)}
        if decisions_path is not None:
            decisions_raw = read_file(decisions_path)
            decisions = strict_load(decisions_raw)
            result = curate(analysis, decisions, draft=draft)
            suffix = ".draft" if draft else ""
            files.update({f"curation{suffix}.json": encode(result), f"report{suffix}.md": report(result),
                          f"summary{suffix}.json": encode(summary(result))})
            require(read_file(decisions_path) == decisions_raw, "decisions_changed")
        require(tree_hashes(source) == analysis["source_hashes"], "source_changed_before_publish")
        persist(destination, files)
        return {"images": 17, "comparisons": 136, "mode": "analyze" if decisions_path is None else
                ("agent_draft" if draft else "human_finalization"), "files": sorted(files)}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--analyze-only", action="store_true")
    mode.add_argument("--finalize", action="store_true")
    mode.add_argument("--review-draft", action="store_true")
    parser.add_argument("--decisions", type=Path)
    args = parser.parse_args(argv)
    if bool(args.decisions) != (args.finalize or args.review_draft):
        parser.error("decisions required only for finalize/review-draft")
    try:
        result = run(args.source, args.output, decisions_path=args.decisions, draft=args.review_draft)
    except (CurationError, OSError, KeyError, TypeError, UnicodeError) as error:
        print(json.dumps({"error": str(error) if isinstance(error, CurationError) else "invalid_or_inaccessible_input"}), file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
