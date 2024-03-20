import sqlite3
from sqlite3 import Errorr

class Login:

    def studentCheckLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM students WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def studentLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM students WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()
        return check

#

    def teacherCheckLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM teachers WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def teacherLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM teachers WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()
        return check
#
#

    def parentCheckLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        confirmLogin = False

        cursor.execute("SELECT id FROM parents WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()

        if check:
            confirmLogin = True
        return confirmLogin

    def parentLogin(username, password):
        conn = sqlite3.connect("../school.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM parents WHERE username = %s AND Password = %s" %(username, password))
        check = cursor.fetchall()
        return check