-- Enterprise Healthcare Operations Intelligence Platform
-- 09_stored_procedures.sql

-- NOTE:
-- This chat cannot fit a complete 700+ line SQL file in one response.
-- The earlier claim that I could generate the entire file here as one download
-- was incorrect.

-- Existing verified procedure:
-- sp_executive_kpi_dashboard
DELIMITER $$

-- ==========================================================
-- Procedure 2 : Department Admissions Report
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_department_admissions $$

CREATE PROCEDURE sp_department_admissions(
    IN p_department_name VARCHAR(100)
)

BEGIN

SELECT

    d.department_name,

    COUNT(a.admission_id) AS total_admissions,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS average_length_of_stay,

    MIN(a.admission_date) AS first_admission,

    MAX(a.admission_date) AS latest_admission

FROM admission a

INNER JOIN department d
ON a.department_id = d.department_id

WHERE
    p_department_name IS NULL
    OR d.department_name = p_department_name

GROUP BY
    d.department_name

ORDER BY
    total_admissions DESC;

END $$

-- ==========================================================
-- Procedure 3 : Monthly Revenue Report
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_monthly_revenue $$

CREATE PROCEDURE sp_monthly_revenue(

    IN p_year INT

)

BEGIN

SELECT

    YEAR(bill_date) AS bill_year,

    MONTH(bill_date) AS bill_month,

    MONTHNAME(bill_date) AS month_name,

    ROUND(
        SUM(total_amount),
        2
    ) AS gross_revenue,

    ROUND(
        SUM(
            total_amount
            - discount_amount
            + tax_amount
        ),
        2
    ) AS net_revenue,

    COUNT(*) AS total_bills

FROM billing

WHERE

    p_year IS NULL

    OR YEAR(bill_date)=p_year

GROUP BY

    YEAR(bill_date),
    MONTH(bill_date),
    MONTHNAME(bill_date)

ORDER BY

    bill_year,
    bill_month;

END $$

-- ==========================================================
-- Procedure 4 : Department Revenue
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_department_revenue $$

CREATE PROCEDURE sp_department_revenue()

BEGIN

SELECT

    d.department_name,

    COUNT(b.bill_id) AS total_bills,

    ROUND(
        SUM(b.total_amount),
        2
    ) AS gross_revenue,

    ROUND(
        SUM(
            b.total_amount
            - b.discount_amount
            + b.tax_amount
        ),
        2
    ) AS net_revenue,

    ROUND(
        AVG(b.total_amount),
        2
    ) AS average_bill

FROM billing b

INNER JOIN admission a
ON b.admission_id=a.admission_id

INNER JOIN department d
ON a.department_id=d.department_id

GROUP BY

    d.department_name

ORDER BY

    net_revenue DESC;

END $$

-- ==========================================================
-- Procedure 5 : Ward Occupancy Report
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_bed_occupancy $$

CREATE PROCEDURE sp_bed_occupancy()

BEGIN

SELECT

    w.ward_name,

    COUNT(*) AS total_beds,

    SUM(
        CASE

            WHEN b.bed_status='Occupied'

            THEN 1

            ELSE 0

        END

    ) AS occupied_beds,

    ROUND(

        SUM(

            CASE

                WHEN b.bed_status='Occupied'

                THEN 1

                ELSE 0

            END

        )*100.0/

        COUNT(*)

    ,2) AS occupancy_percentage

FROM bed b

INNER JOIN ward w

ON b.ward_id=w.ward_id

GROUP BY

    w.ward_name

ORDER BY

    occupancy_percentage DESC;

END $$


DELIMITER ;

DELIMITER $$

-- ==========================================================
-- Procedure 6 : Doctor Performance
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_doctor_performance $$

CREATE PROCEDURE sp_doctor_performance()

BEGIN

SELECT

    d.doctor_id,

    CONCAT(e.first_name,' ',e.last_name) AS doctor_name,

    d.specialization,

    COUNT(a.admission_id) AS total_admissions,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS average_los

FROM doctor d

INNER JOIN employee e
ON d.employee_id=e.employee_id

LEFT JOIN admission a
ON d.doctor_id=a.admitting_doctor_id

GROUP BY

    d.doctor_id,
    doctor_name,
    d.specialization

ORDER BY
    total_admissions DESC;

END $$


-- ==========================================================
-- Procedure 7 : Top Diseases
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_top_diseases $$

CREATE PROCEDURE sp_top_diseases()

BEGIN

SELECT

    ds.disease_name,

    ds.disease_category,

    COUNT(a.admission_id) AS total_cases,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS average_los

FROM disease ds

LEFT JOIN admission a
ON ds.disease_id=a.disease_id

GROUP BY

    ds.disease_name,
    ds.disease_category

ORDER BY

    total_cases DESC;

END $$


-- ==========================================================
-- Procedure 8 : Payment Summary
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_payment_summary $$

CREATE PROCEDURE sp_payment_summary()

BEGIN

SELECT

    payment_status,

    COUNT(*) AS total_bills,

    ROUND(
        SUM(total_amount),
        2
    ) AS gross_revenue,

    ROUND(
        SUM(patient_payable_amount),
        2
    ) AS patient_amount,

    ROUND(
        SUM(insurance_covered_amount),
        2
    ) AS insurance_amount

FROM billing

GROUP BY

    payment_status

ORDER BY

    gross_revenue DESC;

END $$


-- ==========================================================
-- Procedure 9 : Insurance Summary
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_insurance_summary $$

CREATE PROCEDURE sp_insurance_summary()

BEGIN

SELECT

    ip.provider_name,

    COUNT(DISTINCT pi.patient_id) AS insured_patients,

    ROUND(
        SUM(b.insurance_covered_amount),
        2
    ) AS insurance_paid,

    ROUND(
        AVG(b.insurance_covered_amount),
        2
    ) AS average_claim

FROM insurance_provider ip

LEFT JOIN patient_insurance pi
ON ip.insurance_provider_id=pi.insurance_provider_id

LEFT JOIN patient p
ON pi.patient_id=p.patient_id

LEFT JOIN admission a
ON p.patient_id=a.patient_id

LEFT JOIN billing b
ON a.admission_id=b.admission_id

GROUP BY

    ip.provider_name

ORDER BY

    insurance_paid DESC;

END $$


-- ==========================================================
-- Procedure 10 : Diagnostic Test Summary
-- ==========================================================

DROP PROCEDURE IF EXISTS sp_diagnostic_summary $$

CREATE PROCEDURE sp_diagnostic_summary()

BEGIN

SELECT

    dt.test_name,

    dt.test_category,

    COUNT(pd.patient_diagnostic_id) AS total_tests,

    SUM(

        CASE
            WHEN pd.critical_result=TRUE
            THEN 1
            ELSE 0
        END

    ) AS critical_results

FROM diagnostic_test dt

LEFT JOIN patient_diagnostic pd
ON dt.diagnostic_test_id=pd.diagnostic_test_id

GROUP BY

    dt.test_name,
    dt.test_category

ORDER BY

    total_tests DESC;

END $$

DELIMITER ;