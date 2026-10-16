"""Prepare private exact-input Android proof and diagnose existing exports; never train.

Use the isolated training Python. Inputs/artifacts and device results stay outside Git.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil

import train_experimental as training

MODEL_SHA = "82c7bab4de164c70cd97e6651397ab19078437852ea8f2246d99ebdd2dafbf3c"
LABELS_SHA = "0299f64143a228cc0268ee8f92917ccb71f0e9971b3396dc5bb7cb12785a3c47"


def file_ref(path):
    data = Path(path).read_bytes()
    return {"file": Path(path).name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
            "md5": hashlib.md5(data, usedforsecurity=False).hexdigest()}


def verify_run(run):
    inventory = json.loads((run / "artifact-manifest.json").read_text())
    for name in ("model-float32.tflite", "model-float16.tflite", "model-int8.tflite",
                 "model.keras", "labels.json", "report.json", "split.json"):
        if training.sha(run / name) != inventory[name]:
            raise ValueError("Changed input artifact")
    if training.sha(run / "model-float32.tflite") != MODEL_SHA or training.sha(run / "labels.json") != LABELS_SHA:
        raise ValueError("Different experiment")


def upcast_half_storage(payload):
    """Controlled CPU ablation: preserve graph and rounded values, remove half storage."""
    import numpy as np
    import flatbuffers
    from tensorflow.lite.python import schema_py_generated as schema
    model = schema.ModelT.InitFromObj(schema.Model.GetRootAsModel(payload, 0))
    graph = model.subgraphs[0]
    half = set()
    converted_buffers = set()
    for i, tensor in enumerate(graph.tensors):
        if tensor.type == schema.TensorType.FLOAT16:
            buffer = model.buffers[tensor.buffer]
            if buffer.data is None or not len(buffer.data):
                raise ValueError("Expected stored half constant, not half activation")
            if tensor.buffer not in converted_buffers:
                values = np.frombuffer(buffer.data.tobytes(), dtype="<f2").astype("<f4")
                buffer.data = np.frombuffer(values.tobytes(), dtype="uint8")
                converted_buffers.add(tensor.buffer)
            tensor.type = schema.TensorType.FLOAT32
            half.add(i)
    rewrites = {}
    keep = []
    for op in graph.operators:
        code = model.operatorCodes[op.opcodeIndex]
        builtin = max(code.builtinCode, code.deprecatedBuiltinCode)
        if builtin == schema.BuiltinOperator.DEQUANTIZE and int(op.inputs[0]) in half:
            rewrites[int(op.outputs[0])] = int(op.inputs[0])
        else:
            keep.append(op)
    if not half or len(rewrites) != len(half):
        raise ValueError("Unexpected half dequantization graph")
    for op in keep:
        op.inputs = np.array([rewrites.get(int(i), int(i)) for i in op.inputs], dtype="int32")
    graph.outputs = np.array([rewrites.get(int(i), int(i)) for i in graph.outputs], dtype="int32")
    graph.operators = keep
    builder = flatbuffers.Builder(1024)
    builder.Finish(model.Pack(builder), file_identifier=b"TFL3")
    return bytes(builder.Output()), len(half)


def make_interpreter(tf, path, preserve=False):
    interpreter = tf.lite.Interpreter(model_path=str(path), num_threads=2,
        experimental_preserve_all_tensors=preserve,
        experimental_op_resolver_type=tf.lite.experimental.OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES)
    interpreter.allocate_tensors()
    return interpreter


def intermediate_diagnostics(tf, run, pixels, rows):
    """Matched tensor ranges; boundary occupancy alone is not evidence of clipping."""
    import numpy as np
    float_model = make_interpreter(tf, run / "model-float32.tflite", True)
    quant_model = make_interpreter(tf, run / "model-int8.tflite", True)
    floats = {d["name"]: d for d in float_model.get_tensor_details()}
    quant = {d["name"]: d for d in quant_model.get_tensor_details()}
    produced_float = {int(i) for op in float_model._get_ops_details() for i in op["outputs"]}
    produced_quant = {int(i) for op in quant_model._get_ops_details() for i in op["outputs"]}
    matches = []
    for name, q in quant.items():
        f = floats.get(name)
        if f is not None and q["dtype"] == np.int8 and f["dtype"] == np.float32 and q["quantization"][0] > 0:
            if (f["index"] in produced_float and q["index"] in produced_quant
                    and list(f["shape"]) == list(q["shape"]) and len(q["shape"]) in (2, 4) and q["shape"][0] == 1):
                matches.append((name, f, q))
    stats = {name: {"name": name, "quantization": list(q["quantization"]),
             "max_absolute_error": 0.0, "train_outside_range": 0, "evaluation_outside_range": 0,
             "train_values": 0, "evaluation_values": 0} for name, f, q in matches}
    for pixel, row in zip(pixels, rows):
        for model in (float_model, quant_model):
            d = model.get_input_details()[0]
            value = pixel[None]
            if d["dtype"] == np.uint8:
                scale, zero = d["quantization"]
                value = np.clip(np.rint(value / scale + zero), 0, 255)
            model.set_tensor(d["index"], value.astype(d["dtype"]))
            model.invoke()
        for name, f, q in matches:
            fv = float_model.get_tensor(f["index"])
            qv = quant_model.get_tensor(q["index"])
            scale, zero = q["quantization"]
            restored = (qv.astype("float32") - zero) * scale
            item = stats[name]; split = row["split"]
            item["max_absolute_error"] = max(item["max_absolute_error"], float(np.max(np.abs(restored - fv))))
            # Floating reference outside the representable range, not proof of one causal defect.
            lo, hi = (-128 - zero) * scale, (127 - zero) * scale
            item[split + "_outside_range"] += int(((fv < lo) | (fv > hi)).sum())
            item[split + "_values"] += int(fv.size)
    return list(stats.values())


def prepare_and_diagnose(args):
    import numpy as np
    run = Path(args.run).resolve()
    verify_run(run)
    m, labels, rows = training.prepare_inputs(args.manifest, args.authorization)
    if json.loads((run / "split.json").read_text()) != rows:
        raise ValueError("Run split differs")
    out = training.safe_output(args.output, [m["canonical_snapshot"]["root"],
        Path(args.manifest).parent, run.parent, Path(__file__).resolve().parents[2]])
    os.environ["KERAS_HOME"] = str(out / "keras-home")
    tf = training.bootstrap_tf()
    pixels = training.load_pixels(rows)
    model = tf.keras.models.load_model(run / "model.keras", compile=False)
    native = model(pixels, training=False).numpy()
    outputs = {}
    for name in ("float32", "float16", "int8"):
        outputs[name], _ = training.tflite_outputs(tf, run / f"model-{name}.tflite", pixels)
    controlled, half_count = upcast_half_storage((run / "model-float16.tflite").read_bytes())
    (out / "controlled-half-upcast.tflite").write_bytes(controlled)
    upcast, _ = training.tflite_outputs(tf, out / "controlled-half-upcast.tflite", pixels)
    errors = {name: {"max_absolute_error_vs_native": float(np.max(np.abs(value-native))),
                    "max_absolute_error_vs_float32": float(np.max(np.abs(value-outputs["float32"]))),
                    "top1_agreement_with_native": int((value.argmax(1) == native.argmax(1)).sum()),
                    "technical_cases": len(rows), **training.parity_status(name, float(np.max(np.abs(value-native))))}
              for name, value in outputs.items()}
    diagnostic = {"schema_version": 1, "models_unchanged": True, "retraining": False,
        "input": "exact pipeline Pillow bilinear RGB224 Float32 0..255; embedded -1..1 rescaling",
        "errors": errors, "float16_control": {"half_constant_count": half_count,
            "max_error_half_vs_upcast": float(np.max(np.abs(outputs["float16"]-upcast))),
            "max_error_upcast_vs_float32": float(np.max(np.abs(upcast-outputs["float32"]))),
            "meaning": "Same rounded constants stored in float32; no training, calibration or tolerance change"},
        "int8": {"input_quantization": [1.0, 0], "output_quantization": [1/256, 0],
            "calibration": "unchanged 18 train images only, no evaluation data",
            "matched_intermediates": intermediate_diagnostics(tf, run, pixels, rows),
            "range_interpretation": "Float32 reference outside INT8 range is a coverage limitation signal, not proof of a collector/converter defect. Zero at ReLU boundary is not treated as clipping."},
        "criteria_origin": "Engineering thresholds fixed in previous experiment, not official accuracy standards",
        "references": ["https://developers.google.com/edge/litert/conversion/tensorflow/quantization/post_training_float16_quant",
            "https://developers.google.com/edge/litert/conversion/tensorflow/quantization/post_training_integer_quant",
            "https://github.com/mrousavy/react-native-fast-tflite/blob/v2.0.0/src/TensorflowLite.ts"]}
    training.write_json(out / "diagnosis.json", diagnostic)
    bundle = out / "bundle"; bundle.mkdir(mode=0o700)
    shutil.copyfile(run / "model-float32.tflite", bundle / "model.tflite")
    shutil.copyfile(run / "labels.json", bundle / "labels.json")
    cases = []
    mapping = []
    for i, (pixel, row) in enumerate(zip(pixels, rows)):
        path = bundle / f"case-{i:02d}.f32"; path.write_bytes(pixel.astype("<f4").tobytes())
        cases.append({"index": i, "input": file_ref(path), "probabilities": outputs["float32"][i].tolist()})
        mapping.append({"case_index": i, "candidate_id": row["candidate_id"], "split": row["split"],
                        "source_sanitized": row["sanitized"]})
    manifest = {"schema_version": 1, "kind": "p08_private_android_float32_proof",
        "model": file_ref(bundle / "model.tflite"), "labels": file_ref(bundle / "labels.json"),
        "preprocessing": "pipeline_pillow_bilinear_rgb224_float32_0_255_embedded_rescaling",
        "parity_tolerance": 0.0001, "stability_tolerance": 0.000001,
        "warmup_runs": 2, "timed_runs": 20, "cases": cases}
    training.write_json(bundle / "manifest.json", manifest)
    training.write_json(out / "private-case-map.json", mapping)
    training.write_json(out / "prepare-result.json", {"bundle_id": training.sha(bundle / "manifest.json"),
        "manifest": str(bundle / "manifest.json"), "model_sha256": MODEL_SHA,
        "labels_sha256": LABELS_SHA, "case_count": 24, "script_sha256": training.sha(__file__),
        "training_script_sha256": training.sha(training.__file__), "dataset_mutation": False})
    print(json.dumps({"output": str(out), "bundle_id": training.sha(bundle / "manifest.json"), "errors": errors}))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--run", required=True)
    p.add_argument("--manifest", required=True)
    p.add_argument("--authorization", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    os.umask(0o077)
    prepare_and_diagnose(args)


if __name__ == "__main__":
    main()
