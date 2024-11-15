key = list(map(int, input().split()))

while True:
    line = input()
    if line == "find":
        break

    decrypted_message = ""
    key_index = 0
    for char in line:
        decrypted_message += chr(ord(char) - key[key_index])
        key_index = (key_index + 1) % len(key)

    treasure_type_start = decrypted_message.index("&") + 1
    treasure_type_end = decrypted_message.index("&", treasure_type_start)
    treasure_type = decrypted_message[treasure_type_start:treasure_type_end]

    coordinates_start = decrypted_message.index("<") + 1
    coordinates_end = decrypted_message.index(">")
    coordinates = decrypted_message[coordinates_start:coordinates_end]

    print(f"Found {treasure_type} at {coordinates}")
