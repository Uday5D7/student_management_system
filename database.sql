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
CREATE TABLE faculty (
    id INT PRIMARY KEY,
    faculty_id VARCHAR(20) UNIQUE,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    department VARCHAR(50),
    password VARCHAR(255)
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