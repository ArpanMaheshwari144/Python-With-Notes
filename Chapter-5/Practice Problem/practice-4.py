s = set()
s.add(20)
s.add(20.0)  # 20.0 --> 20 and set does not allow duplicate values
s.add("20")
print(s)
print(len(s))
