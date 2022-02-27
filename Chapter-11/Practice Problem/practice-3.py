class Employee:
    salary = 10000
    increment = 1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salaryAfterIncrement):
        # salaryAfterIncrement = salary * increment
        self.increment = salaryAfterIncrement/self.salary


emp = Employee()
print(emp.salaryAfterIncrement)  # this will calls ->  @property
print(emp.increment)
emp.salaryAfterIncrement = 2000   # this will calls -> @salaryAfterIncrement.setter
print(emp.increment)