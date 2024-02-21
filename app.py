from flask import Flask

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
    return """<h1>Student Dashboard</h1>
    <p>""" + studentid + """</p>"""
