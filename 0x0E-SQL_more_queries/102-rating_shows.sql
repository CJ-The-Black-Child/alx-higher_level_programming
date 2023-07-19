-- Use the database hbtn_0d_tvshows_rate
USE hbtn_0d_tvshows_rate;

-- List all shows by their rating sum
SELECT tv_shows.title, SUM(rating) AS rating_SUM
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
