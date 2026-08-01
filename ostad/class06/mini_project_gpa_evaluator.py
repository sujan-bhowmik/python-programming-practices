"""
Mini Project (Option A): Grade Evaluator
Ostad Batch 11 - Live Class 06 (Module 2: Logic & Condition Building)

Combines everything from Live Class 04-05: comparison operators, the
logical operator "and", a truthy/falsy guard on the student ID, a
teacher-login style nested condition (same pattern as the Live Class
05 ATM PIN example), an if-elif-else grading chain, and one more
nested condition for extra feedback - to build a complete Grade
Evaluator that also reports a GPA.

Extra additions:
    - Each grade's GPA value is kept in its own constant (GPA_A_PLUS,
      GPA_A, ...) instead of being written directly next to every "elif".
    - A simple "robot check" (like a mini CAPTCHA) runs first: two random
      numbers are shown, and only a correct sum lets the user continue to
      the student ID + password login - one more nested condition, wrapped
      around the login check.
    - Every branch of the grading chain now has its own small nested
      condition: Invalid marks say exactly which boundary was broken, A+
      splits into a regular pass and a Distinction, B and C tell the
      student how close they are to the next grade, and F distinguishes a
      close call from a result that needs serious improve114ment.

How to run (in terminal):
    python mini_project_grade_evaluator.py
"""

import random

CORRECT_PASSWORD = "Python123"

GPA_A_PLUS = 5.00
GPA_A = 4.00
GPA_A_MINUS = 3.50
GPA_B = 3.00
GPA_C = 2.00
GPA_F = 0.00

robot_1 = random.randint(1, 100)
robot_2 = random.randint(1, 100)


print(f"Check -> What is {robot_1} + {robot_2}=?")
robot_ans = int(input("Enter Your Answer: "))


if robot_ans == robot_1 + robot_2:
    student_id = int(input("Enter your ID:"))
    password = input("Password: ")

    if student_id and password == CORRECT_PASSWORD:
        name = input("Enter Your Name: ")
        marks = float(input("Enter Your Marks (1,100): "))

        if not name:
            name = "Student"

        extra_message = ""

        if marks < 0 or marks > 100:
            grade = "Invalid"
            gpa = 0.00

            if marks < 0:
                extra_message = "Marks cannot be negative."
            else:
                extra_message = "Marks cannot exceed 100."
        elif marks >= 80:
            grade = "A+"
            gpa = GPA_A_PLUS

            if marks >= 90:
                extra_message = "A+ with laddu."
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
            print(
                f"Student ID {student_id}: {name} scored {marks} -> Grade: {grade} (GPA: {gpa:.2f})"
            )
            if extra_message:
                print(extra_message)
            if marks == 100:
                print("Congratulations ! You're too good .. ;p")
    else:
        print("Invalid Id Password!")
else:
    print("Wrong Ans! Robot !")
