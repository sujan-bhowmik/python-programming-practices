age = int("25")  # str -> int
price = float("99.5")  # str -> float
label = str(100)  # int -> str
print(f"age   = {age!r}    type = {type(age)}")
print(f"price = {price!r}  type = {type(price)}")
print(f"label = {label!r}  type = {type(label)}")

print(type(age), type(price), type(label))
print(id(age))  # object's memory identity

# A common bug: converting a non-numeric string.
try:
    bad = int("25 years")  # ValueError: invalid literal for int()
except ValueError as error:
    print(f"[ERROR] {error}")
