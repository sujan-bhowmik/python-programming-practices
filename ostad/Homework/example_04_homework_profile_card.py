"""
Example 04: Homework Walkthrough - Profile Card
Live Class 03 - Practice Session

This is the worked solution to Class 02's Assignment #1 (profile_card.py):
take name, city, and profession, then display them as a bordered card
using f-strings and aligned formatting.
"""

name = input("Name: ")
city = input("City: ")
profession = input("Profession: ")

print("=" * 40)
print(f"{'PROFILE CARD':^40}")
print("=" * 40)
print(f"{'Name':<12}: {name}")
print(f"{'City':<12}: {city}")
print(f"{'Profession':<12}: {profession}")
print("=" * 40)
