from logging import currentframe


def spend(expenses):
    """TODO: Add a new cost in expenses"""
    a = int(input("Enter expense: "))
    expenses.append(a)

def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    expenses.pop(-1)

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(expenses)
    print(f"Total: {sum(expenses)}")

def main():
    running = True
    current_expenses = []

    while running:
        command = input("\nCommand: ")
        if command == "spend":
            spend(current_expenses)
        if command == "refund":
            refund(current_expenses)
        if command == "show":
            show(current_expenses)
        if command == "exit":
            print("bye!")
            break

main()
