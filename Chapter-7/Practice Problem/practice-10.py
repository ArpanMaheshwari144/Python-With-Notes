num = int(input("Enter a number to print multiplication table on reverse order: "))
for i in range(10, 0, -1):
    print(f"{num} X {i} = {num*i}")   # fstrings
