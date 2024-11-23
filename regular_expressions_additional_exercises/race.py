import re

participants = input().split(", ")
race_data = input()

distance_dict = {name: 0 for name in participants}

name_pattern = re.compile(r"[A-Za-z]+")
distance_pattern = re.compile(r"\d")

while race_data != "end of race":
    name_match = "".join(name_pattern.findall(race_data))
    distance_match = sum(int(digit) for digit in distance_pattern.findall(race_data))

    if name_match in distance_dict:
        distance_dict[name_match] += distance_match

    race_data = input()

sorted_participants = sorted(distance_dict.items(), key=lambda x: x[1], reverse=True)

for i in range(min(3, len(sorted_participants))):
    position = i + 1
    name, distance = sorted_participants[i]
    print(f"{position}st place: {name}" if i == 0 else f"{position}nd place: {name}" if i == 1 else f"{position}rd place: {name}")
