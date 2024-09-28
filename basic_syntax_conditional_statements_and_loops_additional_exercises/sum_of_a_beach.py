input_string = input()
input_string = input_string.lower()

words = ["sand", "water", "fish", "sun"]

count = 0
for word in words:
    count += input_string.count(word)
print(count)