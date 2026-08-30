#!/usr/bin/env bash
# Manual, foreground-only P01 mutation evidence runner (config-root-fixed v5).
# Run this directly from a WSL terminal; do not launch it through Codex.

set -uo pipefail

REPO_ROOT="${SCANPLANT_P01_REPO:-/home/administradorarthur/code/scanplant-work/.bianchini-worktrees/ScanPlant/v1-p01}"
DOTNET_ROOT_8="/home/administradorarthur/.dotnet-scanplant-8"
DOTNET="${DOTNET_ROOT_8}/dotnet"
DOTNET_CLI_HOME_SAFE="/home/administradorarthur"
HARNESS_DIR="${REPO_ROOT}/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness"
HARNESS_PROJECT="${HARNESS_DIR}/ScanPlantAPI.MutationHarness.csproj"
APP_ROOT="${REPO_ROOT}/ScanPlantAPI/ScanPlantAPI"
SDK_VERSION="8.0.424"
RUNTIME_VERSION="8.0.30"
EXPECTED_STRYKER_VERSION="4.16.0"
PREFLIGHT_ONLY=0
CONFIG_VALIDATION_ONLY=0

case "${1:-}" in
  "") ;;
  --preflight-only) PREFLIGHT_ONLY=1 ;;
  --validate-config-only) CONFIG_VALIDATION_ONLY=1 ;;
  *) printf 'Usage: %s [--preflight-only|--validate-config-only]\n' "$0" >&2; exit 64 ;;
esac
[[ "$#" -le 1 ]] || { printf 'Usage: %s [--preflight-only|--validate-config-only]\n' "$0" >&2; exit 64; }

if [[ "${SCANPLANT_P01_SANITIZED:-}" != "1" ]]; then
  exec /usr/bin/env -i \
    SCANPLANT_P01_SANITIZED=1 \
    SCANPLANT_P01_REPO="${REPO_ROOT}" \
    SCANPLANT_P01_PREFLIGHT_ONLY="${PREFLIGHT_ONLY}" \
    SCANPLANT_P01_CONFIG_VALIDATION_ONLY="${CONFIG_VALIDATION_ONLY}" \
    HOME="/home/administradorarthur" USER="administradorarthur" LOGNAME="administradorarthur" SHELL="/bin/bash" \
    DOTNET_ROOT="${DOTNET_ROOT_8}" DOTNET_HOST_PATH="${DOTNET}" DOTNET_MULTILEVEL_LOOKUP=0 \
    DOTNET_CLI_HOME="${DOTNET_CLI_HOME_SAFE}" NUGET_PACKAGES="/home/administradorarthur/.nuget/packages" \
    PATH="${DOTNET_ROOT_8}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
    /bin/bash "$0" "${1:-}"
fi

PREFLIGHT_ONLY="${SCANPLANT_P01_PREFLIGHT_ONLY:-0}"
CONFIG_VALIDATION_ONLY="${SCANPLANT_P01_CONFIG_VALIDATION_ONLY:-0}"
RUN_DIR="$(mktemp -d /tmp/scanplant-p01-manual-final-v5-XXXXXXXX)"
RUN_TOKEN="${RUN_DIR##*-}"
CONFIG_NAME="stryker-config.json"
CONFIG_PATH="${RUN_DIR}/${CONFIG_NAME}"
export TMPDIR="${RUN_DIR}/tmp"
mkdir -p "$TMPDIR"

FINAL_CODE=125
FINAL_CODE_SET=0
PHASE="initializing"
START_EPOCH="$(date +%s)"
printf '%s\n' "$RUN_DIR" > "${RUN_DIR}/run-dir.txt"
printf '%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${RUN_DIR}/start.utc"

finalize() {
  local shell_status=$?
  local end_epoch
  [[ "$FINAL_CODE_SET" -eq 1 ]] || FINAL_CODE=$shell_status
  end_epoch="$(date +%s)"
  printf '%s\n' "$PHASE" > "${RUN_DIR}/final-phase.txt"
  printf '%s\n' "$FINAL_CODE" > "${RUN_DIR}/exit-code.txt"
  printf '%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${RUN_DIR}/end.utc"
  printf '%s\n' "$((end_epoch - START_EPOCH))" > "${RUN_DIR}/duration-seconds.txt"
  find "$RUN_DIR" -type f ! -name 'SHA256SUMS' -print0 | sort -z | xargs -0r sha256sum > "${RUN_DIR}/SHA256SUMS"
  printf 'P01 manual run directory: %s\nFinal phase: %s; exit code: %s\n' "$RUN_DIR" "$PHASE" "$FINAL_CODE"
}
trap finalize EXIT
trap 'FINAL_CODE=130; FINAL_CODE_SET=1; PHASE=interrupted; exit 130' INT
trap 'FINAL_CODE=143; FINAL_CODE_SET=1; PHASE=terminated; exit 143' TERM

