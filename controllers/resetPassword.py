import sqlite3
import bcrypt 

class Reset:

    def resetPasswordS(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        salt = bcrypt.gensalt() 
        bytes = newpassword.encode('utf-8') 
        hash = bcrypt.hashpw(bytes, salt) 

        cursor.execute("UPDATE students SET password = ?, resetpassword = 1 WHERE id = ?", (hash, id))
        conn.commit()

    def checkprevpasswordS(self, id, newpassword):
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

    def resetPasswordT(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        newpassword = "'" + newpassword + "'"
        cursor.execute("UPDATE teachers SET password = %s, resetpassword = 1 WHERE id= %s" %(newpassword, id))
        conn.commit()

    def checkprevpasswordT(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM teachers WHERE id = '%s'" %(id))
        oldpassword = cursor.fetchall()
        oldpassword = str(oldpassword)
        oldpassword = oldpassword[3:-4]
        if oldpassword == newpassword:
            similar = True
        else:
            similar = False
        return similar

    def resetPasswordP(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        newpassword = "'" + newpassword + "'"
        cursor.execute("UPDATE parents SET password = %s, resetpassword = 1 WHERE id= %s" %(newpassword, id))
        conn.commit()

    def checkprevpasswordP(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM parents WHERE id = '%s'" %(id))
        oldpassword = cursor.fetchall()
        oldpassword = str(oldpassword)
        oldpassword = oldpassword[3:-4]
        if oldpassword == newpassword:
            similar = True
        else:
            similar = False
        return similar