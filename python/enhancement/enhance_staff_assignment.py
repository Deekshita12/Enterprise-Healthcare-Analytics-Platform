# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Staff Assignment
# ==========================================================

import random
from datetime import timedelta

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/staff_assignment.csv"

EMPLOYEE_FILE = "datasets/enhanced/employee.csv"
DEPARTMENT_FILE = "datasets/enhanced/department.csv"
WARD_FILE = "datasets/enhanced/ward.csv"
ADMISSION_FILE = "datasets/enhanced/admission.csv"

OUTPUT_FILE = "datasets/enhanced/staff_assignment.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

staff_df = pd.read_csv(INPUT_FILE)

employee_df = pd.read_csv(EMPLOYEE_FILE)
department_df = pd.read_csv(DEPARTMENT_FILE)
ward_df = pd.read_csv(WARD_FILE)
admission_df = pd.read_csv(ADMISSION_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Staff Assignment Dataset")
print("=" * 60)

print(f"Original Shape : {staff_df.shape}")

# ==========================================================
# Standardize Columns
# ==========================================================

for df in [
    staff_df,
    employee_df,
    department_df,
    ward_df,
    admission_df
]:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

# Legacy compatibility

if "staff_id" in employee_df.columns:
    employee_df.rename(
        columns={
            "staff_id":"employee_id"
        },
        inplace=True
    )

if "shift" in staff_df.columns:
    staff_df.rename(
        columns={
            "shift":"shift_type"
        },
        inplace=True
    )

SYSTEM_USER = "System"

print("\nGenerating enterprise staff assignment attributes...")
# ==========================================================
# Department Assignment
# ==========================================================

staff_df["department_id"] = np.random.choice(
    department_df["department_id"],
    len(staff_df)
)

# ==========================================================
# Admission Assignment
# ==========================================================

staff_df["admission_id"] = np.random.choice(
    admission_df["admission_id"],
    len(staff_df)
)

# ==========================================================
# Assignment Date
# ==========================================================

start_date = pd.Timestamp("2023-01-01")
end_date = pd.Timestamp("2025-12-31")

days = np.random.randint(
    0,
    (end_date - start_date).days,
    len(staff_df)
)

staff_df["assignment_date"] = (
    start_date +
    pd.to_timedelta(days, unit="D")
)

# ==========================================================
# Shift Timing
# ==========================================================

shift_times = {

    "Morning": ("07:00:00","15:00:00"),
    "Evening": ("15:00:00","23:00:00"),
    "Night": ("23:00:00","07:00:00")

}

staff_df["shift_type"] = (
    staff_df["shift_type"]
    .str.title()
)

staff_df["shift_start_time"] = (
    staff_df["shift_type"]
    .map(lambda x: shift_times.get(x, ("08:00:00","16:00:00"))[0])
)

staff_df["shift_end_time"] = (
    staff_df["shift_type"]
    .map(lambda x: shift_times.get(x, ("08:00:00","16:00:00"))[1])
)

# ==========================================================
# Assignment Role
# ==========================================================

staff_df["assignment_role"] = np.random.choice(

    [
        "Staff Nurse",
        "Ward Assistant",
        "Emergency Technician",
        "Lab Technician",
        "Pharmacist",
        "Reception Executive"
    ],

    len(staff_df),

    p=[
        0.34,
        0.18,
        0.10,
        0.12,
        0.12,
        0.14
    ]

)

# ==========================================================
# Assignment Status
# ==========================================================

staff_df["assignment_status"] = np.random.choice(

    [
        "Active",
        "Completed",
        "Cancelled"
    ],

    len(staff_df),

    p=[
        0.74,
        0.22,
        0.04
    ]

)

# ==========================================================
# Supervisor
# ==========================================================

staff_df["supervisor_id"] = np.random.choice(
    employee_df["employee_id"],
    len(staff_df)
)

# ==========================================================
# Remarks
# ==========================================================

staff_df["remarks"] = np.random.choice(

    [
        "System Generated",
        "Shift Completed",
        "On Duty",
        "Emergency Coverage",
        "Temporary Assignment"
    ],

    len(staff_df)

)

# ==========================================================
# Audit Columns
# ==========================================================

staff_df["created_by"] = SYSTEM_USER
staff_df["updated_by"] = SYSTEM_USER

staff_df["created_date"] = (
    staff_df["assignment_date"].dt.date
)

staff_df["updated_date"] = (
    staff_df["assignment_date"] +
    pd.to_timedelta(
        np.random.randint(
            0,
            7,
            len(staff_df)
        ),
        unit="D"
    )
).dt.date
# ==========================================================
# Final Column Order
# ==========================================================

staff_df = staff_df[
    [
        "assignment_id",
        "employee_id",
        "department_id",
        "ward_id",
        "admission_id",
        "assignment_date",
        "shift_type",
        "shift_start_time",
        "shift_end_time",
        "assignment_role",
        "assignment_status",
        "supervisor_id",
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

print("\nValidating enhanced staff assignment dataset...")

duplicate_ids = staff_df["assignment_id"].duplicated().sum()

invalid_employee = (
    ~staff_df["employee_id"].isin(employee_df["employee_id"])
).sum()

invalid_department = (
    ~staff_df["department_id"].isin(department_df["department_id"])
).sum()

invalid_ward = (
    ~staff_df["ward_id"].isin(ward_df["ward_id"])
).sum()

invalid_admission = (
    ~staff_df["admission_id"].isin(admission_df["admission_id"])
).sum()

null_summary = staff_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

staff_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 65)
print("STAFF ASSIGNMENT DATASET ENHANCEMENT SUMMARY")
print("=" * 65)

print(f"Original Shape : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape : {staff_df.shape}")

print(f"\nDuplicate Assignment IDs : {duplicate_ids}")
print(f"Invalid Employee IDs     : {invalid_employee}")
print(f"Invalid Department IDs   : {invalid_department}")
print(f"Invalid Ward IDs         : {invalid_ward}")
print(f"Invalid Admission IDs    : {invalid_admission}")

print("\nNull Summary")
print(null_summary)

print("\nOutput File")
print(OUTPUT_FILE)

print("\nStaff Assignment enhancement completed successfully.")
print("=" * 65)