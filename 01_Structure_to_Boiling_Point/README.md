# Module 1: Structure to Boiling Point

This module introduces a complete materials-analytics workflow: start with chemical identifiers and structures, build machine-readable features, then evaluate models that predict boiling point.

## Learning outcomes

By the end of the module, students should be able to:

- distinguish chemical identifiers, SMILES, descriptors, functional groups, and fingerprints;
- explain why a feature representation affects model performance;
- train and compare regression models for boiling-point prediction; and
- describe the evidence, limitations, and likely failure modes of a model.

## Notebook sequence

| Notebook | Purpose | Normal input | Output |
| --- | --- | --- | --- |
| `01_NIST_BP_V2.ipynb` | Explore data sources and discuss data collection. | Supplied Parquet files for normal use. | `CompoundData.parquet` when the optional collection workflow is run. |
| `02_SMILES_BP_v3.ipynb` | Create chemical descriptors, functional-group labels, and fingerprints. | `CompoundData.parquet` | `CompoundDataFuncsFingerprints.parquet` |
| `03_ML_Benchmarking_V3.ipynb` | Benchmark ML model choices. | `CompoundDataFuncsFingerprints.parquet` | Figures and model metrics. |
| `04_Feature_Engineering_V1.ipynb` | Compare feature selection and reduction. | `CompoundDataFuncsFingerprints.parquet` | Figures and model metrics. |

Run the notebooks in that order. Cells marked **STOP** intentionally halt **Run All** before an optional installation, long data-collection job, or long model-training exercise. Read the message, then comment out the `raise RuntimeError(...)` line only when you intentionally want to continue.

## Environment

Create the course environment from the repository root:

```powershell
conda env create -f environment.yml
conda activate ci8615
python -m ipykernel install --user --name ci8615 --display-name "Python (ci8615)"
jupyter lab
```

The environment pins `numpy=2.0` because the version of `numba` used by `umap-learn` is incompatible with NumPy 2.2 or later.

## Data files

The normal student workflow uses the prepared Parquet files rather than regenerating them from live web services. Download the Module 1 files from the course SharePoint folder and either:

1. place them in this notebook folder, or
2. set `CHE8615_MODULE1_DATA_DIR` to the folder that contains them.

For the current local release, the notebooks also detect the sibling folder:

```text
8615_2026FS_parquet_files_release/01_Structure_to_Boiling_Point
```

The expected files are `Compounds.parquet`, `CompoundData.parquet`, `CompoundDataFuncs.parquet`, and `CompoundDataFuncsFingerprints.parquet`.

The NIST retrieval code is retained as an instructional example, but it depends on a third-party HTML parser and live websites. It is optional and may require maintenance when those services change.

## Accessibility and participation

- Every figure is followed by a caption that states the key pattern, evidence, and limitation in words.
- Use the printed table previews and summary statistics alongside visualizations; do not rely on color alone.
- Notebook cells show a small preview instead of an entire dataset. Increase the preview deliberately if you need more rows.
- For synchronous teaching, offer the prepared Parquet data so participation does not depend on a long download, high-bandwidth connection, or a particular machine.

## Time expectations

- Notebooks 1–2: about one class session when using the supplied data.
- Notebook 3: individual model cells range from about a minute to many minutes; begin with the shorter settings.
- Notebook 4: dimensionality-reduction and neural-network cells can take several minutes. Run one experiment at a time and record its settings.
