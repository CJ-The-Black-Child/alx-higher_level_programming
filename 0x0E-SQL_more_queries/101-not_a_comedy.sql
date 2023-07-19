-- Use the database `hbtn_0d_tvshows`
USE `hbtn_0d_tvshows`;

-- List all shows without the genre 'Comedy'
SELECT `title`
FROM `tv_shows`
WHERE `id` NOT IN (
	SELECT `tv_show_id`
	FROM `tv_show_genres`
	WHERE `genre_id` = (
		SELECT `id`
		FROM `tv_genres`
		WHERE `name` = 'Comedy'
		)
	)
ORDER BY `title` ASC;
