-- Create the table unique_id if i doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
		id INT DEFAULT ! UNIQUE,
		name VARCHAR(256)
		);
-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;
