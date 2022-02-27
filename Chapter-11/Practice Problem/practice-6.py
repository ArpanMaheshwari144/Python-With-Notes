class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}i + {self.vec[2]}i"


v1 = Vector([1, 4, 6])
print(v1)
