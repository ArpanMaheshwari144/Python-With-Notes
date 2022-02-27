def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

greater_than_10 = lambda num: num > 10

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list(filter(greater_than_5, l)))
print(list(filter(greater_than_10, l)))