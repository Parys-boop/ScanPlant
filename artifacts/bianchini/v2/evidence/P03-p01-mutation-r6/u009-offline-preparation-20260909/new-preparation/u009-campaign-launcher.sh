#!/usr/bin/env bash
# Future-only U-009 campaign. Do not execute without explicit human authorization.
set -Eeuo pipefail

readonly RUN_DIR='/var/tmp/p03-r6-u009-prepared-offline.N4w7Ls'
readonly REPOSITORY='/home/administradorarthur/code/scanplant-personal/.bianchini-worktrees/ScanPlant/v2-p03'
readonly EXPECTED_REVISION='79f2a5a834c2678130a3d44c81373a8b75a0d29d'
readonly APPROVED_DIGEST='18cef0bf86bc6eecfaa10a8ee241e0c4fa3d543fbcdcd90cca75d6b661c032e1'
readonly DOTNET_ROOT='/home/administradorarthur/.dotnet-scanplant-8'
readonly DOTNET="$DOTNET_ROOT/dotnet"
readonly PREFLIGHT='/var/tmp/p03-r6-host-preflight.Yw7rqr'
readonly R5='/tmp/p03-r5-u007.h8rfIr'
readonly LOCAL_FEED="$R5/local-feed"
readonly APPROVED_NUGET_PACKAGES="$PREFLIGHT/nuget-packages"
readonly SOLUTION="$PREFLIGHT/context/P03-R6-net8.sln"
readonly API_PROJECT="$REPOSITORY/ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj"
readonly HARNESS_PROJECT="$REPOSITORY/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj"
readonly FORBIDDEN_PROJECT="$REPOSITORY/ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj"
readonly VERSIONED_SOLUTION="$REPOSITORY/ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.sln"
readonly CONFIG="$RUN_DIR/u009-stryker-config.json"
readonly NUGET_CONFIG="$RUN_DIR/NuGet.Config"
readonly RESOLVER="$RUN_DIR/cli-home/.dotnet/toolResolverCache/1/dotnet-stryker"
readonly STRYKER_CLI="$R5/nuget-packages/dotnet-stryker/4.16.0/tools/net8.0/any/Stryker.CLI.dll"
readonly START_MARKER="$RUN_DIR/u009-campaign-started"
readonly LOGS="$RUN_DIR/logs"
readonly PROGRESS="$LOGS/progress.log"
readonly OUTPUT="$RUN_DIR/output"
readonly EFFECTIVE_NUGET="$RUN_DIR/effective-nuget-settings.txt"

CURRENT_STAGE='bootstrap'; CURRENT_REASON='launcher initialization'; FAILURE_STAGE=''; FAILURE_REASON=''; FAILURE_EXIT=''
progress() { printf 'stage=%s event=%s detail=%s\n' "$1" "$2" "$3" >> "$PROGRESS"; }
record_failure() { local code="$1"; [[ -n "$FAILURE_STAGE" ]] || { FAILURE_STAGE="$CURRENT_STAGE"; FAILURE_REASON="$CURRENT_REASON"; FAILURE_EXIT="$code"; progress "$CURRENT_STAGE" failed "$CURRENT_REASON; exit_code=$code"; }; }
on_error() { record_failure "$?"; }
on_exit() { local code="$?"; trap - EXIT; set +e; [[ "$code" -eq 0 ]] && { FAILURE_STAGE='none'; FAILURE_REASON='none'; FAILURE_EXIT=0; } || record_failure "$code"; printf 'campaign_count_before=1\ncampaign_count_after=%s\nU-008=consumed_non_reusable\nU-009=%s\nfailure_stage=%s\nfailure_reason=%s\nexit_code=%s\n' "$( [[ -e "$START_MARKER" ]] && printf 2 || printf 1)" "$( [[ -e "$START_MARKER" ]] && printf consumed || printf reserved_not_authorized)" "$FAILURE_STAGE" "$FAILURE_REASON" "$FAILURE_EXIT" > "$RUN_DIR/campaign-summary.txt"; exit "$code"; }
trap on_error ERR
trap on_exit EXIT
guard() { CURRENT_STAGE="$1"; CURRENT_REASON="$2"; progress "$1" started "$2"; shift 2; "$@"; progress "$CURRENT_STAGE" passed "$CURRENT_REASON"; }
record_effective_nuget() { test "$RestoreConfigFile" = "$NUGET_CONFIG" && test "$RestoreSources" = "$LOCAL_FEED" && test "$NUGET_PACKAGES" = "$APPROVED_NUGET_PACKAGES" && printf 'RestoreConfigFile=%s\nRestoreSources=%s\nNUGET_PACKAGES=%s\nRestoreIgnoreFailedSources=%s\n' "$RestoreConfigFile" "$RestoreSources" "$NUGET_PACKAGES" "$RestoreIgnoreFailedSources" > "$EFFECTIVE_NUGET"; }

