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

## Setup Instructions for Participants

### Step 1: Download Files

Download and extract **both** of these:

1. **Workshop code** (from GitHub):
   - Download: `V3-SEA-8-main.zip` from the repository
   - Extract to any folder on your computer

2. **CCRS Climate Data** (external link):
   - Download and extract to: `~/Downloads/V3-SEA-8-CCRS-data/`
   - (Or any location; you'll configure it in Step 3)

3. **Malaysia Shapefiles** (external link):
   - Download and extract to: `~/Downloads/Malaysia-Shapefiles/`
   - (Or any location; you'll configure it in Step 3)

### Step 2: Verify Folder Structure

After extracting, your folders should look like this:

```
Your Computer:
├── Downloads/
│   ├── V3-SEA-8-CCRS-data/           ← Extract CCRS zip here
│   │   ├── ACCESS-CM2/
│   │   │   ├── historical/
│   │   │   ├── ssp126/
│   │   │   └── ... (other scenarios)
│   │   ├── EC-Earth3/
│   │   └── ... (other models)
│   │
│   └── Malaysia-Shapefiles/          ← Extract shapefiles zip here
│       ├── PENINSULAR_MALAYSIA/
│       │   ├── PM_Shapefile_Zone1/
│       │   ├── PM_Shapefile_Zone2/
│       │   └── PM_Shapefile_Zone3/
│       ├── SABAH/
│       │   ├── SBH_Shapefile_Zone1/
│       │   └── SBH_Shapefile_Zone2/
│       └── SARAWAK/
│           ├── SRWK_Shapefile_Zone1/
│           └── SRWK_Shapefile_Zone2/
│
└── Desktop/ (or anywhere)
    └── V3-SEA-8-main/                ← Extracted GitHub repo
        ├── PENINSULAR_MALAYSIA/
        ├── SABAH/
        ├── SARAWAK/
        └── workshop/
            ├── 01_tas_malaysia_timeseries_workshop.ipynb
            ├── config.py              ← Path configuration file
            ├── README.md
            └── requirements.txt
```

### Step 3: Configure Paths (if needed)

**Most users:** If you extracted CCRS data and shapefiles to your Downloads folder, skip this step—it should work automatically.

**Alternative locations:** If you extracted files elsewhere:

1. Open `workshop/config.py` in a text editor
2. Update these lines to match your file locations:

```python
CCRS_DATA_PATH = Path.home() / "Downloads" / "V3-SEA-8-CCRS-data"
SHAPEFILES_PATH = Path.home() / "Downloads" / "Malaysia-Shapefiles"
```

For example, if you extracted to Desktop instead:

```python
CCRS_DATA_PATH = Path.home() / "Desktop" / "V3-SEA-8-CCRS-data"
SHAPEFILES_PATH = Path.home() / "Desktop" / "Malaysia-Shapefiles"
```

Or use absolute paths:

```python
CCRS_DATA_PATH = Path("C:/Users/YourName/MyData/V3-SEA-8-CCRS-data")
SHAPEFILES_PATH = Path("C:/Users/YourName/MyData/Malaysia-Shapefiles")
```

### Step 4: Install Python Dependencies

From the `workshop` folder:

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**macOS/Linux (Terminal):**
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 5: Start Jupyter and Run the Notebook

Activate the virtual environment (if not already active), then:

```powershell
jupyter lab
```

or:

```powershell
jupyter notebook
```

Open `01_tas_malaysia_timeseries_workshop.ipynb` and run the first cell. It will validate your paths and give you feedback.

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

## Troubleshooting

### Error: "CCRS data folder not found"

**Solution:**
- Verify that the CCRS zip file was extracted to the expected location
- Check that the extracted folder contains model subdirectories (ACCESS-CM2, EC-Earth3, etc.)
- Edit `config.py` and update `CCRS_DATA_PATH` to match your actual download location
- Run the notebook's first cell again to validate paths

### Error: "Shapefiles folder not found"

**Solution:**
- Verify that the shapefiles zip file was extracted to the expected location
- Check that the extracted folder contains: `PENINSULAR_MALAYSIA/`, `SABAH/`, `SARAWAK/`
- Edit `config.py` and update `SHAPEFILES_PATH` to match your actual download location
- Run the notebook's first cell again to validate paths

### Error: "Missing region folders in shapefiles"

**Solution:**
- The shapefile archive might have an extra nested folder
- Try extracting one level higher in the hierarchy
- Verify the three region folders exist: `PENINSULAR_MALAYSIA/`, `SABAH/`, `SARAWAK/`

### Error: "ModuleNotFoundError: No module named 'xarray'" or similar

**Solution:**
- Ensure you activated the virtual environment:
  - **Windows:** `.\.venv\Scripts\Activate.ps1`
  - **macOS/Linux:** `source .venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

### Error: No output or plots appear

**Solution:**
- Run the notebook cells in order (top to bottom)
- If caching is enabled, check `outputs/tas/cache/` for existing CSV files
- Try setting `USE_CACHE = False` in the notebook to force recomputation

### Still having issues?

Contact the workshop organizer with:
- The full error message
- Your operating system (Windows/macOS/Linux)
- The output of `python --version` and `pip list` (in your virtual environment)
- The paths you configured in `config.py`

## Notes For GitHub

The NetCDF climate files are large and should not be committed directly to GitHub. Keep the data folders external and provide download links:

- CCRS climate model data: [external link to download]
- Malaysia shapefiles: [external link to download]

The notebook writes caches and outputs to `workshop/outputs/`, which is safe to commit or ignore as needed.
