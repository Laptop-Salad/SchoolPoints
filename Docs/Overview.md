# High-level Pseudocode

https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/ - We can use the jinja2 templating engine to be able to use the same footer for different pages.

# Login
* When a student logs in successfully they will be redirected to /student/{student id}
* When a teacher logs in successfully they will be redirected to /teacher
* When a parent logs in successfully they will be redirected to /student/{student id}

On first login of student, teacher they will be redirected to /changepassword.

https://testdriven.io/blog/flask-sessions/ - verify someone is logged in by saving their session.

# Logout
```
Destory current session
Display "Successfully Logged out"
```

# Change Password
PUT to changepassword

```
Ensure there is someone logged in

Display form to change password
```

# Teacher Dashboard
```
Path: teacher

Ensure a teacher is logged in

Get all students

Display all students

When click on student goto student/<student id>

```

AJAX can be used to make search bar to get data from server.

# Student Dashboard
```
Path: student/23

Get data from student whose id is 23

Ensure student with id of 23 is signed in OR teacher is signed in OR parent has student id of 23

Display Grades total
Display Attendance total
Display Behaviour
Display Other total

IF parent
  Display contact details of all teachers

```

# In Grades/Attendance/Behaviour/Other
POST to updatestudent/{studentid}

```
Path: student/23/attendance

Ensure student with id of 23 is signed in OR teacher is signed in OR parent has student id of 23

IF teacher
  Display form to change attendance

Get all points and display

```
