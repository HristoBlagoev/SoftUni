age = float(input())
gender = input()
user_output = ''

if gender == 'm':
    if age >= 16:
        user_output = 'Mr.'
    else:
        user_output = 'Master'
if gender == 'f':
    if age >= 16:
        user_output = 'Ms.'
    else:
        user_output = 'Miss'

print(user_output)