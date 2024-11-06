products = {}

while True:
    command = input().strip()

    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name in products:
        existing_price, existing_quantity = products[name]
        products[name] = (price, existing_quantity + quantity)
    else:
        products[name] = (price, quantity)

for name, (price, quantity) in products.items():
    total_price = price * quantity
    print(f"{name} -> {total_price:.2f}")
