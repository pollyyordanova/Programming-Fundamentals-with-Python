current_string = input()
counter = int(input())

repeat_string = lambda a,b: a * b

result = repeat_string(current_string, counter)
print(result)