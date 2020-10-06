# The Logical Operators
# AND => Booth Conditions must be true
# OR => At Least one of the Conditions must be true
# NOT => It Changes the output. In short it reverses the result: It returns false for true and true for false


x = 45
y = 20
m = 20

#And Llogical
print(m==y and x>y and m<x)
print(m==y and x==y and m<x)

# OR Llogical Operrator

print(y!=m or m==y or m<x)
print(m<x or x<y or m==x)

# not Logical Operator

print(not(m==y))
print(not(x>y))
print(m<x)


# Using the And Logical Operator Output the following

#         i. false
#         ii. true
#         iii. false


a = 40
b = 40
c = 20


d = a>b and c<b and b<c
e = a==b and b>c
f = c!=a and c==b

print(f" Assignment i is {d}")
print(f" Assignment ii is {e}")
print(f" Assignment iii is {f}")
