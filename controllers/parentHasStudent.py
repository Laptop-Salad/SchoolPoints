import sqlite3
import sys

sys.path.append("controllers/")
from student import Student

class ParentHasStudent:
    def hasStudent(parentid, studentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT studentid FROM parents WHERE id = " + "'" + parentid + "'")
        res = cursor.fetchall()
        conn.close()
        return str(res[0][0]) == studentid
    
    def getStudent(parentid):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT studentid FROM parents WHERE id = " + "'" + parentid + "'")
        res = cursor.fetchall()
        conn.close()
        return str(res[0][0])
