n = int(input())

students_grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")
