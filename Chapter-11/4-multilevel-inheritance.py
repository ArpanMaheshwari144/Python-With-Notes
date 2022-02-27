class Person:
    country = "India"

    def takeBreak(self):
        print("Person takes a Break")

class Employee(Person):
    company = "TCS"
    salary = 1000000

    def getSalary(self):
        print(f"Salary of a Employee is {self.salary}")

    def takeBreak(self):
        print("Employee takes a Break")

class Programmer(Employee):
    company = "Mahindra"

    def getSalary(self):
        print(f"The salary of a Programmer is {self.salary}")

    def takeBreak(self):
        print("Programmer takes a Break")


p = Person()
p.takeBreak()
print(p.country)

emp = Employee()
emp.getSalary()
emp.takeBreak()
print(emp.company)
print(emp.country)

prg = Programmer()
prg.getSalary()
prg.takeBreak()
print(prg.company)
print(prg.country)
