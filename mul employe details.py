#multiple employee details

class employee:
    #eorganization="intel"
    def getData(self):
        self.eid=int(input("enetr the empid:"))
        self.ename=int(input("enetr the empname:"))
        self.esalary=float(input("enetr the empsalary:"))
    def putData(self):
        print("employee id:",self.eid)
        print("employee name:",self.ename)
        print("employee salary:",self.esalary)

oc=[]
numofobjects=int(input("enetr the num of objects:"))
for obj in range(numofobjects):
    emp=employee()
    emp.getData()
    oc.append(emp)
#for objindex in range(numof object):
#  print("===============Fetchiung employee details:%d========="((objIndex)+1))
#oc[objIndex].putData()
empid=int(input("enetr the employee id:"))
print("**************************************************")
empcount=0
empfound=0
for empData in oc:
    empcount=empcount+1
    if empData.eid ++ empid:
        Print("===================FETCHING EMPLOYEES DETAILS:%D========"%(EMPCOUNT))
        empData.putData()
        empfound =1
    if empfound==0:
        print("employee details")
for objIndex in range(numofobjects):
        print("=============Fetching employee details:%d=============="%d((objIndex)+1))
        oc[objInex].putData()
        print("***************************************************")
        empcount=0
        for empDatam in oc:
            empcount=empcount+1
            print("========================fetching employee details:%d============"%(empcount))
            empData.putData()
