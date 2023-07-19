-- Use the database `hbtn_0d_tvshows`
USE `hbtn_0d_tvshows`;

-- Get the genre_id for the show 'Dexter'
SELECT id FROM tv_shows WHERE title = 'Dexter';

-- List all genres not linked to the show 'Dexter'
SELECT `name` FROM `tv_genres`
WHERE `id` NOT IN (
	SELECT `genre_id` FROM `tv_show_genres` WHERE `tv_show_id` = (
		SELECT `id` FROM `tv_shows` WHERE `title` = 'Dexter'
		)
)
ORDER BY `name` ASC;
