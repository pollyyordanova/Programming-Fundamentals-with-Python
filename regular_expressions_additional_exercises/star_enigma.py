import re


def decrypt_message(message):
    decryption_key = sum(1 for char in message if char.lower() in 'star')

    decrypted_message = ''.join(chr(ord(char) - decryption_key) for char in message)

    return decrypted_message


def extract_data(decrypted_message):
    pattern = r"@([A-Za-z]+):(\d+)!([AD])!->(\d+)"
    match = re.search(pattern, decrypted_message)

    if match:
        planet_name = match.group(1)
        population = int(match.group(2))
        attack_type = match.group(3)
        soldier_count = int(match.group(4))
        return planet_name, population, attack_type, soldier_count
    else:
        return None


def main():
    n = int(input())
    attacked_planets = []
    destroyed_planets = []

    for _ in range(n):
        encrypted_message = input()

        decrypted_message = decrypt_message(encrypted_message)

        extracted_data = extract_data(decrypted_message)

        if extracted_data:
            planet_name, population, attack_type, soldier_count = extracted_data

            if attack_type == 'A':
                attacked_planets.append(planet_name)
            elif attack_type == 'D':
                destroyed_planets.append(planet_name)

    attacked_planets = sorted(attacked_planets)
    destroyed_planets = sorted(destroyed_planets)

    print(f"Attacked planets: {len(attacked_planets)}")
    for planet in attacked_planets:
        print(f"-> {planet}")

    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planet in destroyed_planets:
        print(f"-> {planet}")


if __name__ == "__main__":
    main()
