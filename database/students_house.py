from flask import Flask
import sqlite3

app = Flask(__name__)

# Connect to school db
conn = sqlite3.connect("../school.db")

if (not conn):
    print("db couldn't connect successfully")
else:
    print("successfully connected to db")

cursor = conn.cursor()

#
# # Students table
# cursor.execute("""ALTER TABLE students ADD houseid INTEGER;""")
#

# Add houses for students
# cursor.execute("""UPDATE students
# SET houseid = 1
# WHERE id = 1;
# """)
#
# cursor.execute("""UPDATE students
# SET houseid = 2
# WHERE id = 2;
# """)
#
# print("Records added to Database")
# conn.commit()
# conn.close()



