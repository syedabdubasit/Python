student_marks = int(input("Input Student's Marks: "))

if student_marks < 1 or student_marks > 100:
    print("Input a valid marks between 1 and 100.")
else:
    if student_marks < 50:
        grade = 'F'
    elif student_marks <= 60:
        grade = 'E'
    elif student_marks <= 70:
        grade = 'D'
    elif student_marks <= 80:
        grade = 'C'
    elif student_marks <= 90:
        grade = 'B'
    else:
        grade = 'A'
    print("Grade:", grade)
