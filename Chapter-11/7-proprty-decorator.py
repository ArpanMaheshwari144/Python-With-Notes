class Employee:
    comapny = "TCS"
    salary = 5000
    salaryBonus = 2000

    # this is a getter method
    @property  # this acts as a class property but internally it is a function
    def totalSalary(self):
        return self.salary + self.salaryBonus

    # this is a setter method
    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary

emp = Employee()
print(emp.totalSalary)  # this will call -> @property wala method
emp.totalSalary = 9000  # this will call -> @totalSalary.setter wala method
print(emp.salary)
print(emp.salaryBonus)
