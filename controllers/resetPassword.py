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



    def resetPasswordT(self, id, newpassword):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        salt = bcrypt.gensalt()
        bytes = newpassword.encode('utf-8')
        hash = bcrypt.hashpw(bytes, salt)

        cursor.execute("UPDATE teachers SET password = ?, resetpassword = 1 WHERE id = ?", (hash, id))
        conn.commit()


