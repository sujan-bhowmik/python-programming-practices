"""
Example 06: Homework Walkthrough - Temperature Converter
Live Class 03 - Practice Session

This is the worked solution to Class 02's Assignment #3: take a Celsius
value and convert it to both Fahrenheit and Kelvin, shown to 2 decimals.
"""

KELVIN_OFFSET = 273.15

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + KELVIN_OFFSET

print(f"{celsius:.2f} C = {fahrenheit:.2f} F")
print(f"{celsius:.2f} C = {kelvin:.2f} K")

# Expected Output (example):
# Enter temperature in Celsius: 25
# 25.00 C = 77.00 F
# 25.00 C = 298.15 K
