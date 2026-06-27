# TODO: Ask the user how many items will be calculated
input_count = int(input("How many item?: "))
total = 0
packs = 0
x = 1

# TODO: Use a for loop to ask for more than one cost and count
for item in range(input_count):
    print()
    item_cost = int(input(f"ITEM{x}: How much?: "))  # Let the user enter a number
    item_packs = int(input(f"ITEM{x}: How many?: "))
    item_costs = item_cost * item_packs
    total += item_costs
    packs += item_packs
    x += 1

print()
print(f"Total item/s: {packs}")
print(f"Total Amount: {total}")
