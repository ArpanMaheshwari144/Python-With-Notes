class Employee:
    # Constructor
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("Employee is created!!")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The language of the employee is {self.language}")

arpan = Employee("Arpan", 100000, "Kotlin") # this will call the constructor automatically
arpan.getDetails()
