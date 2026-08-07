-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- File : 08_business_queries.sql
-- Database : hospital_analytics
-- Purpose : Enterprise Business Analytics Queries
-- ==========================================================

USE hospital_analytics;

-- ==========================================================
-- SECTION 1 : EXECUTIVE DASHBOARD
-- ==========================================================

-- ==========================================================
-- KPI 1 : Total Patients
-- ==========================================================

SELECT
    COUNT(DISTINCT patient_id) AS total_patients
FROM patient;

-- ==========================================================
-- KPI 2 : Total Admissions
-- ==========================================================

SELECT
    COUNT(*) AS total_admissions
FROM admission;

-- ==========================================================
-- KPI 3 : Current Inpatients
-- ==========================================================

SELECT
    COUNT(*) AS current_inpatients
FROM admission
WHERE discharge_date IS NULL;

-- ==========================================================
-- KPI 4 : Total Revenue
-- ==========================================================

SELECT
    ROUND(SUM(total_amount),2) AS total_revenue
FROM billing;

-- ==========================================================
-- KPI 5 : Net Revenue
-- ==========================================================

SELECT
    ROUND(
        SUM(total_amount-discount_amount+tax_amount),
        2
    ) AS net_revenue
FROM billing;

-- ==========================================================
-- KPI 6 : Average Length of Stay
-- ==========================================================

SELECT
    ROUND(AVG(actual_length_of_stay),2) AS average_los
FROM admission
WHERE actual_length_of_stay IS NOT NULL;

-- ==========================================================
-- KPI 7 : Bed Occupancy
-- ==========================================================

SELECT

    COUNT(DISTINCT CASE
        WHEN bed_status='Occupied'
        THEN bed_id
    END) AS occupied_beds,

    COUNT(*) AS total_beds,

    ROUND(
        COUNT(DISTINCT CASE
            WHEN bed_status='Occupied'
            THEN bed_id
        END)*100.0/COUNT(*),
        2
    ) AS occupancy_percentage

FROM bed;

-- ==========================================================
-- KPI 8 : Average Revenue Per Admission
-- ==========================================================

SELECT

    ROUND(
        SUM(total_amount)/
        COUNT(DISTINCT admission_id),
        2
    ) AS revenue_per_admission

FROM billing;

-- ==========================================================
-- KPI 9 : Insurance Coverage Ratio
-- ==========================================================

SELECT

    ROUND(

        SUM(insurance_covered_amount)*100/

        SUM(total_amount)

    ,2) AS insurance_coverage_percentage

FROM billing;

-- ==========================================================
-- KPI 10 : Patient Payment Ratio
-- ==========================================================

SELECT

    ROUND(

        SUM(patient_payable_amount)*100/

        SUM(total_amount)

    ,2) AS patient_payment_percentage

FROM billing;
-- ==========================================================
-- SECTION 2 : PATIENT FLOW ANALYTICS
-- ==========================================================

-- ==========================================================
-- Query 11 : Monthly Admission Trend
-- ==========================================================

SELECT

    YEAR(admission_date) AS admission_year,
    MONTH(admission_date) AS admission_month,
    MONTHNAME(admission_date) AS month_name,
    COUNT(*) AS total_admissions

FROM admission

GROUP BY
    YEAR(admission_date),
    MONTH(admission_date),
    MONTHNAME(admission_date)

ORDER BY
    admission_year,
    admission_month;

-- ==========================================================
-- Query 12 : Admission Type Distribution
-- ==========================================================

SELECT

    admission_type,
    COUNT(*) AS total_admissions,
    ROUND(COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM admission),2)
        AS percentage

FROM admission

GROUP BY admission_type

ORDER BY total_admissions DESC;

-- ==========================================================
-- Query 13 : Department-wise Admissions
-- ==========================================================

SELECT

    d.department_name,
    COUNT(a.admission_id) AS total_admissions

FROM admission a

INNER JOIN department d
        ON a.department_id = d.department_id

GROUP BY
    d.department_name

ORDER BY
    total_admissions DESC;

-- ==========================================================
-- Query 14 : Disease-wise Admissions
-- ==========================================================

