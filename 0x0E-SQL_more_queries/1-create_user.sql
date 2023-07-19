-- Create the user `user_0d_1` if it doesn't exist
CREATE USER
	IF NOT EXISTS `user_0d_1`@`localhost`
	IDENTIFIED BY `user_0d_1_pwd`;

-- Grant all privileges to `user_0d_1` on all databases and tables
GRANT ALL PRIVILEGES
	ON *.*
	TO `user_0d_1`@`localhost`;

-- Flush the privileges to apply changes
FLUSH PRIVILEGES;
