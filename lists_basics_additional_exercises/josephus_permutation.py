people_in_circle = list(map(int, input().split()))
k = int(input())

output = []
current_index = 0

while people_in_circle:
    current_execution = (current_index + k - 1) % len(people_in_circle)
    executed_person = people_in_circle.pop(current_execution)
    output.append(str(executed_person))
    current_index = current_execution

print("[" + ",".join(output) + "]")