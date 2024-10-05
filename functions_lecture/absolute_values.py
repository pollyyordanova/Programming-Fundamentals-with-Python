def get_absolute_values(numbers):
    numbers_list = [float(num) for num in numbers.split()]

    return [abs(num) for num in numbers_list]


numbers = input()

absolute_values = get_absolute_values(numbers)
print(absolute_values)