SELECT

    ds.disease_name,
    COUNT(a.admission_id) AS total_cases

FROM admission a

INNER JOIN disease ds
        ON a.disease_id = ds.disease_id

GROUP BY
    ds.disease_name

ORDER BY
    total_cases DESC;

-- ==========================================================
-- Query 15 : Average Length of Stay by Department
-- ==========================================================

SELECT

    d.department_name,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS average_los

FROM admission a

INNER JOIN department d
        ON a.department_id = d.department_id

WHERE
    a.actual_length_of_stay IS NOT NULL

GROUP BY
    d.department_name

ORDER BY
    average_los DESC;

-- ==========================================================
-- Query 16 : Average Length of Stay by Disease
-- ==========================================================

SELECT

    ds.disease_name,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS average_los

FROM admission a

INNER JOIN disease ds
        ON a.disease_id = ds.disease_id

WHERE
    a.actual_length_of_stay IS NOT NULL

GROUP BY
    ds.disease_name

ORDER BY
    average_los DESC;

-- ==========================================================
-- Query 17 : Long Stay Patients (>10 Days)
-- ==========================================================

SELECT

    a.admission_id,

    CONCAT(
        p.first_name,
        ' ',
        p.last_name
    ) AS patient_name,

    d.department_name,

    a.actual_length_of_stay

FROM admission a

INNER JOIN patient p
        ON a.patient_id = p.patient_id

INNER JOIN department d
        ON a.department_id = d.department_id

WHERE
    a.actual_length_of_stay > 10

ORDER BY
    a.actual_length_of_stay DESC;

-- ==========================================================
-- Query 18 : Readmission Analysis
-- ==========================================================

SELECT

    patient_id,

    COUNT(admission_id) AS admission_count

FROM admission

GROUP BY
    patient_id

HAVING
    COUNT(admission_id) > 1

ORDER BY
    admission_count DESC;

-- ==========================================================
-- Query 19 : Admission Status Summary
-- ==========================================================

SELECT

    admission_status,

    COUNT(*) AS total_cases

FROM admission

GROUP BY
    admission_status

ORDER BY
    total_cases DESC;

-- ==========================================================
-- Query 20 : Patient Age Group Analysis
-- ==========================================================

SELECT

CASE

WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) <18
THEN 'Child'

WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 18 AND 35
THEN 'Young Adult'

WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 36 AND 55
THEN 'Adult'

WHEN TIMESTAMPDIFF(YEAR,date_of_birth,CURDATE()) BETWEEN 56 AND 75
THEN 'Senior Adult'

ELSE 'Geriatric'

END AS age_group,

COUNT(*) AS total_patients

FROM patient

GROUP BY age_group

ORDER BY total_patients DESC;
-- ==========================================================
-- SECTION 3 : BED MANAGEMENT ANALYTICS
-- ==========================================================

-- ==========================================================
-- Query 21 : Ward-wise Bed Capacity
-- ==========================================================

SELECT

    w.ward_name,
    w.ward_type,
    COUNT(b.bed_id) AS total_beds

FROM ward w

INNER JOIN bed b
        ON w.ward_id = b.ward_id

GROUP BY
    w.ward_name,
    w.ward_type

ORDER BY
    total_beds DESC;

-- ==========================================================
-- Query 22 : Bed Status Distribution
-- ==========================================================

SELECT

    bed_status,
    COUNT(*) AS total_beds

FROM bed

GROUP BY
    bed_status

ORDER BY
    total_beds DESC;

-- ==========================================================
-- Query 23 : Ward Occupancy Rate
-- ==========================================================

SELECT

    w.ward_name,

    COUNT(b.bed_id) AS total_beds,

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
        ) * 100.0 /

        COUNT(b.bed_id)

    ,2) AS occupancy_percentage

FROM ward w

INNER JOIN bed b
        ON w.ward_id = b.ward_id

GROUP BY
    w.ward_name

ORDER BY
    occupancy_percentage DESC;

-- ==========================================================
-- Query 24 : Available Beds by Ward
-- ==========================================================

