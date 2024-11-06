phohebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name , phone_number = entry.split("-")
    phohebook[name] = phone_number
searches = int(entry)
for current_search in range(searches):
    searched_name = input()
    if searched_name in phohebook.keys():
        print(f"{searched_name} -> {phohebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")