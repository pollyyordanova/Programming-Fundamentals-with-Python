import re

input_data = input()

pattern = r"([^\d]+)(\d+)"
matches = re.findall(pattern, input_data)

rage_message = ""

for string, repeat_count in matches:
    rage_message += string.upper() * int(repeat_count)

unique_symbols = len(set(rage_message))

print(f"Unique symbols used: {unique_symbols}")
print(rage_message)
