stock_data = input().split(" ")

stock = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = int(stock_data[i + 1])
    stock[product] = quantity

searched_products = input().split(" ")

for product in searched_products:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
