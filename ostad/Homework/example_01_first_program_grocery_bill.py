"""
Example 01: Your First 10-Line Program - Grocery Bill Calculator
Live Class 03 - Practice Session

Goal: Combine everything from Class 01 (print, input) into ONE small,
complete program you could write from scratch in a live session -
input, type conversion, an expression, and a formatted output.
"""

item_name = input("Item name: ")
price = float(input("Price per unit: "))
quantity = int(input("Quantity: "))

total = price * quantity

print("\n----- Grocery Bill -----")
print(f"Item     : {item_name}")
print(f"Price    : {price:.3f}")
print(f"Quantity : {quantity}")
print(f"Total    : {total:.4f}")
