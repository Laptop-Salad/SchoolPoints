import sqlite3
import sys

sys.path.append("controllers/")
from student import Student

class Leaderboard:
    def getHouseTotals(self):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT housename FROM houses")
        houses = cursor.fetchall()
        student = Student()
        house_names = []
        house_totals = []
        top_three_students = ["", "", ""]
        top_three_points = [0, 0, 0] # index 0 is the top student

        for house in houses:
            # Every student in house
            cursor.execute("SELECT studentid FROM houses WHERE housename = '" + house[0] + "'")
            house_students = cursor.fetchall()
            house_total = 0

            # for each student get their total points
            for studentid in house_students:
                curr_total = student.get_summary(studentid[0])["total_points"]
                house_total += curr_total

                # See if the current students score is greater than any of the below
                for points in range(0, len(top_three_points)):
                    if (curr_total > top_three_points[points]):
                        top_three_points.insert(0, curr_total)
                        top_three_points.pop(-1)
                        top_three_students.insert(0, student.get_student_name(studentid[0]))
                        top_three_students.pop(-1)
                        break
                        
            house_names.append(house[0])
            house_totals.append(house_total)

        # Use bubble sort to sort students
        for i in range(len(top_three_points)-1):
            swapped = False

            for j in range(0, len(top_three_points)-i-1):
                if top_three_points[j] < top_three_points[j + 1]:
                    swapped = True
                    top_three_points[j], top_three_points[j + 1] = top_three_points[j + 1], top_three_points[j]
                    top_three_students[j], top_three_students[j + 1] = top_three_students[j + 1], top_three_students[j]

            if not swapped:
                break

        # Use bubble sort to sort houses
        houses = len(house_names)
        for i in range(houses-1):
            swapped = False

            for j in range(0, houses-i-1):
                if house_totals[j] < house_totals[j + 1]:
                    swapped = True
                    house_totals[j], house_totals[j + 1] = house_totals[j + 1], house_totals[j]
                    house_names[j], house_names[j + 1] = house_names[j + 1], house_names[j]

            if not swapped:
                break

        return {
            "house_names": house_names,
            "house_totals": house_totals,
            "top_students_names": top_three_students,
            "top_students_points": top_three_points
        }
