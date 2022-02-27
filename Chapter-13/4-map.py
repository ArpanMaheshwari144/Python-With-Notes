# Using normal method
# def square(num):
#     return num * num

# l1 = [1, 2, 4]
# l2 = []
# for item in l1:
#     l2.append(square(item))
# print(l2)


# using map
def square(num):
    return num * num

l1 = [1, 2, 4]
print(list(map(square, l1)))