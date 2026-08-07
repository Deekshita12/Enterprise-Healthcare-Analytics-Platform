\
-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- File : 07_views.sql
-- Database : hospital_analytics
-- Purpose : Enterprise Semantic Layer for Tableau
--
-- Description:
-- Enterprise semantic views optimized for Tableau dashboards.
--
-- Views Included:
-- 1. vw_admission_fact
-- 2. vw_finance_fact
-- 3. vw_pharmacy_fact
-- 4. vw_workforce_fact
--
-- This is the project skeleton. The semantic views should be
-- implemented against the finalized schema.
-- ==========================================================

USE hospital_analytics;

-- ==========================================================
-- VIEW : vw_admission_fact
-- Grain : One Row = One Admission
-- ==========================================================

DROP VIEW IF EXISTS vw_admission_fact;

CREATE VIEW vw_admission_fact AS
SELECT
    a.admission_id,
    a.patient_id,
    CONCAT(p.first_name,' ',p.last_name) AS patient_name,
    p.gender,
    TIMESTAMPDIFF(YEAR,p.date_of_birth,a.admission_date) AS patient_age,
    a.admission_date,
    a.discharge_date,
    CASE
        WHEN a.discharge_date IS NULL THEN DATEDIFF(CURDATE(),a.admission_date)
        ELSE DATEDIFF(a.discharge_date,a.admission_date)
    END AS length_of_stay,
    a.expected_length_of_stay,
    a.actual_length_of_stay,
    dpt.department_name,
    w.ward_name,
    b.bed_number,
    dis.disease_name,
    dis.severity_level,
    doc.doctor_id,
    CONCAT(emp.first_name,' ',emp.last_name) AS admitting_doctor_name,
    YEAR(a.admission_date) AS admission_year,
    QUARTER(a.admission_date) AS admission_quarter,
    MONTH(a.admission_date) AS admission_month,
    MONTHNAME(a.admission_date) AS admission_month_name,
    DAYNAME(a.admission_date) AS admission_weekday,
    CASE WHEN DAYOFWEEK(a.admission_date) IN (1,7) THEN 'Weekend'
         ELSE 'Weekday' END AS admission_day_type,
    CASE WHEN a.discharge_date IS NULL THEN 1 ELSE 0 END AS current_inpatient_flag
FROM admission a
JOIN patient p ON a.patient_id=p.patient_id
JOIN department dpt ON a.department_id=dpt.department_id
JOIN ward w ON a.ward_id=w.ward_id
JOIN bed b ON a.bed_id=b.bed_id
JOIN disease dis ON a.disease_id=dis.disease_id
LEFT JOIN doctor doc ON a.admitting_doctor_id=doc.doctor_id
LEFT JOIN employee emp ON doc.employee_id=emp.employee_id;

  -- ==========================================================
-- VIEW : vw_finance_fact
-- ==========================================================
--
-- Business Purpose
-- ----------------
-- Enterprise semantic layer for financial analytics.
--
-- Grain
-- -----
-- One Row = One Bill
--
-- Used By
-- -------
-- Executive Dashboard
-- Revenue Dashboard
-- Finance Dashboard
-- Insurance Dashboard
--
-- ==========================================================

DROP VIEW IF EXISTS vw_finance_fact;

CREATE VIEW vw_finance_fact AS

SELECT

/*==========================================================
 Billing Information
==========================================================*/

      b.bill_id
    , b.admission_id
    , a.patient_id

    , b.bill_date

    , YEAR(b.bill_date)              AS bill_year
    , QUARTER(b.bill_date)           AS bill_quarter
    , MONTH(b.bill_date)             AS bill_month
    , MONTHNAME(b.bill_date)         AS bill_month_name
    , WEEK(b.bill_date)              AS bill_week
    , DAYNAME(b.bill_date)           AS bill_weekday

/*==========================================================
 Revenue Metrics
==========================================================*/

    , b.total_amount                 AS gross_revenue

    , b.discount_amount

    , b.tax_amount

    , (b.total_amount
       - b.discount_amount
       + b.tax_amount)
       AS net_revenue

    , b.insurance_covered_amount

    , b.patient_payable_amount

/*==========================================================
 Billing Status
==========================================================*/

    , b.payment_status

    , b.payment_mode

    , b.bill_status

/*==========================================================
 Patient Information
==========================================================*/

    , CONCAT(p.first_name,' ',p.last_name)
      AS patient_name

    , p.gender

    , p.city
    , p.state

/*==========================================================
 Department
==========================================================*/

    , d.department_name

