# min, Sum and Max Function
# With Dinamic Data

students_marks = []
a = int(input("Enter first mark: "))
students_marks.append(a)

b = int(input("Enter second mark: "))
students_marks.append(b)

c= int(input("Enter third mark: "))
students_marks.append(c)

d = int(input("Enter fourth mark: "))
students_marks.append(d)

e = int(input("Enter fifth mark: "))
students_marks.append(e)

f = int(input("Enter sixth mark: "))
students_marks.append(f)

g = int(input("Enter seventh mark: "))
students_marks.append(g)

h = int(input("Enter eighth mark: "))
students_marks.append(h)

number_of_students = len(students_marks)
print(f" Total number of students: {number_of_students}")

students_marks.sort() 
print(f" The Four hiest scores: {students_marks[0:4]}")

minM = students_marks[0] #Other wise use the min() function
maxM = students_marks[-1] #Other wise use the max() function
print(f"Minimum: {minM} \n Maximum: {maxM}")

averageScore = sum(students_marks)/number_of_students
print(f"Average Score: {averageScore}")