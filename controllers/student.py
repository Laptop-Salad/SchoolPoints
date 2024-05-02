import sqlite3
import sys
from sqlite3 import Error

class Student:
    def get_student_name(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT username FROM students WHERE id = '" + str(studentid) + "';")
        res = cursor.fetchall()
        conn.close()

        return res[0][0]

    def get_points(self, studentid, type):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        character = None

        match type.lower():
            case "attendance":
                character = "A"
            case "behavior":
                character = "B"
            case "grades":
                character = "G"
            case "others":
                character = "O"

        # Get all behavior points
        cursor.execute("SELECT * FROM points WHERE pointsTo = '" + character + "' AND studentid = " + str(studentid))
        
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

        conn.close()
        
        return {
            "points": points,
            "comments": comments,
            "teachers": teachers,
            "totalPoints": totalPoints
        }

    def get_summary(self, studentid):
        behavior = self.get_points(studentid, "behavior")["totalPoints"]
        attendance = self.get_points(studentid, "attendance")["totalPoints"]
        grades = self.get_points(studentid, "grades")["totalPoints"]
        others = self.get_points(studentid, "others")["totalPoints"]

        total_points = behavior + attendance + grades + others

        return {
            "behavior_points": behavior,
            "attendance_points": attendance,
            "grades_points": grades,
            "others_points": others,
            "total_points": total_points
        }

    def getHouse(self, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT housename FROM houses WHERE id = '" + str(studentid) + "';")
        res = cursor.fetchall()
        conn.close()

        return res[0][0]

