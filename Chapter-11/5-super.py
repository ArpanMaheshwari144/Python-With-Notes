class Person:
    country = "India"
    
    def __init__(self):
        print("I am Person's Contructor")

    def takeBreak(self):
        print("Person takes a Break")

class Employee(Person):
    company = "TCS"
    salary = 1000000

    def __init__(self):
        super().__init__()
        print("I am Employee's Contructor")

    def getSalary(self):
        print(f"Salary of a Employee is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("Employee takes a Break")

class Programmer(Employee):
    company = "Mahindra"

    def __init__(self):
        super().__init__()
        print("I am Programmer's Contructor")

    def getSalary(self):
        print(f"The salary of a Programmer is {self.salary}")

    def takeBreak(self):
        super().takeBreak()
        print("Programmer takes a Break")


p = Person()
p.takeBreak()

emp = Employee()
emp.takeBreak()

prg = Programmer()
prg.takeBreak()