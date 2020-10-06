number = int(input("Enter number: "))
modeOfNumber = number%2

if modeOfNumber>0 and number>=1:
    print(f"{number} is an ODD number")
elif modeOfNumber==0 and number>=1:
    print(f"{number} is an EVEN number")
else:
    print("Number must be greater than 0, try again with the fight digit")

# Another way that works too

if number>0:
    if number%2==0:
        print(f"{number} is an EVEN number")
    elif number%2==1:
        print(f"{number} is an ODD number")
else:
    print("Enter a number greater that Zero")