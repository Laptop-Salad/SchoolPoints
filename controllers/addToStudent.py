import sqlite3
import sys
from sqlite3 import Error
# Teacherids arent real for now
class AddToStudent:
    def add_points(self, studentid, teacherid, comment, points, pointsTo):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        sql_string = "INSERT into points (studentid, teacherid, comment, points, pointsTo) VALUES ( ?, ?, ?, ?, ?)"

        cursor.execute(sql_string, [studentid, teacherid, comment, points, pointsTo])

        try:
            conn.commit()
            conn.close()
        except:
            print("Error occurred")
        

