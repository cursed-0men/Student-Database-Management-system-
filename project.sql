create database if not exists project;
use project;


-- COURSE(branch) TBALE
create table course(
course_id int auto_increment primary key,
course_name varchar(50),
duration_years INT NOT NULL
);


-- ADDING COURSES
INSERT INTO course(course_name, duration_years) VALUES 
('Computer Science and Engineering',4),
('Cyber security',4),
('Civil Engineering',4),
('Robotics',4),
('Mathematics and computing',4),
('Electronics and communication Engineering',4),
('Electrical Engineering',4);


-- STUDENT TABLE
create table student(
prn_no int auto_increment primary key,
name varchar(50) NOT NULL,
age int not null,
contact_no varchar(25) NOT NULL,
email varchar(50) not null,
course_id int not null,
FOREIGN KEY(course_id) REFERENCES course(course_id)
)auto_increment = 200;


-- RESULT TABLE
create table result(
student_prn int NOT NULL,
marks int NOT NULL,
grade varchar(5),
course_id int,
remark varchar(6) NOT NULL,
FOREIGN KEY(student_prn) REFERENCES student(prn_no),
FOREIGN KEY(course_id) REFERENCES course(course_id)
);
