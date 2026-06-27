total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":
        # TODO: Ask for number
        number = int(input("Enter number: "))
        # TODO: Add that number to the total
        total = total + number
        # TODO: Print the current total
        print(f"Total is {total}")
        pass

    if command == "sub":
        # TODO: Ask for number
        number = int(input("Enter number: "))
        # TODO: Add that number to the total
        total = total - number
        # TODO: Print the current total
        print(f"Total is {total}")
        pass

    elif command == "exit":
        print("\nbye!")
        running = False
