a = int(input())
b = int(input())

print("Before:")
print(f"a = {a}")
print(f"b = {b}")

temporary_variable = a
a = b
b = temporary_variable

print("After:")
print(f"a = {a}")
print(f"b = {b}")