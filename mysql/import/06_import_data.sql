-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- 06_import_data.sql
-- Master Data Import
-- ==========================================================

USE hospital_analytics;

-- Enable Local File Import
SET FOREIGN_KEY_CHECKS = 0;

ROLLBACK;

-- ==========================================================
-- CLEAN EXISTING DATA
-- ==========================================================

TRUNCATE TABLE staff_assignment;
TRUNCATE TABLE prescription;
TRUNCATE TABLE patient_insurance;
TRUNCATE TABLE patient_diagnostic;
TRUNCATE TABLE billing_detail;
TRUNCATE TABLE billing;
TRUNCATE TABLE admission;
TRUNCATE TABLE patient;

TRUNCATE TABLE drug_inventory;
TRUNCATE TABLE drug;
TRUNCATE TABLE drug_manufacturer;
TRUNCATE TABLE diagnostic_test;
TRUNCATE TABLE disease;
TRUNCATE TABLE bed;
TRUNCATE TABLE ward;
TRUNCATE TABLE doctor;
TRUNCATE TABLE employee;
TRUNCATE TABLE insurance_provider;
TRUNCATE TABLE department;

-- ==========================================================
-- MASTER TABLE : DEPARTMENT
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/department.csv'
INTO TABLE department
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- MASTER TABLE : EMPLOYEE
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/employee.csv'
INTO TABLE employee
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- MASTER TABLE : DOCTOR
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/doctor.csv'
INTO TABLE doctor
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- MASTER TABLE : WARD
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/ward.csv'
INTO TABLE ward
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    ward_id,
    @ward_code,
    ward_name,
    ward_type,
    ward_category,
    department_id,
    capacity,
    @head_nurse_employee_id,
    ward_status,
    floor_number,
    nurse_station,
    occupancy_target,
    cleaning_frequency,
    priority_level,
    @isolation_capability,
    created_date,
    updated_date
)
SET
    isolation_capability =
        IF(LOWER(@isolation_capability)='true',1,0),

    created_by='System',

    updated_by='System';

-- ==========================================================
-- MASTER TABLE : BED
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/bed.csv'
INTO TABLE bed
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- MASTER TABLE : DISEASE
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/disease.csv'
INTO TABLE disease
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
    disease_id,
    disease_name,
    disease_category,
    severity_level,
    @contagious,
    @chronic,
    average_los_days,
    @mortality_risk_text,
    @treatment_priority,
    @follow_up_required,
    @readmission_risk,
    created_date,
    updated_date
)
SET
    icd10_code = CONCAT('ICD-', LPAD(disease_id, 4, '0')),

    mortality_risk =
        CASE
            WHEN LOWER(@mortality_risk_text)='low' THEN 1.00
            WHEN LOWER(@mortality_risk_text)='medium' THEN 2.50
            WHEN LOWER(@mortality_risk_text)='high' THEN 5.00
            WHEN LOWER(@mortality_risk_text)='critical' THEN 10.00
            ELSE NULL
        END,

    contagious =
        IF(LOWER(@contagious)='true',1,0),

    treatment_protocol =
        CASE
            WHEN LOWER(@treatment_priority)='immediate'
                THEN 'Immediate Treatment'
            WHEN LOWER(@treatment_priority)='urgent'
                THEN 'Urgent Treatment'
            ELSE 'Standard Treatment'
        END,

    created_by='System',
    updated_by='System';
-- ==========================================================
-- MASTER TABLE : DIAGNOSTIC TEST
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/diagnostic_test.csv'
INTO TABLE diagnostic_test
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/drug_manufacturer.csv'
INTO TABLE drug_manufacturer
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
manufacturer_id,
manufacturer_name,
country,
@reliability_rating,
@contract_status,
@email,
@phone,
@lead_time,
supplier_tier,
manufacturer_code,
@gmp,
@iso,
website,
@preferred_supplier,
manufacturer_status,
created_date,
updated_date
)

SET
phone_number = @phone,
email = @email,
contact_person = 'Supplier Manager',
regulatory_approval =
    CASE
        WHEN LOWER(@gmp)='true'
        THEN 'GMP Approved'
        ELSE 'Pending'
    END,
average_lead_time_days=@lead_time,
created_by='System',
updated_by='System';

-- ==========================================================
-- MASTER TABLE : DRUG
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/drug.csv'
INTO TABLE drug
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
drug_id,
drug_name,
generic_name,
drug_category,
@unit_price,
manufacturer_id,
dosage_form,
@prescription_required,
@storage_temperature,
@shelf_life_months,
route_of_administration,
therapeutic_class,
drug_schedule,
strength,
@unit_of_measure,
@generic_or_brand,
@controlled_substance,
@high_alert,
drug_status,
created_by,
updated_by,
created_date,
updated_date
)

