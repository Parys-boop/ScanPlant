#!/usr/bin/env bash
# Manual, foreground-only P01-R1 mutation evidence runner (launcher-fixed v3).
# Run this directly from a WSL terminal; do not launch it through Codex.

set -uo pipefail

REPO_ROOT="${SCANPLANT_P01_REPO:-/home/administradorarthur/code/scanplant-work/.bianchini-worktrees/ScanPlant/v1-p01}"
DOTNET_ROOT_8="/home/administradorarthur/.dotnet-scanplant-8"
DOTNET="${DOTNET_ROOT_8}/dotnet"
DOTNET_CLI_HOME_SAFE="/home/administradorarthur"
HARNESS_DIR="${REPO_ROOT}/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness"
HARNESS_PROJECT="${HARNESS_DIR}/ScanPlantAPI.MutationHarness.csproj"
SDK_VERSION="8.0.424"
RUNTIME_VERSION="8.0.30"
EXPECTED_STRYKER_VERSION="4.16.0"
PREFLIGHT_ONLY=0

case "${1:-}" in
  "") ;;
  --preflight-only) PREFLIGHT_ONLY=1 ;;
  *)
    printf 'Usage: %s [--preflight-only]\n' "$0" >&2
    exit 64
    ;;
esac
if [[ "$#" -gt 1 ]]; then
  printf 'Usage: %s [--preflight-only]\n' "$0" >&2
  exit 64
fi

# Re-exec once with a deliberately minimal environment. This deliberately
# retains the stable CLI home containing the already-restored local-tool
# resolver cache; the per-run directory remains only for temporary files.
if [[ "${SCANPLANT_P01_SANITIZED:-}" != "1" ]]; then
  exec /usr/bin/env -i \
    SCANPLANT_P01_SANITIZED=1 \
    SCANPLANT_P01_REPO="${REPO_ROOT}" \
    SCANPLANT_P01_PREFLIGHT_ONLY="${PREFLIGHT_ONLY}" \
    HOME="/home/administradorarthur" \
    USER="administradorarthur" \
    LOGNAME="administradorarthur" \
    SHELL="/bin/bash" \
    DOTNET_ROOT="${DOTNET_ROOT_8}" \
    DOTNET_HOST_PATH="${DOTNET}" \
    DOTNET_MULTILEVEL_LOOKUP=0 \
    DOTNET_CLI_HOME="${DOTNET_CLI_HOME_SAFE}" \
    NUGET_PACKAGES="/home/administradorarthur/.nuget/packages" \
    PATH="${DOTNET_ROOT_8}:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" \
    /bin/bash "$0" "${1:-}"
fi

PREFLIGHT_ONLY="${SCANPLANT_P01_PREFLIGHT_ONLY:-0}"

RUN_DIR="$(mktemp -d /tmp/scanplant-p01-manual-final-v3-XXXXXXXX)"
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
  if [[ "$FINAL_CODE_SET" -eq 0 ]]; then
    FINAL_CODE=$shell_status
  fi
  end_epoch="$(date +%s)"
  printf '%s\n' "$PHASE" > "${RUN_DIR}/final-phase.txt"
  printf '%s\n' "$FINAL_CODE" > "${RUN_DIR}/exit-code.txt"
  printf '%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "${RUN_DIR}/end.utc"
  printf '%s\n' "$((end_epoch - START_EPOCH))" > "${RUN_DIR}/duration-seconds.txt"
  find "$RUN_DIR" -type f ! -name 'SHA256SUMS' -print0 | sort -z | xargs -0r sha256sum > "${RUN_DIR}/SHA256SUMS"
  printf 'P01 manual run directory: %s\n' "$RUN_DIR"
  printf 'Final phase: %s; exit code: %s\n' "$PHASE" "$FINAL_CODE"
}

on_interrupt() {
  FINAL_CODE=130
  FINAL_CODE_SET=1
  PHASE="interrupted"
  exit 130
}

on_terminate() {
  FINAL_CODE=143
  FINAL_CODE_SET=1
  PHASE="terminated"
  exit 143
}

trap finalize EXIT
trap on_interrupt INT
trap on_terminate TERM

