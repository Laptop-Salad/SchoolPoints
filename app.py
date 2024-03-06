from flask import Flask, render_template, request

import sys
sys.path.append("controllers/")

from behavior import Student
from teacher import Teacher
from search_students import SearchStudents


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
@app.route("/student/<studentid>/behaviour", methods=['GET'])
def student_behaviour(studentid):
    student = Student()
    behaviors = student.get_behavior(studentid)
    return render_template("behavior.html", behaviors=behaviors, student_num = studentid)
    
# Attendance
@app.route("/student/<studentid>/attendance", methods=['GET'])
def student_attendance(studentid):
    student = Student()
    attendance = student.get_attendance(studentid)
    return render_template("attendance.html", attendance=attendance, student_num = studentid)

# Grades
@app.route("/student/<studentid>/grades", methods=['GET'])
def student_grades(studentid):
    student = Student()
    grades = student.get_grades(studentid)
    return render_template("grades.html", grades=grades, student_num = studentid)

# Others
@app.route("/student/<studentid>/others", methods=['GET'])
def student_others(studentid):
    student = Student()
    others = student.get_others(studentid)
    return render_template("others.html", others=others, student_num = studentid)
    
# End of dashboard routes

if __name__ == '__main__':
   app.run()