mkdir -p "$LOGS" "$OUTPUT" "$RUN_DIR/home" "$RUN_DIR/tmp" "$RUN_DIR/nuget-http-cache" "$RUN_DIR/nuget-plugins-cache"
guard authorization 'U-009 requires explicit human grant' test "${U009_AUTHORIZATION:-}" = granted
guard single_use 'no previous U-009 marker may exist' test ! -e "$START_MARKER"
guard integrity.prepared 'launcher, config, NuGet config, static audit, and resolver match reviewed SHA-256 values independent of caller cwd' bash -c 'cd "$1" && sha256sum -c --strict SHA256SUMS' _ "$RUN_DIR"
guard binding.branch 'branch is bm/v2-p03' test "$(git -C "$REPOSITORY" branch --show-current)" = bm/v2-p03
guard binding.head 'HEAD matches approved revision' test "$(git -C "$REPOSITORY" rev-parse HEAD)" = "$EXPECTED_REVISION"
guard binding.upstream 'upstream matches approved revision' test "$(git -C "$REPOSITORY" rev-parse '@{upstream}')" = "$EXPECTED_REVISION"
guard binding.divergence 'branch divergence is 0/0' test "$(git -C "$REPOSITORY" rev-list --left-right --count HEAD...@{upstream})" = $'0\t0'
guard binding.tree 'repository is clean' test -z "$(git -C "$REPOSITORY" status --porcelain=v1)"
guard binding.digest 'approved manifest digest matches' test "$(sha256sum "$REPOSITORY/artifacts/bianchini/v2/approval/manifest-p03-r6.sha256" | awk '{print $1}')" = "$APPROVED_DIGEST"
guard preflight.checksums 'approved host preflight checksums verify' bash -c 'cd "$1" && sha256sum -c --strict checksums.sha256' _ "$PREFLIGHT"
guard preflight.status 'approved host preflight status remains passed' grep -Fxq 'PREFLIGHT_HOST_STATUS=passed' "$PREFLIGHT/preflight-host-summary.txt"
guard preflight.results 'approved restore/build/harness results remain passed' grep -Fxq 'RESTORE_EXIT=0' "$PREFLIGHT/preflight-host-summary.txt"
guard preflight.build 'approved isolated Release/net8.0 build passed' grep -Fxq 'BUILD_EXIT=0' "$PREFLIGHT/preflight-host-summary.txt"
guard preflight.harness 'approved MutationHarness result is exactly 23/23' grep -Fxq 'MUTATION_HARNESS_RESULT=23_of_23_passed' "$PREFLIGHT/preflight-host-summary.txt"
guard environment.sdk 'SDK is exactly 8.0.424' test "$("$DOTNET" --version)" = 8.0.424
guard environment.paths 'all run directories are real writable directories' bash -c 'for d in "$@"; do test -d "$d" && test ! -L "$d" && test -w "$d" || exit 1; done' _ "$RUN_DIR" "$LOGS" "$RUN_DIR/home" "$RUN_DIR/tmp" "$RUN_DIR/cli-home" "$OUTPUT" "$RUN_DIR/nuget-http-cache" "$RUN_DIR/nuget-plugins-cache"
guard environment.sources 'NuGet config clears inherited sources and lists only the local feed without HTTP or NuGet.org' bash -c 'grep -Fqx "    <clear />" "$1" && grep -Fqx "    <add key=\"R5-local-feed\" value=\"$2\" />" "$1" && ! grep -Eiq "https?://|nuget\.org" "$1"' _ "$NUGET_CONFIG" "$LOCAL_FEED"
guard environment.tool 'resolver and Stryker 4.16.0 CLI are fixed local files' bash -c 'test -f "$1" && test -f "$2" && grep -Fq "\"Version\":\"4.16.0\"" "$1" && grep -Fq "\"PathToExecutable\":\"$2\"" "$1"' _ "$RESOLVER" "$STRYKER_CLI"
guard topology.solution 'temporary solution has only approved members' bash -c 'test "$("$1" sln "$2" list | rg -c "\.csproj$")" = 2 && "$1" sln "$2" list | rg -Fqx "../../../../home/administradorarthur/code/scanplant-personal/.bianchini-worktrees/ScanPlant/v2-p03/ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj" && "$1" sln "$2" list | rg -Fqx "../../../../home/administradorarthur/code/scanplant-personal/.bianchini-worktrees/ScanPlant/v2-p03/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness/ScanPlantAPI.MutationHarness.csproj"' _ "$DOTNET" "$SOLUTION"
guard topology.exclusions 'versioned solution, multi-target project, and net10.0 are excluded' bash -c '! grep -Fq "ScanPlantAPI.Tests.csproj" "$1" && ! grep -Fq "ScanPlantAPI.sln" "$1" && ! grep -Fq net10.0 "$1" && test -f "$2"' _ "$SOLUTION" "$CONFIG"
guard configuration.targets 'only the two approved mutation targets and concurrency 1 are configured' bash -c 'grep -Fqx "      \"Services/ExternalProviders/ExternalFallbackUploadValidator.cs\"," "$1" && grep -Fqx "      \"Services/ExternalProviders/ExternalFallbackService.cs\"" "$1" && test "$(grep -Fc ".cs" "$1")" = 2 && grep -Fqx "    \"concurrency\": 1," "$1"' _ "$CONFIG"

