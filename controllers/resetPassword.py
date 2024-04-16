import sqlite3

class Reset:

    def resetPasswordS(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET password = %s resetpassword = 0 WHERE id= %s" %(newpassword, id))


