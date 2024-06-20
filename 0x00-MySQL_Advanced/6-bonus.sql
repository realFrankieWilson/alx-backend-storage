-- A SQL script that Creates a stored procedure AddBonus that adds a new correction for a student.

DELIMITER $$

CREATE PROCEDURE AddBonus(
  IN user_id INTERGER,
  IN project_name VARCHAR(255),
  IN score INTERGER
)
BEGIN
  INSERT INTO project(name)
  SELECT project_name FROM DUAL
  WHERE NOT EXISTS(SELECT * FROM projects WHERE name = project_name LIMIT 1);

  INSERT INTO corrections(user_id, project_id, score)
  VALUES(user_id, (SELECT id FROM projects WHERE name = project_name), score);
END$$
DELIMITER;
