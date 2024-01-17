maximum_bad_grades = int(input())
average_score = 0
total_problems_solved = 0
last_problem = ""
got_too_many_bad_grades = False
bad_grades_counter = 0

current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == maximum_bad_grades:
            got_too_many_bad_grades = True
            break
    average_score += current_grade
    total_problems_solved += 1
    last_problem = current_problem
    current_problem = input()

if got_too_many_bad_grades:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    average_score /= total_problems_solved
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {total_problems_solved}")
    print(f"Last problem: {last_problem}")
