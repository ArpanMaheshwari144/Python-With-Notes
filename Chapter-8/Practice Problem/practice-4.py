def sumOfNNaturalNumber(num):
    if(num<=1):
        return num
    else:
        return num + sumOfNNaturalNumber(num-1)

num = int(input("Enter a number: "))
if(num<0):
    print("Enter a whole positive number")
else:
    firstSum = sumOfNNaturalNumber(num)
    print(f"The factorial of {num} is {firstSum}")
