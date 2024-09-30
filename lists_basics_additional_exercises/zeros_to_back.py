numbers_string_list = input().split(", ")
for num in numbers_string_list:
    if num == "0":
        numbers_string_list.remove(num)
        numbers_string_list.append(num[-1])
numbers_as_integers = [int(num) for num in numbers_string_list]
print(numbers_as_integers)