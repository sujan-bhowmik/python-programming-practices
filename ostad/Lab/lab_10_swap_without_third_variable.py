a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("Before swap: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swap: a =", a, ", b =", b)
