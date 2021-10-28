def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")
pin = input("Enter PIN: ")
balance = 0
print(str(name) + " has been registered starting balance of $" + str(balance))

print("          === Automated Teller Machine ===          ")
print("LOGIN")
name_to_validate = name
pin_to_validate = pin
while True:
    user = input("Enter name: ")
    password = input("Enter password: ")

    if(name_to_validate == name_to_validate == name and pin_to_validate == pin):
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

# SECOND WHILE LOOP
while True:
    atm_menu(user)
    print(balance)
    option = input("Choose an option: ")