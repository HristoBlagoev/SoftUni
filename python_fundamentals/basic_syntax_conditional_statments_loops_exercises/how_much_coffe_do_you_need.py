command = input()
needed_coffee = 0


while command != 'END':
    if command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        needed_coffee += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        needed_coffee += 2
    command = input()

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(needed_coffee)
