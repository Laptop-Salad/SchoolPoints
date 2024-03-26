# Reuse this script for inserting new students - replace anything in values or referencing a studentid.
import sqlite3
from sqlite3 import Error


conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# create student
cursor.execute("""INSERT INTO students(username, password)
   VALUES ("Jacob", "Password1!")""")

### Grades points
cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
VALUES (3, 1, 'Doesnt die, very good', 1, 'B');

""")

### Grades points
cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
VALUES (3, 1, 'Doesnt know what a dog is but otherwise very good student', 1, 'G');

""")

### Attendance points
cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
VALUES (3, 1, 'Always comes to class on time', 10, 'A');

""")

### Others points
cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
VALUES (3, 1, 'Smiled at me', 100, 'O');

""")

# Add student to houses table
cursor.execute("""INSERT INTO houses (studentid, housename)
VALUES (3, "Red Rabbits")""")

print("New student added!")
conn.commit()
conn.close()
