student = {
    "name":"AAA",
    "age":21,
    "course":"B.SC"
    }
print("student dictionary:",student)
print("name:",student["name"])
print("age:",student["age"])
print("course:",student["course"])
student["age"]=22
student["grade"]="b+"
del student["course"]
print("\nstudent details:")
for key, value in student.items():
     print(key,":",value)
      
