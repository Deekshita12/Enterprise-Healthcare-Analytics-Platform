-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- File: 14_performance_optimization.sql
-- Purpose:
-- Performance Validation & Database Health Check
-- ==========================================================

USE hospital_analytics;

-- ==========================================================
-- 1. UPDATE TABLE STATISTICS
-- ==========================================================

SELECT 'Updating Table Statistics...' AS Status;

ANALYZE TABLE patient;
ANALYZE TABLE admission;
ANALYZE TABLE billing;
ANALYZE TABLE billing_detail;
ANALYZE TABLE department;
ANALYZE TABLE doctor;
ANALYZE TABLE employee;
ANALYZE TABLE ward;
ANALYZE TABLE bed;
ANALYZE TABLE disease;
ANALYZE TABLE patient_diagnostic;
ANALYZE TABLE diagnostic_test;
ANALYZE TABLE drug;
ANALYZE TABLE drug_inventory;
ANALYZE TABLE insurance_provider;

-- ==========================================================
-- 2. OPTIMIZE TABLES
-- ==========================================================

SELECT 'Optimizing Tables...' AS Status;

OPTIMIZE TABLE patient;
OPTIMIZE TABLE admission;
OPTIMIZE TABLE billing;
OPTIMIZE TABLE billing_detail;
OPTIMIZE TABLE patient_diagnostic;

-- ==========================================================
-- 3. VERIFY INDEXES
-- ==========================================================

SELECT 'Patient Indexes' AS Section;
SHOW INDEX FROM patient;

SELECT 'Admission Indexes' AS Section;
SHOW INDEX FROM admission;

SELECT 'Billing Indexes' AS Section;
SHOW INDEX FROM billing;

SELECT 'Billing Detail Indexes' AS Section;
SHOW INDEX FROM billing_detail;

SELECT 'Patient Diagnostic Indexes' AS Section;
SHOW INDEX FROM patient_diagnostic;

SELECT 'Bed Indexes' AS Section;
SHOW INDEX FROM bed;

-- ==========================================================
-- 4. QUERY EXECUTION PLAN
-- ==========================================================

SELECT 'Execution Plan - Patient Search' AS Section;

EXPLAIN
SELECT *
FROM patient
WHERE patient_id = 100;

SELECT 'Execution Plan - Admission Search' AS Section;

EXPLAIN
SELECT *
FROM admission
WHERE patient_id = 100;

SELECT 'Execution Plan - Billing Search' AS Section;

EXPLAIN
SELECT *
FROM billing
WHERE admission_id = 100;

SELECT 'Execution Plan - Department Revenue' AS Section;

EXPLAIN
SELECT
department_id,
COUNT(*)
FROM admission
GROUP BY department_id;

SELECT 'Execution Plan - Monthly Revenue' AS Section;

EXPLAIN
SELECT
YEAR(bill_date),
MONTH(bill_date),
SUM(total_amount)
FROM billing
GROUP BY YEAR(bill_date), MONTH(bill_date);

-- ==========================================================
-- 5. TABLE STATUS
-- ==========================================================

SELECT 'Table Status' AS Section;

SHOW TABLE STATUS;

-- ==========================================================
-- 6. DATABASE SIZE
-- ==========================================================

SELECT
table_schema AS database_name,
ROUND(SUM(data_length+index_length)/1024/1024,2) AS database_size_mb
FROM information_schema.tables
WHERE table_schema='hospital_analytics'
GROUP BY table_schema;

-- ==========================================================
-- 7. TABLE STORAGE DETAILS
-- ==========================================================

SELECT
table_name,
engine,
table_rows,
ROUND((data_length+index_length)/1024/1024,2) AS size_mb
FROM information_schema.tables
WHERE table_schema='hospital_analytics'
ORDER BY size_mb DESC;

-- ==========================================================
-- 8. STORAGE ENGINE VALIDATION
-- ==========================================================

SELECT
table_name,
engine
FROM information_schema.tables
WHERE table_schema='hospital_analytics'
ORDER BY table_name;

-- ==========================================================
-- 9. FOREIGN KEY VALIDATION
-- ==========================================================

SELECT
table_name,
constraint_name,
referenced_table_name
FROM information_schema.key_column_usage
WHERE table_schema='hospital_analytics'
AND referenced_table_name IS NOT NULL
ORDER BY table_name;

-- ==========================================================
-- 10. PROCEDURE VALIDATION
-- ==========================================================

SHOW PROCEDURE STATUS
WHERE Db='hospital_analytics';

-- ==========================================================
-- 11. FUNCTION VALIDATION
-- ==========================================================

SHOW FUNCTION STATUS
WHERE Db='hospital_analytics';

-- ==========================================================
-- 12. TRIGGER VALIDATION
-- ==========================================================

SHOW TRIGGERS;

-- ==========================================================
-- 13. EVENT VALIDATION
-- ==========================================================

SHOW EVENTS;

SHOW VARIABLES
LIKE 'event_scheduler';

-- ==========================================================
-- 14. VIEW VALIDATION
-- ==========================================================

SHOW FULL TABLES
WHERE Table_type='VIEW';

-- ==========================================================
-- 15. ROW COUNT VALIDATION
-- ==========================================================

SELECT 'Patient' AS Table_Name, COUNT(*) AS Total_Rows FROM patient
UNION ALL
SELECT 'Admission', COUNT(*) FROM admission
UNION ALL
SELECT 'Billing', COUNT(*) FROM billing
UNION ALL
SELECT 'Billing Detail', COUNT(*) FROM billing_detail
UNION ALL
SELECT 'Department', COUNT(*) FROM department
UNION ALL
SELECT 'Doctor', COUNT(*) FROM doctor
UNION ALL
SELECT 'Employee', COUNT(*) FROM employee
UNION ALL
SELECT 'Ward', COUNT(*) FROM ward
UNION ALL
SELECT 'Bed', COUNT(*) FROM bed
UNION ALL
SELECT 'Disease', COUNT(*) FROM disease
UNION ALL
SELECT 'Diagnostic Test', COUNT(*) FROM diagnostic_test
UNION ALL
SELECT 'Patient Diagnostic', COUNT(*) FROM patient_diagnostic
UNION ALL
SELECT 'Drug', COUNT(*) FROM drug
UNION ALL
SELECT 'Drug Inventory', COUNT(*) FROM drug_inventory
UNION ALL
SELECT 'Insurance Provider', COUNT(*) FROM insurance_provider;

-- ==========================================================
-- 16. DATABASE PERFORMANCE SUMMARY
-- ==========================================================

SELECT
DATABASE() AS Database_Name,
NOW() AS Validation_Time,
VERSION() AS MySQL_Version;

SELECT 'Performance Validation Completed Successfully' AS Status;