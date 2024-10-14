def group_numbers(input_numbers):
    numbers = list(map(int, input_numbers.split(", ")))
    group_boundary = 10
    while numbers:
        current_group = [num for num in numbers if num <= group_boundary]
        numbers = [num for num in numbers if num > group_boundary]
        print(f"Group of {group_boundary}'s: {current_group}")
        group_boundary += 10

if __name__ == "__main__":
    input_numbers = input()
    group_numbers(input_numbers)
