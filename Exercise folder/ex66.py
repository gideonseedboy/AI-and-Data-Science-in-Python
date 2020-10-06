

number = int(input("Enter number: "))
factorial = 1
for x in range(1, number+1):
    factorial = factorial * (x)

print(f"Factorial of {number} is: {factorial}")

