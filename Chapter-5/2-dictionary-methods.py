myDict = {
    "Arpan":"Cool",  
    "Maheshwari":"Boy",
    "Marks":[1,2,3], 
    "anotherDict":{"arpan":"Player"},
    1:2
}

# print(myDict.keys())  # prints the keys of the dictionary
# print(myDict.values())  # prints the values of the dictionary

# print(type(myDict.keys()))
# print(type(myDict.values()))

# Dictionary can change into list with typecasting
# print(list(myDict.keys()))
# print(list(myDict.values()))

# print(type(list(myDict.keys())))
# print(type(list(myDict.values())))

# print(myDict.items())  # return the (key value) pair for all contents of the dictionary in the form of tuple

# print(myDict.get("Arpan"))  # prints value associated with key "Arpan"
# print(myDict["Arpan"])   # prints value associated with key "Arpan"

# The difference between myDict.get() and myDict[] syntax in dictionaries:  
# print(myDict.get("Arpan1")) # returns None as Arpan1 is not present in the dictionary
# print(myDict["Arpan1"])  # throws an error as Arpan1 is not present in the dictionary


print(myDict)
updateDict = {
    "Adarsh":"Friend",
    "Verma":"Friend",
    "Patra":"Friend",
    "Arpan":"Hot"
}
myDict.update(updateDict)  # updates the dictionary by adding key-value pairs from updateDict
print(myDict)