fail_preflight() {
  local code=$1
  PHASE="preflight_failed"
  FINAL_CODE=$code
  FINAL_CODE_SET=1
  printf '%s\n' "$code" > "${RUN_DIR}/preflight-exit-code.txt"
  printf 'Preflight failed (exit %s); Stryker will not be started.\n' "$code" >&2
  exit "$code"
}

MUTATE_TARGETS=(
  'Services/ExternalProviders/ExternalFallbackUploadValidator.cs'
  'Services/ExternalProviders/ExternalFallbackService.cs'
)
LAUNCHER_COMMAND=("$DOTNET" tool run dotnet-stryker --)
STRYKER_COMMAND=(
  "${LAUNCHER_COMMAND[@]}"
  --config-file "$CONFIG_PATH"
  --project ScanPlantAPI.csproj
  --target-framework net8.0
  --concurrency 1
  --reporter json
  --reporter cleartext
  --reporter progress
  --verbosity trace
  --log-to-file
  --skip-version-check
  --output "${RUN_DIR}/results"
)

write_config() {
  umask 077
  cat > "$CONFIG_PATH" <<'JSON'
{
  "stryker-config": {
    "mutate": [
      "Services/ExternalProviders/ExternalFallbackUploadValidator.cs",
      "Services/ExternalProviders/ExternalFallbackService.cs"
    ]
  }
}
JSON
  cp -- "$CONFIG_PATH" "${RUN_DIR}/stryker-config.effective.json"
  printf '%s\n' "$CONFIG_PATH" > "${RUN_DIR}/config-path.txt"
}

validate_config() {
  command -v python3 >/dev/null 2>&1 || return 76
  python3 - "$CONFIG_PATH" "${MUTATE_TARGETS[@]}" "${RUN_DIR}/config-validation.json" <<'PY'
import json, pathlib, sys
config_path, first, second, output = sys.argv[1:]
expected = [first, second]
try:
    config = json.load(open(config_path, encoding="utf-8"))
    root = config.get("stryker-config")
    actual = root.get("mutate") if isinstance(root, dict) else None
    valid = set(config) == {"stryker-config"} and isinstance(root, dict) and set(root) == {"mutate"} and actual == expected
except Exception as error:
    valid, actual, error_text = False, None, str(error)
else:
    error_text = None
pathlib.Path(output).write_text(json.dumps({"valid": valid, "expected": expected, "actual": actual, "error": error_text}, indent=2) + "\n", encoding="utf-8")
sys.exit(0 if valid else 75)
PY
}

validate_config_natively() {
  # Stryker.NET 4.16.0 has no dry-run option. A deliberately absent project
  # forces config parsing before project resolution fails, so no mutant can run.
  local sentinel_project="__scanplant_p01_config_validation_only__.csproj"
  local status
  local -a command=(
    "${LAUNCHER_COMMAND[@]}"
    --config-file "$CONFIG_PATH"
    --project "$sentinel_project"
    --target-framework net8.0
    --concurrency 1
    --reporter cleartext
    --verbosity trace
    --log-to-file
    --skip-version-check
    --output "${RUN_DIR}/config-validation-results"
  )
  printf '%q ' "${command[@]}" > "${RUN_DIR}/config-validation-command.txt"
  printf '\n' >> "${RUN_DIR}/config-validation-command.txt"
  PHASE="config_validating"
  (cd "$APP_ROOT" && "${command[@]}") > "${RUN_DIR}/config-validation.log" 2>&1
  status=$?
  printf '%s\n' "$status" > "${RUN_DIR}/config-validation-exit-code.txt"
  [[ "$status" -ne 0 ]] || return 77
  grep -Fq -- 'must contain a single "stryker-config" root object' "${RUN_DIR}/config-validation.log" && return 78
  grep -Fq -- "$sentinel_project" "${RUN_DIR}/config-validation.log" || return 79
  grep -Fq -- 'No project found' "${RUN_DIR}/config-validation.log" || return 80
  grep -Fq -- 'Failed to analyze project builds' "${RUN_DIR}/config-validation.log" || return 81
  grep -Fq -- "${MUTATE_TARGETS[0]##*/}" "${RUN_DIR}/config-validation.log" || return 82
  grep -Fq -- "${MUTATE_TARGETS[1]##*/}" "${RUN_DIR}/config-validation.log" || return 83
  printf 'accepted_root=stryker-config\nrecognized_mutate_filters=%s\nrecognized_mutate_filters=%s\nno_mutants_executed=true\n' \
    "${MUTATE_TARGETS[0]}" "${MUTATE_TARGETS[1]}" > "${RUN_DIR}/config-validation-summary.txt"
}

