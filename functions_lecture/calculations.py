def calculate(operator, first_number, second_number):
    result = None
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = int(first_number / second_number)
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    return result

operator = input()
first_number = int(input())
second_number = int(input())

result = calculate(operator, first_number, second_number)
print(result)