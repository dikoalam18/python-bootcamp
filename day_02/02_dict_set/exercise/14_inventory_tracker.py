def add(inventory):
    """TODO:
        Ask for item name, info, and stock
        Create a dictionary with key: name, info, stock
        Add that dictionary to inventory
    """
    a = input("Enter Item: ")
    b = int(input("Enter SN: "))
    c = float(input("Enter QTY: "))
    item = {
        "name": a,
        "info": b,
        "stock": c
    }
    inventory.append(item)
    #print(inventory)

def remove(inventory):
    """TODO:
        Ask for item index (int)
        Remove item in that index in inventory
    """
    index = int(input("Index: "))
    try:
        inventory.pop(index)
    except:
        print("Index not found")
        pass

def read(inventory):
    """TODO:
        Ask for item index (int)
                Show item in that index in inventory
    """
    index = int(input("Index: "))
    try:
        print(inventory[index])
    except:
        print("Index not found")
        pass

def show(inventory):
    """TODO: Print items line-by-line"""
    print("Items: ")
    for a in inventory:
        print()
        for x, y in a.items():
            print(f"\t{x}: {y}")

def main():
    """Created to test functions"""
    running = True
    item_detail = str | int | float
    inventory: list[dict[str, item_detail]] = []

    while running:
        command = input("Command: ")
        if command == "add":
            # TODO: Use add command"""
            add(inventory)
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            remove(inventory)
            pass
        elif command == "read":
            # TODO: Use read command"""
            read(inventory)
            pass
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)
            pass
        elif command == "exit":
            running = False


main()
