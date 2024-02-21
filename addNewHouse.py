import sqlite3

try:
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    #connected to database

    query = """INSERT INTO houses (studentid, housename)
    VALUES (1,"Blue")"""
    cursor.execute(query)
    record = cursor.fetchall()
    # SQL version is recorded

except sqlite3.Error as error:
    print(error)
finally:
    if conn:
        conn.close()
        #connection to database is closed
