# try:
#     a = int(input("Enter a number: "))
#     c = 1/a
#     print(c)
# except Exception as e:
#     print(f"Error Occured: {e}")

# print("Thanks")


try:
    a = int(input("Enter a number: "))
    c = 1/a
    print(c)
except ValueError as e:
    print("Please enter a valid value")
except ZeroDivisionError as e:
    print("Make sure you are not dividing by zero")

print("Thanks")