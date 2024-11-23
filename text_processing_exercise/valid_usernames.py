def is_valid_username(username):
    if 3 <= len(username) <= 16 and username.replace("-", "").replace("_", "").isalnum():
        return True
    return False

usernames = input().split(", ")

for username in usernames:
    if is_valid_username(username):
        print(username)
