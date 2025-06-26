# Brick E2 – Iceberg for Geospatial

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/modern-gis/e2-iceberg)

Welcome to **Brick E2** of the Modern GIS Bricks series! In this lab you’ll learn how to build and manage versioned, partitioned geospatial tables using **Apache Iceberg** and interact with them via **PyIceberg**, **Arrow**, and **DuckDB**.

---

## 🔑 Enrollment Code (paid students only)

After you purchase the course, you’ll receive a **one-time enrollment code** by email. To unlock the auto-grader and earn your badge:

1. Fork this repo and clone locally (or open it in Gitpod via the badge above).
2. At the **project root**, create a file named

   ```text
   enrollment_code.txt
   ```
3. Paste **exactly** your one-time code into that file (no extra whitespace).
4. Run through the notebook, commit your changes, and open a PR.

The CI will run both the lab tests and verify your enrollment code before issuing your badge.

---

## 📖 Lab Objectives

1. **Create** an Iceberg table with a spatial schema and partition spec.
2. **Ingest** initial GeoParquet data into Iceberg via PyIceberg.
3. **Explore** versioning: list snapshots and time-travel to past states.
4. **Append** new data and observe additional snapshots.
5. **Perform** schema evolution: add a new column and query across versions.
6. **Inspect** metadata (manifests, snapshots) and manage retention.
7. **Query** the Iceberg table from DuckDB using the Iceberg extension.

---

## 🚀 Quickstart

### 1. In Gitpod

Click **“Open in Gitpod”** at the top of this README and wait for the workspace to spin up.
Jupyter Notebook will be available at **8888**.

### 2. Locally

```bash
git clone https://github.com/modern-gis/e2-iceberg.git
cd e2-iceberg

# create a Python 3.11 venv
python3.11 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# start Jupyter Notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser
```

> If you want to test against a local filesystem catalog instead of S3, edit the catalog configuration in the notebook (e.g. `warehouse = "file:///workspace/iceberg_warehouse"`).

---

## 🧱 Notebook Structure

1. **00-Introduction**
   Overview of Iceberg and lab goals.
2. **01-Setup & Catalog Configuration**
   Install packages, configure PyIceberg catalog (local or S3).
3. **02-Create Iceberg Table**
   Define schema, partition spec, and create table.
4. **03-Ingest Initial Data**
   Read a GeoParquet file and append it to the table.
5. **04-Time Travel & Snapshot History**
   List snapshots and query an older snapshot.
6. **05-Append New Data**
   Commit additional records and validate new snapshot.
7. **06-Schema Evolution**
   Add a column (e.g. `source`) and verify schema update.
8. **07-Metadata Inspection & Maintenance**
   Examine manifests, perform snapshot expiration.
9. **08-Query via DuckDB**
   Enable Iceberg in DuckDB and run SQL against the table.

All code cells marked **`# TODO:`** are where you’ll fill in bucket names, file paths, or implement missing steps.

---

## 📂 Repo Layout

```text
├── .gitpod.Dockerfile          ← custom image (Python 3.11-slim + deps)
├── .gitpod.yml                 ← Gitpod tasks & ports
├── requirements.txt            ← pip dependencies
├── notebook.ipynb              ← Jupyter notebook with TODOs
├── tests/                      ← public pytest suite for core tasks
│   └── test_e2_iceberg.py
├── examples/                   ← sample Parquet files (initial & new)
│   ├── parks.parquet
│   └── new_parks.parquet
├── enrollment_code.txt         ← **YOU** must create this with your code
├── README.md                   ← you are here
└── .github/
    └── workflows/
        └── grade.yml           ← CI: install, pytest, badge issuance
```

---

## ✅ Submission & Badge

1. Run all **public** tests locally:

   ```bash
   pytest -q
   ```
2. Commit your notebook edits **and** `enrollment_code.txt`.
3. Push to your fork and open a pull request.
4. The GitHub Actions CI will run:

   * Public lab tests
   * Enrollment code verification
   * If everything passes, issues your Open Badge via Badgr.

Enjoy learning how to use Iceberg for modern geospatial engineering!
