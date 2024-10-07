def multiplication_sign(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"

    negative_count = sum(1 for num in (a, b, c) if num < 0)

    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"


a = int(input())
b = int(input())
c = int(input())

result = multiplication_sign(a, b, c)
print(result)
