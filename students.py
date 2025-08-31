#students
CREATE TABLE students( id INT,name VARCHAR(100),MARK INT);
INSERT INTO students (id,name,MARKs)values 
(1,'aaa',88),
(2,'bbb',75),
(3,'ccc',67),
(4,'ddd',99),
(5,'eee',45);
SELECT AVG(MARK) FROM students;
