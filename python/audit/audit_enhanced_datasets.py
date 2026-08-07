# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# ETL Audit - Enhanced Dataset Validation
# ==========================================================

import os
import pandas as pd

# ==========================================================
# CONFIGURATION
# ==========================================================

DATASET_FOLDER = "datasets/enhanced"

PRIMARY_KEYS = {
    "department.csv": "department_id",
    "employee.csv": "employee_id",
    "doctor.csv": "doctor_id",
    "ward.csv": "ward_id",
    "bed.csv": "bed_id",
    "disease.csv": "disease_id",
    "diagnostic_test.csv": "test_id",
    "drug_manufacturer.csv": "manufacturer_id",
    "drug.csv": "drug_id",
    "drug_inventory.csv": "inventory_id",
    "insurance_provider.csv": "insurance_provider_id",
    "patient.csv": "patient_id",
    "admission.csv": "admission_id",
    "billing.csv": "bill_id",
    "billing_detail.csv": "billing_detail_id",
    "patient_diagnostic.csv": "patient_diagnostic_id",
    "patient_insurance.csv": "patient_insurance_id",
    "prescription.csv": "prescription_id",
    "staff_assignment.csv": "assignment_id"
}

print("=" * 80)
print("ENTERPRISE HEALTHCARE OPERATIONS INTELLIGENCE PLATFORM")
print("ENHANCED DATASET AUDIT")
print("=" * 80)

summary = []

# ==========================================================
# LOOP THROUGH DATASETS
# ==========================================================

for file in sorted(os.listdir(DATASET_FOLDER)):

    if not file.endswith(".csv"):
        continue

    filepath = os.path.join(DATASET_FOLDER, file)

    try:

        df = pd.read_csv(filepath)

        rows = len(df)
        cols = len(df.columns)

        pk = PRIMARY_KEYS.get(file)

        duplicate_pk = 0
        null_pk = 0

        if pk in df.columns:

            duplicate_pk = df.duplicated(subset=[pk]).sum()
            null_pk = df[pk].isnull().sum()

        total_nulls = df.isnull().sum().sum()

        duplicate_rows = df.duplicated().sum()

        summary.append({
            "Dataset": file,
            "Rows": rows,
            "Columns": cols,
            "Duplicate PK": duplicate_pk,
            "NULL PK": null_pk,
            "Duplicate Rows": duplicate_rows,
            "Total NULLs": total_nulls
        })

        print("\n" + "=" * 80)
        print(file.upper())
        print("=" * 80)

        print(f"Rows               : {rows}")
        print(f"Columns            : {cols}")
        print(f"Primary Key        : {pk}")
        print(f"Duplicate PK       : {duplicate_pk}")
        print(f"NULL PK            : {null_pk}")
        print(f"Duplicate Rows     : {duplicate_rows}")
        print(f"Total NULL Values  : {total_nulls}")

        print("\nColumn Data Types")

        print(df.dtypes)

    except Exception as e:

        print("\nERROR:", file)
        print(e)

# ==========================================================
# SUMMARY
# ==========================================================

summary_df = pd.DataFrame(summary)

print("\n")
print("=" * 80)
print("FINAL AUDIT SUMMARY")
print("=" * 80)

print(summary_df)

summary_df.to_csv(
    "documentation/enhanced_dataset_audit_summary.csv",
    index=False
)

print("\nAudit Summary Saved Successfully")

print("=" * 80)
print("AUDIT COMPLETED")
print("=" * 80)