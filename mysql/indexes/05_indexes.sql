-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- Indexes
-- ==========================================================

USE hospital_analytics;

-- ==========================================================
-- PATIENT
-- ==========================================================

CREATE INDEX idx_patient_last_name
ON patient(last_name);

CREATE INDEX idx_patient_city
ON patient(city);

CREATE INDEX idx_patient_status
ON patient(patient_status);

-- ==========================================================
-- ADMISSION
-- ==========================================================

CREATE INDEX idx_admission_date
ON admission(admission_date);

CREATE INDEX idx_discharge_date
ON admission(discharge_date);

CREATE INDEX idx_admission_status
ON admission(admission_status);

CREATE INDEX idx_admission_type
ON admission(admission_type);

CREATE INDEX idx_admission_patient
ON admission(patient_id);

CREATE INDEX idx_admission_department
ON admission(department_id);

CREATE INDEX idx_admission_ward
ON admission(ward_id);

CREATE INDEX idx_admission_bed
ON admission(bed_id);

CREATE INDEX idx_admission_disease
ON admission(disease_id);

CREATE INDEX idx_billing_admission
ON billing(admission_id);

CREATE INDEX idx_prescription_patient
ON prescription(patient_id);

CREATE INDEX idx_prescription_drug
ON prescription(drug_id);

CREATE INDEX idx_billing_date
ON billing(bill_date);

CREATE INDEX idx_patient_diagnostic_date
ON patient_diagnostic(test_date);

CREATE INDEX idx_staff_assignment_date
ON staff_assignment(assignment_date);

CREATE INDEX idx_drug_inventory_expiry
ON drug_inventory(expiry_date);

CREATE INDEX idx_drug_inventory_stock
ON drug_inventory(current_stock);


SHOW INDEX FROM patient;

SHOW INDEX FROM admission;

SHOW INDEX FROM billing;