pirate_ship = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break

    command_parts = command.split()

    if command_parts[0] == "Fire":
        index = int(command_parts[1])
        damage = int(command_parts[2])

        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()

    elif command_parts[0] == "Defend":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        damage = int(command_parts[3])

        if 0 <= start_index <= end_index < len(pirate_ship):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()

    elif command_parts[0] == "Repair":
        index = int(command_parts[1])
        health = int(command_parts[2])

        if 0 <= index < len(pirate_ship):
            pirate_ship[index] = min(pirate_ship[index] + health, max_health)

    elif command_parts[0] == "Status":
        repair_needed_count = sum(1 for section in pirate_ship if section < 0.2 * max_health)
        print(f"{repair_needed_count} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")

