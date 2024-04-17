from flask import Flask, render_template, request, redirect, session

import sys
sys.path.append("controllers/")

from student import Student
from teacher import Teacher
from search_students import SearchStudents
from login import Login
from addToStudent import AddToStudent
from leaderboardBackend import Leaderboard
from resetPassword import Reset

app = Flask(__name__)
app.secret_key = 'BAD_SECRET_KEY'

@app.route('/', methods=['GET', 'POST'])
def login():
        return render_template("index.html", title="Logged Out")

@app.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return "<h1>Successfully Logged Out</h1>"

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
        return render_template("teacherDashboard.html", title="Teacher Dashboard", teacher_name=teacher_name, students=students)

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
    student = Student()
    attendance = student.get_points(studentid, "attendance")
    behavior = student.get_points(studentid, "behavior")
    grades = student.get_points(studentid, "grades")
    others = student.get_points(studentid, "others")


    return render_template("dashboard.html", student_num = studentid,
                           attendance=attendance,
                           behavior=behavior,
                           grades=grades,
                           others=others,
                           title="Student Dashboard")

# Behaviour
@app.route("/student/<studentid>/behaviour", methods=['GET', 'POST'])
def student_behaviour(studentid):
    if request.method == "GET":
        student = Student()
        behaviors = student.get_points(studentid, "behavior")
        return render_template("behavior.html", title="Student behavior", behaviors=behaviors, student_num = studentid)
    else:
        comment = request.form.get("comment")
        points = request.form.get("points")

        add_to_student = AddToStudent()
        add_to_student.add_points(studentid, 1, comment, points, "B")
        redirect_url = "/student/" + studentid + "/behaviour"
        return redirect(redirect_url, code=302)
    
# Attendance
@app.route("/student/<studentid>/attendance", methods=['GET', 'POST'])
def student_attendance(studentid):
    if request.method == "GET":
        student = Student()
        attendance = student.get_points(studentid, "attendance")
        return render_template("attendance.html", title="Student attendance",  attendance=attendance, student_num = studentid)
    else:
        comment = request.form.get("comment")
        points = request.form.get("points")

        add_to_student = AddToStudent()
        add_to_student.add_points(studentid, 1, comment, points, "A")
        redirect_url = "/student/" + studentid + "/attendance"
        return redirect(redirect_url, code=302)
        
# Grades
@app.route("/student/<studentid>/grades", methods=['GET', 'POST'])
def student_grades(studentid):
    if request.method == "GET":
        student = Student()
        grades = student.get_points(studentid, "grades")
        return render_template("grades.html", title="Student Grades", grades=grades, student_num = studentid)
    else:
        comment = request.form.get("comment")
        points = request.form.get("points")

        add_to_student = AddToStudent()
        add_to_student.add_points(studentid, 1, comment, points, "G")
        redirect_url = "/student/" + studentid + "/grades"
        return redirect(redirect_url, code=302)

# Others
@app.route("/student/<studentid>/others", methods=['GET', 'POST'])
def student_others(studentid):
    if request.method == "GET":
        student = Student()
        others = student.get_points(studentid, "others")
        return render_template("others.html", title="Student Others", others=others, student_num = studentid)
    else:
        comment = request.form.get("comment")
        points = request.form.get("points")

        add_to_student = AddToStudent()
        add_to_student.add_points(studentid, 1, comment, points, "O")
        redirect_url = "/student/" + studentid + "/others"
        return redirect(redirect_url, code=302)

    
# End of dashboard routes

#student login

@app.route('/studentlogin', methods=['GET', 'POST'])
def student_Login():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['Password']

        login = Login()

        #check to see if username and password are correct
        check = login.studentCheckLogin(username, password)
        if check == True:
            #if the username and password are correct get the id
            id = login.studentLogin(username, password)
            id = str(id)
            id = id[2:3]

            # start session
            session["username"] = username
            session["userid"] = id
            session["type"] = "student"

            #check to see if they need to reset their password
            redirecturl = "/student/"+ id +"/changepassword"
            reset = login.checkPasswordStudent(id)
            if reset == "false":
                redirecturl = "/student/" + id

            return redirect(redirecturl)
        else:
            return render_template("SLoginUI.html", title="Student Login", msg = "Your username or password is incorrect")
    else:
        return render_template("SLoginUI.html", title="Student Login")


#teacherLogin
@app.route('/teacherlogin', methods=['GET', 'POST'])
def teacher_Login():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['Password']
        login = Login()

        #check to see if username and password are correct
        check = login.teacherCheckLogin(username, password)
        if check == True:
            # start session
            session["username"] = username
            session["userid"] = id
            session["type"] = "teacher"

            #if the username and password are correct get the id
            id = login.teacherLogin(username, password)
            id = str(id)
            id = id[2:3]
            redirecturl = "/teacher/" + id
            return redirect(redirecturl)
        else:
            return render_template("TLoginUI.html", title="Teacher Login", msg = "Your username or password is incorrect")
    else:
        return render_template("TLoginUI.html", title="Teacher Login")

#parentlogin
@app.route('/parentlogin', methods=['GET', 'POST'])
def parent_Login():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['Password']

        login = Login()

        #check to see if username and password are correct
        check = login.parentCheckLogin(username, password)
        if check == True:
            #if the username and password are correct get the id
            id = login.parentLogin(username, password)
            id = str(id)
            id = id[2:3]

            session["username"] = username
            session["userid"] = id
            session["type"] = "parent"

            redirecturl = "/student/" + id
            return redirect(redirecturl)
        else:
            return render_template("PLoginUI.html", title="Parent Login", msg = "Your username or password is incorrect")
    else:
        return render_template("PLoginUI.html", title="Parent Login")

#leaderboard
@app.route('/leaderboard', methods=['GET'])
def leaderboardcalc():
    if request.method == "GET":
        leaderboard = Leaderboard()

        leaderboard_res = leaderboard.getHouseTotals()

        return render_template("leaderboard.html",
        house_names = leaderboard_res["house_names"],
        house_totals = leaderboard_res["house_totals"],
        top_students_names = leaderboard_res["top_students_names"],
        top_students_points = leaderboard_res["top_students_points"])

@app.route("/student/<studentid>/changepassword", methods=['GET', 'POST'])
def changepasswordStudent(studentid):
    if request.method == "POST":
        password1 = request.form['password1']
        password2 = request.form['password2']
        if password1 == password2:
            reset = Reset
            reset.resetPasswordS(studentid, password1)
            redirecturl = "/student/" + studentid
            return redirect(redirecturl)
        else:
            redirecturl = "/student/" + studentid + "/changepassword"
            return redirect(redirecturl)
    elif request.method == "GET":
        return render_template("LoginPassword.html", title="Change Psassword")


if __name__ == '__main__':
   app.run(debug=True, port=8801)
