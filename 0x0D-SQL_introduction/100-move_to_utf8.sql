-- Convert hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Covert first_table table to UTF8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode ci;

-- Convert name field in first_table to UTF8
ALTER TABLE first_table MODIFY column name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci
