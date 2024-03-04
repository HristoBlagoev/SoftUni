number_of_students = int(input())
students = {}

for _ in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = []

    students[name].append(grade)

students_above_average = {name: sum(grades) / len(grades) for name, grades in students.items()
                          if sum(grades) / len(grades) >= 4.50}

for name, average_grades in students_above_average.items():
    print(f"{name} -> {average_grades:.2f}")