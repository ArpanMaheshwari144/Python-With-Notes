# num = int(input("Enter a number to calculate its factorial: "))
# factorial = 1
# for i in range(num):
#     factorial = factorial * (i+1)
# print(f"The factorial of {num} is {factorial}")


# def factorial_iter(num):
#     if(num==1 or num==0):
#         return 1
#     else:
#         factorial = 1
#         for i in range(num):
#             factorial = factorial * (i+1)
#         return factorial

# num = int(input("Enter a number to calculate its factorial: "))
# fact = factorial_iter(num)
# print(f"The factorial of {num} is {fact}")


def factorial_recursive(num):
    if(num==1 or num==0):
        return 1
    else:
        return num * factorial_recursive(num-1)

num = int(input("Enter a number to calculate its factorial: "))
fact = factorial_recursive(num)
print(f"The factorial of {num} is {fact}")
