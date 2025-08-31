#exception handling


'''num1 = int(input("enter the number:"))
num2 = int(input("enter the number:"))
try:
     res = num1/num2
     print("res is:",res)
except ZeroDivisionError:
         print("ZeroDivisionError exception occured")
print("after exception")'''

#exception value error


'''try:
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    res = num1/num2
    print("res is:",res)
except ZeroDivisionError:
    print("ZeroDivisionError exception occured")
except ValueError:
    print("valueError error occured")
print("after exception")'''





#genetric exception


'''try:
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    res = num1/num2
    print("res is:",res)
except Exception as e:
    print(e,"exception occured")
print("after exception")'''


#exception with else:


'''try:
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    res = num1/num2
    print("res is:",res)
except Exception as e:
    print(e,"exception occured")
else:
    print("program executed successfully")
print("after exception")'''


#exception with finally  :



try:
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    res = num1/num2
    print("res is:",res)
except Exception as e:
    print(e,"exception occured")
else:
    print("program executed successfully")
finally:
    print("this will executed always")
print("after exception")














































































































































































