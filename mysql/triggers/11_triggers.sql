    USE hospital_analytics;

DELIMITER $$

-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- 11_triggers.sql
-- ==========================================================

-- ==========================================================
-- Trigger 1 : Prevent Negative Billing Amount
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_bill_amount $$

CREATE TRIGGER trg_validate_bill_amount

BEFORE INSERT

ON billing

FOR EACH ROW

BEGIN

    IF NEW.total_amount < 0 THEN

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT='Billing amount cannot be negative';

    END IF;

END $$


-- ==========================================================
-- Trigger 2 : Prevent Negative Discount
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_discount $$

CREATE TRIGGER trg_validate_discount

BEFORE INSERT

ON billing

FOR EACH ROW

BEGIN

    IF NEW.discount_amount < 0 THEN

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT='Discount cannot be negative';

    END IF;

END $$


-- ==========================================================
-- Trigger 3 : Prevent Future Admission Date
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_admission_date $$

CREATE TRIGGER trg_validate_admission_date

BEFORE INSERT

ON admission

FOR EACH ROW

BEGIN

    IF NEW.admission_date > CURDATE() THEN

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT='Admission date cannot be in the future';

    END IF;

END $$


-- ==========================================================
-- Trigger 4 : Validate Discharge Date
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_discharge_date $$

CREATE TRIGGER trg_validate_discharge_date

BEFORE INSERT

ON admission

FOR EACH ROW

BEGIN

    IF NEW.discharge_date IS NOT NULL
    AND NEW.discharge_date < NEW.admission_date THEN

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT='Discharge date cannot be before admission date';

    END IF;

END $$


-- ==========================================================
-- Trigger 5 : Prevent Negative Salary
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_salary $$

CREATE TRIGGER trg_validate_salary

BEFORE INSERT

ON employee

FOR EACH ROW

BEGIN

    IF NEW.salary < 0 THEN

        SIGNAL SQLSTATE '45000'

        SET MESSAGE_TEXT='Salary cannot be negative';

    END IF;

END $$

DELIMITER ;
DELIMITER $$

-- ==========================================================
-- Trigger 6 : Prevent Negative Billing Amount (UPDATE)
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_bill_amount_update $$

CREATE TRIGGER trg_validate_bill_amount_update
BEFORE UPDATE
ON billing
FOR EACH ROW
BEGIN

    IF NEW.total_amount < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Billing amount cannot be negative';
    END IF;

END $$


-- ==========================================================
-- Trigger 7 : Prevent Negative Discount (UPDATE)
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_discount_update $$

CREATE TRIGGER trg_validate_discount_update
BEFORE UPDATE
ON billing
FOR EACH ROW
BEGIN

    IF NEW.discount_amount < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Discount cannot be negative';
    END IF;

END $$


-- ==========================================================
-- Trigger 8 : Validate Salary (UPDATE)
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_salary_update $$

CREATE TRIGGER trg_validate_salary_update
BEFORE UPDATE
ON employee
FOR EACH ROW
BEGIN

    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Salary cannot be negative';
    END IF;

END $$


-- ==========================================================
-- Trigger 9 : Validate Admission Dates (UPDATE)
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_admission_update $$

CREATE TRIGGER trg_validate_admission_update
BEFORE UPDATE
ON admission
FOR EACH ROW
BEGIN

    IF NEW.discharge_date IS NOT NULL
       AND NEW.discharge_date < NEW.admission_date THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Discharge date cannot be before admission';

    END IF;

END $$


-- ==========================================================
-- Trigger 10 : Prevent Future DOB
-- ==========================================================

DROP TRIGGER IF EXISTS trg_validate_patient_dob $$

CREATE TRIGGER trg_validate_patient_dob
BEFORE INSERT
ON patient
FOR EACH ROW
BEGIN

    IF NEW.date_of_birth > CURDATE() THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT='Date of birth cannot be in the future';

    END IF;

END $$

DELIMITER ;