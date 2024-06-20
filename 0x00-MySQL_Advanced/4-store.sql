-- A SQL script that creates a trigger to decrease the quantity
-- of an item after adding a new order.
CREATE TRIGGER decrease_quantity
AFTER
INSERT ON orders FOR EACH ROW
UPDATE itmes
SET quantity = quantity - NEW.number
WHERE NEW.item_name;
