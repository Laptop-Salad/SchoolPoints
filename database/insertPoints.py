import sqlite3
from sqlite3 import Error


conn = sqlite3.connect("../school.db")
cursor = conn.cursor()

# Delete all existing records from points
#cursor.execute("DELETE FROM points WHERE 1=1")

# Drop points table
#cursor.execute("DROP TABLE points")

# Changed points db structure in db.py


# cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
# VALUES (1, 1, 'Is very quiet and doesnt ask for my help or attention ever', 10, 'B');
#
# """)
#
# cursor.execute("""INSERT INTO points(studentid, teacherid, comment, points, pointsTo)
# VALUES(1, 2, 'Doesnt sit still and not speak', -10, 'B');
#
# """)

print("Records added to Database")
conn.commit()
conn.close()

