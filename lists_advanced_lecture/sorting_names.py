names_input = input()

names = names_input.split(", ")

sorted_names = sorted(names, key=lambda x: (-len(x), x))

print(sorted_names)