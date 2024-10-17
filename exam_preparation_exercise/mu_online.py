dungeon_rooms = input().split('|')

health = 100
bitcoins = 0
room_counter = 0

for room in dungeon_rooms:
    room_counter += 1
    command, number = room.split()
    number = int(number)

    if command == "potion":
        healed_amount = min(100 - health, number)
        health += healed_amount
        print(f"You healed for {healed_amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_counter}")
            break
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
