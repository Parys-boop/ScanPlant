#!/usr/bin/env bash
# U-008 single-campaign launcher.  Do not execute without recorded authorization.
set -Eeuo pipefail
umask 077

readonly EXPECTED_HEAD='f6ecda9342913d3dd6b98587984ded7a2af72fd1'
readonly EXPECTED_BRANCH='bm/v2-p03'
readonly EXPECTED_SDK='8.0.424'
readonly EXPECTED_RUNTIME='8.0.30'
readonly EXPECTED_STRYKER='4.16.0'
readonly REQUIRED_AUTHORIZATION='P03-R5-U008-APPROVED'
readonly SOURCE_A='Services/ExternalProviders/ExternalFallbackUploadValidator.cs'
readonly SOURCE_B='Services/ExternalProviders/ExternalFallbackService.cs'

repo_root=$(git rev-parse --show-toplevel)
campaign_count=0
phase=initializing
failure_recorded=false
: "${CAMPAIGN_RUN_DIR:?set a new campaign run directory}"
[[ $CAMPAIGN_RUN_DIR == "$repo_root"/artifacts/bianchini/v2/evidence/P03-p01-mutation-r5/campaign-run-* ]]
[[ ! -e $CAMPAIGN_RUN_DIR ]]
mkdir -p "$CAMPAIGN_RUN_DIR"

record_count() { printf '%s campaign_count=%s\n' "$(date -u +%FT%TZ)" "$campaign_count" >> "$CAMPAIGN_RUN_DIR/campaign-count.txt"; }
failure() {
  [[ $failure_recorded == false ]] || return 0
  failure_recorded=true
  printf '%s\n' "$phase" > "$CAMPAIGN_RUN_DIR/failed-phase.txt"
  printf '%s\n' "$1" > "$CAMPAIGN_RUN_DIR/failed-exit-code.txt"
}
on_err() { local code=$?; trap - ERR; set +e; failure "$code"; exit "$code"; }
on_exit() {
  local code=$?
  trap - EXIT
  set +e
  (( code == 0 )) || phase=failed
  (( code == 0 )) || failure "$code"
  record_count
  {
    printf 'phase=%s\nexit_code=%s\ncampaign_count=%s\n' "$phase" "$code" "$campaign_count"
    printf 'campaign_authorized=%s\n' "$([[ ${P03_R5_U008_AUTHORIZATION:-} == "$REQUIRED_AUTHORIZATION" ]] && printf true || printf false)"
    printf 'campaign_executed=%s\n' "$([[ $campaign_count -eq 1 ]] && printf true || printf false)"
  } > "$CAMPAIGN_RUN_DIR/execution-summary.txt"
  printf '%s\n' "$phase" > "$CAMPAIGN_RUN_DIR/final-phase.txt"
  (
    cd "$CAMPAIGN_RUN_DIR" || exit 0
    find . -type f ! -name checksums.sha256 ! -name checksums.verify.txt -print0 | sort -z | xargs -0r sha256sum > checksums.sha256
    sha256sum -c checksums.sha256 > checksums.verify.txt 2>&1
  ) || true
  exit "$code"
}
trap on_err ERR
trap on_exit EXIT

run() {
  local name=$1; shift
  printf '%q ' "$@" > "$CAMPAIGN_RUN_DIR/$name.command"; printf '\n' >> "$CAMPAIGN_RUN_DIR/$name.command"
  pwd > "$CAMPAIGN_RUN_DIR/$name.cwd"; date -u +%FT%TZ > "$CAMPAIGN_RUN_DIR/$name.started-at.utc"
  if "$@" > "$CAMPAIGN_RUN_DIR/$name.stdout" 2> "$CAMPAIGN_RUN_DIR/$name.stderr"; then
    printf '0\n' > "$CAMPAIGN_RUN_DIR/$name.exit"
  else
    local code=$?; printf '%s\n' "$code" > "$CAMPAIGN_RUN_DIR/$name.exit"; cat "$CAMPAIGN_RUN_DIR/$name.stdout" "$CAMPAIGN_RUN_DIR/$name.stderr" > "$CAMPAIGN_RUN_DIR/$name.console" || true; return "$code"
  fi
  cat "$CAMPAIGN_RUN_DIR/$name.stdout" "$CAMPAIGN_RUN_DIR/$name.stderr" > "$CAMPAIGN_RUN_DIR/$name.console"
}
gate() { phase=$1; shift; run "$phase" "$@"; }

