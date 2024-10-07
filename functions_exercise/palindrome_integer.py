def is_palindrome(num):
    return str(num) == str(num)[::-1]


def check_palindromes(numbers):
    num_list = [int(num) for num in numbers.split(', ')]

    for num in num_list:
        print(is_palindrome(num))


numbers = input()

check_palindromes(numbers)
