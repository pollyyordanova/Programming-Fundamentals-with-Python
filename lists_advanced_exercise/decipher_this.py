def decipher_word(word):
    ascii_code = ""
    for char in word:
        if char.isdigit():
            ascii_code += char
        else:
            break

    first_letter = chr(int(ascii_code))

    rest_of_word = word[len(ascii_code):]

    if len(rest_of_word) > 1:
        rest_of_word = rest_of_word[-1] + rest_of_word[1:-1] + rest_of_word[0]

    return first_letter + rest_of_word


def decipher_message(message):
    words = message.split()

    deciphered_words = [decipher_word(word) for word in words]

    return " ".join(deciphered_words)

if __name__ == "__main__":
    message = input()
    print(decipher_message(message))

