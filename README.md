# V3-SEA-8 Malaysia Climate Workshop

This workshop demonstrates how V3-SEA-8 climate data from multiple CMIP models can be used to compare historical and future climate conditions over Malaysia.

The notebook is designed for a local IDE workflow, such as VS Code, JupyterLab, or classic Jupyter Notebook. Running the raw NetCDF workflow directly from Google Colab is not recommended because large NetCDF/HDF5 reads from mounted Google Drive can fail unpredictably.

## Workshop Files

```text
01_tas_malaysia_timeseries_workshop.ipynb
02_rx1day_malaysia_seasonal_change_workshop.ipynb
config.py
README.md
requirements.txt
environment.yml
```

## What The Notebook Does

The TAS notebook:

- inspect the model and scenario folder structure
- open an example NetCDF file with `xarray`
- load regional Malaysia shapefiles
- mask climate grids to Peninsular Malaysia, Sabah, or Sarawak
- compute annual area-mean temperature
- compute the 1995-2014 historical baseline
- convert absolute temperature to anomaly relative to that baseline
- compare historical, SSP1-2.6, SSP2-4.5, and SSP5-8.5
- plot either a single-model result or a multi-model ensemble with shaded spread

The RX1day notebook:

- inspect monthly `rx1day` NetCDF files
- merge the Malaysia shapefiles or focus on one selected region
- convert monthly RX1day data into DJF, MAM, JJA, and SON seasonal values
- compute 1995-2014 historical seasonal climatology
- compute 2080-2099 SSP5-8.5 seasonal climatology
- calculate percentage change per model first, then average the percentage-change maps across selected models
- plot four seasonal percentage-change maps with a shared horizontal colour bar

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

# Starting Setup For This Workshop

Before opening the notebook, create a Python environment and install the required packages. You can then run the notebook either in VS Code or in browser-based JupyterLab.

## Option A: Run Locally With pip

Recommended Python: 3.11 or 3.12.

Windows PowerShell:

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install ipykernel jupyterlab
```

If you are using Windows Command Prompt instead of PowerShell, activate the environment with:

```cmd
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install ipykernel jupyterlab
```

## Option B: Run Locally With Conda

This is a good alternative if `geopandas` or other geospatial packages are difficult to install with pip.

```powershell
git clone https://github.com/Terrancechia/utilizing-climate-rcm-datas.git
cd utilizing-climate-rcm-datas
conda env create -f environment.yml
conda activate v3sea8-workshop
```

## Open The Notebook In VS Code

1. Open VS Code.
2. Open the repository folder `utilizing-climate-rcm-datas`.
3. Open `01_tas_malaysia_timeseries_workshop.ipynb`.
4. Click `Select Kernel` at the top right of the notebook.
5. If you used pip, choose the interpreter that looks like:

```text
...\utilizing-climate-rcm-datas\.venv\Scripts\python.exe
```

It may also appear as:

```text
.venv
Python (.venv)
Python 3.x (.venv)
```

If you used conda, choose:

```text
v3sea8-workshop
```

Then run Cell 0. If Cell 0 says the required packages can be imported, the correct environment is selected.

## Open The Notebook In JupyterLab

If you used pip, activate the virtual environment and launch JupyterLab:

```powershell
.\.venv\Scripts\Activate.ps1
jupyter lab
```

If `jupyter lab` is not recognized, install JupyterLab into the active environment:

```powershell
python -m pip install jupyterlab
jupyter lab
```

If you used conda:

```powershell
conda activate v3sea8-workshop
jupyter lab
```

After JupyterLab opens in the browser, open one of the workshop notebooks:

```text
01_tas_malaysia_timeseries_workshop.ipynb
02_rx1day_malaysia_seasonal_change_workshop.ipynb
```

If JupyterLab only shows `Python 3 (ipykernel)` and you are not sure whether it is the correct environment, run this in the notebook:

```python
import sys
print(sys.executable)
```

For pip, the output should include:

```text
.venv\Scripts\python.exe
```

For conda, the output should include the `v3sea8-workshop` environment path.

If you want JupyterLab to show a clearer kernel name, run this once after activating the environment:

```powershell
python -m ipykernel install --user --name v3sea8-workshop --display-name "Python (v3sea8-workshop)"
```

Then restart JupyterLab and choose:

```text
Python (v3sea8-workshop)
```

## Running The Notebook

In the TAS notebook, choose a region near the top:

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

In the RX1day notebook, the default region is all Malaysia:

```python
REGION_KEY = "malaysia"
```

You can also focus on one region:

```python
REGION_KEY = "penisular"  # or "sabah", "sarawak"
```

The RX1day notebook uses SSP5-8.5 by default:

```python
FUTURE_SCENARIO = "ssp585"
```

For the TAS time-series notebook, when one model is selected, the plot shows that model directly. When more than one model is selected, the plot shows:

- solid line: ensemble mean
- shaded range: model minimum to model maximum

For the RX1day seasonal map notebook, when more than one model is selected, percentage change is calculated per model first and then averaged across the selected models.

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
