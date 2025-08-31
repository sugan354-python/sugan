n=153
product=1
while n>0:
    digit=n%10
    product *=digit
    n=n//10
    print("product for the given number:",product)
