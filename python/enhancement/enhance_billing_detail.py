# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Billing Detail
# ==========================================================

import random

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/billing_detail.csv"

BILL_FILE = "datasets/enhanced/billing.csv"
DOCTOR_FILE = "datasets/enhanced/doctor.csv"
DEPARTMENT_FILE = "datasets/enhanced/department.csv"

OUTPUT_FILE = "datasets/enhanced/billing_detail.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

billing_detail_df = pd.read_csv(INPUT_FILE)

billing_df = pd.read_csv(BILL_FILE)

doctor_df = pd.read_csv(DOCTOR_FILE)

department_df = pd.read_csv(DEPARTMENT_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Billing Detail Dataset")
print("=" * 60)

print(f"Original Shape : {billing_detail_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

billing_detail_df.columns = (
    billing_detail_df.columns
    .str.strip()
    .str.lower()
)

billing_df.columns = (
    billing_df.columns
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

billing_df["bill_date"] = pd.to_datetime(
    billing_df["bill_date"]
)

doctor_ids = doctor_df["doctor_id"].tolist()

department_ids = department_df["department_id"].tolist()

SYSTEM_USER = "System"

print("\nGenerating enterprise billing detail attributes...")
# ==========================================================
# Service Type Mapping
# ==========================================================

SERVICE_MAP = {
    "Consultation": "Doctor Consultation",
    "Lab": "Laboratory Investigation",
    "Radiology": "Radiology Service",
    "Medicine": "Pharmacy",
    "Procedure": "Medical Procedure",
    "Surgery": "Surgical Procedure",
    "Room": "Room Charges",
    "ICU": "ICU Charges",
    "Emergency": "Emergency Services",
    "Misc": "Hospital Services"
}

billing_detail_df["service_type"] = (
    billing_detail_df["charge_type"]
    .astype(str)
    .map(SERVICE_MAP)
    .fillna("General Hospital Service")
)

billing_detail_df["service_description"] = (
    billing_detail_df["service_type"]
)

# ==========================================================
# Pricing
# ==========================================================

billing_detail_df["quantity"] = np.random.randint(
    1,
    6,
    len(billing_detail_df)
)

billing_detail_df["unit_price"] = (
    billing_detail_df["amount"] /
    billing_detail_df["quantity"]
).round(2)

billing_detail_df["total_price"] = (
    billing_detail_df["unit_price"] *
    billing_detail_df["quantity"]
).round(2)

# ==========================================================
# Foreign Keys
# ==========================================================

billing_detail_df["department_id"] = np.random.choice(
    department_ids,
    len(billing_detail_df)
)

billing_detail_df["doctor_id"] = np.random.choice(
    doctor_ids,
    len(billing_detail_df)
)

# ==========================================================
# Service Date
# ==========================================================

bill_date_lookup = billing_df.set_index(
    "bill_id"
)["bill_date"]

billing_detail_df["service_date"] = (
    billing_detail_df["bill_id"]
    .map(bill_date_lookup)
)

# ==========================================================
# Remarks
# ==========================================================

billing_detail_df["remarks"] = np.random.choice(

    [
        "System Generated",
        "Routine Charge",
        "Insurance Claim Item",
        "Verified",
        "Approved"
    ],

    size=len(billing_detail_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

billing_detail_df["created_by"] = SYSTEM_USER
billing_detail_df["updated_by"] = SYSTEM_USER

billing_detail_df["created_date"] = (
    billing_detail_df["service_date"]
)

billing_detail_df["updated_date"] = (
    billing_detail_df["service_date"]
)
# ==========================================================
# Rename Existing Columns
# ==========================================================

billing_detail_df.rename(
    columns={
        "charge_type": "legacy_charge_type",
        "reference_id": "legacy_reference_id",
        "amount": "legacy_amount"
    },
    inplace=True
)

# ==========================================================
# Final Column Order
# ==========================================================

billing_detail_df = billing_detail_df[
    [
        "billing_detail_id",
        "bill_id",
        "service_type",
        "service_description",
        "quantity",
        "unit_price",
        "total_price",
        "service_date",
        "department_id",
        "doctor_id",
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

print("\nValidating enhanced billing detail dataset...")

duplicate_ids = (
    billing_detail_df["billing_detail_id"]
    .duplicated()
    .sum()
)

invalid_bill = (
    ~billing_detail_df["bill_id"].isin(
        billing_df["bill_id"]
    )
).sum()

invalid_department = (
    ~billing_detail_df["department_id"].isin(
        department_df["department_id"]
    )
).sum()

invalid_doctor = (
    ~billing_detail_df["doctor_id"].isin(
        doctor_df["doctor_id"]
    )
).sum()

negative_quantity = (
    billing_detail_df["quantity"] <= 0
).sum()

negative_price = (
    billing_detail_df["unit_price"] < 0
).sum()

negative_total = (
    billing_detail_df["total_price"] < 0
).sum()

null_summary = billing_detail_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

billing_detail_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 65)
print("BILLING DETAIL DATASET ENHANCEMENT SUMMARY")
print("=" * 65)

print(f"Original Shape              : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape              : {billing_detail_df.shape}")

print("\nPrimary Key Validation")

print(f"Duplicate IDs               : {duplicate_ids}")

print("\nForeign Key Validation")

print(f"Invalid Bill IDs            : {invalid_bill}")
print(f"Invalid Department IDs      : {invalid_department}")
print(f"Invalid Doctor IDs          : {invalid_doctor}")

print("\nBusiness Rule Validation")

print(f"Negative Quantity           : {negative_quantity}")
print(f"Negative Unit Price         : {negative_price}")
print(f"Negative Total Price        : {negative_total}")

print("\nNull Summary")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nBilling Detail enhancement completed successfully.")

print("=" * 65)