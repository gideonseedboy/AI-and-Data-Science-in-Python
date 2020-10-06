# loop
#for loop


age = []
cycles = int(input("Enter number of cycles: "))

for k in range(cycles):
    x = int(input("Enter your age: "))
    age.append(x)


totalAge = sum(age)
maxAge = max(age)
minAge = min(age)


print(f"Sumation of ages is: {age}")
print(f"Maximum age was: {maxAge}")
print(f"Minimum age was: {minAge}")