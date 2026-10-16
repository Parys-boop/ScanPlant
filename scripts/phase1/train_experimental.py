"""Private, bounded 24-image experiment. Never changes acquisition state or the app.

All paths, predictions, source evidence and trained artifacts belong outside Git.
No discovery, image downloads, canonical promotion or guard transitions occur here.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import platform

ACCEPTED_MANIFEST = "6253fe5cd88db3adb1c9361d00e95207be329c5eef86d81885ceea4757b22fd1"
ACCEPTED_CATALOG = "41191f9f6efb9acc7119dd8d39fa69b8241a62f71d16517bbdf394652f515994"
SEED = 20261015
SIZE = 224


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def write_json(path, obj):
    with Path(path).open("x", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2, sort_keys=True, allow_nan=False)
        f.write("\n")


def read_bound(ref):
    p = Path(ref["path"])
    if not p.is_file() or p.is_symlink() or sha(p) != ref["sha256"]:
        raise ValueError("Missing, symlinked or changed bound input")
    return p


def labels_from_manifest(manifest):
    labels = [dict(index=x["index"], class_id=x["class_id"],
                   scientific_name=x["scientific_name"]) for x in manifest["classes"]
              if x["kind"] == "species"]
    if len(labels) != 12 or [x["index"] for x in labels] != list(range(12)):
        raise ValueError("Expected twelve ordered species, without protection classes")
    if len({x["class_id"] for x in labels}) != 12:
        raise ValueError("Repeated class")
    return labels


def grouped_split(selection, catalog, labels, seed=SEED):
    """Union relationships through reserved/excluded metadata; never load their images."""
    all_items = catalog["items"] + catalog.get("reserved", []) + catalog.get("excluded", [])
    parent = {}

    def find(x):
        parent.setdefault(x, x)
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a, b = find(a), find(b)
        parent[max(a, b)] = min(a, b)

    for item in all_items:
        cid = item["candidate_id"]
        find(cid)
        for signal in item.get("source_series_signals", []):
            union(cid, "series:" + signal)
        representative = item.get("series_representative_selection") or {}
        if representative.get("group_id"):
            union(cid, "series:" + representative["group_id"])
        if representative.get("other_member"):
            union(cid, representative["other_member"])
        for kind in ("original", "sanitized"):
            if (item.get(kind) or {}).get("sha256"):
                union(cid, kind + ":" + item[kind]["sha256"])
    if len({s["candidate_id"] for s in selection}) != len(selection):
        raise ValueError("Repeated candidate")
    class_ids = {x["class_id"] for x in labels}
    groups = defaultdict(list)
    for item in selection:
        if item["class_id"] not in class_ids:
            raise ValueError("Unknown class")
        groups[find(item["candidate_id"])].append(item)
    if any(len({s["class_id"] for s in v}) != 1 for v in groups.values()):
        raise ValueError("Related group has conflicting class labels")
    result = []
    for label in labels:
        cls = label["class_id"]
        candidates = [g for g, v in groups.items() if v[0]["class_id"] == cls]
        if not candidates:
            raise ValueError("Class without a training example")
        candidates.sort(key=lambda g: hashlib.sha256(f"{seed}:{g}".encode()).hexdigest())
        holdout = candidates[0] if len(candidates) >= 2 else None
        for group in candidates:
            for item in groups[group]:
                result.append({**item, "index": label["index"], "group_id": group,
                               "split": "evaluation" if group == holdout else "train"})
    return sorted(result, key=lambda x: (x["index"], x["candidate_id"]))


def prepare_inputs(manifest_path, authorization_path):
    manifest_path = Path(manifest_path)
    if sha(manifest_path) != ACCEPTED_MANIFEST:
        raise ValueError("Not the accepted data manifest")
    m = json.loads(manifest_path.read_text())
    a = json.loads(Path(authorization_path).read_text())
    if (a.get("data_manifest_sha256") != ACCEPTED_MANIFEST
            or a.get("training_authorized") is not True
            or a.get("private_only") is not True
            or a.get("public_use_authorized") is not False
            or not a.get("owner_instruction")):
        raise ValueError("Explicit bounded training authorization required")
    catalog_path = read_bound(m["catalog"])
    if sha(catalog_path) != ACCEPTED_CATALOG:
        raise ValueError("Not the accepted catalog")
    catalog = json.loads(catalog_path.read_text())
    class_path = read_bound(m["class_manifest"])
    labels = labels_from_manifest(json.loads(class_path.read_text()))
    selected = m["selection"]
    by_id = {x["candidate_id"]: x for x in catalog["items"]}
    if len(selected) != 24 or len(by_id) != 24 or set(by_id) != {x["candidate_id"] for x in selected}:
        raise ValueError("Expected exactly the accepted 24 items")
    root = Path(m["canonical_snapshot"]["root"]).resolve(strict=True)
    for item in selected:
        source = by_id[item["candidate_id"]]
        label = source["provisional_label"]
        expected = next(x for x in labels if x["class_id"] == item["class_id"])
        if (not source.get("eligible_for_private_experiment")
                or label["confidence"] != "provisional_source_supported"
                or label["class_id"] != item["class_id"]
                or label["scientific_name"] != expected["scientific_name"]
                or item["scientific_name"] != expected["scientific_name"]):
            raise ValueError("Unaccepted or mismatched label")
        for kind in ("original", "sanitized"):
            if item[kind] != source[kind]:
                raise ValueError("Catalog reference mismatch")
            p = read_bound(item[kind])
            if not p.resolve().is_relative_to(root):
                raise ValueError("Input outside accepted dataset")
    return m, labels, grouped_split(selected, catalog, labels)


def safe_output(path, forbidden):
    path = Path(path).absolute()
    if any(p.is_symlink() for p in [path, *path.parents]):
        raise ValueError("Symlink in output path")
    path = path.resolve()
    if any(path.is_relative_to(Path(p).resolve()) for p in forbidden):
        raise ValueError("Output cannot be inside dataset, accepted package or repository")
    if path.exists():
        raise ValueError("Output already exists; never overwrite a run")
    path.mkdir(mode=0o700, parents=True, exist_ok=False)
    return path


def snapshot(root):
    """Read-only preservation snapshot, including metadata and existing bytes."""
    return {str(p.relative_to(root)): {"sha256": sha(p), "bytes": p.stat().st_size,
            "mtime_ns": p.stat().st_mtime_ns, "mode": p.stat().st_mode & 0o777}
            for p in sorted(Path(root).rglob("*")) if p.is_file()}


def bootstrap_tf():
    # Environment is set before TensorFlow imports; never use the old environment.
    os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
    os.environ.setdefault("TF_ENABLE_ONEDNN_OPTS", "0")
    os.environ.setdefault("TF_DETERMINISTIC_OPS", "1")
    os.environ.setdefault("CUDA_VISIBLE_DEVICES", "-1")
    import tensorflow as tf
    tf.config.threading.set_inter_op_parallelism_threads(1)
    tf.config.threading.set_intra_op_parallelism_threads(2)
    tf.keras.utils.set_random_seed(SEED)
    tf.config.experimental.enable_op_determinism()
    return tf


def load_pixels(rows):
    import numpy as np
    from PIL import Image
    pixels = []
    for row in rows:
        p = read_bound(row["sanitized"])
        with Image.open(p) as image:
            if image.format not in ("JPEG", "PNG") or image.mode != "RGB" or min(image.size) < 1:
                raise ValueError("Unexpected sanitized image encoding")
            row["source_dimensions"] = list(image.size)
            # Resizing is in memory only; the reviewed sanitized copy is never rewritten.
            pixels.append(np.asarray(image.resize((SIZE, SIZE), Image.Resampling.BILINEAR), dtype="float32"))
    return np.stack(pixels)


def tflite_outputs(tf, path, pixels):
    import numpy as np
    interpreter = tf.lite.Interpreter(model_path=str(path), num_threads=2,
        experimental_op_resolver_type=tf.lite.experimental.OpResolverType.BUILTIN_WITHOUT_DEFAULT_DELEGATES)
    interpreter.allocate_tensors()
    inputs, outputs = interpreter.get_input_details(), interpreter.get_output_details()
    if len(inputs) != 1 or len(outputs) != 1:
        raise ValueError("Expected one input and one output")
    inp, out = inputs[0], outputs[0]
    if list(inp["shape"]) != [1, SIZE, SIZE, 3] or list(out["shape"]) != [1, 12]:
        raise ValueError("Wrong exported tensor dimensions")
    results = []
    for pixel in pixels:
        value = pixel[None]
        if np.issubdtype(inp["dtype"], np.integer):
            scale, zero = inp["quantization"]
            if scale <= 0:
                raise ValueError("Invalid input quantization")
            lim = np.iinfo(inp["dtype"])
            value = np.clip(np.rint(value / scale + zero), lim.min, lim.max)
        interpreter.set_tensor(inp["index"], value.astype(inp["dtype"]))
        interpreter.invoke()
        value = interpreter.get_tensor(out["index"])[0].astype("float32")
        if np.issubdtype(out["dtype"], np.integer):
            scale, zero = out["quantization"]
            if scale <= 0:
                raise ValueError("Invalid output quantization")
            value = (value - zero) * scale
        if not np.isfinite(value).all() or value.min() < -0.01 or abs(float(value.sum()) - 1) > 0.06:
            raise ValueError("Invalid exported probabilities")
        results.append(value)
    return np.stack(results), {"input_shape": inp["shape"].tolist(),
        "output_shape": out["shape"].tolist(), "input_dtype": str(inp["dtype"]),
        "output_dtype": str(out["dtype"]), "input_quantization": list(inp["quantization"]),
        "output_quantization": list(out["quantization"])}


def parity_status(name, error):
    tolerance = {"float32": 1e-4, "float16": 0.02, "int8": 0.15}[name]
    passed = error <= tolerance
    if name == "float32" and not passed:
        raise ValueError(f"Required float32 export exceeds numerical tolerance: {error}")
    return {"numerical_parity_passed": passed, "tolerance": tolerance,
            "status": "technically_verified" if passed else "rejected_numerical_drift"}


def verify_exports(tf, output, pixels, labels):
    import numpy as np
    stored = json.loads((output / "labels.json").read_text())
    if stored != labels:
        raise ValueError("Label index mismatch")
    model = tf.keras.models.load_model(output / "model.keras", compile=False)
    expected = model(pixels, training=False).numpy()
    if expected.shape != (len(pixels), 12) or not np.isfinite(expected).all():
        raise ValueError("Invalid native output")
    signatures = tf.saved_model.load(str(output / "saved_model")).signatures
    saved = signatures["serving_default"](rgb=tf.constant(pixels))
    if set(saved) != {"probabilities"} or not np.allclose(saved["probabilities"].numpy(), expected, atol=1e-5):
        raise ValueError("SavedModel output differs from native model")
    checked = {}
    for name in ("float32", "float16", "int8"):
        p = output / f"model-{name}.tflite"
        if not p.exists():
            continue
        actual, contract = tflite_outputs(tf, p, pixels)
        error = float(np.max(np.abs(actual - expected)))
        checked[name] = {**contract, **parity_status(name, error),
            "bytes": p.stat().st_size, "sha256": sha(p),
            "max_absolute_probability_error": error,
            "top1_agreement_with_native": int((actual.argmax(1) == expected.argmax(1)).sum()),
            "technical_cases": len(pixels), "performance_evidence": False}
    if "float32" not in checked:
        raise ValueError("Required float32 export is missing")
    return checked, expected


def execute(args):
    import numpy as np
    script_sha = sha(__file__)
    m, labels, rows = prepare_inputs(args.manifest, args.authorization)
    if sha(args.weights) != args.weights_sha256:
        raise ValueError("Pretrained weight digest mismatch")
    # Weights are already downloaded with provenance. Training performs no downloads.
    root = Path(m["canonical_snapshot"]["root"])
    output = safe_output(args.output, [root, Path(args.manifest).parent, Path(__file__).resolve().parents[2]])
    os.environ["KERAS_HOME"] = str(output / "keras-home")
    before = snapshot(root)
    write_json(output / "canonical-before.json", before)
    write_json(output / "authorization.json", json.loads(Path(args.authorization).read_text()))
    write_json(output / "labels.json", labels)
    write_json(output / "split.json", rows)
    try:
        tf = bootstrap_tf()
        pixels = load_pixels(rows)
        train_idx = [i for i, x in enumerate(rows) if x["split"] == "train"]
        eval_idx = [i for i, x in enumerate(rows) if x["split"] == "evaluation"]
        y = np.array([x["index"] for x in rows], dtype="int64")
        base = tf.keras.applications.MobileNetV2(input_shape=(SIZE, SIZE, 3),
            alpha=1.0, include_top=False, weights=None, pooling="avg")
        base.load_weights(args.weights)
        base.trainable = False
        features = base(tf.keras.applications.mobilenet_v2.preprocess_input(pixels.copy()), training=False)
        head = tf.keras.Sequential([tf.keras.Input((1280,)), tf.keras.layers.Dense(12, activation="softmax")])
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
        loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
        history = []
        for epoch in range(args.epochs):
            # Full training batch; no evaluation access, augmentation or model selection.
            with tf.GradientTape() as tape:
                predictions = head(tf.gather(features, train_idx), training=True)
                loss = loss_fn(y[train_idx], predictions)
            grads = tape.gradient(loss, head.trainable_variables)
            optimizer.apply_gradients(zip(grads, head.trainable_variables))
            history.append({"epoch": epoch + 1, "training_loss": float(loss.numpy())})
        inp = tf.keras.Input((SIZE, SIZE, 3), name="rgb", dtype="float32")
        x = tf.keras.layers.Rescaling(1 / 127.5, offset=-1)(inp)
        model = tf.keras.Model(inp, head(base(x, training=False)), name="private_mobilenetv2_12_provisional")
        model.save(output / "model.keras")

        @tf.function(input_signature=[tf.TensorSpec([None, SIZE, SIZE, 3], tf.float32, name="rgb")])
        def serve(rgb):
            return {"probabilities": model(rgb, training=False)}

        # Freeze variables for a portable inference graph and stable TFLite conversion.
        from tensorflow.python.framework.convert_to_constants import convert_variables_to_constants_v2
        frozen = convert_variables_to_constants_v2(serve.get_concrete_function())
        module = tf.Module()
        module.serve = tf.function(lambda rgb: {"probabilities": frozen(rgb)[0]},
            input_signature=[tf.TensorSpec([None, SIZE, SIZE, 3], tf.float32, name="rgb")])
        tf.saved_model.save(module, str(output / "saved_model"), signatures={"serving_default": module.serve})
        failures = {}
        for kind in ("float32", "float16", "int8"):
            converter = tf.lite.TFLiteConverter.from_saved_model(str(output / "saved_model"))
            converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS]
            if kind == "float16":
                converter.optimizations = [tf.lite.Optimize.DEFAULT]
                converter.target_spec.supported_types = [tf.float16]
            if kind == "int8":
                converter.optimizations = [tf.lite.Optimize.DEFAULT]
                converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
                converter.representative_dataset = lambda: ([pixels[i:i+1]] for i in train_idx)
                converter.inference_input_type = tf.uint8
                converter.inference_output_type = tf.uint8
            try:
                payload = converter.convert()
                (output / f"model-{kind}.tflite").write_bytes(payload)
            except Exception as exc:
                if kind == "float32":
                    raise
                failures[kind] = {"type": type(exc).__name__, "message": str(exc)}
        verified, probabilities = verify_exports(tf, output, pixels, labels)
        confusion = np.zeros((12, 12), dtype="int64")
        predictions = []
        for i in eval_idx:
            pred = int(probabilities[i].argmax())
            confusion[y[i], pred] += 1
            predictions.append({"candidate_id": rows[i]["candidate_id"], "truth_provisional_index": int(y[i]),
                                "predicted_index": pred, "probabilities": probabilities[i].tolist()})
        supported = sorted({int(y[i]) for i in eval_idx})
        write_json(output / "report.json", {
            "schema_version": 1, "status": "experimental_private_only", "seed": SEED,
            "architecture": "MobileNetV2 alpha1 ImageNet frozen + Dense12 softmax", "epochs": args.epochs,
            "input": "RGB float32 0..255; bilinear resize 224x224, embedded scaling -1..1",
            "data_manifest_sha256": sha(args.manifest), "catalog_sha256": ACCEPTED_CATALOG,
            "authorization_sha256": sha(args.authorization), "script_sha256": script_sha,
            "dependencies_lock_sha256": sha(Path(__file__).with_name("requirements-training.lock")),
            "python_version": platform.python_version(), "platform": platform.platform(),
            "class_manifest_sha256": m["class_manifest"]["sha256"],
            "labels_sha256": sha(output / "labels.json"), "split_sha256": sha(output / "split.json"),
            "pretrained_weights_sha256": sha(args.weights), "tensorflow_version": tf.__version__,
            "train_images": len(train_idx), "evaluation_images": len(eval_idx), "augmentation": None,
            "evaluation_correct": int(np.trace(confusion)), "evaluation_total": len(eval_idx),
            "evaluation_covered_class_indices": supported,
            "classes_without_evaluation": [x["class_id"] for x in labels if x["index"] not in supported],
            "confusion_matrix": confusion.tolist(), "evaluation_predictions": predictions,
            "training_loss_diagnostic_only": history, "exports": verified, "export_failures": failures,
            "per_class": {x["class_id"]: dict(Counter(r["split"] for r in rows if r["class_id"] == x["class_id"])) for x in labels},
            "int8_calibration_split": "train_only", "heldout_used_for_tuning": False,
            "independence_asserted": False, "expert_labels": False, "protection_classes_trained": False,
            "product_ready": False, "limitations": ["24 provisional labels; no expert confirmation",
                "One fixed grouped holdout, no separate test set or architecture selection",
                "Unknown specimen/session correlations may remain despite known group isolation",
                "Singleton classes are training-only; six held-out images cannot establish generalization",
                "No OOD rejection, calibration, mobile-device performance or product validation",
                "ImageNet pretraining is external to this small botanical sample; no redistribution approval"]})
    finally:
        after = snapshot(root)
        write_json(output / "preservation.json", {"unchanged": before == after, "file_count": len(before),
                   "before_snapshot_sha256": sha(output / "canonical-before.json")})
        if before != after:
            raise ValueError("Canonical preservation check failed")
        if sha(__file__) != script_sha:
            raise ValueError("Training script changed during execution")
    inventory = {str(p.relative_to(output)): sha(p) for p in sorted(output.rglob("*")) if p.is_file()}
    write_json(output / "artifact-manifest.json", inventory)
    print(json.dumps({"status": "complete_private_experiment", "output": str(output),
                      "artifact_manifest_sha256": sha(output / "artifact-manifest.json")}))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manifest", required=True)
    p.add_argument("--authorization", required=True)
    p.add_argument("--weights")
    p.add_argument("--weights-sha256")
    p.add_argument("--output")
    p.add_argument("--verify-run", help="Reload existing exports without training or modifying the run")
    p.add_argument("--epochs", type=int, default=50)
    args = p.parse_args()
    if not 1 <= args.epochs <= 1000:
        p.error("epochs must be between 1 and 1000")
    os.umask(0o077)
    if args.verify_run:
        m, labels, rows = prepare_inputs(args.manifest, args.authorization)
        run = Path(args.verify_run)
        inventory = json.loads((run / "artifact-manifest.json").read_text())
        for relative, expected in inventory.items():
            if not (run / relative).resolve().is_relative_to(run.resolve()) or sha(run / relative) != expected:
                raise ValueError("Changed or unsafe run artifact")
        if json.loads((run / "split.json").read_text()) != rows:
            raise ValueError("Run split differs from the accepted inputs")
        verified, _ = verify_exports(bootstrap_tf(), run, load_pixels(rows), labels)
        print(json.dumps({"fresh_process_verification": verified, "canonical_mutation": False}))
    else:
        if not all((args.weights, args.weights_sha256, args.output)):
            p.error("Training requires --weights, --weights-sha256 and --output")
        execute(args)


if __name__ == "__main__":
    main()
