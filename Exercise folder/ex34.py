#Defining a Dictionary
#  Key and Value

peopleAndAges = {"gideon":34, "denzel":22, "mario":28, "grace":24,"tabitha":27}


#Outputing values in a dictionary
print(peopleAndAges["gideon"])

print(peopleAndAges["grace"])

#Other methods of outputting elements within a dictionary

x = peopleAndAges.get("denzel")
print(x)

y = peopleAndAges.get("mario")
print("*"*30)
print(y)

print("*"*26)
z = peopleAndAges.get("tabitha")
print(z)

print("*"*50)
#How to insert element into a dictionary!
print("*"*50)

peopleAndAges["francis"] = 26
peopleAndAges["solomon"] = 22

print("*"*50)

print(peopleAndAges)