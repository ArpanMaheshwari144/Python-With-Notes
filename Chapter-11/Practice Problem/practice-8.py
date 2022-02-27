class Vector:
    def __init__(self, vec1):
        self.vec1 = vec1

    def __str__(self):
        str1 = ""
        index = 0
        for i in (self.vec1):
            str1 += f"{i}a{index} +"
            index = index + 1
        return str1[:-1]

    def __add__(self, vec2):
        newList = []
        for i in range(len(self.vec1)):
            newList.append(self.vec1[i] + vec2.vec1[i])
        return Vector(newList)

    # multiplication karke add karna
    def __mul__(self, vec2):
        sum = 0 
        for i in range(len(self.vec1)):
            sum += self.vec1[i] * vec2.vec1[i]
        return sum

    def __len__(self):
        return len(self.vec1)
        

v1 = Vector([1, 3, 5])
v2 = Vector([5, 7, 9])

if len(v1) == len(v2):
    print(v1 + v2)
else:
    print("The addition of these vector is not possible because they both are unequal in length")

if len(v1) == len(v2):
    print(v1 * v2)
else:
    print("The multiplication of these vector is not possible because they both are unequal in length")
