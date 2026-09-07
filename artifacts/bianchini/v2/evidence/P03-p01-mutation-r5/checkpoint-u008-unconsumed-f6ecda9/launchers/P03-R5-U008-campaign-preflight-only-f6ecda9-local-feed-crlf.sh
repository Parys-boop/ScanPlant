#!/usr/bin/env bash
# Static preflight only: never invokes dotnet or Stryker and always leaves campaign_count at zero.
set -Eeuo pipefail
umask 077

readonly EXPECTED_HEAD='f6ecda9342913d3dd6b98587984ded7a2af72fd1'
readonly EXPECTED_SHA256='408c695e421a45522cf99f88c55baa549c03d108e1faca00d5f57a32ea22bf3c'
readonly LAUNCHER='/tmp/P03-R5-U008-campaign-launcher-f6ecda9-local-feed-crlf.sh'
readonly SOURCE_A='Services/ExternalProviders/ExternalFallbackUploadValidator.cs'
readonly SOURCE_B='Services/ExternalProviders/ExternalFallbackService.cs'

[[ $# -eq 0 ]] || { printf 'Usage: %s\n' "$0" >&2; exit 64; }
repo_root=$(git rev-parse --show-toplevel)
run_dir=$(mktemp -d /tmp/p03-r5-u008-campaign-preflight-local-feed-crlf-XXXXXX)
campaign_count=0
phase=initializing
record() { printf '%s campaign_count=%s\n' "$(date -u +%FT%TZ)" "$campaign_count" >> "$run_dir/campaign-count.txt"; }
finish() {
  local code=$?
  trap - EXIT; set +e
  (( code == 0 )) || phase=failed
  record
  printf 'phase=%s\nexit_code=%s\ncampaign_count=%s\ncampaign_authorized=false\ncampaign_executed=false\n' "$phase" "$code" "$campaign_count" > "$run_dir/execution-summary.txt"
  (
    cd "$run_dir" || exit 0
    find . -type f ! -name checksums.sha256 ! -name checksums.verify.txt -print0 | sort -z | xargs -0r sha256sum > checksums.sha256
    sha256sum -c checksums.sha256 > checksums.verify.txt 2>&1
  ) || true
  printf 'evidence_run_dir=%s\n' "$run_dir"
  exit "$code"
}
trap finish EXIT
check() {
  local name=$1; shift; phase=$name
  printf '%q ' "$@" > "$run_dir/$name.command"; printf '\n' >> "$run_dir/$name.command"
  if "$@" > "$run_dir/$name.stdout" 2> "$run_dir/$name.stderr"; then printf '0\n' > "$run_dir/$name.exit"; else local code=$?; printf '%s\n' "$code" > "$run_dir/$name.exit"; return "$code"; fi
}

record
cd "$repo_root"
check repo-head git rev-parse HEAD
check repo-head-match grep -Fxq "$EXPECTED_HEAD" "$run_dir/repo-head.stdout"
check launcher-file test -f "$LAUNCHER"
printf '%s  %s\n' "$EXPECTED_SHA256" "$LAUNCHER" > "$run_dir/launcher.sha256"
check launcher-sha256 sha256sum -c "$run_dir/launcher.sha256"
check launcher-syntax bash -n "$LAUNCHER"
check branch grep -Fq "readonly EXPECTED_BRANCH='bm/v2-p03'" "$LAUNCHER"
check local-feed-source grep -Fq '<packageSources><clear /><add key="p03-local-cache" value="$LOCAL_FEED"' "$LAUNCHER"
check local-feed-only grep -Fq 'nuget-no-network' "$LAUNCHER"
check no-remote-restore bash -c '! grep -Fq -- "--ignore-failed-sources" "$1"' _ "$LAUNCHER"
check isolated-http-cache grep -Fq 'NUGET_HTTP_CACHE_PATH="$CAMPAIGN_RUN_DIR/nuget-http-cache"' "$LAUNCHER"
check offline-revocation grep -Fq 'NUGET_CERT_REVOCATION_MODE=offline' "$LAUNCHER"
check crlf-safe-nuspec-id grep -Fq "grep -Eq '^[[:space:]]*<id>dotnet-stryker</id>[[:space:]]*$'" "$LAUNCHER"
check crlf-safe-nuspec-version grep -Fq "grep -Eq '^[[:space:]]*<version>4\\.16\\.0</version>[[:space:]]*$'" "$LAUNCHER"
check no-nuspec-fixed-grep bash -c '! grep -E "(nuspec-id|nuspec-version).*grep -Fqx" "$1"' _ "$LAUNCHER"
check sdk grep -Fq "readonly EXPECTED_SDK='8.0.424'" "$LAUNCHER"
check runtime grep -Fq "readonly EXPECTED_RUNTIME='8.0.30'" "$LAUNCHER"
check stryker grep -Fq "readonly EXPECTED_STRYKER='4.16.0'" "$LAUNCHER"
check exact-target-a grep -Fq "$SOURCE_A" "$LAUNCHER"
check exact-target-b grep -Fq "$SOURCE_B" "$LAUNCHER"
check net8 grep -Fq -- '--target-framework net8.0' "$LAUNCHER"
check concurrency grep -Fq -- '--concurrency 1' "$LAUNCHER"
check reporters grep -Fq -- '--reporter json --reporter cleartext --reporter progress' "$LAUNCHER"
check one-transition bash -c 'test "$(grep -Fxc "campaign_count=1" "$1")" -eq 1' _ "$LAUNCHER"
check one-invocation bash -c 'test "$(grep -Foc "run stryker " "$1")" -eq 1' _ "$LAUNCHER"
check no-loop-or-retry bash -c '! grep -Eqi "(^|[^[:alnum:]_])(retry|for|while|until)([^[:alnum:]_]|$)" "$1"' _ "$LAUNCHER"
check transition-before-invocation bash -c 'test "$(grep -nF "campaign_count=1" "$1" | cut -d: -f1)" -lt "$(grep -nF "run stryker " "$1" | cut -d: -f1)"' _ "$LAUNCHER"
check evidence-console grep -Fq '.console' "$LAUNCHER"
check evidence-results grep -Fq 'CAMPAIGN_RUN_DIR/results' "$LAUNCHER"
check evidence-scope grep -Fq 'revision-and-scope.txt' "$LAUNCHER"
check evidence-checksums grep -Fq 'checksums.sha256' "$LAUNCHER"
check count-zero test "$campaign_count" -eq 0
phase=passed
