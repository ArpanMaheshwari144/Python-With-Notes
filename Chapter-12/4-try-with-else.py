# in this case -> else tabhi execute hoga jab try successfully execute ho jayega agar try successfully execute nhi hua to else bhi execute nhi hoga
try:
    a = int(input("Enter a number: "))
except Exception as e:
    print(e)
else:
    print("We were successfull")
