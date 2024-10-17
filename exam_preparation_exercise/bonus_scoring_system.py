import math

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
max_attendance = 0

for _ in range(students_count):
    attendances = int(input())
    if lectures_count > 0:
        total_bonus = attendances / lectures_count * (5 + additional_bonus)
    else:
        total_bonus = 0

    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_attendance = attendances

max_bonus_rounded = math.ceil(max_bonus)

print(f"Max Bonus: {max_bonus_rounded}.")
print(f"The student has attended {max_attendance} lectures.")
