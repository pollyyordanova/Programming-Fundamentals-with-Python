import re

def calculate_health(demon_name):
    return sum(ord(c) for c in demon_name if c.isalpha())


def calculate_damage(demon_name):
    numbers = re.findall(r'[+-]?\d+(\.\d+)?', demon_name)
    damage = sum(float(num) for num in numbers)

    for _ in range(demon_name.count('*')):
        damage *= 2
    for _ in range(demon_name.count('/')):
        damage /= 2

    return damage


def main():
    demons_input = input().strip()
    demons = [demon.strip() for demon in demons_input.split(',')]

    demon_data = []

    for demon in demons:
        health = calculate_health(demon)
        damage = calculate_damage(demon)
        demon_data.append((demon, health, damage))

    demon_data.sort(key=lambda x: x[0])

    for demon, health, damage in demon_data:
        print(f"{demon} - {health} health, {damage:.2f} damage")


if __name__ == "__main__":
    main()
