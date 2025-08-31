student = ("AAA",21,"B.SC")
print("student tuple:",student)
print("name:",student[0])
print("age:",student[1])
print("course:",student[2])
student = [
    ("aaa",21,"b.sc"),
    ("bbb",22,"bca"),
    ("ccc",23,"bba")
    ]
print("\n list of student (using tuples):")
for s in student:
    print("name:",s[0],"| age:",s[1],"| course:",s[2])

numbers=(10,20,30,40,50)
print("forword order:")
for n in numbers:
      print(n,end=" ")
print("\n backword order:")
for n in numbers:
      print(n,end=" ")
      
