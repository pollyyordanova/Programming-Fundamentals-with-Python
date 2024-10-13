def battle_ships():
    n = int(input())  
    field = []

    # Read the field
    for _ in range(n):
        row = list(map(int, input().split()))
        field.append(row)

    attacks = input().split()

    destroyed_ships = 0

    for attack in attacks:
        row, col = map(int, attack.split('-'))
        if 0 <= row < n and 0 <= col < len(field[row]):
            if field[row][col] > 0:
                field[row][col] -= 1
                if field[row][col] == 0:
                    destroyed_ships += 1

    print(destroyed_ships)

if __name__ == "__main__":
    battle_ships()
