# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Patient Diagnostic
# ==========================================================

import random

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/patient_diagnostic.csv"

PATIENT_FILE = "datasets/enhanced/patient.csv"
ADMISSION_FILE = "datasets/enhanced/admission.csv"
DOCTOR_FILE = "datasets/enhanced/doctor.csv"
DIAGNOSTIC_TEST_FILE = "datasets/enhanced/diagnostic_test.csv"

OUTPUT_FILE = "datasets/enhanced/patient_diagnostic.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

diagnostic_df = pd.read_csv(INPUT_FILE)

patient_df = pd.read_csv(PATIENT_FILE)
admission_df = pd.read_csv(ADMISSION_FILE)
doctor_df = pd.read_csv(DOCTOR_FILE)
test_df = pd.read_csv(DIAGNOSTIC_TEST_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Patient Diagnostic Dataset")
print("=" * 60)

print(f"Original Shape : {diagnostic_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

diagnostic_df.columns = (
    diagnostic_df.columns
    .str.strip()
    .str.lower()
)

admission_df.columns = (
    admission_df.columns
    .str.strip()
    .str.lower()
)

patient_df.columns = (
    patient_df.columns
    .str.strip()
    .str.lower()
)

doctor_df.columns = (
    doctor_df.columns
    .str.strip()
    .str.lower()
)

test_df.columns = (
    test_df.columns
    .str.strip()
    .str.lower()
)
# ==========================================================
# Normalize Master Table Keys
# ==========================================================

test_df.rename(
    columns={
        "test_id": "diagnostic_test_id"
    },
    inplace=True
)
diagnostic_df["test_date"] = pd.to_datetime(
    diagnostic_df["test_date"]
)

SYSTEM_USER = "System"

print("\nGenerating enterprise diagnostic attributes...")

# ==========================================================
# Map Admission → Patient
# ==========================================================

patient_lookup = admission_df.set_index(
    "admission_id"
)["patient_id"]

diagnostic_df["patient_id"] = (
    diagnostic_df["admission_id"]
    .map(patient_lookup)
)

# ==========================================================
# Rename Existing Column
# ==========================================================

diagnostic_df.rename(
    columns={
        "test_id": "diagnostic_test_id",
        "result_status": "test_status"
    },
    inplace=True
)

# ==========================================================
# Sample Collection Date
# ==========================================================

hours_before = np.random.randint(
    0,
    24,
    size=len(diagnostic_df)
)

diagnostic_df["sample_collection_date"] = (
    diagnostic_df["test_date"] -
    pd.to_timedelta(hours_before, unit="h")
).dt.date

# ==========================================================
# Report Date
# ==========================================================

hours_after = np.random.randint(
    2,
    72,
    size=len(diagnostic_df)
)

diagnostic_df["report_date"] = (
    diagnostic_df["test_date"] +
    pd.to_timedelta(hours_after, unit="h")
).dt.date

# ==========================================================
# Test Result
# ==========================================================

diagnostic_df["test_result"] = np.random.choice(

    [
        "Normal",
        "Abnormal",
        "Positive",
        "Negative",
        "Borderline"
    ],

    size=len(diagnostic_df),

    p=[
        0.42,
        0.18,
        0.12,
        0.20,
        0.08
    ]

)

# ==========================================================
# Result Summary
# ==========================================================

diagnostic_df["result_summary"] = np.where(

    diagnostic_df["test_result"].isin(
        ["Normal", "Negative"]
    ),

    "No significant abnormalities detected.",

    "Clinical correlation recommended."

)

# ==========================================================
# Critical Result
# ==========================================================

diagnostic_df["critical_result"] = np.random.choice(

    [True, False],

    size=len(diagnostic_df),

    p=[0.07, 0.93]

)

# ==========================================================
# Remarks
# ==========================================================

diagnostic_df["remarks"] = np.random.choice(

    [
        "System Generated",
        "Reviewed by Consultant",
        "Urgent Review Required",
        "Repeat Test Recommended",
        "Quality Checked"
    ],

    size=len(diagnostic_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

diagnostic_df["created_by"] = SYSTEM_USER
diagnostic_df["updated_by"] = SYSTEM_USER

diagnostic_df["created_date"] = (
    diagnostic_df["test_date"].dt.date
)

diagnostic_df["updated_date"] = (
    pd.to_datetime(
        diagnostic_df["report_date"]
    ).dt.date
)
# ==========================================================
# Final Column Order
# ==========================================================

diagnostic_df = diagnostic_df[
    [
        "patient_diagnostic_id",
        "patient_id",
        "admission_id",
        "diagnostic_test_id",
        "doctor_id",
        "test_date",
        "sample_collection_date",
        "report_date",
        "test_status",
        "test_result",
        "result_summary",
        "critical_result",
        "remarks",
        "created_by",
        "updated_by",
        "created_date",
        "updated_date"
    ]
]

# ==========================================================
# Enterprise Validation
# ==========================================================

print("\nValidating enhanced patient diagnostic dataset...")

duplicate_ids = diagnostic_df["patient_diagnostic_id"].duplicated().sum()

invalid_patient = (
    ~diagnostic_df["patient_id"].isin(
        patient_df["patient_id"]
    )
).sum()

invalid_admission = (
    ~diagnostic_df["admission_id"].isin(
        admission_df["admission_id"]
    )
).sum()

invalid_test = (
    ~diagnostic_df["diagnostic_test_id"].isin(
        test_df["diagnostic_test_id"]
    )
).sum()

invalid_doctor = (
    ~diagnostic_df["doctor_id"].isin(
        doctor_df["doctor_id"]
    )
).sum()

future_test_date = (
    pd.to_datetime(diagnostic_df["test_date"]) >
    pd.Timestamp.today()
).sum()

future_report_date = (
    pd.to_datetime(diagnostic_df["report_date"]) >
    pd.Timestamp.today()
).sum()

null_summary = diagnostic_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

diagnostic_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 70)
print("PATIENT DIAGNOSTIC DATASET ENHANCEMENT SUMMARY")
print("=" * 70)

print(f"Original Shape              : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape              : {diagnostic_df.shape}")

print("\nPrimary Key Validation")

print(f"Duplicate IDs               : {duplicate_ids}")

print("\nForeign Key Validation")

print(f"Invalid Patient IDs         : {invalid_patient}")
print(f"Invalid Admission IDs       : {invalid_admission}")
print(f"Invalid Diagnostic Test IDs : {invalid_test}")
print(f"Invalid Doctor IDs          : {invalid_doctor}")

print("\nBusiness Rule Validation")

print(f"Future Test Dates           : {future_test_date}")
print(f"Future Report Dates         : {future_report_date}")

print("\nNull Summary")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nPatient Diagnostic enhancement completed successfully.")

print("=" * 70)