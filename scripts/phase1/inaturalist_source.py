"""Pure iNaturalist v1 adapter for P08; transport and persistence are caller-owned.

Official schema inspected 2026-10-05:
https://github.com/inaturalist/iNaturalistAPI/blob/main/lib/views/swagger_v1.yml.ejs
It documents Photo(id, attribution, license_code, url), observations.photos,
and size variants sharing an extension. A provider original is at most 2048px;
it is never asserted to be a camera original. No API code proves a CC version.

build_query accepts one reviewed crosswalk entry and one canonical manifest
class. parse_page returns at most 100 unique photos, counts deferred/duplicates,
and a *proposed* next cursor; the caller persists that cursor only after all
items are durably consumed/deferred. It never performs IO or makes approvals.
photo_record accepts separate human evidence for photo and observation rights;
without that evidence its download URL is null. All records are PRIVATE data.
"""
from datetime import datetime, timezone
import hashlib
import re
from urllib.parse import urlsplit


class ContractError(ValueError):
    """An input cannot satisfy the frozen source contract."""


API_URL = "https://api.inaturalist.org/v1/observations"
SCHEMA_URL = "https://github.com/inaturalist/iNaturalistAPI/blob/main/lib/views/swagger_v1.yml.ejs"
MEDIA_HOST = "inaturalist-open-data.s3.amazonaws.com"
LICENSES = {
    "cc-by": ("4.0", "https://creativecommons.org/licenses/by/4.0/"),
    "cc0": ("1.0", "https://creativecommons.org/publicdomain/zero/1.0/"),
}


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _integer(value, minimum=1):
    return type(value) is int and value >= minimum


def _hash(value):
    return isinstance(value, str) and re.fullmatch(r"[a-f0-9]{64}", value) is not None


def _date(value):
    try:
        stamp = datetime.fromisoformat(value.replace("Z", "+00:00"))
        if stamp.tzinfo is None:
            raise ValueError
        return stamp.astimezone(timezone.utc)
    except (ValueError, TypeError, AttributeError) as exc:
        raise ContractError("invalid_timestamp") from exc


def _source_url(value, entity, identifier):
    return value == f"https://www.inaturalist.org/{entity}/{identifier}"


def validate_crosswalk(crosswalk, class_item):
    """Reject unmapped/protection/alias taxa before any observation request.

    Evidence and reviewer identify the external human-reviewed document;
    integrity of that document against evidence.sha256 is caller-owned.
    """
    if not isinstance(class_item, dict) or class_item.get("kind") != "species":
        raise ContractError("protection_not_queried")
    if not isinstance(crosswalk, dict):
        raise ContractError("no_crosswalk")
    expected = {"class_id": class_item.get("class_id"), "source": "inaturalist",
                "namespace": "inaturalist", "scientific_name": class_item.get("scientific_name"),
                "rank": "species", "status": "active", "synonym_of": None}
    if any(key not in crosswalk or crosswalk[key] != value for key, value in expected.items()):
        raise ContractError("crosswalk_identity_conflict")
    if not _text(expected["scientific_name"]) or not _integer(crosswalk.get("source_taxon_id")):
        raise ContractError("crosswalk_taxon_missing")
    if "authorship" not in crosswalk or (not _text(crosswalk["authorship"]) and not (
            crosswalk["authorship"] is None and _text(crosswalk.get("authorship_missing_reason")))):
        raise ContractError("crosswalk_authorship_missing")
    refs = class_item.get("taxonomy_ref_ids")
    if not refs or crosswalk.get("taxonomy_ref_ids") != refs:
        raise ContractError("crosswalk_reference_conflict")
    evidence = crosswalk.get("evidence", {})
    reviewer = crosswalk.get("reviewer", {})
    if not isinstance(evidence, dict) or not isinstance(reviewer, dict):
        raise ContractError("crosswalk_review_missing")
    if (not _source_url(evidence.get("url"), "taxa", crosswalk["source_taxon_id"])
            or not _hash(evidence.get("sha256")) or not _text(evidence.get("version"))):
        raise ContractError("crosswalk_evidence_missing")
    try:
        datetime.strptime(evidence.get("date", ""), "%Y-%m-%d")
    except (TypeError, ValueError) as exc:
        raise ContractError("crosswalk_evidence_date_missing") from exc
    if any(not _text(reviewer.get(key)) for key in ("id", "qualification")) or reviewer.get("decision") != "approved":
        raise ContractError("crosswalk_review_missing")
    return crosswalk


