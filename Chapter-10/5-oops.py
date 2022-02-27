class Employee:
    company = "Google"
    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

arpan = Employee()
print(arpan.company)
arpan.salary = 10000000
arpan.getSalary("Thanks!")  # this means -> Employee.getSalary(arpan)