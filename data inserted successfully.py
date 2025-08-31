import pymysql
connection = pymysql.connect(host="localhost",user="root",passwd="",
                             database="employee")
cursor = connection.cursor()

name="sugan"

record1="INSERT INTO BESANT (EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY)
VALUES(1001),'%S','SE',2,200000):"%(name)
record2="INSERT INTO BESANT (EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY)
VALUES(1002),'kesaven','SSE',3,100000);"
record3="INSERT INTO BESANT (EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY)
VALUES(1003),'vasu','SE',2,200000);"
record4="INSERT INTO BESANT (EMPID,NAME,DESIGNATION,EXPERIENCE,SALARY)
VALUES(1004),'mega','SE',2,300000);"


cursor.execute(record1)
cursor.execute(record2)
cursor.execute(record3)
cursor.execute(record4)



connection.commit()
print("data inserted successfully")
connection.close()
