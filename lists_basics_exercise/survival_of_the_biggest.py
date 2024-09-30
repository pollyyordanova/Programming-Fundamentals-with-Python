numbers_input = input()
n = int(input())

numbers = list(map(int, numbers_input.split()))

for _ in range(n):
    numbers.remove(min(numbers))

print(", ".join(map(str, numbers)))