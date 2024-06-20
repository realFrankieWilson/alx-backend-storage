-- A SQl script that creates a trigger for email validation.

DELIMITER $$

CREATE TRIGGER reset_mail
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email != NEW.email THEN
    SET NEW.valid_email = 0;
  END IF;
END$$
DELIMITER ;
