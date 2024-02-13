-- a script that lists the number of records with the same score in the table second_table
SELECT COUNT(*) AS number
FROM (SELECT DISTINCT score FROM second_table)
ORDER BY number DESC;
