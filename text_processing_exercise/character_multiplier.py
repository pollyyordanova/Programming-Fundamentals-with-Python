def character_multiplier(str1, str2):
    total_sum = 0
    for i in range(min(len(str1), len(str2))):
        total_sum += ord(str1[i]) * ord(str2[i])
    if len(str1) > len(str2):
        total_sum += sum(ord(ch) for ch in str1[len(str2):])
    elif len(str2) > len(str1):
        total_sum += sum(ord(ch) for ch in str2[len(str1):])
    return total_sum

str1, str2 = input().split()
print(character_multiplier(str1, str2))
