-- Scripts that lists all records of second_table in MYSQL

SELECT name, score FROM second_table WHERE name IS NOT NULL ORDER BY score DESC; 