SET

unit_price=@unit_price,

prescription_required=
CASE
    WHEN LOWER(@prescription_required)='true' THEN 1
    ELSE 0
END,

storage_temperature=@storage_temperature,

shelf_life_months=@shelf_life_months,

minimum_stock_level=100,

maximum_stock_level=1000;

-- ==========================================================
-- MASTER TABLE : DRUG INVENTORY
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/drug_inventory.csv'
INTO TABLE drug_inventory
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- MASTER TABLE : INSURANCE PROVIDER
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/insurance_provider.csv'
INTO TABLE insurance_provider
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
-- ==========================================================
-- TRANSACTION TABLE : PATIENT
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/patient.csv'
INTO TABLE patient
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(
patient_id,
first_name,
last_name,
gender,
date_of_birth,
blood_group,
city,
state,
country,
@contact_number,
email,
emergency_contact_name,
@emergency_contact_number,
marital_status,
@insurance_provider_id,
allergies,
chronic_conditions,
patient_status,
@created_by,
@updated_by,
@created_date,
@updated_date
)

SET

gender =
CASE
    WHEN UPPER(@gender)='M' THEN 'Male'
    WHEN UPPER(@gender)='F' THEN 'Female'
    ELSE 'Other'
END,

contact_number = LEFT(@contact_number,20),

emergency_contact_number = LEFT(@emergency_contact_number,20),

insurance_provider_id =
CASE
    WHEN @insurance_provider_id='' THEN NULL
    WHEN @insurance_provider_id='0' THEN NULL
    WHEN @insurance_provider_id='0.0' THEN NULL
    ELSE CAST(@insurance_provider_id AS UNSIGNED)
END,

created_by='System',
updated_by='System',

created_date=DATE(@created_date),
updated_date=DATE(@updated_date);

-- ==========================================================
-- TRANSACTION TABLE : ADMISSION
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/admission.csv'
INTO TABLE admission
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : BILLING
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/billing.csv'
INTO TABLE billing
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : BILLING DETAIL
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/billing_detail.csv'
INTO TABLE billing_detail
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : PATIENT DIAGNOSTIC
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/patient_diagnostic.csv'
INTO TABLE patient_diagnostic
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : PATIENT INSURANCE
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/patient_insurance.csv'
INTO TABLE patient_insurance
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : PRESCRIPTION
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/prescription.csv'
INTO TABLE prescription
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- TRANSACTION TABLE : STAFF ASSIGNMENT
-- ==========================================================

LOAD DATA LOCAL INFILE
'C:/Users/User/Desktop/Enterprise-Healthcare-Operations-Intelligence-Platform/datasets/enhanced/staff_assignment.csv'
INTO TABLE staff_assignment
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- ==========================================================
-- ENABLE FOREIGN KEY CHECKS
-- ==========================================================

SET FOREIGN_KEY_CHECKS = 1;

COMMIT;
-- ==========================================================
-- IMPORT VALIDATION
-- ==========================================================

SELECT '================ IMPORT VALIDATION ================' AS '';

-- ==========================================================
-- MASTER TABLE RECORD COUNTS
-- ==========================================================

SELECT 'MASTER TABLE COUNTS' AS '';

SELECT COUNT(*) AS department_count          FROM department;
SELECT COUNT(*) AS employee_count            FROM employee;
SELECT COUNT(*) AS doctor_count              FROM doctor;
SELECT COUNT(*) AS ward_count                FROM ward;
SELECT COUNT(*) AS bed_count                 FROM bed;
SELECT COUNT(*) AS disease_count             FROM disease;
SELECT COUNT(*) AS diagnostic_test_count     FROM diagnostic_test;
SELECT COUNT(*) AS drug_manufacturer_count   FROM drug_manufacturer;
SELECT COUNT(*) AS drug_count                FROM drug;
SELECT COUNT(*) AS drug_inventory_count      FROM drug_inventory;
SELECT COUNT(*) AS insurance_provider_count  FROM insurance_provider;

-- ==========================================================
-- TRANSACTION TABLE RECORD COUNTS
-- ==========================================================

SELECT 'TRANSACTION TABLE COUNTS' AS '';

SELECT COUNT(*) AS patient_count             FROM patient;
SELECT COUNT(*) AS admission_count           FROM admission;
SELECT COUNT(*) AS billing_count             FROM billing;
SELECT COUNT(*) AS billing_detail_count      FROM billing_detail;
SELECT COUNT(*) AS patient_diagnostic_count  FROM patient_diagnostic;
SELECT COUNT(*) AS patient_insurance_count   FROM patient_insurance;
SELECT COUNT(*) AS prescription_count        FROM prescription;
SELECT COUNT(*) AS staff_assignment_count    FROM staff_assignment;

