USE hospital_analytics;

SET GLOBAL event_scheduler = ON;

DELIMITER $$

-- ==========================================================
-- Event 1 : Daily Executive KPI Refresh
-- ==========================================================

DROP EVENT IF EXISTS ev_daily_kpi_refresh $$

CREATE EVENT ev_daily_kpi_refresh
ON SCHEDULE EVERY 1 DAY
STARTS CURRENT_TIMESTAMP
DO
BEGIN

    CALL sp_executive_kpi_dashboard();

END $$


-- ==========================================================
-- Event 2 : Weekly Department Revenue Report
-- ==========================================================

DROP EVENT IF EXISTS ev_weekly_department_revenue $$

CREATE EVENT ev_weekly_department_revenue
ON SCHEDULE EVERY 1 WEEK
STARTS CURRENT_TIMESTAMP
DO
BEGIN

    CALL sp_department_revenue();

END $$


-- ==========================================================
-- Event 3 : Monthly Revenue Summary
-- ==========================================================

DROP EVENT IF EXISTS ev_monthly_revenue $$

CREATE EVENT ev_monthly_revenue
ON SCHEDULE EVERY 1 MONTH
STARTS CURRENT_TIMESTAMP
DO
BEGIN

    CALL sp_monthly_revenue(NULL);

END $$


-- ==========================================================
-- Event 4 : Monthly Insurance Summary
-- ==========================================================

DROP EVENT IF EXISTS ev_monthly_insurance_summary $$

CREATE EVENT ev_monthly_insurance_summary
ON SCHEDULE EVERY 1 MONTH
STARTS CURRENT_TIMESTAMP
DO
BEGIN

    CALL sp_insurance_summary();

END $$


-- ==========================================================
-- Event 5 : Weekly Bed Occupancy Report
-- ==========================================================

DROP EVENT IF EXISTS ev_weekly_bed_occupancy $$

CREATE EVENT ev_weekly_bed_occupancy
ON SCHEDULE EVERY 1 WEEK
STARTS CURRENT_TIMESTAMP
DO
BEGIN

    CALL sp_bed_occupancy();

END $$

DELIMITER ;