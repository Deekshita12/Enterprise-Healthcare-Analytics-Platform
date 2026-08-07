
# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Doctor (Enterprise Final v2.0)
# ==========================================================

import pandas as pd
import random

DOCTOR_FILE = "datasets/original/doctor.csv"
EMPLOYEE_FILE = "datasets/enhanced/employee.csv"
OUTPUT_FILE = "datasets/enhanced/doctor.csv"

doctor_df = pd.read_csv(DOCTOR_FILE)
employee_df = pd.read_csv(EMPLOYEE_FILE)

print("="*60)
print("DOCTOR TABLE AUDIT")
print("="*60)
print("Doctor Shape :", doctor_df.shape)
print("Employee Shape :", employee_df.shape)

employee_required = employee_df[
    [
        "employee_id",
        "email",
        "phone_number"
    ]
]

doctor_df = doctor_df.merge(
    employee_required,
    on="employee_id",
    how="left"
)

SPECIALIZATION_PREMIUM = {
    "Cardiology":1000,
    "Neurology":1200,
    "Orthopedics":800,
    "Pediatrics":500,
    "Radiology":700,
    "Oncology":1500,
    "Emergency Medicine":600,
    "General Medicine":300
}

ROOM_PREFIX = {
    "Cardiology":"CARD",
    "Neurology":"NEUR",
    "Orthopedics":"ORTH",
    "Pediatrics":"PED",
    "Radiology":"RAD",
    "Oncology":"ONC",
    "Emergency Medicine":"ER",
    "General Medicine":"GEN"
}

OPD_DAYS=[
    "Monday-Friday",
    "Tuesday-Saturday",
    "Monday-Wednesday-Friday",
    "Monday-Thursday",
    "Wednesday-Sunday"
]

def premium(spec):
    return SPECIALIZATION_PREMIUM.get(spec,500)

def fee(exp,spec):
    return 500 + exp*80 + premium(spec)

def license_no(doc_id):
    return f"MH-MMC-{100000+int(doc_id)}"

def room(spec,doc_id):
    return f"{ROOM_PREFIX.get(spec,'GEN')}-{100+(int(doc_id)%50)}"

def duration(spec):
    if spec in ["Cardiology","Neurology","Oncology"]:
        return 30
    elif spec in ["Orthopedics","Pediatrics","Radiology"]:
        return 20
    return 15

def max_patients(minutes):
    return {15:40,20:30,30:20}[minutes]

def status():
    return random.choices(
        ["Active","On Leave","Retired"],
        weights=[95,3,2],
        k=1
    )[0]

def availability_status(stat):
    if stat=="On Leave":
        return "On Leave"
    if stat=="Retired":
        return "Off Duty"
    return random.choice(["Available","In Surgery"])

doctor_df["license_number"] = doctor_df["doctor_id"].apply(license_no)
# Rename old column if it exists
if "experience_years" in doctor_df.columns:
    doctor_df.rename(
        columns={"experience_years": "years_of_practice"},
        inplace=True
    )

doctor_df["consultation_fee"] = doctor_df.apply(
    lambda r: fee(r["years_of_practice"], r["specialization"]),
    axis=1
)
doctor_df["consultation_room"] = doctor_df.apply(
    lambda r: room(r["specialization"],r["doctor_id"]),axis=1
)
doctor_df["opd_days"]=[random.choice(OPD_DAYS) for _ in range(len(doctor_df))]
doctor_df["consultation_start_time"]=["09:00"]*len(doctor_df)
doctor_df["consultation_end_time"]=["17:00"]*len(doctor_df)
doctor_df["max_patients_per_day"] = doctor_df[
    "consultation_duration_minutes"
].apply(max_patients)
doctor_df["doctor_status"]=[status() for _ in range(len(doctor_df))]
doctor_df["availability_status"]=doctor_df["doctor_status"].apply(availability_status)
doctor_df["created_by"] = "System"
doctor_df["updated_by"] = "System"

doctor_df["created_date"] = "2023-01-01"
doctor_df["updated_date"] = "2025-01-01"

doctor_df=doctor_df[
[

    "doctor_id",
    "employee_id",
    "specialization",
    "consultation_fee",
    "license_number",
    "years_of_practice",
    "availability_status",
    "consultation_room",
    "consultation_start_time",
    "consultation_end_time",
    "opd_days",
    "consultation_duration_minutes",
    "created_by",
    "updated_by",
    "created_date",
    "updated_date"
]
]

assert doctor_df["doctor_id"].is_unique
assert doctor_df["license_number"].is_unique
assert doctor_df["consultation_fee"].gt(0).all()
assert doctor_df["consultation_room"].notna().all()

print("\nFinal Shape:",doctor_df.shape)
print(doctor_df.head())

doctor_df.to_csv(OUTPUT_FILE,index=False)

print("\nDoctor Enhancement Completed Successfully")
print("Saved:",OUTPUT_FILE)
