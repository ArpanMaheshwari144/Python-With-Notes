def print_multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")


n = int(input("Enter a number to print its multiplication table: "))
print_multiplication_table(n)