#String Formatting II

x = 100
y = 50
z = 100


#Addition
add = x + y + z

#Multiplication

mul = x*y*z
proZ = (mul/z) - x


print("Submission "+str(add))
print(f"Submission {add}")
print(f"The Product is {mul}")
print(f"Result is {proZ}")
print(int(proZ))


#Compressing all Print Comands on one line
print("This is to Summarize all the print commands into one!")
print(f"Submission {add} The Product is {mul} Result is {proZ} {int(proZ)}")