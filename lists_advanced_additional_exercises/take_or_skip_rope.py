def extract_hidden_message(input_string):
    numbers = []
    non_numbers = []

    for char in input_string:
        if char.isdigit():
            numbers.append(int(char))
        else:
            non_numbers.append(char)

    take_list = [numbers[i] for i in range(0, len(numbers), 2)]
    skip_list = [numbers[i] for i in range(1, len(numbers), 2)]

    result = []
    index = 0

    for take, skip in zip(take_list, skip_list):
        result.extend(non_numbers[index:index+take])

        index += take + skip

    return ''.join(result)

input_string = input()
hidden_message = extract_hidden_message(input_string)
print(hidden_message)