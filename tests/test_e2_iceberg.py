import json
import os
import pytest

BADGE_FILE = "badge_proof.json"

def test_badge_file_exists():
    assert os.path.exists(BADGE_FILE), f"{BADGE_FILE} is missing"

def test_badge_proof_structure():
    with open(BADGE_FILE) as f:
        proof = json.load(f)

    # Top‐level keys
    assert isinstance(proof, dict)
    for key in ("table", "columns", "snapshots"):
        assert key in proof, f"Missing key: {key}"

    # table should be a non‐empty string
    assert isinstance(proof["table"], str) and proof["table"], "Invalid table name"

    # columns should be a non‐empty list of strings
    cols = proof["columns"]
    assert isinstance(cols, list) and cols, "columns must be a non‐empty list"
    assert all(isinstance(c, str) and c for c in cols), "each column must be a non‐empty string"

    # snapshots should be a non‐empty list of dicts
    snaps = proof["snapshots"]
    assert isinstance(snaps, list) and snaps, "snapshots must be a non‐empty list"
    for idx, s in enumerate(snaps):
        assert isinstance(s, dict), f"snapshot[{idx}] is not an object"
        # Expect exactly these keys per snapshot
        expected = {"snapshot_id", "timestamp", "row_count"}
        assert set(s.keys()) == expected, f"snapshot[{idx}] keys {set(s.keys())} ≠ {expected}"
        # Validate types
        assert isinstance(s["snapshot_id"], (int, str)), "snapshot_id must be int or str"
        assert isinstance(s["timestamp"], str), "timestamp must be a string"
        assert isinstance(s["row_count"], int) and s["row_count"] >= 0, "row_count must be non-negative int"
