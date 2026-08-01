weather = "rain"

if weather == "rain":
    print("Take an umbrella")
elif weather == "sunny":
    print("Take a cap")
else:
    print("Enjoy your day")

# if = যদি
# elif = নাহলে যদি
# else = অন্য সব ক্ষেত্রে

"""
Example 01: if / else Basics
Ostad Batch 11 - Live Class 04 (Module 2: Logic & Condition Building)

Goal: Understand how a program makes a decision using if and else.
A condition is any expression that Python can evaluate to True or False.
How to run (in terminal):
    python example_01_if_else_basics.py
"""

# ----- INPUT Phase -----
# input() always returns a string, so we convert to int for numeric comparison.
age = int(input("Enter your age: "))

# ----- PROCESS + OUTPUT Phase -----
# The expression "age >= 18" evaluates to a boolean (True or False).
# If it is True, the indented block under "if" runs.
# Otherwise, the block under "else" runs.
if age >= 18:
    print("You are an adult.")
    print("You are eligible to vote.")
else:
    print("You are a minor.")
    print("Please wait a few more years to vote.")

# This line is OUTSIDE the if/else block (no indentation),
# so it always runs no matter which branch was taken.
print("Decision complete. Thank you.")

# Expected Output (example 1):
# Enter your age: 22
# You are an adult.
# You are eligible to vote.
# Decision complete. Thank you.
#
# Expected Output (example 2):
# Enter your age: 15
# You are a minor.
# Please wait a few more years to vote.
# Decision complete. Thank you.
