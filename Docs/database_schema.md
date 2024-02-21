# Database Schema

##Students 
id INTEGER PRIMARY KEY, 
username TEXT, 
password TEXT

## Teacher 
id INTEGER PRIMARY KEY,
username TEXT, 
password TEXT

## Parent 
id INTEGER PRIMARY KEY, 
username TEXT, 
password TEXT, 
student id INTEGER

## Points 
id INTEGER PRIMARY KEY, 
studentid INTEGER, 
teacherid INTEGER, 
comment TEXT,
behaviour INTEGER, 
grades INTEGER, 
attendance INTEGER, 
other INTEGER 

^ note behaviour, grades, attendance, other can be negative to subtract points, all points will be added together to get current points 

## Houses 
id INTEGER PRIMARY KEY,
studentid INTEGER, 
housename TEXT 

For simplicity's sake we will not use foreign keys. 

Apparently, we don’t need to put “autoincrement” because any INTEGER PRIMARY KEY will do so. https://github.com/mikro-orm/mikro-orm/discussions/2657  
