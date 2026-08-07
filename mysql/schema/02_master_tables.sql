 -- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- Master Tables
-- ==========================================================

USE hospital_analytics;
-- ==========================================================
-- MASTER TABLE : DEPARTMENT
-- ==========================================================

CREATE TABLE department (

    department_id INT PRIMARY KEY,

    department_name VARCHAR(100) NOT NULL,

    department_code VARCHAR(20) NOT NULL UNIQUE,

    building_wing VARCHAR(50) NOT NULL,

    operating_hours VARCHAR(100) NOT NULL,

    is_24x7 BOOLEAN NOT NULL,

    capacity_per_day INT NOT NULL
        CHECK (capacity_per_day > 0),

    head_doctor_id INT,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : EMPLOYEE
-- ==========================================================

CREATE TABLE employee (

    employee_id INT PRIMARY KEY,

    first_name VARCHAR(50) NOT NULL,

    last_name VARCHAR(50) NOT NULL,

    gender VARCHAR(20)
        CHECK (gender IN ('Male','Female','Other')),

    date_of_birth DATE NOT NULL,

    phone_number VARCHAR(20) UNIQUE,

    email VARCHAR(150) UNIQUE,

    department_id INT NOT NULL,

    designation VARCHAR(100) NOT NULL,

    qualification VARCHAR(100),

    years_of_experience INT
        CHECK (years_of_experience >= 0),

    salary DECIMAL(12,2)
        CHECK (salary >= 0),

    hire_date DATE NOT NULL,

    employment_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DOCTOR
-- ==========================================================

CREATE TABLE doctor (

    doctor_id INT PRIMARY KEY,

    employee_id INT NOT NULL,

    specialization VARCHAR(100) NOT NULL,

    consultation_fee DECIMAL(10,2)
        CHECK (consultation_fee >= 0),

    license_number VARCHAR(50) NOT NULL UNIQUE,

    years_of_practice INT
        CHECK (years_of_practice >= 0),

    availability_status VARCHAR(30) NOT NULL,

    consultation_room VARCHAR(30),

    consultation_start_time TIME,

    consultation_end_time TIME,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);

-- ==========================================================
-- MASTER TABLE : WARD
-- ==========================================================

CREATE TABLE ward (

    ward_id INT PRIMARY KEY,

    ward_name VARCHAR(100) NOT NULL,

    ward_type VARCHAR(50) NOT NULL,

    capacity INT NOT NULL
        CHECK (capacity > 0),

    department_id INT NOT NULL,

    ward_status VARCHAR(30) NOT NULL,

    floor_number INT NOT NULL,

    nurse_station VARCHAR(100),

    occupancy_target DECIMAL(5,2)
        CHECK (occupancy_target BETWEEN 0 AND 100),

    isolation_capability BOOLEAN NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : BED
-- ==========================================================

CREATE TABLE bed (

    bed_id INT PRIMARY KEY,

    bed_number VARCHAR(20) NOT NULL UNIQUE,

    ward_id INT NOT NULL,

    bed_type VARCHAR(50) NOT NULL,

    bed_status VARCHAR(30) NOT NULL,

    room_number VARCHAR(20) NOT NULL,

    floor_number INT NOT NULL,

    daily_bed_charge DECIMAL(10,2)
        CHECK (daily_bed_charge >= 0),

    oxygen_supported BOOLEAN NOT NULL,

    ventilator_supported BOOLEAN NOT NULL,

    maintenance_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DISEASE
-- ==========================================================

CREATE TABLE disease (

    disease_id INT PRIMARY KEY,

    disease_name VARCHAR(150) NOT NULL,

    disease_category VARCHAR(100) NOT NULL,

    icd10_code VARCHAR(20) NOT NULL UNIQUE,

    severity_level VARCHAR(20) NOT NULL,

    average_los_days INT NOT NULL
        CHECK (average_los_days >= 0),

    mortality_risk DECIMAL(5,2)
        CHECK (mortality_risk BETWEEN 0 AND 100),

    contagious BOOLEAN NOT NULL,

    treatment_protocol VARCHAR(255),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DIAGNOSTIC TEST
-- ==========================================================

CREATE TABLE diagnostic_test (

    diagnostic_test_id INT PRIMARY KEY,

    test_name VARCHAR(150) NOT NULL,

    test_category VARCHAR(100) NOT NULL,

    department_id INT NOT NULL,

    standard_cost DECIMAL(10,2)
        CHECK (standard_cost >= 0),

    report_delivery_hours INT NOT NULL
        CHECK (report_delivery_hours >= 0),

    critical_test BOOLEAN NOT NULL,

    fasting_required BOOLEAN NOT NULL,

    sample_type VARCHAR(100),

    test_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DRUG MANUFACTURER
-- ==========================================================

CREATE TABLE drug_manufacturer (

    manufacturer_id INT PRIMARY KEY,

    manufacturer_name VARCHAR(150) NOT NULL,

    manufacturer_code VARCHAR(30) NOT NULL UNIQUE,

    country VARCHAR(100) NOT NULL,

    contact_person VARCHAR(100),

    phone_number VARCHAR(20),

    email VARCHAR(150),

    website VARCHAR(255),

    regulatory_approval VARCHAR(100),

    manufacturer_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DRUG
-- ==========================================================

CREATE TABLE drug (

    drug_id INT PRIMARY KEY,

    drug_name VARCHAR(150) NOT NULL,

    generic_name VARCHAR(150),

    manufacturer_id INT NOT NULL,

    drug_category VARCHAR(100) NOT NULL,

    dosage_form VARCHAR(50) NOT NULL,

    strength VARCHAR(50) NOT NULL,

    unit_price DECIMAL(10,2) NOT NULL
        CHECK (unit_price >= 0),

    prescription_required BOOLEAN NOT NULL,

    storage_temperature VARCHAR(50),

    drug_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : DRUG INVENTORY
-- ==========================================================

CREATE TABLE drug_inventory (

    inventory_id INT PRIMARY KEY,

    drug_id INT NOT NULL,

    current_stock INT NOT NULL
        CHECK (current_stock >= 0),

    reorder_level INT NOT NULL
        CHECK (reorder_level >= 0),

    inventory_status VARCHAR(30) NOT NULL,

    last_restock_date DATE,

    warehouse_location VARCHAR(100),

    storage_zone VARCHAR(50),

    batch_number VARCHAR(50) NOT NULL UNIQUE,

    supplier_lead_time_days INT
        CHECK (supplier_lead_time_days >= 0),

    expiry_date DATE,

    reorder_quantity INT
        CHECK (reorder_quantity >= 0),

    safety_stock INT
        CHECK (safety_stock >= 0),

    maximum_stock INT
        CHECK (maximum_stock >= 0),

    reorder_point INT
        CHECK (reorder_point >= 0),

    next_inspection_date DATE,

    inspection_status VARCHAR(30),

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);
-- ==========================================================
-- MASTER TABLE : INSURANCE PROVIDER
-- ==========================================================

CREATE TABLE insurance_provider (

    insurance_provider_id INT PRIMARY KEY,

    provider_name VARCHAR(150) NOT NULL,

    provider_type VARCHAR(50) NOT NULL,

    contact_details VARCHAR(255),

    coverage_limit DECIMAL(15,2)
        CHECK (coverage_limit >= 0),

    provider_code VARCHAR(30) NOT NULL UNIQUE,

    claim_processing_days INT
        CHECK (claim_processing_days >= 0),

    network_type VARCHAR(50),

    coverage_type VARCHAR(50),

    claim_settlement_ratio DECIMAL(5,2)
        CHECK (claim_settlement_ratio BETWEEN 0 AND 100),

    cashless_available BOOLEAN NOT NULL,

    pre_authorization_required BOOLEAN NOT NULL,

    max_claim_amount DECIMAL(15,2)
        CHECK (max_claim_amount >= 0),

    policy_validity_years INT
        CHECK (policy_validity_years >= 0),

    support_email VARCHAR(150),

    grievance_email VARCHAR(150),

    support_phone VARCHAR(20),

    website VARCHAR(255),

    provider_status VARCHAR(30) NOT NULL,

    created_by VARCHAR(50) NOT NULL DEFAULT 'System',

    updated_by VARCHAR(50) NOT NULL DEFAULT 'System',

    created_date DATE NOT NULL,

    updated_date DATE NOT NULL

);

USE hospital_analytics;

SHOW TABLES;