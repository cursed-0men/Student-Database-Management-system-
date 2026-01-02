# 🎓 Student Database Management System

## 📌 Introduction

The **Student Database Management System** is a Python-based application designed to manage student information and academic results.

It allows users to perform various operations such as:

- Adding students  
- Recording academic results  
- Displaying the course catalog  
- Searching and updating student records  

The system interacts with a **MySQL database** to store and retrieve all data efficiently.

---

## 📄 Python Code Documentation

### 1️⃣ Overview

The Python code consists of multiple functions that handle the core functionalities of the Student Management System.

It provides a **menu-driven interface** for user interaction and supports:

- Student registration  
- Result management  
- Course-wise student display  
- Record updates and deletions  

---

### 2️⃣ Functions

> **Note:** `PRN` stands for **Permanent Registration Number**

#### 2.1 Core Functions

- `display_courses(cursor)`  
- `add_student(cursor)`  
- `add_result(cursor)`  
- `display_results_by_prn(cursor, prn)`  
- `search_student_by_prn(cursor, prn)`  
- `display_students_by_course(cursor, course_id)`  
- `delete_student_by_prn(cursor, prn)`  
- `update_student_info(cursor)`  
- `display_all_students(cursor)`  
- `delete_all_students(cursor)`

---

### 4️⃣ Menu Function

The `menu()` function provides a **menu-driven interface** that allows users to interact with the system.

It presents various options such as:

- Adding or deleting students  
- Viewing results  
- Searching records  
- Updating student information  

---

### 5️⃣ Integration with MySQL

The application integrates with a **MySQL database** using the `mysql.connector` module.

It:
- Establishes database connections  
- Uses cursor objects to execute SQL queries  
- Fetches and manipulates student and result data  

---

### 6️⃣ Error Handling

The Python code includes **robust error-handling mechanisms** to manage exceptions that may occur during database operations.

- Catches MySQL-related errors  
- Displays meaningful error messages to the user  

---

### 7️⃣ Modules Used

#### 7.1 `mysql.connector`

- Connects Python programs with MySQL databases  
- Executes SQL queries  
- Manages database connections and transactions  

#### 7.2 `tabulate`

- Formats tabular data in a visually appealing way  
- Helps display query results neatly with headers and alignment  

---

## 🗄️ MySQL Query Documentation

### 1️⃣ Overview

The MySQL queries file contains SQL statements used to:

- Create database tables  
- Insert sample data  
- Perform CRUD (Create, Read, Update, Delete) operations  

---

### 2️⃣ Table Creation

- **Course Table**  
  Stores information about different courses offered  

- **Student Table**  
  Stores student details and enrolled course information  

- **Result Table**  
  Records academic results of students  

---

### 3️⃣ Data Population

The queries insert **sample data** into the Course table to populate it with predefined course information.

---

### 4️⃣ Queries

#### 4.1 Select Queries
- Retrieve course catalogs  
- Fetch student details  
- Display academic results  

#### 4.2 Insert Queries
- Add new students  
- Insert academic results  

#### 4.3 Update Queries
- Modify existing student records  

#### 4.4 Delete Queries
- Remove student records using PRN  

---

### 5️⃣ Constraints

The MySQL queries define **foreign key constraints** between the Student and Course tables to ensure **referential integrity**.

These constraints ensure:
- Only valid course IDs can be assigned to students  
- Data consistency across tables  
