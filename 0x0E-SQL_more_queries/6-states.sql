-- Creates database and table that can be unique, auto generated, cant be null and is a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
		id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL,
		name VARCHAR(256) NOT NULL
);
