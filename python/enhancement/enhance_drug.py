# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Drug
# ==========================================================

import pandas as pd
import numpy as np

INPUT_FILE = "datasets/original/drug.csv"
OUTPUT_FILE = "datasets/enhanced/drug.csv"

drug_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("DRUG TABLE AUDIT")
print("=" * 70)

print("\nShape :", drug_df.shape)

print("\nColumns")
print(drug_df.columns.tolist())

print("\nDrug Categories")
print(drug_df["drug_category"].unique())

# ==========================================================
# Lookup Dictionaries
# ==========================================================

dosage_lookup = {
    "Antibiotic": "Capsule",
    "Analgesic": "Tablet",
    "Antipyretic": "Tablet",
    "Antacid": "Suspension",
    "Antihypertensive": "Tablet",
    "Vitamin": "Tablet",
    "Steroid": "Injection",
    "Antidiabetic": "Tablet"
}

storage_lookup = {
    "Antibiotic": "Room Temperature",
    "Analgesic": "Room Temperature",
    "Antipyretic": "Room Temperature",
    "Antacid": "Cool & Dry",
    "Antihypertensive": "Cool & Dry",
    "Vitamin": "Room Temperature",
    "Steroid": "Refrigerated (2-8°C)",
    "Antidiabetic": "Refrigerated (2-8°C)"
}

expiry_lookup = {
    "Antibiotic": 24,
    "Analgesic": 36,
    "Antipyretic": 24,
    "Antacid": 24,
    "Antihypertensive": 36,
    "Vitamin": 36,
    "Steroid": 18,
    "Antidiabetic": 18
}

prescription_lookup = {
    "Antibiotic": True,
    "Analgesic": False,
    "Antipyretic": False,
    "Antacid": False,
    "Antihypertensive": True,
    "Vitamin": False,
    "Steroid": True,
    "Antidiabetic": True
}

route_lookup = {
    "Antibiotic": "Oral",
    "Analgesic": "Oral",
    "Antipyretic": "Oral",
    "Antacid": "Oral",
    "Antihypertensive": "Oral",
    "Vitamin": "Oral",
    "Steroid": "Injection",
    "Antidiabetic": "Injection"
}

therapeutic_lookup = {
    "Antibiotic": "Anti-Infective",
    "Analgesic": "Pain Management",
    "Antipyretic": "Fever Management",
    "Antacid": "Gastrointestinal",
    "Antihypertensive": "Cardiovascular",
    "Vitamin": "Nutritional Supplement",
    "Steroid": "Hormonal Therapy",
    "Antidiabetic": "Endocrinology"
}

schedule_lookup = {
    "Antibiotic": "Schedule H",
    "Analgesic": "OTC",
    "Antipyretic": "OTC",
    "Antacid": "OTC",
    "Antihypertensive": "Schedule H",
    "Vitamin": "OTC",
    "Steroid": "Schedule H",
    "Antidiabetic": "Schedule H"
}

strength_lookup = {
    "Antibiotic": "500 mg",
    "Analgesic": "650 mg",
    "Antipyretic": "500 mg",
    "Antacid": "170 ml",
    "Antihypertensive": "5 mg",
    "Vitamin": "1000 IU",
    "Steroid": "40 mg/ml",
    "Antidiabetic": "500 mg"
}

unit_lookup = {
    "Capsule": "Capsule",
    "Tablet": "Tablet",
    "Suspension": "Bottle",
    "Injection": "Vial"
}

generic_lookup = {
    "Antibiotic": "Generic",
    "Analgesic": "Generic",
    "Antipyretic": "Generic",
    "Antacid": "Brand",
    "Antihypertensive": "Brand",
    "Vitamin": "Brand",
    "Steroid": "Generic",
    "Antidiabetic": "Brand"
}

# ==========================================================
# Helper Function
# ==========================================================

def lookup(dictionary, value, default):
    return dictionary.get(value, default)

# ==========================================================
# Enterprise Columns
# ==========================================================

drug_df["dosage_form"] = drug_df["drug_category"].apply(
    lambda x: lookup(dosage_lookup, x, "Tablet")
)

drug_df["prescription_required"] = drug_df["drug_category"].apply(
    lambda x: lookup(prescription_lookup, x, True)
)

