import sqlite3

conn = sqlite3.connect("../school.db")

cursor = conn.cursor()


class Leaderboard:

    def getBlueTotal(self):
        #find every student that is in the blue house
        cursor.execute("SELECT studentid FROM houses WHERE housename = ""'Blue'")
        blueStudents = cursor.fetchall()

        #look through the points and for every student that was in the blue house get the total of the points
        for i in range ((len(blueStudents))-1):
            cursor.execute("SELECT SUM(points) FROM points WHERE  %s", ("'" + str(blueStudents[i]) + "'"))
            studentspointsBlue1 = cursor.fetchall()
            blueTotal = blueTotal + studentspointsBlue1
        return blueTotal

    def getRedTotal(self):
        #find every student that is in the red house
        cursor.execute("SELECT studentid FROM houses WHERE housename = 'Red Rabbits'")
        redStudents = cursor.fetchall()

        #look through the points and for every student that was in the red house get the total of the points
        for i in range ((len(redStudents))-1):
            cursor.execute("SELECT SUM(points) FROM points WHERE  %s", ("'" + str(redStudents[i]) + "'"))
            studentspointsRed1 = cursor.fetchall()
            redTotal = redTotal + studentspointsRed1
        return redTotal

    def winningHouse(self, redTotal, blueTotal):
        #find out which house has the most points
        if redTotal > blueTotal:
            winner = "Red Rabbits"
        else:
            winner = "blue"
        return winner





