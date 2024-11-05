products = {}

command = input()

while command != "statistics":
    tokens = command.split(": ")
    product = tokens[0]
    quantity = int(tokens[1])

    if product not in products:
        products[product] = 0
    products[product] += quantity

    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")

total_products = len(products)
total_quantity = sum(products.values())

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")

