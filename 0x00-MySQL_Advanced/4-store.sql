-- 4. Buy buy buy
-- Create trigger to decrement item quantity on new order

DELIMITER $$

CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
