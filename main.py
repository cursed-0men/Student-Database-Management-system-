import mysql.connector
from tabulate import tabulate

# connection to database.
mydb = mysql.connector.connect(
      host = 'HOSTNAME',
      user = 'YOUR_USERNAME',
      password = 'YOUR_PASSWORD',
      database = 'YOUR_DATABASE_NAME'
      )

# cursor object -> for fetching results from connected MySQL database.
cursor = mydb.cursor()


# displaying course catalog
def display_courses(cursor):
      sql = "SELECT * FROM course"
      cursor.execute(sql) # executing above query)
      courses = cursor.fetchall() # fetch all records
      # displaying catalog
      print("+----------------------+")
      print("|    Course Catalog    |")
      print("+----------------------+")

      headers =  ["Course ID", "Course Name", "Duration (Years)"]
      print(tabulate(courses, headers=headers, tablefmt="grid")) 


# adding student 
def add_student(cursor):
      name = input("Name : ")
      age = int(input("Age : "))
      contact_no = input("Contact No. : ")
      email = input("Email : ")
      display_courses(cursor)
      course_id = int(input("Course ID(to enroll) : "))
      # query to insert student data
      # %s is the placeholder for attributes of student.
      sql = "INSERT INTO student(name,age,contact_no,email,course_id) VALUES (%s, %s, %s, %s, %s)"
      # Values to insert
      values = (name, age, contact_no, email, course_id)
      try:
          # Execute the query
          cursor.execute(sql, values)
          # Commit the transaction
          mydb.commit()
          # Fetch the last inserted PRN
          cursor.execute("SELECT LAST_INSERT_ID()")
          prn = cursor.fetchone()[0]
          print(f"Student added successfully with PRN: {prn}")
      except mysql.connector.Error as err:
          print(f"Error: {err}")

# add result
def add_result(cursor):
      prn_no = int(input("PRN : "))
      grade = input("Grade : ")
      marks = int(input("Marks (out of 100) : "))
      course_id = int(input("Course ID : "))
      remark = input("Remark (PASS/FAIL) : ")

      sql = "INSERT INTO result (prn_no, grade, marks, course_id,remark) VALUES (%s, %s, %s, %s)"
      values = (prn_no, grade, marks, course_id, remark)
      cursor.execute(sql,values)
      mydb.commit()
      print("Result added Successfully...")

# display results
def display_results_by_prn(cursor, prn):
    # SQL query to fetch results for the specified student by PRN number
    sql = """
    SELECT course.course_name, result.grade, result.marks, result.remark
    FROM result
    INNER JOIN course ON result.course_id = course.course_id
    WHERE result.student_prn = %s;
    """
    # Execute the query
    cursor.execute(sql, (prn,))
    # Fetch all records
    results = cursor.fetchall()
    # Display results for the specified student
    if results:
        print(f"Results for PRN : {prn}:")
        headers = ["Course Name", "Grade", "Marks", "Remark"]
        print(tabulate(results, headers=headers, tablefmt="grid"))
    else:
        print(f"No results found for Student with PRN {prn}.")
      

# search student by prn
def search_student_by_prn(cursor, prn):
    # SQL query to fetch student details by PRN
    sql = """
    SELECT *
    FROM student
    WHERE prn_no = %s;
    """
    # Execute the query
    cursor.execute(sql, (prn,))
    # Fetch the first record
    student = cursor.fetchone()
    # Display student details if found, otherwise print message
    if student:
        print("Student Details:")
        headers = ["PRN", "Name", "Age", "Contact Number", "Email", "Course ID"]
        print(tabulate([student], headers=headers, tablefmt="grid"))
    else:
        print(f"No student found with PRN {prn}.")        


# display students by course
def display_students_by_course(cursor, course_id):
    # SQL query to fetch student details by course ID
    sql = """
    SELECT student.prn_no, student.name, student.age, student.contact_no, student.email
    FROM student
    WHERE student.course_id = %s;
    """
    # Execute the query
    cursor.execute(sql, (course_id,))
    # Fetch all records
    students = cursor.fetchall()
    # Display student details if found, otherwise print message
    if students:
        print(f"Students in Course ID {course_id}:")
        headers = ["PRN", "Name", "Age", "Contact Number", "Email"]
        print(tabulate(students, headers=headers, tablefmt="grid"))
    else:
        print(f"No students found in Course ID {course_id}.")


