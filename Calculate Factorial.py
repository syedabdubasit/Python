number = int(input("To calculate factorial of number: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print("The factorial of", number, "is:", factorial)
