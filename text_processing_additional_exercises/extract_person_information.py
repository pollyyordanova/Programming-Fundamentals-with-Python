n = int(input())

for _ in range(n):
    line = input()
    name_start = line.index("@") + 1
    name_end = line.index("|")
    name = line[name_start:name_end]

    age_start = line.index("#") + 1
    age_end = line.index("*")
    age = line[age_start:age_end]

    print(f"{name} is {age} years old.")
