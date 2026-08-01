# if<outer condition true >: # Front Door Open
#   if <inner condition true>: # Bedroom Door Open
#        <runs only when both condition is true>
#     else: # Drawingroom door is Locked
#       <outer condition true, inner condition false>
# else: # Fron door is Locked
#   <outer condition false>


correct_pin = "1234"
account_balance = 5000.0

entered_pin = input("Enter your 4 digit PIN:")


if entered_pin == correct_pin:
    print("PIN Accepted!")

    amount = float(input("Enter Amount to Withdraw:"))

    if amount <= 0:
        print("Invalid amount. Please enter a positive number.")
    elif amount > account_balance:
        print("Insufficient balance.")
        print(f"Your Available balance is: {account_balance}")
    else:
        account_balance = account_balance - amount
        print(f"Please collect:{amount}")
        print(f"Remaining balance: {account_balance}")
else:
    print("Incorrect PIN, Card Blocked for safety.")
print("Thank you")
