-- SQL script that creates a stored procedure computeAverageScoreForUser that computes and store the average score for a student.

DELIMITER $$

DROP PROCEDURE IF EXISTS computeAverageScoreForUser;
CREATE PROCEDURE computeAverageScoreForUser (In user_id INT)
BEGIN
  UPDATE users
  SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
  WHERE id = user_id;
END$$

DELIMITER ;
