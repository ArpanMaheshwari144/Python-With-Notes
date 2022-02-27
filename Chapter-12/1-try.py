while(True):
    print("Press q to quit")
    a = input("Enter a number: ")
    if a == 'q':
        break
    try:
        print("Trying.....")
        a = int(a)
        if a%2==0:
            print("Your number is divisible by 2")
    except Exception as e:
        print(f"Your input result is an error: {e}")
        
print("Thanks!!")