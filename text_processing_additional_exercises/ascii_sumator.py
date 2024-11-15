char1 = input()
char2 = input()
random_string = input()

ascii_start = min(ord(char1), ord(char2))
ascii_end = max(ord(char1), ord(char2))

ascii_sum = sum(ord(char) for char in random_string if ascii_start < ord(char) < ascii_end)

print(ascii_sum)
