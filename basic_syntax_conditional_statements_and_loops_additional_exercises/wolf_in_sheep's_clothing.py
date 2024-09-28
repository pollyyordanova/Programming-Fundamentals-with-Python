animals = input().split(", ")

wolf_position = animals.index("wolf")

if wolf_position == len(animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    sheep_number = len(animals) - wolf_position - 1
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")