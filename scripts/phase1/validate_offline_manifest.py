"""Read-only validator for the P05 offline manifest; Python 3.12 stdlib."""

import argparse
from datetime import date, datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


BINOMIAL = re.compile(r"[A-Z][a-z]+ [a-z]+(?:-[a-z]+)*", re.ASCII)
REF_ID = re.compile(r"[a-z][a-z0-9]*(?:_[a-z0-9]+)*", re.ASCII)
HEX = re.compile(r"[0-9a-f]{64}", re.ASCII)
ROOT_KEYS = {"schema_version", "manifest_version", "normalization_version",
             "roster_sha256", "references", "classes"}
CLASS_KEYS = {"index", "class_id", "kind", "scientific_name", "display_name",
              "common_names", "synonyms", "taxonomy_ref_ids", "definition"}
ROSTER_KEYS = {"schema_version", "status", "approval_ref", "approved_on", "species"}
PROTECTIONS = (("outra_planta", "Outra planta"),
               ("imagem_invalida", "Imagem inválida"))


class ContractError(ValueError):
    """Diagnostics deliberately contain no untrusted input values."""

    def __init__(self, code, path):
        self.code, self.path = code, path
        super().__init__(f"{code} {path}")


def require(condition, code, path):
    if not condition:
        raise ContractError(code, path)


def normalize_name(value):
    """NFC, Unicode whitespace folding and casefold; no fuzzy matching."""
    require(type(value) is str, "E_STRING", "$")
    for char in value:
        category = unicodedata.category(char)
        require(not (category in {"Cc", "Cf", "Cs"} and not char.isspace()),
                "E_UNICODE", "$")
    result = " ".join(unicodedata.normalize("NFC", value).split()).casefold()
    require(bool(result), "E_EMPTY", "$")
    return result


def text(value, path):
    try:
        normalize_name(value)
    except ContractError as error:
        raise ContractError(error.code, path) from None
    return value


def obj(value, keys, path):
    require(type(value) is dict, "E_OBJECT", path)
    require(set(value) == keys, "E_FIELDS", path)


def array(value, path, nonempty=False):
    require(type(value) is list, "E_ARRAY", path)
    require(not nonempty or bool(value), "E_EMPTY", path)
    return value


def binomial(value, path):
    text(value, path)
    require(BINOMIAL.fullmatch(value) is not None, "E_BINOMIAL", path)


def iso_date(value, path):
    require(type(value) is str and re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value),
            "E_DATE", path)
    try:
        parsed = date.fromisoformat(value)
    except ValueError:
        raise ContractError("E_DATE", path) from None
    require(parsed <= datetime.now(timezone.utc).date(), "E_DATE_FUTURE", path)


def strict_load(raw, path="$"):
    """Validate transport and reject duplicate keys and nonfinite numbers."""
    require(type(raw) is bytes, "E_BYTES", path)
    require(not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw
            and raw.endswith(b"\n"), "E_ENCODING", path)
    try:
        source = raw.decode("utf-8")
    except UnicodeDecodeError:
        raise ContractError("E_ENCODING", path) from None

    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "E_JSON_DUPLICATE_KEY", path)
            result[key] = value
        return result

    def nonfinite(_):
        raise ContractError("E_JSON_NONFINITE", path)

    def finite_float(value):
        parsed = float(value)
        require(math.isfinite(parsed), "E_JSON_NONFINITE", path)
        return parsed

    try:
        return json.loads(source, object_pairs_hook=pairs, parse_constant=nonfinite,
                          parse_float=finite_float)
    except ContractError:
        raise
    except (ValueError, RecursionError):
        raise ContractError("E_JSON", path) from None


def validate_roster(roster):
    obj(roster, ROSTER_KEYS, "$.roster")
    require(type(roster["schema_version"]) is int and roster["schema_version"] == 1,
            "E_SCHEMA", "$.roster.schema_version")
    require(roster["status"] == "approved", "E_APPROVAL", "$.roster.status")
    text(roster["approval_ref"], "$.roster.approval_ref")
    iso_date(roster["approved_on"], "$.roster.approved_on")
    entries = array(roster["species"], "$.roster.species")
    require(len(entries) == 12, "E_ROSTER_COUNT", "$.roster.species")
    names = set()
    for i, entry in enumerate(entries):
        path = f"$.roster.species[{i}]"
        obj(entry, {"index", "approved_name", "source_ref"}, path)
        require(type(entry["index"]) is int and entry["index"] == i, "E_INDEX", path + ".index")
        binomial(entry["approved_name"], path + ".approved_name")
        key = normalize_name(entry["approved_name"])
        require(key not in names, "E_ROSTER_DUPLICATE", path + ".approved_name")
        names.add(key)
        text(entry["source_ref"], path + ".source_ref")


def validate_reference(ref, path):
    obj(ref, {"ref_id", "authority", "url", "consulted_on", "title"}, path)
    require(type(ref["ref_id"]) is str and REF_ID.fullmatch(ref["ref_id"]), "E_REF_ID", path)
    text(ref["title"], path + ".title")
    iso_date(ref["consulted_on"], path + ".consulted_on")
    text(ref["url"], path + ".url")
    # Reject URL parser normalization of tabs/newlines and encoded separators.
    require(not any(c.isspace() for c in ref["url"]), "E_URL", path + ".url")
    try:
        url = urlsplit(ref["url"])
        host = url.hostname
        port = url.port
    except ValueError:
        raise ContractError("E_URL", path + ".url") from None
    require(url.scheme == "https" and not url.query and not url.fragment
            and url.username is None and url.password is None and port is None
            and "?" not in ref["url"] and "#" not in ref["url"], "E_URL", path + ".url")
    if ref["authority"] == "kew_powo":
        valid = host == "powo.science.kew.org" and re.fullmatch(
            r"/taxon/(?:urn:lsid:ipni\.org:names:)?[0-9]+-[0-9]+", unquote(url.path))
    elif ref["authority"] == "jbrj_flora":
        valid = host in {"floradobrasil.jbrj.gov.br", "reflora.jbrj.gov.br"} and re.fullmatch(
            r"/(?:reflora/)?floradobrasil/FB[0-9]+", url.path)
    else:
        valid = False
    require(bool(valid), "E_URL_AUTHORITY", path + ".url")


