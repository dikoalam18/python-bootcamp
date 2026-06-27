# Price notification template
price_notification = "The price of {} is ${}."

# TODO: Post: Latte ($3.5)
product =  str("Latte")
price =  float(3.5)
new = price_notification.format(product, price)
print()
print(new)

# TODO: Post: Espresso ($2.75)
product =  str("Espresso")
price =  float(2.75)
new = price_notification.format(product, price)
print()
print(new)


# TODO: Post: Cappuccino ($4.0)
product =  str("Cappuccino")
price =  float(4.0)
new = price_notification.format(product, price)
print()
print(new)
