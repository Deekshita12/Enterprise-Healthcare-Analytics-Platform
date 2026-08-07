-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- Foreign Key Constraints
-- ==========================================================

USE hospital_analytics;
-- ==========================================================
-- MASTER TABLE FOREIGN KEYS
-- ==========================================================

ALTER TABLE employee
ADD CONSTRAINT fk_employee_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);
ALTER TABLE doctor
ADD CONSTRAINT fk_doctor_employee
FOREIGN KEY (employee_id)
REFERENCES employee(employee_id);
ALTER TABLE ward
ADD CONSTRAINT fk_ward_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);
ALTER TABLE bed
ADD CONSTRAINT fk_bed_ward
FOREIGN KEY (ward_id)
REFERENCES ward(ward_id);
ALTER TABLE diagnostic_test
ADD CONSTRAINT fk_diagnostic_test_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);
ALTER TABLE drug
ADD CONSTRAINT fk_drug_manufacturer
FOREIGN KEY (manufacturer_id)
REFERENCES drug_manufacturer(manufacturer_id);
ALTER TABLE drug_inventory
ADD CONSTRAINT fk_drug_inventory_drug
FOREIGN KEY (drug_id)
REFERENCES drug(drug_id);

-- ==========================================================
-- TRANSACTION TABLE FOREIGN KEYS
-- ==========================================================

ALTER TABLE patient
ADD CONSTRAINT fk_patient_insurance_insurance_provider
FOREIGN KEY (insurance_provider_id)
REFERENCES insurance_provider(insurance_provider_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_patient
FOREIGN KEY (patient_id)
REFERENCES patient(patient_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_ward
FOREIGN KEY (ward_id)
REFERENCES ward(ward_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_bed
FOREIGN KEY (bed_id)
REFERENCES bed(bed_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_disease
FOREIGN KEY (disease_id)
REFERENCES disease(disease_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_admitting_doctor
FOREIGN KEY (admitting_doctor_id)
REFERENCES doctor(doctor_id);

ALTER TABLE admission
ADD CONSTRAINT fk_admission_discharge_doctor
FOREIGN KEY (discharge_doctor_id)
REFERENCES doctor(doctor_id);

ALTER TABLE billing
ADD CONSTRAINT fk_billing_admission
FOREIGN KEY (admission_id)
REFERENCES admission(admission_id);

-- ==========================================================
-- BILLING DETAIL FOREIGN KEYS
-- ==========================================================

ALTER TABLE billing_detail
ADD CONSTRAINT fk_billing_detail_bill
FOREIGN KEY (bill_id)
REFERENCES billing(bill_id);

ALTER TABLE billing_detail
ADD CONSTRAINT fk_billing_detail_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);

ALTER TABLE billing_detail
ADD CONSTRAINT fk_billing_detail_doctor
FOREIGN KEY (doctor_id)
REFERENCES doctor(doctor_id);

-- ==========================================================
-- PATIENT DIAGNOSTIC FOREIGN KEYS
-- ==========================================================

ALTER TABLE patient_diagnostic
ADD CONSTRAINT fk_patient_diagnostic_patient
FOREIGN KEY (patient_id)
REFERENCES patient(patient_id);

ALTER TABLE patient_diagnostic
ADD CONSTRAINT fk_patient_diagnostic_admission
FOREIGN KEY (admission_id)
REFERENCES admission(admission_id);

ALTER TABLE patient_diagnostic
ADD CONSTRAINT fk_patient_diagnostic_test
FOREIGN KEY (diagnostic_test_id)
REFERENCES diagnostic_test(diagnostic_test_id);

ALTER TABLE patient_diagnostic
ADD CONSTRAINT fk_patient_diagnostic_doctor
FOREIGN KEY (doctor_id)
REFERENCES doctor(doctor_id);

-- ==========================================================
-- PATIENT INSURANCE FOREIGN KEYS
-- ==========================================================

ALTER TABLE patient_insurance
ADD CONSTRAINT fk_patient_insurance_patient
FOREIGN KEY (patient_id)
REFERENCES patient(patient_id);

ALTER TABLE patient_insurance
ADD CONSTRAINT fk_patient_insurance_provider
FOREIGN KEY (insurance_provider_id)
REFERENCES insurance_provider(insurance_provider_id);

-- ==========================================================
-- PRESCRIPTION FOREIGN KEYS
-- ==========================================================

ALTER TABLE prescription
ADD CONSTRAINT fk_prescription_patient
FOREIGN KEY (patient_id)
REFERENCES patient(patient_id);

ALTER TABLE prescription
ADD CONSTRAINT fk_prescription_admission
FOREIGN KEY (admission_id)
REFERENCES admission(admission_id);

ALTER TABLE prescription
ADD CONSTRAINT fk_prescription_doctor
FOREIGN KEY (doctor_id)
REFERENCES doctor(doctor_id);

ALTER TABLE prescription
ADD CONSTRAINT fk_prescription_drug
FOREIGN KEY (drug_id)
REFERENCES drug(drug_id);

-- ==========================================================
-- STAFF ASSIGNMENT FOREIGN KEYS
-- ==========================================================

ALTER TABLE staff_assignment
ADD CONSTRAINT fk_staff_assignment_employee
FOREIGN KEY (employee_id)
REFERENCES employee(employee_id);

ALTER TABLE staff_assignment
ADD CONSTRAINT fk_staff_assignment_department
FOREIGN KEY (department_id)
REFERENCES department(department_id);

ALTER TABLE staff_assignment
ADD CONSTRAINT fk_staff_assignment_ward
FOREIGN KEY (ward_id)
REFERENCES ward(ward_id);

ALTER TABLE staff_assignment
ADD CONSTRAINT fk_staff_assignment_admission
FOREIGN KEY (admission_id)
REFERENCES admission(admission_id);

ALTER TABLE staff_assignment
ADD CONSTRAINT fk_staff_assignment_supervisor
FOREIGN KEY (supervisor_id)
REFERENCES employee(employee_id);

SELECT DATABASE();
SHOW CREATE TABLE patient_insurance;