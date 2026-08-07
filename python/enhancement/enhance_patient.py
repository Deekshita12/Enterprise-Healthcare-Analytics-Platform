# ==========================================================
# Enterprise Healthcare Operations Intelligence Platform
# Transaction Table Enhancement : Patient
# ==========================================================

import random
from datetime import timedelta

import numpy as np
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_FILE = "datasets/original/patient.csv"
INSURANCE_FILE = "datasets/enhanced/insurance_provider.csv"
OUTPUT_FILE = "datasets/enhanced/patient.csv"

RANDOM_SEED = 42

random.seed(RANDOM_SEED)
np.random.seed(RANDOM_SEED)

# ==========================================================
# Load Data
# ==========================================================

patient_df = pd.read_csv(INPUT_FILE)
insurance_df = pd.read_csv(INSURANCE_FILE)

print("=" * 60)
print("Enterprise Healthcare Operations Intelligence Platform")
print("Enhancing Patient Dataset")
print("=" * 60)
print(f"Original Shape : {patient_df.shape}")

# ==========================================================
# Enterprise Master Lists
# ==========================================================

FIRST_NAMES_MALE = [
    "Aarav","Vivaan","Aditya","Arjun","Vihaan","Sai",
    "Krishna","Rahul","Rohan","Karan","Akash","Amit",
    "Siddharth","Nikhil","Yash","Ritvik","Ankit","Abhishek",
    "Harsh","Varun","Raj","Aryan","Shubham","Manish"
]

FIRST_NAMES_FEMALE = [
    "Aanya","Diya","Ananya","Ishita","Sneha","Pooja",
    "Neha","Kavya","Riya","Priya","Meera","Aditi",
    "Nandini","Anjali","Khushi","Simran","Shruti",
    "Sakshi","Tanvi","Radhika","Swati","Muskan",
    "Preeti","Komal"
]

FIRST_NAMES_OTHER = [
    "Alex",
    "Jordan",
    "Taylor",
    "Robin",
    "Sam"
]

LAST_NAMES = [
    "Sharma","Patel","Reddy","Verma","Gupta",
    "Joshi","Nair","Menon","Kulkarni","Iyer",
    "Das","Kapoor","Yadav","Singh","Mishra",
    "Bose","Pandey","Chavan","Jain","Thomas",
    "Fernandes","Khan","Shetty","Pillai"
]

EMERGENCY_RELATIVES = [
    "Father",
    "Mother",
    "Brother",
    "Sister",
    "Husband",
    "Wife",
    "Guardian",
    "Son",
    "Daughter"
]

ALLERGIES = [
    "None",
    "Penicillin",
    "Peanuts",
    "Dust",
    "Seafood",
    "Latex",
    "Milk",
    "Pollen",
    "Sulfa Drugs",
    "Egg"
]

CHRONIC_CONDITIONS = [
    "None",
    "Diabetes",
    "Hypertension",
    "Asthma",
    "COPD",
    "Arthritis",
    "Thyroid Disorder",
    "Kidney Disease",
    "Heart Disease",
    "Migraine"
]

MARITAL_STATUS = [
    "Single",
    "Married",
    "Divorced",
    "Widowed"
]

PATIENT_STATUS = [
    "Active",
    "Inactive",
    "Deceased"
]

EMAIL_DOMAINS = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "hotmail.com"
]

STATES = [
    "Maharashtra",
    "Karnataka",
    "Tamil Nadu",
    "Gujarat",
    "Delhi",
    "Telangana"
]

COUNTRY = "India"

insurance_ids = insurance_df["insurance_provider_id"].tolist()
# ==========================================================
# Helper Functions
# ==========================================================

def generate_first_name(gender):
    """
    Generate first name based on gender.
    """

    gender = str(gender).strip().upper()

    if gender == "M":
        return random.choice(FIRST_NAMES_MALE)

    elif gender == "F":
        return random.choice(FIRST_NAMES_FEMALE)

    return random.choice(FIRST_NAMES_OTHER)


def generate_last_name():
    return random.choice(LAST_NAMES)


def generate_email(first_name, last_name, patient_id):
    domain = random.choice(EMAIL_DOMAINS)

    first = first_name.lower().replace(" ", "")
    last = last_name.lower().replace(" ", "")

    return f"{first}.{last}{str(patient_id)[-4:]}@{domain}"


def generate_mobile():
    return "9" + "".join(
        random.choices("0123456789", k=9)
    )


