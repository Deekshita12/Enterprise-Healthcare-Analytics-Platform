# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Prescription
# ==========================================================

import random
import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/prescription.csv"

PATIENT_FILE = "datasets/enhanced/patient.csv"
ADMISSION_FILE = "datasets/enhanced/admission.csv"
DOCTOR_FILE = "datasets/enhanced/doctor.csv"
DRUG_FILE = "datasets/enhanced/drug.csv"

OUTPUT_FILE = "datasets/enhanced/prescription.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

prescription_df = pd.read_csv(INPUT_FILE)

patient_df = pd.read_csv(PATIENT_FILE)
admission_df = pd.read_csv(ADMISSION_FILE)
doctor_df = pd.read_csv(DOCTOR_FILE)
drug_df = pd.read_csv(DRUG_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Prescription Dataset")
print("=" * 60)

print(f"Original Shape : {prescription_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

for df in [
    prescription_df,
    patient_df,
    admission_df,
    doctor_df,
    drug_df
]:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

# Normalize Drug Primary Key
if "medicine_id" in drug_df.columns:
    drug_df.rename(
        columns={
            "medicine_id":"drug_id"
        },
        inplace=True
    )

admission_df["admission_date"] = pd.to_datetime(
    admission_df["admission_date"]
)

SYSTEM_USER = "System"

print("\nGenerating enterprise prescription attributes...")
# ==========================================================
# Admission Lookup
# ==========================================================

admission_lookup = admission_df.set_index(
    "admission_id"
)

prescription_df["patient_id"] = (
    admission_lookup.loc[
        prescription_df["admission_id"],
        "patient_id"
    ].values
)

# ==========================================================
# Doctor Assignment
# ==========================================================

if "admitting_doctor_id" in admission_df.columns:

    prescription_df["doctor_id"] = (
        admission_lookup.loc[
            prescription_df["admission_id"],
            "admitting_doctor_id"
        ].values
    )

else:

    prescription_df["doctor_id"] = np.random.choice(
        doctor_df["doctor_id"],
        len(prescription_df)
    )

# ==========================================================
# Prescription Date
# ==========================================================

offset = np.random.randint(
    0,
    5,
    len(prescription_df)
)

prescription_df["prescription_date"] = (

    admission_lookup.loc[
        prescription_df["admission_id"],
        "admission_date"
    ].values

    +

    pd.to_timedelta(
        offset,
        unit="D"
    )

)

# ==========================================================
# Quantity
# ==========================================================

prescription_df["quantity"] = (

    prescription_df["duration_days"]

    *

    np.random.choice(
        [1,2,3],
        len(prescription_df),
        p=[0.40,0.45,0.15]
    )

).astype(int)

# ==========================================================
# Route of Administration
# ==========================================================

prescription_df["route_of_administration"] = np.random.choice(

    [
        "Oral",
        "Intravenous",
        "Intramuscular",
        "Topical",
        "Inhalation",
        "Subcutaneous"
    ],

    size=len(prescription_df),

    p=[
        0.58,
        0.14,
        0.08,
        0.08,
        0.07,
        0.05
    ]

)

# ==========================================================
# Instructions
# ==========================================================

prescription_df["instructions"] = np.random.choice(

    [
        "Take after meals",
        "Take before meals",
        "Take with water",
        "Bedtime only",
        "Complete full course",
        "As directed by physician"
    ],

    len(prescription_df)

)

# ==========================================================
# Status
# ==========================================================

prescription_df["prescription_status"] = np.random.choice(

    [
        "Active",
        "Completed",
        "Cancelled"
    ],

    len(prescription_df),

    p=[
        0.18,
        0.77,
        0.05
    ]

)

# ==========================================================
# Remarks
# ==========================================================

prescription_df["remarks"] = np.random.choice(

    [
        "System Generated",
        "Reviewed",
        "Verified",
        "Requires Monitoring",
        "Completed Successfully"
    ],

    len(prescription_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

prescription_df["created_by"] = SYSTEM_USER
prescription_df["updated_by"] = SYSTEM_USER

prescription_df["created_date"] = (
    pd.to_datetime(
        prescription_df["prescription_date"]
    ).dt.date
)

prescription_df["updated_date"] = (
    pd.to_datetime(
        prescription_df["prescription_date"]
    ).dt.date
)
# ==========================================================
# Final Column Order
# ==========================================================

prescription_df = prescription_df[
    [
        "prescription_id",
        "patient_id",
        "admission_id",
        "doctor_id",
        "drug_id",
        "prescription_date",
        "dosage",
        "frequency",
        "duration_days",
        "quantity",
        "route_of_administration",
        "instructions",
        "prescription_status",
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

print("\nValidating enhanced prescription dataset...")

duplicate_ids = (
    prescription_df["prescription_id"]
    .duplicated()
    .sum()
)

invalid_patient = (
    ~prescription_df["patient_id"].isin(
        patient_df["patient_id"]
    )
).sum()

invalid_admission = (
    ~prescription_df["admission_id"].isin(
        admission_df["admission_id"]
    )
).sum()

invalid_doctor = (
    ~prescription_df["doctor_id"].isin(
        doctor_df["doctor_id"]
    )
).sum()

invalid_drug = (
    ~prescription_df["drug_id"].isin(
        drug_df["drug_id"]
    )
).sum()

invalid_quantity = (
    prescription_df["quantity"] <= 0
).sum()

invalid_duration = (
    prescription_df["duration_days"] <= 0
).sum()

future_prescriptions = (
    pd.to_datetime(
        prescription_df["prescription_date"]
    ) > pd.Timestamp.today()
).sum()

null_summary = prescription_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

prescription_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 70)
print("PRESCRIPTION DATASET ENHANCEMENT SUMMARY")
print("=" * 70)

print(f"Original Shape              : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape              : {prescription_df.shape}")

print("\nPrimary Key Validation")

print(f"Duplicate IDs               : {duplicate_ids}")

print("\nForeign Key Validation")

print(f"Invalid Patient IDs         : {invalid_patient}")
print(f"Invalid Admission IDs       : {invalid_admission}")
print(f"Invalid Doctor IDs          : {invalid_doctor}")
print(f"Invalid Drug IDs            : {invalid_drug}")

print("\nBusiness Rule Validation")

print(f"Invalid Quantity            : {invalid_quantity}")
print(f"Invalid Duration            : {invalid_duration}")
print(f"Future Prescription Dates   : {future_prescriptions}")

print("\nNull Summary")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nPrescription enhancement completed successfully.")

print("=" * 70)