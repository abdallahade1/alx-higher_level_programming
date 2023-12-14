-- script that creates the table unique_id
-- The database name will be passed as an argument of the mysql command
-- If the table unique_id already exists, your script should not fail
-- The unique_id takes a description id INT with the default value 1 and must be unique
-- And name VARCHAR(256)

CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
