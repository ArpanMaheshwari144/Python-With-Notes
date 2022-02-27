def celsiusToFahrenhiet(cel):
    return (cel * (9/5)) + 32


num = int(input("Enter a temperature to covert it into fahrenhiet:"))
temp = celsiusToFahrenhiet(num)
print(f"The {num}°C = {temp}°F")
