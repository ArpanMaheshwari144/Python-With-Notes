def inchesToCms(num):
    return (num * 2.54)


num = int(input("Enter a length to conert it to centimeters: "))
length = inchesToCms(num)
print(f"The {num}inches = {length}centimeters")