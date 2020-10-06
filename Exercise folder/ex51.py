

firstnumber = int(input("Enter first number: "))
secondnumber = int(input("Enter second number: "))



if firstnumber>secondnumber:
    print("First number is highest!")
elif firstnumber==secondnumber:
    print("The numbers are equal")
else:
    print("The two numbers are equal!")

age = int(input("Enter Age: "))
agelimit = 18


if age>=agelimit:
    print("You are elligible to vote")
else:
    print(f"Sorry you are not elegible to vote you will be eligible to vote in {int(agelimit)-int(age)} years!")


