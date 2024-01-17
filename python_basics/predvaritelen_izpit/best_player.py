from sys import maxsize

max_goals = -maxsize
best_player = ''

player_name = input()
while player_name != 'END':
    number_of_goals = int(input())
    if number_of_goals > max_goals:
        max_goals = number_of_goals
        best_player = player_name
        if max_goals >= 10:
            break

    player_name = input()

print(f"{best_player} is the best player!")

if max_goals >= 3:
    print(f"He has scored {number_of_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {number_of_goals} goals.")