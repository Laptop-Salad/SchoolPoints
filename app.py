from flask import Flask, render_template, request

import sys
sys.path.append("controllers/")

from student import Student
from teacher import Teacher
from search_students import SearchStudents
from login import login

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    return "<h1>Login</h1>"

@app.route("/logout", methods=['GET'])
def logout():
    return "<h1>Logout</h1>"

@app.route("/changepassword", methods=['GET', 'PUT'])
def changepassword():
    return "<h1>Change Password</h1>"

# Teacher dashboard
@app.route("/teacher/<teacherid>", methods=['GET'])
def teacher(teacherid):
    if request.method == "GET":
        teacher = Teacher()
        teacher_name = teacher.dashboard_data(teacherid)
        students = teacher.get_all_students()
        return render_template("teacherDashboard.html", teacher_name=teacher_name, students=students)

# Search for students
@app.route("/searchstudents/<term>", methods=['GET'])
def search_students(term):
    if request.method == "GET":
        search_students = SearchStudents()
        res = search_students.get_like_students(term)
        return res

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

#student login

@app.route('/loginUI', methods=['GET', 'POST'])
def student_Login():
    if request.method == "GET":
        return render_template("loginUI.html")
    else:
        username = request.form['Username']
        password = request.form['Password']

        check = login.studentCheckLogin(username, password)
        if check == True:
            id = login.studentLogin(username, password)
            return render_template("dashboard", studentid = id)
        else:
            return 'incorrect username or password'

if __name__ == '__main__':
   app.run()
