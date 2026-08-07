
# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Table Enhancement : Employee (Enterprise ETL v2.0)
# ==========================================================

import pandas as pd
import random
from datetime import datetime

INPUT_FILE = "datasets/original/employee.csv"
OUTPUT_FILE = "datasets/enhanced/employee.csv"
CURRENT_YEAR = 2026

random.seed(42)

employee_df = pd.read_csv(INPUT_FILE)

print("=" * 70)
print("EMPLOYEE ENTERPRISE ETL")
print("=" * 70)
print("Original Shape :", employee_df.shape)

ROLE_RULES = {
    "Doctor":{"age":(30,65),"min":27,"base":70000,"inc":5000,"shift":["Morning","Evening","Night"],
              "qual":["MBBS","MD","MS","DM","MCh"],
              "spec":["Cardiology","Neurology","Orthopedics","General Medicine","Pediatrics","Pulmonology","Radiology","Oncology"]},
    "Nurse":{"age":(22,60),"min":21,"base":30000,"inc":2000,"shift":["Morning","Evening","Night"],
             "qual":["GNM","B.Sc Nursing","M.Sc Nursing"],
             "spec":["ICU","Emergency","OT","Ward","NICU"]},
    "Technician":{"age":(22,58),"min":20,"base":28000,"inc":1800,"shift":["Morning","Evening"],
                  "qual":["DMLT","BMLT","MMLT"],
                  "spec":["Radiology","Laboratory","MRI","CT Scan","Blood Bank"]},
    "Pharmacist":{"age":(23,60),"min":22,"base":35000,"inc":2200,"shift":["Morning","Evening"],
                  "qual":["D.Pharm","B.Pharm","M.Pharm"],
                  "spec":["Clinical Pharmacy","Retail Pharmacy","Inventory"]},
    "Admin":{"age":(21,58),"min":18,"base":25000,"inc":1500,"shift":["General"],
             "qual":["BBA","MBA","B.Com","M.Com"],
             "spec":["HR","Finance","Operations","Procurement"]}
}

blood_groups=["A+","A-","B+","B-","AB+","AB-","O+","O-"]
relations=["Father","Mother","Spouse","Brother","Sister"]
marital=["Single","Married","Divorced"]

def get_rule(role):
    for k,v in ROLE_RULES.items():
        if k.lower() in str(role).lower():
            return k,v
    return "Admin", ROLE_RULES["Admin"]

def designation(role,exp):
    if role=="Doctor":
        return "Junior Resident" if exp<=3 else "Consultant" if exp<=8 else "Senior Consultant" if exp<=15 else "Head Consultant"
    if role=="Nurse":
        return "Staff Nurse" if exp<=3 else "Senior Nurse" if exp<=8 else "Nursing Supervisor" if exp<=15 else "Chief Nursing Officer"
    if role=="Technician":
        return "Lab Technician" if exp<=5 else "Senior Technician" if exp<=12 else "Chief Technician"
    if role=="Pharmacist":
        return "Pharmacist" if exp<=5 else "Senior Pharmacist" if exp<=12 else "Pharmacy Manager"
    return "Executive" if exp<=5 else "Senior Executive" if exp<=12 else "Manager"

phones=set()
def unique_phone():
    while True:
        p="9"+"".join(str(random.randint(0,9)) for _ in range(9))
        if p not in phones:
            phones.add(p)
            return p

rows=[]
for _,r in employee_df.iterrows():
    role_name,rule=get_rule(r["role"])
    age=random.randint(*rule["age"])
    exp=random.randint(1,max(1,age-rule["min"]))
    dob=datetime(CURRENT_YEAR-age,random.randint(1,12),random.randint(1,28))
    hire=datetime(CURRENT_YEAR-exp,random.randint(1,12),random.randint(1,28))

    parts=str(r["employee_name"]).strip().split(maxsplit=1)
    first=parts[0]
    last=parts[1] if len(parts)>1 else ""

    rows.append({
        "employee_id":r["employee_id"],
        "employee_code":f"EMP{int(r['employee_id']):06d}",
        "first_name":first,
        "last_name":last,
        "gender":r["gender"],
        "date_of_birth":dob.strftime("%Y-%m-%d"),
        "blood_group":random.choice(blood_groups),
        "marital_status":random.choice(marital),
        "role":r["role"],
        "designation":designation(role_name,exp),
        "qualification":random.choice(rule["qual"]),
        "specialization":random.choice(rule["spec"]),
        "employment_type":r["employment_type"],
        "department_id":r["department_id"],
        "reporting_manager_id":pd.NA,
        "years_of_experience":exp,
        "salary":rule["base"]+exp*rule["inc"]+random.randint(2000,10000),
        "hire_date":hire.strftime("%Y-%m-%d"),
        "shift_type":random.choice(rule["shift"]),
        "employment_status":"Active",
        "email":first.lower()+"."+last.lower().replace(" ","")+f"{int(r['employee_id'])}@apollohospital.com",
        "phone_number":unique_phone(),
        "emergency_contact_name":"Emergency Contact",
        "emergency_contact":unique_phone(),
        "emergency_contact_relation":random.choice(relations),
        "created_by":"System",
        "updated_by":"System",
        "created_date":"2023-01-01",
        "updated_date":"2025-01-01"
    })

final_df=pd.DataFrame(rows)

assert final_df.employee_id.is_unique
assert final_df.employee_code.is_unique
assert final_df.email.is_unique

final_df.to_csv(
    OUTPUT_FILE,
    index=False,
    na_rep="\\N"
)

print("Enhanced Shape:",final_df.shape)
print(final_df.head())
print("Saved:",OUTPUT_FILE)