fail_preflight() {
  local code=$1
  PHASE="preflight_failed"
  FINAL_CODE=$code
  FINAL_CODE_SET=1
  printf '%s\n' "$code" > "${RUN_DIR}/preflight-exit-code.txt"
  printf 'Preflight failed (exit %s); Stryker will not be started.\n' "$code" >&2
  exit "$code"
}

LAUNCHER_COMMAND=("$DOTNET" tool run dotnet-stryker)
MUTATE_TARGETS=(
  'Services/ExternalProviders/ExternalFallbackUploadValidator.cs'
  'Services/ExternalProviders/ExternalFallbackService.cs'
)
STRYKER_COMMAND=(
  "${LAUNCHER_COMMAND[@]}"
  --project ScanPlantAPI.csproj
  --target-framework net8.0
  --concurrency 1
  --mutate "${MUTATE_TARGETS[0]}"
  --mutate "${MUTATE_TARGETS[1]}"
  --reporter json
  --reporter cleartext
  --reporter progress
  --verbosity trace
  --log-to-file
  --skip-version-check
  --output "${RUN_DIR}/results"
)

validate_stryker_parameters() {
  local expected
  local actual
  local index
  local -a expected_command=(
    "${LAUNCHER_COMMAND[@]}"
    --project ScanPlantAPI.csproj
    --target-framework net8.0
    --concurrency 1
    --mutate "${MUTATE_TARGETS[0]}"
    --mutate "${MUTATE_TARGETS[1]}"
    --reporter json
    --reporter cleartext
    --reporter progress
    --verbosity trace
    --log-to-file
    --skip-version-check
    --output "${RUN_DIR}/results"
  )

  [[ "${#STRYKER_COMMAND[@]}" -eq "${#expected_command[@]}" ]] || return 1
  for index in "${!expected_command[@]}"; do
    expected="${expected_command[$index]}"
    actual="${STRYKER_COMMAND[$index]}"
    [[ "$actual" == "$expected" ]] || return 1
  done
  printf '%q ' "${STRYKER_COMMAND[@]}" > "${RUN_DIR}/validated-stryker-command.txt"
  printf '\n' >> "${RUN_DIR}/validated-stryker-command.txt"
}

{
  printf 'repo=%s\n' "$REPO_ROOT"
  printf 'harness=%s\n' "$HARNESS_DIR"
  printf 'dotnet=%s\n' "$DOTNET"
  printf 'dotnet_cli_home=%s\n' "$DOTNET_CLI_HOME"
  printf 'expected_sdk=%s\nexpected_runtime=%s\nexpected_stryker=%s\n' "$SDK_VERSION" "$RUNTIME_VERSION" "$EXPECTED_STRYKER_VERSION"
  printf 'authorized_mutate=Services/ExternalProviders/ExternalFallbackUploadValidator.cs\n'
  printf 'authorized_mutate=Services/ExternalProviders/ExternalFallbackService.cs\n'
  printf 'preflight_only=%s\n' "$PREFLIGHT_ONLY"
  printf 'network=disabled_by_sanitized_environment; no restore/install command is used\n'
} > "${RUN_DIR}/preflight-contract.txt"
env | sort > "${RUN_DIR}/environment.txt"
git -C "$REPO_ROOT" status --short --branch > "${RUN_DIR}/git-status.txt" 2>&1 || fail_preflight $?
git -C "$REPO_ROOT" status --porcelain > "${RUN_DIR}/git-porcelain.txt" 2>&1 || fail_preflight $?
[[ ! -s "${RUN_DIR}/git-porcelain.txt" ]] || fail_preflight 74
"$DOTNET" --info > "${RUN_DIR}/dotnet-info.txt" 2>&1 || fail_preflight $?
(cd "$REPO_ROOT" && "$DOTNET" tool list --local) > "${RUN_DIR}/dotnet-tools.txt" 2>&1 || fail_preflight $?

