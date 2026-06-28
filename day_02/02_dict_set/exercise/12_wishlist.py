# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "CPU",
    "Brand": "Lenovo",
    "OS": "Windows",
    "RAM": "16 GB",
    "CORE": "4 core"
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
print()
print("Order: ")
for x, y in order.items():
    print(f"\t{x}: {y}")
