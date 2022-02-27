num = int(input("Enter a number to check whether it is prime or not: "))
isPrime = True

if (num==1 or num==0):
    print(f"{num} is not a prime number")
else:
    for i in range(2, num):
        if(num % i == 0):
            isPrime = False
            break

    if(isPrime):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")




