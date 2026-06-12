# Student Management System

## Overview

Student Management System is a web-based application developed using python Flask and MySQL. It allows administrators and faculty members to manage student records efficiently through a user-friendly interface.

The system provides secure authentication, student record management, faculty management, and administrative controls for educational institutions.

---

## Features

### Authentication

* Admin Login
* Admin Registration
* Faculty Login
* Faculty Registration
* Session Management
* Logout Functionality

### Student Management

* Add Student
* View Students
* Update Student Details
* Delete Student Records
* Search Students
* Manage Student Information

### Faculty Management

* Faculty Registration
* Faculty Login
* Faculty Dashboard
* View Student Records

### Admin Features

* Manage Students
* Edit Student Information
* Delete Student Information
* Manage Faculty Accounts
* Full Administrative Access

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* Jinja2 Templates

### Backend

* Python
* Flask Framework

### Database

* MySQL

### Tools

* Visual Studio Code
* XAMPP / MySQL Server
* Git & GitHub

---

## Project Structure

student_management_system/

├── app.py

├── database.sql

├── templates/

│ ├── login.html

│ ├── register.html

│ ├── faculty_login.html

│ ├── faculty_register.html

│ ├── dashboard.html

│ ├── students.html

│ ├── add_student.html

│ ├── edit_student.html

│ └── faculty_dashboard.html

├── static/

│ ├── css/

│ └── images/

└── README.md

---


## Installation

### 1. Clone Repository

```bash
git clone https://github.com/Uday5D7/student_management_system.git
```

### 2. Navigate to Project

```bash
cd student-management-system
```

### 3. Install Dependencies

```bash
pip install flask
pip install flask-mysqldb
pip install mysqlclient
```

### 4. Configure Database

Update MySQL credentials in app.py:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'student_management'
```

### 5. Run Application

```bash
python app.py
```

### 6. Open Browser

```text
http://127.0.0.1:5000
```

---

## Available Routes

| Route                | Description          |
| -------------------- | -------------------- |
| /                    | Home Page            |
| /login               | Admin Login          |
| /register            | Admin Registration   |
| /faculty_login       | Faculty Login        |
| /faculty_register    | Faculty Registration |
| /dashboard           | Admin Dashboard      |
| /faculty_dashboard   | Faculty Dashboard    |
| /students            | View Students        |
| /add_student         | Add Student          |
| /edit_student/       | Update Student       |
| /delete_student/     | Delete Student       |
| /logout              | Logout               |

---

### Login Page

* Admin Login
* Faculty Login

### Dashboard

* Student Statistics
* Quick Actions

### Student Management

* Add Student
* Edit Student
* Delete Student
* View Student List

---

## Future Enhancements

* Attendance Management
* Marks Management
* Student Photo Upload
* PDF Report Generation
* CSV Export
* Email Notifications
* Role-Based Access Control
* Responsive Admin Dashboard

---

### Developer

uday

### Technologies Used

Python | Flask | MySQL | Bootstrap

---
