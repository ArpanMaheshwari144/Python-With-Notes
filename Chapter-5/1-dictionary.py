# dictionary can allows duplicate values
# dictionary cannot allow duplicate keys

myDict = {
    "Arpan":"Cool",  
    "Maheshwari":"Boy",
    "Marks":[1,2,3], 
    "anotherDict":{"arpan":"Player"}
}

# print(myDict)
# print(myDict["Arpan"])
# print(myDict["Maheshwari"])
# print(myDict["Marks"])
# print(myDict["anotherDict"])
# print(myDict["anotherDict"]["arpan"])

# Dictionary is mutable(can change)
print(myDict)
print(myDict["Marks"])
myDict["Marks"] = [100,88,90]
print(myDict)
print(myDict["Marks"])


