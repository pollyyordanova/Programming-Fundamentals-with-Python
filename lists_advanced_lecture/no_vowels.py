text = input()

vowels = 'aeiouAEIOU'

result = ''.join([char for char in text if char not in vowels])

print(result)
