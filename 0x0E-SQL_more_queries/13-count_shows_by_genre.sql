-- Use the database `hbtn_0d_tvshows`
USE `hbtn_0d_tvshows`;

-- List all genres and the number of shows linked to each genre
SELECT `tv_genres`.`genre` AS `genre`, COUNT(`tv_show_genres`.`tv_show_id`) AS `number_of_shows`
FROM `tv_genres`
JOIN `tv_show_genres` ON `tv_genres`.`id` = `tv_show_genre`.`genre_id`
GROUP BY `tv_genres`.`genre`
ORDER BY `number_of_shows` DESC;
