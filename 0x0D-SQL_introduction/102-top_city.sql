-- Displays the top 3 cities tempmduting July and August
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP by city
ORDER BY avg_temp DESC
LIMIT 3;