export DOTNET_ROOT DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_HOME="$RUN_DIR/cli-home" HOME="$RUN_DIR/home"
export TMPDIR="$RUN_DIR/tmp" TMP="$RUN_DIR/tmp" TEMP="$RUN_DIR/tmp"
export NUGET_PACKAGES="$APPROVED_NUGET_PACKAGES" NUGET_CONFIG_FILE="$NUGET_CONFIG" NUGET_HTTP_CACHE_PATH="$RUN_DIR/nuget-http-cache" NUGET_PLUGINS_CACHE_PATH="$RUN_DIR/nuget-plugins-cache"
export RestoreConfigFile="$NUGET_CONFIG" RestoreSources="$LOCAL_FEED" RestoreIgnoreFailedSources=false
export NUGET_AUDIT=false DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1 DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=1 DOTNET_GENERATE_ASPNET_CERTIFICATE=false
export PATH="$DOTNET_ROOT:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
guard environment.effective_nuget 'MSBuild/NuGet RestoreConfigFile, RestoreSources, and NUGET_PACKAGES are exact and recorded before the marker' record_effective_nuget
guard environment.network_namespace 'a user-mapped network namespace can be created before the marker' unshare --user --map-root-user --net -- true

mkdir "$START_MARKER"
printf 'campaign_count_before=1\ncampaign_count_after=2\nU-009=consumed\n' > "$START_MARKER/campaign-count"
progress campaign claimed 'atomic transition reserved: campaign_count 1 -> 2'
cd "$REPOSITORY/ScanPlantAPI/ScanPlantAPI"
CURRENT_STAGE='campaign'; CURRENT_REASON='execute exactly one authorized Stryker U-009 campaign in an isolated network namespace'
progress "$CURRENT_STAGE" started "$CURRENT_REASON"
unshare --user --map-root-user --net -- "$DOTNET" tool run dotnet-stryker -- --config-file "$CONFIG" --solution "$SOLUTION" --project "$API_PROJECT" --test-project "$HARNESS_PROJECT" --target-framework net8.0 --concurrency 1 --output "$OUTPUT" --skip-version-check > "$LOGS/stryker.log" 2>&1
progress "$CURRENT_STAGE" passed "$CURRENT_REASON"
