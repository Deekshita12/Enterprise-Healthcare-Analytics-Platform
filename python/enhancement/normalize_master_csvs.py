# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Master CSV Normalization
# ==========================================================

import os
import pandas as pd

BASE_PATH = "datasets/enhanced"

print("=" * 70)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Master CSV Normalization")
print("=" * 70)

# ==========================================================
# Column Renaming Rules
# ==========================================================

COLUMN_MAPPING = {

    # ------------------------------------------------------
    # Diagnostic Test
    # ------------------------------------------------------

    "diagnostic_test.csv": {
        "test_id": "diagnostic_test_id"
    },

    # ------------------------------------------------------
    # Drug Manufacturer
    # ------------------------------------------------------

    "drug_manufacturer.csv": {
        "manufacturer_name": "manufacturer_name"
    },

    # ------------------------------------------------------
    # Employee
    # ------------------------------------------------------

    "employee.csv": {
        "employee_name": "full_name"
    },

    # ------------------------------------------------------
    # Bed
    # ------------------------------------------------------

    "bed.csv": {
        "daily_charge": "bed_charge_per_day"
    }

}

# ==========================================================
# Duplicate Columns To Remove
# ==========================================================

DROP_COLUMNS = {

    "employee.csv": [
        "date_of_joining.1"
    ]

}