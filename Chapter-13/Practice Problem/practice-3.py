l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

a = filter(lambda num: num%5==0, l)
print(list(a))