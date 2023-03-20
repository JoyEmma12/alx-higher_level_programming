-- Creates table with default value 1 that must be unique
CREATE TABLE IF NOT EXISTS unique_id(
		id INT DEFAULT 1 UNIQUE,
		name VARCHAR(256)
);
