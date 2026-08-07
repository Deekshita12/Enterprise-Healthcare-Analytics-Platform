# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Diagnostic Test
# ==========================================================

import pandas as pd
import numpy as np

INPUT_FILE = "datasets/original/diagnostic_test.csv"
OUTPUT_FILE = "datasets/enhanced/diagnostic_test.csv"

diagnostic_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("DIAGNOSTIC TEST TABLE AUDIT")
print("=" * 70)

print("\nShape :", diagnostic_df.shape)

print("\nColumns")
print(diagnostic_df.columns.tolist())

print("\nTest Categories")
print(diagnostic_df["test_category"].unique())

# ==========================================================
# Lookup Dictionaries
# ==========================================================

test_code_lookup = {
    "Complete Blood Count": "LAB001",
    "Liver Function Test": "LAB002",
    "Urine Routine": "LAB003",
    "X-Ray Chest": "RAD001",
    "CT Scan Brain": "RAD002",
    "MRI Spine": "RAD003",
    "Ultrasound Abdomen": "RAD004",
    "ECG": "CAR001",
    "Biopsy": "PAT001"
}

department_lookup = {
    "Blood Test": 8,
    "Urine Test": 8,
    "Pathology": 8,
    "Radiology": 5,
    "Imaging": 5,
    "Cardiology": 6
}

duration_lookup = {
    "Blood Test": 30,
    "Urine Test": 20,
    "Imaging": 60,
    "Radiology": 45,
    "Cardiology": 40,
    "Pathology": 30
}

fasting_lookup = {
    "Blood Test": True,
    "Urine Test": False,
    "Imaging": False,
    "Radiology": False,
    "Cardiology": False,
    "Pathology": False
}

report_lookup = {
    "Blood Test": 12,
    "Urine Test": 8,
    "Imaging": 24,
    "Radiology": 24,
    "Cardiology": 12,
    "Pathology": 24
}

critical_lookup = {
    "Blood Test": False,
    "Urine Test": False,
    "Imaging": True,
    "Radiology": True,
    "Cardiology": True,
    "Pathology": False
}

lab_lookup = {
    "Blood Test": "Pathology Laboratory",
    "Urine Test": "Pathology Laboratory",
    "Pathology": "Pathology Laboratory",
    "Radiology": "Radiology Department",
    "Imaging": "Radiology Department",
    "Cardiology": "Cardiology Department"
}

sample_lookup = {
    "Blood Test": "Blood",
    "Urine Test": "Urine",
    "Pathology": "Tissue",
    "Radiology": "Imaging",
    "Imaging": "Imaging",
    "Cardiology": "ECG"
}

equipment_lookup = {
    "Complete Blood Count": "Hematology Analyzer",
    "Liver Function Test": "Biochemistry Analyzer",
    "Urine Routine": "Urine Analyzer",
    "X-Ray Chest": "Digital X-Ray Machine",
    "CT Scan Brain": "CT Scanner",
    "MRI Spine": "MRI Scanner",
    "Ultrasound Abdomen": "Ultrasound Machine",
    "ECG": "ECG Machine",
    "Biopsy": "Histopathology Workstation"
}

cost_lookup = {
    "Complete Blood Count": 500,
    "Liver Function Test": 900,
    "Urine Routine": 300,
    "X-Ray Chest": 1200,
    "CT Scan Brain": 4500,
    "MRI Spine": 7000,
    "Ultrasound Abdomen": 2500,
    "ECG": 700,
    "Biopsy": 5000
}

appointment_lookup = {
    "Blood Test": False,
    "Urine Test": False,
    "Pathology": True,
    "Radiology": True,
    "Imaging": True,
    "Cardiology": True
}

technician_lookup = {
    "Blood Test": "Lab Technician",
    "Urine Test": "Lab Technician",
    "Pathology": "Pathologist",
    "Radiology": "Radiology Technician",
    "Imaging": "Radiology Technician",
    "Cardiology": "Cardiac Technician"
}

risk_lookup = {
    "Blood Test": "Low",
    "Urine Test": "Low",
    "Pathology": "High",
    "Radiology": "Medium",
    "Imaging": "Medium",
    "Cardiology": "High"
}

prep_lookup = {
    "Blood Test": "8-hour fasting if required",
    "Urine Test": "Morning sample preferred",
    "Pathology": "As advised by physician",
    "Radiology": "Follow technician instructions",
    "Imaging": "Remove all metallic objects",
    "Cardiology": "Avoid caffeine before test"
}

report_format_lookup = {
    "Blood Test": "Digital PDF",
    "Urine Test": "Digital PDF",
    "Pathology": "Digital PDF",
    "Radiology": "DICOM + PDF",
    "Imaging": "DICOM + PDF",
    "Cardiology": "Digital ECG Report"
}

home_collection_lookup = {
    "Blood Test": True,
    "Urine Test": True,
    "Pathology": False,
    "Radiology": False,
    "Imaging": False,
    "Cardiology": False
}

repeat_lookup = {
    "Blood Test": 30,
    "Urine Test": 15,
    "Pathology": 180,
    "Radiology": 90,
    "Imaging": 90,
    "Cardiology": 30
}

# ==========================================================
# Helper Function
# ==========================================================

def lookup(dictionary, value, default):
    return dictionary.get(value, default)

# ==========================================================
# Enterprise Columns
# ==========================================================

diagnostic_df["test_code"] = diagnostic_df["test_name"].apply(
    lambda x: lookup(test_code_lookup, x, "LAB999")
)


diagnostic_df["average_duration_minutes"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(duration_lookup, x, 30)
)

diagnostic_df["requires_fasting"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(fasting_lookup, x, False)
)

diagnostic_df["report_delivery_hours"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(report_lookup, x, 24)
)

diagnostic_df["critical_test"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(critical_lookup, x, False)
)

diagnostic_df["laboratory_department"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(lab_lookup, x, "General Laboratory")
)

diagnostic_df["sample_type"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(sample_lookup, x, "General")
)

diagnostic_df["equipment_required"] = diagnostic_df["test_name"].apply(
    lambda x: lookup(equipment_lookup, x, "General Equipment")
)

diagnostic_df["requires_appointment"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(appointment_lookup, x, False)
)

diagnostic_df["technician_required"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(technician_lookup, x, "Lab Technician")
)

diagnostic_df["risk_level"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(risk_lookup, x, "Low")
)

diagnostic_df["normal_turnaround_sla"] = np.where(
    diagnostic_df["report_delivery_hours"] <= 12,
    "Same Day",
    "Next Day"
)

diagnostic_df["preparation_instructions"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(prep_lookup, x, "No preparation required")
)

diagnostic_df["report_format"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(report_format_lookup, x, "Digital PDF")
)

diagnostic_df["home_collection_available"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(home_collection_lookup, x, False)
)

diagnostic_df["repeat_interval_days"] = diagnostic_df["test_category"].apply(
    lambda x: lookup(repeat_lookup, x, 30)
)

diagnostic_df["test_priority"] = diagnostic_df["critical_test"].map(
    {
        True: "High",
        False: "Normal"
    }
)

# ==========================================================
# Enterprise Administrative Columns
# ==========================================================

diagnostic_df["active_flag"] = True

diagnostic_df["test_status"] = "Active"

diagnostic_df["accreditation_required"] = "NABH"

diagnostic_df["display_order"] = range(
    1,
    len(diagnostic_df) + 1
)

diagnostic_df["created_by"] = "System"

diagnostic_df["updated_by"] = "System"

diagnostic_df["created_date"] = "2023-01-01"

diagnostic_df["updated_date"] = "2025-01-01"

# ==========================================================
# Data Quality Checks
# ==========================================================

diagnostic_df["test_name"] = diagnostic_df["test_name"].astype(str).str.strip()

diagnostic_df["test_category"] = diagnostic_df["test_category"].astype(str).str.strip()

diagnostic_df["equipment_required"] = diagnostic_df["equipment_required"].fillna(
    "General Equipment"
)

diagnostic_df["laboratory_department"] = diagnostic_df[
    "laboratory_department"
].fillna("General Laboratory")

diagnostic_df["sample_type"] = diagnostic_df["sample_type"].fillna(
    "General"
)

diagnostic_df["technician_required"] = diagnostic_df[
    "technician_required"
].fillna("Lab Technician")

diagnostic_df["report_format"] = diagnostic_df["report_format"].fillna(
    "Digital PDF"
)

diagnostic_df["risk_level"] = diagnostic_df["risk_level"].fillna(
    "Low"
)

diagnostic_df["preparation_instructions"] = diagnostic_df[
    "preparation_instructions"
].fillna("No preparation required")

diagnostic_df["repeat_interval_days"] = diagnostic_df[
    "repeat_interval_days"
].fillna(30)

# ==========================================================
# Duplicate Check
# ==========================================================

duplicate_count = diagnostic_df.duplicated().sum()

print("\nDuplicate Records :", duplicate_count)

# ==========================================================
# Missing Value Report
# ==========================================================

print("\nMissing Values")

print(diagnostic_df.isnull().sum())

# ==========================================================
# Final Preview
# ==========================================================

print("\nEnhanced Diagnostic Test Preview\n")

print(diagnostic_df.head())

print("\nFinal Columns\n")

for column in diagnostic_df.columns:
    print(column)

print("\nFinal Shape :", diagnostic_df.shape)

# ==========================================================
# Save Enhanced Dataset
# ==========================================================

diagnostic_df.to_csv(
    OUTPUT_FILE,
    index=False
)

print("\nEnhanced Diagnostic Test dataset saved successfully.")

print(f"Output File : {OUTPUT_FILE}")

print("\nDiagnostic Test Enhancement Completed Successfully")