try:
    x=10/0
    y='2'+4
except ZeroDivisionError as e:
        print(e)
except TypeError as a:
        print(a)
