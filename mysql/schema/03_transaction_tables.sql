-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- Transaction Tables
-- ==========================================================

USE hospital_analytics;
-- ==========================================================
-- TRANSACTION TABLE : PATIENT
-- ==========================================================

CREATE TABLE patient (

    patient_id INT PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    gender VARCHAR(20)
        CHECK (gender IN ('Male','Female','Other')),

    date_of_birth DATE NOT NULL,

    blood_group VARCHAR(10),

    city VARCHAR(100),

    state VARCHAR(100),

    country VARCHAR(100),

    contact_number VARCHAR(20),

    email VARCHAR(150),

    emergency_contact_name VARCHAR(100),

    emergency_contact_number VARCHAR(20),

    marital_status VARCHAR(30),

    insurance_provider_id INT,

    allergies VARCHAR(255),

    chronic_conditions VARCHAR(255),

    patient_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : ADMISSION
-- ==========================================================

CREATE TABLE admission (

    admission_id INT PRIMARY KEY,

    patient_id INT NOT NULL,

    admission_date DATE NOT NULL,

    discharge_date DATE,

    admission_type VARCHAR(50) NOT NULL,

    admission_status VARCHAR(30) NOT NULL,

    department_id INT NOT NULL,

    ward_id INT NOT NULL,

    bed_id INT NOT NULL,

    disease_id INT NOT NULL,

    admitting_doctor_id INT,

    discharge_doctor_id INT,

    admission_source VARCHAR(50),

    referral_source VARCHAR(100),

    expected_length_of_stay INT
        CHECK (expected_length_of_stay >= 0),

    actual_length_of_stay INT
        CHECK (actual_length_of_stay >= 0),

    discharge_disposition VARCHAR(100),

    admission_priority VARCHAR(30),

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);  
-- ==========================================================
-- TRANSACTION TABLE : BILLING
-- ==========================================================

CREATE TABLE billing (

    bill_id INT PRIMARY KEY,

    admission_id INT NOT NULL,

    bill_date DATE NOT NULL,

    total_amount DECIMAL(12,2) NOT NULL
        CHECK (total_amount >= 0),

    insurance_covered_amount DECIMAL(12,2)
        CHECK (insurance_covered_amount >= 0),

    patient_payable_amount DECIMAL(12,2)
        CHECK (patient_payable_amount >= 0),

    payment_status VARCHAR(30) NOT NULL,

    payment_mode VARCHAR(30),

    discount_amount DECIMAL(12,2)
        DEFAULT 0
        CHECK (discount_amount >= 0),

    tax_amount DECIMAL(12,2)
        DEFAULT 0
        CHECK (tax_amount >= 0),

    bill_status VARCHAR(30) NOT NULL DEFAULT 'Generated',

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : BILLING DETAIL
-- ==========================================================

CREATE TABLE billing_detail (

    billing_detail_id INT PRIMARY KEY,

    bill_id INT NOT NULL,

    service_type VARCHAR(50) NOT NULL,

    service_description VARCHAR(255),

    quantity INT NOT NULL
        CHECK (quantity > 0),

    unit_price DECIMAL(12,2) NOT NULL
        CHECK (unit_price >= 0),

    total_price DECIMAL(12,2) NOT NULL
        CHECK (total_price >= 0),

    service_date DATE NOT NULL,

    department_id INT,

    doctor_id INT,

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : PATIENT DIAGNOSTIC
-- ==========================================================

CREATE TABLE patient_diagnostic (

    patient_diagnostic_id INT PRIMARY KEY,

    patient_id INT NOT NULL,

    admission_id INT NOT NULL,

    diagnostic_test_id INT NOT NULL,

    doctor_id INT NOT NULL,

    test_date DATE NOT NULL,

    sample_collection_date DATE,

    report_date DATE,

    test_status VARCHAR(30) NOT NULL,

    test_result VARCHAR(100),

    result_summary VARCHAR(500),

    critical_result BOOLEAN NOT NULL DEFAULT FALSE,

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : PATIENT INSURANCE
-- ==========================================================

CREATE TABLE patient_insurance (

    patient_insurance_id INT PRIMARY KEY,

    patient_id INT NOT NULL,

    insurance_provider_id INT NOT NULL,

    policy_number VARCHAR(100) NOT NULL UNIQUE,

    policy_holder_name VARCHAR(150) NOT NULL,

    relationship_with_holder VARCHAR(50),

    policy_start_date DATE NOT NULL,

    policy_end_date DATE NOT NULL,

    coverage_amount DECIMAL(15,2)
        CHECK (coverage_amount >= 0),

    remaining_coverage DECIMAL(15,2)
        CHECK (remaining_coverage >= 0),

    insurance_status VARCHAR(30) NOT NULL,

    cashless_eligible BOOLEAN NOT NULL DEFAULT FALSE,

    pre_authorization_number VARCHAR(100),

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : PRESCRIPTION
-- ==========================================================

CREATE TABLE prescription (

    prescription_id INT PRIMARY KEY,

    patient_id INT NOT NULL,

    admission_id INT,

    doctor_id INT NOT NULL,

    drug_id INT NOT NULL,

    prescription_date DATE NOT NULL,

    dosage VARCHAR(100) NOT NULL,

    frequency VARCHAR(100) NOT NULL,

    duration_days INT
        CHECK (duration_days > 0),

    quantity INT
        CHECK (quantity > 0),

    route_of_administration VARCHAR(50),

    instructions VARCHAR(500),

    prescription_status VARCHAR(30) NOT NULL,

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- TRANSACTION TABLE : STAFF ASSIGNMENT
-- ==========================================================

CREATE TABLE staff_assignment (

    assignment_id INT PRIMARY KEY,

    employee_id INT NOT NULL,

    department_id INT NOT NULL,

    ward_id INT,

    admission_id INT,

    assignment_date DATE NOT NULL,

    shift_type VARCHAR(30) NOT NULL,

    shift_start_time TIME NOT NULL,

    shift_end_time TIME NOT NULL,

    assignment_role VARCHAR(100) NOT NULL,

    assignment_status VARCHAR(30) NOT NULL,

    supervisor_id INT,

    remarks VARCHAR(500),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
SHOW tables;