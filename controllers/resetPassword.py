import sqlite3

class Reset:

    def resetPasswordS(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        newpassword = "'" + newpassword + "'"
        cursor.execute("UPDATE students SET password = %s, resetpassword = 0 WHERE id= %s" %(newpassword, id))
        conn.commit()

    def checkprevpassword(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM students WHERE id = '%s'" %(id))
        oldpassword = cursor.fetchall()
        oldpassword = str(oldpassword)
        oldpassword = oldpassword[3:-4]
        if oldpassword == newpassword:
            similar = True
        else:
            similar = False
        return similar