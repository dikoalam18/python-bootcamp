orders = {}

order = input("Enter order: ")
while order:
    count = int(input("Enter how many: "))

    if order in orders:
        count =+ count
        orders[order] = count
    else:
        orders[order] = count


    order = input("Enter order: ")

    # TODO: Record the person’s order
     # TODO: If the order already exist, just add the count


print(orders)
