"""
Example 02: elif Chain - Grading System
Ostad Batch 11 - Live Class 04 (Module 2: Logic & Condition Building)

Goal: Use an if / elif / else chain to map a numeric score to a grade.
Key idea: Python checks each condition top to bottom and runs the FIRST
one that is True, then skips the rest of the chain.
How to run (in terminal):
    python example_02_elif_grading.py
"""

# ----- INPUT Phase -----
marks = float(input("Enter your marks (0 - 100): "))

# ----- PROCESS + OUTPUT Phase -----
# Order matters: we check from the highest boundary downwards.
# Because only the first matching branch runs, we do not need to
# write the upper bound again (e.g. "marks >= 80 and marks < 90").
if marks < 0 or marks > 100:
    grade = "Invalid"
    print("Marks must be between 0 and 100.")
elif marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F (Fail)"

print(f"Marks: {marks} -> Grade: {grade}")

# Expected Output (example 1):
# Enter your marks (0 - 100): 84
# Marks: 84.0 -> Grade: A+
#
# Expected Output (example 2):
# Enter your marks (0 - 100): 47
# Marks: 47.0 -> Grade: C
#
# Expected Output (example 3):
# Enter your marks (0 - 100): 33
# Marks: 33.0 -> Grade: F (Fail)
