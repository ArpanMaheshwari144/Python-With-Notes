def maximumOfThreeNumbers(num1, num2, num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3


num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

maxNum = maximumOfThreeNumbers(num1, num2, num3)
print(f"The maximum from {num1}, {num2} and {num3} is", maxNum)