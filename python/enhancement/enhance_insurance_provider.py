# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Insurance Provider
# Part 1
# ==========================================================

import pandas as pd
import random

INPUT_FILE = "datasets/original/insurance_provider.csv"
OUTPUT_FILE = "datasets/enhanced/insurance_provider.csv"

insurance_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("INSURANCE PROVIDER TABLE AUDIT")
print("=" * 70)

print("\nShape :", insurance_df.shape)

print("\nColumns")
print(insurance_df.columns.tolist())

print("\nProvider Types")
print(insurance_df["provider_type"].unique())

print("\nDuplicate Records :", insurance_df.duplicated().sum())

# ==========================================================
# Lookup Dictionaries
# ==========================================================

claim_processing_lookup = {
    "Private": 7,
    "Govt": 15
}

network_lookup = {
    "Private": "Regional Network",
    "Govt": "National Network"
}

coverage_lookup = {
    "Private": "Individual Health Insurance",
    "Govt": "Government Health Scheme"
}

claim_ratio_lookup = {
    "Private": 93.2,
    "Govt": 96.5
}

cashless_lookup = {
    "Private": "Yes",
    "Govt": "Yes"
}

pre_auth_lookup = {
    "Private": "Yes",
    "Govt": "Yes"
}

max_claim_lookup = {
    "Private": 1000000,
    "Govt": 500000
}

policy_year_lookup = {
    "Private": 1,
    "Govt": 1
}

# ==========================================================
# Helper Function
# ==========================================================

def lookup(dictionary, value, default):
    return dictionary.get(value, default)

# ==========================================================
# Enterprise Columns
# ==========================================================

insurance_df["provider_code"] = [
    f"INS{str(i).zfill(3)}"
    for i in range(1, len(insurance_df) + 1)
]

insurance_df["claim_processing_days"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        claim_processing_lookup,
        x,
        10
    )
)

insurance_df["network_type"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        network_lookup,
        x,
        "Regional Network"
    )
)

insurance_df["coverage_type"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        coverage_lookup,
        x,
        "Individual Health Insurance"
    )
)

insurance_df["claim_settlement_ratio"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        claim_ratio_lookup,
        x,
        95.0
    )
)

insurance_df["cashless_available"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        cashless_lookup,
        x,
        "Yes"
    )
)

insurance_df["pre_authorization_required"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        pre_auth_lookup,
        x,
        "Yes"
    )
)

insurance_df["max_claim_amount"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        max_claim_lookup,
        x,
        500000
    )
)

insurance_df["policy_validity_years"] = insurance_df[
    "provider_type"
].apply(
    lambda x: lookup(
        policy_year_lookup,
        x,
        1
    )
)

insurance_df["support_email"] = (
    insurance_df["provider_name"]
    .str.lower()
    .str.replace(" ", "", regex=False)
    .str.replace(".", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.replace("&", "", regex=False)
    + "@insurance.com"
)

insurance_df["grievance_email"] = (
    "grievance@"
    + insurance_df["provider_name"]
        .str.lower()
        .str.replace(" ", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("&", "", regex=False)
    + ".com"
)

insurance_df["support_phone"] = [
    f"+91-1800-{random.randint(100000,999999)}"
    for _ in range(len(insurance_df))
]

insurance_df["website"] = (
    "www."
    + insurance_df["provider_name"]
        .str.lower()
        .str.replace(" ", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("&", "", regex=False)
    + ".com"
)

insurance_df["provider_status"] = "Active"

insurance_df["created_by"] = "System"

insurance_df["updated_by"] = "System"

insurance_df["created_date"] = "2023-01-01"

insurance_df["updated_date"] = "2025-01-01"

# ==========================================================
# Data Quality Checks
# ==========================================================

insurance_df["provider_code"] = insurance_df[
    "provider_code"
].fillna("INS000")

insurance_df["claim_processing_days"] = insurance_df[
    "claim_processing_days"
].fillna(10)

insurance_df["network_type"] = insurance_df[
    "network_type"
].fillna("Regional Network")

insurance_df["coverage_type"] = insurance_df[
    "coverage_type"
].fillna("Individual Health Insurance")

insurance_df["claim_settlement_ratio"] = insurance_df[
    "claim_settlement_ratio"
].fillna(95.0)

insurance_df["cashless_available"] = insurance_df[
    "cashless_available"
].fillna("Yes")

insurance_df["pre_authorization_required"] = insurance_df[
    "pre_authorization_required"
].fillna("Yes")

insurance_df["max_claim_amount"] = insurance_df[
    "max_claim_amount"
].fillna(500000)

insurance_df["policy_validity_years"] = insurance_df[
    "policy_validity_years"
].fillna(1)

insurance_df["support_email"] = insurance_df[
    "support_email"
].fillna("support@insurance.com")

insurance_df["grievance_email"] = insurance_df[
    "grievance_email"
].fillna("grievance@insurance.com")

insurance_df["support_phone"] = insurance_df[
    "support_phone"
].fillna("+91-1800-000000")

insurance_df["website"] = insurance_df[
    "website"
].fillna("www.insurance.com")

insurance_df["provider_status"] = insurance_df[
    "provider_status"
].fillna("Active")

insurance_df["created_by"] = insurance_df[
    "created_by"
].fillna("System")

insurance_df["updated_by"] = insurance_df[
    "updated_by"
].fillna("System")

insurance_df["created_date"] = insurance_df[
    "created_date"
].fillna("2023-01-01")

insurance_df["updated_date"] = insurance_df[
    "updated_date"
].fillna("2025-01-01")

# ==========================================================
# Data Type Standardization
# ==========================================================

insurance_df["claim_processing_days"] = insurance_df[
    "claim_processing_days"
].astype(int)

insurance_df["claim_settlement_ratio"] = insurance_df[
    "claim_settlement_ratio"
].astype(float)

insurance_df["max_claim_amount"] = insurance_df[
    "max_claim_amount"
].astype(int)

insurance_df["policy_validity_years"] = insurance_df[
    "policy_validity_years"
].astype(int)

# ==========================================================
# Duplicate Check
# ==========================================================

duplicate_count = insurance_df.duplicated().sum()

print("\nDuplicate Records :", duplicate_count)

# ==========================================================
# Missing Value Report
# ==========================================================

print("\nMissing Values\n")

print(insurance_df.isnull().sum())

# ==========================================================
# Preview
# ==========================================================

print("\nEnhanced Insurance Provider Preview\n")

print(insurance_df.head())

# ==========================================================
# Final Columns
# ==========================================================

print("\nFinal Columns\n")

for column in insurance_df.columns:
    print(column)

# ==========================================================
# Final Shape
# ==========================================================

print("\nFinal Shape :", insurance_df.shape)

# ==========================================================
# Save Enhanced Dataset
# ==========================================================

insurance_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nEnhanced Insurance Provider dataset saved successfully.")

print(f"Output File : {OUTPUT_FILE}")

print("\nInsurance Provider Enhancement Completed Successfully")