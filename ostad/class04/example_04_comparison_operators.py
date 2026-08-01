"""
Example 04: Comparison Operators
Ostad Batch 11 - Live Class 04 (Module 2: Logic & Condition Building)

Goal: See how Python's comparison operators work - each one compares two
values and evaluates to a Boolean (True/False) result. These are the
building blocks of every if/elif condition.

Operators covered:
    >   Greater Than
    <   Less Than
    >=  Greater Than or Equal To
    <=  Less Than or Equal To
    ==  Equal To
    !=  Not Equal To

How to run (in terminal):
    python example_04_comparison_operators.py
"""

# ----- INPUT Phase -----
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# ----- PROCESS + OUTPUT Phase -----
print(f"{a} > {b}  ->", a > b)
print(f"{a} < {b}  ->", a < b)
print(f"{a} >= {b} ->", a >= b)
print(f"{a} <= {b} ->", a <= b)
print(f"{a} == {b} ->", a == b)
print(f"{a} != {b} ->", a != b)

# Expected Output (example - first number 10, second number 7):
# Enter first number: 10
# Enter second number: 7
# 10 > 7  -> True
# 10 < 7  -> False
# 10 >= 7 -> True
# 10 <= 7 -> False
# 10 == 7 -> False
# 10 != 7 -> True
