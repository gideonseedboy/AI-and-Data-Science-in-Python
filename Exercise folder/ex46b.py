# Functions with Dictionaries


studentsDetails = {}


studentsDetails["student_id1"] = input("Enter Student ID: ")
studentsDetails["student_mark1"] = input("Enter mark: ")


studentsDetails["student_id2"] = input("Enter Student ID: ")
studentsDetails["student_mark2"] = input("Enter mark: ")


studentsDetails["student_id3"] = input("Enter Student ID: ")
studentsDetails["student_mark3"] = input("Enter mark: ")

print(studentsDetails)

print(f""" 
    Students                       ID Number                    Mark       
    Student 1 {studentsDetails["student_id1"] studentsDetails["student_mark1"]}
    Student 2 {studentsDetails["student_id2"] studentsDetails["student_mark2"]}
    Student 3  {studentsDetails["student_id3"] studentsDetails["student_mark3"]}

    """)

