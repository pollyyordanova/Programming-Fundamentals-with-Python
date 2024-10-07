import math

def factorial_division(num1, num2):
    factorial_num1 = math.factorial(num1)
    factorial_num2 = math.factorial(num2)

    result = factorial_num1 / factorial_num2

    print(f"{result:.2f}")


num1 = int(input())
num2 = int(input())

factorial_division(num1, num2)
