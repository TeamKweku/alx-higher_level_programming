-- select all records ordering by score in ascending order
SELECT score, name
FROM second_table 
WHERE score >= 10
ORDER BY score DESC;
