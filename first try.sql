CREATE DATABASE students;
USE students;

CREATE TABLE Course (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);


CREATE TABLE Student (
    id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL, 
    email VARCHAR(100) UNIQUE,
    gender CHAR(1)constraint check(gender in('Male', 'Female')) NOT NULL,
    course_id INT,

    PRIMARY KEY (id),

    
	FOREIGN KEY (course_id) REFERENCES Course(id) ON DELETE CASCADE

);
SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE, TABLE_NAME
FROM information_schema.TABLE_CONSTRAINTS
WHERE TABLE_SCHEMA = 'students' AND TABLE_NAME = 'Student';

