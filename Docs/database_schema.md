# Database Schema

## Students 
id INTEGER PRIMARY KEY, <br>
username TEXT, <br>
password TEXT <br>

## Teacher 
id INTEGER PRIMARY KEY, <br>
username TEXT, <br>
password TEXT <br>

## Parent 
id INTEGER PRIMARY KEY, <br>
username TEXT, <br>
password TEXT, <br>
student id INTEGER <br>

## Points 
id INTEGER PRIMARY KEY, <br>
studentid INTEGER, <br>
teacherid INTEGER, <br>
comment TEXT,<br>
behaviour INTEGER, <br>
grades INTEGER, <br>
attendance INTEGER, <br>
other INTEGER <br>

^ note behaviour, grades, attendance, other can be negative to subtract points, all points will be added together to get current points 

## Houses 
id INTEGER PRIMARY KEY,<br>
studentid INTEGER, <br>
housename TEXT <br>

For simplicity's sake we will not use foreign keys. 

Apparently, we don’t need to put “autoincrement” because any INTEGER PRIMARY KEY will do so. https://github.com/mikro-orm/mikro-orm/discussions/2657  
