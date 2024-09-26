key = int(input())

number = int(input())

decrypted_message = ""

for _ in range(number):
    char = input()
    decrypted_char = chr(ord(char) + key)
    decrypted_message += decrypted_char

print(decrypted_message)
