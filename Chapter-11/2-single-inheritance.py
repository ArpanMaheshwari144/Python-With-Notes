class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

# Inheritance
class Programmer(Employee):
    language = "Python"

    def getLangauge(self):
        print(f"The language of the programmer is {self.language}")

    # Overriding of Employee showDetails function
    def showDetails(self):
        print("This is a programmer")


emp = Employee()
prg = Programmer()
print(emp.company)
prg.getLangauge()
emp.showDetails()
prg.showDetails()