gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    command_parts = command.split()
    action = command_parts[0]

    if action == "OutOfStock":
        gift = command_parts[1]
        gifts = ["None" if x == gift else x for x in gifts]
    elif action == "Required":
        gift = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif action == "JustInCase":
        gift = command_parts[1]
        gifts[-1] = gift

print(" ".join(gift for gift in gifts if gift != "None"))