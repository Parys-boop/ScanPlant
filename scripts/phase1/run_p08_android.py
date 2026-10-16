"""Private USB proof runner. No install, network acquisition, training or release.

Requires the existing debuggable Development Client and a private isolated Metro copy.
Restores radio settings and only the port mapping it creates, even on failure.
"""
import argparse
import io
import json
import math
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import tarfile
import time
import urllib.request

import train_experimental as training
from p08_android_experiment import MODEL_SHA, LABELS_SHA


def verified_bundle(bundle):
    manifest_path = bundle / "manifest.json"
    m = json.loads(manifest_path.read_text())
    if (m.get("kind") != "p08_private_android_float32_proof" or len(m["cases"]) != 24
            or m["model"]["sha256"] != MODEL_SHA or m["labels"]["sha256"] != LABELS_SHA
            or m["parity_tolerance"] != 0.0001 or m["stability_tolerance"] != 0.000001
            or m["timed_runs"] != 20 or m["warmup_runs"] != 2
            or m["preprocessing"] != "pipeline_pillow_bilinear_rgb224_float32_0_255_embedded_rescaling"):
        raise ValueError("Different proof contract")
    if any(c["index"] != i or c["input"]["bytes"] != 224*224*3*4 or len(c["probabilities"]) != 12
           for i, c in enumerate(m["cases"])):
        raise ValueError("Different input or label dimensions/order")
    refs = [m["model"], m["labels"], *[c["input"] for c in m["cases"]]]
    if len({r["file"] for r in refs}) != 26:
        raise ValueError("Repeated proof file")
    for ref in refs:
        if not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", ref["file"]):
            raise ValueError("Unsafe bundle filename")
        p = bundle / ref["file"]
        training.read_bound({"path": str(p), "sha256": ref["sha256"]})
        if p.stat().st_size != ref["bytes"]:
            raise ValueError("Size mismatch")
    return m, ["manifest.json", *[r["file"] for r in refs]], training.sha(manifest_path)


def check_report(result, manifest, bundle_id):
    if (result.get("bundleId") != bundle_id or result.get("modelSha256") != MODEL_SHA
            or result.get("labelsSha256") != LABELS_SHA or len(result.get("cases", [])) != 24):
        raise ValueError("Device report identity mismatch")
    max_error = 0.0
    for i, (actual, expected) in enumerate(zip(result["cases"], manifest["cases"])):
        if actual["index"] != i or len(actual["output"]) != 12:
            raise ValueError("Device output order mismatch")
        values = actual["output"]
        if any(not isinstance(x, (int, float)) or not 0 <= x <= 1 for x in values) or abs(sum(values)-1) > 0.0001:
            raise ValueError("Invalid device probabilities")
        max_error = max(max_error, max(abs(a-b) for a,b in zip(values, expected["probabilities"])))
    if (len(result.get("repeats", [])) != 20 or result["latency"]["count"] != 20
            or not all(r["passed"] and r["tolerance"] == 0.000001
                       and 0 <= r["maxAbsoluteError"] <= 0.000001 for r in result["repeats"])):
        raise ValueError("Stability verification failed or missing")
    latency = result["latency"]
    if (result.get("delegate") != "default" or not all(math.isfinite(latency[k]) and latency[k] >= 0
            for k in ("minMs", "medianMs", "p95Ms", "maxMs", "meanMs"))
            or not latency["minMs"] <= latency["medianMs"] <= latency["p95Ms"] <= latency["maxMs"]):
        raise ValueError("Invalid latency/CPU result")
    if max_error > 0.0001 or not result.get("passed"):
        raise ValueError(f"Desktop/device parity failed: {max_error}")
    return {"max_absolute_error": max_error, "tolerance": 0.0001, "cases": 24}


def adb_call(adb, *args, serial=None, data=None, check=True, timeout=None):
    prefix = [str(adb)] + (["-s", serial] if serial else [])
    deadline = timeout if timeout is not None else (8 if args[0] in ("devices", "logcat", "get-state", "reverse") else 45)
    p = subprocess.run(prefix + list(args), input=data, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, timeout=deadline)
    if check and p.returncode:
        raise RuntimeError(p.stderr.decode(errors="replace")[-1200:])
    return p


