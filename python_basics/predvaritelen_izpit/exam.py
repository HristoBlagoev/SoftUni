number_of_students = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0

total_grade = 0

for student in range(number_of_students):
    current_grade = float(input())
    total_grade += current_grade
    if 2.00 <= current_grade <= 2.99:
        p1_counter += 1
    elif 3.00 <= current_grade <= 3.99:
        p2_counter += 1
    elif 4.00 <= current_grade <= 4.99:
        p3_counter += 1
    elif current_grade >= 5.00:
        p4_counter += 1

average_grade = total_grade / number_of_students

p1_percentage = p1_counter / number_of_students * 100
p2_percentage = p2_counter / number_of_students * 100
p3_percentage = p3_counter / number_of_students * 100
p4_percentage = p4_counter / number_of_students * 100

print(f"Top students: {p4_percentage:.2f}%")
print(f"Between 4.00 and 4.99: {p3_percentage:.2f}%")
print(f"Between 3.00 and 3.99: {p2_percentage:.2f}%")
print(f"Fail: {p1_percentage:.2f}%")
print(f"Average: {average_grade:.2f}")