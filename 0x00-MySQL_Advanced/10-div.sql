-- 10. Safe divide
-- Function to divide or return 0 if divisor is zero

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;
