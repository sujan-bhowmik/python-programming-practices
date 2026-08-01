# even - odd number


number = 1

even_count = 0

odd_count = 0

while number < 10:
    if number % 2 == 0:
        print(number, "is even") 
        even_count += 1
    else:
        odd_count += 1
        print(number, "is odd")
    number += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
