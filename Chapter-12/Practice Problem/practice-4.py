a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a==0):
    print("Undefined")
else:
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Infinte")