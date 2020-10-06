#Excercise 24
# Signup Form


print("STUDENT'S VITAL INFO")
print("Enter First Name")
surName = input()
print("Enter Last Name")
firstName = input()
print("Enter Middle Name")
middleName = input()
print("Enter Gender")
_gender = input()
print("Enter Address")
_address = input()
print("What's your School Fee")
_schFee = input()



print("STUDENT'S CAMPUS INFO")
print("Enter your University")
nameOfUniversity = input()

print("Enter your Faculty")
stuFaculty = input()


print("Enter your Department")
stuDepartment = input()

print("Enter your Email")
email = input()

print("Enter your password")
password = input()

#Excercise Extra
# Signup Form

print(f"""
                            GIDEON'S UNIVERSITY STUDENTS PORTALS
 ******************************* Student's Record *****************************

                        Students Deatails are as follows:

        STUDENT'S VITAL INFO
                        
 Surname :              {surName} 
 Middle name:           {firstName}
 Other name:            {middleName},
 Gender:                {_gender} 
 Address                {_address} 
 School Fee             ${_schFee}

        STUDENT'S CAMPUS INFO

Name of University:     {nameOfUniversity}
Student's Facullty:     {stuFaculty}
Student's Department:   {stuDepartment}
Student Email:          {email}
Password                {f" Private"}
------------------------------------------------------------------------------
..................Developed By Ojay Technologies Incorporated..................
 """)
