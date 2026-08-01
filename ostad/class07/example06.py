print("Menu -1.balance, 2. View A/C, 3. Deposit, 4. Withdraw, 5. Exit")


while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance: $1000")
    elif choice == 2:
        print("View A/C: Account details here")
    elif choice == 3:
        amount = float(input("Enter deposit amount: "))
        print(f"Deposited ${amount}")
    elif choice == 4:
        amount = float(input("Enter withdraw amount: "))
        print(f"Withdrew ${amount}")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")