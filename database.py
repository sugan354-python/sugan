import pymysql
connection=pymysql.connect(host="localhost",user="root",password="",
                           database="employee")
print("My database connected successfully")
connection.close()
