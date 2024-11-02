student_percentage = float(input("Input student percentage: "))

if student_percentage > 90:
    print("Grade: A")
elif student_percentage > 80 and student_percentage <= 90:
    print("Grade: A-")
elif student_percentage > 70 and student_percentage <= 80:
    print("Grade: B")
elif student_percentage > 60 and student_percentage <= 70:
    print("Grade: C")
else:
    print("Grade: FAIL")