-- ==========================================================
-- PRIMARY KEY DUPLICATE VALIDATION
-- ==========================================================

SELECT 'PRIMARY KEY VALIDATION' AS '';

SELECT
COUNT(*) - COUNT(DISTINCT patient_id)
AS duplicate_patient_ids
FROM patient;

SELECT
COUNT(*) - COUNT(DISTINCT admission_id)
AS duplicate_admission_ids
FROM admission;

SELECT
COUNT(*) - COUNT(DISTINCT bill_id)
AS duplicate_bill_ids
FROM billing;

SELECT
COUNT(*) - COUNT(DISTINCT prescription_id)
AS duplicate_prescription_ids
FROM prescription;

-- ==========================================================
-- FOREIGN KEY VALIDATION
-- ==========================================================

SELECT 'FOREIGN KEY VALIDATION' AS '';

-- Admission → Patient

SELECT COUNT(*) AS invalid_patient_fk
FROM admission a
LEFT JOIN patient p
ON a.patient_id = p.patient_id
WHERE p.patient_id IS NULL;

-- Admission → Department

SELECT COUNT(*) AS invalid_department_fk
FROM admission a
LEFT JOIN department d
ON a.department_id = d.department_id
WHERE d.department_id IS NULL;

-- Admission → Ward

SELECT COUNT(*) AS invalid_ward_fk
FROM admission a
LEFT JOIN ward w
ON a.ward_id = w.ward_id
WHERE w.ward_id IS NULL;

-- Admission → Bed

SELECT COUNT(*) AS invalid_bed_fk
FROM admission a
LEFT JOIN bed b
ON a.bed_id = b.bed_id
WHERE b.bed_id IS NULL;

-- Admission → Disease

SELECT COUNT(*) AS invalid_disease_fk
FROM admission a
LEFT JOIN disease d
ON a.disease_id = d.disease_id
WHERE d.disease_id IS NULL;

-- Billing → Admission

SELECT COUNT(*) AS invalid_billing_fk
FROM billing b
LEFT JOIN admission a
ON b.admission_id = a.admission_id
WHERE a.admission_id IS NULL;

-- Billing Detail → Billing

SELECT COUNT(*) AS invalid_billing_detail_fk
FROM billing_detail bd
LEFT JOIN billing b
ON bd.bill_id = b.bill_id
WHERE b.bill_id IS NULL;

-- Prescription → Patient

SELECT COUNT(*) AS invalid_prescription_patient_fk
FROM prescription p
LEFT JOIN patient pt
ON p.patient_id = pt.patient_id
WHERE pt.patient_id IS NULL;

-- Prescription → Drug

SELECT COUNT(*) AS invalid_drug_fk
FROM prescription p
LEFT JOIN drug d
ON p.drug_id = d.drug_id
WHERE d.drug_id IS NULL;

-- Diagnostic → Admission

SELECT COUNT(*) AS invalid_diagnostic_fk
FROM patient_diagnostic pd
LEFT JOIN admission a
ON pd.admission_id = a.admission_id
WHERE a.admission_id IS NULL;

-- Staff Assignment → Employee

SELECT COUNT(*) AS invalid_employee_fk
FROM staff_assignment sa
LEFT JOIN employee e
ON sa.employee_id = e.employee_id
WHERE e.employee_id IS NULL;

-- ==========================================================
-- NULL VALIDATION
-- ==========================================================

SELECT 'NULL VALIDATION' AS '';

SELECT
SUM(patient_id IS NULL) AS null_patient_id,
SUM(first_name IS NULL) AS null_first_name,
SUM(last_name IS NULL) AS null_last_name
FROM patient;

SELECT
SUM(admission_id IS NULL) AS null_admission_id,
SUM(patient_id IS NULL) AS null_patient_fk
FROM admission;

SELECT
SUM(bill_id IS NULL) AS null_bill_id,
SUM(admission_id IS NULL) AS null_admission_fk
FROM billing;

-- ==========================================================
-- SHOW WARNINGS
-- ==========================================================

SHOW COUNT(*) WARNINGS;

SHOW WARNINGS LIMIT 50;

-- ==========================================================
-- IMPORT STATUS
-- ==========================================================

SELECT
'Enterprise Healthcare Operations Intelligence Platform'
AS Project;

SELECT
'Database Import Completed Successfully'
AS Status;

SELECT NOW() AS ImportCompletedAt;

-- ==========================================================
-- END OF FILE
-- ==========================================================