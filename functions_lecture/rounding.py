def round_numbers(numbers):
    rounded_list = [round(float(num)) for num in numbers.split()]
    return rounded_list

numbers = input()

result = round_numbers(numbers)
print(result)