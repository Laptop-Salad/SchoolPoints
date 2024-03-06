import sqlite3
import sys
from sqlite3 import Error

class Teacher:
    def dashboard_data(self, teacherid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        teacher_name = None

        # Get teacher names
        sqlQuery = "SELECT username FROM teachers WHERE id = " + str(teacherid) +";"
        cursor.execute(sqlQuery)
        result = cursor.fetchall()

        teacher_name = result[0][0]
        
        return teacher_name

        conn.commit()
        conn.close()
        
    def get_all_students(self):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Get all students
        cursor.execute("SELECT * FROM students")

        student_ids = []
        student_names = []

        result = cursor.fetchall()

        for row in result:
            student_ids.append(row[0])
            student_names.append(row[1])
        
        return {
            "student_ids": student_ids,
            "student_names": student_names,
        }

        conn.commit()
        conn.close()




