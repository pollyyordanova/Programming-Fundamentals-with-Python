budget = float(input())
flour_price = float(input())

egg_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price_per_250ml = milk_price_per_liter * 0.250

loaves = 0
colored_eggs = 0

cost_per_loaf = flour_price + egg_price + milk_price_per_250ml

while budget >= cost_per_loaf:
    budget -= cost_per_loaf
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)
        if colored_eggs < 0:
            colored_eggs = 0

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")