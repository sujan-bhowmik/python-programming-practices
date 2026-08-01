attempts_left = 3
while attempts_left > 0:
    password = input("Enter your password: ")
    if password == "ostad":
        print("Access granted")
        break
    else:
        attempts_left -= 1
        print(f"Incorrect password. You have {attempts_left} attempts left.")
else:
    print("Too many incorrect attempts. Access denied.")