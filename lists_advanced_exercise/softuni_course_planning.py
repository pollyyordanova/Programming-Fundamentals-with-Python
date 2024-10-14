def add_lesson(schedule, lesson_title):
    if lesson_title not in schedule:
        schedule.append(lesson_title)


def insert_lesson(schedule, lesson_title, index):
    if lesson_title not in schedule:
        schedule.insert(index, lesson_title)


def remove_lesson(schedule, lesson_title):
    if lesson_title in schedule:
        lesson_index = schedule.index(lesson_title)
        schedule.pop(lesson_index)
        exercise = f"{lesson_title}-Exercise"
        if exercise in schedule:
            schedule.remove(exercise)


def swap_lessons(schedule, lesson_title1, lesson_title2):
    if lesson_title1 in schedule and lesson_title2 in schedule:
        index1, index2 = schedule.index(lesson_title1), schedule.index(lesson_title2)
        schedule[index1], schedule[index2] = schedule[index2], schedule[index1]
        exercise1, exercise2 = f"{lesson_title1}-Exercise", f"{lesson_title2}-Exercise"
        if exercise1 in schedule:
            schedule.remove(exercise1)
            schedule.insert(schedule.index(lesson_title1) + 1, exercise1)
        if exercise2 in schedule:
            schedule.remove(exercise2)
            schedule.insert(schedule.index(lesson_title2) + 1, exercise2)


def add_exercise(schedule, lesson_title):
    exercise = f"{lesson_title}-Exercise"
    if lesson_title in schedule and exercise not in schedule:
        lesson_index = schedule.index(lesson_title)
        schedule.insert(lesson_index + 1, exercise)
    elif lesson_title not in schedule:
        schedule.append(lesson_title)
        schedule.append(exercise)

schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    command_parts = command.split(":")
    action = command_parts[0]

    if action == "Add":
        add_lesson(schedule, command_parts[1])
    elif action == "Insert":
        insert_lesson(schedule, command_parts[1], int(command_parts[2]))
    elif action == "Remove":
        remove_lesson(schedule, command_parts[1])
    elif action == "Swap":
        swap_lessons(schedule, command_parts[1], command_parts[2])
    elif action == "Exercise":
        add_exercise(schedule, command_parts[1])

for index, lesson in enumerate(schedule):
    print(f"{index + 1}.{lesson}")
