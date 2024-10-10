numbers_input = input()

numbers = list(map(int, numbers_input.split(", ")))

even_indices = [index for index, number in enumerate(numbers) if number % 2 == 0]

print(even_indices)