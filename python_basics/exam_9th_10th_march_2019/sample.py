first_player_name = input()
second_player_name = input()
first_player_points_counter = 0
second_player_points_counter = 0


is_number_wars = False

command = input()
while command != 'End of game':
    for i in range(1, 36 + 1):
        first_player_number = int(input())
        first_player_points_counter += first_player_number
    for i in range(1, 36 + 1):
        second_player_number = int(input())
        second_player_points_counter += second_player_number

difference = abs(first_player_points_counter - second_player_points_counter)

if first_player_number == second_player_number:
    break
if first_player_number > second_player_number:
    first_player_points_counter += difference
elif second_player_number > first_player_number:
    second_player_points_counter += difference
elif first_player_number == second_player_number:
    is_number_wars = True
    break


    command = input()