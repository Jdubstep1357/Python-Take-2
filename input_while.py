while True: 
    print("1. Number One")
    print("2. Number 2")
    print("3. Number 3")
    # variable option is linked to the input choice
    option = input("Pick an option: ")
    if option == "1":
        print("You choose 1")
    elif option == "2":
        print("You choose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop.")