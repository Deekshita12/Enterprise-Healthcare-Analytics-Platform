# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Department
# ==========================================================

# ----------------------------------------------------------
# Import Libraries
# ----------------------------------------------------------

import pandas as pd

# ----------------------------------------------------------
# File Paths
# ----------------------------------------------------------

INPUT_FILE = "datasets/original/department.csv"
OUTPUT_FILE = "datasets/enhanced/department.csv"

# ----------------------------------------------------------
# Read Dataset
# ----------------------------------------------------------

department_df = pd.read_csv(INPUT_FILE)

# ----------------------------------------------------------
# Data Audit
# ----------------------------------------------------------

print("=" * 60)
print("DEPARTMENT TABLE AUDIT")
print("=" * 60)

print(f"\nShape : {department_df.shape}")

print("\nCurrent Columns")
print(department_df.columns.tolist())

# ----------------------------------------------------------
# Department Lookup Dictionary
# ----------------------------------------------------------

department_lookup = {

    "Emergency": {
        "code": "ER",
        "wing": "A",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 250
    },

    "Internal Medicine": {
        "code": "IM",
        "wing": "B",
        "hours": "08:00-18:00",
        "is_24x7": False,
        "capacity": 180
    },

    "Surgery": {
        "code": "SUR",
        "wing": "A",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 150
    },

    "Pediatrics": {
        "code": "PED",
        "wing": "C",
        "hours": "08:00-18:00",
        "is_24x7": False,
        "capacity": 120
    },

    "Orthopedics": {
        "code": "ORT",
        "wing": "B",
        "hours": "08:00-18:00",
        "is_24x7": False,
        "capacity": 140
    },

    "ICU": {
        "code": "ICU",
        "wing": "A",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 80
    },

    "Radiology": {
        "code": "RAD",
        "wing": "D",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 220
    },

    "Pathology": {
        "code": "PAT",
        "wing": "D",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 300
    },

    "Pharmacy": {
        "code": "PHR",
        "wing": "Ground",
        "hours": "24x7",
        "is_24x7": True,
        "capacity": 500
    },

    "Billing": {
        "code": "BIL",
        "wing": "Ground",
        "hours": "08:00-20:00",
        "is_24x7": False,
        "capacity": 200
    },

    "HR": {
        "code": "HR",
        "wing": "Admin",
        "hours": "09:00-17:00",
        "is_24x7": False,
        "capacity": 50
    }

}

# ----------------------------------------------------------
# Add Enterprise Columns
# ----------------------------------------------------------

department_df["department_code"] = department_df["department_name"].apply(
    lambda x: department_lookup[x]["code"]
)

department_df["building_wing"] = department_df["department_name"].apply(
    lambda x: department_lookup[x]["wing"]
)

department_df["operating_hours"] = department_df["department_name"].apply(
    lambda x: department_lookup[x]["hours"]
)

department_df["is_24x7"] = department_df["department_name"].apply(
    lambda x: department_lookup[x]["is_24x7"]
)

department_df["capacity_per_day"] = department_df["department_name"].apply(
    lambda x: department_lookup[x]["capacity"]
)

department_df["head_doctor_id"] = pd.NA

department_df["created_date"] = "2023-01-01"

department_df["updated_date"] = "2025-01-01"
# ==========================================================
# Audit Columns
# ==========================================================

department_df["created_by"] = "System"
department_df["updated_by"] = "System"

# ==========================================================
# Convert Boolean to TinyInt (MySQL Compatible)
# ==========================================================

department_df["is_24x7"] = department_df["is_24x7"].astype(int)

# ==========================================================
# Reorder Columns to Match MySQL Table
# ==========================================================

department_df = department_df[
    [
        "department_id",
        "department_name",
        "department_code",
        "building_wing",
        "operating_hours",
        "is_24x7",
        "capacity_per_day",
        "head_doctor_id",
        "created_by",
        "updated_by",
        "created_date",
        "updated_date"
    ]
]

# ==========================================================
# Validation
# ==========================================================

print("\nFinal Columns")
print(department_df.columns.tolist())

print("\nPreview")
print(department_df.head())

# ==========================================================
# Export
# ==========================================================

department_df.to_csv(
    OUTPUT_FILE,
    index=False,
    na_rep="\\N"
)

print("\nDepartment CSV Regenerated Successfully")
print(f"Rows : {len(department_df)}")
print(f"Columns : {len(department_df.columns)}")