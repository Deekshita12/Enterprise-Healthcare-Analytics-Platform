# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Bed
# ==========================================================

# ----------------------------------------------------------
# Import Libraries
# ----------------------------------------------------------

import pandas as pd
import random
from datetime import datetime, timedelta

# ----------------------------------------------------------
# File Paths
# ----------------------------------------------------------

BED_FILE = "datasets/original/bed.csv"
WARD_FILE = "datasets/enhanced/ward.csv"

OUTPUT_FILE = "datasets/enhanced/bed.csv"

# ----------------------------------------------------------
# Read Datasets
# ----------------------------------------------------------

bed_df = pd.read_csv(BED_FILE)

ward_df = pd.read_csv(WARD_FILE)

# ----------------------------------------------------------
# Audit
# ----------------------------------------------------------

print("=" * 60)
print("BED TABLE AUDIT")
print("=" * 60)

print("\nBed Shape :", bed_df.shape)
print("Ward Shape :", ward_df.shape)

print("\nBed Columns")
print(bed_df.columns.tolist())

print("\nWard Columns")
print(ward_df.columns.tolist())

# ----------------------------------------------------------
# Merge Ward Information
# ----------------------------------------------------------

ward_required = ward_df[
    [
        "ward_id",
        "ward_type"
    ]
]

bed_df = bed_df.merge(
    ward_required,
    on="ward_id",
    how="left"
)

print("\nMerged Shape :", bed_df.shape)

print("\nPreview")

print(
    bed_df.head()
)

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def get_bed_type(ward_type):

    if ward_type == "General":
        return "General Bed"

    elif ward_type == "Private":
        return "Private Bed"

    elif ward_type == "Semi-Private":
        return "Semi-Private Bed"

    elif ward_type == "ICU":
        return "ICU Bed"

    else:
        return "General Bed"


def get_daily_charge(ward_type):

    if ward_type == "General":
        return 2500

    elif ward_type == "Private":
        return 8000

    elif ward_type == "Semi-Private":
        return 5000

    elif ward_type == "ICU":
        return 15000

    else:
        return 2500


def oxygen_support(ward_type):

    return ward_type in ["Private", "Semi-Private", "ICU"]


def ventilator_support(ward_type):

    return ward_type == "ICU"


def generate_room_number(bed_number):

    room = str(bed_number).split("-")[0]

    return f"R-{room}"

# ----------------------------------------------------------
# Add Enterprise Columns
# ----------------------------------------------------------

bed_df["bed_type"] = bed_df["ward_type"].apply(
    get_bed_type
)

bed_df["room_number"] = bed_df["bed_number"].apply(
    generate_room_number
)

bed_df["daily_charge"] = bed_df["ward_type"].apply(
    get_daily_charge
)

bed_df["oxygen_supported"] = bed_df["ward_type"].apply(
    oxygen_support
)

bed_df["ventilator_supported"] = bed_df["ward_type"].apply(
    ventilator_support
)
# ----------------------------------------------------------
# Enterprise Columns
# ----------------------------------------------------------

bed_df["bed_code"] = bed_df["bed_id"].apply(
    lambda x: f"BED-{x:06d}"
)

# ---------------- Maintenance Status ----------------

def maintenance_status(status):

    if status == "Occupied":
        return "Operational"

    return random.choices(
        [
            "Operational",
            "Under Maintenance",
            "Reserved"
        ],
        weights=[95,3,2],
        k=1
    )[0]


bed_df["maintenance_status"] = bed_df["bed_status"].apply(
    maintenance_status
)

bed_df.loc[
    bed_df["maintenance_status"] == "Under Maintenance",
    "bed_status"
] = "Maintenance"

bed_df.loc[
    bed_df["maintenance_status"] == "Reserved",
    "bed_status"
] = "Reserved"

# ---------------- Bed Condition ----------------

bed_df["bed_condition"] = random.choices(
    population=[
        "Excellent",
        "Good",
        "Needs Repair"
    ],
    weights=[70,25,5],
    k=len(bed_df)
)

# ---------------- Last Sanitized Date ----------------

today = datetime(2025, 1, 1) 

bed_df["last_sanitized_date"] = [

    (
        today - timedelta(days=random.randint(0,30))
    ).strftime("%Y-%m-%d")

    for _ in range(len(bed_df))

]

# ---------------- Sanitation Frequency ----------------

def sanitation_frequency(ward_type):

    if ward_type in ["ICU","Emergency"]:

        return "Every Patient"

    return "Daily"

bed_df["sanitation_frequency"] = bed_df["ward_type"].apply(
    sanitation_frequency
)
# ----------------------------------------------------------
# Business Rule
# ----------------------------------------------------------

bed_df.loc[
    bed_df["maintenance_status"]=="Under Maintenance",
    "bed_status"
] = "Maintenance"

bed_df.loc[
    bed_df["maintenance_status"]=="Reserved",
    "bed_status"
] = "Reserved"

bed_df["created_date"] = "2023-01-01"

bed_df["updated_date"] = "2025-01-01"

# ----------------------------------------------------------
# Validation
# ----------------------------------------------------------

print("\nEnhanced Columns")

print(bed_df.columns.tolist())

print("\nPreview")

print(bed_df.head())

print("\nMissing Values")

print(bed_df.isnull().sum())

bed_df = bed_df[
    [
        "bed_id",
        "bed_code",
        "bed_number",
        "bed_status",
        "ward_id",
        "ward_type",
        "bed_type",
        "room_number",
        "daily_charge",
        "oxygen_supported",
        "ventilator_supported",
        "maintenance_status",
        "bed_condition",
        "last_sanitized_date",
        "sanitation_frequency",
        "created_date",
        "updated_date"
    ]
]

assert bed_df["bed_id"].is_unique

assert bed_df["bed_code"].is_unique

# ----------------------------------------------------------
# Export Dataset
# ----------------------------------------------------------

bed_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ----------------------------------------------------------
# Completion Message
# ----------------------------------------------------------

print("\n" + "=" * 60)
print("Bed Enhancement Completed Successfully")
print("=" * 60)

print(f"\nSaved File : {OUTPUT_FILE}")

print(f"Final Shape : {bed_df.shape}")