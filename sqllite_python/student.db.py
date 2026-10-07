import sqlite3

# -----------------------------------------
# STEP 1: Connect to SQLite Database
# -----------------------------------------

connection = sqlite3.connect("student.db")

# -----------------------------------------
# STEP 2: Create Cursor
# -----------------------------------------

cursor = connection.cursor()

# -----------------------------------------
# STEP 3: Create Students Table
# -----------------------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
)
""")

connection.commit()

print("Students table created successfully.")


# -----------------------------------------
# STEP 4: Insert Student Records
# -----------------------------------------

students = [
    (101, "Ravi", 19, "BCA", 85.5),
    (102, "Sita", 20, "BCA", 91.0),
    (103, "Kiran", 19, "BCA", 78.5),
    (104, "Anjali", 20, "BCA", 88.0),
    (105, "Rahul", 19, "BCA", 72.5)
]

cursor.executemany("""
INSERT OR IGNORE INTO students
(id, name, age, course, marks)
VALUES (?, ?, ?, ?, ?)
""", students)

connection.commit()

print("Student records inserted successfully.")


# -----------------------------------------
# STEP 5: Display All Students
# -----------------------------------------

print("\n----- ALL STUDENTS -----")

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for student in records:
    print(student)


# -----------------------------------------
# STEP 6: Search Student
# -----------------------------------------

print("\n----- SEARCH STUDENT -----")

student_id = 103

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (student_id,)
)

student = cursor.fetchone()

print("Student:", student)


# -----------------------------------------
# STEP 7: Update Student
# -----------------------------------------

print("\n----- UPDATE STUDENT -----")

cursor.execute("""
UPDATE students
SET marks = ?
WHERE id = ?
""", (90.0, 101))

connection.commit()

print("Marks updated successfully.")


# -----------------------------------------
# STEP 8: Display Updated Record
# -----------------------------------------

cursor.execute(
    "SELECT * FROM students WHERE id = ?",
    (101,)
)

updated_student = cursor.fetchone()

print("Updated Student:", updated_student)


# -----------------------------------------
# STEP 9: Delete Student
# -----------------------------------------

print("\n----- DELETE STUDENT -----")

cursor.execute(
    "DELETE FROM students WHERE id = ?",
    (105,)
)

connection.commit()

print("Student deleted successfully.")


# -----------------------------------------
# STEP 10: Display Final Records
# -----------------------------------------

print("\n----- FINAL STUDENT LIST -----")

cursor.execute("SELECT * FROM students")

records = cursor.fetchall()

for student in records:
    print(student)


# -----------------------------------------
# STEP 11: Count Students
# -----------------------------------------

cursor.execute("SELECT COUNT(*) FROM students")

count = cursor.fetchone()[0]

print("\nTotal Students:", count)


# -----------------------------------------
# STEP 12: Average Marks
# -----------------------------------------

cursor.execute("SELECT AVG(marks) FROM students")

average = cursor.fetchone()[0]

print("Average Marks:", average)


# -----------------------------------------
# STEP 13: Close Connection
# -----------------------------------------

connection.close()

print("\nDatabase connection closed.")