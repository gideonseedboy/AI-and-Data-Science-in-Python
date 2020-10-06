#function

def opperateFunction():
    a = int(input("Enter Integer: "))
    b = int(input("Enter Integer: "))
    c = int(input("Enter Integer: "))

    sumResult = a + b + c
    prodResult = a * b * c
    defResult = a - b - c
    print(f"""
        Sumation :  {sumResult}
        Product:    {prodResult}
        Defference: {defResult}
    """)
opperateFunction()

def multiplication():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))

    result = x * y
    print(f"Product: {result}")

def division():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))
    
    result = x / y
    print(f"Dividence: {result}")

def addition():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))

    result = x - y
    print(f"Sumation: {result}")

def subtraction():
    x = int(input("Enter x value: "))
    y = int(input("Enter y value: "))

    result = x - y
    print(f"Difference between{x} and {y}: {result}")

operator = input("Enter  operator *, /, +, or -: ")

if operator=="*":
    multiplication()
elif operator=="/":
    division()
elif operator=="+":
    addition()
elif operator=="-":
    subtraction()
else:
    print("Operator is unknown!")

