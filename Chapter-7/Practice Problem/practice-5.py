num = int(input("Enter a number: "))
num1 = num
sum = 0

if(num<=0):
    print("Enter a whole positive number")
else:
    while(num>0):
        sum = sum + num
        num = num - 1
    print(f"The sum of first {num1} natural numbers is {sum}")
