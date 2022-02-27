name = "a Arpan Maheshwari is a good good boy"

# String functions
print(len(name))

print(name.endswith("boy"))

print(name.count('o'))
print(name.count('oo'))
print(name.count("good"))

print(name.capitalize())

# returns the index of first occurence if multiple occurrence is occur
print(name.find("good"))  
print(name.find('r'))

# it replaces all the occurence if the multiple occurence is occur
print(name.replace("Arpan", "Adarsh"))
print(name.replace('a', 'j'))