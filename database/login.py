import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

def studentLogin():
    username = input("Enter username: ")
    password = input("Enter Password: ")

    username = "'"+username+"'"
    password = "'"+password+"'"

    cursor.execute("SELECT id FROM students WHERE username = %s AND Password = %s" %(username, password))
    check = cursor.fetchall()
    if str(check) == "[]" :
        print("incorrect")
    else:
        check = check =  str(check [0])
        check = check[1:2]
        print("Id is" , check)

def parentLogin():
    username = input("Enter username: ")
    password = input("Enter Password: ")

    username = "'"+username+"'"
    password = "'"+password+"'"

    cursor.execute("SELECT id FROM parents WHERE username = %s AND Password = %s" %(username, password))
    check = cursor.fetchall()
    if str(check) == "[]" :
        print("incorrect")
    else:
        check = check =  str(check [0])
        check = check[1:2]
        print("Id is", check)

def teacherLogin():
    username = input("Enter username: ")
    password = input("Enter Password: ")

    username = "'"+username+"'"
    password = "'"+password+"'"

    cursor.execute("SELECT id FROM teachers WHERE username = %s AND Password = %s" %(username, password))
    check = cursor.fetchall()
    if str(check) == "[]" :
        print("incorrect")
    else:
        check = check =  str(check [0])
        check = check[1:2]
        print("Id is" , check)

studentLogin()