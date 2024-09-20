first_string = input()
second_string = input()

current_string = list(first_string)

previous_string = first_string

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        current_string[i] = second_string[i]

        result = ''.join(current_string)

        if result != previous_string:
            print(result)
            previous_string = result

# 10.1
# first_string = input()
# second_string = input()
# last_printed_string = first_string
# for character_index in range(len(first_string)):
#     left_part = second_string[:character_index + 1]
#     right_part = first_string[character_index +1:]
#     new_string = left_part + right_part
#     if new_string != last_printed_string:
#         print(new_string)
#         last_printed_string = new_string