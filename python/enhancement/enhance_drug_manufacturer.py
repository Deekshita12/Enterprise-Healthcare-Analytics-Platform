# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Drug Manufacturer
# ==========================================================

import pandas as pd
import random

INPUT_FILE = "datasets/original/drug_manufacturer.csv"
OUTPUT_FILE = "datasets/enhanced/drug_manufacturer.csv"

manufacturer_df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("DRUG MANUFACTURER TABLE AUDIT")
print("=" * 60)

print("\nShape :", manufacturer_df.shape)

print("\nColumns")
print(manufacturer_df.columns.tolist())

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def generate_email(name):

    clean = (
        name.lower()
        .replace(",", "")
        .replace(".", "")
        .replace("-", " ")
    )

    words = clean.split()

    abbreviation = "".join(word[0] for word in words)

    company = "".join(words[:2])

    domains = [
        f"{abbreviation}pharma.com",
        f"{company}pharma.com",
        f"{company}labs.com",
        f"{abbreviation}health.com"
    ]

    prefixes = [
        "contact",
        "support",
        "info",
        "sales"
    ]

    return f"{random.choice(prefixes)}@{random.choice(domains)}"


def generate_phone():

    return "9" + "".join(
        str(random.randint(0, 9))
        for _ in range(9)
    )


def generate_lead_time(rating):

    if rating >= 4.5:
        return random.randint(3, 7)

    elif rating >= 4.0:
        return random.randint(6, 12)

    else:
        return random.randint(10, 21)


def supplier_tier(rating):

    if rating >= 4.7:
        return "Strategic"

    elif rating >= 4.3:
        return "Preferred"

    elif rating >= 3.8:
        return "Approved"

    else:
        return "Conditional"


# ----------------------------------------------------------
# Add Enterprise Columns
# ----------------------------------------------------------

manufacturer_df["contact_email"] = manufacturer_df["manufacturer_name"].apply(
    generate_email
)

manufacturer_df["contact_phone"] = manufacturer_df["manufacturer_id"].apply(
    lambda x: generate_phone()
)

manufacturer_df["lead_time_days"] = manufacturer_df["reliability_rating"].apply(
    generate_lead_time
)

manufacturer_df["supplier_tier"] = manufacturer_df["reliability_rating"].apply(
    supplier_tier
)

manufacturer_df["manufacturer_code"] = manufacturer_df[
    "manufacturer_id"
].apply(
    lambda x: f"MFG{x:04d}"
)

manufacturer_df["gmp_certified"] = manufacturer_df[
    "reliability_rating"
].apply(
    lambda x: x >= 4.0
)

manufacturer_df["iso_certification"] = "ISO 9001"

manufacturer_df["website"] = manufacturer_df["contact_email"].apply(
    lambda x: f"https://www.{x.split('@')[1]}"
)

manufacturer_df["preferred_supplier"] = manufacturer_df[
    "supplier_tier"
].isin(
    ["Strategic", "Preferred"]
)

manufacturer_df["manufacturer_status"] = manufacturer_df[
    "contract_status"
].replace(
    {
        "Expired": "Inactive",
        "Active": "Active"
    }
)

manufacturer_df["created_date"] = "2023-01-01"

manufacturer_df["updated_date"] = "2025-01-01"

# ----------------------------------------------------------
# Validation
# ----------------------------------------------------------

print("\nPreview\n")

print(manufacturer_df.head())

print("\nMissing Values\n")

print(manufacturer_df.isnull().sum())

print("\nDuplicate Records :", manufacturer_df.duplicated().sum())

print("\nFinal Columns\n")

for col in manufacturer_df.columns:
    print(col)

manufacturer_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nDrug Manufacturer Enhancement Completed Successfully")

print("\nFinal Shape :", manufacturer_df.shape)

print("\nOutput Saved :", OUTPUT_FILE)