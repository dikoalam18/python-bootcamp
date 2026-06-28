# TODO: Fill in the details of the items you plan to buy
orders = [
    {
        "Name": "CPU",
        "Brand": "Lenovo",
        "OS": "Windows",
        "RAM": "16 GB",
        "CORE": "4 core"
    },
    {
        "Name": "Laptop",
        "Brand": "ASUS",
        "OS": "Linux",
        "RAM": "32 GB",
        "CORE": "8 core"
    }
]

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
print()
print("Items: ")
for a in orders:
    print()
    for x, y in a.items():
        print(f"\t{x}: {y}")

