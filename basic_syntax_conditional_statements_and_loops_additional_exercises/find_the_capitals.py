input_string = input()

capital_indices = [index for index, char in enumerate(input_string) if char.isupper()]

print(capital_indices)