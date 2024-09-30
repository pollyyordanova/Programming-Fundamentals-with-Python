sequence_numbers = input().split()

left_car_time = 0
right_car_time = 0

middle_ground = len(sequence_numbers) // 2

left_car_ground = sequence_numbers[:middle_ground]

right_car_ground = sequence_numbers[1 + middle_ground:]

for time_l in left_car_ground:
    time_int = int(time_l)
    left_car_time += time_int
    if time_l == '0':
        left_car_time *= 0.80
    else:
        right_car_time *= 1.00

for time_r in right_car_ground[::-1]:
    time_int = int(time_r)
    right_car_time += time_int
    if time_r == '0':
        right_car_time *= 0.80
    else:
        right_car_time *= 1.00

if left_car_time > right_car_time:
    print(f"The winner is right with total time: {right_car_time:.1f}")
else:
    print(f"The winner is left with total time: {left_car_time:.1f}")