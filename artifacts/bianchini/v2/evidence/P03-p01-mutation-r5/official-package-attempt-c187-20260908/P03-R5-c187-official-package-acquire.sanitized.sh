#!/usr/bin/env bash
set -uo pipefail

readonly run_dir='<RUN_DIR>'
readonly package_url='https://api.nuget.org/v3-flatcontainer/dotnet-stryker/4.16.0/dotnet-stryker.4.16.0.nupkg'
readonly checksum_url='https://api.nuget.org/v3-flatcontainer/dotnet-stryker/4.16.0/dotnet-stryker.4.16.0.nupkg.sha512'
readonly package_path="$run_dir/local-feed/dotnet-stryker.4.16.0.nupkg"
readonly checksum_path="$run_dir/local-feed/dotnet-stryker.4.16.0.nupkg.sha512"
readonly dotnet_root='<HOME>/.dotnet-scanplant-8'
readonly dotnet_host="$dotnet_root/dotnet"
readonly cached_package='<HOME>/.nuget/packages/dotnet-stryker/4.16.0/dotnet-stryker.4.16.0.nupkg'

mkdir -p "$run_dir/local-feed" "$run_dir/home" "$run_dir/tmp"
phase='initializing'
signature_exit='not-run'

finalize() {
  local shell_exit=$?
  cat >"$run_dir/execution-summary.txt" <<EOF
phase=$phase
package_url=$package_url
checksum_url=$checksum_url
signature_exit=$signature_exit
network_source=api.nuget.org HTTPS only
EOF
  sha256sum "$run_dir/P03-R5-c187-official-package-acquire.sh" >"$run_dir/acquisition-launcher.sha256" 2>/dev/null || true
  (
    cd "$run_dir"
    find . -type f ! -name checksums.sha256 -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
    sha256sum -c checksums.sha256 > checksums.verify.txt 2>&1
  ) || true
  exit "$shell_exit"
}
trap finalize EXIT

[ -x "$dotnet_host" ] || { phase='dotnet-missing'; exit 10; }
printf 'package_url=%s\nchecksum_url=%s\ndownload_started_utc=%s\n' "$package_url" "$checksum_url" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >"$run_dir/acquisition-request.txt"

curl --proto '=https' --proto-redir '=https' --max-redirs 0 --tlsv1.2 --fail --show-error --silent \
  --dump-header "$run_dir/package.headers" \
  --write-out 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nscheme=%{scheme}\nssl_verify_result=%{ssl_verify_result}\nsize_download=%{size_download}\n' \
  --output "$package_path" "$package_url" >"$run_dir/package.curl-meta" 2>"$run_dir/package.curl-stderr" || { phase='package-download-failed'; exit 11; }
curl --proto '=https' --proto-redir '=https' --max-redirs 0 --tlsv1.2 --fail --show-error --silent \
  --dump-header "$run_dir/checksum.headers" \
  --write-out 'url_effective=%{url_effective}\nhttp_code=%{http_code}\nscheme=%{scheme}\nssl_verify_result=%{ssl_verify_result}\nsize_download=%{size_download}\n' \
  --output "$checksum_path" "$checksum_url" >"$run_dir/checksum.curl-meta" 2>"$run_dir/checksum.curl-stderr" || { phase='checksum-download-failed'; exit 12; }
printf 'download_completed_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >>"$run_dir/acquisition-request.txt"

/usr/bin/rg -Fxq "url_effective=$package_url" "$run_dir/package.curl-meta" || { phase='package-origin-mismatch'; exit 13; }
/usr/bin/rg -Fxq "url_effective=$checksum_url" "$run_dir/checksum.curl-meta" || { phase='checksum-origin-mismatch'; exit 14; }
/usr/bin/rg -Fxq 'http_code=200' "$run_dir/package.curl-meta" || { phase='package-http-status'; exit 15; }
/usr/bin/rg -Fxq 'http_code=200' "$run_dir/checksum.curl-meta" || { phase='checksum-http-status'; exit 16; }
/usr/bin/rg -Fxq 'scheme=https' "$run_dir/package.curl-meta" || { phase='package-scheme'; exit 17; }
/usr/bin/rg -Fxq 'scheme=https' "$run_dir/checksum.curl-meta" || { phase='checksum-scheme'; exit 18; }
/usr/bin/rg -Fxq 'ssl_verify_result=0' "$run_dir/package.curl-meta" || { phase='package-tls'; exit 19; }
/usr/bin/rg -Fxq 'ssl_verify_result=0' "$run_dir/checksum.curl-meta" || { phase='checksum-tls'; exit 20; }

