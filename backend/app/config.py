"""
Central configuration for the Nagpur Safety Map project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# --- Nagpur geography ---
NAGPUR_CENTER_LAT = 21.1458
NAGPUR_CENTER_LNG = 79.0882
DEFAULT_ZOOM = 12

# Rough bounding box used later to reject out-of-city junk reports
NAGPUR_BOUNDS = {
    "min_lat": 20.95,
    "max_lat": 21.35,
    "min_lng": 78.90,
    "max_lng": 79.25,
}

# --- Database ---
DATABASE_URL = os.getenv(
    "DATABASE_URL", f"sqlite:///{BASE_DIR}/data/nagpur_safety.db"
)

# --- DBSCAN clustering params (used in Phase 4) ---
DBSCAN_EPS_KM = 0.3       # ~300m neighborhood radius
DBSCAN_MIN_SAMPLES = 4    # minimum reports to form a "Red Zone"
