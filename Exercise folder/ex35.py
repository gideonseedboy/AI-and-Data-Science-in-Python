#Sort Function

namesOfMembers  = ["ojong damian","monde denzel","abigail abunow","monde denzel","gideon abunow","monde denzel","mario ashu","bronze Jr","ayuk tabe"]
namesOfStudentMembers = ["ojong damian", "monde denzel","abigail abunow","monde denzel","Gideon abunow","gideon abunow","monde denzel","mario ashu","bronze Jr","ayuk tabe"]
studentsAge = [30,52,56,23,23,23,78,5]

namesOfMembers.sort()
print(namesOfMembers)

print("*"*50)
studentsChronologically = namesOfStudentMembers.sort()
print(namesOfStudentMembers)

print("*"*50)
# studentsAgeSorted = studentsAge.sort() # Assigning a sort function to a variable is illegal in Python
studentsAge.sort()
print(studentsAge)
