class Number:

    # dunder methods
    def __init__(self, num1):
        self.num1 = num1

    def __add__(self, num2):
        return self.num1 + num2.num1

    def __sub__(self, num2):
        return self.num1 - num2.num1

    def __mul__(self, num2):
        return self.num1 * num2.num1

    def __truediv__(self, num2):
        return self.num1 / num2.num1

    def __floordiv__(self, num2):
        return self.num1 // num2.num1

    def __str__(self):
        return f"{self.num1}"


n1 = Number(6)
n2 = Number(4)

mySum = n1 + n2
mySub = n1 - n2
myMult = n1 * n2
myDiv = n1 / n2
myFloorDiv = n1 // n2

print(f"The addition of {n1} and {n2} is {mySum}")
print(f"The substraction of {n1} and {n2} is {mySub}")
print(f"The multiplication of {n1} and {n2} is {myMult}")
print(f"The division of {n1} and {n2} is {myDiv}")
print(f"The floor division of {n1} and {n2} is {myFloorDiv}")
