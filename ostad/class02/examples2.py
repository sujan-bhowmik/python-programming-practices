# sep controls what goes BETWEEN the arguments (default is a single space).
print("2026", "06", "29", sep="-")  # looks like a date
print("user", "domain.com", sep="@")  # looks like an email

# end controls what is printed AFTER all arguments (default is a newline "\n").
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".")  # default end="\n" finishes the line

product_name = "Laptop"
price = 75500
quantity = 3
total = price * quantity

print(f"Total   : {total}")
# :,  -> add a thousands separator for large numbers
print(f"Total with separator    : {total:,}")
# :>10 -> right-align inside a width of 10 characters
print(f"Right aligned: |{product_name:>10}|")
