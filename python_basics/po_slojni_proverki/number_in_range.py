number = int(input())
user_output = ''

if -100 <= number <= 100 and number != 0:
    user_output = 'Yes'
else:
    user_output = 'No'

print(user_output)