def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Please pass a valid value to function")

a = increment('dhgf12')
print(a)
