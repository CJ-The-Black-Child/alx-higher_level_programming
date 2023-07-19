-- Use the database `hbtn_0d_usa`
USE `hbtn_0d_usa`;

-- Find the `state_id` for the state with name `California`
SELECT `id` FROM `state` WHERE `name` = `California`;

-- List all cities of California using a subquery for the `state_id`
SELECT * FROM `cities` WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = `California`) ORDER BY `id` ASC;
