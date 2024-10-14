sequence = list(map(int, input().split()))
sum_removed = 0

while sequence:
    index = int(input())

    if index < 0:
        removed_element = sequence[0]
        sequence[0] = sequence[-1]
    elif index >= len(sequence):
        removed_element = sequence[-1]
        sequence[-1] = sequence[0]
    else:
        removed_element = sequence.pop(index)

    sum_removed += removed_element

    for i in range(len(sequence)):
        if sequence[i] <= removed_element:
            sequence[i] += removed_element
        else:
            sequence[i] -= removed_element

print(sum_removed)
