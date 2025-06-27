# tests/test_badge_proof.py

import json
import os
import pytest

BADGE_FILE = "badge_proof.json"

def test_badge_file_exists():
    assert os.path.isfile(BADGE_FILE), f"{BADGE_FILE} is missing"

def test_badge_proof_structure():
    with open(BADGE_FILE) as f:
        proof = json.load(f)

    # Must be a dict with the three top-level keys
    assert isinstance(proof, dict)
    for key in ("table", "columns", "snapshots"):
        assert key in proof, f"Missing key: {key}"

    # table: non-empty string "namespace.table"
    table = proof["table"]
    assert isinstance(table, str) and "." in table and table.split(".", 1)[1], "Invalid table name"

    # columns: non-empty list of non-empty strings
    cols = proof["columns"]
    assert isinstance(cols, list) and cols, "columns must be a non-empty list"
    assert all(isinstance(c, str) and c for c in cols), "each column must be a non-empty string"

    # snapshots: non-empty list of ints (or strified ints)
    snaps = proof["snapshots"]
    assert isinstance(snaps, list) and snaps, "snapshots must be a non-empty list"
    assert all(isinstance(s, (int, str)) for s in snaps), "each snapshot must be an int or string"
