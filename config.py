"""
Workshop configuration for V3-SEA-8 Malaysia Climate Data

This file helps locate your downloaded data files. Edit the paths below if your
downloads went to different locations than expected.
"""

from pathlib import Path

# ============================================================================
# CONFIGURE THESE PATHS
# ============================================================================
# Point these to wherever you downloaded the data files

# Path to CCRS climate model data (contains: ACCESS-CM2/, EC-Earth3/, etc.)
CCRS_DATA_PATH = Path.home() / "Downloads" / "V3-SEA-8-CCRS-data"

# Path to Malaysia shapefiles (contains: PENINSULAR_MALAYSIA/, SABAH/, SARAWAK/)
SHAPEFILES_PATH = Path.home() / "Downloads" / "Malaysia-Shapefiles"

# ============================================================================
# VALIDATION (do not edit below this line)
# ============================================================================

def validate_paths():
    """Check that all required data folders exist and provide helpful error messages."""
    
    errors = []
    suggestions = []
    
    # Check CCRS
    if not CCRS_DATA_PATH.exists():
        errors.append(f"❌ CCRS data folder not found at:\n    {CCRS_DATA_PATH}")
        suggestions.append(
            f"   → Extract V3-SEA-8 CCRS download to: {CCRS_DATA_PATH}\n"
            f"   → Or update CCRS_DATA_PATH in config.py"
        )
    else:
        # Verify it has model subdirectories
        model_dirs = [d for d in CCRS_DATA_PATH.iterdir() if d.is_dir()]
        if not model_dirs:
            errors.append(f"❌ CCRS folder is empty (no model folders found):\n    {CCRS_DATA_PATH}")
    
    # Check Shapefiles
    if not SHAPEFILES_PATH.exists():
        errors.append(f"❌ Shapefiles folder not found at:\n    {SHAPEFILES_PATH}")
        suggestions.append(
            f"   → Extract Malaysia shapefiles download to: {SHAPEFILES_PATH}\n"
            f"   → Or update SHAPEFILES_PATH in config.py"
        )
    else:
        # Verify it has regional subdirectories
        expected_regions = {"PENINSULAR_MALAYSIA", "SABAH", "SARAWAK"}
        found_regions = {d.name for d in SHAPEFILES_PATH.iterdir() if d.is_dir()}
        missing = expected_regions - found_regions
        if missing:
            errors.append(
                f"❌ Missing region folders in shapefiles:\n"
                f"    Expected: {expected_regions}\n"
                f"    Found: {found_regions}\n"
                f"    Missing: {missing}"
            )
    
    # Report errors
    if errors:
        print("\n" + "=" * 70)
        print("⚠️  DATA SETUP ERROR")
        print("=" * 70)
        for error in errors:
            print(f"\n{error}")
        print("\n" + "-" * 70)
        print("SOLUTIONS:")
        for suggestion in suggestions:
            print(suggestion)
        print("\n" + "=" * 70)
        raise FileNotFoundError("Please fix the paths in config.py and try again")
    
    print("✓ All data paths validated successfully")
    print(f"  • CCRS data:     {CCRS_DATA_PATH}")
    print(f"  • Shapefiles:    {SHAPEFILES_PATH}")


# Run validation when config is imported
validate_paths()