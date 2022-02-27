class Employee:
    # Creating Class Attribute
    company = "Google"
    salary = 100

arpan = Employee()
adarsh = Employee()
print(arpan.company)   
print(adarsh.company)
print(arpan.salary)
print(adarsh.salary)
Employee.company = "Apple"
arpan.salary = 200
adarsh.salary = 200
print(arpan.company)
print(adarsh.company)
print(arpan.salary)
print(adarsh.salary)