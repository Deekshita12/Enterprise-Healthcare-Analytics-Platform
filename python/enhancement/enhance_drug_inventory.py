# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Drug Inventory
# Part 1
# ==========================================================

import pandas as pd
import random
from datetime import datetime, timedelta

INPUT_FILE = "datasets/original/drug_inventory.csv"
OUTPUT_FILE = "datasets/enhanced/drug_inventory.csv"

inventory_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("DRUG INVENTORY TABLE AUDIT")
print("=" * 70)

print("\nShape :", inventory_df.shape)

print("\nColumns")
print(inventory_df.columns.tolist())

print("\nDuplicate Records :", inventory_df.duplicated().sum())

# ==========================================================
# Lookup Lists
# ==========================================================

warehouse_lookup = [
    "Central Pharmacy",
    "Emergency Pharmacy",
    "ICU Pharmacy",
    "Warehouse A",
    "Warehouse B"
]

storage_lookup = [
    "Ambient Storage",
    "Cold Storage (2-8°C)",
    "Controlled Drug Room"
]

inspection_status_lookup = [
    "Pending",
    "Completed"
]

# ==========================================================
# Helper Functions
# ==========================================================

def generate_warehouse():
    return random.choice(warehouse_lookup)


def generate_storage():
    return random.choice(storage_lookup)


def generate_batch():
    return f"BT-{random.randint(100000,999999)}"


def generate_supplier_lead_time():
    return random.randint(3, 14)


def generate_expiry_date():

    start = datetime(2026, 1, 1)
    end = datetime(2028, 12, 31)

    random_days = random.randint(
        0,
        (end - start).days
    )

    return (
        start + timedelta(days=random_days)
    ).strftime("%Y-%m-%d")


def calculate_reorder_quantity(stock, reorder):

    if stock <= reorder:
        return reorder * 2

    return 0


def calculate_safety_stock(reorder):

    return max(
        int(reorder * 0.50),
        10
    )


def calculate_maximum_stock(reorder):

    return reorder * 4


def generate_next_inspection():

    return (
        datetime.today()
        + timedelta(days=random.randint(15, 60))
    ).strftime("%Y-%m-%d")


# ==========================================================
# Enterprise Columns
# ==========================================================

inventory_df["warehouse_location"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_warehouse()
)

inventory_df["storage_zone"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_storage()
)

inventory_df["batch_number"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_batch()
)

inventory_df["supplier_lead_time_days"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_supplier_lead_time()
)

inventory_df["expiry_date"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_expiry_date()
)

inventory_df["reorder_quantity"] = inventory_df.apply(
    lambda row: calculate_reorder_quantity(
        row["current_stock"],
        row["reorder_level"]
    ),
    axis=1
)

inventory_df["safety_stock"] = inventory_df[
    "reorder_level"
].apply(
    calculate_safety_stock
)

inventory_df["maximum_stock"] = inventory_df[
    "reorder_level"
].apply(
    calculate_maximum_stock
)

inventory_df["reorder_point"] = inventory_df[
    "reorder_level"
]

inventory_df["next_inspection_date"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: generate_next_inspection()
)

inventory_df["inspection_status"] = inventory_df[
    "inventory_id"
].apply(
    lambda x: random.choice(
        inspection_status_lookup
    )
)

inventory_df["created_by"] = "System"

inventory_df["updated_by"] = "System"

inventory_df["created_date"] = "2023-01-01"

inventory_df["updated_date"] = "2025-01-01"
# ==========================================================
# Data Quality Checks
# ==========================================================

inventory_df["warehouse_location"] = inventory_df[
    "warehouse_location"
].fillna("Central Pharmacy")

inventory_df["storage_zone"] = inventory_df[
    "storage_zone"
].fillna("Ambient Storage")

inventory_df["batch_number"] = inventory_df[
    "batch_number"
].fillna("UNKNOWN")

inventory_df["supplier_lead_time_days"] = inventory_df[
    "supplier_lead_time_days"
].fillna(7)

inventory_df["expiry_date"] = inventory_df[
    "expiry_date"
].fillna("2027-12-31")

inventory_df["reorder_quantity"] = inventory_df[
    "reorder_quantity"
].fillna(0)

inventory_df["safety_stock"] = inventory_df[
    "safety_stock"
].fillna(0)

inventory_df["maximum_stock"] = inventory_df[
    "maximum_stock"
].fillna(0)

inventory_df["reorder_point"] = inventory_df[
    "reorder_point"
].fillna(0)

inventory_df["next_inspection_date"] = inventory_df[
    "next_inspection_date"
].fillna("2026-12-31")

inventory_df["inspection_status"] = inventory_df[
    "inspection_status"
].fillna("Pending")

inventory_df["created_by"] = inventory_df[
    "created_by"
].fillna("System")

inventory_df["updated_by"] = inventory_df[
    "updated_by"
].fillna("System")

inventory_df["created_date"] = inventory_df[
    "created_date"
].fillna("2023-01-01")

inventory_df["updated_date"] = inventory_df[
    "updated_date"
].fillna("2025-01-01")

# ==========================================================
# Data Type Standardization
# ==========================================================

inventory_df["current_stock"] = inventory_df[
    "current_stock"
].astype(int)

inventory_df["reorder_level"] = inventory_df[
    "reorder_level"
].astype(int)

inventory_df["reorder_quantity"] = inventory_df[
    "reorder_quantity"
].astype(int)

inventory_df["safety_stock"] = inventory_df[
    "safety_stock"
].astype(int)

inventory_df["maximum_stock"] = inventory_df[
    "maximum_stock"
].astype(int)

inventory_df["supplier_lead_time_days"] = inventory_df[
    "supplier_lead_time_days"
].astype(int)

# ==========================================================
# Duplicate Check
# ==========================================================

duplicate_count = inventory_df.duplicated().sum()

print("\nDuplicate Records :", duplicate_count)

# ==========================================================
# Missing Values Report
# ==========================================================

print("\nMissing Values\n")

print(inventory_df.isnull().sum())

# ==========================================================
# Preview
# ==========================================================

print("\nEnhanced Drug Inventory Preview\n")

print(inventory_df.head())

# ==========================================================
# Final Columns
# ==========================================================

print("\nFinal Columns\n")

for column in inventory_df.columns:
    print(column)

# ==========================================================
# Final Shape
# ==========================================================

print("\nFinal Shape :", inventory_df.shape)

# ==========================================================
# Save Enhanced Dataset
# ==========================================================

inventory_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nEnhanced Drug Inventory dataset saved successfully.")

print(f"Output File : {OUTPUT_FILE}")

print("\nDrug Inventory Enhancement Completed Successfully")