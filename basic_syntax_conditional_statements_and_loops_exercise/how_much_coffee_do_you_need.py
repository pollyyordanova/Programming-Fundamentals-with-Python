coffee_count = 0

while True:
    event = input()
    if event == "END":
        break

    if event.lower() in ["coding", "dog", "cat", "movie"]:
        if event.islower():
            coffee_count += 1
        else:
            coffee_count += 2

    if coffee_count > 5:
        print("You need extra sleep")
        break

if coffee_count <= 5:
    print(coffee_count)