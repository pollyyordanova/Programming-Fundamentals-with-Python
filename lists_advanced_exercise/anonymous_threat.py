def merge_elements(data, start_index, end_index):
    start_index = max(0, start_index)
    end_index = min(len(data) - 1, end_index)
    merged_string = ''.join(data[start_index:end_index + 1])
    data = data[:start_index] + [merged_string] + data[end_index + 1:]
    return data

def divide_element(data, index, partitions):
    element = data[index]
    part_size = len(element) // partitions
    remainder = len(element) % partitions
    new_parts = []
    start = 0
    for i in range(partitions):
        extra = 1 if i < remainder else 0
        new_parts.append(element[start:start + part_size + extra])
        start += part_size + extra
    data = data[:index] + new_parts + data[index + 1:]
    return data

data = input().split()
command = input()

while command != "3:1":
    command_parts = command.split()
    action = command_parts[0]

    if action == "merge":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])
        data = merge_elements(data, start_index, end_index)

    elif action == "divide":
        index = int(command_parts[1])
        partitions = int(command_parts[2])
        data = divide_element(data, index, partitions)

    command = input()

print(' '.join(data))

