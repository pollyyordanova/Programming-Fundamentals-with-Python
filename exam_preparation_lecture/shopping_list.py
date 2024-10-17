groceries = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    command_parts = command.split()

    if command_parts[0] == "Urgent":
        item = command_parts[1]
        if item not in groceries:
            groceries.insert(0, item)

    elif command_parts[0] == "Unnecessary":
        item = command_parts[1]
        if item in groceries:
            groceries.remove(item)

    elif command_parts[0] == "Correct":
        old_item = command_parts[1]
        new_item = command_parts[2]
        if old_item in groceries:
            index = groceries.index(old_item)
            groceries[index] = new_item

    elif command_parts[0] == "Rearrange":
        item = command_parts[1]
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))
