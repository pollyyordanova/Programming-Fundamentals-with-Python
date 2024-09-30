sequence_list = input().split()
string = input()
message = []

for number_str in sequence_list:
    sum_letters_int = sum(int(digit) for digit in number_str)

    while sum_letters_int >= len(string):
        sum_letters_int -= len(string)

    char_index = sum_letters_int

    if 0 <= char_index < len(string):
        message.append(string[char_index])
        string = string[:char_index] + string[char_index + 1:]

print(''.join(message))