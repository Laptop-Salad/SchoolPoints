from flask import Flask, render_template

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

@app.route("/teacher", methods=['GET'])
def teacher():
    return "<h1>Teacher Dashboard</h1>"

@app.route("/student/<studentid>", methods=['GET'])
def student(studentid):
    return render_template("dashboard.html")

# Dashboard: Attendance, grades, behaviour, others

@app.route("/student/<studentid>/attendance", methods=['GET', 'POST'])
def student(studentid):
    return render_template("attendance.html")

@app.route("/student/<studentid>/grades", methods=['GET', 'POST'])
def student(studentid):
    return render_template("grades.html")


@app.route("/student/<studentid>/grades", methods=['GET', 'POST'])
def student(studentid):
    return render_template("grades.html")


@app.route("/student/<studentid>/others", methods=['GET', 'POST'])
def student(studentid):
    return render_template("others.html")

if __name__ == '__main__':
   app.run()