record_count
phase=authorization
[[ ${P03_R5_U008_AUTHORIZATION:-} == "$REQUIRED_AUTHORIZATION" ]]
cd "$repo_root"
gate repo-branch git branch --show-current
gate repo-branch-match grep -Fxq "$EXPECTED_BRANCH" "$CAMPAIGN_RUN_DIR/repo-branch.stdout"
gate repo-head git rev-parse HEAD
gate repo-head-match grep -Fxq "$EXPECTED_HEAD" "$CAMPAIGN_RUN_DIR/repo-head.stdout"
gate repo-upstream git rev-parse '@{upstream}'
gate repo-upstream-match grep -Fxq "$EXPECTED_HEAD" "$CAMPAIGN_RUN_DIR/repo-upstream.stdout"
gate repo-divergence git rev-list --left-right --count HEAD...@{upstream}
gate repo-divergence-match grep -Fxq $'0\t0' "$CAMPAIGN_RUN_DIR/repo-divergence.stdout"
gate repo-worktree git diff --quiet
gate repo-index git diff --cached --quiet
gate repo-status git status --porcelain=v1 --untracked-files=all
gate repo-status-empty test ! -s "$CAMPAIGN_RUN_DIR/repo-status.stdout"

host_home=${HOME:?natural HOME is required before sanitization}
readonly DOTNET_ROOT="$host_home/.dotnet-scanplant-8"
readonly DOTNET_HOST="$DOTNET_ROOT/dotnet"
readonly NUGET_PACKAGES="$host_home/.nuget/packages"
readonly TOOL_DIR="$NUGET_PACKAGES/dotnet-stryker/$EXPECTED_STRYKER"
readonly TOOL_NUPKG="$TOOL_DIR/dotnet-stryker.$EXPECTED_STRYKER.nupkg"
readonly TOOL_NUSPEC="$TOOL_DIR/dotnet-stryker.nuspec"
readonly LOCAL_FEED="$CAMPAIGN_RUN_DIR/nuget-local-source"
gate dotnet-host test -x "$DOTNET_HOST"
gate nuget-cache test -d "$NUGET_PACKAGES"
gate manifest-id grep -Fq '"dotnet-stryker"' .config/dotnet-tools.json
gate manifest-version grep -Fq '"version": "4.16.0"' .config/dotnet-tools.json
gate tool-nupkg test -f "$TOOL_NUPKG"
gate tool-nuspec test -f "$TOOL_NUSPEC"
# [[:space:]] accepts CRLF after the closing XML tag and retains exact id/version matching.
gate nuspec-id grep -Eq '^[[:space:]]*<id>dotnet-stryker</id>[[:space:]]*$' "$TOOL_NUSPEC"
gate nuspec-version grep -Eq '^[[:space:]]*<version>4\.16\.0</version>[[:space:]]*$' "$TOOL_NUSPEC"
gate tool-nupkg-sha256 sha256sum "$TOOL_NUPKG"
mv "$CAMPAIGN_RUN_DIR/tool-nupkg-sha256.stdout" "$CAMPAIGN_RUN_DIR/dotnet-stryker-4.16.0.nupkg.sha256"

export DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_TELEMETRY_OPTOUT=1 DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1 DOTNET_CLI_WORKLOAD_UPDATE_NOTIFY_DISABLE=1 NUGET_CERT_REVOCATION_MODE=offline
export DOTNET_CLI_HOME="$CAMPAIGN_RUN_DIR/cli-home" HOME="$CAMPAIGN_RUN_DIR/home" TMPDIR="$CAMPAIGN_RUN_DIR/tmp" NUGET_HTTP_CACHE_PATH="$CAMPAIGN_RUN_DIR/nuget-http-cache" NUGET_PLUGINS_CACHE_PATH="$CAMPAIGN_RUN_DIR/nuget-plugins-cache" PATH="$DOTNET_ROOT:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" LANG=C LC_ALL=C
gate isolated-directories mkdir -p "$DOTNET_CLI_HOME" "$HOME" "$TMPDIR" "$NUGET_HTTP_CACHE_PATH" "$NUGET_PLUGINS_CACHE_PATH" "$LOCAL_FEED"
gate local-feed-stryker-link ln -s "$TOOL_NUPKG" "$LOCAL_FEED/dotnet-stryker.$EXPECTED_STRYKER.nupkg"
gate local-feed-list bash -c 'find "$1" -maxdepth 1 -type l -printf "%f -> %l\\n" | sort' _ "$LOCAL_FEED"
mv "$CAMPAIGN_RUN_DIR/local-feed-list.stdout" "$CAMPAIGN_RUN_DIR/local-nuget-source.manifest"
gate local-feed-stryker grep -Fqx "dotnet-stryker.4.16.0.nupkg -> $TOOL_NUPKG" "$CAMPAIGN_RUN_DIR/local-nuget-source.manifest"
cat > "$CAMPAIGN_RUN_DIR/NuGet.Config" <<EOF
<?xml version="1.0" encoding="utf-8"?>
<configuration><packageSources><clear /><add key="p03-local-cache" value="$LOCAL_FEED" /></packageSources><disabledPackageSources><clear /></disabledPackageSources><auditSources><clear /></auditSources></configuration>
EOF
gate nuget-local-source grep -Fq "key=\"p03-local-cache\" value=\"$LOCAL_FEED\"" "$CAMPAIGN_RUN_DIR/NuGet.Config"
gate nuget-no-network bash -c '! grep -Eqi "https?://|nuget\\.org" "$1"' _ "$CAMPAIGN_RUN_DIR/NuGet.Config"
gate sdk "$DOTNET_HOST" --version
gate sdk-match grep -Fxq "$EXPECTED_SDK" "$CAMPAIGN_RUN_DIR/sdk.stdout"
gate runtimes "$DOTNET_HOST" --list-runtimes
gate runtime-core grep -Eq "^Microsoft\\.NETCore\\.App[[:space:]]+$EXPECTED_RUNTIME[[:space:]]+\\[$DOTNET_ROOT/shared/Microsoft\\.NETCore\\.App\\][[:space:]]*$" "$CAMPAIGN_RUN_DIR/runtimes.stdout"
gate runtime-aspnet grep -Eq "^Microsoft\\.AspNetCore\\.App[[:space:]]+$EXPECTED_RUNTIME[[:space:]]+\\[$DOTNET_ROOT/shared/Microsoft\\.AspNetCore\\.App\\][[:space:]]*$" "$CAMPAIGN_RUN_DIR/runtimes.stdout"
gate tool-verify "$DOTNET_HOST" nuget verify --all --configfile "$CAMPAIGN_RUN_DIR/NuGet.Config" "$TOOL_NUPKG"
gate tool-restore "$DOTNET_HOST" tool restore --configfile "$CAMPAIGN_RUN_DIR/NuGet.Config" --disable-parallel
gate tool-list "$DOTNET_HOST" tool list --local
gate tool-version grep -Eq '^dotnet-stryker[[:space:]]+4\.16\.0[[:space:]]+' "$CAMPAIGN_RUN_DIR/tool-list.stdout"

cd "$repo_root/ScanPlantAPI/ScanPlantAPI"
cat > "$CAMPAIGN_RUN_DIR/stryker-config.json" <<EOF
{"stryker-config":{"mutate":["$SOURCE_A","$SOURCE_B"]}}
EOF
printf 'expected_revision=%s\nrevision=%s\nsource_a=%s\nsource_b=%s\nframework=net8.0\nconcurrency=1\nreporters=json,cleartext,progress\n' "$EXPECTED_HEAD" "$(git -C "$repo_root" rev-parse HEAD)" "$SOURCE_A" "$SOURCE_B" > "$CAMPAIGN_RUN_DIR/revision-and-scope.txt"
gate exact-targets grep -Fq "\"$SOURCE_A\",\"$SOURCE_B\"" "$CAMPAIGN_RUN_DIR/stryker-config.json"

# Sole durable 0 -> 1 transition; every gate above is non-mutational.
phase=campaign-invocation
campaign_count=1
record_count
run stryker "$DOTNET_HOST" tool run dotnet-stryker -- --config-file "$CAMPAIGN_RUN_DIR/stryker-config.json" --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --reporter json --reporter cleartext --reporter progress --verbosity trace --log-to-file --skip-version-check --output "$CAMPAIGN_RUN_DIR/results"
