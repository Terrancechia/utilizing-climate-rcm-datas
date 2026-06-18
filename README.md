# V3-SEA-8 Malaysia Climate Workshop

This workshop demonstrates how V3-SEA-8 climate data from multiple CMIP models can be used to compare historical and future annual mean near-surface air temperature (`tas`) over Malaysia.

The notebook is designed for a local IDE workflow, such as VS Code, JupyterLab, or classic Jupyter Notebook. Running the raw NetCDF workflow directly from Google Colab is not recommended because large NetCDF/HDF5 reads from mounted Google Drive can fail unpredictably.

## Workshop Files

```text
01_tas_malaysia_timeseries_workshop.ipynb
config.py
README.md
requirements.txt
environment.yml
```

## What The Notebook Does

- inspect the model and scenario folder structure
- open an example NetCDF file with `xarray`
- load regional Malaysia shapefiles
- mask climate grids to Peninsular Malaysia, Sabah, or Sarawak
- compute annual area-mean temperature
- compute the 1995-2014 historical baseline
- convert absolute temperature to anomaly relative to that baseline
- compare historical, SSP1-2.6, SSP2-4.5, and SSP5-8.5
- plot either a single-model result or a multi-model ensemble with shaded spread

## Data You Need

You need the CCRS climate data folder containing model folders such as:

```text
ACCESS-CM2/
EC-Earth3/
MIROC6/
MPI-ESM1-2-HR/
NorESM2-MM/
UKESM1-0-LL/
```

You also need the Malaysia shapefile folders:

```text
PENINSULAR_MALAYSIA/
SABAH/
SARAWAK/
```

The NetCDF data are large, so they should stay outside GitHub.

## Recommended Local Layout

This repository is expected to sit beside the original V3-SEA-8 data folder:

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
      ...
  utilizing-climate-rcm-datas/
    01_tas_malaysia_timeseries_workshop.ipynb
    config.py
    README.md
```

The default `config.py` tries this layout first.

Alternative local layout:

```text
Downloads/
  V3-SEA-8-CCRS-data/
    ACCESS-CM2/
    EC-Earth3/
    MIROC6/
    ...
  Malaysia-Shapefiles/
    PENINSULAR_MALAYSIA/
    SABAH/
    SARAWAK/
```

If your folders are somewhere else, edit `config.py` or set environment variables:

```text
V3SEA8_CCRS
V3SEA8_SHAPES
```

Example in Windows PowerShell:

```powershell
$env:V3SEA8_CCRS = "C:\path\to\CCRS"
$env:V3SEA8_SHAPES = "C:\path\to\Malaysia-Shapefiles"
```

## Option A: Run Locally With Conda

This is the recommended setup because geospatial packages are usually smoother with conda.

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
conda env create -f environment.yml
conda activate v3sea8-workshop
jupyter lab
```

Open:

```text
01_tas_malaysia_timeseries_workshop.ipynb
```

## Option B: Run Locally With pip

Recommended Python: 3.11 or 3.12.

Windows PowerShell:

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

macOS/Linux:

```bash
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

## Running The Notebook

Near the top of the notebook, choose a region:

```python
REGION_KEY = "sabah"
```

Available regions:

```text
penisular
sabah
sarawak
```

Choose one model for a fast first run:

```python
MODELS_TO_RUN = ["ACCESS-CM2"]
```

Choose two or more models to show ensemble spread:

```python
MODELS_TO_RUN = ["ACCESS-CM2", "MIROC6"]
```

Run every available model:

```python
MODELS_TO_RUN = "all"
```

When one model is selected, the plot shows that model directly. When more than one model is selected, the plot shows:

- solid line: ensemble mean
- shaded range: model minimum to model maximum

The notebook writes caches and figures under:

```text
outputs/
```

Caches are intermediate processed files. They are safe to delete; the notebook will recompute them from the raw data.

## Troubleshooting

### CCRS data folder not found

Check that the CCRS folder contains model folders such as `ACCESS-CM2` and `MIROC6`. Then update `config.py` or set `V3SEA8_CCRS`.

### Shapefiles folder not found

Check that the shapefile root contains `PENINSULAR_MALAYSIA`, `SABAH`, and `SARAWAK`. Then update `config.py` or set `V3SEA8_SHAPES`.

### ModuleNotFoundError

Make sure your environment is activated, then reinstall dependencies:

```powershell
pip install -r requirements.txt
```

If `geopandas` fails with pip, use the conda setup instead:

```powershell
conda env create -f environment.yml
```

### Notebook is slow

Use one model first:

```python
MODELS_TO_RUN = ["ACCESS-CM2"]
```

The full six-model ensemble can take substantially longer.

### Plots do not change after editing settings

Run cells from the top again, especially the settings and computation cells. If needed, set:

```python
USE_CACHE = False
```

to force recomputation.

## GitHub Notes

Do not commit large NetCDF climate data to GitHub. Keep data external and provide download links. The `.gitignore` ignores generated outputs and common local environment folders.
