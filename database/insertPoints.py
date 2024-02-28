import sqlite3
from sqlite3 import Error


conn = sqlite3.connect("../school.db")
cursor = conn.cursor()

# Delete all existing records from points
#cursor.execute("DELETE FROM points WHERE 1=1")

# Drop points table
#cursor.execute("DROP TABLE points")

# Changed points db structure in db.py

# Behavior points
# cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
# VALUES (1, 1, 'Is very quiet and doesnt ask for my help or attention ever', 10, 'B');
#
# """)
#
# cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
# VALUES(1, 2, 'Doesnt sit still and not speak', -10, 'B');
#
# """)


### Grades points
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES (1, 1, 'Doesnt know what a dog is but otherwise very good student', 20, 'G');
##
##""")
##
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES(1, 2, 'Is not too good at english', -5, 'G');
##
##""")
##
##
### Attendance points
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES (1, 1, 'Always comes to class on time', 10, 'A');
##
##""")
##
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES(1, 2, 'Was 34.30 minutes late to class today', -34.3, 'A');
##
##""")
##
##
### Others points
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES (1, 1, 'Smiled at me', 100, 'O');
##
##""")
##
##cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
##VALUES(1, 2, 'Didnt smile at me', -1, 'O');
##
##""")


print("Records added to Database")
conn.commit()
conn.close()