def mobile_setting_key(sub_id, per_subscription_value):
    if re.fullmatch(r"\d+", sub_id) and per_subscription_value in ("0", "1"):
        return "mobile_data" + sub_id
    return "mobile_data"


def verify_device_hashes(output, expected):
    parsed = {}
    for line in output.splitlines():
        match = re.fullmatch(r"([a-f0-9]{64})\s+(.+)", line.strip())
        if not match or match[2] in parsed:
            raise ValueError("Missing or malformed device checksum acknowledgement")
        parsed[match[2]] = match[1]
    if parsed != expected:
        raise ValueError("Device bytes do not match all expected files")


def require_windows_metro_reachability(adb):
    # WSL readiness does not prove the Windows ADB server can reach Metro.
    if os.name == "posix" and str(adb).lower().endswith(".exe"):
        code = "try { $r=Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:8081/status' -TimeoutSec 3; Write-Output $r.Content } catch { exit 1 }"
        p = subprocess.run(["powershell.exe", "-NoProfile", "-NonInteractive", "-Command", code],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=8)
        if p.returncode or b"packager-status:running" not in p.stdout:
            raise ValueError("Windows ADB cannot reach Metro; resolve the host loopback transport before touching device radios")


def restore_device(call, before, reverses, effect_started, own_reverse, package="com.parysboop.scanplant"):
    """Try every restoration step even if one command fails or USB disappears."""
    errors = []
    def attempt(*parts):
        try:
            p = call(*parts, check=False, timeout=5)
            if p.returncode:
                errors.append(" ".join(parts))
            return p.stdout.decode(errors="replace").strip()
        except Exception as exc:
            errors.append(type(exc).__name__ + ": " + " ".join(parts))
            return None
    radios = {}
    if effect_started:
        attempt("shell", "am", "force-stop", package)
        data_key = next(k for k in before if k.startswith("mobile_data"))
        for key, service in (("wifi_on", "wifi"), (data_key, "data")):
            attempt("shell", "svc", service, "enable" if before[key] == "1" else "disable")
        radios = {k: attempt("shell", "settings", "get", "global", k) for k in before}
    if own_reverse:
        attempt("reverse", "--remove", "tcp:8081")
    after_reverse = attempt("reverse", "--list")
    return {"errors": errors, "radios": radios, "expected": before,
        "radio_settings_match": not effect_started or radios == before,
        "reverse_before": reverses, "reverse_after": after_reverse,
        "reverse_matches": after_reverse is not None and set(after_reverse.splitlines()) == set(reverses.splitlines()),
        "radio_recovery_commands_if_needed": (["adb shell svc wifi " + ("enable" if before["wifi_on"] == "1" else "disable"),
             "adb shell svc data " + ("enable" if before[next(k for k in before if k.startswith("mobile_data"))] == "1" else "disable")]
             if effect_started and (errors or radios != before) else [])}


