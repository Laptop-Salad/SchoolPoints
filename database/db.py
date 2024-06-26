from flask import Flask
import sqlite3

app = Flask(__name__)

# Create a db named school db if doesnt exist yet
connection = sqlite3.connect("../school.db")

if (not connection):
    print("db couldn't connect successfully")
else:
    print("successfully connected to db")

cursor = connection.cursor()

# Students table
# cursor.execute("""CREATE TABLE IF NOT EXISTS students
# (id INTEGER PRIMARY KEY, username TEXT, password TEXT)""")

# Teachers table
# cursor.execute("""CREATE TABLE IF NOT EXISTS teachers
# (id INTEGER PRIMARY KEY, username TEXT, password TEXT)""")

# Parents table
# cursor.execute("""CREATE TABLE IF NOT EXISTS parents
# (id INTEGER PRIMARY KEY, username TEXT, password TEXT,
# studentid INTEGER NOT NULL)""")

# Points
#cursor.execute("""CREATE TABLE IF NOT EXISTS points
#(id INTEGER PRIMARY KEY, studentid INTEGER NOT NULL,
#teacherid INTEGER NOT NULL, comment TEXT, points INTEGER, pointsTo TEXT)""")

# Houses
# cursor.execute("""CREATE TABLE IF NOT EXISTS houses
# (id INTEGER PRIMARY KEY, studentid INTEGER NOT NULL,
# housename TEXT)""")

# save changes
connection.commit()

# close connection
connection.close()
