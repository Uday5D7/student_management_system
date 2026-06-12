CREATE DATABASE student_management;

USE student_management;


CREATE TABLE admins (
    id INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id INT  PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'student',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE students (
    id INT  PRIMARY KEY,
    student_id VARCHAR(50),
    name VARCHAR(100),
    gender VARCHAR(20),
    dob DATE,
    email VARCHAR(100),
    phone VARCHAR(20),
    department VARCHAR(100),
    address TEXT
);

INSERT INTO admins(username,password)
VALUES('admin','admin123');