# try:
#     a = int(input("Enter a number: "))
# except Exception as e:
#     print(e)
#     exit()
# finally:
#     print("We are done")


# try:
#     a = int(input("Enter a number: "))
# except Exception as e:
#     print(e)
#     exit()
# else:
#     print("We are done")


try:
    a = int(input("Enter a number: "))
except Exception as e:
    print(e)
    exit()
else:
    print("We are in else")
finally:
    print("We are in finally")