SELECT

    w.ward_name,

    COUNT(*) AS available_beds

FROM bed b

INNER JOIN ward w
        ON b.ward_id = w.ward_id

WHERE
    b.bed_status='Available'

GROUP BY
    w.ward_name

ORDER BY
    available_beds DESC;

-- ==========================================================
-- Query 25 : ICU / Isolation Bed Availability
-- ==========================================================

SELECT

    w.ward_name,

    w.isolation_capability,

    COUNT(b.bed_id) AS total_beds,

    SUM(
        CASE
            WHEN b.bed_status='Available'
            THEN 1
            ELSE 0
        END
    ) AS available_beds

FROM ward w

INNER JOIN bed b
        ON w.ward_id=b.ward_id

WHERE
    w.isolation_capability=TRUE

GROUP BY
    w.ward_name,
    w.isolation_capability;

-- ==========================================================
-- Query 26 : Oxygen Supported Beds
-- ==========================================================

SELECT

    COUNT(*) AS oxygen_supported_beds

FROM bed

WHERE
    oxygen_supported=TRUE;

-- ==========================================================
-- Query 27 : Ventilator Supported Beds
-- ==========================================================

SELECT

    COUNT(*) AS ventilator_supported_beds

FROM bed

WHERE
    ventilator_supported=TRUE;

-- ==========================================================
-- Query 28 : Beds Under Maintenance
-- ==========================================================

SELECT

    bed_number,
    room_number,
    maintenance_status

FROM bed

WHERE
    maintenance_status <> 'Operational'

ORDER BY
    maintenance_status;

-- ==========================================================
-- Query 29 : Ward-wise Bed Type Distribution
-- ==========================================================

SELECT

    w.ward_name,

    b.bed_type,

    COUNT(*) AS total_beds

FROM bed b

INNER JOIN ward w
        ON b.ward_id=w.ward_id

GROUP BY
    w.ward_name,
    b.bed_type

ORDER BY
    w.ward_name,
    total_beds DESC;

-- ==========================================================
-- Query 30 : High Occupancy Wards (>85%)
-- ==========================================================

SELECT

    w.ward_name,

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

FROM ward w

INNER JOIN bed b
        ON w.ward_id=b.ward_id

GROUP BY
    w.ward_name

HAVING
    occupancy_percentage > 85

ORDER BY
    occupancy_percentage DESC;

-- ==========================================================
-- SECTION 4 : CLINICAL QUALITY ANALYTICS
-- ==========================================================

-- ==========================================================
-- Query 31 : Department-wise Disease Distribution
-- ==========================================================

SELECT

    d.department_name,
    ds.disease_name,
    COUNT(a.admission_id) AS total_cases

FROM admission a

INNER JOIN department d
        ON a.department_id = d.department_id

INNER JOIN disease ds
        ON a.disease_id = ds.disease_id

GROUP BY
    d.department_name,
    ds.disease_name

ORDER BY
    d.department_name,
    total_cases DESC;

-- ==========================================================
-- Query 32 : Disease Severity Distribution
-- ==========================================================

SELECT

    severity_level,

    COUNT(*) AS total_diseases

FROM disease

GROUP BY
    severity_level

ORDER BY
    total_diseases DESC;

-- ==========================================================
-- Query 33 : High Mortality Risk Diseases
-- ==========================================================

SELECT

    disease_name,
    disease_category,
    mortality_risk

FROM disease

WHERE
    mortality_risk >= 50

ORDER BY
    mortality_risk DESC;

-- ==========================================================
-- Query 34 : Contagious Disease Cases
-- ==========================================================

SELECT

    ds.disease_name,

    COUNT(a.admission_id) AS total_cases

FROM admission a

INNER JOIN disease ds
        ON a.disease_id = ds.disease_id

WHERE
    ds.contagious = TRUE

GROUP BY
    ds.disease_name

ORDER BY
    total_cases DESC;

-- ==========================================================
-- Query 35 : Diagnostic Test Utilization
-- ==========================================================

SELECT

    dt.test_name,

    dt.test_category,

    COUNT(pd.patient_diagnostic_id) AS total_tests

