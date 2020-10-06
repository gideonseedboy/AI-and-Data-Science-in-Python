#functions

def addition(a, b):
    result = a + b
    print(f"Sumation: {result}")

def subtraction(a, b):
    result = a - b
    print(f"Deifference: {result}")

num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))
operator = input("Choose one of the operators + or -: ")

if operator=="+":
    addition(num1, num2)
elif operator=="-":
    subtraction(num1, num2)
else:
    print(f"Operator unknown ")