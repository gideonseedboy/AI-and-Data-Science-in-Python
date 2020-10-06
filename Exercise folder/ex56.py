x = int(input("Enter value x: "))
y = int(input("Enter value y: "))
z = int(input("Enter value z: "))

if x>y:
    if x>z:
        print(f"{x} is the highest")
if y>x:
    if y>z:
        print(f"{y} is the highest")
if z>y:
    if z>x:
        print(f"{z} is the greatest")  