/*==========================================================
 Insurance
==========================================================*/

    , ip.provider_name

    , pi.policy_number

    , pi.cashless_eligible

    , pi.coverage_amount

    , pi.remaining_coverage

/*==========================================================
 Business Calculations
==========================================================*/

    , ROUND(
        (b.insurance_covered_amount /
         NULLIF(b.total_amount,0))*100,
         2
      ) AS insurance_coverage_percent

    , ROUND(
        (b.patient_payable_amount /
         NULLIF(b.total_amount,0))*100,
         2
      ) AS patient_contribution_percent

    , CASE

          WHEN b.total_amount >= 100000
          THEN 'Very High'

          WHEN b.total_amount >= 50000
          THEN 'High'

          WHEN b.total_amount >= 20000
          THEN 'Medium'

          ELSE 'Low'

      END AS revenue_category

    , CASE

          WHEN b.total_amount >= 100000
          THEN 1

          ELSE 0

      END AS high_value_bill_flag

    , CASE

          WHEN b.payment_status='Paid'
          THEN 'Collected'

          WHEN b.payment_status='Partial'
          THEN 'Partially Collected'

          ELSE 'Outstanding'

      END AS collection_status

FROM billing b

INNER JOIN admission a
        ON b.admission_id = a.admission_id

INNER JOIN patient p
        ON a.patient_id = p.patient_id

INNER JOIN department d
        ON a.department_id = d.department_id

LEFT JOIN
(
    SELECT
        patient_id,
        insurance_provider_id,
        policy_number,
        cashless_eligible,
        coverage_amount,
        remaining_coverage
    FROM
    (
        SELECT
            patient_id,
            insurance_provider_id,
            policy_number,
            cashless_eligible,
            coverage_amount,
            remaining_coverage,
            ROW_NUMBER() OVER
            (
                PARTITION BY patient_id
                ORDER BY
                    coverage_amount DESC,
                    insurance_provider_id
            ) AS rn
        FROM patient_insurance
   ) x
    WHERE rn = 1
) pi
ON p.patient_id = pi.patient_id

LEFT JOIN insurance_provider ip
ON pi.insurance_provider_id = ip.insurance_provider_id;

-- ==========================================================
-- VIEW : vw_pharmacy_fact
-- ==========================================================
--
-- Business Purpose:
-- Enterprise semantic layer for pharmacy analytics.
--
-- Grain:
-- One Row = One Prescription
--
-- Used By:
-- • Pharmacy Dashboard
-- • Drug Utilization Dashboard
-- • Inventory Dashboard
-- • Doctor Prescription Dashboard
--
-- ==========================================================

DROP VIEW IF EXISTS vw_pharmacy_fact;

CREATE VIEW vw_pharmacy_fact AS

SELECT

/*==========================================================
 Prescription Information
==========================================================*/

      pr.prescription_id
    , pr.patient_id
    , pr.admission_id
    , pr.doctor_id
    , pr.drug_id

    , pr.prescription_date

    , YEAR(pr.prescription_date)          AS prescription_year
    , QUARTER(pr.prescription_date)       AS prescription_quarter
    , MONTH(pr.prescription_date)         AS prescription_month
    , MONTHNAME(pr.prescription_date)     AS prescription_month_name
    , WEEK(pr.prescription_date)          AS prescription_week
    , DAYNAME(pr.prescription_date)       AS prescription_weekday

    , pr.dosage
    , pr.frequency
    , pr.duration_days
    , pr.quantity

    , pr.route_of_administration
    , pr.instructions

    , pr.prescription_status

/*==========================================================
 Patient Information
==========================================================*/

    , CONCAT(p.first_name,' ',p.last_name)
      AS patient_name

    , p.gender
    , p.city
    , p.state

/*==========================================================
 Drug Information
==========================================================*/

    , d.drug_name
    , d.generic_name
    , d.drug_category
    , d.dosage_form
    , d.strength
    , d.unit_price
    , d.prescription_required
    , d.storage_temperature
    , d.drug_status

/*==========================================================
 Manufacturer Information
==========================================================*/

    , dm.manufacturer_name
    , dm.country AS manufacturer_country

/*==========================================================
 Doctor Information
==========================================================*/

    , CONCAT(emp.first_name,' ',emp.last_name)
      AS doctor_name

    , doc.specialization

