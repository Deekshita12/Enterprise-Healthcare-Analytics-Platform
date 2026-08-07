-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- 13_security_roles.sql
-- ==========================================================

USE hospital_analytics;

-- ==========================================================
-- Drop Existing Roles (if they exist)
-- ==========================================================

DROP ROLE IF EXISTS 'hospital_admin';
DROP ROLE IF EXISTS 'executive_role';
DROP ROLE IF EXISTS 'doctor_role';
DROP ROLE IF EXISTS 'nurse_role';
DROP ROLE IF EXISTS 'reception_role';
DROP ROLE IF EXISTS 'finance_role';
DROP ROLE IF EXISTS 'hr_role';
DROP ROLE IF EXISTS 'lab_role';
DROP ROLE IF EXISTS 'pharmacy_role';
DROP ROLE IF EXISTS 'data_analyst_role';
DROP ROLE IF EXISTS 'bi_developer_role';

-- ==========================================================
-- Create Roles
-- ==========================================================

CREATE ROLE 'hospital_admin';
CREATE ROLE 'executive_role';
CREATE ROLE 'doctor_role';
CREATE ROLE 'nurse_role';
CREATE ROLE 'reception_role';
CREATE ROLE 'finance_role';
CREATE ROLE 'hr_role';
CREATE ROLE 'lab_role';
CREATE ROLE 'pharmacy_role';
CREATE ROLE 'data_analyst_role';
CREATE ROLE 'bi_developer_role';

-- ==========================================================
-- Hospital Administrator
-- ==========================================================

GRANT ALL PRIVILEGES
ON hospital_analytics.*
TO 'hospital_admin';

-- ==========================================================
-- Executive Dashboard Access
-- ==========================================================

GRANT SELECT
ON hospital_analytics.*
TO 'executive_role';

-- ==========================================================
-- Doctor Access
-- ==========================================================

GRANT SELECT
ON hospital_analytics.patient
TO 'doctor_role';

GRANT SELECT
ON hospital_analytics.admission
TO 'doctor_role';

GRANT SELECT
ON hospital_analytics.patient_diagnostic
TO 'doctor_role';

GRANT SELECT
ON hospital_analytics.diagnostic_test
TO 'doctor_role';

GRANT SELECT
ON hospital_analytics.drug
TO 'doctor_role';

-- ==========================================================
-- Nurse
-- ==========================================================

GRANT SELECT
ON hospital_analytics.patient
TO 'nurse_role';

GRANT SELECT
ON hospital_analytics.admission
TO 'nurse_role';

GRANT SELECT
ON hospital_analytics.bed
TO 'nurse_role';

GRANT SELECT
ON hospital_analytics.ward
TO 'nurse_role';

-- ==========================================================
-- Reception
-- ==========================================================

GRANT SELECT,INSERT,UPDATE
ON hospital_analytics.patient
TO 'reception_role';

GRANT SELECT,INSERT,UPDATE
ON hospital_analytics.admission
TO 'reception_role';

-- ==========================================================
-- Finance
-- ==========================================================

GRANT SELECT
ON hospital_analytics.billing
TO 'finance_role';

GRANT SELECT
ON hospital_analytics.billing_detail
TO 'finance_role';

GRANT SELECT
ON hospital_analytics.insurance_provider
TO 'finance_role';

-- ==========================================================
-- HR
-- ==========================================================

GRANT SELECT
ON hospital_analytics.employee
TO 'hr_role';

GRANT SELECT
ON hospital_analytics.doctor
TO 'hr_role';

GRANT SELECT
ON hospital_analytics.department
TO 'hr_role';

-- ==========================================================
-- Laboratory
-- ==========================================================

GRANT SELECT,UPDATE
ON hospital_analytics.patient_diagnostic
TO 'lab_role';

GRANT SELECT
ON hospital_analytics.diagnostic_test
TO 'lab_role';

-- ==========================================================
-- Pharmacy
-- ==========================================================

GRANT SELECT
ON hospital_analytics.drug
TO 'pharmacy_role';

GRANT SELECT
ON hospital_analytics.drug_inventory
TO 'pharmacy_role';

GRANT SELECT
ON hospital_analytics.drug_manufacturer
TO 'pharmacy_role';

-- ==========================================================
-- Data Analyst
-- ==========================================================

GRANT SELECT
ON hospital_analytics.*
TO 'data_analyst_role';

-- ==========================================================
-- BI Developer
-- ==========================================================

GRANT SELECT
ON hospital_analytics.*
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_executive_kpi_dashboard
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_department_revenue
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_department_admissions
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_monthly_revenue
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_doctor_performance
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_payment_summary
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_top_diseases
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_insurance_summary
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_diagnostic_summary
TO 'bi_developer_role';

GRANT EXECUTE
ON PROCEDURE hospital_analytics.sp_bed_occupancy
TO 'bi_developer_role';

-- ==========================================================
-- Sample Users
-- ==========================================================

DROP USER IF EXISTS 'hospital_admin_user'@'localhost';
DROP USER IF EXISTS 'doctor_user'@'localhost';
DROP USER IF EXISTS 'finance_user'@'localhost';
DROP USER IF EXISTS 'analyst_user'@'localhost';

CREATE USER 'hospital_admin_user'@'localhost'
IDENTIFIED BY 'Admin@123';

CREATE USER 'doctor_user'@'localhost'
IDENTIFIED BY 'Doctor@123';

CREATE USER 'finance_user'@'localhost'
IDENTIFIED BY 'Finance@123';

CREATE USER 'analyst_user'@'localhost'
IDENTIFIED BY 'Analyst@123';

-- ==========================================================
-- Assign Roles
-- ==========================================================

GRANT hospital_admin TO 'hospital_admin_user'@'localhost';

GRANT doctor_role TO 'doctor_user'@'localhost';

GRANT finance_role TO 'finance_user'@'localhost';

GRANT data_analyst_role TO 'analyst_user'@'localhost';

SET DEFAULT ROLE hospital_admin
TO 'hospital_admin_user'@'localhost';

SET DEFAULT ROLE doctor_role
TO 'doctor_user'@'localhost';

SET DEFAULT ROLE finance_role
TO 'finance_user'@'localhost';

SET DEFAULT ROLE data_analyst_role
TO 'analyst_user'@'localhost';

FLUSH PRIVILEGES;

-- ==========================================================
-- Verification Queries
-- ==========================================================

SHOW ROLES;

SHOW GRANTS FOR hospital_admin;

SHOW GRANTS FOR doctor_role;

SHOW GRANTS FOR finance_role;

SHOW GRANTS FOR data_analyst_role;

SHOW GRANTS FOR bi_developer_role;

SELECT CURRENT_ROLE();