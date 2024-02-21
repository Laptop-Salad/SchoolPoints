import sqlite3
from sqlite3 import Error


conn = sqlite3.connect("school.db")


cursor = conn.cursor()

#add to students table
cursor.execute("""INSERT INTO students(username, password)
    VALUES ("Tim", "PasswordAHH")""")

#add to teachers table
#cursor.execute("""INSERT INTO teachers(username, password)
 #   VALUES ("Tommyteacher", "Password1")"""
  #             )

#add to parents table
#.execute("""INSERT INTO parents(username, password, studentid)
 #   VALUES ("PamParent", "Password1", 1)"""
  #             )

#add to points table
#cursor.execute("""INSERT INTO points(studentid, teacherid, comment, behaviour, grades, attendance, other)
 #   VALUES (1, 1, "you r cool", 80, 80, 80, 80 )"""
           #    )

#add to houses table
#cursor.execute("""INSERT INTO houses (studentid, housename)
 #   VALUES (1, "Blue")"""
             #  )
conn.commit()
conn.close()



