myDict = {
    "Pankha":"Fan",
    "Dabba":"Box",
    "Dewar":"Wall",
    "Basta":"Bag"
}

print("Options are", list(myDict.keys()))
a = input("Enter your choice from these hindi words to see there english translation: ")

# Below line will throw an error if the key is not present in the dictionary
# print("The English Translation of", a, "is", myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The English Translation of", a, "is", myDict.get(a))