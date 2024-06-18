# Student Database Management System
# Introduction
The Student Management System is a Python-based application designed to manage 
student information and academic results. 
It allows users to perform various operations such as adding students, 
recording results, displaying course catalog, and more. 
The system interacts with a MySQL database to store and retrieve data.
# Python code Documentation
1. Overview
The Python code consists of functions to handle different functionalities of the Student Management System.
It includes functions for displaying course catalogs, adding students, recording results, searching students,
updating student information, and more. The application provides a menu-driven interface for user interaction.

2. Functions
Here 'prn' means Permanent Registration Number
2.1 display_courses(cursor).
2.2 add_student(cursor).
2.3 add_result(cursor).
2.4 display_results_by_prn(cursor, prn).
2.5 search_student_by_prn(cursor, prn).
2.6 display_students_by_course(cursor, course_id).
2.7 delete_student_by_prn(cursor, prn).
2.8 update_student_info(cursor).
2.9 display_all_students(cursor).
2.10 delete_all_students(cursor).

4. Menu Function
The menu() function provides a menu-driven interface for users to interact with the
Student Management System. It presents various options to the user,
allowing them to perform different operations on student data.

5. Integration with MySQL
The Python code integrates with a MySQL database to store and
retrieve student information and academic results.
It establishes a connection to the database using the mysql.connector
module and utilizes cursor objects to execute SQL queries.

6. Error Handling
The Python code includes error-handling mechanisms to manage
exceptions that may occur during database operations.
It catches MySQL errors and provides appropriate error messages to the user.

7. Modules Used
7.1 mysql.connector: This module is used to connect Python programs with MySQL databases.
  It provides an interface for working with MySQL databases by executing SQL queries, fetching data,
  and managing database connections.

7.2 tabulate: The tabulate module is used to format tabular data in a visually appealing way. 
  It simplifies the process of displaying data in tabular format by providing functions to 
  create tables with headers and align data neatly.

# MySQL Query Documentation
1. Overview
The MySQL queries file contains SQL statements to create tables for storing student
data, populate the tables with sample data and perform various database operations.

2. Table Creation
2.1 Course Table: Stores information about different courses offered.
2.2 Student Table: Stores details of students enrolled in courses.
2.3 Result Table: Records academic results of students for different courses.

3. Data Population
The MySQL queries file inserts sample data into the course table to populate
it with information about different courses.

4. Queries
4.1 Select Queries: Retrieve information from the database, including the course catalog,
student details, and academic results.
4.2 Insert Queries: Add new records to the student and results from tables to store
student information and academic results.
4.3 Update Queries: Update existing records in the student table to modify
student information.
4.4 Delete Queries: Remove records from the student table based on the PRN of
the student.

5. Constraints
The MySQL queries define foreign key constraints between the student and course tables
to enforce referential integrity. These constraints ensure that only valid course IDs
are assigned to students.
