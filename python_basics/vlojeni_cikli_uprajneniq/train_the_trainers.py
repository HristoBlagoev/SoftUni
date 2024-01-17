number_of_jury = int(input())
final_grade = 0
number_of_presentations = 0

command = input()
while command != 'Finish':
    current_presentation_name = command
    current_presentation_grades = 0
    for presentation_grade in range(number_of_jury):
        current_grade = float(input())
        current_presentation_grades += current_grade
    current_presentation_average_grade = current_presentation_grades / number_of_jury
    final_grade += current_presentation_average_grade
    number_of_presentations += 1
    print(f"{current_presentation_name} - {current_presentation_average_grade:.2f}.")
    command = input()
final_average_grade = final_grade / number_of_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")
