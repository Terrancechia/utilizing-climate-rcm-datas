# V3-SEA-8 Malaysia Climate Workshop

This workshop demonstrates how V3-SEA-8 climate data from multiple CMIP models can be used to compare historical and future climate conditions over Malaysia.

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

## Files In This Folder

```text
workshop/
  01_tas_malaysia_timeseries_workshop.ipynb
  config.py
  README.md
  requirements.txt
  environment.yml
```

## Data You Need

You need two data downloads:

1. CCRS climate data folder containing model folders such as:

```text
ACCESS-CM2/
EC-Earth3/
MIROC6/
MPI-ESM1-2-HR/
NorESM2-MM/
UKESM1-0-LL/
```

2. Malaysia shapefile folder containing:

```text
PENINSULAR_MALAYSIA/
SABAH/
SARAWAK/
```

The NetCDF data are large, so they are not expected to be committed directly to GitHub.

## Recommended Data Layout

Local layout beside the repository:

```text
V3-SEA-8/
  PENINSULAR_MALAYSIA/
  SABAH/
  SARAWAK/
  V3-SEA-8/
    CCRS/
      ACCESS-CM2/
      EC-Earth3/
      ...
  workshop/
    01_tas_malaysia_timeseries_workshop.ipynb
```

Alternative local layout in Downloads:

```text
Downloads/
  V3-SEA-8-CCRS-data/
    ACCESS-CM2/
    EC-Earth3/
    ...
  Malaysia-Shapefiles/
    PENINSULAR_MALAYSIA/
    SABAH/
    SARAWAK/
```

Google Colab layout in Google Drive:

```text
MyDrive/
  V3-SEA-8-data/
    CCRS/
      ACCESS-CM2/
      EC-Earth3/
      ...
    shapefiles/
      PENINSULAR_MALAYSIA/
      SABAH/
      SARAWAK/
```

If your folders are somewhere else, edit `config.py`:

```python
CCRS_DATA_PATH = Path("path/to/your/CCRS")
SHAPEFILES_PATH = Path("path/to/your/shapefiles")
```

You can also set environment variables:

```text
V3SEA8_CCRS
V3SEA8_SHAPES
```

## Option A: Run On Google Colab

Colab avoids most local installation issues, but reading many large NetCDF files from Google Drive can be slower.

Repository:

```text
https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
```

Alternative Colab opening method:

1. Go to `https://colab.research.google.com`
2. Select `File -> Open notebook -> GitHub`
3. Paste:

```text
https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
```

4. Open:

```text
workshop/01_tas_malaysia_timeseries_workshop.ipynb
```

Data setup for Colab:

1. Upload/extract the CCRS and shapefile data to Google Drive:

```text
MyDrive/V3-SEA-8-data/CCRS
MyDrive/V3-SEA-8-data/shapefiles
```

2. Run the first setup cell in the notebook. It will:
   - install missing Python packages
   - mount Google Drive
   - clone this GitHub repository into `/content/utilizing-climate-rcm-datas`
   - switch the notebook working directory to `/content/utilizing-climate-rcm-datas/workshop`
   - validate the configured data paths
3. If your data is in a different Drive folder, edit `workshop/config.py` or update the path variables in the notebook.

For workshops, start with one model or two models:

```python
MODELS_TO_RUN = ["ACCESS-CM2"]
```

or:

```python
MODELS_TO_RUN = ["ACCESS-CM2", "MIROC6"]
```

Then switch to the full ensemble when ready:

```python
MODELS_TO_RUN = "all"
```

## Option B: Run Locally With Conda

This is the most reliable local setup for geospatial packages.

First clone the repository:

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas\workshop
```

Then create the environment:

```powershell
conda env create -f environment.yml
conda activate v3sea8-workshop
jupyter lab
```

Open:

```text
01_tas_malaysia_timeseries_workshop.ipynb
```

## Option C: Run Locally With pip

Recommended Python: 3.11 or 3.12.

First clone the repository:

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas\workshop
```

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
jupyter lab
```

## Running The Notebook

Near the top of the notebook, choose:

```python
REGION_KEY = "sabah"
MODELS_TO_RUN = ["ACCESS-CM2", "MIROC6"]
```

Available regions:

```text
penisular
sabah
sarawak
```

When one model is selected, the plot shows that model directly. When more than one model is selected, the plot shows:

- solid line: ensemble mean
- shaded range: model minimum to model maximum

The notebook writes caches and figures under:

```text
workshop/outputs/
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
