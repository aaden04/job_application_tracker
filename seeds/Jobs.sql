DROP TABLE IF EXISTS applications;
DROP SEQUENCE IF EXISTS aplications_id_seq;
DROP TABLE IF EXISTS progress;
DROP SEQUENCE IF EXISTS progress_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS applications_id_seq;
CREATE TABLE applications (id SERIAL PRIMARY KEY, 
company VARCHAR(255), title VARCHAR(255), 
location VARCHAR(255), salary INTEGER, date_applied DATE

);

CREATE SEQUENCE IF NOT EXISTS progress_id_seq;
CREATE TABLE progress (id SERIAL PRIMARY KEY, status VARCHAR(255), interview_date DATE,
decison VARCHAR(255), applications_id INTEGER

); 

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (id SERIAL PRIMARY KEY, name VARCHAR(225), 
email VARCHAR(225), password VARCHAR(225)

);


INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Google', 'Software Engineer', 'London', 100000, '2023-01-01');
INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Microsoft', 'Software Engineer', 'London', 100000, '2023-01-01');
INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Amazon', 'Software Engineer', 'London', 100000, '2023-01-01');
INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Facebook', 'Software Engineer', 'London', 100000, '2023-01-01');
INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Apple', 'Software Engineer', 'London', 100000, '2023-01-01');
INSERT INTO applications (company, title, location, salary, date_applied) VALUES ('Makers', 'DevOps Engineer', 'Watford', 100000, '2023-01-01');



INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 1);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 2);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 3);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 4);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 5);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 6);
INSERT INTO progress (status, interview_date, decison, applications_id) VALUES ('Applied', '2023-01-01', 'Accepted', 7);



INSERT INTO users (name, email, password) VALUES ('John', 'john@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Jane', 'jane@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Jack', 'jack@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Jill', 'jill@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Joe', 'joe@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Jenny', 'jenny@gmail.com', 'password');