# marks1 = [45, 78, 86, 77]
# percentage1 = ((marks1[0] + marks1[1] + marks1[2] + marks1[3])/400)*100
#            # OR
# # percentage1 = (sum(marks1)/400)*100


# marks2 = [75, 98, 88, 78]
# percentage2 = ((marks2[0] + marks2[1] + marks2[2] + marks2[3])/400)*100
#             # OR
# # percentage2 = (sum(marks2)/400)*100

# print(percentage1, percentage2)

              # OR

def percentage(marks):
    per = (sum(marks)/400)*100
    return per

marks1 = [75, 98, 88, 78]
marks2 = [55, 78, 67, 88]
print(percentage(marks1))
print(percentage(marks2))