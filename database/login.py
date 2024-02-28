import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("school.db")

cursor = conn.cursor()

def studentLogin():
    #get username
    username = input("Enter username: ")
    username = "'"+ username+ "'"

    #look for username is database and get ID
    cursor.execute("SELECT id FROM students WHERE username = %s" %(username))
    check = cursor.fetchall()
    if str(check) == "[]" :
        #if username isn't in the database
        print("username incorrect")
    else:
        #if username is in the databse
        check =  str(check [0])
        check = check[1:2]

        #get password
        password = input("Enter password: ")
        #get password from the same row as the ID of username in database
        cursor.execute("SELECT password FROM students WHERE id = %s" %(check))
        check1 = cursor.fetchall()
        check1 =  str(check1 [0])
        num = len(check1) - 3
        check1 = check1[2:num]
        if check1 == password:
            #password in database is the same as the one entered
            print("Password correct go to logged in page")
        else:
            #password is different
            print("Password incorrect")
        return None

def teacherLogin():
    username = input("Enter username: ")
    username = "'"+ username+ "'"

    cursor.execute("SELECT id FROM teachers WHERE username = %s" %(username))
    check = cursor.fetchall()
    if str(check) == "[]" :
        print("username incorrect")
    else:
        check =  str(check [0])
        check = check[1:2]

        password = input("Enter password: ")
        cursor.execute("SELECT password FROM teachers WHERE id = %s" %(check))
        check1 = cursor.fetchall()
        check1 =  str(check1 [0])
        num = len(check1) - 3
        check1 = check1[2:num]
        if check1 == password:
            print("Password correct go to logged in page")
        else:
            print("Password incorrect")
        return None

def parentLogin():
    username = input("Enter username: ")
    username = "'"+ username+ "'"

    cursor.execute("SELECT id FROM parents WHERE username = %s" %(username))
    check = cursor.fetchall()
    if str(check) == "[]" :
        print("username incorrect")
    else:
        check =  str(check [0])
        check = check[1:2]

        password = input("Enter password: ")
        cursor.execute("SELECT password FROM parents WHERE id = %s" %(check))
        check1 = cursor.fetchall()
        check1 =  str(check1 [0])
        num = len(check1) - 3
        check1 = check1[2:num]
        if check1 == password:
            print("Password correct go to logged in page")
        else:
            print("Password incorrect")
    return None

def studentLogin2():
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

def parentLogin2():
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

def teacherLogin2():
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

studentLogin2()
parentLogin2()
teacherLogin2()


