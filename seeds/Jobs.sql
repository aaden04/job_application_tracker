DROP TABLE IF EXISTS progress;
DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS applications_id_seq;
DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(225),
    email VARCHAR(225), 
    password VARCHAR(225)
);

CREATE SEQUENCE IF NOT EXISTS applications_id_seq;
CREATE TABLE applications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    company VARCHAR(255),
    title VARCHAR(255),
    location VARCHAR(255),
    salary INTEGER,
    date_applied DATE,
    status VARCHAR(255) DEFAULT 'Applied',
    interview_date DATE,
    decision VARCHAR(255) DEFAULT 'Pending'
);

-- Insert 5 users
INSERT INTO users (name, email, password) VALUES ('John', 'john@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Jane', 'jane@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Mike', 'mike@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Sarah', 'sarah@gmail.com', 'password');
INSERT INTO users (name, email, password) VALUES ('Alex', 'alex@gmail.com', 'password');

-- Jobs for John (user_id = 1)
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (1, 'Google', 'Software Engineer', 'London', 100000, '2024-01-01', 'Applied', '2024-01-15', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (1, 'Amazon', 'Full Stack Developer', 'Manchester', 95000, '2024-01-05', 'Interview Scheduled', '2024-01-20', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (1, 'Microsoft', 'Backend Developer', 'Birmingham', 90000, '2024-01-10', 'Under Review', '2024-02-01', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (1, 'Meta', 'Frontend Developer', 'London', 85000, '2024-01-15', 'Offer', '2024-01-25', 'Accepted');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (1, 'Netflix', 'DevOps Engineer', 'Leeds', 92000, '2024-01-20', 'Applied', '2024-02-05', 'Pending');

-- Jobs for Jane (user_id = 2)
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (2, 'Apple', 'iOS Developer', 'London', 98000, '2024-01-02', 'Interview Scheduled', '2024-01-18', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (2, 'Spotify', 'Backend Engineer', 'Manchester', 88000, '2024-01-07', 'Applied', '2024-01-22', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (2, 'Twitter', 'Full Stack Engineer', 'Edinburgh', 86000, '2024-01-12', 'Under Review', '2024-02-03', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (2, 'LinkedIn', 'Frontend Engineer', 'Glasgow', 84000, '2024-01-17', 'Rejected', '2024-01-27', 'Rejected');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (2, 'Adobe', 'Software Developer', 'Bristol', 89000, '2024-01-22', 'Applied', '2024-02-07', 'Pending');

-- Jobs for Mike (user_id = 3)
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (3, 'Salesforce', 'Cloud Engineer', 'London', 95000, '2024-01-03', 'Offer', '2024-01-19', 'Accepted');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (3, 'Oracle', 'Database Engineer', 'Liverpool', 87000, '2024-01-08', 'Applied', '2024-01-23', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (3, 'IBM', 'Systems Engineer', 'Cardiff', 83000, '2024-01-13', 'Interview Scheduled', '2024-02-04', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (3, 'Intel', 'Hardware Engineer', 'Belfast', 91000, '2024-01-18', 'Under Review', '2024-01-28', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (3, 'AMD', 'Software Engineer', 'Newcastle', 88000, '2024-01-23', 'Applied', '2024-02-08', 'Pending');

-- Jobs for Sarah (user_id = 4)
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (4, 'Uber', 'Mobile Developer', 'London', 93000, '2024-01-04', 'Under Review', '2024-01-20', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (4, 'Deliveroo', 'Backend Developer', 'Brighton', 85000, '2024-01-09', 'Applied', '2024-01-24', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (4, 'Just Eat', 'Frontend Developer', 'Southampton', 82000, '2024-01-14', 'Interview Scheduled', '2024-02-05', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (4, 'Ocado', 'DevOps Engineer', 'Oxford', 89000, '2024-01-19', 'Rejected', '2024-01-29', 'Rejected');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (4, 'Tesco', 'Software Developer', 'Cambridge', 86000, '2024-01-24', 'Applied', '2024-02-09', 'Pending');

-- Jobs for Alex (user_id = 5)
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (5, 'Sky', 'Cloud Developer', 'London', 91000, '2024-01-05', 'Offer', '2024-01-21', 'Accepted');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (5, 'BBC', 'Full Stack Developer', 'Reading', 84000, '2024-01-10', 'Applied', '2024-01-25', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (5, 'ITV', 'Software Engineer', 'Sheffield', 81000, '2024-01-15', 'Interview Scheduled', '2024-02-06', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (5, 'Channel 4', 'Frontend Engineer', 'Leeds', 87000, '2024-01-20', 'Under Review', '2024-01-30', 'Pending');
INSERT INTO applications (user_id, company, title, location, salary, date_applied, status, interview_date, decision) 
VALUES (5, 'BT', 'Backend Engineer', 'Nottingham', 85000, '2024-01-25', 'Applied', '2024-02-10', 'Pending');