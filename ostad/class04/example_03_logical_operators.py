"""
Example 03: Logical Operators and Short-Circuit Evaluation
Ostad Batch 11 - Live Class 04 (Module 2: Logic & Condition Building)

Goal: Combine multiple conditions using "and", "or", "not".
Also demonstrate short-circuit evaluation, where Python stops checking
as soon as the result is already decided.
How to run (in terminal):
    python example_03_logical_operators.py
"""

# ----- INPUT Phase -----
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ").lower() == "yes"
is_vip = input("Are you a VIP member? (yes/no): ").lower() == "yes"

# ----- PROCESS + OUTPUT Phase -----

# "and": ALL conditions must be True.
# A normal visitor needs both a valid age AND a ticket.
if age >= 18 and has_ticket:
    print("Entry allowed: you are an adult with a ticket.")
else:
    print("Entry denied for the standard gate.")

# "or": AT LEAST ONE condition must be True.
# A VIP can skip the queue, OR a ticket holder can use the normal queue.
if is_vip or has_ticket:
    print("You may proceed to the seating area.")
else:
    print("Please buy a ticket first.")

# "not": reverses a boolean value.
if not has_ticket:
    print("Reminder: you still need to purchase a ticket.")

# ----- Short-circuit demonstration -----
# In "A and B", if A is False, Python never evaluates B.
# In "A or B", if A is True, Python never evaluates B.
# This is useful to guard against errors, e.g. divide-by-zero below.
divisor = 0
if divisor != 0 and (100 / divisor) > 10:
    # The right side (100 / divisor) is never executed because
    # "divisor != 0" is False, so no ZeroDivisionError occurs.
    print("Big result.")
else:
    print("Safe: division was skipped because divisor is zero.")

# Expected Output (example - age 25, ticket yes, vip no):
# Enter your age: 25
# Do you have a ticket? (yes/no): yes
# Are you a VIP member? (yes/no): no
# Entry allowed: you are an adult with a ticket.
# You may proceed to the seating area.
# Safe: division was skipped because divisor is zero.
