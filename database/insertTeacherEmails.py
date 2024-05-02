ALTER TABLE teachers
ADD email varchar(255);

UPDATE teachers
SET email = "tommyteachers@acas.edu"
WHERE id = 1;

UPDATE teachers
SET email = "mycreepshow@acas.edu"
WHERE id = 2;