FROM patient_diagnostic pd

INNER JOIN diagnostic_test dt
        ON pd.diagnostic_test_id = dt.diagnostic_test_id

GROUP BY
    dt.test_name,
    dt.test_category

ORDER BY
    total_tests DESC;

-- ==========================================================
-- Query 36 : Critical Test Results
-- ==========================================================

SELECT

    dt.test_name,

    COUNT(pd.patient_diagnostic_id) AS critical_cases

FROM patient_diagnostic pd

INNER JOIN diagnostic_test dt
        ON pd.diagnostic_test_id = dt.diagnostic_test_id

WHERE
    pd.critical_result = TRUE

GROUP BY
    dt.test_name

ORDER BY
    critical_cases DESC;

-- ==========================================================
-- Query 37 : Average Diagnostic Turnaround Time
-- ==========================================================

SELECT

    dt.test_name,

    ROUND(
        AVG(
            DATEDIFF(
                pd.report_date,
                pd.sample_collection_date
            )
        ),
        2
    ) AS average_turnaround_days

FROM patient_diagnostic pd

INNER JOIN diagnostic_test dt
        ON pd.diagnostic_test_id = dt.diagnostic_test_id

WHERE
    pd.report_date IS NOT NULL
AND pd.sample_collection_date IS NOT NULL

GROUP BY
    dt.test_name

ORDER BY
    average_turnaround_days DESC;

-- ==========================================================
-- Query 38 : Doctor-wise Diagnostic Requests
-- ==========================================================

SELECT

    CONCAT(
        e.first_name,
        ' ',
        e.last_name
    ) AS doctor_name,

    COUNT(pd.patient_diagnostic_id) AS total_tests_requested

FROM patient_diagnostic pd

INNER JOIN doctor d
        ON pd.doctor_id = d.doctor_id

INNER JOIN employee e
        ON d.employee_id = e.employee_id

GROUP BY
    doctor_name

ORDER BY
    total_tests_requested DESC;

-- ==========================================================
-- Query 39 : Average Length of Stay vs Standard LOS
-- ==========================================================

SELECT

    ds.disease_name,

    ds.average_los_days AS standard_los,

    ROUND(
        AVG(a.actual_length_of_stay),
        2
    ) AS actual_average_los,

    ROUND(
        AVG(a.actual_length_of_stay) - ds.average_los_days,
        2
    ) AS los_variance

FROM admission a

INNER JOIN disease ds
        ON a.disease_id = ds.disease_id

WHERE
    a.actual_length_of_stay IS NOT NULL

GROUP BY
    ds.disease_name,
    ds.average_los_days

ORDER BY
    los_variance DESC;

-- ==========================================================
-- Query 40 : Top 10 Doctors by Patient Admissions
-- ==========================================================

SELECT

    CONCAT(
        e.first_name,
        ' ',
        e.last_name
    ) AS doctor_name,

    d.specialization,

    COUNT(a.admission_id) AS total_admissions

FROM admission a

INNER JOIN doctor d
        ON a.admitting_doctor_id = d.doctor_id

INNER JOIN employee e
        ON d.employee_id = e.employee_id

GROUP BY
    doctor_name,
    d.specialization

ORDER BY
    total_admissions DESC

LIMIT 10;

-- ==========================================================
-- SECTION 5 : FINANCIAL ANALYTICS
-- ==========================================================

-- ==========================================================
-- Query 41 : Monthly Revenue Trend
-- ==========================================================

SELECT

    YEAR(bill_date) AS bill_year,
    MONTH(bill_date) AS bill_month,
    MONTHNAME(bill_date) AS month_name,

    ROUND(
        SUM(total_amount),
        2
    ) AS total_revenue,

    ROUND(
        SUM(total_amount-discount_amount+tax_amount),
        2
    ) AS net_revenue

FROM billing

GROUP BY
    YEAR(bill_date),
    MONTH(bill_date),
    MONTHNAME(bill_date)

ORDER BY
    bill_year,
    bill_month;

-- ==========================================================
-- Query 42 : Department-wise Revenue
-- ==========================================================