{
  printf 'package_bytes='; stat -c '%s' "$package_path"
  printf 'checksum_bytes='; stat -c '%s' "$checksum_path"
} >"$run_dir/file-sizes.txt"
sha256sum "$package_path" >"$run_dir/package.sha256"
sha512sum "$package_path" | awk '{print $1}' >"$run_dir/package.sha512.hex"
openssl dgst -sha512 -binary "$package_path" | base64 -w0 >"$run_dir/package.sha512.base64"
tr -d '\r\n' <"$checksum_path" >"$run_dir/package.sha512.official.base64"
{
  printf 'sha512_hex_length='; wc -c <"$run_dir/package.sha512.hex"
  printf 'sha512_base64_calculated_length='; wc -c <"$run_dir/package.sha512.base64"
  printf 'sha512_base64_official_length='; wc -c <"$run_dir/package.sha512.official.base64"
  printf 'sha512_hex_format='; if /usr/bin/rg -qx '[0-9a-f]{128}' "$run_dir/package.sha512.hex"; then printf 'valid-lowercase-hex\n'; else printf 'invalid\n'; fi
  printf 'sha512_base64_calculated_format='; if /usr/bin/rg -qx '[A-Za-z0-9+/]{86}==' "$run_dir/package.sha512.base64"; then printf 'valid-base64-64-bytes\n'; else printf 'invalid\n'; fi
  printf 'sha512_base64_official_format='; if /usr/bin/rg -qx '[A-Za-z0-9+/]{86}==' "$run_dir/package.sha512.official.base64"; then printf 'valid-base64-64-bytes\n'; else printf 'invalid\n'; fi
} >"$run_dir/sha512-formats-and-lengths.txt"
cmp -s "$run_dir/package.sha512.base64" "$run_dir/package.sha512.official.base64" || { phase='official-sha512-mismatch'; exit 21; }
printf 'match\n' >"$run_dir/package.sha512.normalized-comparison.txt"

nuspec_entry="$(unzip -Z1 "$package_path" | /usr/bin/rg '(^|/)dotnet-stryker\.nuspec$')"
[ -n "$nuspec_entry" ] || { phase='nuspec-missing'; exit 22; }
unzip -p "$package_path" "$nuspec_entry" >"$run_dir/dotnet-stryker.nuspec" || { phase='nuspec-extract-failed'; exit 23; }
/usr/bin/rg -q '<id>dotnet-stryker</id>' "$run_dir/dotnet-stryker.nuspec" || { phase='package-id-mismatch'; exit 24; }
/usr/bin/rg -q '<version>4\.16\.0</version>' "$run_dir/dotnet-stryker.nuspec" || { phase='package-version-mismatch'; exit 25; }

printf '%q ' env DOTNET_NUGET_SIGNATURE_VERIFICATION=true NUGET_CERT_REVOCATION_MODE=offline DOTNET_ROOT="$dotnet_root" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_HOME="$run_dir/home" HOME="$run_dir/home" TMPDIR="$run_dir/tmp" PATH="$dotnet_root:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" "$dotnet_host" nuget verify --all "$package_path" >"$run_dir/nuget-verify.command"
printf '\n' >>"$run_dir/nuget-verify.command"
set +e
env DOTNET_NUGET_SIGNATURE_VERIFICATION=true NUGET_CERT_REVOCATION_MODE=offline DOTNET_ROOT="$dotnet_root" DOTNET_MULTILEVEL_LOOKUP=0 DOTNET_CLI_HOME="$run_dir/home" HOME="$run_dir/home" TMPDIR="$run_dir/tmp" PATH="$dotnet_root:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin" DOTNET_NOLOGO=1 DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1 DOTNET_CLI_TELEMETRY_OPTOUT=1 "$dotnet_host" nuget verify --all "$package_path" >"$run_dir/nuget-verify.stdout" 2>"$run_dir/nuget-verify.stderr"
signature_exit=$?
set -e
printf '%s\n' "$signature_exit" >"$run_dir/nuget-verify.exit"
[ "$signature_exit" = '0' ] || { phase='signature-verify-failed'; exit 26; }

if [ -f "$cached_package" ]; then
  sha256sum "$cached_package" >"$run_dir/cache-package.sha256"
  sha512sum "$cached_package" | awk '{print $1}' >"$run_dir/cache-package.sha512.hex"
  openssl dgst -sha512 -binary "$cached_package" | base64 -w0 >"$run_dir/cache-package.sha512.base64"
  if cmp -s "$package_path" "$cached_package"; then printf 'byte-identical\n'; else printf 'byte-different\n'; fi >"$run_dir/cache-package-byte-comparison.txt"
fi

phase='passed'
exit 0
