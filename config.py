"""
Local workshop configuration for V3-SEA-8 Malaysia climate data.

Edit the paths below if your downloaded data folders are in different
locations, or set the environment variables V3SEA8_CCRS and V3SEA8_SHAPES.
This file uses plain ASCII messages so it displays cleanly in Windows
terminals and Jupyter.
"""

from __future__ import annotations

import os
from pathlib import Path


def first_existing(*paths: Path) -> Path:
    """Return the first path that exists, or the first candidate as a fallback."""

    for path in paths:
        if path.exists():
            return path
    return paths[0]


WORKSHOP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = WORKSHOP_DIR.parent

# Optional environment-variable overrides.
# Windows PowerShell examples:
#   $env:V3SEA8_CCRS = "C:\data\V3-SEA-8-CCRS-data"
#   $env:V3SEA8_SHAPES = "C:\data\Malaysia-Shapefiles"
ENV_CCRS = os.environ.get("V3SEA8_CCRS")
ENV_SHAPES = os.environ.get("V3SEA8_SHAPES")

DEFAULT_CCRS = first_existing(
    PROJECT_ROOT / "V3-SEA-8" / "CCRS",
    PROJECT_ROOT / "CCRS",
    WORKSHOP_DIR / "CCRS",
    Path.home() / "Downloads" / "V3-SEA-8-CCRS-data",
    Path.home() / "Downloads" / "V3-SEA-8-data" / "CCRS",
)

DEFAULT_SHAPES = first_existing(
    PROJECT_ROOT,
    PROJECT_ROOT / "shapefiles",
    WORKSHOP_DIR / "shapefiles",
    Path.home() / "Downloads" / "Malaysia-Shapefiles",
    Path.home() / "Downloads" / "V3-SEA-8-data" / "shapefiles",
)

CCRS_DATA_PATH = Path(ENV_CCRS) if ENV_CCRS else DEFAULT_CCRS
SHAPEFILES_PATH = Path(ENV_SHAPES) if ENV_SHAPES else DEFAULT_SHAPES


def validate_paths() -> None:
    """Check required folders and print participant-friendly guidance."""

    errors: list[str] = []
    suggestions: list[str] = []

    if not CCRS_DATA_PATH.exists():
        errors.append(f"CCRS data folder not found:\n    {CCRS_DATA_PATH}")
        suggestions.append(
            "Download/extract the CCRS data, then either:\n"
            "  1. edit CCRS_DATA_PATH in config.py, or\n"
            "  2. set environment variable V3SEA8_CCRS to the CCRS folder."
        )
    else:
        expected_models = {
            "ACCESS-CM2",
            "EC-Earth3",
            "MIROC6",
            "MPI-ESM1-2-HR",
            "NorESM2-MM",
            "UKESM1-0-LL",
        }
        found_models = {path.name for path in CCRS_DATA_PATH.iterdir() if path.is_dir()}
        missing_models = expected_models - found_models
        if not found_models:
            errors.append(f"CCRS folder has no model subfolders:\n    {CCRS_DATA_PATH}")
        elif missing_models:
            suggestions.append(
                "CCRS folder was found, but some expected model folders are missing:\n"
                f"  Missing: {sorted(missing_models)}\n"
                "The notebook can still run if you select only models that exist."
            )

    if not SHAPEFILES_PATH.exists():
        errors.append(f"Shapefiles folder not found:\n    {SHAPEFILES_PATH}")
        suggestions.append(
            "Download/extract the Malaysia shapefiles, then either:\n"
            "  1. edit SHAPEFILES_PATH in config.py, or\n"
            "  2. set environment variable V3SEA8_SHAPES to the shapefile root."
        )
    else:
        expected_regions = {"PENINSULAR_MALAYSIA", "SABAH", "SARAWAK"}
        found_regions = {path.name for path in SHAPEFILES_PATH.iterdir() if path.is_dir()}
        missing_regions = expected_regions - found_regions
        if missing_regions:
            errors.append(
                "Shapefile root is missing required region folders:\n"
                f"    Root: {SHAPEFILES_PATH}\n"
                f"    Missing: {sorted(missing_regions)}"
            )

    if errors:
        print("\n" + "=" * 72)
        print("DATA SETUP ERROR")
        print("=" * 72)
        for error in errors:
            print(f"\n{error}")
        if suggestions:
            print("\nSuggested fixes:")
            for suggestion in suggestions:
                print(f"\n{suggestion}")
        print(
            "\nRecommended local layout:\n"
            "  project-folder/\n"
            "    PENINSULAR_MALAYSIA/\n"
            "    SABAH/\n"
            "    SARAWAK/\n"
            "    V3-SEA-8/CCRS/\n"
            "    utilizing-climate-rcm-datas/\n"
            "\nIf your folders are elsewhere, edit config.py to point at them."
        )
        print("=" * 72)
        raise FileNotFoundError("Please fix the workshop data paths and rerun the cell.")

    print("Data paths validated successfully.")
    print(f"  CCRS data:  {CCRS_DATA_PATH}")
    print(f"  Shapefiles: {SHAPEFILES_PATH}")
    if suggestions:
        print("\nWarnings:")
        for suggestion in suggestions:
            print(suggestion)


validate_paths()