def build_query(crosswalk, class_item, cutoff, id_above=0):
    """Return official query parameters, never a request or guessed taxon ID.

    created_d2 has date granularity in v1. parse_page separately enforces the
    exact timestamp cutoff, so later observations cannot enter this round.
    """
    entry = validate_crosswalk(crosswalk, class_item)
    stamp = _date(cutoff)
    if not _integer(id_above, 0):
        raise ContractError("invalid_cursor")
    return {"taxon_id": entry["source_taxon_id"], "photos": "true",
            "quality_grade": "research", "order_by": "id", "order": "asc",
            "per_page": 100, "id_above": id_above, "created_d2": stamp.date().isoformat()}


def _original_url(photo):
    value = photo.get("url")
    if not _text(value):
        return None
    try:
        parsed = urlsplit(value)
        if (parsed.scheme != "https" or parsed.hostname != MEDIA_HOST or
                parsed.username is not None or parsed.password is not None or
                parsed.port not in (None, 443) or parsed.fragment):
            return None
    except ValueError:
        return None
    # Entire path, ID and extension must match the documented provider scheme.
    match = re.fullmatch(r"/photos/([1-9][0-9]*)/(?:square|thumb|small|medium|large|original)\.(jpg|jpeg|png)", parsed.path)
    if not match or int(match.group(1)) != photo["id"]:
        return None
    if parsed.query and re.fullmatch(r"[0-9]+", parsed.query) is None:
        return None
    return f"https://{MEDIA_HOST}/photos/{photo['id']}/original.{match.group(2)}"


def _rights(proof, code, entity, identifier):
    if not isinstance(proof, dict) or not isinstance(code, str) or code not in LICENSES:
        return False
    version, url = LICENSES[code]
    return (proof.get("license_code") == code and proof.get("version") == version
            and proof.get("legal_url") == url and _hash(proof.get("evidence_sha256"))
            and _source_url(proof.get("source_url"), entity, identifier)
            and proof.get("restrictions") == [])


def photo_record(photo, observation, legal_evidence=None):
    """Normalize a photo without conflating photo, observation and DB rights.

    legal_evidence schema is exemplified in the synthetic contract tests. Both
    entities need a canonical individual legal URL, version, evidence SHA256,
    no extra restrictions, and a human-approved ID-bound attribution record.
    """
    if not isinstance(photo, dict) or not isinstance(observation, dict):
        raise ContractError("invalid_photo_schema")
    if not _integer(photo.get("id")) or not _integer(observation.get("id")):
        raise ContractError("invalid_source_id")
    reasons = []
    proof = legal_evidence if isinstance(legal_evidence, dict) else {}
    identity_ok = (proof.get("photo_id") == photo["id"] and proof.get("observation_id") == observation["id"]
                   and proof.get("decision") == "approved"
                   and all(_text(proof.get(key)) for key in ("reviewer", "author", "licensor", "credit")))
    try:
        _date(proof.get("reviewed_at"))
    except ContractError:
        identity_ok = False
    photo_rights = _rights(proof.get("photo"), photo.get("license_code"), "photos", photo["id"])
    observation_rights = _rights(proof.get("observation"), observation.get("license_code"), "observations", observation["id"])
    database_rights = proof.get("database_rights") == "compatible"
    attribution = photo.get("attribution")
    if not (identity_ok and photo_rights and observation_rights and database_rights and _text(attribution)):
        reasons.append("needs_license_review")
    if not observation_rights:
        reasons.append("observation_rights_unresolved")
    if not database_rights:
        reasons.append("database_rights_unresolved")
    original_url = _original_url(photo)
    if not original_url:
        reasons.append("unproven_original_url")
    media_id = str(photo["id"])
    return {"source": "inaturalist", "media_id": media_id, "photo_id": photo["id"],
            "candidate_id": hashlib.sha256(f"inaturalist:{media_id}".encode()).hexdigest(),
            "observation_id": observation["id"], "license_code": photo.get("license_code"),
            "observation_license_code": observation.get("license_code"), "credit": attribution,
            "author": proof.get("author") if identity_ok else None,
            "licensor": proof.get("licensor") if identity_ok else None,
            "license_version": proof.get("photo", {}).get("version") if photo_rights else None,
            "legal_url": proof.get("photo", {}).get("legal_url") if photo_rights else None,
            "license_evidence_sha256": proof.get("photo", {}).get("evidence_sha256") if photo_rights else None,
            "observation_license_version": proof.get("observation", {}).get("version") if observation_rights else None,
            "observation_legal_url": proof.get("observation", {}).get("legal_url") if observation_rights else None,
            "observation_license_evidence_sha256": proof.get("observation", {}).get("evidence_sha256") if observation_rights else None,
            "rights_reviewer": proof.get("reviewer") if identity_ok else None,
            "rights_reviewed_at": proof.get("reviewed_at") if identity_ok else None,
            "source_page_url": f"https://www.inaturalist.org/photos/{photo['id']}",
            "observation_page_url": f"https://www.inaturalist.org/observations/{observation['id']}",
            "file_url": original_url if not reasons else None,
            "download_allowed": not reasons, "reasons": reasons,
            "state": "discovered" if not reasons else "needs_license_review",
            "origin_fidelity": "provider_original", "camera_original_verified": False,
            "original_url_contract": SCHEMA_URL,
            "photo_rights_passed": bool(identity_ok and photo_rights),
            "observation_rights_passed": bool(identity_ok and observation_rights),
            "database_rights_passed": bool(identity_ok and database_rights)}


