# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Admission
# ==========================================================

import random
from datetime import timedelta

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/admission.csv"

PATIENT_FILE = "datasets/enhanced/patient.csv"
DOCTOR_FILE = "datasets/enhanced/doctor.csv"
DEPARTMENT_FILE = "datasets/enhanced/department.csv"
WARD_FILE = "datasets/enhanced/ward.csv"
BED_FILE = "datasets/enhanced/bed.csv"
DISEASE_FILE = "datasets/enhanced/disease.csv"

OUTPUT_FILE = "datasets/enhanced/admission.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

admission_df = pd.read_csv(INPUT_FILE)

patient_df = pd.read_csv(PATIENT_FILE)
doctor_df = pd.read_csv(DOCTOR_FILE)
department_df = pd.read_csv(DEPARTMENT_FILE)
ward_df = pd.read_csv(WARD_FILE)
bed_df = pd.read_csv(BED_FILE)
disease_df = pd.read_csv(DISEASE_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Admission Dataset")
print("=" * 60)

print(f"Original Shape : {admission_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

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

department_df.columns = (
    department_df.columns
    .str.strip()
    .str.lower()
)

ward_df.columns = (
    ward_df.columns
    .str.strip()
    .str.lower()
)

bed_df.columns = (
    bed_df.columns
    .str.strip()
    .str.lower()
)

disease_df.columns = (
    disease_df.columns
    .str.strip()
    .str.lower()
)

# ==========================================================
# Convert Dates
# ==========================================================

admission_df["admission_date"] = pd.to_datetime(
    admission_df["admission_date"]
)

admission_df["discharge_date"] = pd.to_datetime(
    admission_df["discharge_date"],
    errors="coerce"
)

# ==========================================================
# Foreign Key Lists
# ==========================================================

doctor_ids = doctor_df["doctor_id"].tolist()

department_ids = department_df["department_id"].tolist()

ward_ids = ward_df["ward_id"].tolist()

bed_ids = bed_df["bed_id"].tolist()

disease_ids = disease_df["disease_id"].tolist()

# ==========================================================
# Enterprise Lookup Values
# ==========================================================

ADMISSION_SOURCES = [
    "Emergency",
    "Referral",
    "Walk-In",
    "Transfer",
    "Outpatient"
]

ADMISSION_SOURCE_WEIGHTS = [
    0.34,
    0.22,
    0.16,
    0.08,
    0.20
]

REFERRAL_SOURCES = [
    "Self",
    "Clinic",
    "Corporate",
    "Government",
    "Primary Care",
    None
]

REFERRAL_WEIGHTS = [
    0.30,
    0.18,
    0.12,
    0.08,
    0.12,
    0.20
]

DISCHARGE_DISPOSITIONS = [
    "Home",
    "Transferred",
    "Expired",
    "Rehabilitation"
]

DISCHARGE_WEIGHTS = [
    0.82,
    0.08,
    0.03,
    0.07
]

ADMISSION_PRIORITY = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

PRIORITY_WEIGHTS = [
    0.22,
    0.46,
    0.23,
    0.09
]

SYSTEM_USER = "System"

print("\nGenerating enterprise admission attributes...")
# ==========================================================
# Enterprise Attribute Generation
# ==========================================================

# -------------------------------
# Length of Stay
# -------------------------------

admission_df["actual_length_of_stay"] = (
    admission_df["discharge_date"] -
    admission_df["admission_date"]
).dt.days

admission_df["actual_length_of_stay"] = (
    admission_df["actual_length_of_stay"]
    .fillna(0)
    .clip(lower=0)
    .astype(int)
)

variation = np.random.randint(
    -1,
    3,
    size=len(admission_df)
)

admission_df["expected_length_of_stay"] = (
    admission_df["actual_length_of_stay"] +
    variation
).clip(lower=1)

# -------------------------------
# Doctor Assignment
# -------------------------------

admission_df["admitting_doctor_id"] = np.random.choice(
    doctor_ids,
    size=len(admission_df)
)

admission_df["discharge_doctor_id"] = np.where(

    admission_df["admission_status"]
    .str.lower()
    .eq("discharged"),

    np.random.choice(
        doctor_ids,
        size=len(admission_df)
    ),

    np.nan

)

# -------------------------------
# Admission Source
# -------------------------------

admission_df["admission_source"] = np.random.choice(

    ADMISSION_SOURCES,

    size=len(admission_df),

    p=ADMISSION_SOURCE_WEIGHTS

)

# -------------------------------
# Referral Source
# -------------------------------

admission_df["referral_source"] = np.random.choice(

    REFERRAL_SOURCES,

    size=len(admission_df),

    p=REFERRAL_WEIGHTS

)

# -------------------------------
# Discharge Disposition
# -------------------------------

disposition = np.random.choice(

    DISCHARGE_DISPOSITIONS,

    size=len(admission_df),

    p=DISCHARGE_WEIGHTS

)

admission_df["discharge_disposition"] = np.where(

    admission_df["admission_status"]
    .str.lower()
    .eq("discharged"),

    disposition,

    None

)

# -------------------------------
# Admission Priority
# -------------------------------

admission_df["admission_priority"] = np.random.choice(

    ADMISSION_PRIORITY,

    size=len(admission_df),

    p=PRIORITY_WEIGHTS

)

# -------------------------------
# Remarks
# -------------------------------

remark_options = [

    "Stable Condition",
    "Routine Admission",
    "Observation Required",
    "High Risk Patient",
    "Post Surgery Monitoring",
    "Transferred From Another Facility",
    "Requires Specialist Consultation",
    "System Generated"

]

admission_df["remarks"] = np.random.choice(

    remark_options,

    size=len(admission_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

admission_df["created_by"] = SYSTEM_USER

admission_df["updated_by"] = SYSTEM_USER

random_days = np.random.randint(
    0,
    365,
    size=len(admission_df)
)

admission_df["created_date"] = (
    admission_df["admission_date"] -
    pd.to_timedelta(random_days, unit="D")
)

admission_df["created_date"] = (
    admission_df["created_date"]
    .dt.date
)

admission_df["updated_date"] = np.where(

    admission_df["discharge_date"].notna(),

    admission_df["discharge_date"],

    admission_df["admission_date"]

)

admission_df["updated_date"] = pd.to_datetime(
    admission_df["updated_date"]
).dt.date

# ==========================================================
# Data Quality Standardization
# ==========================================================

admission_df["admission_source"] = (
    admission_df["admission_source"]
    .str.title()
)

admission_df["referral_source"] = (
    admission_df["referral_source"]
)

admission_df["discharge_disposition"] = (
    admission_df["discharge_disposition"]
)

admission_df["admission_priority"] = (
    admission_df["admission_priority"]
)

admission_df["remarks"] = (
    admission_df["remarks"]
)

print("Enterprise attributes generated successfully.")
# ==========================================================
# Final Column Order
# ==========================================================

admission_df = admission_df[
    [
        "admission_id",
        "patient_id",
        "admission_date",
        "discharge_date",
        "admission_type",
        "admission_status",
        "department_id",
        "ward_id",
        "bed_id",
        "disease_id",
        "admitting_doctor_id",
        "discharge_doctor_id",
        "admission_source",
        "referral_source",
        "expected_length_of_stay",
        "actual_length_of_stay",
        "discharge_disposition",
        "admission_priority",
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

print("\nValidating enhanced admission dataset...")

duplicate_admission_ids = admission_df["admission_id"].duplicated().sum()

invalid_patient = (
    ~admission_df["patient_id"].isin(patient_df["patient_id"])
).sum()

invalid_department = (
    ~admission_df["department_id"].isin(department_df["department_id"])
).sum()

invalid_ward = (
    ~admission_df["ward_id"].isin(ward_df["ward_id"])
).sum()

invalid_bed = (
    ~admission_df["bed_id"].isin(bed_df["bed_id"])
).sum()

invalid_disease = (
    ~admission_df["disease_id"].isin(disease_df["disease_id"])
).sum()

invalid_admitting_doctor = (
    ~admission_df["admitting_doctor_id"].isin(doctor_df["doctor_id"])
).sum()

invalid_discharge_doctor = (
    admission_df["discharge_doctor_id"].notna()
    &
    ~admission_df["discharge_doctor_id"].isin(doctor_df["doctor_id"])
).sum()

null_summary = admission_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

admission_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 65)
print("ADMISSION DATASET ENHANCEMENT SUMMARY")
print("=" * 65)

print(f"Original Shape                : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape                : {admission_df.shape}")

print("\nPrimary Key Validation")

print(f"Duplicate Admission IDs       : {duplicate_admission_ids}")

print("\nForeign Key Validation")

print(f"Invalid Patient IDs           : {invalid_patient}")
print(f"Invalid Department IDs        : {invalid_department}")
print(f"Invalid Ward IDs              : {invalid_ward}")
print(f"Invalid Bed IDs               : {invalid_bed}")
print(f"Invalid Disease IDs           : {invalid_disease}")
print(f"Invalid Admitting Doctor IDs  : {invalid_admitting_doctor}")
print(f"Invalid Discharge Doctor IDs  : {invalid_discharge_doctor}")

print("\nNull Summary")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nAdmission enhancement completed successfully.")

print("=" * 65)