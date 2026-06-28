prices = [10_000, 20, 3_000, 3, -200, 1_000]
print()
print(f"Current: {prices}")

# TODO: Print the first, third, and last item
indices = [0, 2, -1]
print()
for index in indices:
    print(f"Current Price on {[index]}: {prices[index]}")

# TODO: Change the first, third, and last values to half the price
indices = [0, 2, -1]
for x in indices:
    prices[x] = prices[x] // 2

print()
print(f"New: {prices}")

# TODO: Print the first, third, and last item again to see new price
indices = [0, 2, -1]
print()
for index in indices:
    print(f"New Price on {[index]}: {prices[index]}")
