def get_letter_position(letter):
    return ord(letter.lower()) - ord('a') + 1

def process_string(s):
    first_letter = s[0]
    last_letter = s[-1]
    number = int(s[1:-1])

    if first_letter.isupper():
        number /= get_letter_position(first_letter)
    else:
        number *= get_letter_position(first_letter)

    if last_letter.isupper():
        number -= get_letter_position(last_letter)
    else:
        number += get_letter_position(last_letter)

    return number

input_data = input().split()
total_sum = sum(process_string(s) for s in input_data)

print(f"{total_sum:.2f}")