def parse_page(response, crosswalk, class_item, cutoff, id_above=0):
    """Parse one page, preserving taxonomic conflicts as pending candidates.

    No raw observations/coordinates are copied. API total_results is metadata,
    not an examined-count claim. A next cursor is only a suggestion for the
    durable checkpoint owned by the orchestrator. Duplicate photos do not
    inflate counts; the photo budget applies to entries examined as well.
    """
    build_query(crosswalk, class_item, cutoff, id_above)
    if not isinstance(response, dict):
        raise ContractError("invalid_page_schema")
    rows = response.get("results")
    if (not isinstance(rows, list) or len(rows) > 100 or type(response.get("page")) is not int or response["page"] != 1
            or type(response.get("per_page")) is not int or response["per_page"] != 100 or not _integer(response.get("total_results"), 0)
            or response["total_results"] < len(rows)):
        raise ContractError("invalid_page_schema")
    result = {"candidates": [], "deferred_photo_count": 0, "duplicate_photo_count": 0,
              "next_id_above": id_above, "total_results": response["total_results"], "examined_photo_count": 0}
    seen = set()
    last = id_above
    for observation in rows:
        if not isinstance(observation, dict) or not _integer(observation.get("id")) or observation["id"] <= last:
            raise ContractError("regressive_observation_page")
        last = observation["id"]
        if _date(observation.get("created_at")) > _date(cutoff):
            raise ContractError("observation_after_cutoff")
        photos = observation.get("photos")
        if not isinstance(photos, list) or not photos or observation.get("quality_grade") != "research":
            raise ContractError("invalid_observation_schema")
        taxon = observation.get("taxon")
        if not isinstance(taxon, dict):
            raise ContractError("invalid_taxon_schema")
        exact = (taxon.get("id") == crosswalk["source_taxon_id"] and taxon.get("name") == crosswalk["scientific_name"]
                 and taxon.get("rank") == "species" and taxon.get("is_active") is True)
        for photo in photos:
            if result["examined_photo_count"] >= 100:
                result["deferred_photo_count"] += 1
                continue
            result["examined_photo_count"] += 1
            candidate = photo_record(photo, observation)
            if candidate["photo_id"] in seen:
                result["duplicate_photo_count"] += 1
                continue
            seen.add(candidate["photo_id"])
            candidate.update({"class_id": class_item["class_id"], "source_taxon_id": taxon.get("id"),
                              "scientific_name": taxon.get("name"), "namespace": "inaturalist",
                              "taxonomic_confidence": "source_supported" if exact else "conflict"})
            if not exact:
                candidate["reasons"].append("needs_taxonomic_mapping")
                candidate["download_allowed"] = False
                candidate["file_url"] = None
            result["candidates"].append(candidate)
    result["next_id_above"] = last
    return result
