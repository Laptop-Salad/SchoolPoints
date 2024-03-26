import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM points WHERE id = 17 OR id = 18;")

print("Records added to Database")
conn.commit()
conn.close()