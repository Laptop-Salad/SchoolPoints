import sqlite3
import sys
from sqlite3 import Error
import urllib.parse

class SearchStudents:
    def get_like_students(self, term):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        decoded_term = "%" + urllib.parse.unquote(term) + "%"

        # Get all like students
        sql_string = "SELECT * FROM students WHERE lower(username) LIKE lower('" + decoded_term + "')"
        cursor.execute(sql_string)

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
