import sqlite3
from sqlite3 import Error


conn = sqlite3.connect("school.db")


cursor = conn.cursor()

#add to students table
#cursor.execute("""INSERT INTO students(username, password)
 #   VALUES ("Tim", "PasswordAHH")""")

#add to teachers table
#cursor.execute("""INSERT INTO teachers(username, password)
 #  VALUES ("Mr Creepshow", "Password666")"""
  #           )

#add to parents table
#cursor.execute("""INSERT INTO parents(username, password, studentid)
 #  VALUES ("apple", "this is not a password", 2)"""
  #             )

#add to points table
#cursor.execute("""INSERT INTO points(studentid, teacherid, comment, behaviour, grades, attendance, other)
 #  VALUES (2, 2, "good at math", 0, 0, 0, 3 )"""
  #             )

#add to houses table
#cursor.execute("""INSERT INTO houses (studentid, housename)
 #   VALUES (2, "Red Rabbits")"""
  #             )

print("Records added to Database")
conn.commit()
conn.close()



