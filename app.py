from flask import Flask, render_template, request

import sys
sys.path.append("controllers/")

from behavior import Student


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return render_template("loginUI.html")

@app.route("/logout", methods=['GET'])
def logout():
    return "<h1>Logout</h1>"

@app.route("/changepassword", methods=['GET', 'PUT'])
def changepassword():
    return "<h1>Change Password</h1>"

@app.route("/teacher", methods=['GET'])
def teacher():
    return "<h1>Teacher Dashboard</h1>"

# Dashboard: Attendance, grades, behaviour, others
@app.route("/student/<studentid>", methods=['GET'])
def student(studentid):
    return render_template("dashboard.html", student_num = studentid)

# Behaviour
@app.route("/student/<studentid>/behaviour", methods=['GET', 'POST'])
def student_behaviour(studentid):
    if request.method == "GET":
        student = Student()
        behaviors = student.get_behavior(studentid)
        return render_template("behavior.html", behaviors=behaviors, student_num = studentid)
    else:
        return "<h1>POST</h1>"
    
# Attendance
@app.route("/student/<studentid>/attendance", methods=['GET', 'POST'])
def student_attendance(studentid):
    if request.method == "GET":
        student = Student()
        attendance = student.get_attendance(studentid)
        return render_template("attendance.html", attendance=attendance, student_num = studentid)
    else:
        return "<h1>POST</h1>"

# Grades
@app.route("/student/<studentid>/grades", methods=['GET', 'POST'])
def student_grades(studentid):
    if request.method == "GET":
        student = Student()
        grades = student.get_grades(studentid)
        return render_template("grades.html", grades=grades, student_num = studentid)
    else:
        return "<h1>POST</h1>"

# Others
@app.route("/student/<studentid>/others", methods=['GET', 'POST'])
def student_others(studentid):
    if request.method == "GET":
        student = Student()
        others = student.get_others(studentid)
        return render_template("others.html", others=others, student_num = studentid)
    else:
        return "<h1>POST</h1>"
    
# End of dashboard routes

if __name__ == '__main__':
   app.run()
