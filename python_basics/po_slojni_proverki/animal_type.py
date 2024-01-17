animal = input()
user_output = ''

if animal == 'dog':
    user_output = 'mammal'
elif animal == 'snake' or animal == 'tortoise' or animal == 'crocodile':
    user_output = 'reptile'
else:
    user_output = 'unknown'

print(user_output)
