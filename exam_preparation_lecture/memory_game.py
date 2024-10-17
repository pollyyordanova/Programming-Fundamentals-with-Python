def memory_game():
    elements = input().split()
    moves = 0

    while True:
        command = input()

        if command == "end":
            print(f"Sorry you lose :(\n{' '.join(elements)}")
            break

        indexes = command.split()
        index1 = int(indexes[0])
        index2 = int(indexes[1])
        moves += 1

        if index1 == index2 or not (0 <= index1 < len(elements)) or not (0 <= index2 < len(elements)):
            mid_index = len(elements) // 2
            elements.insert(mid_index, f"-{moves}a")
            elements.insert(mid_index, f"-{moves}a")
            print("Invalid input! Adding additional elements to the board")
            continue

        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            first = elements.pop(max(index1, index2))
            elements.pop(min(index1, index2))
        else:
            print("Try again!")

        if not elements:
            print(f"You have won in {moves} turns!")
            break


memory_game()
