# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Patient Insurance
# ==========================================================

import random
import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/patient_insurance.csv"

PATIENT_FILE = "datasets/enhanced/patient.csv"
INSURANCE_PROVIDER_FILE = "datasets/enhanced/insurance_provider.csv"

OUTPUT_FILE = "datasets/enhanced/patient_insurance.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

insurance_df = pd.read_csv(INPUT_FILE)

patient_df = pd.read_csv(PATIENT_FILE)

provider_df = pd.read_csv(INSURANCE_PROVIDER_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Patient Insurance Dataset")
print("=" * 60)

print(f"Original Shape : {insurance_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

insurance_df.columns = (
    insurance_df.columns
    .str.strip()
    .str.lower()
)

patient_df.columns = (
    patient_df.columns
    .str.strip()
    .str.lower()
)

provider_df.columns = (
    provider_df.columns
    .str.strip()
    .str.lower()
)

# ==========================================================
# Normalize Provider Primary Key
# ==========================================================

if "provider_id" in provider_df.columns:
    provider_df.rename(
        columns={
            "provider_id":"insurance_provider_id"
        },
        inplace=True
    )

insurance_df["policy_start_date"] = pd.to_datetime(
    insurance_df["policy_start_date"]
)

insurance_df["policy_end_date"] = pd.to_datetime(
    insurance_df["policy_end_date"]
)

SYSTEM_USER = "System"

print("\nGenerating enterprise insurance attributes...")
# ==========================================================
# Patient Name Lookup
# ==========================================================

patient_lookup = (
    patient_df
    .set_index("patient_id")
)

insurance_df["policy_holder_name"] = (

    patient_lookup.loc[
        insurance_df["patient_id"],
        "first_name"
    ].values

    + " "

    +

    patient_lookup.loc[
        insurance_df["patient_id"],
        "last_name"
    ].values

)

# ==========================================================
# Relationship
# ==========================================================

insurance_df["relationship_with_holder"] = np.random.choice(

    [
        "Self",
        "Spouse",
        "Father",
        "Mother",
        "Guardian"
    ],

    size=len(insurance_df),

    p=[
        0.76,
        0.10,
        0.06,
        0.05,
        0.03
    ]

)

# ==========================================================
# Coverage Amount
# ==========================================================

coverage_amount = np.random.choice(

    [
        100000,
        200000,
        300000,
        500000,
        1000000
    ],

    size=len(insurance_df),

    p=[
        0.18,
        0.22,
        0.22,
        0.28,
        0.10
    ]

)

insurance_df["coverage_amount"] = coverage_amount

insurance_df["remaining_coverage"] = (

    coverage_amount *

    np.random.uniform(
        0.20,
        1.00,
        len(insurance_df)
    )

).round(2)

# ==========================================================
# Insurance Status
# ==========================================================

today = pd.Timestamp.today()

insurance_df["insurance_status"] = np.where(

    insurance_df["policy_end_date"] >= today,

    "Active",

    "Expired"

)

# ==========================================================
# Cashless Eligibility
# ==========================================================

insurance_df["cashless_eligible"] = np.random.choice(

    [True, False],

    size=len(insurance_df),

    p=[
        0.72,
        0.28
    ]

)

# ==========================================================
# Pre-Authorization Number
# ==========================================================

pre_auth = np.where(

    insurance_df["cashless_eligible"],

    [
        f"PA{100000+i}"
        for i in range(len(insurance_df))
    ],

    None

)

insurance_df["pre_authorization_number"] = pre_auth

# ==========================================================
# Remarks
# ==========================================================

insurance_df["remarks"] = np.random.choice(

    [
        "System Generated",
        "Verified",
        "Cashless Approved",
        "Waiting Approval",
        "Policy Renewed"
    ],

    size=len(insurance_df)

)

insurance_df["created_by"] = SYSTEM_USER
insurance_df["updated_by"] = SYSTEM_USER

insurance_df["created_date"] = (
    insurance_df["policy_start_date"].dt.date
)

insurance_df["updated_date"] = (
    insurance_df["policy_start_date"].dt.date
)
# ==========================================================
# Final Column Order
# ==========================================================

insurance_df = insurance_df[
    [
        "patient_insurance_id",
        "patient_id",
        "insurance_provider_id",
        "policy_number",
        "policy_holder_name",
        "relationship_with_holder",
        "policy_start_date",
        "policy_end_date",
        "coverage_amount",
        "remaining_coverage",
        "insurance_status",
        "cashless_eligible",
        "pre_authorization_number",
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

print("\nValidating enhanced patient insurance dataset...")

duplicate_ids = (
    insurance_df["patient_insurance_id"]
    .duplicated()
    .sum()
)

duplicate_policy = (
    insurance_df["policy_number"]
    .duplicated()
    .sum()
)

invalid_patient = (
    ~insurance_df["patient_id"].isin(
        patient_df["patient_id"]
    )
).sum()

invalid_provider = (
    ~insurance_df["insurance_provider_id"].isin(
        provider_df["insurance_provider_id"]
    )
).sum()

invalid_coverage = (
    insurance_df["remaining_coverage"] >
    insurance_df["coverage_amount"]
).sum()

invalid_policy_dates = (
    insurance_df["policy_end_date"] <
    insurance_df["policy_start_date"]
).sum()

null_summary = insurance_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

insurance_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 70)
print("PATIENT INSURANCE DATASET ENHANCEMENT SUMMARY")
print("=" * 70)

print(f"Original Shape              : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape              : {insurance_df.shape}")

print("\nPrimary Key Validation")

print(f"Duplicate IDs               : {duplicate_ids}")
print(f"Duplicate Policy Numbers    : {duplicate_policy}")

print("\nForeign Key Validation")

print(f"Invalid Patient IDs         : {invalid_patient}")
print(f"Invalid Provider IDs        : {invalid_provider}")

print("\nBusiness Rule Validation")

print(f"Remaining > Coverage Amount : {invalid_coverage}")
print(f"Invalid Policy Dates        : {invalid_policy_dates}")

print("\nNull Summary")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nPatient Insurance enhancement completed successfully.")

print("=" * 70)