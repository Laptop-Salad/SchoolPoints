from flask import Flask
import sqlite3


app = Flask(__name__)

# Create a db named school db if doesnt exist yet
connection = sqlite3.connect("school.db")

if (not connection):
    print("db couldnt connect successfully")
else:
    print("successfully connected to db")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