[[ -x "$DOTNET" ]] || fail_preflight 64
[[ -d "$DOTNET_CLI_HOME/.dotnet/toolResolverCache" ]] || fail_preflight 65
"$DOTNET" --list-sdks | grep -Fqx -- "${SDK_VERSION} [${DOTNET_ROOT_8}/sdk]" || fail_preflight 66
"$DOTNET" --list-runtimes | grep -Fqx -- "Microsoft.NETCore.App ${RUNTIME_VERSION} [${DOTNET_ROOT_8}/shared/Microsoft.NETCore.App]" || fail_preflight 67
[[ -f "${REPO_ROOT}/.config/dotnet-tools.json" ]] || fail_preflight 68
grep -Fqx -- '      "version": "4.16.0",' "${REPO_ROOT}/.config/dotnet-tools.json" || fail_preflight 68
grep -Fqx -- '        "dotnet-stryker"' "${REPO_ROOT}/.config/dotnet-tools.json" || fail_preflight 68
grep -F -- 'dotnet-stryker' "${RUN_DIR}/dotnet-tools.txt" | grep -F -- "$EXPECTED_STRYKER_VERSION" > "${RUN_DIR}/launcher-version.txt" || fail_preflight 68
validate_stryker_parameters || fail_preflight 75

# This is intentionally the same launcher prefix used by STRYKER_COMMAND.
# Stryker 4.16.0 uses --version for a dashboard project-version setting, so it
# cannot be used as an executable-version switch. The manifest and local-tool
# listing above prove the selected launcher resolves at 4.16.0 without invoking
# Stryker; --preflight-only must finish before any Stryker command is run.
PHASE="launcher_preflight"
printf '%q ' "${LAUNCHER_COMMAND[@]}" > "${RUN_DIR}/launcher-command.txt"
printf '%s\n' '-- --help' >> "${RUN_DIR}/launcher-command.txt"
printf '%s\n' 'Resolved at 4.16.0 from validated local manifest and dotnet tool list; not invoked during preflight.' > "${RUN_DIR}/launcher-resolution.txt"

[[ -f "$HARNESS_PROJECT" ]] || fail_preflight 69
[[ -f "${HARNESS_DIR}/obj/project.assets.json" ]] || fail_preflight 70
[[ -f "${HARNESS_DIR}/bin/Debug/net8.0/ScanPlantAPI.Tests.dll" ]] || fail_preflight 71
[[ -f "${REPO_ROOT}/ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackUploadValidator.cs" ]] || fail_preflight 72
[[ -f "${REPO_ROOT}/ScanPlantAPI/ScanPlantAPI/Services/ExternalProviders/ExternalFallbackService.cs" ]] || fail_preflight 73

PHASE="harness_preflight"
cd "$HARNESS_DIR" || fail_preflight $?
"$DOTNET" test "$HARNESS_PROJECT" --framework net8.0 --no-build --no-restore 2>&1 | tee "${RUN_DIR}/preflight-console.log"
PREFLIGHT_STATUS=${PIPESTATUS[0]}
printf '%s\n' "$PREFLIGHT_STATUS" > "${RUN_DIR}/preflight-exit-code.txt"
if [[ "$PREFLIGHT_STATUS" -ne 0 ]]; then
  fail_preflight "$PREFLIGHT_STATUS"
fi

if [[ "$PREFLIGHT_ONLY" == "1" ]]; then
  PHASE="preflight_complete"
  FINAL_CODE=0
  FINAL_CODE_SET=1
  printf 'Preflight-only completed successfully; Stryker was not started.\n'
  exit 0
fi

PHASE="stryker_running"
printf '%q ' "${STRYKER_COMMAND[@]}" > "${RUN_DIR}/command.txt"
printf '\n' >> "${RUN_DIR}/command.txt"
printf 'Starting foreground Stryker run; console is being recorded in %s\n' "${RUN_DIR}/console.log"

# This subshell is part of the foreground pipeline (not detached/background).
(
  printf '%s\n' "$BASHPID" > "${RUN_DIR}/stryker-launcher.pid"
  exec "${STRYKER_COMMAND[@]}"
) 2>&1 | tee "${RUN_DIR}/console.log"
STRYKER_STATUS=${PIPESTATUS[0]}

printf '%s\n' "$STRYKER_STATUS" > "${RUN_DIR}/stryker-exit-code.txt"
PHASE="stryker_finished"
FINAL_CODE=$STRYKER_STATUS
FINAL_CODE_SET=1
exit "$STRYKER_STATUS"
