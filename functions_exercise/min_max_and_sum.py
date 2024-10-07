numbers = input()

num_list = [int(num) for num in numbers.split()]

min_num = min(num_list)
max_num = max(num_list)
sum_num = sum(num_list)

print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_num}")
