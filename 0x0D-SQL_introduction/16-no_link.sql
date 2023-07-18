-- List all recorods with a name and order by descening order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
