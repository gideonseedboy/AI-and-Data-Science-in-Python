# Seperating even numbers from odd numbers in a given range!

evenNums = []
oddNums = []
for i in range(1, 101):
    if i%2==0:
        evenNums.append(i)
    else:
        oddNums.append(i)

print(f"Even numbers are: {evenNums}")
print(f"Odds numbers are: {oddNums}")