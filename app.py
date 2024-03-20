from flask import Flask, render_template, request, redirect

import sys
sys.path.append("controllers/")

from student import Student
from teacher import Teacher
from search_students import SearchStudents
from login import Login
from addToStudent import AddToStudent
from leaderboardBackend import Leaderboard

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
    student = Student()
    attendance = student.get_attendance(studentid)
    behavior = student.get_behavior(studentid)
    grades = student.get_grades(studentid)
    others = student.get_others(studentid)


    return render_template("dashboard.html", student_num = studentid,
                           attendance=attendance,
                           behavior=behavior,
                           grades=grades,
                           others=others)

# Behaviour
@app.route("/student/<studentid>/behaviour", methods=['GET', 'POST'])
def student_behaviour(studentid):
    if request.method == "GET":
        student = Student()
        behaviors = student.get_behavior(studentid)
        return render_template("behavior.html", behaviors=behaviors, student_num = studentid)
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
        attendance = student.get_attendance(studentid)
        return render_template("attendance.html", attendance=attendance, student_num = studentid)
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
        grades = student.get_grades(studentid)
        return render_template("grades.html", grades=grades, student_num = studentid)
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
        others = student.get_others(studentid)
        return render_template("others.html", others=others, student_num = studentid)
    else:
        comment = request.form.get("comment")
        points = request.form.get("points")

        add_to_student = AddToStudent()
        add_to_student.add_points(studentid, 1, comment, points, "O")
        redirect_url = "/student/" + studentid + "/others"
        return redirect(redirect_url, code=302)

    
# End of dashboard routes

#student login

@app.route('/SloginUI', methods=['GET', 'POST'])
def student_Login():
    if request.method == "GET":
        return render_template("SloginUI.html")
    else:
        username = request.form['Username']
        password = request.form['Password']
        print(username, password)
        username = "'" + username + "'"
        password = "'" + password + "'"

        login = Login()

        check = login.studentCheckLogin(username, password)
        if check == True:
            id = login.studentLogin(username, password)
            id = str(id[1:2])
            return redirect("../templates/dashboard", id= id)
        else:
            return render_template("SLoginUI", msg = "Incorrect Username or Password")

#teacherLogin
@app.route('/TloginUI', methods=['GET', 'POST'])
def teacher_Login():
    if request.method == "GET":
        return render_template("TloginUI.html")
    else:
        username = request.form['Username']
        password = request.form['Password']
        print(username, password)
        username = "'" + username + "'"
        password = "'" + password + "'"

        login = Login()

        check = login.teacherCheckLogin(username, password)
        if check == True:
            id = login.teacherLogin(username, password)
            id = str(id[1:2])
            return redirect("../templates/dashboard", id= id)
        else:
            return render_template("TLoginUI", msg = "Incorrect Username or Password")

#parentlogin
@app.route('/PloginUI', methods=['GET', 'POST'])
def parent_Login():
    if request.method == "GET":
        return render_template("PloginUI.html")
    else:
        username = request.form['Username']
        password = request.form['Password']
        print(username, password)
        username = "'" + username + "'"
        password = "'" + password + "'"

        login = Login()

        check = login.parentCheckLogin(username, password)
        if check == True:
            id = login.teacherLogin(username, password)
            id = str(id[1:2])
            return redirect("../templates/dashboard", id= id)
        else:
            return render_template("PLoginUI", msg = "Incorrect Username or Password")

#leaderboard
@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboardcalc():
    losingTotal = 0
    winningTotal = 0
    winningHouse = "Winning house"
    losingHouse = "losing house"
    if request.method == "GET":
        leaderboard = Leaderboard()
        #get the total points for the blue house
        blueTotal = leaderboard.getBlueTotal()

        #get the total points for the red house
        redTotal = leaderboard.getRedTotal()

        #calc which of the houses has the most points
        winningHouse = leaderboard.winningHouse(redTotal, blueTotal)

        #set the winning/losing house and points to the right varible
        if winningHouse == "blue":
            losingHouse = "Red Rabbits"
            losingTotal = redTotal
            winningTotal = blueTotal
        else:
            losingHouse = "Blue"
            losingTotal = blueTotal
            winningTotal =redTotal

        return render_template("leaderboard.html", winningTotal = winningTotal, winners = winningHouse, losingTotal = losingTotal, losers = losingHouse)
    else:
        return "<h1> POST </h1>"

if __name__ == '__main__':
   app.run()
