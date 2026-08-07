# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Ward
# ==========================================================

import pandas as pd
import random

INPUT_FILE = "datasets/original/ward.csv"
EMPLOYEE_FILE = "datasets/enhanced/employee.csv"

OUTPUT_FILE = "datasets/enhanced/ward.csv"

ward_df = pd.read_csv(INPUT_FILE)
employee_df = pd.read_csv(EMPLOYEE_FILE)

print("="*60)
print("WARD TABLE AUDIT")
print("="*60)

print("\nShape :", ward_df.shape)
print("\nColumns")
print(ward_df.columns.tolist())

# ----------------------------------------------------------
# Ward Lookup
# ----------------------------------------------------------

ward_lookup = {

    "ICU": {
        "status": "Active",
        "floor": 1,
        "station": "ICU Station",
        "target": 95,
        "isolation": True,
        "category": "Critical Care",
        "priority": "Critical",
        "cleaning": "Every 8 Hours"
    },

    "Emergency": {
        "status": "Active",
        "floor": 0,
        "station": "Emergency Station",
        "target": 95,
        "isolation": True,
        "category": "Critical Care",
        "priority": "Critical",
        "cleaning": "Every 8 Hours"
    },

    "General": {
        "status": "Active",
        "floor": 2,
        "station": "General Station",
        "target": 85,
        "isolation": False,
        "category": "General Care",
        "priority": "Medium",
        "cleaning": "Daily"
    },

    "Private": {
        "status": "Active",
        "floor": 3,
        "station": "Private Station",
        "target": 80,
        "isolation": False,
        "category": "Premium Care",
        "priority": "High",
        "cleaning": "Every 12 Hours"
    },

    "Semi-Private": {
        "status": "Active",
        "floor": 2,
        "station": "Semi Station",
        "target": 85,
        "isolation": False,
        "category": "Standard Care",
        "priority": "Medium",
        "cleaning": "Daily"
    }

}
# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def get_lookup(value, field):

    if value in ward_lookup:

        return ward_lookup[value][field]

    return None

# ----------------------------------------------------------
# Add Enterprise Columns
# ----------------------------------------------------------

ward_df["ward_status"] = ward_df["ward_type"].apply(
    lambda x:get_lookup(x,"status")
)

ward_df["floor_number"] = ward_df["ward_type"].apply(
    lambda x:get_lookup(x,"floor")
)

ward_df["nurse_station"] = ward_df["ward_type"].apply(
    lambda x:get_lookup(x,"station")
)

ward_df["occupancy_target"] = ward_df["ward_type"].apply(
    lambda x:get_lookup(x,"target")
)

ward_df["isolation_capability"] = ward_df["ward_type"].apply(
    lambda x:get_lookup(x,"isolation")
)
# ----------------------------------------------------------
# Enterprise Columns
# ----------------------------------------------------------

ward_df["ward_code"] = ward_df["ward_id"].apply(
    lambda x: f"WRD-{x:03d}"
)

ward_df["ward_category"] = ward_df["ward_type"].apply(
    lambda x: get_lookup(x, "category")
)

ward_df["cleaning_schedule"] = ward_df["ward_type"].apply(
    lambda x: get_lookup(x, "cleaning")
)

ward_df["ward_priority"] = ward_df["ward_type"].apply(
    lambda x: get_lookup(x, "priority")
)

# ----------------------------------------------------------
# Assign Head Nurse
# ----------------------------------------------------------

nurse_ids = employee_df.loc[
    employee_df["role"] == "Nurse",
    "employee_id"
].tolist()

ward_df["head_nurse_employee_id"] = [

    f"EMP{random.choice(nurse_ids):06d}"

    for _ in range(len(ward_df))

]

ward_df["created_date"] = "2023-01-01"

ward_df["updated_date"] = "2025-01-01"

print("\nEnhanced Columns")

print(ward_df.columns.tolist())

print("\nPreview")

print(ward_df.head())

print("\nMissing Values")

print(ward_df.isnull().sum())

assert ward_df["ward_id"].is_unique

assert ward_df["ward_code"].is_unique

ward_df = ward_df[
    [
        "ward_id",
        "ward_code",
        "ward_name",
        "ward_type",
        "ward_category",
        "department_id",
        "total_beds",
        "head_nurse_employee_id",
        "ward_status",
        "floor_number",
        "nurse_station",
        "occupancy_target",
        "cleaning_schedule",
        "ward_priority",
        "isolation_capability",
        "created_date",
        "updated_date"
    ]
]

ward_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nWard Enhancement Completed Successfully")

print("\nFinal Shape :",ward_df.shape)