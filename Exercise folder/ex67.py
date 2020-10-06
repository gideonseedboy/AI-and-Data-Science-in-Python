idList = []
ageList = []
genderList = []

totalStudents = int(input("Enter number of students: "))

for i in range(totalStudents):
    student_id = input("Enter student ID: ")
    idList.append(student_id)

    student_age = int(input("Enter student Age: "))
    ageList.append(student_age)

    student_gender = input("Gender, type male/female: ")
    genderList.append(student_gender)

    print(".....................................")


for k in range(totalStudents):
    print(f""" 

    ............Students Information.............
    .............................................

    Student List:       {idList[k]}
    Student Age:        {ageList[k]}
    Student Gender:     {genderList[k]}
    
    .............................................
    .............................................
    """)