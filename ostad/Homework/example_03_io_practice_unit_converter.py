"""
Example 03: Hands-On I/O Practice - Kilometers to Miles Converter
Live Class 03 - Practice Session

Goal: A short, live, type-along practice exercise combining input(),
float conversion, an arithmetic expression, and f-string formatting -
the exact same pattern used in every real-world small utility program.
"""

MILES_PER_KM = 0.621371

distance_km = float(input("Enter distance in kilometers: "))
distance_miles = distance_km * MILES_PER_KM

print(f"{distance_km} km is approximately {distance_miles:.2f} miles")