drug_df["storage_condition"] = drug_df["drug_category"].apply(
    lambda x: lookup(storage_lookup, x, "Room Temperature")
)

drug_df["expiry_months"] = drug_df["drug_category"].apply(
    lambda x: lookup(expiry_lookup, x, 24)
)

drug_df["route_of_administration"] = drug_df["drug_category"].apply(
    lambda x: lookup(route_lookup, x, "Oral")
)

drug_df["therapeutic_class"] = drug_df["drug_category"].apply(
    lambda x: lookup(therapeutic_lookup, x, "General Medicine")
)

drug_df["drug_schedule"] = drug_df["drug_category"].apply(
    lambda x: lookup(schedule_lookup, x, "OTC")
)

drug_df["strength"] = drug_df["drug_category"].apply(
    lambda x: lookup(strength_lookup, x, "500 mg")
)

drug_df["unit_of_measure"] = drug_df["dosage_form"].apply(
    lambda x: lookup(unit_lookup, x, "Tablet")
)

drug_df["generic_or_brand"] = drug_df["drug_category"].apply(
    lambda x: lookup(generic_lookup, x, "Generic")
)

drug_df["controlled_substance"] = np.where(
    drug_df["drug_schedule"] == "Schedule H",
    True,
    False
)

drug_df["high_alert_medication"] = drug_df["drug_category"].isin(
    [
        "Steroid",
        "Antidiabetic",
        "Antihypertensive"
    ]
)

drug_df["drug_status"] = "Active"
# ==========================================================
# Enterprise Audit Columns
# ==========================================================

drug_df["created_by"] = "System"

drug_df["updated_by"] = "System"

drug_df["created_date"] = "2023-01-01"

drug_df["updated_date"] = "2025-01-01"

# ==========================================================
# Data Quality Checks
# ==========================================================

drug_df["drug_name"] = (
    drug_df["drug_name"]
    .astype(str)
    .str.strip()
)

drug_df["brand_name"] = (
    drug_df["brand_name"]
    .astype(str)
    .str.strip()
)

drug_df["drug_category"] = (
    drug_df["drug_category"]
    .astype(str)
    .str.strip()
)

drug_df["dosage_form"] = drug_df["dosage_form"].fillna("Tablet")

drug_df["storage_condition"] = drug_df["storage_condition"].fillna(
    "Room Temperature"
)

drug_df["route_of_administration"] = drug_df[
    "route_of_administration"
].fillna("Oral")

drug_df["therapeutic_class"] = drug_df[
    "therapeutic_class"
].fillna("General Medicine")

drug_df["drug_schedule"] = drug_df[
    "drug_schedule"
].fillna("OTC")

drug_df["strength"] = drug_df[
    "strength"
].fillna("500 mg")

drug_df["unit_of_measure"] = drug_df[
    "unit_of_measure"
].fillna("Tablet")

drug_df["generic_or_brand"] = drug_df[
    "generic_or_brand"
].fillna("Generic")

drug_df["drug_status"] = drug_df[
    "drug_status"
].fillna("Active")

drug_df["expiry_months"] = drug_df[
    "expiry_months"
].fillna(24)

drug_df["prescription_required"] = drug_df[
    "prescription_required"
].fillna(True)

drug_df["controlled_substance"] = drug_df[
    "controlled_substance"
].fillna(False)

drug_df["high_alert_medication"] = drug_df[
    "high_alert_medication"
].fillna(False)

# ==========================================================
# Duplicate Check
# ==========================================================

duplicate_count = drug_df.duplicated().sum()

print("\nDuplicate Records :", duplicate_count)

# ==========================================================
# Missing Value Report
# ==========================================================

print("\nMissing Values\n")

print(drug_df.isnull().sum())

# ==========================================================
# Final Preview
# ==========================================================

print("\nEnhanced Drug Preview\n")

print(drug_df.head())

print("\nFinal Columns\n")

for column in drug_df.columns:
    print(column)

print("\nFinal Shape :", drug_df.shape)

# ==========================================================
# Save Enhanced Dataset
# ==========================================================

drug_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nEnhanced Drug dataset saved successfully.")

print(f"Output File : {OUTPUT_FILE}")

print("\nDrug Enhancement Completed Successfully")