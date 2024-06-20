-- A SQL script that creates a trigger to decrease the quantity
-- of an item after adding a new order.
CREATE TRIGGER decrement
AFTER INSERT
ON orders
FOR EACH ROW
UPDATE itmes
UPDATE items SET quantity = quantity - NEW.number WHERE NAME = NEW.item_name;
