import random

CORRECT_PASSWORD = "Python123"

GPA_A_PLUS = 5.00
GPA_A = 4.00
GPA_A_MINUS = 3.50
GPA_B = 3.00
GPA_C = 2.00
GPA_F = 0.00


robot_1 = random.randint(1,100)
robot_2 = random.randint(1,100)


print("R-1", robot_1)
print("R-2",robot_2)


print(f"Check -> What is {robot_1} + {robot_2} = ?")

robot_ans = int(input("Enter Your Answer: "))

if robot_ans == robot_1 + robot_2:
    student_id = int(input("Enter Your Student ID: "))
    password = input("Password: ")

    if student_id and password == CORRECT_PASSWORD:
        name = input("Enter Your Name: ")
        marks = float(input("Enter Your Marks(1,100):"))

        if not name:
            name = "Student"

            extra_message = ""

        if marks < 0 or marks > 100:
            grade = "Invalid"
            gpa = 0.00

            if marks < 0:
                extra_message = "Marks can not be negative."
            else:
                extra_message = "Marks cannot exceed 100."

    elif marks >= 80:
        grade = "A+"
        gpa = GPA_A_PLUS

        if marks >= 90:
           extra_message = "A+ with laddu"

    elif marks >= 70:
        grade = "A"
        gpa = GPA_A
    elif marks >= 60:
        grade = "A-"
        gpa = GPA_A_MINUS
    elif marks >= 50:
        grade = "B"
        gpa = GPA_B
    elif marks >= 40:
        grade = "C"
        gpa = GPA_C
    else:
        grade = "F"
        gpa = GPA_F

    if grade == "Invalid":
        print(extra_message)
    else:
        print(f"Student ID {student_id}: {name} scored {marks} -> Grade: {grade} (GPA: {gpa:.2f}) ")

else:
    print("Invalid ID or Password!")
    
   