def generate_emergency_contact(first_name):
    relation = random.choice(EMERGENCY_RELATIVES)

    return (
        f"{relation} of {first_name}",
        generate_mobile()
    )


def calculate_age(dob):

    dob = pd.to_datetime(dob)

    today = pd.Timestamp.today()

    age = int(
        (today - dob).days / 365.25
    )

    return max(age, 0)


def assign_marital_status(age):

    if age < 21:
        return "Single"

    if age < 30:
        return random.choices(
            ["Single", "Married"],
            weights=[60, 40]
        )[0]

    if age < 50:
        return random.choices(
            ["Married", "Single", "Divorced"],
            weights=[70, 20, 10]
        )[0]

    return random.choices(
        ["Married", "Widowed", "Divorced"],
        weights=[70, 20, 10]
    )[0]


def assign_patient_status():

    return random.choices(
        PATIENT_STATUS,
        weights=[94, 5, 1]
    )[0]


def assign_allergies():

    return random.choices(
        ALLERGIES,
        weights=[
            55,
            8,
            7,
            6,
            5,
            5,
            4,
            4,
            3,
            3
        ]
    )[0]


def assign_chronic_condition(age):

    if age < 18:

        return random.choices(
            CHRONIC_CONDITIONS,
            weights=[
                80,
                1,
                1,
                10,
                0,
                0,
                2,
                0,
                0,
                6
            ]
        )[0]

    elif age < 40:

        return random.choices(
            CHRONIC_CONDITIONS,
            weights=[
                60,
                12,
                8,
                6,
                1,
                1,
                5,
                1,
                1,
                5
            ]
        )[0]

    elif age < 60:

        return random.choices(
            CHRONIC_CONDITIONS,
            weights=[
                35,
                22,
                20,
                4,
                3,
                4,
                5,
                2,
                3,
                2
            ]
        )[0]

    return random.choices(
        CHRONIC_CONDITIONS,
        weights=[
            20,
            25,
            25,
            3,
            5,
            6,
            5,
            4,
            5,
            2
        ]
    )[0]


def assign_insurance():

    if random.random() < 0.88:
        return random.choice(insurance_ids)

    return np.nan


def random_timestamp():

    start = pd.Timestamp("2022-01-01")

    end = pd.Timestamp("2025-12-31")

    seconds = random.randint(
        0,
        int((end - start).total_seconds())
    )

    return start + timedelta(seconds=seconds)
# ==========================================================
# Enterprise Patient Enhancement
# ==========================================================

# Normalize existing columns
patient_df.columns = patient_df.columns.str.strip().str.lower()

patient_df["gender"] = (
    patient_df["gender"]
    .astype(str)
    .str.upper()
    .replace(
        {
            "MALE": "M",
            "FEMALE": "F"
        }
    )
)

patient_df["date_of_birth"] = pd.to_datetime(
    patient_df["date_of_birth"]
)

# ==========================================================
# Generate Enterprise Attributes
# ==========================================================

first_names = []
last_names = []
emails = []
emergency_names = []
emergency_numbers = []

marital_status = []
insurance_provider = []
allergies = []
chronic_conditions = []
patient_status = []

states = []
countries = []

created_by = []
updated_by = []

created_date = []
updated_date = []

print("\nGenerating enterprise patient attributes...")

for _, row in patient_df.iterrows():

    gender = row["gender"]

    first = generate_first_name(gender)
    last = generate_last_name()

    first_names.append(first)
    last_names.append(last)

    emails.append(
        generate_email(
            first,
            last,
            row["patient_id"]
        )
    )

    emergency_name, emergency_number = generate_emergency_contact(first)

    emergency_names.append(emergency_name)
    emergency_numbers.append(emergency_number)

    age = calculate_age(
        row["date_of_birth"]
    )

    marital_status.append(
        assign_marital_status(age)
    )

    insurance_provider.append(
        assign_insurance()
    )

    allergies.append(
        assign_allergies()
    )

    chronic_conditions.append(
        assign_chronic_condition(age)
    )

    patient_status.append(
        assign_patient_status()
    )

    states.append(
        random.choice(STATES)
    )

    countries.append(
        COUNTRY
    )

    created = random_timestamp()

    updated = created + timedelta(
        days=random.randint(0, 365)
    )

    created_by.append("SYSTEM")
    updated_by.append("SYSTEM")

    created_date.append(created)
    updated_date.append(updated)

