#!/bin/bash
set -u -o pipefail
RUN_DIR=/tmp/scanplant-p01r1-final-foreground-O5Xa2Q
REPO=/home/administradorarthur/code/scanplant-work/.bianchini-worktrees/ScanPlant/v1-p01
DOTNET=/home/administradorarthur/.dotnet-scanplant-8/dotnet
export HOME=/home/administradorarthur USER=administradorarthur LOGNAME=administradorarthur SHELL=/bin/bash TMPDIR=/tmp
export DOTNET_ROOT=/home/administradorarthur/.dotnet-scanplant-8 DOTNET_HOST_PATH=/home/administradorarthur/.dotnet-scanplant-8/dotnet
export DOTNET_CLI_HOME=/home/administradorarthur DOTNET_MULTILEVEL_LOOKUP=0 NUGET_PACKAGES=/home/administradorarthur/.nuget/packages
export PATH=/home/administradorarthur/.dotnet-scanplant-8:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
cd "$REPO/ScanPlantAPI/ScanPlantAPI.Tests/MutationHarness"
cmd="$DOTNET tool run dotnet-stryker --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --mutate Services/ExternalProviders/ExternalFallbackUploadValidator.cs --mutate Services/ExternalProviders/ExternalFallbackService.cs --reporter json --reporter cleartext --reporter progress --verbosity trace --log-to-file --skip-version-check --output $RUN_DIR/results"
printf '%s\n' "$cmd" > "$RUN_DIR/command.txt"
env | sort > "$RUN_DIR/environment.txt"
printf '%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$RUN_DIR/start.utc"
printf '%s\n' "$$" > "$RUN_DIR/pid.txt"
start=$(date +%s)
"$DOTNET" tool run dotnet-stryker --project ScanPlantAPI.csproj --target-framework net8.0 --concurrency 1 --mutate Services/ExternalProviders/ExternalFallbackUploadValidator.cs --mutate Services/ExternalProviders/ExternalFallbackService.cs --reporter json --reporter cleartext --reporter progress --verbosity trace --log-to-file --skip-version-check --output "$RUN_DIR/results" > "$RUN_DIR/console.log" 2>&1
status=$?
end=$(date +%s)
printf '%s\n' "$status" > "$RUN_DIR/exit-code.txt"
printf '%s\n' "$((end-start))" > "$RUN_DIR/duration-seconds.txt"
printf '%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$RUN_DIR/end.utc"
find "$RUN_DIR" -type f -printf '%P\n' | sort > "$RUN_DIR/file-inventory.txt"
exit "$status"
