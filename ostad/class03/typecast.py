item_name = input("Enter the name of the item: ")
price = float(
    input("Enter the price of the item: ")
)  # type conversion from stringto float
quantity = int(
    input("Enter the quantity of the item: ")
)  # type conversion from string to integer
total = price * quantity  # calculate total cost


print("\n------ Grocery Bill -------")
print(f"Item: {item_name}")
print(f"Price: ${price:.3f}")  # formatting the price to 2 decimal places
print(f"Quantity: {quantity}")
print(f"Total cost for {item_name}: ${total:.2f}")