# ==========================================================
# Populate Columns
# ==========================================================

patient_df["first_name"] = first_names
patient_df["last_name"] = last_names

patient_df["state"] = states
patient_df["country"] = countries

patient_df["email"] = emails

patient_df["emergency_contact_name"] = emergency_names
patient_df["emergency_contact_number"] = emergency_numbers

patient_df["marital_status"] = marital_status

patient_df["insurance_provider_id"] = insurance_provider

patient_df["allergies"] = allergies

patient_df["chronic_conditions"] = chronic_conditions

patient_df["patient_status"] = patient_status

patient_df["created_by"] = created_by
patient_df["updated_by"] = updated_by

patient_df["created_date"] = created_date
patient_df["updated_date"] = updated_date

# ==========================================================
# Data Quality Standardization
# ==========================================================

patient_df["first_name"] = (
    patient_df["first_name"]
    .str.title()
)

patient_df["last_name"] = (
    patient_df["last_name"]
    .str.title()
)

patient_df["city"] = (
    patient_df["city"]
    .astype(str)
    .str.title()
)

patient_df["state"] = (
    patient_df["state"]
    .str.title()
)

patient_df["country"] = (
    patient_df["country"]
    .str.title()
)

patient_df["blood_group"] = (
    patient_df["blood_group"]
    .astype(str)
    .str.upper()
)

patient_df["contact_number"] = (
    patient_df["contact_number"]
    .astype(str)
    .str.replace(r"\D", "", regex=True)
)

patient_df["emergency_contact_number"] = (
    patient_df["emergency_contact_number"]
    .astype(str)
)

patient_df["email"] = (
    patient_df["email"]
    .str.lower()
)

# ==========================================================
# Final Column Order
# ==========================================================

patient_df = patient_df[
    [
        "patient_id",
        "first_name",
        "last_name",
        "gender",
        "date_of_birth",
        "blood_group",
        "city",
        "state",
        "country",
        "contact_number",
        "email",
        "emergency_contact_name",
        "emergency_contact_number",
        "marital_status",
        "insurance_provider_id",
        "allergies",
        "chronic_conditions",
        "patient_status",
        "created_by",
        "updated_by",
        "created_date",
        "updated_date"
    ]
]
# ==========================================================
# Enterprise Data Validation
# ==========================================================

print("\nValidating enhanced patient dataset...")

# Primary Key Validation
duplicate_patient_ids = patient_df["patient_id"].duplicated().sum()

# Foreign Key Validation
valid_insurance_ids = set(insurance_df["insurance_provider_id"])

invalid_insurance_ids = (
    patient_df[
        patient_df["insurance_provider_id"].notna()
        & ~patient_df["insurance_provider_id"].isin(valid_insurance_ids)
    ]
).shape[0]

# Contact Number Validation
invalid_contact_numbers = (
    patient_df["contact_number"]
    .astype(str)
    .str.fullmatch(r"\d{10}")
    .isna()
    .sum()
)

invalid_emergency_numbers = (
    patient_df["emergency_contact_number"]
    .astype(str)
    .str.fullmatch(r"\d{10}")
    .isna()
    .sum()
)

# Email Validation
invalid_emails = (
    patient_df["email"]
    .str.contains("@", regex=False)
    .eq(False)
    .sum()
)

# Null Check
null_summary = patient_df.isnull().sum()

# ==========================================================
# Export
# ==========================================================

patient_df.to_csv(
    OUTPUT_FILE,
    index=False
)

# ==========================================================
# Audit Summary
# ==========================================================

print("\n" + "=" * 60)
print("PATIENT DATASET ENHANCEMENT SUMMARY")
print("=" * 60)

print(f"Original Shape              : {pd.read_csv(INPUT_FILE).shape}")
print(f"Enhanced Shape              : {patient_df.shape}")

print("\nValidation Results")

print(f"Duplicate Patient IDs       : {duplicate_patient_ids}")
print(f"Invalid Insurance IDs       : {invalid_insurance_ids}")
print(f"Invalid Contact Numbers     : {invalid_contact_numbers}")
print(f"Invalid Emergency Numbers   : {invalid_emergency_numbers}")
print(f"Invalid Emails              : {invalid_emails}")

print("\nNull Values")

print(null_summary)

print("\nOutput File")

print(OUTPUT_FILE)

print("\nPatient enhancement completed successfully.")

print("=" * 60)