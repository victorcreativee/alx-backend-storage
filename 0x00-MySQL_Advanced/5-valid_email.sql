-- 5. Email validation to sent
-- Trigger to reset valid_email if email changes

DELIMITER $$

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
