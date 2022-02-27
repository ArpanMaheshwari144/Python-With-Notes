class Number:
    def sum(self):
        return self.a + self.b


num = Number()  # object instantiation
num.a = 12
num.b = 12
s = num.sum()
print(s)