SELECT

    d.department_name,

    COUNT(b.bill_id) AS total_bills,

    ROUND(
        SUM(b.total_amount),
        2
    ) AS gross_revenue,

    ROUND(
        SUM(b.total_amount-b.discount_amount+b.tax_amount),
        2
    ) AS net_revenue

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN department d
        ON a.department_id=d.department_id

GROUP BY
    d.department_name

ORDER BY
    net_revenue DESC;

-- ==========================================================
-- Query 43 : Payment Status Analysis
-- ==========================================================

SELECT

    payment_status,

    COUNT(*) AS total_bills,

    ROUND(
        SUM(total_amount),
        2
    ) AS revenue

FROM billing

GROUP BY
    payment_status

ORDER BY
    revenue DESC;

-- ==========================================================
-- Query 44 : Payment Mode Analysis
-- ==========================================================

SELECT

    payment_mode,

    COUNT(*) AS total_transactions,

    ROUND(
        SUM(total_amount),
        2
    ) AS total_amount

FROM billing

GROUP BY
    payment_mode

ORDER BY
    total_amount DESC;

-- ==========================================================
-- Query 45 : Insurance Provider Performance
-- ==========================================================

SELECT

    ip.provider_name,

    COUNT(pi.patient_id) AS insured_patients,

    ROUND(
        SUM(b.insurance_covered_amount),
        2
    ) AS insurance_paid,

    ROUND(
        AVG(b.insurance_covered_amount),
        2
    ) AS average_claim

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN patient p
        ON a.patient_id=p.patient_id

INNER JOIN patient_insurance pi
        ON p.patient_id=pi.patient_id

INNER JOIN insurance_provider ip
        ON pi.insurance_provider_id=ip.insurance_provider_id

GROUP BY
    ip.provider_name

ORDER BY
    insurance_paid DESC;

-- ==========================================================
-- Query 46 : Top 10 Highest Bills
-- ==========================================================

SELECT

    b.bill_id,

    CONCAT(
        p.first_name,
        ' ',
        p.last_name
    ) AS patient_name,

    d.department_name,

    b.total_amount

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN patient p
        ON a.patient_id=p.patient_id

INNER JOIN department d
        ON a.department_id=d.department_id

ORDER BY
    b.total_amount DESC

LIMIT 10;

-- ==========================================================
-- Query 47 : Average Revenue Per Department
-- ==========================================================

SELECT

    d.department_name,

    ROUND(
        AVG(b.total_amount),
        2
    ) AS average_bill_amount

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN department d
        ON a.department_id=d.department_id

GROUP BY
    d.department_name

ORDER BY
    average_bill_amount DESC;

-- ==========================================================
-- Query 48 : Discount Analysis
-- ==========================================================

SELECT

    d.department_name,

    ROUND(
        SUM(b.discount_amount),
        2
    ) AS total_discount,

    ROUND(
        AVG(b.discount_amount),
        2
    ) AS average_discount

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN department d
        ON a.department_id=d.department_id

GROUP BY
    d.department_name

ORDER BY
    total_discount DESC;

-- ==========================================================
-- Query 49 : Outstanding Payments
-- ==========================================================

SELECT

    b.bill_id,

    CONCAT(
        p.first_name,
        ' ',
        p.last_name
    ) AS patient_name,

    b.patient_payable_amount,

    b.payment_status

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

INNER JOIN patient p
        ON a.patient_id=p.patient_id

WHERE
    b.payment_status <> 'Paid'

ORDER BY
    b.patient_payable_amount DESC;

-- ==========================================================
-- Query 50 : Revenue by Admission Type
-- ==========================================================

SELECT

    a.admission_type,

    COUNT(b.bill_id) AS total_bills,

    ROUND(
        SUM(b.total_amount),
        2
    ) AS total_revenue,

    ROUND(
        AVG(b.total_amount),
        2
    ) AS average_bill_amount

FROM billing b

INNER JOIN admission a
        ON b.admission_id=a.admission_id

GROUP BY
    a.admission_type

ORDER BY
    total_revenue DESC;