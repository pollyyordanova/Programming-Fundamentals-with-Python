wagons_count = int(input())

train = [0] * wagons_count

while True:
    command = input()

    if command == "End":
        break

    parts = command.split()

    if parts[0] == "add":
        people = int(parts[1])
        train[-1] += people

    elif parts[0] == "insert":
        index = int(parts[1])
        people = int(parts[2])
        train[index] += people

    elif parts[0] == "leave":
        index = int(parts[1])
        people = int(parts[2])
        train[index] -= people

print(train)