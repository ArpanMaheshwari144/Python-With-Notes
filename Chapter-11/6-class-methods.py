class Employee:
    company = "Google"
    salary = 100
    location = "Delhi"

    # def changeSalary(self, salary):
    #     # self.salary = salary
    #     self.__class__.salary = salary

    @classmethod
    def changeSalary(cls, salary):
        cls.salary = salary

e = Employee()
print(e.salary)
e.changeSalary(233)
print(e.salary)
print(Employee.salary)
