# a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 122, 67]
# b = []
# for items in a:
#     if items%2==0:
#         b.append(items)
# print(b)

# above code by list comprehensions
a = [3, 6, 7, 8, 9, 2, 4, 23, 75, 23, 122, 67]
b = [items for items in a if items%2==0]
print(b)