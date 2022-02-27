greetings = "Good Morning, "
name = "Arpan"

# print(greetings + name)  # string concatenation

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])

# --> ek baar assign hone ke baad ab string ka koi bhi character change nhi kiya jaa sakta hai 
# name[1] = 'd'
  
print(name[0:3])  # 0 se 3-1 tak string return hogi
print(name[1:3])  # 1 se 3-1 tak string return hogi
print(name[:4])   # 0 se 4-1 tak string return hogi
print(name[0:])   # 0 se 5-1 tak string return hogi
print(name[-4:-1]) # is same as name[1:4]
print(name[0:4:2]) # 0 se 4-1 tak string return hogi or one character skip hoga
print(name[0::2]) # 0 se 5-1 tak string return hogi or one character skip hoga
print(name[0::3]) # 0 se 5-1 tak string return hogi or two character skip honge
