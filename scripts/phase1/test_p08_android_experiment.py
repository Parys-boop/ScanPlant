import json
from pathlib import Path
import subprocess
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from p08_android_experiment import upcast_half_storage, MODEL_SHA, LABELS_SHA, file_ref
from run_p08_android import check_report, restore_device, run, mobile_setting_key, verify_device_hashes, adb_call, require_windows_metro_reachability


class HostContractTests(unittest.TestCase):
    def fixture(self):
        p = [1.0] + [0.0] * 11
        manifest = {"cases": [{"probabilities": p} for _ in range(24)]}
        result = {"bundleId": "a"*64, "modelSha256": MODEL_SHA, "labelsSha256": LABELS_SHA,
            "delegate": "default", "passed": True,
            "cases": [{"index": i, "output": p} for i in range(24)],
            "repeats": [{"passed": True, "tolerance": 0.000001, "maxAbsoluteError": 0.0} for _ in range(20)],
            "latency": {"count": 20, "minMs": 1, "medianMs": 2, "p95Ms": 3, "maxMs": 4, "meanMs": 2}}
        return manifest, result

    def test_checks_actual_device_vectors_instead_of_trusting_pass_flag(self):
        m, r = self.fixture()
        self.assertEqual(check_report(r, m, "a"*64)["max_absolute_error"], 0)
        r["cases"][0]["output"] = [0.999] + [0.001] + [0.0]*10
        with self.assertRaisesRegex(ValueError, "parity"):
            check_report(r, m, "a"*64)

    def test_changed_model_label_order_or_stale_bundle_cannot_pass(self):
        for field, changed in (("modelSha256", "wrong"), ("labelsSha256", "wrong"), ("bundleId", "old")):
            m, r = self.fixture(); r[field] = changed
            with self.assertRaises(ValueError): check_report(r, m, "a"*64)
        m, r = self.fixture(); r["cases"][0]["index"] = 1
        with self.assertRaises(ValueError): check_report(r, m, "a"*64)

    def test_nonfinite_probabilities_fail(self):
        m, r = self.fixture(); r["cases"][0]["output"] = [float("nan")] * 12
        with self.assertRaises(ValueError): check_report(r, m, "a"*64)

    def test_missing_repetition_or_invalid_latency_fails(self):
        m, r = self.fixture(); r["repeats"].pop()
        with self.assertRaises(ValueError): check_report(r, m, "a"*64)
        m, r = self.fixture(); r["latency"]["medianMs"] = -1
        with self.assertRaises(ValueError): check_report(r, m, "a"*64)

    def test_stability_cannot_hide_error_in_pass_flag(self):
        m, r = self.fixture(); r["repeats"][0]["maxAbsoluteError"] = 0.001
        with self.assertRaises(ValueError): check_report(r, m, "a"*64)

    def test_restore_attempts_all_steps_after_transport_failure(self):
        calls = []
        def failing_call(*args, **kwargs):
            calls.append(args)
            if args[:4] == ("shell", "svc", "wifi", "enable"):
                raise TimeoutError("USB lost")
            return subprocess.CompletedProcess(args, 0, stdout=b"0\n", stderr=b"")
        restored = restore_device(failing_call, {"wifi_on": "1", "mobile_data": "0"}, "", True, True)
        self.assertTrue(restored["errors"])
        self.assertIn(("shell", "svc", "data", "disable"), calls)
        self.assertIn(("reverse", "--remove", "tcp:8081"), calls)
        self.assertFalse(restored["radio_settings_match"])
        self.assertEqual(restored["radio_recovery_commands_if_needed"], ['adb shell svc wifi enable', 'adb shell svc data disable'])

    def test_transport_timeouts_are_bounded_and_cleanup_uses_short_deadline(self):
        with patch('run_p08_android.subprocess.run', return_value=subprocess.CompletedProcess([],0,stdout=b'',stderr=b'')) as process:
            adb_call('adb', 'logcat', '-d')
            self.assertEqual(process.call_args.kwargs['timeout'], 8)
            adb_call('adb', 'shell', 'svc', 'wifi', 'enable', timeout=5)
            self.assertEqual(process.call_args.kwargs['timeout'], 5)

    def test_wsl_readiness_cannot_substitute_for_windows_adb_host_reachability(self):
        with patch('run_p08_android.subprocess.run', return_value=subprocess.CompletedProcess([],1,stdout=b'',stderr=b'')):
            with self.assertRaisesRegex(ValueError, "before touching device radios"):
                require_windows_metro_reachability('adb.exe')
        with patch('run_p08_android.subprocess.run', return_value=subprocess.CompletedProcess([],0,stdout=b'packager-status:running',stderr=b'')):
            require_windows_metro_reachability('adb.exe')

    def test_never_removes_unowned_reverse_mapping(self):
        calls = []
        def call(*args, **kwargs):
            calls.append(args)
            return subprocess.CompletedProcess(args, 0, stdout=b"existing\n", stderr=b"")
        restore_device(call, {"wifi_on": "0", "mobile_data": "0"}, "existing", False, False)
        self.assertEqual(calls, [("reverse", "--list")])

    def test_android15_per_subscription_flag_overrides_stale_legacy_flag(self):
        self.assertEqual(mobile_setting_key("7", "0"), "mobile_data7")
        self.assertEqual(mobile_setting_key("7", "1"), "mobile_data7")
        self.assertEqual(mobile_setting_key("-1", "null"), "mobile_data")

    def test_checksum_requires_remote_acknowledgement_for_every_file(self):
        expected = {"files/private/model.tflite": "a"*64, "files/private/case.f32": "b"*64}
        for wrong in ("", "a"*64+"  files/private/model.tflite\n", "a"*64+"  files/private/model.tflite\n"+"c"*64+"  files/private/case.f32\n"):
            with self.assertRaises(ValueError): verify_device_hashes(wrong, expected)
        verify_device_hashes("".join(f"{h}  {p}\n" for p,h in expected.items()), expected)

    def test_file_reference_binds_exact_bytes(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/"tensor.f32"; p.write_bytes(b"example")
            before = file_ref(p); p.write_bytes(b"changed")
            self.assertNotEqual(before["sha256"], file_ref(p)["sha256"])

    def test_unauthorized_device_does_not_start_transfer_radios_or_metro(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d); out = root/"evidence"; out.mkdir()
            bundle = root/"prepared/bundle"; bundle.mkdir(parents=True)
            (bundle.parent/"private-case-map.json").write_text(json.dumps([{"source_sanitized": {"path": str(root/"canonical/quarantine/image")}}]))
            args = SimpleNamespace(bundle=str(bundle), app=str(root/"app"), evidence=str(out), adb="adb", package="com.parysboop.scanplant")
            response = subprocess.CompletedProcess([], 0, stdout=b"List of devices attached\nexample unauthorized\n", stderr=b"")
            with patch('run_p08_android.verified_bundle', return_value=({}, [], 'a'*64)), \
                 patch('run_p08_android.training.safe_output', return_value=out), \
                 patch('run_p08_android.adb_call', return_value=response) as adb, \
                 patch('run_p08_android.subprocess.Popen') as metro:
                self.assertEqual(run(args), 2)
                self.assertEqual(adb.call_count, 1); metro.assert_not_called()
                self.assertFalse(json.loads((out/"status.json").read_text())["physical_inference_executed"])


class PrecisionAblationTests(unittest.TestCase):
    def half_model(self):
        import numpy as np
        import flatbuffers
        from tensorflow.lite.python import schema_py_generated as s
        model = s.ModelT(); model.version = 3
        empty = s.BufferT(); data = s.BufferT()
        data.data = np.frombuffer(np.array([0.1, 100.125], dtype="<f2").tobytes(), dtype="uint8")
        model.buffers = [empty, data]
        op = s.OperatorCodeT(); op.builtinCode = s.BuiltinOperator.DEQUANTIZE
        op.deprecatedBuiltinCode = s.BuiltinOperator.DEQUANTIZE; model.operatorCodes = [op]
        graph = s.SubGraphT(); graph.tensors = []; graph.operators = []
        for i in range(2):
            a = s.TensorT(); a.type = s.TensorType.FLOAT16; a.buffer = 1; a.shape = [2]; a.name = f"half{i}"
            b = s.TensorT(); b.type = s.TensorType.FLOAT32; b.buffer = 0; b.shape = [2]; b.name = f"float{i}"
            graph.tensors.extend([a,b]); dq = s.OperatorT(); dq.opcodeIndex = 0; dq.inputs = [i*2]; dq.outputs = [i*2+1]
            graph.operators.append(dq)
        graph.inputs = []; graph.outputs = [1,3]; model.subgraphs = [graph]
        builder = flatbuffers.Builder(1024); builder.Finish(model.Pack(builder), file_identifier=b"TFL3")
        return bytes(builder.Output())

    def test_upcast_changes_storage_only_and_preserves_shared_rounded_constants(self):
        import numpy as np
        from tensorflow.lite.python import schema_py_generated as s
        raw = self.half_model(); original = bytes(raw)
        controlled, count = upcast_half_storage(raw)
        model = s.ModelT.InitFromObj(s.Model.GetRootAsModel(controlled,0))
        self.assertEqual(count, 2); self.assertEqual(raw, original)
        self.assertEqual(len(model.subgraphs[0].operators), 0)
        self.assertEqual(list(model.subgraphs[0].outputs), [0,2])
        values = np.frombuffer(model.buffers[1].data.tobytes(), dtype="<f4")
        np.testing.assert_array_equal(values, np.array([0.1,100.125],dtype="<f2").astype("<f4"))


if __name__ == "__main__":
    unittest.main()
