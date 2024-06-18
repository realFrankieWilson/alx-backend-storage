-- A SQL script that creates a table users
-- id: integer, never null, auto increament and primary key
-- email: string(255)
-- name: string(255);
CREATE TABLE if NOT EXISTS users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(2455)
);
