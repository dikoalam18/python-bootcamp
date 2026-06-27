# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter price of Milk: "))  # Let the user enter a number
item_count_1 = int(input("Enter quantity: "))  # Let the user enter a number

print()
item_cost_2 = int(input("Enter price of Coffee: "))  # Let the user enter a number
item_count_2 = int(input("Enter quantity: "))  # Let the user enter a number

print()
item_cost_3 = int(input("Enter price of Creamier: "))  # Let the user enter a number
item_count_3 = int(input("Enter quantity: "))  # Let the user enter a number

# Calculate the total
print()
total = (item_cost_1 * item_count_1) + (item_cost_2 * item_count_2) + (item_cost_3 * item_count_3)
print(f"Total Price: {total}")



