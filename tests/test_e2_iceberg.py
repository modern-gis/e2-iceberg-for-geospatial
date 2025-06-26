import pytest
from pyiceberg.catalog import load_catalog
from pyiceberg.schema import Schema
import duckdb

# Load the local Iceberg catalog defined in the notebook
CAT = load_catalog(name="local")

def test_table_exists():
    """Test that the Iceberg table 'modern_gis.parks' exists"""
    table = CAT.load_table("modern_gis.parks")
    assert table is not None

def test_initial_data_ingest():
    """Test that initial data was ingested in the first snapshot"""
    table = CAT.load_table("modern_gis.parks")
    snapshots = table.snapshots
    assert len(snapshots) >= 1
    first = CAT.load_table("modern_gis.parks", snapshot_id=snapshots[0].snapshot_id)
    df = first.to_pandas()
    assert df.shape[0] > 0

def test_time_travel_has_multiple_snapshots():
    """Test that at least two snapshots exist after updates"""
    table = CAT.load_table("modern_gis.parks")
    assert len(table.snapshots) >= 2

def test_schema_evolution_column_present():
    """Test that the 'source' column was added via schema evolution"""
    schema = CAT.load_table("modern_gis.parks").schema
    column_names = [field.name for field in schema.columns]
    assert "source" in column_names

def test_duckdb_read_count():
    """Test reading the Iceberg table via DuckDB returns rows"""
    con = duckdb.connect()
    con.execute("INSTALL iceberg; LOAD iceberg;")
    con.execute(
        "CALL iceberg.system.create_catalog('c', 'hadoop', {'warehouse':'s3://YOUR_BUCKET/iceberg_warehouse'});"
    )
    result = con.execute("SELECT COUNT(*) FROM c.modern_gis.parks;").fetchone()[0]
    assert result > 0