validate_report_scope() {
  local report="${RUN_DIR}/results/reports/mutation-report.json"
  python3 - "$report" "$APP_ROOT" "${MUTATE_TARGETS[@]}" "${RUN_DIR}/mutation-files.json" "${RUN_DIR}/scope-validation.json" <<'PY'
import collections, json, pathlib, sys
report_path, app_root, first, second, files_out, validation_out = sys.argv[1:]
allowed = {str(pathlib.PurePosixPath(app_root) / first), str(pathlib.PurePosixPath(app_root) / second)}
data = json.load(open(report_path, encoding="utf-8"))
rows, outside, effective_allowed = [], [], set()
for file_name, entry in data.get("files", {}).items():
    statuses = collections.Counter(m.get("status", "Unknown") for m in entry.get("mutants", []))
    effective = sum(count for status, count in statuses.items() if status not in {"Ignored", "CompileError"})
    if statuses:
        rows.append({"file": file_name, "statuses": dict(sorted(statuses.items())), "effective_mutants": effective})
    if effective and file_name not in allowed:
        outside.append(file_name)
    if effective and file_name in allowed:
        effective_allowed.add(file_name)
rows.sort(key=lambda row: row["file"])
valid = not outside and effective_allowed == allowed
pathlib.Path(files_out).write_text(json.dumps({"files": rows}, indent=2) + "\n", encoding="utf-8")
pathlib.Path(validation_out).write_text(json.dumps({"valid": valid, "authorized_files": sorted(allowed), "effective_files": sorted(effective_allowed), "outside_scope_effective_files": sorted(outside)}, indent=2) + "\n", encoding="utf-8")
sys.exit(0 if valid else 90)
PY
}

{
  printf 'repo=%s\nharness=%s\ndotnet=%s\n' "$REPO_ROOT" "$HARNESS_DIR" "$DOTNET"
  printf 'expected_sdk=%s\nexpected_runtime=%s\nexpected_stryker=%s\n' "$SDK_VERSION" "$RUNTIME_VERSION" "$EXPECTED_STRYKER_VERSION"
  printf 'authorized_mutate=%s\nauthorized_mutate=%s\n' "${MUTATE_TARGETS[0]}" "${MUTATE_TARGETS[1]}"
  printf 'preflight_only=%s\nconfig_validation_only=%s\nnetwork=disabled_by_sanitized_environment; no restore/install command is used\n' "$PREFLIGHT_ONLY" "$CONFIG_VALIDATION_ONLY"
} > "${RUN_DIR}/preflight-contract.txt"
env | sort > "${RUN_DIR}/environment.txt"
git -C "$REPO_ROOT" status --short --branch > "${RUN_DIR}/git-status.txt" 2>&1 || fail_preflight $?
git -C "$REPO_ROOT" status --porcelain > "${RUN_DIR}/git-porcelain.txt" 2>&1 || fail_preflight $?
[[ ! -s "${RUN_DIR}/git-porcelain.txt" ]] || fail_preflight 74
"$DOTNET" --info > "${RUN_DIR}/dotnet-info.txt" 2>&1 || fail_preflight $?
(cd "$REPO_ROOT" && "$DOTNET" tool list --local) > "${RUN_DIR}/dotnet-tools.txt" 2>&1 || fail_preflight $?
[[ -x "$DOTNET" && -d "$DOTNET_CLI_HOME/.dotnet/toolResolverCache" ]] || fail_preflight 65
"$DOTNET" --list-sdks | grep -Fqx -- "${SDK_VERSION} [${DOTNET_ROOT_8}/sdk]" || fail_preflight 66
"$DOTNET" --list-runtimes | grep -Fqx -- "Microsoft.NETCore.App ${RUNTIME_VERSION} [${DOTNET_ROOT_8}/shared/Microsoft.NETCore.App]" || fail_preflight 67
grep -Fqx -- '      "version": "4.16.0",' "${REPO_ROOT}/.config/dotnet-tools.json" || fail_preflight 68
grep -F -- 'dotnet-stryker' "${RUN_DIR}/dotnet-tools.txt" | grep -F -- "$EXPECTED_STRYKER_VERSION" > "${RUN_DIR}/launcher-version.txt" || fail_preflight 68
[[ -f "$HARNESS_PROJECT" && -f "${HARNESS_DIR}/obj/project.assets.json" && -f "${HARNESS_DIR}/bin/Debug/net8.0/ScanPlantAPI.Tests.dll" ]] || fail_preflight 71
for target in "${MUTATE_TARGETS[@]}"; do [[ -f "${APP_ROOT}/${target}" ]] || fail_preflight 72; done

