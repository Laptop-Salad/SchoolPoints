import sqlite3
import sys

sys.path.append("controllers/")
from student import Student

class Leaderboard:
    def getHouseTotal(self, house):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        houseTotal = 0
        student = Student()

        #find every student that is in the blue house
        cursor.execute("SELECT studentid FROM houses WHERE housename = '" + house + "'")
        houseStudents = cursor.fetchall()

        # for each student get their total points
        for studentid in houseStudents:
            houseTotal += student.get_summary(studentid[0])["total_points"]

        conn.close()    
        return houseTotal

    def getBlueTotal(self):
        return self.getHouseTotal("Blue")  

    def getRedTotal(self):
        return self.getHouseTotal("Red Rabbits")  
    
    def getTop3Students(self):
        # Note: This is school-wide

    def winningHouse(self, redTotal, blueTotal):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        #find out which house has the most points
        if redTotal > blueTotal:
            winner = "Red Rabbits"
        else:
            winner = "blue"

        conn.close()
        return winner
