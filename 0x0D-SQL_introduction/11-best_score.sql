-- a script that lists all records with a score >= 10 in the table second_table
SELECT score, name from second_table WHERE score >= 10 AND ORDER BY score DESC;