# delete student info by PRN
def delete_student_by_prn(cursor, prn):
    # SQL query to delete student by PRN
    sql = "DELETE FROM student WHERE prn_no = %s;"
    # Execute the query
    cursor.execute(sql, (prn,))
    # Commit the transaction
    mydb.commit()
    # Check if any row was affected by the delete operation
    if cursor.rowcount > 0:
        print(f"Student with PRN {prn} deleted successfully.")
    else:
        print(f"No student found with PRN {prn}.")

# update student info
def update_student_info(cursor):
    prn = int(input("Enter PRN number of the student to update: "))
    # Check if the student exists
    sql_check = "SELECT * FROM student WHERE prn_no = %s"
    cursor.execute(sql_check, (prn,))
    student = cursor.fetchone()
    if not student:
        print(f"No student found with PRN {prn}.")
        return
    
    print("Current Student Details:")
    headers = ["PRN", "Name", "Age", "Contact Number", "Email", "Course ID"]
    print(tabulate([student], headers=headers, tablefmt="grid"))
    
    # Options menu for updating student fields
    print("\nOptions:")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Contact Number")
    print("4. Update Email")
    print("5. Update Course ID")
    print("6. Cancel")
    choice = input("Enter your choice: ")

    if choice == "6":
        print("Update cancelled.")
        return

    fields = ["name", "age", "contact_no", "email", "course_id"]
    if choice.isdigit() and 1 <= int(choice) <= 5:
        field = fields[int(choice) - 1]
        new_value = input(f"Enter new {field.replace('_', ' ').title()}: ")
        if new_value:
            sql_update = f"UPDATE student SET {field} = %s WHERE prn_no = %s"
            cursor.execute(sql_update, (new_value, prn))
            mydb.commit()
            print(f"Student with PRN {prn} updated successfully.")
        else:
            print("Value cannot be empty.")
    else:
        print("Invalid choice.")

# display all students
def display_all_students(cursor):
    try:
        # SQL query to fetch all students
        sql = "SELECT * FROM student"
        # Execute the query
        cursor.execute(sql)
        # Fetch all records
        students = cursor.fetchall()
        # Display student details if found, otherwise print message
        if students:
            print("All Students:")
            headers = ["PRN", "Name", "Age", "Contact Number", "Email", "Course ID"]
            print(tabulate(students, headers=headers, tablefmt="grid"))
        else:
            print("No students found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# deleting all students
def delete_all_students(cursor):
    confirm = input("Are you sure you want to delete all students? (y/n): ").lower()
    if confirm == 'y':
        sql = "DELETE FROM student"
        cursor.execute(sql)
        mydb.commit()
        print("All students deleted successfully.")
    else:
        print("Deletion cancelled.")


def menu():
    while True:
        print("\n")
        print("\033[92m          SELECT OPTION           \033[0m")
        print("\033[92m+--------------------------------+\033[0m")
        print("\033[92m| 1. Display Course Catalog      |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 2. Add Student                 |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 3. Add Result                  |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 4. Display Results by PRN      |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 5. Search Student by PRN       |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 6. Display Students by Course  |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 7. Delete Student by PRN       |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 8. Update Student Info         |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 9. Display All Students        |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 10. Delete All Students        |\033[0m")
        print("\033[92m|--------------------------------|\033[0m")
        print("\033[92m| 11. Exit                       |\033[0m")
        print("\033[92m+--------------------------------+\033[0m")
        
        choice = input("Enter your choice : ")

        if choice == "1":
            display_courses(cursor)
        elif choice == "2":
            add_student(cursor)
        elif choice == "3":
            add_result(cursor)
        elif choice == "4":
            prn = int(input("Enter PRN: "))
            display_results_by_prn(cursor, prn)
        elif choice == "5":
            prn = int(input("Enter PRN: "))
            search_student_by_prn(cursor, prn)
        elif choice == "6":
            course_id = int(input("Enter Course ID: "))
            display_students_by_course(cursor, course_id)
        elif choice == "7":
            prn = int(input("Enter PRN: "))
            delete_student_by_prn(cursor, prn)
        elif choice == "8":
            update_student_info(cursor)
        elif choice == "9":
            display_all_students(cursor)
        elif choice == "10":
            delete_all_students(cursor)
        elif choice == "11":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    menu()

