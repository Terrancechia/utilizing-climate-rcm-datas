# V3-SEA-8 Malaysia Climate Workshop

This workshop shows how V3-SEA-8 climate data from multiple CMIP models can be used to compare historical and future climate conditions over Malaysia.

The first notebook focuses on annual mean near-surface air temperature (`tas`) for Peninsular Malaysia, Sabah, and Sarawak. It walks through the full workflow directly inside the notebook:

- inspect the model/scenario folder structure
- open example NetCDF files with `xarray`
- load and merge regional shapefiles
- mask climate grids to a selected Malaysia region
- compute annual area-mean temperature
- compute the 1995-2014 historical baseline
- convert absolute temperature to anomaly relative to that baseline
- compare historical, SSP1-2.6, SSP2-4.5, and SSP5-8.5
- plot either a single-model result or a multi-model ensemble with shaded spread

## Folder Layout

Expected layout:

```text
V3-SEA-8/
  PENINSULAR_MALAYSIA/
  SABAH/
  SARAWAK/
  V3-SEA-8/
    CCRS/
      ACCESS-CM2/
      EC-Earth3/
      MIROC6/
      MPI-ESM1-2-HR/
      NorESM2-MM/
      UKESM1-0-LL/
  workshop/
    01_tas_malaysia_timeseries_workshop.ipynb
    README.md
    requirements.txt
```

## Local Setup

From the `workshop` folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Then start Jupyter:

```powershell
jupyter lab
```

or:

```powershell
jupyter notebook
```

Open:

```text
01_tas_malaysia_timeseries_workshop.ipynb
```

## Running The Notebook

Near the top of the notebook, choose the region and models:

```python
REGION_KEY = "sabah"
MODELS_TO_RUN = ["ACCESS-CM2", "MIROC6"]
```

For a quick test, use one model:

```python
MODELS_TO_RUN = ["ACCESS-CM2"]
```

For the full ensemble:

```python
MODELS_TO_RUN = "all"
```

When one model is selected, the plot shows that model directly. When more than one model is selected, the plot shows:

- solid line: ensemble mean
- shaded range: model minimum to model maximum

## Notes For GitHub

The NetCDF climate files are large and usually should not be committed directly to GitHub. For a public repository, use one of these approaches:

- provide a download link for the data
- use Git LFS for selected sample files
- include a small sample dataset for quick demonstration
- keep the full data folder outside Git and document where users should place it

The notebook writes caches and figures under:

```text
workshop/outputs/
```
