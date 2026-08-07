# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Billing
# ==========================================================

import random

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/billing.csv"

ADMISSION_FILE = "datasets/enhanced/admission.csv"

OUTPUT_FILE = "datasets/enhanced/billing.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

billing_df = pd.read_csv(INPUT_FILE)

admission_df = pd.read_csv(ADMISSION_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Billing Dataset")
print("=" * 60)

print(f"Original Shape : {billing_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

billing_df.columns = (
    billing_df.columns
    .str.strip()
    .str.lower()
)

admission_df.columns = (
    admission_df.columns
    .str.strip()
    .str.lower()
)

billing_df["bill_date"] = pd.to_datetime(
    billing_df["bill_date"]
)

SYSTEM_USER = "System"

print("\nGenerating enterprise billing attributes...")
# ==========================================================
# Discount Amount
# ==========================================================

discount_percent = np.random.choice(

    [0, 2, 5, 10, 15],

    size=len(billing_df),

    p=[0.45, 0.15, 0.20, 0.15, 0.05]

)

billing_df["discount_amount"] = (
    billing_df["total_amount"] *
    discount_percent /
    100
).round(2)

# ==========================================================
# Tax Amount (5%)
# ==========================================================

billing_df["tax_amount"] = (

    (
        billing_df["total_amount"] -
        billing_df["discount_amount"]
    ) * 0.05

).round(2)

# ==========================================================
# Bill Status
# ==========================================================

billing_df["bill_status"] = np.where(

    billing_df["payment_status"]
    .str.lower()
    .eq("paid"),

    "Closed",

    np.random.choice(

        [
            "Generated",
            "Pending",
            "Processing"
        ],

        size=len(billing_df),

        p=[0.50,0.35,0.15]

    )

)

# ==========================================================
# Remarks
# ==========================================================

remarks = [

    "System Generated",

    "Insurance Processing",

    "Awaiting Payment",

    "Corporate Billing",

    "Cash Settlement",

    "Final Invoice"

]

billing_df["remarks"] = np.random.choice(

    remarks,

    size=len(billing_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

billing_df["created_by"] = SYSTEM_USER

billing_df["updated_by"] = SYSTEM_USER

days_back = np.random.randint(

    0,

    60,

    size=len(billing_df)

)

billing_df["created_date"] = (

    billing_df["bill_date"] -

    pd.to_timedelta(days_back, unit="D")

).dt.date

billing_df["updated_date"] = (

    billing_df["bill_date"]

).dt.date

print("Enterprise billing attributes generated.")
# ==========================================================
# Final Column Order
# ==========================================================

billing_df = billing_df[

    [

        "bill_id",

        "admission_id",

        "bill_date",

        "total_amount",

        "insurance_covered_amount",

        "patient_payable_amount",

        "payment_status",

        "payment_mode",

        "discount_amount",

        "tax_amount",

        "bill_status",

        "remarks",

        "created_by",

        "updated_by",

        "created_date",

        "updated_date"

    ]

]

# ==========================================================
# Validation
# ==========================================================

duplicate_bill_ids = billing_df["bill_id"].duplicated().sum()

invalid_admission_ids = (

    ~billing_df["admission_id"].isin(

        admission_df["admission_id"]

    )

).sum()

# ==========================================================
# Export
# ==========================================================

billing_df.to_csv(

    OUTPUT_FILE,

    index=False

)

# ==========================================================
# Summary
# ==========================================================

print("\n" + "="*60)

print("BILLING DATASET ENHANCEMENT SUMMARY")

print("="*60)

print(f"Original Shape : {pd.read_csv(INPUT_FILE).shape}")

print(f"Enhanced Shape : {billing_df.shape}")

print()

print(f"Duplicate Bill IDs : {duplicate_bill_ids}")

print(f"Invalid Admission IDs : {invalid_admission_ids}")

print()

print("Output File")

print(OUTPUT_FILE)

print()

print("Billing enhancement completed successfully.")

print("="*60)