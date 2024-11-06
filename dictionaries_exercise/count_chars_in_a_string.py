characters = input()
characters = characters.replace(" ", "" )
occurrences = {}
for symbol in characters:
    if symbol not in occurrences.keys(): 
        occurrences[symbol] = 0
    occurrences[symbol] += 1
for symbol, occurrences in occurrences.items():
    print(f"{symbol} -> {occurrences}")