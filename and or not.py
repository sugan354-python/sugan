def true_fun():
    print("true_func() called")
    return True
def false_func():
    print("false_func()called")
    return False
print("===Demonstrating and/or/not ===")
print("True and True:",True and True)
print("True and False:",True and False)
print("False or True:",False or True)
print("False or False:",False or False)
print("not True:",not True)
print("not False:",not False)

print("\n===short-circuit behavior ===")
print("false_func() and true_func():")
print(false_func() and true_func())

print("0 and 5:",0 and 5)
print("3 and 5:",3 and 5)
print("[] or 'hi':",[] or "hi")
print("'hello' or []:","hello" or [])

print("\n== using or for defaults ==")
username = input("enter your username (or leave blank):") or "guest"
print("hello,",username)


