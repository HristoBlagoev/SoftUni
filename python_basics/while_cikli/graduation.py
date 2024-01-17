name_of_student = input()
grade_counter = 0
classes_counter = 0
failed_classes_counter = 0


while True:
    current_class_grade = float(input())

    if current_class_grade < 4.00:
        failed_classes_counter += 1
        if failed_classes_counter > 1:
            print(f"{name_of_student} has been excluded at {classes_counter + 1} grade")
            break
        continue

    classes_counter += 1
    grade_counter += current_class_grade

    if classes_counter == 12:
        average_grade = f'{grade_counter / 12:.2f}'
        print(f'{name_of_student} graduated. Average grade: {average_grade}')
        break
