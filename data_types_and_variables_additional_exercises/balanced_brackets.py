number = int(input())
is_balanced = True
last_open_bracket = False

for _ in range(number):
    line = input().strip()

    if line == "(":
        if last_open_bracket:
            is_balanced = False
            break
        last_open_bracket = True
    elif line == ")":
        if not last_open_bracket:
            is_balanced = False
            break
        last_open_bracket = False

if is_balanced and not last_open_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")