/*==========================================================
 Business Metrics
==========================================================*/

    , (pr.quantity * d.unit_price)
      AS prescription_value

    , CASE

          WHEN pr.quantity >= 30
          THEN 'High Quantity'

          WHEN pr.quantity >= 15
          THEN 'Medium Quantity'

          ELSE 'Low Quantity'

      END AS prescription_volume

    , CASE

          WHEN d.prescription_required = TRUE
          THEN 'Prescription Drug'

          ELSE 'OTC'

      END AS drug_type

FROM prescription pr

INNER JOIN patient p
        ON pr.patient_id = p.patient_id

INNER JOIN drug d
        ON pr.drug_id = d.drug_id

INNER JOIN drug_manufacturer dm
        ON d.manufacturer_id = dm.manufacturer_id

INNER JOIN doctor doc
        ON pr.doctor_id = doc.doctor_id

INNER JOIN employee emp
        ON doc.employee_id = emp.employee_id;

-- ==========================================================
-- VIEW : vw_workforce_fact
-- ==========================================================
--
-- Business Purpose:
-- Enterprise semantic layer for workforce analytics.
--
-- Grain:
-- One Row = One Staff Assignment
--
-- Used By:
-- • HR Dashboard
-- • Workforce Dashboard
-- • Shift Analytics
-- • Department Staffing Dashboard
--
-- ==========================================================

DROP VIEW IF EXISTS vw_workforce_fact;

CREATE VIEW vw_workforce_fact AS

SELECT

/*==========================================================
 Assignment Information
==========================================================*/

      sa.assignment_id
    , sa.employee_id
    , sa.department_id
    , sa.ward_id
    , sa.admission_id

    , sa.assignment_date

    , YEAR(sa.assignment_date)          AS assignment_year
    , QUARTER(sa.assignment_date)       AS assignment_quarter
    , MONTH(sa.assignment_date)         AS assignment_month
    , MONTHNAME(sa.assignment_date)     AS assignment_month_name
    , WEEK(sa.assignment_date)          AS assignment_week
    , DAYNAME(sa.assignment_date)       AS assignment_weekday

    , sa.shift_type
    , sa.shift_start_time
    , sa.shift_end_time

    , sa.assignment_role
    , sa.assignment_status

/*==========================================================
 Employee Information
==========================================================*/

    , CONCAT(e.first_name,' ',e.last_name)
      AS employee_name

    , e.gender
    , e.designation
    , e.qualification
    , e.years_of_experience
    , e.salary
    , e.employment_status

/*==========================================================
 Department Information
==========================================================*/

    , d.department_name
    , d.department_code

/*==========================================================
 Ward Information
==========================================================*/

    , w.ward_name
    , w.ward_type
    , w.floor_number

/*==========================================================
 Supervisor
==========================================================*/

    , CONCAT(sup.first_name,' ',sup.last_name)
      AS supervisor_name

/*==========================================================
 Business Metrics
==========================================================*/

    , CASE
          WHEN sa.shift_end_time >= sa.shift_start_time
          THEN TIMESTAMPDIFF(
                   HOUR,
                   sa.shift_start_time,
                   sa.shift_end_time
               )
          ELSE TIMESTAMPDIFF(
                   HOUR,
                   sa.shift_start_time,
                   ADDTIME(sa.shift_end_time,'24:00:00')
               )
      END AS shift_hours

    , CASE
          WHEN
              (
                  CASE
                      WHEN sa.shift_end_time >= sa.shift_start_time
                      THEN TIMESTAMPDIFF(
                               HOUR,
                               sa.shift_start_time,
                               sa.shift_end_time
                           )
                      ELSE TIMESTAMPDIFF(
                               HOUR,
                               sa.shift_start_time,
                               ADDTIME(sa.shift_end_time,'24:00:00')
                           )
                  END
              ) >= 12
          THEN 'Extended Shift'

          WHEN
              (
                  CASE
                      WHEN sa.shift_end_time >= sa.shift_start_time
                      THEN TIMESTAMPDIFF(
                               HOUR,
                               sa.shift_start_time,
                               sa.shift_end_time
                           )
                      ELSE TIMESTAMPDIFF(
                               HOUR,
                               sa.shift_start_time,
                               ADDTIME(sa.shift_end_time,'24:00:00')
                           )
                  END
              ) >= 8
          THEN 'Regular Shift'

          ELSE 'Short Shift'
      END AS shift_category
      FROM staff_assignment sa

INNER JOIN employee e
    ON sa.employee_id = e.employee_id

INNER JOIN department d
    ON sa.department_id = d.department_id

LEFT JOIN ward w
    ON sa.ward_id = w.ward_id

LEFT JOIN employee sup
    ON sa.supervisor_id = sup.employee_id;