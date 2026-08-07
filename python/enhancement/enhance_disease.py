# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Disease
# ==========================================================

import pandas as pd

INPUT_FILE = "datasets/original/disease.csv"
OUTPUT_FILE = "datasets/enhanced/disease.csv"

disease_df = pd.read_csv(INPUT_FILE)

print("="*60)
print("DISEASE TABLE AUDIT")
print("="*60)

print("\nShape :", disease_df.shape)

print("\nColumns")
print(disease_df.columns.tolist())

# ----------------------------------------------------------
# Disease Lookup
# ----------------------------------------------------------

severity_lookup = {
    "Cardiac": "Critical",
    "Neurological": "High",
    "Trauma": "Critical",
    "Infectious": "High",
    "Respiratory": "High",
    "Endocrine": "Medium",
    "Renal": "High",
    "Hematological": "Medium",
    "Orthopedic": "Medium",
    "Surgical": "Medium",
    "Pediatric": "Low"
}

# ----------------------------------------------------------
# Helper Functions
# ----------------------------------------------------------

def severity(category):

    return severity_lookup.get(category,"Medium")


def contagious(category):

    return category == "Infectious"


def chronic(category):

    return category in [
        "Cardiovascular",
        "Neurological",
        "Oncology"
    ]


def los(category):

    mapping = {

        "Cardiac": 8,
        "Neurological": 10,
        "Trauma": 12,
        "Infectious": 7,
        "Respiratory": 6,
        "Endocrine": 4,
        "Renal": 8,
        "Hematological": 5,
        "Orthopedic": 6,
        "Surgical": 5,
        "Pediatric": 4

    }

    return mapping.get(category,5)


def mortality(category):

    mapping = {

        "Cardiac": "High",
        "Neurological": "High",
        "Trauma": "Critical",
        "Infectious": "Medium",
        "Respiratory": "Medium",
        "Endocrine": "Low",
        "Renal": "Medium",
        "Hematological": "Medium",
        "Orthopedic": "Low",
        "Surgical": "Low",
        "Pediatric": "Low"
}


    return mapping.get(category,"Low")

# ----------------------------------------------------------
# Add Enterprise Columns
# ----------------------------------------------------------

disease_df["severity_level"] = disease_df["disease_category"].apply(severity)

disease_df["contagious"] = disease_df["disease_category"].apply(contagious)

disease_df["chronic"] = disease_df["disease_category"].apply(chronic)

disease_df["average_los_days"] = disease_df["disease_category"].apply(los)

disease_df["mortality_risk"] = disease_df["disease_category"].apply(mortality)
priority_lookup = {
    "Critical": "Immediate",
    "High": "Urgent",
    "Medium": "Routine",
    "Low": "Routine"
}

disease_df["treatment_priority"] = disease_df["severity_level"].map(priority_lookup)

disease_df["follow_up_required"] = disease_df["chronic"]

disease_df["readmission_risk"] = disease_df["severity_level"].map({
    "Critical": "High",
    "High": "High",
    "Medium": "Medium",
    "Low": "Low"
})

disease_df["created_date"] = "2023-01-01"

disease_df["updated_date"] = "2025-01-01"

print("\nPreview\n")

print(disease_df.head())

print("\nMissing Values\n")

print(disease_df.isnull().sum())

disease_df = disease_df[
    [
        "disease_id",
        "disease_name",
        "disease_category",
        "severity_level",
        "contagious",
        "chronic",
        "average_los_days",
        "mortality_risk",
        "treatment_priority",
        "follow_up_required",
        "readmission_risk",
        "created_date",
        "updated_date"
    ]
]

disease_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nDisease Enhancement Completed Successfully")

print("\nFinal Shape :",disease_df.shape)