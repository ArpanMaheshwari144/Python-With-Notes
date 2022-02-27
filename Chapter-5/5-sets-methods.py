# Creating an empty set
a = set()
# print(a)
# print(type(a))

# Adding values to an empty set
a.add(1)
a.add(2)
a.add(3)
a.add(3)  # adding a value repeatedly does not changes a set

a.add((4, 5, 6))  # tuple can add to the set bcoz tuple cannot further change as set 

# a.add([110,11])  # list cannot add to the set bcoz list can further change but set cannot further change

# a.add({33:12})  # dictionary cannot add to the set bcoz dictionary can further change but set cannot further change

# print(a)

# print(len(a))

# print(a)
# a.remove(2)  # removes 2 from set a
# a.remove(12)  # throws an error while trying to removes 12 from set a bcoz 12 is not present to the set
# print(a)

# print(a)
# print(a.pop())
# print(a)

# print(a)
# print(a.clear()) # it removes all the values that present in the set

# print(a)
# print(a.union({77, 88, 99}))

print(a)
print(a.intersection({1, 2, 3}))