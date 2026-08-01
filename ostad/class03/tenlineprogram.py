# MILES_PER_KM = 0.621371
# distance_km = float(input("Enter distance in kilometers: "))
# distance_miles = distance_km * MILES_PER_KM
# # print(f"Distance in miles: {distance_miles:.2f} miles")

# print(f"{distance_km} km is approximately {distance_miles:.2f} miles.")


# a = 100
# a = b
# b = temp
# # print(f"After swapping: a = {a}, b = {b}")
# print(f"After swapping: a = ",a)

# print(f"After swapping: b = ",b)


ch = input("Enter a character: ")
# small_letter = ch.lower()  # convert to lowercase

small_letter = chr(ord(ch) + 32)  # convert to lowercase

capital_letter = chr(ord(ch) - 32)  # convert to uppercase
print(f"The ASCII value of '{ch}' is: {ord(ch)}")  # using ord() to get ASCII value
print(f"The lowercase of '{ch}' is: {small_letter}")
print(f"The uppercase of '{ch}' is: {capital_letter}")
