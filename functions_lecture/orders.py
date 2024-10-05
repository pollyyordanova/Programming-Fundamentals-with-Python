def calculate_total_price(product, quantity):
    prices = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }

    total_price = prices.get(product, 0) * quantity

    return f"{total_price:.2f}"


product = input()
quantity = int(input())
print(calculate_total_price(product, quantity))