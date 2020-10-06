# Excercise: Students_marks [50, 30, 41,52, 74, 23, 60, 41]

# i) Find Total Students
# ii) Find find the first four highest scores
# iii) Find the minimum and the maximum scores
# iv) Find the average Score


students_marks = [50, 30, 41,52, 74, 23, 60, 41]

number_of_students = len(students_marks)
print(f" Total number of students: {number_of_students}")

students_marks.sort() 
print(f" The Four hiest scores: {students_marks[0:4]}")

minM = students_marks[0] #Other wise use the min() function
maxM = students_marks[-1] #Other wise use the max() function
print(f"Minimum: {minM} \n Maximum: {maxM}")

averageScore = sum(students_marks)/number_of_students
print(f"Average Score: {averageScore}")