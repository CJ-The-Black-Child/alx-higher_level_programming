-- Use the database hbtn_0d_tvshows
USE `hbtn_0d_tvshows`;

-- List all genres of the show Dexter
SELECT `tv_genres`.`name`
FROM `tv_genres`
JOIN `tv_show_genres` ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
JOIN `tv_shows` on `tv_show_genres`.`tv_show_id` = `tv_shows`.`id`
WHERE `tv_shows`.`title` = `Dexter`
ORDER BY `tv_genres`.`name` ASC;
