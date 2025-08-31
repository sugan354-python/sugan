def inside_function():
    x,y=(10,5)
    print("inside function:")
    print("add:",x+y)
    print("sub:",x-y)
    print("mul:",x*y)
    print("div:",x/y)
    print()
def outside_function(values):
    x,y = values
    print("outside function:")
    print("add:",x+y)
    print("sub:",x-y)
    print("mul:",x*y)
    print("div:",x/y)
number_outside=(20,4)
inside_function()
outside_function(number_outside)
 
