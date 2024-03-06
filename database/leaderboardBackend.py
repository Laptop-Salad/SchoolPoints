import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("../databases/school.db")

cursor = conn.cursor()

#for each house get the id's of the students
#each house get the total points for each student
#add up all the points for each house
#figure out which one is first, second, third and last


cursor.execute("SELECT studentid FROM houses WHERE housename = 'Blue'")
blueStudents = cursor.fetchall()

cursor.execute("SELECT studentid FROM houses WHERE housename = 'Red Rabbits'")
redStudents = cursor.fetchall()

for i in range ((len(blueStudents))-1):
    cursor.execute("SELECT SUM(points) FROM points WHERE  %s", (blueStudents[i]))
    studentspointsBlue1 = cursor.fetchall()
    blueTotal = blueTotal + studentspointsBlue1

for i in range ((len(redStudents))-1):
    cursor.execute("SELECT SUM(points) FROM points WHERE  %s", (redStudents[i]))
    studentspointsRed1 = cursor.fetchall()
    redTotal = redTotal + studentspointsRed1

if redTotal > blueTotal:
    print("red has the most points: ", redTotal)
else:
    print("Blue has the most points: ", blueTotal)


