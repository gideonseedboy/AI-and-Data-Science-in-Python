#1 Write a python Program to Convert the following

#Convert the following into int

a1 = 10
b1 = 3.14
c1 = "251"
d1 = "41.52"

a1Int = int(a1)
b1Int = int(b1)
c1Int = int(c1)
# d1Int = int(d1) #Problem

print(f"A1 into Integer: {a1Int}")
print(f"B1 into Integer: {b1Int}")
print(f"C1 Integer is: {c1Int}")
#print(f" D1 Into Integer is: {d1Int}") # PS C:\Users\ACER\Desktop\python> python ex18b.py

#This is the problem Statement I got because of the line 13
# Traceback (most recent call last):
#   File "ex18b.py", line 13, in <module>
#     d1Int = int(d1, 2)
# ValueError: invalid literal for int() with base 2: '41.52'


#Convert the following into string(str)

a2 = 3.214
b2 = 41
c2 = 74.25

a2Str = str(a2)
b2Str = str(b2)
c2Str = str(c2)

print(f"A2 to String: {a2Str}")
print(f"B2 to String: {b2Str}")
print(f"C2 to String: {c2Str}")




#Convert the following to float

a3 = 9
b3 = "52"
c3 = 96.47
d3 = "41.51"

a3Float = float(a3)
b3Float = float(b3)
c3Float = float(c3)
d3Float = float(d3)

print(f"A3 Into Float is: {a3Float}")
print(f"B3 Into Float is: {b3Float}")
print(f"C3 Into Float is: {c3Float}")
print(f"D3 Into Float is: {d3Float}")


