-- Create the table force_name if it doesnt exist
CREATE TABLE IF NOT EXISTS force_name (
		id INT,
		name VARCHAR(256) NOT NULL
		);

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;
