def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

n =  int(input())

for num in range(1, n + 1):
    digit_sum = sum_of_digits(num)

    is_special = digit_sum == 5 or digit_sum == 7 or digit_sum == 11

    print(f"{num} -> {is_special}")