write_config
validate_config || fail_preflight $?
printf '%q ' "${LAUNCHER_COMMAND[@]}" > "${RUN_DIR}/launcher-command.txt"
printf '%s\n' '-- --help' >> "${RUN_DIR}/launcher-command.txt"
printf '%s\n' 'Resolved at 4.16.0 from validated local manifest and dotnet tool list; not invoked during preflight.' > "${RUN_DIR}/launcher-resolution.txt"
printf '%q ' "${STRYKER_COMMAND[@]}" > "${RUN_DIR}/validated-stryker-command.txt"
printf '\n' >> "${RUN_DIR}/validated-stryker-command.txt"

PHASE="harness_preflight"
cd "$HARNESS_DIR" || fail_preflight $?
"$DOTNET" test "$HARNESS_PROJECT" --framework net8.0 --no-build --no-restore 2>&1 | tee "${RUN_DIR}/preflight-console.log"
PREFLIGHT_STATUS=${PIPESTATUS[0]}
printf '%s\n' "$PREFLIGHT_STATUS" > "${RUN_DIR}/preflight-exit-code.txt"
[[ "$PREFLIGHT_STATUS" -eq 0 ]] || fail_preflight "$PREFLIGHT_STATUS"

if [[ "$PREFLIGHT_ONLY" == "1" ]]; then
  PHASE="preflight_complete"
  FINAL_CODE=0
  FINAL_CODE_SET=1
  printf 'Preflight-only completed successfully; Stryker was not started.\n'
  exit 0
fi

if [[ "$CONFIG_VALIDATION_ONLY" == "1" ]]; then
  validate_config_natively
  CONFIG_VALIDATION_STATUS=$?
  [[ -f "${RUN_DIR}/config-validation-exit-code.txt" ]] || printf '%s\n' "$CONFIG_VALIDATION_STATUS" > "${RUN_DIR}/config-validation-exit-code.txt"
  PHASE="config_validated"
  FINAL_CODE=$CONFIG_VALIDATION_STATUS
  FINAL_CODE_SET=1
  exit "$CONFIG_VALIDATION_STATUS"
fi

PHASE="stryker_running"
printf '%q ' "${STRYKER_COMMAND[@]}" > "${RUN_DIR}/command.txt"
printf '\n' >> "${RUN_DIR}/command.txt"
(
  printf '%s\n' "$BASHPID" > "${RUN_DIR}/stryker-launcher.pid"
  exec "${STRYKER_COMMAND[@]}"
) 2>&1 | tee "${RUN_DIR}/console.log"
STRYKER_STATUS=${PIPESTATUS[0]}
printf '%s\n' "$STRYKER_STATUS" > "${RUN_DIR}/stryker-exit-code.txt"
if [[ "$STRYKER_STATUS" -ne 0 ]]; then
  PHASE="stryker_failed"
  FINAL_CODE=$STRYKER_STATUS
  FINAL_CODE_SET=1
  exit "$STRYKER_STATUS"
fi

validate_report_scope
SCOPE_STATUS=$?
printf '%s\n' "$SCOPE_STATUS" > "${RUN_DIR}/scope-validation-exit-code.txt"
PHASE="scope_validated"
FINAL_CODE=$SCOPE_STATUS
FINAL_CODE_SET=1
exit "$SCOPE_STATUS"
