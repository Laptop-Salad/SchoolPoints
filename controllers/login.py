import sqlite3
from sqlite3 import Error

class Login:

    def studentCheckLogin(self,username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM students WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def studentLogin(self,username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()
        return check

#

    def teacherCheckLogin(self,username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM teachers WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def teacherLogin(sself, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM teachers WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()
        return check
#
#

    def parentCheckLogin(self, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM parents WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def parentLogin(self, username, password):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM parents WHERE username = '%s' AND Password = '%s'" %(username, password))
        check = cursor.fetchall()
        return check

    def checkPasswordStudent(self, id):
        conn = sqlite3.connect("school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT resetpassword FROM students WHERE id = '%s'" %(id))
        check = cursor.fetchall()
        check = str(check)
        check = check[2:3]
        if check == 1:
            reset = "true"
        else:
            reset = "false"
        return reset



