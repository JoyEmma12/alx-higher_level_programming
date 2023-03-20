-- Creates database and table that is unique, auto generated , foreign key and can't be null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
		id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
		state_id INT NOT NULL,
		name VARCHAR(256) NOT NULL,
		FOREIGN KEY (state_id) REFERENCES states(id)
);
