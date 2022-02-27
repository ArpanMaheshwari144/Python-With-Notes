class Sample:
    a = "Arpan"

obj = Sample()
print(obj.a)
print(Sample.a)
obj.a = "Adarsh"  # instance attribute cannot change class attribute
# Sample.a = "Adarsh" # class attribute can change class attribute
print(obj.a)
print(Sample.a)  
