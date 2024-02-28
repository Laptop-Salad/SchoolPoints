import sqlite3
import sys
from sqlite3 import Error

class Student:
    def get_behavior(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Get all behavior points
        cursor.execute("SELECT * FROM points WHERE pointsTo = 'B'")
        
        totalPoints = 100
        points = []
        comments = []
        teachers= []

        result = cursor.fetchall()

        for row in result:
            teachers.append(row[2])
            comments.append(row[3])
            points.append(row[4])

            totalPoints += int(row[4])

        # Get teacher names
        for teacher in range(0, len(teachers)):
            sqlQuery = "SELECT username FROM teachers WHERE id = " + str(teachers[teacher]) +";"
            cursor.execute(sqlQuery)
            result = cursor.fetchall()

            teachers[teacher] = result[0][0] # Get first item from first row
        
        return {
            "points": points,
            "comments": comments,
            "teachers": teachers,
            "totalPoints": totalPoints
        }

        conn.commit()
        conn.close()
        
    def get_attendance(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Get all behavior points
        cursor.execute("SELECT * FROM points WHERE pointsTo = 'A'")
        
        totalPoints = 100
        points = []
        comments = []
        teachers= []

        result = cursor.fetchall()

        for row in result:
            teachers.append(row[2])
            comments.append(row[3])
            points.append(row[4])

            totalPoints += int(row[4])

        # Get teacher names
        for teacher in range(0, len(teachers)):
            sqlQuery = "SELECT username FROM teachers WHERE id = " + str(teachers[teacher]) +";"
            cursor.execute(sqlQuery)
            result = cursor.fetchall()

            teachers[teacher] = result[0][0] # Get first item from first row
        
        return {
            "points": points,
            "comments": comments,
            "teachers": teachers,
            "totalPoints": totalPoints
        }

        conn.commit()
        conn.close()
        
    def get_grades(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Get all behavior points
        cursor.execute("SELECT * FROM points WHERE pointsTo = 'G'")
        
        totalPoints = 100
        points = []
        comments = []
        teachers= []

        result = cursor.fetchall()

        for row in result:
            teachers.append(row[2])
            comments.append(row[3])
            points.append(row[4])

            totalPoints += int(row[4])

        # Get teacher names
        for teacher in range(0, len(teachers)):
            sqlQuery = "SELECT username FROM teachers WHERE id = " + str(teachers[teacher]) +";"
            cursor.execute(sqlQuery)
            result = cursor.fetchall()

            teachers[teacher] = result[0][0] # Get first item from first row
        
        return {
            "points": points,
            "comments": comments,
            "teachers": teachers,
            "totalPoints": totalPoints
        }

        conn.commit()
        conn.close()   

    def get_others(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        # Get all behavior points
        cursor.execute("SELECT * FROM points WHERE pointsTo = 'O'")
        
        totalPoints = 100
        points = []
        comments = []
        teachers= []

        result = cursor.fetchall()

        for row in result:
            teachers.append(row[2])
            comments.append(row[3])
            points.append(row[4])

            totalPoints += int(row[4])

        # Get teacher names
        for teacher in range(0, len(teachers)):
            sqlQuery = "SELECT username FROM teachers WHERE id = " + str(teachers[teacher]) +";"
            cursor.execute(sqlQuery)
            result = cursor.fetchall()

            teachers[teacher] = result[0][0] # Get first item from first row
        
        return {
            "points": points,
            "comments": comments,
            "teachers": teachers,
            "totalPoints": totalPoints
        }

        conn.commit()
        conn.close() 
