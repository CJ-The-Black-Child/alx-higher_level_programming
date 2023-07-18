-- Displays the avg temp by city ordered by temp (desc)
SELECT city, AVG(temperatute) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