def run(args):
    bundle = Path(args.bundle).resolve()
    app = Path(args.app).resolve()
    manifest, names, bundle_id = verified_bundle(bundle)
    if not re.fullmatch(r"[a-z][a-z0-9_.]+", args.package):
        raise ValueError("Unsafe package name")
    mapping = json.loads((bundle.parent / "private-case-map.json").read_text())
    canonical_root = Path(mapping[0]["source_sanitized"]["path"]).resolve().parents[1]
    out = training.safe_output(args.evidence, [canonical_root, bundle.parent, app,
        Path(__file__).resolve().parents[2]])
    adb = Path(args.adb)
    devices = adb_call(adb, "devices", "-l").stdout.decode(errors="replace")
    training.write_json(out / "adb-discovery.json", {"output": devices})
    ready = re.findall(r"^(\S+)\s+device\b", devices, re.M)
    if len(ready) != 1:
        training.write_json(out / "status.json", {"status": "blocked_device_connection",
            "unauthorized": "unauthorized" in devices, "physical_inference_executed": False,
            "action": "Unlock the USB-connected Redmi A5 and accept its RSA USB-debugging prompt; adb devices -l must show device."})
        print("BLOCKED_DEVICE_CONNECTION: unlock phone and accept USB-debugging RSA prompt")
        return 2
    serial = ready[0]
    def call(*parts, **kw):
        return adb_call(adb, *parts, serial=serial, **kw)
    def text(*parts):
        return call(*parts).stdout.decode(errors="replace").strip()
    model = text("shell", "getprop", "ro.product.model")
    if model not in ("Redmi A5", "25028RN03L"):
        raise ValueError("Connected device is not the authorized Redmi A5")
    text("shell", "run-as", args.package, "id")  # Requires existing debug build; never replaces APK.
    remote = f"files/p08-experiment/{bundle_id}"
    if call("shell", "run-as", args.package, "test", "-d", remote, check=False).returncode:
        call("shell", "run-as", args.package, "mkdir", "-p", remote)
        stream = io.BytesIO()
        with tarfile.open(fileobj=stream, mode="w") as tar:
            for name in names:
                info = tarfile.TarInfo(name); payload = (bundle/name).read_bytes()
                info.size = len(payload); info.mode = 0o600
                tar.addfile(info, io.BytesIO(payload))
        call("exec-in", "run-as", args.package, "tar", "-xf", "-", "-C", remote, data=stream.getvalue())
    # An existing directory is reused only if every transferred byte still matches.
    expected_hashes = {f"{remote}/{name}": training.sha(bundle/name) for name in names}
    # exec-in streams only stdin; it cannot acknowledge remote checks. Read every hash back.
    checksum = call("exec-out", "run-as", args.package, "sha256sum", *expected_hashes)
    (out / "device-checksums.txt").write_bytes(checksum.stdout)
    verify_device_hashes(checksum.stdout.decode(), expected_hashes)
    # Do not take over another developer's Metro server.
    with socket.socket() as probe:
        if probe.connect_ex(("127.0.0.1", 8081)) == 0:
            raise ValueError("Port 8081 already in use; no server was stopped or reused")
    sub_id = text("shell", "settings", "get", "global", "multi_sim_data_call")
    per_sub = text("shell", "settings", "get", "global", "mobile_data" + sub_id) if sub_id.isdecimal() else "null"
    data_key = mobile_setting_key(sub_id, per_sub)
    before = {k: text("shell", "settings", "get", "global", k) for k in ("wifi_on", data_key)}
    if any(v not in ("0", "1") for v in before.values()):
        raise ValueError("Cannot safely restore unknown radio state")
    reverses = text("reverse", "--list")
    if any("tcp:8081" in line for line in reverses.splitlines()):
        raise ValueError("Existing 8081 mapping was preserved; cannot own this test mapping")
    training.write_json(out / "device-before.json", {"model": model, "serial": serial,
        "android": text("shell", "getprop", "ro.build.version.release"), "radios": before, "reverse": reverses})
    env = {**os.environ, "EXPO_PUBLIC_P08_EXPERIMENTAL_PROOF": "1",
        "EXPO_PUBLIC_P08_EXPERIMENT_ID": bundle_id, "EXPO_PUBLIC_PT05_OFFLINE_PROOF": "0",
        "EXPO_OFFLINE": "1", "EXPO_NO_TELEMETRY": "1", "EXPO_NO_DOTENV": "1", "CI": "1",
        "TMPDIR": str(out / "tmp")}
    (out / "tmp").mkdir(mode=0o700)
    metro = None; own_reverse = False; effect_started = False
    log = (out / "metro.log").open("x")
    try:
        metro = subprocess.Popen(["node", "node_modules/expo/bin/cli", "start", "--dev-client",
            "--localhost", "--port", "8081", "--max-workers", "2"], cwd=app, env=env,
            stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
        deadline = time.monotonic() + 90
        while time.monotonic() < deadline:
            if metro.poll() is not None:
                raise ValueError("Private Metro exited before readiness")
            try:
                with urllib.request.urlopen("http://127.0.0.1:8081/status", timeout=2) as response:
                    if b"packager-status:running" in response.read():
                        break
            except OSError:
                time.sleep(1)
        else:
            raise TimeoutError("Private Metro readiness timeout")
        require_windows_metro_reachability(adb)
        call("reverse", "tcp:8081", "tcp:8081"); own_reverse = True
        effect_started = True
        call("shell", "svc", "wifi", "disable"); call("shell", "svc", "data", "disable")
        time.sleep(2)
        offline = {k: text("shell", "settings", "get", "global", k) for k in before}
        wifi_status = text("shell", "cmd", "wifi", "status").splitlines()[0]
        connectivity = text("shell", "dumpsys", "connectivity")
        (out / "connectivity-offline.txt").write_text(connectivity)
        if (any(v != "0" for v in offline.values()) or wifi_status != "Wifi is disabled"
                or not re.search(r"Active default network:\s*(?:none|null|0)\b", connectivity, re.I)):
            raise ValueError("Offline state not proven; no inference reported as offline")
        start_epoch = int(text("shell", "date", "+%s")) * 1000
        call("shell", "am", "force-stop", args.package)
        call("shell", "am", "start", "-W", "-a", "android.intent.action.VIEW", "-d",
             "exp+scanplant://expo-development-client/?url=http%3A%2F%2F127.0.0.1%3A8081")
        deadline = time.monotonic() + 300
        while time.monotonic() < deadline:
            logs = text("logcat", "-d", "-t", "250", "-v", "raw", "ReactNativeJS:I", "*:S")
            for entry in re.findall(r'P08_EXPERIMENT_ERROR\s+(\{[^\r\n]+\})', logs):
                error = json.loads(entry)
                if error.get("bundleId") == bundle_id and error.get("epochMs", 0) >= start_epoch:
                    raise RuntimeError("Experimental screen: " + error["message"])
            entries = re.findall(r'P08_EXPERIMENT_RESULT\s+(\{[^\r\n]+\})', logs)
            for entry in reversed(entries):
                event = json.loads(entry)
                file = event.get("file", "")
                match = re.fullmatch(r"result-(\d+)\.json", file)
                if event.get("bundleId") == bundle_id and match and int(match[1]) >= start_epoch:
                    raw = call("exec-out", "run-as", args.package, "cat", f"{remote}/{file}").stdout
                    (out / "android-result.json").write_bytes(raw)
                    proof = check_report(json.loads(raw), manifest, bundle_id)
                    training.write_json(out / "status.json", {"status": "physical_proof_passed", "device": model,
                        "physical_inference_executed": True, "offline_radios": offline,
                        "default_network": "none", "usb_metro_only_for_code": True, "host_parity": proof,
                        "result_sha256": training.sha(out / "android-result.json"), "botanical_performance_claim": False})
                    print("PHYSICAL_PROOF_PASSED: private result", out)
                    return 0
            time.sleep(2)
        raise TimeoutError("No fresh device result in 300 seconds")
    finally:
        restoration = restore_device(call, before, reverses, effect_started, own_reverse, args.package)
        if metro and metro.poll() is None:
            os.killpg(metro.pid, signal.SIGTERM)
            try:
                metro.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(metro.pid, signal.SIGKILL); metro.wait()
        log.close()
        training.write_json(out / "restoration.json", restoration)
        if restoration["errors"] or not restoration["radio_settings_match"] or not restoration["reverse_matches"]:
            raise RuntimeError("Device restoration incomplete; inspect private restoration.json")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--adb", required=True)
    p.add_argument("--app", required=True)
    p.add_argument("--bundle", required=True)
    p.add_argument("--evidence", required=True)
    p.add_argument("--package", default="com.parysboop.scanplant")
    args = p.parse_args(); os.umask(0o077)
    raise SystemExit(run(args))


if __name__ == "__main__":
    main()