def scientific_map(manifest):
    """Build only the scientific namespace and reject ambiguous keys."""
    result = {}
    for i, item in enumerate(manifest["classes"]):
        if item["kind"] != "species":
            continue
        for name in [item["scientific_name"]] + [s["name"] for s in item["synonyms"]]:
            key = normalize_name(name)
            require(key not in result, "E_NAME_COLLISION", f"$.classes[{i}]")
            result[key] = item["class_id"]
    return result


def resolve_scientific_name(manifest, name):
    """Resolve against a validated manifest; unknown text returns None."""
    return scientific_map(manifest).get(normalize_name(name))


def validate_manifest(manifest, roster_bytes):
    roster = strict_load(roster_bytes, "$.roster")
    validate_roster(roster)
    obj(manifest, ROOT_KEYS, "$")
    require(type(manifest["schema_version"]) is int and manifest["schema_version"] == 1,
            "E_SCHEMA", "$.schema_version")
    require(manifest["manifest_version"] == "1.0.0", "E_VERSION", "$.manifest_version")
    require(manifest["normalization_version"] == "1", "E_VERSION", "$.normalization_version")
    digest = hashlib.sha256(roster_bytes).hexdigest()
    require(type(manifest["roster_sha256"]) is str and HEX.fullmatch(manifest["roster_sha256"])
            and manifest["roster_sha256"] == digest, "E_ROSTER_HASH", "$.roster_sha256")
    refs = {}
    for i, ref in enumerate(array(manifest["references"], "$.references", True)):
        path = f"$.references[{i}]"
        validate_reference(ref, path)
        require(ref["ref_id"] not in refs, "E_REF_DUPLICATE", path)
        refs[ref["ref_id"]] = ref
    used = set()

    def ref_list(values, path):
        seen = set()
        for value in array(values, path, True):
            require(type(value) is str and value in refs, "E_REF_MISSING", path)
            require(value not in seen, "E_REF_DUPLICATE", path)
            seen.add(value)
            used.add(value)

    classes = array(manifest["classes"], "$.classes")
    require(len(classes) == 14, "E_CLASS_COUNT", "$.classes")
    for i, item in enumerate(classes):
        path = f"$.classes[{i}]"
        obj(item, CLASS_KEYS, path)
        require(type(item["index"]) is int and item["index"] == i, "E_INDEX", path + ".index")
        expected_id = f"species_{i + 1:02}" if i < 12 else PROTECTIONS[i - 12][0]
        require(item["class_id"] == expected_id, "E_CLASS_ID", path + ".class_id")
        require(item["kind"] == ("species" if i < 12 else "protection"), "E_KIND", path + ".kind")
        text(item["display_name"], path + ".display_name")
        array(item["common_names"], path + ".common_names")
        array(item["synonyms"], path + ".synonyms")
        array(item["taxonomy_ref_ids"], path + ".taxonomy_ref_ids")
        if i >= 12:
            require(item["scientific_name"] is None and item["common_names"] == []
                    and item["synonyms"] == [] and item["taxonomy_ref_ids"] == []
                    and item["display_name"] == PROTECTIONS[i - 12][1], "E_PROTECTION", path)
            text(item["definition"], path + ".definition")
            continue
        binomial(item["scientific_name"], path + ".scientific_name")
        require(item["definition"] is None, "E_SPECIES_DEFINITION", path)
        require(bool(item["common_names"]) and item["display_name"] in item["common_names"],
                "E_DISPLAY_NAME", path)
        common_keys = set()
        for j, name in enumerate(item["common_names"]):
            text(name, f"{path}.common_names[{j}]")
            key = normalize_name(name)
            require(key not in common_keys, "E_COMMON_DUPLICATE", path + ".common_names")
            common_keys.add(key)
        ref_list(item["taxonomy_ref_ids"], path + ".taxonomy_ref_ids")
        for j, synonym in enumerate(item["synonyms"]):
            spath = f"{path}.synonyms[{j}]"
            obj(synonym, {"name", "ref_ids"}, spath)
            binomial(synonym["name"], spath + ".name")
            ref_list(synonym["ref_ids"], spath + ".ref_ids")
    names = scientific_map(manifest)
    for i, entry in enumerate(roster["species"]):
        require(names.get(normalize_name(entry["approved_name"])) == f"species_{i + 1:02}",
                "E_ROSTER_MAPPING", f"$.roster.species[{i}].approved_name")
    require(used == set(refs), "E_REF_ORPHAN", "$.references")
    return {"valid": True, "species": 12, "protection": 2, "classes": 14,
            "schema_version": 1, "manifest_version": "1.0.0", "normalization_version": "1",
            "roster_sha256": digest}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--roster", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        raw = args.manifest.read_bytes()
        roster_raw = args.roster.read_bytes()
    except OSError:
        print("E_FILE $", file=sys.stderr)
        return 2
    try:
        result = validate_manifest(strict_load(raw), roster_raw)
    except ContractError as error:
        print(str(error), file=sys.stderr)
        return 1
    result["manifest_sha256"] = hashlib.sha256(raw).hexdigest()
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
