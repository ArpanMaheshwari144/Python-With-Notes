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
        

v1 = Vector([1, 3, 5])
v2 = Vector([5, 7, 9])
print(v1 + v2)
print(v1 * v2)
