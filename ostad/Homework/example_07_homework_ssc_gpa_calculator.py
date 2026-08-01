"""
Example 07: Homework Walkthrough - SSC Result & GPA Calculator (Bonus)
Live Class 03 - Practice Session

This is the worked solution to Class 02's Assignment #4 (bonus mini project):
take five subjects' marks, convert each to a grade point using the real
Bangladesh SSC grading scale, then compute the final GPA. If ANY subject's
grade point is 0.00 (an F, marks below 33), the final GPA becomes 0.00 and
the result is "Failed" - matching the real SSC rule (one failed subject
fails the whole result, no matter what the average of the other four is).

NOTE: written as one plain top-to-bottom script (no functions, no loops) -
each subject's grade lookup is its own if/elif/else chain, same pattern as
mini_project_student_report.py from Class 02.
"""

GRADE_A_PLUS = 80
GRADE_A = 70
GRADE_A_MINUS = 60
GRADE_B = 50
GRADE_C = 40
GRADE_D = 33
NUMBER_OF_SUBJECTS = 5

# ----- Header -----
print("=" * 50)
print("   SSC RESULT & GPA CALCULATOR")
print("=" * 50)

# ----- INPUT Phase -----
student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

bangla_marks = float(input("Enter Bangla marks (0-100): "))
english_marks = float(input("Enter English marks (0-100): "))
math_marks = float(input("Enter Math marks (0-100): "))
science_marks = float(input("Enter Science marks (0-100): "))
religion_marks = float(input("Enter Religion marks (0-100): "))

# ----- PROCESS Phase: one grade-lookup chain per subject -----
if bangla_marks >= GRADE_A_PLUS:
    bangla_grade, bangla_point = "A+", 5.00
elif bangla_marks >= GRADE_A:
    bangla_grade, bangla_point = "A", 4.00
elif bangla_marks >= GRADE_A_MINUS:
    bangla_grade, bangla_point = "A-", 3.50
elif bangla_marks >= GRADE_B:
    bangla_grade, bangla_point = "B", 3.00
elif bangla_marks >= GRADE_C:
    bangla_grade, bangla_point = "C", 2.00
elif bangla_marks >= GRADE_D:
    bangla_grade, bangla_point = "D", 1.00
else:
    bangla_grade, bangla_point = "F", 0.00

if english_marks >= GRADE_A_PLUS:
    english_grade, english_point = "A+", 5.00
elif english_marks >= GRADE_A:
    english_grade, english_point = "A", 4.00
elif english_marks >= GRADE_A_MINUS:
    english_grade, english_point = "A-", 3.50
elif english_marks >= GRADE_B:
    english_grade, english_point = "B", 3.00
elif english_marks >= GRADE_C:
    english_grade, english_point = "C", 2.00
elif english_marks >= GRADE_D:
    english_grade, english_point = "D", 1.00
else:
    english_grade, english_point = "F", 0.00

if math_marks >= GRADE_A_PLUS:
    math_grade, math_point = "A+", 5.00
elif math_marks >= GRADE_A:
    math_grade, math_point = "A", 4.00
elif math_marks >= GRADE_A_MINUS:
    math_grade, math_point = "A-", 3.50
elif math_marks >= GRADE_B:
    math_grade, math_point = "B", 3.00
elif math_marks >= GRADE_C:
    math_grade, math_point = "C", 2.00
elif math_marks >= GRADE_D:
    math_grade, math_point = "D", 1.00
else:
    math_grade, math_point = "F", 0.00

if science_marks >= GRADE_A_PLUS:
    science_grade, science_point = "A+", 5.00
elif science_marks >= GRADE_A:
    science_grade, science_point = "A", 4.00
elif science_marks >= GRADE_A_MINUS:
    science_grade, science_point = "A-", 3.50
elif science_marks >= GRADE_B:
    science_grade, science_point = "B", 3.00
elif science_marks >= GRADE_C:
    science_grade, science_point = "C", 2.00
elif science_marks >= GRADE_D:
    science_grade, science_point = "D", 1.00
else:
    science_grade, science_point = "F", 0.00

if religion_marks >= GRADE_A_PLUS:
    religion_grade, religion_point = "A+", 5.00
elif religion_marks >= GRADE_A:
    religion_grade, religion_point = "A", 4.00
elif religion_marks >= GRADE_A_MINUS:
    religion_grade, religion_point = "A-", 3.50
elif religion_marks >= GRADE_B:
    religion_grade, religion_point = "B", 3.00
elif religion_marks >= GRADE_C:
    religion_grade, religion_point = "C", 2.00
elif religion_marks >= GRADE_D:
    religion_grade, religion_point = "D", 1.00
else:
    religion_grade, religion_point = "F", 0.00

# ----- GPA + the "one F fails everything" rule -----
average_point = (bangla_point + english_point + math_point
                  + science_point + religion_point) / NUMBER_OF_SUBJECTS

has_failed = (bangla_point == 0.00 or english_point == 0.00 or math_point == 0.00
              or science_point == 0.00 or religion_point == 0.00)

if has_failed:
    final_gpa = 0.00
    result = "Failed"
else:
    final_gpa = average_point
    result = "Passed"

# ----- OUTPUT Phase -----
print("\n" + "-" * 50)
print(f"Name        : {student_name}")
print(f"Roll Number : {roll_number}")
print("-" * 50)
print(f"{'Subject':<12}{'Marks':>8}{'Grade':>8}{'Point':>8}")
print(f"{'Bangla':<12}{bangla_marks:>8.2f}{bangla_grade:>8}{bangla_point:>8.2f}")
print(f"{'English':<12}{english_marks:>8.2f}{english_grade:>8}{english_point:>8.2f}")
print(f"{'Math':<12}{math_marks:>8.2f}{math_grade:>8}{math_point:>8.2f}")
print(f"{'Science':<12}{science_marks:>8.2f}{science_grade:>8}{science_point:>8.2f}")
print(f"{'Religion':<12}{religion_marks:>8.2f}{religion_grade:>8}{religion_point:>8.2f}")
print("-" * 50)
print(f"GPA    : {final_gpa:.2f}")
print(f"Result : {result}")
print("-" * 50)

# Expected Output (example - all subjects pass):
# Enter student name: Tahmid
# Enter roll number: 17
# Enter Bangla marks (0-100): 85
# Enter English marks (0-100): 75
# Enter Math marks (0-100): 65
# Enter Science marks (0-100): 55
# Enter Religion marks (0-100): 90
#
# --------------------------------------------------
# Name        : Tahmid
# Roll Number : 17
# --------------------------------------------------
# Subject        Marks   Grade   Point
# Bangla         85.00      A+    5.00
# English        75.00       A    4.00
# Math           65.00      A-    3.50
# Science        55.00       B    3.00
# Religion       90.00      A+    5.00
# --------------------------------------------------
# GPA    : 4.10
# Result : Passed
# --------------------------------------------------
#
# Expected Output (example - one subject fails, e.g. Math = 30):
# GPA    : 0.00
# Result : Failed
