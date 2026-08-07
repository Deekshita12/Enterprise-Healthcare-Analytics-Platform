USE hospital_analytics;

DELIMITER $$

-- ==========================================================
-- Enterprise Healthcare Operations Intelligence Platform
-- 10_functions.sql
-- ==========================================================

-- ==========================================================
-- Function 1 : Calculate Patient Age
-- ==========================================================

DROP FUNCTION IF EXISTS fn_patient_age $$

CREATE FUNCTION fn_patient_age
(
    p_dob DATE
)
RETURNS INT
DETERMINISTIC

BEGIN

    RETURN TIMESTAMPDIFF
    (
        YEAR,
        p_dob,
        CURDATE()
    );

END $$

-- ==========================================================
-- Function 2 : Length of Stay
-- ==========================================================

DROP FUNCTION IF EXISTS fn_length_of_stay $$

CREATE FUNCTION fn_length_of_stay
(
    p_admission DATE,
    p_discharge DATE
)
RETURNS INT
DETERMINISTIC

BEGIN

    RETURN DATEDIFF
    (
        IFNULL(p_discharge,CURDATE()),
        p_admission
    );

END $$

-- ==========================================================
-- Function 3 : Net Revenue
-- ==========================================================

DROP FUNCTION IF EXISTS fn_net_revenue $$

CREATE FUNCTION fn_net_revenue
(
    gross DECIMAL(12,2),
    discount DECIMAL(12,2),
    tax DECIMAL(12,2)
)
RETURNS DECIMAL(12,2)
DETERMINISTIC

BEGIN

    RETURN gross-discount+tax;

END $$

-- ==========================================================
-- Function 4 : Insurance Percentage
-- ==========================================================

DROP FUNCTION IF EXISTS fn_insurance_percentage $$

CREATE FUNCTION fn_insurance_percentage
(
    insurance DECIMAL(12,2),
    total DECIMAL(12,2)
)
RETURNS DECIMAL(8,2)
DETERMINISTIC

BEGIN

    IF total=0 THEN
        RETURN 0;
    END IF;

    RETURN ROUND
    (
        insurance*100/total,
        2
    );

END $$

-- ==========================================================
-- Function 5 : Bed Occupancy Percentage
-- ==========================================================

DROP FUNCTION IF EXISTS fn_occupancy_percentage $$

CREATE FUNCTION fn_occupancy_percentage
(
    occupied INT,
    total INT
)
RETURNS DECIMAL(8,2)
DETERMINISTIC

BEGIN

    IF total=0 THEN
        RETURN 0;
    END IF;

    RETURN ROUND
    (
        occupied*100/total,
        2
    );

END $$

DELIMITER ;
DELIMITER $$

-- ==========================================================
-- Function 6 : Patient Age Group
-- ==========================================================

DROP FUNCTION IF EXISTS fn_age_group $$

CREATE FUNCTION fn_age_group
(
    p_age INT
)
RETURNS VARCHAR(30)
DETERMINISTIC

BEGIN

    RETURN
    CASE

        WHEN p_age < 18 THEN 'Child'

        WHEN p_age BETWEEN 18 AND 35 THEN 'Young Adult'

        WHEN p_age BETWEEN 36 AND 55 THEN 'Adult'

        WHEN p_age BETWEEN 56 AND 75 THEN 'Senior Adult'

        ELSE 'Geriatric'

    END;

END $$


-- ==========================================================
-- Function 7 : Revenue Category
-- ==========================================================

DROP FUNCTION IF EXISTS fn_revenue_category $$

CREATE FUNCTION fn_revenue_category
(
    p_amount DECIMAL(12,2)
)
RETURNS VARCHAR(20)
DETERMINISTIC

BEGIN

    RETURN
    CASE

        WHEN p_amount >= 75000 THEN 'Very High'

        WHEN p_amount >= 50000 THEN 'High'

        WHEN p_amount >= 25000 THEN 'Medium'

        ELSE 'Low'

    END;

END $$


-- ==========================================================
-- Function 8 : Bill Outstanding
-- ==========================================================

DROP FUNCTION IF EXISTS fn_outstanding_amount $$

CREATE FUNCTION fn_outstanding_amount
(
    total DECIMAL(12,2),
    insurance DECIMAL(12,2)
)
RETURNS DECIMAL(12,2)
DETERMINISTIC

BEGIN

    RETURN total-insurance;

END $$


-- ==========================================================
-- Function 9 : Bed Availability
-- ==========================================================

DROP FUNCTION IF EXISTS fn_bed_availability $$

CREATE FUNCTION fn_bed_availability
(
    occupied INT,
    total INT
)
RETURNS INT
DETERMINISTIC

BEGIN

    RETURN total-occupied;

END $$


-- ==========================================================
-- Function 10 : Risk Category
-- ==========================================================

DROP FUNCTION IF EXISTS fn_risk_category $$

CREATE FUNCTION fn_risk_category
(
    p_los INT
)
RETURNS VARCHAR(20)
DETERMINISTIC

BEGIN

    RETURN
    CASE

        WHEN p_los >= 15 THEN 'Critical'

        WHEN p_los >= 10 THEN 'High'

        WHEN p_los >= 5 THEN 'Medium'

        ELSE 'Low'

    END;

END $$

DELIMITER ;