-- Create the table id_not_null if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
		id INT DEFAULT 1,
		name VARCHAR(256)
		);
-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;
