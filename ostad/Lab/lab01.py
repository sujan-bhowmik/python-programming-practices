# Task 01: Write a Python program that will print your name.

print("Sujan Bhowmik")  # Replace with your name

# Task 02: Write a Python program that will print your name, your father's and mother's name in three separate lines.

print("My Name:Sujan Bhowmik")  # Replace with your name
print("Father's Name: Late Bijoy Krishna Bhowmik")  # Replace with your father's name
print("Mother's Name: Arati Rani Bhowmik")  # Replace with your mother's name

# Task 03: Write a Python program that will print the sum of two variables a and b; where a = 10 and b = 20.
a = 10
b = 20
sum = a + b
print("The sum of a and b is:", sum)  # Output: The sum of a and b is: 30

# Task 04: Write a Python program to calculate the sum of two integer numbers (given by the user) and print it.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print("The sum of the two numbers is:", sum)

# Task 05: Write a Python program that will take three numbers from the user and find their average.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
average = (number1 + number2 + number3) / 3
print("The average of the three numbers is:", average)

# Task 06: Write a Python program that will take three integers as input from the user and print their average. (Use type-cast to get the proper result)
number1 = int(input("Enter first number: "))
number2 = int(input("Enter Second number: "))
number3 = int(input("Enter third number: "))
average = (number1 + number2 + number3) / 3
print(
    f"The average of the three numbers is: {average:.2f}"
)  # Output: The average of the three numbers is: 20.00

# Task 07: Write a Python program to convert a Km value into a meter value.
km = float(input("Enter distance in kilometers: "))
meters = km * 1000
print(f"Distance in meters is: {meters}")

# Task 08: Write a Python program to convert a Celsius value into a Fahrenheit value. (Formula: F = C * 9/5 + 32)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"Temperature in Fahrenheit is: {fahrenheit:.2f}")

# Task 09: Write a Python program to interchange the values of two numbers using a third variable.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
temp = number1
number1 = number2
number2 = temp
print(f"After interchange: First number = {number1:.2f}, Second number = {number2:.2f}")

# Task 10: Write a Python program to interchange the values of two numbers without using a third variable.
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number1, number2 = number2, number1
print(f"After interchange: First number = {number1:.2f}, Second number = {number2:.2f}")

# Task 11: Write a Python program to input two numbers and print their quotient and remainder.
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
quotient = number1 // number2
remainder = number1 % number2
print(f"Quotient: {quotient}, Remainder: {remainder}")

# Task 12: Write a Python program to accept any character from the user and display its ASCII number on screen.
ch = input("Enter a character: ")
ascii_value = ord(ch)
print(f"ASCII value of '{ch}' is: {ascii_value}")

# Task 13: Write a Python program to input any ASCII number and display the appropriate character on screen.
ascii_number = int(input("Enter an ASCII number: "))
ch = chr(ascii_number)
print(
    f"display the appropriate character on screen for ASCII number {ascii_number} is: {ch}"
)

# Task 14: Write a Python program to input any capital letter and display it in small letter.
ch = input("Enter a capital letter: ")
small_letter = chr(ord(ch) + 32)  # convert to lowercase
print(f"Small letter of '{ch}' is: {small_letter}")

# Task 15: Write a Python program to input any small letter and display it in capital letter.
ch = input("Enter a small letter: ")
capital_letter = chr(ord(ch) - 32)  # convert to uppercase
print(f"Capital letter of '{ch}' is: {capital_letter}")

# Task 16: Write a Python program to input any capital letter and display it in small letter. (Without using the lower() method)
ch = input("Enter a capital letter: ")
small_letter = chr(ord(ch) + 32)  # convert to lowercase
print(f"Small letter of '{ch}' is: {small_letter}")

# Task 17: Write a Python program to input any small letter and display it in capital letter. (Without using the upper() method)
ch = input("Enter a small letter: ")
capital_letter = chr(ord(ch) - 32)  # convert to uppercase
print(f"Capital letter of '{ch}' is: {capital_letter}")

# Task 18: Write a Python program to input the number of days from the user and convert it into years, months and days.
days = int(input("Enter Number of Days:"))
years = days // 365
years_quotient = days % 365
months = years_quotient // 12
months_quotient = years_quotient % 12
days = months_quotient

print(years, "years", months, "months and ", days, "days")

# Task 19: Write a Python program to input a three-digit number from the user and calculate the sum of the first and last digits. (Hint: Input: 358, Output: 11)

number = int(input("Enter a Three Digit Number"))
first_digit = number // 100
last_digit = number % 10
sum = first_digit + last_digit
print("sum of the first and last digits is: ", sum)

# Task 20: Write a Python program to input a three-digit number from the user and display the square of the first and last digits. (Hint: Input: 358, Output: Square of 3 is 9 and Square of 8 is 64)

number = int(input("Enter a Three Digit Number"))
first_digit = number // 100
last_digit = number % 10
sq_first = first_digit * first_digit
sq_last = last_digit * last_digit
print(
    "Square of the first digit",
    first_digit,
    "is: ",
    sq_first,
    "Square of the last digit",
    last_digit,
    "is: ",
    sq_last,
)

# alternative way

number = int(input("Enter a Three Digit Number"))
first_digit = number // 100
last_digit = number % 10

print(
    f"Square of the {first_digit} is {first_digit ** 2} and Square of the {last_digit} is {last_digit ** 2}"
)


# Task 21: Write a Python program to input a two-digit number from the user and display it with digits reversed. (Hint: Input: 32, Output: 23)

number = int(input("Enter a Two Digit Number"))
first_digit = number // 10
last_digit = number % 10
reversed_number = (last_digit * 10) + first_digit

print(f"Reversed number of {number} is {reversed_number}")

# alternative short_cut

number = input("Enter a two-digit number: ")
print(f"Reversed number of {number} is {number[::-1]}")


# Task 22: Write a Python program to find the quotient and remainder of two numbers. (Without using the modulus % operator)

number1 = int(input("Enter dividend number:"))
number2 = int(input("Enter divisor number:"))

quotient = number1 // number2
remainder = number1 - (quotient * number2)

print(f"Quotient of {number1} and {number2} is {quotient} and remainder is {remainder}")
