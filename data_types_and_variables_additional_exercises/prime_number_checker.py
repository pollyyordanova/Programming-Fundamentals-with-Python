number = int(input())

if number <= 1:
    print(False)
else:
    is_prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

    print(is_prime)