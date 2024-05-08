import sqlite3
from sqlite3 import Error
import bcrypt

class Login:

    def studentCheckLogin(self,username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM students WHERE username = '%s'" %(username))
        check = cursor.fetchall()

        if (len(check) > 0):
            userBytes = password.encode('utf-8') 
            bytes = check[0][0]
            try:
                bytes = bytes.encode('utf-8') 
            except:
                pass   
            result = bcrypt.checkpw(userBytes, bytes) 
            return result
        
        return False    

    def studentLogin(self, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students WHERE username = '%s'" %(username))
        check = cursor.fetchall()
        return check

    def teacherCheckLogin(self,username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM teachers WHERE username = '%s'" %(username))
        check = cursor.fetchall()

        if (len(check) > 0):
            userBytes = password.encode('utf-8') 
            bytes = check[0][0]
            bytes = bytes.encode('utf-8') 
            result = bcrypt.checkpw(userBytes, bytes) 
            return result
        
        return False  

    def teacherLogin(sself, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM teachers WHERE username = '%s'" %(username))
        check = cursor.fetchall()
        return check

    def parentCheckLogin(self, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()

        cursor.execute("SELECT password FROM parents WHERE username = '%s'" %(username))
        check = cursor.fetchall()

        if (len(check) > 0):
            userBytes = password.encode('utf-8') 
            bytes = check[0][0]
            bytes = bytes.encode('utf-8') 
            result = bcrypt.checkpw(userBytes, bytes) 
            return result
        
        return False  

    def parentLogin(self, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM parents WHERE username = '%s'" %(username))
        check = cursor.fetchall()
        return check

    def checkPasswordStudent(self, id):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT resetpassword FROM students WHERE id = '%s'" %(id))
        check = cursor.fetchall()
        check = str(check)
        check = check[2:3]
        return check == "1"


    def checkPasswordTeacher(self, id):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT resetpassword FROM teachers WHERE id = '%s'" %(id))
        check = cursor.fetchall()
        check = str(check)
        check = check[2:3]
        return check == "1"

    def checkPasswordParent(self, id):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT resetpassword FROM parents WHERE id = '%s'" %(id))
        check = cursor.fetchall()
        check = str(check)
        check = check[2:3]
        if check == "1":
            reset = "true"
        else:
            reset = "false"
        return reset




