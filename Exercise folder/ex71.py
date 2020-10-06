#loop
#while loop
#While loops work with conditions as For Loops work with Range

#Finding the sumation of all numbers between a Low Integer and a High Integer

number = int(input("Enter high integer: "))
sum = 0
i = int(input("Enter low integer: "))
while i <= number:
    sum = sum+i
    i+= 1

print(f"sumation: {sum}")

