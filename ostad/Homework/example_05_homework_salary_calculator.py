"""
Example 05: Homework Walkthrough - Salary Calculator
Live Class 03 - Practice Session

This is the worked solution to Class 02's Assignment #2: take monthly
salary, compute yearly salary and a 10% bonus, and display every amount
with a thousands separator and 2 decimal places ({value:,.2f}).
"""

BONUS_RATE = 0.10

monthly_salary = float(input("Enter monthly salary: "))

yearly_salary = monthly_salary * 12
bonus = yearly_salary * BONUS_RATE
total_with_bonus = yearly_salary + bonus

print("\n----- Salary Summary -----")
print(f"Monthly salary     : {monthly_salary:,.2f}")
print(f"Yearly salary      : {yearly_salary:,.2f}")
print(f"Bonus (10%)        : {bonus:,.2f}")
print(f"Total with bonus   : {total_with_bonus:,.2f}")

# Expected Output (example):
# Enter monthly salary: 45000
#
# ----- Salary Summary -----
# Monthly salary     : 45,000.00
# Yearly salary      : 540,000.00
# Bonus (10%)        : 54,000.00
# Total with bonus   : 594,000.00
