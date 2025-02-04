DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS progress;

CREATE SEQUENCE IF NOT EXISTS applications_id_seq;
CREATE TABLE applications (id SERIAL PRIMARY KEY, 
company VARCHAR(255), title VARCHAR(255), 
location VARCHAR(255), salary INTEGER, date_applied DATE);

CREATE SEQUENCE IF NOT EXISTS progress_id_seq;
CREATE TABLE progress (id SERIAL PRIMARY KEY,

); 