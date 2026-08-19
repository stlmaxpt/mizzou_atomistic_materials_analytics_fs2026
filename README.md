# ChE 8615: Atomistic Materials Analytics

Course notebooks for the University of Missouri. The `main` branch contains the current course release; `2025SP` preserves the Spring 2025 endpoint and `2026FS` preserves the Fall 2026 development endpoint.

## Quick start

Install [Miniforge](https://conda-forge.org/download/) or Miniconda, then create the fully specified course environment from this repository's root folder:

```powershell
conda env create -f environment.yml
conda activate ci
python -m ipykernel install --user --name ci --display-name "Python (ci)"
jupyter lab
```

Use the `Python (ci)` kernel for every notebook. The environment definition includes the chemistry, data-science, visualization, and deep-learning dependencies used across the course.

## Data releases

Large prepared datasets are distributed separately from the notebook repository. Each module README identifies its required files and data location. Module 1 uses the Parquet files in the course SharePoint release; see [Module 1](01_Structure_to_Boiling_Point/README.md) for setup and workflow details.

## Course modules

- [01 — Structure to Boiling Point](01_Structure_to_Boiling_Point/README.md)
- 02 — FTIR to Structure
- 03 — Electrical Conductivity Prediction

### Acknowledgement

We acknowledge support from the NSF Division of Graduate Education NRT Program through Award Number 2243526 for the development of these resources.
