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

# Creating instance attribute for both the objects
# Employee.company = "Apple"
# arpan.salary = 200
# adarsh.salary = 200

print(arpan.company)
print(adarsh.company)
print(arpan.salary)
print(adarsh.salary)

# phle ye check karega ki instance object hai ya fir nhi hai agar hai to uski value print kardega agar nhi hai to fir class mei dekhega or agar class mei bhi nhi mila to fir error throw kardega in simple words (Instance attributes take preference over class attributes during assignment and retrieval)
# print(arpan.address) # Below line throws an error as address is not present in instance/class
