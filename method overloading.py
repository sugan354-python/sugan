class parent:
    def mymethod(self,a):
        print(a)
        print("calling parent method")
class child(parent):
    def mymethod(self,a,b):
        print(a)
        print(b)
        print("calling child method")

#main
c=child()
p=parent()
p.mymethod(100)
c.mymethod(100,200)
